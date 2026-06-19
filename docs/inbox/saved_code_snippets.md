---
title: Saved Code Snippets and Patterns
status:
purpose:
---

# Draft / Preliminary Proposal — Logic Package Architecture from the UA–FOL Spine

This document is a preliminary architecture sketch for a `logic/` package organized around the settled distinction between:

1. **universal algebra as a general algebraic engine**, and  
2. **first-order logic as a logical development that admits that engine at specific points**.

It is not a final API specification. Names, classes, modules, and methods below are suggestions. The architectural order is the important part.

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

The main principle:

```text
Universal algebra is not syntax-specific.
Syntax appears when one builds a free algebra over a signature.
First-order logic admits universal algebra repeatedly, at specific layers.
```

The main guardrails:

```text
A signature is not syntax by itself.

The term signature Σ_L builds terms only.

Raw formula syntax uses a different constructor signature from Σ_L.

Variables are generators, not constants and not function symbols.

Constants are nullary function symbols.

Relation symbols do not build terms.

Equality is logical, not a nonlogical relation symbol.

Structures interpret syntax; they are generally semantic targets / quotient-image targets,
not faithful presentations of free syntax.

Quotient operations require descent / representative-independence.
```

---

## 1. Proposed top-level package shape

A full eventual package could be organized as:

```text
logic/
  foundations/
    sorts.py
    profiles.py
    families.py
    maps.py

  symbols/
    identity.py
    symbols.py
    families.py

  ua/
    signatures.py
    algebras.py
    homomorphisms.py
    generated.py
    free.py
    quotients.py
    presentations.py

  syntax/
    variables.py
    terms.py
    constructors.py
    folds.py
    contexts.py
    substitution.py
    presentations.py

  fol/
    vocabulary.py
    language.py
    relations.py
    equality.py
    atoms.py
    formulas_raw.py
    binding.py
    formulas.py
    substitution.py

  semantics/
    structures.py
    assignments.py
    evaluation.py
    satisfaction.py
    consequence.py

  proof/
    calculi.py
    rules.py
    derivations.py
    closure.py
    theories.py

  quotients/
    congruences.py
    term_models.py
    lindenbaum.py
    descent.py

  model_theory/
    elementary.py
    diagrams.py
    types.py
    ultraproducts.py

  presentations/
    trees.py
    tuples.py
    strings.py
    dags.py

  tests/
    test_ua_signature.py
    test_terms.py
    test_fol_atoms.py
    test_semantics.py
```

This is the full conceptual map, not the first implementation target.

A near-term package may stay flatter, but it should preserve the same dependency direction.

---

## 2. Dependency direction

The intended import flow is one-way:

```text
foundations
  ↓
symbols
  ↓
ua
  ↓
syntax
  ↓
fol
  ↓
semantics / proof / quotients / model_theory
```

More explicitly:

```text
fol may import syntax and ua.

ua must not import fol.

syntax may import ua.

semantics may import fol, syntax, and ua.

proof may import fol.

quotients may import fol, proof, semantics, syntax, and ua.

model_theory may import semantics, proof, and fol.
```

This matters because first-order logic should not be allowed to leak back downward into the universal-algebra layer.

---

# Part I — Foundations

## 3. `foundations/`: neutral sorted infrastructure

This is the "not yet syntax" layer.

Even if the first implementation is single-sorted, the architecture should remember that the single-sorted case is a collapse of the sorted picture.

### 3.1 `foundations.sorts`

Possible objects:

```text
Sort
SortSet
```

Responsibilities:

```text
Sort:
  identity/name of a universe sort

SortSet:
  collection of sorts
  membership check
```

In single-sorted FOL, this can be represented by a distinguished default object sort:

```text
*
```

or:

```text
Object
```

No symbols, variables, terms, formulas, or structures belong here.

---

### 3.2 `foundations.profiles`

Possible objects:

```text
ProfileWord
Arity
```

Mathematical role:

```text
w = (s_1, ..., s_n)
```

