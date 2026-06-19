# Logic-Layer Agent Guidance

## Required Reference

Before substantive discussion, design, explanation, review, or implementation concerning the `logic/` layer, read this document in full:

`docs/concepts/mathematics/THEORY_ATLAS.md`

`THEORY_ATLAS.md` is the authoritative mathematical ground source for logic-layer work. Use it as the source of truth for mathematical claims, distinctions, data, maps, invariants, dependencies, information boundaries, and laws. Use longer or older mathematical reference files only when the Atlas explicitly points outward, leaves the current question unresolved, or a precise result needs verification. If another theory note conflicts with the Atlas, treat the Atlas as authoritative unless the user explicitly says otherwise.

The Atlas is a mathematical reference, not a package architecture. It fixes the canonical mathematical model for selected logic-layer concepts; it does not by itself require implementing every room, following its section order as package structure, or deriving APIs from its exposition.

## Primary Design Priority

In the logic layer, the project mathematics is authoritative for the canonical conceptual model.

Faithfully represent the mathematical data, distinctions, maps, invariants, dependencies, information boundaries, and laws of each concept that is chosen for implementation. Python built-ins may represent the underlying sets, indexed families, functions, and relations. Custom set-theoretic objects are not required.

## Mathematical Objects and Their Python Encodings

Distinguish the mathematical object from the particular encoding used to realize it in Python.

A mathematical definition may present data using sets, indexed families, membership relations, tuples, and maps. A faithful Python implementation does not have to reproduce each of those using a literal `set`, `frozenset`, tuple, or dictionary. Python classes, subclasses, fields, tags, discriminated unions, and validated records may encode the same mathematical data and invariants.

For example, membership in distinct mathematical symbol families may be encoded either by:

- one `Symbol` type plus literal collections recording family membership; or
- distinct Python symbol types whose class identity encodes that membership.

Neither representation is more faithful merely because one visually resembles set-theoretic notation. Judge faithfulness by whether the mathematical distinctions and valid states can be recovered, whether the required invariants are enforced, and whether the specified maps and operations behave correctly.

Do not call an object encoding a conflation merely because several mathematical facts are represented through its type or fields. First determine whether the representation actually erases a distinction or instead encodes that distinction in another form. Conversely, do not use object encoding as an excuse to erase information, admit invalid states without a policy, or change the mathematical object being represented.

When comparing representations, explain the correspondence between the mathematical data and each Python encoding. Keep literal set encoding and object encoding available as genuine alternatives unless the mathematics or a project requirement rules one out.

Do not collapse mathematically distinct concepts merely because combining them produces fewer classes, less code, a more conventional API, or a faster implementation. Python idioms and convenience are subordinate to mathematical fidelity in this layer.

Minimal implementation means implementing a smaller mathematical slice faithfully. It does not mean weakening or combining the concepts inside that slice.

The mathematics fixes the conceptual requirements, not every Python representation. When multiple representations are faithful, explain their consequences and rationale. Do not choose one merely because it is shortest, easiest, or most visually similar to the set-theoretic definition. If a representation stores mathematically distinct data together, determine whether it erases the distinction or faithfully encodes it through types, fields, tags, or validated access.

Convenience constructors, wrappers, views, caching, and ergonomic APIs may be added around the faithful core. They must not replace it or obscure which mathematical object is being represented.

## Design Order

For a logic-layer concept or vertical slice, reason in this order:

1. Choose the next mathematical concept or narrow slice.
2. Identify its mathematical data from the relevant rooms of `THEORY_ATLAS.md`.
3. Identify its invariants and laws.
4. Identify its maps, operations, dependencies, consumers, outputs, and mathematical level.
5. Determine what the mathematics fixes and what remains a Python representation choice.
6. Discuss faithful Python representations and their tradeoffs.
7. Choose a representation provisionally.
8. Produce a learning template when code is requested.
9. Verify that the implementation preserves the identified invariants and laws.

This is an order of reasoning, not a fixed package architecture. Do not implement later mathematical layers merely because they appear later in the Atlas or this sequence. Keep coverage narrow and commitments provisional.

Do not create a separate catalogue of every mathematical object or require the user to maintain a design-basis document. Extract only the information relevant to the current slice from the Atlas and any necessary supporting references.

## Interaction Rules

When the user requests discussion only, discuss the mathematical objects, distinctions, and representation alternatives without immediately producing class definitions or implementation code.

A request to "speed up" normally concerns conversational pacing. It does not authorize optimizing the design for speed, convenience, fewer types, or less mathematical fidelity unless the user explicitly asks for the fastest or simplest implementation.

Do not use "Pythonic," "simple," "minimal," or "no current consumer" as sufficient reasons to erase a distinction present in the selected mathematical slice.
