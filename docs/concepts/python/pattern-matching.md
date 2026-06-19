# Python Pattern Matching: Formal Semantics & Mapping to Free Algebras

This document gives a concise, operational specification of Python's structural pattern-matching (PEP 634) expressed as inference-style rules, and maps those rules to the free-algebra / formula ASTs present in this workspace (`Atom`/`Functor`, `logic.formulas`).

## 1. Informal summary
- Patterns test the *shape* of a subject value and, on success, produce a binding environment mapping pattern names to subvalues. Matching is structural (class/type + attributes or sequence contents) and runs left-to-right in a `match` statement: the first successful `case` is selected. Guards are evaluated after structural matching.

## 2. Pattern language (subset)
We use the following pattern grammar (subset of Python patterns):

- `_` : wildcard
- `L` : literal
- `x` : capture name
- `(P1,...,Pn)` : tuple/sequence pattern
- `P1 | P2` : or-pattern
- `P as x` : as-pattern
- `P if G` : guarded pattern (G is an expression evaluated under the pattern bindings)
- `C(P1,...,Pn)` : class pattern (uses `C.__match_args__` or keywords)

## 3. Matching relation
We write `match(s, P) => fail` or `match(s, P) => (ok, ρ)` where `ρ` is an environment (finite map from names to values).

### 3.1. Formal inference rules

We use big-step style rules. Each rule describes when `match(s, P)` succeeds and what environment it produces.

**(Lit)**

```
---------------
match(L, L) => (ok, {})
```

and if `s ≠ L` then `match(s, L) => fail`.

**(Wildcard)**

```
-----------------
match(s, _) => (ok, {})
```

**(Name)**

```
----------------
match(s, x) => (ok, {x ↦ s})
```

**(Tuple)**

```
match(s1, P1) => (ok, ρ1)   ...   match(sn, Pn) => (ok, ρn)
dom(ρi) ∩ dom(ρj) = ∅ for i ≠ j
--------------------------------------------------
match((s1,...,sn), (P1,...,Pn)) => (ok, ρ1 ∪ ... ∪ ρn)
```

**(Or-Left)**

```
match(s, P1) => (ok, ρ)
------------------------
match(s, P1 | P2) => (ok, ρ)
```

**(Or-Right)**

```
match(s, P1) => fail   match(s, P2) => (ok, ρ)
---------------------------------------------
match(s, P1 | P2) => (ok, ρ)
```

**(As)**

```
match(s, P) => (ok, ρ)   x ∉ dom(ρ)
----------------------------------
match(s, P as x) => (ok, ρ ∪ {x ↦ s})
```

**(Guard)**

```
match(s, P) => (ok, ρ)   eval_guard(G, ρ) = True
-----------------------------------------------
match(s, P if G) => (ok, ρ)
```

**(Class)**

Let `C.__match_args__ = (a1,...,an)`.

```
isinstance(s, C)
match(getattr(s, a1), P1) => (ok, ρ1) ... match(getattr(s, an), Pn) => (ok, ρn)
dom(ρi) ∩ dom(ρj) = ∅ for i ≠ j
---------------------------------------------------------
match(s, C(P1,...,Pn)) => (ok, ρ1 ∪ ... ∪ ρn)
```

If the class pattern uses explicit keywords, the same rule applies with the corresponding attribute names.

### 3.2. `match` statement rule

```
match(subject):
  case P1: B1
  case P2: B2
  ...
```

is equivalent to

```
v = eval(subject)
if match(v, P1) => (ok, ρ1) and guard1(ρ1) succeeds:
    execute B1 with env ρ1
elif match(v, P2) => (ok, ρ2) and guard2(ρ2) succeeds:
    execute B2 with env ρ2
else:
    raise MatchError
```

Guards are only evaluated after the pattern structure matches.

### 3.3. Environment and capture discipline

- Bindings are created only on successful matches.
- Duplicate names within the same pattern alternative are not allowed.
- `P1 | P2` returns the bindings from the successful alternative only.
- `P as x` binds the whole subject after the subpattern matches.

