"""Pattern matching tracer for a readable step-by-step simulation of PEP 634 rules.

This module provides a small pattern DSL (Pattern subclasses) and a
`match_with_trace(subject, pattern)` function that returns (success, env, trace).

It is intended for teaching and debugging; it does not hook into Python's
native pattern syntax, but mirrors its semantics so you can trace matches
against your `Atom`/`Functor` and `logic.formulas` AST nodes.
"""
from dataclasses import dataclass
from typing import Any, Dict, List, Tuple


# --- Pattern classes -------------------------------------------------
@dataclass(frozen=True)
class PWildcard:
    def __repr__(self):
        return "_"


@dataclass(frozen=True)
class PLiteral:
    value: Any

    def __repr__(self):
        return f"{self.value!r}"


@dataclass(frozen=True)
class PName:
    name: str

    def __repr__(self):
        return self.name


@dataclass(frozen=True)
class PTuple:
    patterns: Tuple[Any, ...]

    def __repr__(self):
        return f"({', '.join(map(repr, self.patterns))})"


@dataclass(frozen=True)
class POr:
    left: Any
    right: Any

    def __repr__(self):
        return f"({self.left!r} | {self.right!r})"


@dataclass(frozen=True)
class PAs:
    pat: Any
    name: str

    def __repr__(self):
        return f"({self.pat!r} as {self.name})"


@dataclass(frozen=True)
class PGuard:
    pat: Any
    guard_fn: Any

    def __repr__(self):
        return f"({self.pat!r} if <guard>)"


@dataclass(frozen=True)
class PClass:
    cls: type
    patterns: Tuple[Any, ...]

    def __repr__(self):
        return f"{self.cls.__name__}({', '.join(map(repr, self.patterns))})"


# --- Matching engine -------------------------------------------------
class MatchFailure(Exception):
    pass


def merge_envs(envs: List[Dict[str, Any]]) -> Dict[str, Any]:
    out = {}
    for e in envs:
        for k, v in e.items():
            if k in out:
                raise MatchFailure(f"conflicting binding for {k}")
            out[k] = v
    return out


def match_with_trace(subject: Any, pattern: Any) -> Tuple[bool, Dict[str, Any], List[str]]:
    trace: List[str] = []

    def rec(s, p, depth=0) -> Dict[str, Any]:
        indent = "  " * depth
        trace.append(f"{indent}TRY match({s!r}, {p!r})")

        # Wildcard
        if isinstance(p, PWildcard):
            trace.append(f"{indent}=> wildcard matches, env={{}}")
            return {}

        # Literal
        if isinstance(p, PLiteral):
            if s == p.value:
                trace.append(f"{indent}=> literal {p.value!r} matches")
                return {}
            trace.append(f"{indent}X literal {p.value!r} does not match {s!r}")
            raise MatchFailure()

        # Name / capture
        if isinstance(p, PName):
            trace.append(f"{indent}=> capture {p.name} -> {s!r}")
            return {p.name: s}

        # Tuple / sequence
        if isinstance(p, PTuple):
            if not hasattr(s, "__len__"):
                trace.append(f"{indent}X subject not a sequence: {s!r}")
                raise MatchFailure()
            if len(s) != len(p.patterns):
                trace.append(f"{indent}X length mismatch: {len(s)} vs {len(p.patterns)}")
                raise MatchFailure()
            envs = []
            for i, subp in enumerate(p.patterns):
                envs.append(rec(s[i], subp, depth + 1))
            merged = merge_envs(envs)
            trace.append(f"{indent}=> tuple matched, env={merged}")
            return merged

        # Or pattern
        if isinstance(p, POr):
            try:
                return rec(s, p.left, depth + 1)
            except MatchFailure:
                return rec(s, p.right, depth + 1)

        # As pattern
        if isinstance(p, PAs):
            env = rec(s, p.pat, depth + 1)
            if p.name in env:
                trace.append(f"{indent}X as-pattern: name conflict {p.name}")
                raise MatchFailure()
            env[p.name] = s
            trace.append(f"{indent}=> as-pattern binds {p.name} -> {s!r}")
            return env

        # Guarded pattern
        if isinstance(p, PGuard):
            env = rec(s, p.pat, depth + 1)
            ok = p.guard_fn(env)
            trace.append(f"{indent}=> guard -> {ok}")
            if ok:
                return env
            raise MatchFailure()

        # Class pattern
        if isinstance(p, PClass):
            if not isinstance(s, p.cls):
                trace.append(f"{indent}X instanceof check failed: {s!r} is not {p.cls.__name__}")
                raise MatchFailure()
            # follow __match_args__ order if present
            names = getattr(p.cls, "__match_args__", None)
            values = []
            if names is not None and len(names) == len(p.patterns):
                for name in names:
                    values.append(getattr(s, name))
            else:
                # fallback: best-effort positional attributes
                for attr, subp in zip(names or [], p.patterns):
                    values.append(getattr(s, attr))
            envs = []
            for val, subp in zip(values, p.patterns):
                envs.append(rec(val, subp, depth + 1))
            merged = merge_envs(envs)
            trace.append(f"{indent}=> class matched, env={merged}")
            return merged

        trace.append(f"{indent}X unknown pattern type: {p!r}")
        raise MatchFailure()

    try:
        env = rec(subject, pattern, 0)
        return True, env, trace
    except MatchFailure:
        return False, {}, trace


# --- Demo when run as script ----------------------------------------
if __name__ == "__main__":
    # import local Atom/Functor if available
    try:
        from .recursion import Atom, Functor
    except Exception:
        # fallback simple definitions
        @dataclass
        class Atom:
            value: Any

        @dataclass
        class Functor:
            op: str
            children: Tuple[Any, ...]
            __match_args__ = ("op", "children")

    expr = Functor("*", (Functor("+", (Atom(3), Atom(5))), Atom(2)))

    # Pattern: Functor("*", (left, right))
    pattern = PClass(Functor, (PLiteral("*"), PTuple((PName("left"), PName("right")))))

    ok, env, trace = match_with_trace(expr, pattern)
    print("MATCH OK:", ok)
    print("ENV:", env)
    print("TRACE:")
    for line in trace:
        print(line)