In the single-sorted case this collapses to a natural-number arity:

```text
n
```

Responsibilities:

```text
ProfileWord:
  finite input list of sorts
  arity
  empty profile
```

Possible interface:

```text
ProfileWord.empty()
ProfileWord.from_sorts(s1, ..., sn)
ProfileWord.of_arity(n, object_sort)
```

Important guard:

```text
A profile word is not syntactic text.
It is a finite tuple/list of sorts.
```

---

### 3.3 `foundations.families`

Possible objects:

```text
SortedFamily
CarrierFamily
GeneratorFamily
```

Responsibilities:

```text
SortedFamily:
  mapping Sort -> collection/object

CarrierFamily:
  mapping Sort -> semantic carrier

GeneratorFamily:
  mapping Sort -> generator set
```

In single-sorted FOL, each sorted family is just one set. The distinction still matters conceptually:

```text
carrier set M
variable set Var
term set Term
formula set Form
```

These are not the same object, even when each is one-sorted.

---

### 3.4 `foundations.maps`

Possible objects:

```text
ProfileCorrectMap
FamilyMap
```

Responsibilities:

```text
ProfileCorrectMap:
  sortwise map between sorted families

FamilyMap:
  generic map respecting sort indices
```

This abstracts the common shape of:

```text
homomorphisms
assignments
substitutions
renamings
semantic valuations
```

In the single-sorted case, this reduces to an ordinary function.

---

# Part II — Symbols

## 4. `symbols/`: formal symbol identity and symbol stocks

This layer represents symbols as identity-bearing objects.

It should not yet assign all possible mathematical roles. A generated symbol stock should not itself know whether it will become part of a functional signature, relation vocabulary, variable supply, or logical vocabulary.

---

### 4.1 `symbols.identity`

Possible objects:

```text
SymbolKey
SymbolId
```

Responsibilities:

```text
SymbolKey:
  local key inside one generated symbol family

SymbolId:
  canonical internal identity
  usually family_id + key
```

This lets glyph/display remain distinct from symbol identity.

---

### 4.2 `symbols.symbols`

Possible objects:

```text
Symbol
FunctionSymbol
RelationSymbol
LogicalSymbol
```

Recommended current stance:

```text
FunctionSymbol:
  universal-algebra reading: operation symbol
  FOL reading: function symbol

RelationSymbol:
  relation / predicate symbol
  not part of the term signature

LogicalSymbol:
  object-language logical marker, if represented explicitly
```

There is no current need for both `OperationSymbol` and `FunctionSymbol` as separate runtime classes unless they eventually carry different behavior. The role difference is contextual:

```text
In universal algebra:
  function symbol is read as operation symbol.

In FOL:
  function symbol is read as a member of Func_L.
```

---

### 4.3 `symbols.families`

Possible objects:

```text
SymbolFamilySpec
GeneratedSymbolFamily
```

Responsibilities:

```text
SymbolFamilySpec:
  immutable recipe for symbol generation
  family identity
  symbol class
  glyph/rendering policy

GeneratedSymbolFamily:
  stateful lazy generator
  memoization
  fresh symbol generation
  returns same object for same key
```

Important guard:

```text
GeneratedSymbolFamily is symbol infrastructure.

It does not know profiles.

It does not know whether its symbols are admitted by a signature or language.

Admission belongs to the signature/vocabulary layer.
```

Later profiled wrappers may exist:

```text
ProfiledGeneratedFunctionFamily
ProfiledGeneratedRelationFamily
```

These belong conceptually closer to `ua.signatures` and `fol.vocabulary`, not raw symbol identity.

---

# Part III — Universal Algebra

## 5. `ua/`: pure universal algebra

This is the central neutral layer. It should exist before first-order logic.

It contains:

```text
functional signatures
algebras
homomorphisms
generated subalgebras
free algebras
quotients
descent
presentations
```

---

## 5.1 `ua.signatures`

Possible objects:

