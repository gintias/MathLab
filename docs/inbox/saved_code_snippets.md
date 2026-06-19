---
title: Saved Code Snippets and Patterns
status:
purpose:
---
## 0. Governing doctrine

The package should not begin with a monolithic `FirstOrderLanguage` object.

The package should begin with the neutral universal-algebra spine:

```text
sorts
profile words / arities
sorted families
profile-correct maps
symbols
functional signatures
algebras
homomorphisms
free algebras
quotients
descent
```

Then first-order logic should enter as a layer that **uses** this machinery:

```text
functional reduct
terms
atoms
raw formulas
binding-aware formulas
structures
evaluation
satisfaction
proof systems
theories
term models
Lindenbaum–Tarski quotients
model theory
```

The main p