### 3.4. Class-pattern semantics for free algebras

For a free-algebra node `N` with `__match_args__ = (a1,...,an)`, the class pattern `N(P1,...,Pn)` means:

1. test `isinstance(subject, N)`
2. extract `value_i = getattr(subject, ai)` for each i
3. recursively match `value_i` against `Pi`

This is the structural core of pattern matching on user-defined algebraic nodes.

### 3.5. Example: `Atom` / `Functor`

Given:

```python
class Atom:
    __match_args__ = ("value",)

class Functor:
    __match_args__ = ("op", "children")
```

Then:

- `case Atom(v)` binds `v` to `subject.value`.
- `case Functor("+", (left, right))` checks `subject.op == "+"`, then matches `subject.children` as a tuple against `(left, right)`.
- `case Functor("+", left, right)` would require `__match_args__ = ("op","left","right")` instead.

### 3.6. Example: `logic.formulas`

For `dataclass` formula nodes, positional patterns follow field order.

```python
match formula:
    case Not(body):
        ...
    case And(left, right):
        ...
    case ForAll(var, body):
        ...
    case ForAllIn(var, domain, body):
        ...
```

This means the match against `ForAll(var, body)` is equivalent to:
1. `isinstance(formula, ForAll)`
2. `match(formula.var, var)`
3. `match(formula.body, body)`

The same structural principle applies to any recursively defined algebraic AST.

## 4. `match` statement semantics
Given `match subject: case P1: B1 case P2: B2 ...` evaluate `subject` to `v` then try `match(v, Pi)` in order; for the first `Pi` that yields `(ok, ρ)` and whose guard (if present) evaluates true under `ρ`, execute `Bi` with names bound as in `ρ`.

## 5. Mapping to free algebras (`Atom` / `Functor`)

- If your free-algebra node exposes positional fields (e.g. `op`, `left`, `right`) and sets `__match_args__ = ("op","left","right")`, then `case Functor("+", left, right):` performs:
  1. `isinstance(subject, Functor)` check
  2. `subject.op == "+"` comparison
  3. destructure `subject.left` → `left`, `subject.right` → `right` and run subpattern matches

- If your `Functor` uses a single `children` tuple, expose `__match_args__ = ("op","children")` and match with `case Functor("+", (l, r)):`—the tuple pattern will destructure the `children` tuple.

Examples:

```
match expr:
    case Atom(v):             # uses Atom.__match_args__
        ...
    case Functor("+", (a, b)):
        ...
```

## 6. Guards and evaluation ordering
- Structural matching (the rules above) runs before the guard. Only after a structural match succeeds do we evaluate the guard expression with the bound names.

## 7. Operational intuition / translation
Every `case` can be seen as a nested sequence of `isinstance` checks, attribute extractions and recursive matches. Pseudocode for `case Functor("+", left, right):` is:

```
if isinstance(subject, Functor) and subject.op == "+":
    tmp_left = subject.left
    tmp_right = subject.right
    if match(tmp_left, left) succeeds and match(tmp_right, right) succeeds and guard passes:
        bind names and run body
```

## 8. Recommendations for your codebase

- Choose either positional attributes (`op,left,right`) or a single `children` tuple and set `__match_args__` accordingly.
- Prefer `children` as a tuple for n-ary signatures (uniform sequence matching). Use `case Functor(op, children):` then match `children` further.
- Avoid properties with side-effects because match will access attributes during pattern checks.

## 9. Concrete examples for `logic.formulas`

Using the dataclasses in `logic.formulas`, you can write:

```
match f:
    case PredCall(name, args): ...
    case Not(body):            ...
    case And(l, r):           ...
    case ForAll(var, body):    ...
```

The dataclass fields are automatically available for positional patterns, so `ForAll(var, body)` binds the `var` and `body` fields.

---

If you want, I can: add runnable tracing utilities that show step-by-step matching for a given subject and pattern, or generate a short test suite mapping pattern forms to the inference rules. Which next step do you prefer?