```text
FunctionProfile
FunctionalSignature
SignatureInclusion
SignatureReduct
SignatureExpansion
ProfiledGeneratedFunctionFamily
```

### `FunctionProfile`

Mathematical role:

```text
f : w -> s
```

In the single-sorted case:

```text
f : n -> *
```

Possible fields:

```text
input_profile: ProfileWord
output_sort: Sort
```

Possible properties:

```text
arity
input_sorts
is_nullary
```

Constants are exactly nullary function symbols:

```text
c : () -> s
```

or in single-sorted form:

```text
c : 0 -> *
```

No separate `ConstantSymbol` or `ConstantProfile` is needed.

---

### `FunctionalSignature`

Mathematical object:

```text
Σ = (S, Op_{w,s})
```

In code, using FOL-friendly names:

```text
FunctionalSignature:
  sorts
  function_profiles: FunctionSymbol -> FunctionProfile
  generated_function_families
```

Responsibilities:

```text
store profiled function/operation symbols

validate all profile sorts are declared

answer profile lookup

admit explicit finite symbols

admit generated profiled function families

reject unknown function symbols

reject undeclared sorts inside profiles
```

Possible methods:

```text
has_sort(s)
function_profile(f)
admits_function(f)
declared_functions()
```

Important guard:

```text
FunctionalSignature is not syntax.

It is the operation-symbol interface.

Syntax appears only when building the free algebra over it.
```

---

## 5.2 `ua.algebras`

Possible objects:

```text
Algebra
CarrierFamily
OperationInterpretation
```

Mathematical object:

```text
A = ((A_s), (f^A))
```

In single-sorted form:

```text
A = set A + operations f^A : A^n -> A
```

Responsibilities:

```text
store a FunctionalSignature

store carriers

store interpretations of function symbols

validate arity/profile correctness where possible

apply interpreted operations
```

Possible methods:

```text
carrier(sort)
interpret_function(f)
apply(f, args)
```

Important guard:

```text
A Σ-algebra is not necessarily syntactic.

It may be:
  integers with arithmetic operations
  a term algebra
  a quotient term algebra
  a Boolean algebra
  a formula algebra
```

---

## 5.3 `ua.homomorphisms`

Possible objects:

```text
Homomorphism
HomomorphismCheck
Isomorphism
Kernel
```

Responsibilities:

```text
store source algebra
store target algebra
store underlying profile-correct map
check operation preservation
represent kernel where possible
```

Possible methods:

```text
apply(sort, value)
preserves(symbol, args)
kernel_relation()
```

In the single-sorted case:

```text
h(f^A(a_1, ..., a_n)) = f^B(h(a_1), ..., h(a_n))
```

---

## 5.4 `ua.generated`

Possible objects:

```text
GeneratedSubalgebra
ClosureOperator
```

Responsibilities:

```text
stage closure under operations
least closed subcarrier containing generators
generated image of a homomorphism
```

This becomes important for:

```text
semantic images of term evaluations
generated substructures
proof/deductive closures by analogy
```

---

## 5.5 `ua.free`

Possible objects:

```text
FreeAlgebra
FreeAlgebraSpec
GeneratorInsertion
UniqueExtension
```

Mathematical object:

```text
T_Σ(X)
```

Responsibilities:

```text
record signature Σ
record generator family X
state/implement constructor formation
provide UMP interface
```

Possible conceptual API:

```text
free_algebra.signature
free_algebra.generators
free_algebra.inject_generator(x)
free_algebra.extend(generator_map, target_algebra)
```

The concrete implementation of `extend` will usually be a fold/evaluator over a concrete term representation.

Important guard:

```text
This is the first genuinely syntactic object in the UA spine.
```

---

## 5.6 `ua.quotients`

Possible objects:

```text
Congruence
KernelCongruence
QuotientAlgebra
QuotientProjection
```

Responsibilities:

```text
represent operation-compatible equivalence relations

form quotient algebras

state/prove descent of operations

represent first-isomorphism comparisons
```

Possible methods:

```text
compatible_with(signature)
quotient(algebra, congruence)
projection()
```

This machinery will later support:

```text
semantic kernels
term models
Lindenbaum–Tarski algebras
alpha quotient
```

---

## 5.7 `ua.presentations`

Possible objects:

```text
ConstructorPresentation
FreePresentation
PresentationIsomorphism
```

Responsibilities:

```text
certify concrete carriers as presentations of abstract free syntax

record no-junk/no-confusion or UMP-based certification

record comparison maps between presentations
```

Concrete examples:

```text
tree syntax
tuple syntax
string syntax
DAG syntax
AST node syntax
```

Critical distinction:

```text
Faithful free-syntax presentation:
  P ≅ T_Σ(X)

Semantic image / quotient:
  A ≅ T_Σ(X) / ker
```

Do not call every semantic algebra a faithful syntax presentation.

---

# Part IV — Syntax over Signatures

## 6. `syntax/`: free syntax over functional signatures

This layer is not FOL-specific yet. It is syntax as the concrete/free algebra over a functional signature.

---

## 6.1 `syntax.variables`

Possible objects:

```text
Variable
VariableFamily
FreshVariableSupply
```

Responsibilities:

```text
store variable identity
store sort
generate fresh variables
support renaming
```

For single-sorted FOL, sort may be implicit. Architecturally, variables are still generators, not constants.

Important guard:

```text
Variables are generators.

Constants are nullary function symbols.

Variables are not in the functional signature.
```

---

## 6.2 `syntax.terms`

Possible objects:

```text
Term
VariableTerm
FunctionApplication
```

Mathematical formation cases:

```text
x

f(t_1, ..., t_n)
```

Constants are represented as:

```text
FunctionApplication(c, ())
```

where `c` has nullary profile.

Responsibilities:

```text
store signature
store output sort
ensure function symbol is admitted by signature
ensure argument sorts match function profile
support one-step decomposition
support structural recursion/fold
```

Possible methods:

```text
term.sort
term.signature
term.variables()
term.decompose()
term.fold(...)
```

This is where a prior generic `Decomposable` / `Atomic` / `Constructed` prototype becomes relevant, but it should be specialized to actual term cases:

```text
VariableTerm
FunctionApplication
```

not generic arbitrary atoms.

---

## 6.3 `syntax.folds`

Possible objects:

```text
TermFold
TermAlgebraEvaluator
RecursiveTermDefinition
```

Responsibilities:

```text
perform structural recursion over free term syntax

implement the UMP extension concretely

define size, depth, pretty printing, evaluation, substitution, etc.
```

Possible conceptual API:

```text
fold_term(
  variable_case,
  function_case,
)
```

or:

```text
extend_assignment(
  assignment: Variable -> TargetCarrier,
  algebra: Algebra
)
```

This is the computational face of the free-algebra UMP.

---

## 6.4 `syntax.substitution`

Possible objects:

```text
TermSubstitution
TermRenaming
```

Mathematical object:

```text
σ : Var -> Term

σ̂ : Term -> Term
```

Responsibilities:

```text
store sort-correct variable-to-term map
homomorphically extend to all terms
identity substitution
composition / Kleisli composition
```

Substitution is not textual replacement at the foundation level. It is a homomorphic extension.

---

## 6.5 `syntax.contexts`

Possible objects:

```text
Hole
Context
OneHoleContext
MultiHoleContext
Plugging
```

Mathematical object:

```text
T_Σ(X ⊔ H)
```

Responsibilities:

```text
represent terms with holes
plug terms into holes
compose contexts
distinguish holes from variables by role
```

Contexts are not FOL-specific.

---

## 6.6 `syntax.presentations`

Possible objects:

```text
TreeTerm
TupleTerm
StringTerm
DAGTerm
ParserPresentation
```

Responsibilities:

```text
provide concrete syntax carriers

state whether they are faithful presentations

avoid treating addresses, pointer identity, or sharing as invariant syntax
```

Concrete presentation data belongs here, not in the abstract `Term`.

---

# Part V — First-Order Logic

## 7. `fol/`: first-order vocabulary and syntax

This is where first-order logic proper begins.

A single monolithic `FirstOrderLanguage` object is too ambiguous unless its role is explicitly fixed.

The architecture should split:

```text
FirstOrderVocabulary
FirstOrderFormationSystem
FirstOrderLanguage facade, optional
```

---

## 7.1 `fol.vocabulary`

Possible objects:

```text
RelationProfile
RelationVocabulary
FirstOrderVocabulary
```

### `RelationProfile`

Single-sorted form:

```text
R : n
```

Many-sorted eventual form:

```text
R : w
```

Possible field:

```text
input_profile: ProfileWord
```

No output sort. Relation symbols do not build terms.

---

### `RelationVocabulary`

Responsibilities:

```text
store relation symbols with profiles

admit explicit and generated relation families

validate profile sorts

answer relation_profile(R)

reject unknown relation symbols
```

---

### `FirstOrderVocabulary`

Strict nonlogical vocabulary:

```text
FirstOrderVocabulary:
  functional_signature: FunctionalSignature
  relation_vocabulary: RelationVocabulary
```

This corresponds to the strict first-order nonlogical datum:

```text
L = (Func_L, Rel_L)
```

or in many-sorted form:

```text
L = (S, Func_L, Rel_L)
```

It should not include:

```text
variables
logical connectives
quantifier syntax
proof calculus
semantics
```

---

## 7.2 `fol.language`

Possible objects:

```text
FirstOrderFormationSystem
FirstOrderLanguage
```

### `FirstOrderFormationSystem`

Broader syntactic formation environment:

```text
FirstOrderFormationSystem:
  vocabulary: FirstOrderVocabulary
  variable_supply: VariableFamily
  equality_policy: EqualityPolicy
  logical_constructors: LogicalVocabulary
  binding_policy: BindingPolicy
```

Responsibilities:

```text
provide enough data to form:
  terms
  atoms
  raw formulas
  binding-aware formulas
```

This is broader than the strict nonlogical vocabulary.

---

### `FirstOrderLanguage`

Optional public façade.

Possible role:

```text
FirstOrderLanguage:
  wraps FirstOrderVocabulary
  exposes helpers for term/atom/formula construction
```

or:

```text
FirstOrderLanguage:
  public bundle of FirstOrderVocabulary + FirstOrderFormationSystem
```

Do not let this become the mathematical root of the package.

---

## 7.3 `fol.equality`

Possible objects:

```text
EqualityPolicy
ObjectEquality
EqualityAtomPolicy
```

Responsibilities:

```text
decide whether equality is available
ensure equality atoms compare terms of appropriate sort
mark equality as logical, not RelationSymbol
```

For classical FOL with equality:

```text
t = u
```

is an atom, but `=` is not a member of `Rel_L`.

---

## 7.4 `fol.atoms`

Possible objects:

```text
Atom
RelationAtom
EqualityAtom
```

Responsibilities:

```text
consume terms

check relation profile against term arity/sorts

produce formula base cases
```

Important boundary:

```text
RelationAtom is not a Term.

EqualityAtom is not a Term.

Atoms are not values of an object sort.
```

Atom formation is the layer change from terms to formulas.

---

## 7.5 `fol.formulas_raw`

Possible objects:

```text
RawFormula
AtomicFormula
Not
Implies
And
Or
ForAllRaw
ExistsRaw
FormulaConstructorSignature
```

This is the second major UA admission.

Mathematical reading:

```text
Form_raw ≅ T_Ωform(Atom_L)
```

where:

```text
Atom_L = generators

Ω_form = logical formula constructors
```

Responsibilities:

```text
build raw formulas

support formula recursion

compute syntactic support/free variables at the raw level

remain pre-alpha
```

Important guard:

```text
Raw formulas are not elements of T_Σ_L(Var).

They are free syntax for a different constructor signature.
```

---

## 7.6 `fol.binding`

Possible objects:

```text
FreeVariableAnalysis
BoundVariableAnalysis
AlphaEquivalence
FreshnessPolicy
CaptureAvoidance
Binder
```

Responsibilities:

```text
free/bound occurrence
fresh variable generation
alpha-renaming
capture-avoidance
free-for checks
```

This is not just ordinary universal algebra. It is the binding layer.

---

## 7.7 `fol.formulas`

Possible objects:

```text
Formula
AlphaClassFormula
FormulaView
```

Mathematical object:

```text
Form_L = Form_raw / ≡_α
```

Responsibilities:

```text
represent formulas modulo alpha-equivalence

ensure operations are alpha-compatible

avoid unsafe representative-dependent operations
```

This is the binding-aware formula object.

---

## 7.8 `fol.substitution`

Possible objects:

```text
FormulaSubstitution
CaptureAvoidingSubstitution
SchemaInstantiation
```

Responsibilities:

```text
apply term substitution at atomic leaves

recurse through connectives

handle quantifiers with freshness/renaming

enforce side conditions
```

Depends on:

```text
syntax.substitution.TermSubstitution
fol.binding
fol.formulas
```

---

# Part VI — Semantics

## 8. `semantics/`: structures, evaluation, satisfaction

This is where FOL syntax receives meaning.

---

## 8.1 `semantics.structures`

Possible objects:

```text
Structure
FunctionalReduct
RelationInterpretation
```

### `Structure`

Single-sorted FOL structure:

```text
carrier M
function interpretations f^M : M^n -> M
relation interpretations R^M ⊆ M^n
equality interpreted as identity
```

Responsibilities:

```text
validate each function symbol has an operation of correct arity

validate each relation symbol has a relation/predicate of correct arity

expose functional_reduct()
```

---

### `FunctionalReduct`

A `ua.Algebra` over `Σ_L`.

Responsibilities:

```text
forget relations

forget satisfaction

retain carrier and function interpretations
```

This is the exact point where structures admit universal algebra.

---

## 8.2 `semantics.assignments`

Possible objects:

```text
Assignment
AssignmentUpdate
```

Responsibilities:

```text
map variables to carrier elements

validate sort if many-sorted

update variable x to value m

restrict to relevant variables
```

Single-sorted form:

```text
Var -> M
```

---

## 8.3 `semantics.evaluation`

Possible objects:

```text
TermEvaluation
EvaluationHomomorphism
EvaluationKernel
```

Mathematical object:

```text
ev_{M,a}: Term_L -> M_alg
```

Responsibilities:

```text
evaluate variables by assignment

evaluate constants/functions by structure

represent semantic kernel where possible

support substitution lemma
```

This is UMP into the semantic algebraic reduct.

---

## 8.4 `semantics.satisfaction`

Possible objects:

```text
Satisfaction
TruthDefinition
```

Responsibilities:

```text
truth of equality atoms

truth of relation atoms

truth under connectives

truth under quantifiers via assignment update

locality on free variables

alpha-invariance
```

Important boundary:

```text
Satisfaction is not merely a homomorphism from Term_L.

It is structural recursion on formulas.
```

---

## 8.5 `semantics.consequence`

Possible objects:

```text
SemanticConsequence
Validity
Satisfiability
TheoryOfStructure
```

Responsibilities:

```text
Γ ⊨ φ

⊨ φ

model of Γ

Th(M)
```

This is model-theoretic semantics, not plain universal algebra.

---

# Part VII — Proof and Theories

## 9. `proof/`: calculi, derivations, closure

This layer records proof systems.

---

## 9.1 `proof.calculi`

Possible objects:

```text
Calculus
HilbertCalculus
NaturalDeduction
SequentCalculus
Rule
AxiomSchema
SideCondition
```

Responsibilities:

```text
store axiom schemata

store inference rules

store side conditions

fix what ⊢ means
```

There should be no global derivability relation without a calculus.

---

## 9.2 `proof.derivations`

Possible objects:

```text
Derivation
ProofTree
ProofStep
Judgment
Sequent
```

A proof tree is another optional free-constructor / inductive syntax object:

```text
axiom leaf

rule node with premise derivations
```

Responsibilities:

```text
store finite proof object

extract conclusion

list assumptions

verify rule applications
```

---

## 9.3 `proof.closure`

Possible objects:

```text
ConsequenceClosure
DeductiveClosure
RuleClosure
```

Mathematical object:

```text
Cn_C(Γ)
```

Responsibilities:

```text
least set containing Γ and axioms, closed under rules
```

This is not a term algebra, but it is another algebraic/closure admission.

---

## 9.4 `proof.theories`

Possible objects:

```text
Theory
AxiomSet
DeductivelyClosedTheory
ConsistentTheory
CompleteTheory
```

Responsibilities:

```text
store sentences/formulas

represent deductive closure

compare semantic and syntactic closure

track consistency relative to a calculus
```

Theories sit at the boundary of proof, semantics, and quotients.

---

# Part VIII — Quotients and Descent

## 10. `quotients/`: congruences, term models, Lindenbaum–Tarski

This layer should be explicit because quotient mistakes are common.

---

## 10.1 `quotients.congruences`

Possible objects:

```text
EquivalenceRelation
Congruence
FormulaCongruence
FullyInvariantCongruence
DescentProof
```

Responsibilities:

```text
record what relation is being quotiented

state compatibility with operations

state which operations descend
```

Used for:

```text
alpha quotient
semantic evaluation kernel
provable equality on terms
provable equivalence on formulas
Lindenbaum congruence
```

---

## 10.2 `quotients.term_models`

Possible objects:

```text
ClosedTermAlgebra
ProvableEqualityCongruence
TermModel
```

Mathematical object:

```text
TM(T) = closed terms / provable equality
```

Responsibilities:

```text
construct carrier as equivalence classes of closed terms

descend function interpretations

descend relation interpretations via provability

support truth lemma later
```

This is a quotient of term syntax.

---

## 10.3 `quotients.lindenbaum`

Possible objects:

```text
ProvableEquivalence
LindenbaumTarskiAlgebra
SentenceLindenbaumAlgebra
BooleanSkeleton
CylindricEnrichment
```

Mathematical object:

```text
LT(T) = Form_L / ≡_T
```

Responsibilities:

```text
quotient formulas by provable equivalence

descend connectives

represent Boolean algebra operations

represent quantifier/cylindric operators when included

distinguish full formula algebra from sentence algebra
```

---

## 10.4 `quotients.descent`

Possible objects:

```text
DescentCondition
DescendedOperation
RepresentativeIndependence
```

Responsibilities:

```text
prove/check an operation is well-defined on quotient classes

centralize quotient obligations
```

Any operation on quotient syntax should go through this layer conceptually.

---

# Part IX — Model Theory

## 11. `model_theory/`: beyond plain universal algebra

This layer should be later and should not contaminate the syntax core.

Possible modules:

```text
elementary.py
diagrams.py
types.py
ultraproducts.py
compactness.py
loewenheim_skolem.py
```

Possible objects:

```text
Embedding
ElementaryEmbedding
Substructure
GeneratedSubstructure
Diagram
Type
CompleteType
Ultraproduct
```

Responsibilities:

```text
model-theoretic maps

elementary equivalence

types and realization

diagram methods

ultraproduct construction
```

Important boundary:

```text
compactness, Löwenheim–Skolem, elementary equivalence, and types
are not merely UMP/quotient/descent phenomena.
```

---

# Part X — Implementation phases

## 12. Phase 1: Neutral UA signature

Implement first:

```text
Sort
ProfileWord
SymbolId
SymbolKey
Symbol
FunctionSymbol
RelationSymbol
FunctionProfile
FunctionalSignature
```

Goal:

```text
zero : 0
succ : 1
add  : 2
```

as a single-sorted functional signature.

No terms yet. No formulas yet. No FOL language yet.

---

## 13. Phase 2: Free term syntax

Implement:

```text
Variable
Term
VariableTerm
FunctionApplication
TermFold
TermSubstitution
```

Goal:

```text
add(succ(zero), zero)
```

is a well-formed term over a functional signature.

---

## 14. Phase 3: Algebra and evaluation

Implement:

```text
Algebra
Assignment
TermEvaluation
```

Goal:

```text
evaluate add(succ(zero), zero) in N
```

This proves the UMP/evaluation vertical slice.

---

## 15. Phase 4: FOL vocabulary and atoms

Implement:

```text
RelationProfile
RelationVocabulary
FirstOrderVocabulary
RelationAtom
EqualityAtom
```

Goal:

```text
lt(add(x, y), z)

x = succ(y)
```

are atoms, not terms.

---

## 16. Phase 5: Raw formulas

Implement:

```text
RawFormula
Not
Implies
And
Or
ForAllRaw
ExistsRaw
```

Goal:

```text
∀x (P(x) -> Q(x))
```

as raw syntax.

---

## 17. Phase 6: Binding-aware formulas

Implement:

```text
FreeVariableAnalysis
AlphaEquivalence
CaptureAvoidingSubstitution
Formula
```

Goal:

```text
∀x P(x) ==_alpha ∀y P(y)
```

when appropriate.

---

## 18. Phase 7: Semantics

Implement:

```text
Structure
FunctionalReduct
Assignment
TermEvaluation
Satisfaction
```

Goal:

```text
M, a ⊨ φ
```

with term evaluation at atoms.

---

## 19. Phase 8: Proof and theories

Implement:

```text
Calculus
Rule
Derivation
DeductiveClosure
Theory
```

Goal:

```text
Γ ⊢_C φ
```

with calculus dependence explicit.

---

## 20. Phase 9: Quotients

Implement:

```text
Congruence
TermModel
LindenbaumTarskiAlgebra
DescentProof
```

Goal:

```text
closed terms / provable equality

formulas / provable equivalence
```

---

## 21. Phase 10: Model theory

Only after semantics, proof, and theories are stable.

---

# Part XI — Minimal current repo plan

For the current codebase, do not build everything at once.

A good near-term shape is:

```text
logic/
  foundations/
    sorts.py
    profiles.py

  symbols/
    identity.py
    symbols.py
    families.py

  ua/
    signatures.py

  syntax/
    variables.py
    terms.py
    folds.py
```

Or temporarily:

```text
logic/
  language.py
  algebra.py
  terms.py
```

with the understanding that:

```text
language.py:
  temporary holding area for symbols/sorts/profiles

algebra.py:
  FunctionalSignature and later Algebra

terms.py:
  free term syntax
```

The immediate code correction remains:

```text
OperationProfile and FunctionProfile should not both exist.

Use FunctionProfile as the profile object for term-forming/function/operation symbols.

FunctionalSignature should be the neutral UA signature object.

FirstOrderVocabulary comes later.
```

---

# Final architecture compression

```text
UA foundation:
  sorts, profiles, signatures, algebras, homomorphisms

Free syntax:
  free algebra over a signature

FOL term layer:
  functional reduct Σ_L + variables -> Term_L

FOL atom/formula layer:
  relations/equality consume terms -> atoms
  connectives/quantifiers close atoms -> raw formulas

Binding layer:
  alpha, freshness, capture-avoidance

Semantics:
  structures interpret symbols
  functional reduct is a Σ_L-algebra
  term evaluation is UMP extension
  satisfaction is formula recursion

Proof:
  calculus fixes ⊢
  derivations are inductively generated
  consequence is least rule-closed set

Quotients:
  semantic kernels
  term models
  Lindenbaum–Tarski algebras
  descent obligations

Model theory:
  elementary maps, types, compactness, LS, ultraproducts
```

This architecture preserves the settled distinction:

```text
Universal algebra is the reusable engine.

First-order logic repeatedly admits that engine at specific layers.

No single "Language" object should flatten those layers.
```
