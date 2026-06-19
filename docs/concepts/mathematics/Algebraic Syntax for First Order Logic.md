---
title: "Algebraic Syntax for First-Order Logic Preparation"
subtitle: "Free Syntax, Concrete Presentations, Transfer, Substitution, Clones, Evaluation, and Quotient Syntax"
tags: [universal-algebra, term-algebra, free-algebra, syntax, presentations, transfer, substitution, contexts, clones, evaluation, congruence, quotient, descent, first-order-logic]
---

# Algebraic Syntax for First-Order Logic Preparation

## 0. Orientation and Scope

### 0.1. Purpose of the Note

#### 0.1.1. Restricted Universal-Algebraic Aim

This treatise is not a general text on universal algebra. It develops exactly the fragment of universal algebra that functions as a **syntax engine**: the theory of absolutely free $\Omega$-algebras, their concrete realizations, the canonical maps among those realizations, and the structural operations (substitution, contexts, clones, evaluation, quotients) that freeness underwrites. Topics of independent universal-algebraic interest — congruence lattice theory, Mal'cev conditions, subdirect representation, Birkhoff's variety theorem in full, clone lattices — are excluded or reduced to the minimal statements required by the syntactic development. The eventual target is the syntax of first-order logic: the term-forming layer of a first-order language is an absolutely free algebra over the function-symbol signature, and every later first-order construction (atomic formulas, satisfaction, deduction, theories) is built on top of the machinery isolated here. The restriction of scope is deliberate: depth on the syntax bridge, not breadth across algebra.

#### 0.1.2. Syntax Before Semantics

The governing methodological decision is that **raw syntax is an abstract free algebra prior to any interpretation**. The construction of terms (a closure process governed by a signature) is strictly separated from the evaluation of terms (a homomorphism into a chosen target algebra determined by a valuation). The first process produces an object $\mathbf{T}_{\Omega}(X)$ characterized by a universal mapping property; the second process consumes that object. Keeping the two processes apart is what later permits a clean account of the distinction between syntactic equality and semantic equality, between generated and freely generated structures, and between maps that build representations and maps that assign meaning. For first-order logic this separation isolates the term-forming component: terms exist and have exact structural theory before any structure interprets them.

#### 0.1.3. Why Concrete Presentations Matter

The abstract free algebra is unique only up to canonical isomorphism; to compute with it, store it, parse it, or display it, one chooses a **concrete presentation**: recursively defined term expressions, labelled ranked trees, tagged set-theoretic tuples, or well-formed strings over an alphabet. These presentations are pairwise canonically isomorphic but are **not literally identical objects**: a string is not a tree, and a tree is not a nested tuple. Each presentation exposes different machinery — trees expose positions and subtrees, tuples expose set-theoretic coding, strings expose linear input/output and parsing — and each is verified to be free on the same generators by a uniform set-theoretic criterion (Chapter 5). A dedicated transfer chapter (Chapter 11) then establishes that all structure, all proofs, and all operations transport across the canonical isomorphisms, so that the later theory is developed once, on the invariant object, rather than four times.

### 0.2. Main Development Pipeline

#### 0.2.1. Abstract Free Syntax

Part II introduces the free $\Omega$-algebra on a generator set $X$ as the invariant syntax object. Its defining feature is the **universal mapping property** (UMP): every assignment of the generators into the carrier of any $\Omega$-algebra extends to a unique homomorphism. The UMP — not any particular carrier — is the definition. Existence is then witnessed by the canonical term algebra $\mathbf{T}_{\Omega}(X)$ (Chapter 4), and a set-theoretic construction engine (Chapter 5) supplies reusable criteria certifying that a candidate concrete carrier realizes the same free object. Concrete syntax is thereafter treated as a system of *representations* of one abstract object.

#### 0.2.2. Concrete Syntax Algebras

Part III constructs four concrete syntax algebras in full: the recursive term-expression algebra (Chapter 6), the tree algebra on addressed, labelled, arity-correct trees (Chapter 7), the tagged tuple algebra of set-theoretic codes (Chapter 8), and the string algebra of well-formed strings under hygiene conditions (Chapter 9), with a survey of implementation-oriented variants (Chapter 10). For each, the development records the carrier, the constructor operations, the generator map, the unique-decomposition property, and the freeness theorem, and sets up the canonical generator-preserving isomorphism with $\mathbf{T}_{\Omega}(X)$.

#### 0.2.3. Operations and Evaluation

Parts IV–VI develop the operational layer, in each case *after* transfer is available, so that every operation is defined once on the invariant object: structural decomposition, subterms, positions, and complexity measures (Chapter 12); structural induction and recursion (Chapter 13); substitution as syntax-valued evaluation (Chapter 14); contexts as derived syntax operations (Chapter 15); the syntactic clone of arity-indexed terms under formal superposition (Chapter 16); evaluation into target algebras, with the image identified as the generated subalgebra and the kernel as the record of semantic collapse (Chapter 17); and quotient syntax with the descent conditions governing recursion, evaluation, and substitution modulo identifications (Chapter 18). The spine is the chain

$$
\text{term algebra} \longrightarrow \text{presentation} \longrightarrow \text{evaluation} \longrightarrow \text{image / generated subalgebra} \longrightarrow \text{kernel / quotient}.
$$

### 0.3. Standing Distinctions

#### 0.3.1. Syntax Equality versus Semantic Equality

Two terms are **syntactically equal** when they are the same element of the free algebra — equivalently, when they have identical constructor decompositions. Two terms are **semantically equal under a valuation** when evaluation sends them to the same element of the target algebra. Syntactic equality implies semantic equality; the converse fails in general, and the failure is recorded exactly by the **kernel of the evaluation homomorphism**, a congruence on syntax (Chapter 17). Two kernel-type relations must themselves be kept distinct: the **valuation kernel** (equality under one fixed assignment) and the **clone kernel / equational kernel** (equality of induced term operations under *all* assignments, Chapter 16). The first is local; the second is global and substitution-stable.

> [!warning] Warning 0.1: Never identify a term with its value
> The symbol $f$ acts on terms as a formal constructor and on a target carrier as an interpreted operation $f^{\mathbf{B}}$. The equation $f^{\mathbf{T}}(t_1,\dots,t_n) = f^{\mathbf{B}}(b_1,\dots,b_n)$ is type-incorrect: the left side is a term, the right side an element of $B$. Every later failure mode in this treatise — ill-defined recursion on collapsed structures, illegitimate quotient substitution, parser/evaluator confusion — originates in an identification of syntax with its semantic image.

#### 0.3.2. Generated versus Freely Generated

A structure is **generated** by a set when every element is reachable from that set by finitely many constructor applications; this yields *existence* of representations (surjectivity of a canonical comparison map out of syntax). A structure is **freely generated** when, in addition, representations are *unique* (injectivity of that comparison map). The algebraic test for the additional condition is **triviality of the kernel** of the comparison or evaluation map: no two distinct terms collapse. The slogan, made precise in Theorem 17.10, is

$$
\text{freeness} \;=\; \text{generatedness} \;+\; \text{no accidental identification}.
$$

#### 0.3.3. Parsing, Substitution, Evaluation, Quotienting

Four families of maps with different domains and codomains are kept rigorously apart throughout, and are assembled into a final taxonomy in Chapter 19:

1. **representation-level maps** — representation maps $r_P : \mathbf{T}_{\Omega}(X) \to \mathbf{P}$ identifying concrete carriers with abstract syntax, transfer maps between presentations, and parsers carrying strings or codes *into* syntax;
2. **syntax-level maps** — substitutions $\widehat{\sigma} : \mathbf{T}_{\Omega}(X) \to \mathbf{T}_{\Omega}(Y)$ carrying syntax to syntax, and context/plugging operations;
3. **semantic maps** — evaluation homomorphisms $\operatorname{ev}_g : \mathbf{T}_{\Omega}(X) \to \mathbf{B}$ carrying syntax to a target algebra, and clone interpretations carrying formal operations to concrete operations;
4. **quotient maps** — projections $\operatorname{nat}_{\theta} : \mathbf{T}_{\Omega}(X) \to \mathbf{T}_{\Omega}(X)/\theta$ carrying raw syntax to syntax modulo identifications.

A parser is not an evaluator: the parser's codomain is syntax, the evaluator's codomain is a semantic algebra, and an *interpreter* is their composite (Chapter 9). A substitution is not a valuation: both extend generator data by the same universal mechanism, but the codomain of a substitution is again a syntax algebra.

> [!remark] Remark 0.2: Reading conventions
> Numbered items (Definition, Notation, Construction, Lemma, Proposition, Theorem, Corollary, Proof Sketch, Example, Remark, Warning) form the formal spine; items are numbered consecutively within each chapter, so "Theorem 4.7" is the seventh item of Chapter 4. Running prose between items records structural relationships only. Proof sketches accompany nontrivial results and identify the construction, the key verification, and the universal property invoked; they are not complete proofs.

### 0.4. Dependency Spine and Companion Alignment

The logical dependencies are linear with one deliberate loop. Part I (Chapters 1–2) supplies the algebraic vocabulary. Part II defines freeness abstractly (Chapter 3), constructs the canonical witness (Chapter 4), and isolates the set-theoretic engine (Chapter 5); the engine's recursion theorem is proved independently of Chapter 4 and then certifies it (Remark 5.14), so no circularity remains. Part III applies the engine four times; Part IV proves the transfer theorem; Parts V–VI consume only the UMP, the transfer theorem, and the toolkit of Part I. Part VII is closure.

The treatise is aligned with two companion developments and may be read against them. The set-theoretic companion develops generation, free generation, well-founded recursion, and the structural recursion theorem for arbitrary families of constructor relations on an ambient set; Chapter 5 is the single-valued, total specialization of that machinery, with constructor maps in place of constructor relations and ranks in place of general well-founded recursion; the official carrier (Construction 4.13) is assembled from exactly the finite-sequence and concatenation apparatus that the companion develops. The clone-theoretic companion develops concrete clones, polymorphisms, invariant relations, and polynomial operations in full; Chapter 16 extracts from it exactly the syntactic clone, the interpretation map, and the kernel comparison, deferring the Galois-theoretic superstructure. Where notational variants exist, this treatise fixes: boldface algebras with italic carriers, $\widehat{\sigma}$ for substitution extensions, $\operatorname{ev}_g$ for evaluations, $\star$ for substitution composition, and $\theta_E$ versus $\theta_E^{\mathrm{fi}}$ for ground versus fully invariant congruence generation.

---

# Part I — Minimal Algebraic Toolkit
## 1. Signatures, Algebras, and Homomorphisms

This chapter assembles only the algebraic vocabulary required for term formation and term evaluation. The ambient foundation is a fixed model of Zermelo–Fraenkel set theory with Choice (ZFC); $\mathbb{N} = \{0,1,2,\dots\}$, each $n \in \mathbb{N}$ is identified with $\{1,\dots,n\}$ for indexing purposes when convenient, $A^{n}$ denotes the set of $n$-tuples from $A$, $A^{<\omega} = \bigcup_{n \in \mathbb{N}} A^{n}$ the set of finite sequences over $A$ with empty sequence $\varepsilon$ and concatenation $u \cdot v$, $\mathcal{P}(A)$ the power set, and $f[S] = \{f(a) : a \in S\}$ the image of $S \subseteq \operatorname{dom}(f)$. Three relations are kept strictly distinct: set-theoretic equality $=$, isomorphism $\cong$, and definitional identity $:=$.

### 1.1. Finitary Signatures

#### 1.1.1. Operation Symbols and Arity

> [!definition] Definition 1.1: Signature
> A **(one-sorted, finitary) signature** is a pair $\Omega = (\Omega, \operatorname{ar})$ consisting of a set $\Omega$ of **operation symbols** together with an **arity function**
>
> $$
> \operatorname{ar} : \Omega \to \mathbb{N}.
> $$
>
> For $f \in \Omega$, the natural number $\operatorname{ar}(f)$ is the **arity** of $f$; the symbol $f$ is **$n$-ary** when $\operatorname{ar}(f) = n$, and **nullary**, **unary**, **binary** for $n = 0, 1, 2$. For each $n \in \mathbb{N}$ set
>
> $$
> \Omega_n := \{\, f \in \Omega : \operatorname{ar}(f) = n \,\},
> $$
>
> so that $\Omega = \coprod_{n \in \mathbb{N}} \Omega_n$ as a disjoint union of arity classes. Specifying a signature is equivalent to specifying the family $(\Omega_n)_{n \in \mathbb{N}}$ of pairwise disjoint sets.

The arity of a symbol is its **constructor shape**: it prescribes how many already-formed terms the symbol consumes when it forms a new term. Throughout the treatise the setting is one-sorted and finitary; each statement that depends essentially on finitary arity (stabilization of stage constructions at $\omega$, finiteness of terms) is flagged where it occurs. Signatures and generator sets may be of arbitrary cardinality.

> [!remark] Remark 1.2: Overloading is excluded
> The arity function assigns exactly one arity to each symbol. A symbol may not be simultaneously binary and ternary; "overloaded" notations are modeled by distinct symbols. This convention is load-bearing: the determinism of prefix string syntax (Chapter 10) and the disjointness clauses of the free-generation criteria (Chapter 5) both fail under overloading.

#### 1.1.2. Nullary Symbols

> [!definition] Definition 1.3: Constant symbols
> The elements of $\Omega_0$ are the **nullary operation symbols** of $\Omega$, also called **(formal) constant symbols**. In every $\Omega$-algebra a nullary symbol is interpreted as a distinguished element of the carrier (Remark 1.7), and in every syntax algebra a nullary symbol appears as an **atomic term**: a term with no immediate subterms, produced by a constructor consuming the empty tuple.

Nullary symbols are signature-controlled: their interpretation is fixed by the choice of algebra, not by any assignment of values to generators. They therefore behave as rigid atoms of syntax, in contrast with the freely assignable generators introduced next.

#### 1.1.3. Constants versus Generators

> [!warning] Warning 1.4: Constants are forced; generators are free
> A **constant symbol** $c \in \Omega_0$ is part of the signature: it is interpreted in every $\Omega$-algebra, and every homomorphism preserves it ($h(c^{\mathbf{A}}) = c^{\mathbf{B}}$, Definition 1.10). A **generator** $x \in X$ is an element of an auxiliary set adjoined to the signature from outside: it carries no interpretation of its own, receives a value only through a valuation or assignment $g : X \to B$, and is preserved only by maps explicitly required to respect the generator structure. Both constants and generators occur as atomic terms, but they behave oppositely under maps: constants are forced, generators are free. The construction of $\mathbf{T}_{\Omega}(X)$ requires $X \cap \Omega = \varnothing$ (Definition 4.1), and conflating $\Omega_0$ with $X$ destroys freeness: a "generator" that every homomorphism must preserve cannot receive arbitrary values.

This distinction is the first standing distinction of §0.3 in local form, and it persists into first-order logic: individual constants of a first-order language are nullary function symbols, while individual variables are generators of the term algebra.

### 1.2. $\Omega$-Algebras

#### 1.2.1. Carrier and Operations

> [!definition] Definition 1.5: $\Omega$-algebra
> Let $\Omega$ be a signature. An **$\Omega$-algebra** is a pair
>
> $$
> \mathbf{A} = \big(A,\ (f^{\mathbf{A}})_{f \in \Omega}\big)
> $$
>
> where $A$ is a set, the **carrier** of $\mathbf{A}$, and for each $f \in \Omega_n$,
>
> $$
> f^{\mathbf{A}} : A^{n} \to A
> $$
>
> is a total $n$-ary operation, the **interpretation** of $f$ in $\mathbf{A}$. Boldface letters $\mathbf{A}, \mathbf{B}, \mathbf{P}$ denote algebras and the corresponding italic letters $A, B, P$ their carriers. $\mathbf{A}$ is **trivial** if $A$ is a singleton and **empty** if $A = \varnothing$, which is possible iff $\Omega_0 = \varnothing$.

> [!notation] Notation 1.6: Basic operation family
> For an $\Omega$-algebra $\mathbf{A}$, write $F_{\mathbf{A}} := \{ f^{\mathbf{A}} : f \in \Omega \}$ for its family of **basic operations**. Operations definable from $F_{\mathbf{A}}$ by formal terms — the **term operations** — are strictly more general and are developed in Chapter 16.

> [!remark] Remark 1.7: Nullary interpretations are distinguished elements
> Since $A^{0} = \{()\}$ is a singleton, a nullary interpretation $c^{\mathbf{A}} : A^{0} \to A$ is determined by its unique value $c^{\mathbf{A}}() \in A$, with which it is identified; one writes $c^{\mathbf{A}} \in A$. Whenever $\Omega_0 \neq \varnothing$, every $\Omega$-algebra has nonempty carrier.

#### 1.2.2. Syntax Algebras versus Target Algebras

> [!definition] Definition 1.8: Syntax algebra, target algebra
> An $\Omega$-algebra is used in this treatise in one of two roles. A **syntax algebra** is an algebra whose elements are themselves syntactic objects (formal terms, trees, tuples, strings) and whose operations are formal constructor applications; the principal example is $\mathbf{T}_{\Omega}(X)$ (Chapter 4) and its presentations (Part III). A **target algebra** (or **semantic algebra**) is an arbitrary $\Omega$-algebra $\mathbf{B}$ into which syntax is evaluated (Chapter 17). The role is not intrinsic: a syntax algebra may serve as the target of a substitution (Chapter 14), which is precisely evaluation into syntax.

> [!warning] Warning 1.9: One symbol, two meanings
> A single operation symbol $f \in \Omega_n$ has a syntax-side meaning — the formal constructor $f^{\mathbf{T}}(t_1, \dots, t_n)$, which builds a longer term and forgets nothing — and an algebra-side meaning — the interpreted operation $f^{\mathbf{B}}(b_1, \dots, b_n)$, which computes an element and may collapse information. The two are connected only through evaluation homomorphisms. Writing bare "$f$" for both is standard but must never be read as an identification.

#### 1.2.3. Reducts and Expansions, Briefly

> [!definition] Definition 1.10: Reduct and expansion
> Let $\Omega' \subseteq \Omega$ be a subsignature (a subset with the restricted arity function). The **$\Omega'$-reduct** of an $\Omega$-algebra $\mathbf{A}$ is
>
> $$
> \mathbf{A}\!\restriction_{\Omega'} := \big(A,\ (f^{\mathbf{A}})_{f \in \Omega'}\big),
> $$
>
> the algebra with the same carrier and only the $\Omega'$-operations. Conversely, $\mathbf{A}$ is an **expansion** of $\mathbf{B}$ when $\mathbf{A}\!\restriction_{\Omega'} = \mathbf{B}$. Reducts keep the carrier and discard structure; expansions keep the carrier and add structure.

The single later use is this: a first-order structure for a language with function and relation symbols has an underlying **algebraic reduct** obtained by forgetting the relation symbols, and the term syntax of the language is the free algebra over exactly that function-symbol signature. No general theory of reducts is developed.

### 1.3. Homomorphisms

#### 1.3.1. Preservation of Operations

> [!definition] Definition 1.11: Homomorphism
> Let $\mathbf{A}, \mathbf{B}$ be $\Omega$-algebras. A **homomorphism** $h : \mathbf{A} \to \mathbf{B}$ is a function $h : A \to B$ satisfying, for every $f \in \Omega_n$ and all $a_1, \dots, a_n \in A$, the **preservation equation**
>
> $$
> h\big(f^{\mathbf{A}}(a_1, \dots, a_n)\big) \;=\; f^{\mathbf{B}}\big(h(a_1), \dots, h(a_n)\big).
> $$
>
> For $n = 0$ the equation reads $h(c^{\mathbf{A}}) = c^{\mathbf{B}}$ for every $c \in \Omega_0$: homomorphisms preserve constants. The set of homomorphisms $\mathbf{A} \to \mathbf{B}$ is denoted $\operatorname{Hom}_{\Omega}(\mathbf{A}, \mathbf{B})$.

> [!proposition] Proposition 1.12: Closure of homomorphisms under composition
> The identity map $\mathrm{id}_A$ is a homomorphism $\mathbf{A} \to \mathbf{A}$; if $h : \mathbf{A} \to \mathbf{B}$ and $k : \mathbf{B} \to \mathbf{C}$ are homomorphisms then $k \circ h : \mathbf{A} \to \mathbf{C}$ is a homomorphism. Hence $\Omega$-algebras and homomorphisms form a category $\mathbf{Alg}(\Omega)$.

> [!proof-sketch] Proof Sketch 1.12
> For the composite, apply the preservation equation for $h$ inside the arguments of $f^{\mathbf{B}}$ and then the preservation equation for $k$; the identity case is the preservation equation with $h = \mathrm{id}_A$. Associativity and unit laws of composition are inherited from functions.

#### 1.3.2. Isomorphisms

> [!definition] Definition 1.13: Isomorphism, embedding, endomorphism
> A homomorphism $h : \mathbf{A} \to \mathbf{B}$ is an **isomorphism** if there exists a homomorphism $h^{-1} : \mathbf{B} \to \mathbf{A}$ with $h^{-1} \circ h = \mathrm{id}_A$ and $h \circ h^{-1} = \mathrm{id}_B$; one writes $\mathbf{A} \cong \mathbf{B}$. An **embedding** is an injective homomorphism; an **endomorphism** is a homomorphism $\mathbf{A} \to \mathbf{A}$; an **automorphism** is an isomorphism $\mathbf{A} \to \mathbf{A}$.

> [!proposition] Proposition 1.14: Bijective homomorphisms are isomorphisms
> For $\Omega$-algebras (total operations, no relation symbols), a homomorphism is an isomorphism iff it is bijective: the set-theoretic inverse of a bijective homomorphism is automatically a homomorphism.

> [!proof-sketch] Proof Sketch 1.14
> Given bijective $h$ and $b_i \in B$, write $b_i = h(a_i)$; the preservation equation for $h$ applied to $f^{\mathbf{A}}(a_1,\dots,a_n)$ yields $h^{-1}\big(f^{\mathbf{B}}(b_1,\dots,b_n)\big) = f^{\mathbf{A}}\big(h^{-1}(b_1),\dots,h^{-1}(b_n)\big)$.

> [!warning] Warning 1.15: Isomorphism is not literal equality
> $\mathbf{A} \cong \mathbf{B}$ asserts the existence of a structure-preserving bijection; it does not assert $A = B$. The discipline matters most for syntax presentations (Part III): the tree algebra and the string algebra are canonically isomorphic but are different sets, and statements about internal encoding (string length, tuple rank) do not transfer across the isomorphism. Proposition 1.14 itself fails for structures with relation symbols, a point that resurfaces when the relational layer of first-order logic is added on top of the present algebraic layer.

#### 1.3.3. Generator-Preserving Isomorphisms

> [!definition] Definition 1.16: Maps over $X$
> Let $X$ be a set and let $\mathbf{A}, \mathbf{B}$ be $\Omega$-algebras equipped with **generator maps** $\eta_{\mathbf{A}} : X \to A$ and $\eta_{\mathbf{B}} : X \to B$. A homomorphism $h : \mathbf{A} \to \mathbf{B}$ is a **homomorphism over $X$** (synonym: **generator-preserving**) when
>
> $$
> h \circ \eta_{\mathbf{A}} = \eta_{\mathbf{B}},
> $$
>
> i.e. $h$ carries the $\mathbf{A}$-copy of each generator to the $\mathbf{B}$-copy of the same generator. An **isomorphism over $X$** is an isomorphism that is a homomorphism over $X$; its inverse is then automatically a homomorphism over $X$.

> [!remark] Remark 1.17: Why the over-$X$ condition is needed
> Two presentations of syntax must agree not merely as abstract algebras but on *which element represents which variable*: an isomorphism that permutes the variables is structure-preserving yet useless for transfer of substitution or evaluation, since those operations are indexed by the variables themselves. All transfer maps of Chapter 11 are isomorphisms over $X$, and the uniqueness assertion of the master transfer theorem (Theorem 11.10) holds only in the over-$X$ category. Freeness will guarantee that between free objects there is exactly one such isomorphism.

### 1.4. Standing Examples

> [!example] Example 1.18: Standard signatures
> (i) **Magmas**: $\Omega = \{\cdot\}$, $\operatorname{ar}(\cdot) = 2$. (ii) **Monoid signature**: $\{\cdot, e\}$, arities $2, 0$. (iii) **Group signature**: $\{\cdot, {}^{-1}, e\}$, arities $2, 1, 0$. (iv) **Unital ring signature**: $\{+, \cdot, -, 0, 1\}$, arities $2, 2, 1, 0, 0$. (v) **Boolean signature**: $\{\vee, \wedge, \neg, \mathbf{0}, \mathbf{1}\}$, arities $2, 2, 1, 0, 0$. (vi) **Successor signature**: $\{\mathsf{s}\}$, arity $1$, with a constant $\mathsf{0}$ adjoined when a base point is wanted. A signature fixes only the **type** of a structure; the usual axioms (associativity, inverses, distributivity) are equations and play no role in absolutely free syntax — they enter only as congruences on syntax in Chapter 18.

> [!example] Example 1.19: Algebras, reducts, homomorphisms
> (i) $(\mathbb{Z}, +, -, 0)$ is an algebra for the group signature; its reduct to $\{+\}$ is the magma $(\mathbb{Z}, +)$. (ii) For a set $U$, $(\mathcal{P}(U), \cup, \cap, {}^{\complement}, \varnothing, U)$ is a Boolean-signature algebra, and the two-element algebra $\mathbf{2} = (\{0, 1\}, \vee, \wedge, \neg, 0, 1)$ is the standard semantic target of propositional logic. (iii) The parity map $h : \mathbb{Z} \to \mathbb{Z}/2\mathbb{Z}$ is a homomorphism for the group signature: it preserves $+$, $-$, and the constant $0$. (iv) The inclusion $(\mathbb{N}, +, 0) \hookrightarrow (\mathbb{Z}, +, 0)$ is an embedding of monoid-signature algebras; the absolute-value map $\mathbb{Z} \to \mathbb{N}$ is **not** a homomorphism for $+$ (preservation fails at $1 + (-1)$), illustrating that carrier maps require verification against every operation, constants included.

> [!remark] Remark 1.20: Many-sorted generalization, deferred
> All definitions of this chapter extend to **many-sorted** signatures: a sort set $S$, symbols typed $f : s_1 \times \cdots \times s_n \to s$, carriers replaced by $S$-indexed families of sets, and operations and homomorphisms required to respect sorts. Every theorem of this treatise generalizes sortwise with only notational overhead. The one-sorted setting is retained because the term layer of first-order logic over a single domain of individuals is one-sorted; the many-sorted version becomes relevant for typed languages and is not developed here.

---
## 2. Subalgebras, Kernels, Congruences, and Quotients

This chapter records the four pieces of structure theory that the syntactic development consumes: closed subsets and generated subalgebras (which model "reachable by constructors"), kernels (which record semantic identification), congruences (which are exactly the equivalence relations that quotients tolerate), and the first isomorphism theorem (which presents every homomorphic image as a quotient). Lattice-theoretic refinements are omitted.

### 2.1. Subalgebras and Generated Subalgebras

#### 2.1.1. Closed Subsets

> [!definition] Definition 2.1: Closed subset and subalgebra
> Let $\mathbf{A}$ be an $\Omega$-algebra and $C \subseteq A$. The set $C$ is **closed under the operations of $\mathbf{A}$** if for every $f \in \Omega_n$ and all $c_1, \dots, c_n \in C$,
>
> $$
> f^{\mathbf{A}}(c_1, \dots, c_n) \in C;
> $$
>
> for $n = 0$ this requires $c^{\mathbf{A}} \in C$ for every $c \in \Omega_0$ (**nullary closure**). A closed subset carries the **induced operations** $f^{\mathbf{C}} := f^{\mathbf{A}}\!\restriction_{C^{n}}$, making it an $\Omega$-algebra $\mathbf{C}$, the **subalgebra of $\mathbf{A}$ on $C$**, written $\mathbf{C} \leq \mathbf{A}$; the inclusion $C \hookrightarrow A$ is an embedding.

> [!warning] Warning 2.2: Nullary closure is the standard omission
> If $\Omega_0 \neq \varnothing$ then no closed subset is empty, since it must contain every $c^{\mathbf{A}}$. Checking closure under the positive-arity operations while forgetting the constants is the most common error in subalgebra verifications; in the syntactic reading, it corresponds to forgetting that constants are terms.

Closure under operations is the exact algebraic rendering of "closed under the constructors": a set of syntactic objects closed under all formal constructor applications is a closed subset of the relevant syntax algebra.

#### 2.1.2. Generated Subalgebras

> [!proposition] Proposition 2.3: Intersection stability
> For any family $(C_i)_{i \in I}$ of closed subsets of $\mathbf{A}$ (with the convention $\bigcap_{i \in \varnothing} C_i = A$), the intersection $\bigcap_{i \in I} C_i$ is closed.

> [!proof-sketch] Proof Sketch 2.3
> Arguments lying in the intersection lie in each $C_i$; each $C_i$ contains the value $f^{\mathbf{A}}(\vec{c}\,)$; hence so does the intersection. Nullary closure is the $n=0$ instance.

> [!definition] Definition 2.4: Generated subalgebra
> For $S \subseteq A$, the **subalgebra of $\mathbf{A}$ generated by $S$** is
>
> $$
> \langle S \rangle_{\mathbf{A}} := \bigcap \{\, C \subseteq A : S \subseteq C,\ C \text{ closed in } \mathbf{A} \,\},
> $$
>
> well-defined by Proposition 2.3 and characterized as the **least** closed subset of $\mathbf{A}$ containing $S$ (a minimality condition: $\langle S\rangle_{\mathbf{A}}$ contains $S$, is closed, and is contained in every closed superset of $S$). $\mathbf{A}$ is **generated by $S$** when $\langle S \rangle_{\mathbf{A}} = A$.

> [!construction] Construction 2.5: Stage construction of $\langle S \rangle_{\mathbf{A}}$
> Define a $\subseteq$-increasing sequence of subsets of $A$ by
>
> $$
> S^{(0)} := S \cup \{\, c^{\mathbf{A}} : c \in \Omega_0 \,\},
> $$
>
> $$
> S^{(k+1)} := S^{(k)} \cup \{\, f^{\mathbf{A}}(a_1, \dots, a_n) : n \geq 1,\ f \in \Omega_n,\ a_1, \dots, a_n \in S^{(k)} \,\}.
> $$
>
> Then $\langle S \rangle_{\mathbf{A}} = \bigcup_{k < \omega} S^{(k)}$. The union is closed because every $f \in \Omega_n$ is finitary: any $n$ arguments from the union already lie in a common stage $S^{(k)}$, so their image lies in $S^{(k+1)}$.

> [!warning] Warning 2.6: Stabilization at $\omega$ requires finitary arity
> With operations of infinite arity, $\bigcup_{k<\omega} S^{(k)}$ need not be closed, and the iteration must continue through limit ordinals. The intersection formula of Definition 2.4 is correct at every arity; the stage construction is a tool valid in the finitary setting adopted here, and it is the tool that yields finite construction ranks for syntax (Chapter 5).

#### 2.1.3. Images of Homomorphisms

> [!proposition] Proposition 2.7: Homomorphic images are subalgebras; images of generated are generated
> Let $h : \mathbf{A} \to \mathbf{B}$ be a homomorphism. Then (i) $\operatorname{im}(h) = h[A]$ is a closed subset of $\mathbf{B}$, hence a subalgebra $\operatorname{im}(h) \leq \mathbf{B}$; (ii) for every $S \subseteq A$,
>
> $$
> h\big[\langle S \rangle_{\mathbf{A}}\big] \;=\; \big\langle h[S] \big\rangle_{\operatorname{im}(h)} \;=\; \big\langle h[S] \big\rangle_{\mathbf{B}}.
> $$

> [!proof-sketch] Proof Sketch 2.7
> (i) $f^{\mathbf{B}}(h(a_1),\dots,h(a_n)) = h(f^{\mathbf{A}}(a_1,\dots,a_n)) \in h[A]$ by preservation. (ii) Both inclusions follow by stagewise induction on Construction 2.5: $h$ maps $S^{(k)}$ into the $k$-th stage of $\langle h[S]\rangle_{\mathbf{B}}$ and conversely every stage of $\langle h[S]\rangle_{\mathbf{B}}$ is reached by images, since $h$ commutes with each operation.

Clause (ii) is the seed of the evaluation-image theorem (Theorem 17.6): the image of an evaluation homomorphism out of syntax is exactly the subalgebra generated by the values of the generators. No general image-factorization theory beyond this is required.

### 2.2. Kernels and Congruences

#### 2.2.1. Kernel of a Homomorphism

> [!definition] Definition 2.8: Kernel
> The **kernel** of a homomorphism $h : \mathbf{A} \to \mathbf{B}$ is the binary relation
>
> $$
> \ker h := \{\, (a, a') \in A \times A : h(a) = h(a') \,\}.
> $$
>
> Elements $a, a'$ are **identified by $h$** when $(a, a') \in \ker h$. The **diagonal** $\Delta_A := \{(a,a) : a \in A\}$ is the kernel of any injective homomorphism; $h$ is injective iff $\ker h = \Delta_A$.

In the syntactic reading, the kernel of an evaluation map is the set of pairs of terms with the same value: the **semantic identification relation**, the exact record of collapse. Triviality of the kernel is the algebraic formulation of "no two distinct pieces of syntax denote the same thing."

#### 2.2.2. Congruences

> [!definition] Definition 2.9: Congruence
> A **congruence** on an $\Omega$-algebra $\mathbf{A}$ is an equivalence relation $\theta \subseteq A \times A$ that is **compatible** with every basic operation: for each $f \in \Omega_n$ and all $a_i, b_i \in A$,
>
> $$
> (a_1, b_1) \in \theta, \ \dots, \ (a_n, b_n) \in \theta \;\Longrightarrow\; \big(f^{\mathbf{A}}(a_1, \dots, a_n),\ f^{\mathbf{A}}(b_1, \dots, b_n)\big) \in \theta.
> $$
>
> (The $n = 0$ instance is vacuous.) The set of congruences on $\mathbf{A}$ is $\operatorname{Con}(\mathbf{A})$; it always contains $\Delta_A$ and the total relation $\nabla_A := A \times A$. The **$\theta$-class** of $a$ is $[a]_\theta := \{b : (a,b) \in \theta\}$.

> [!construction] Construction 2.10: Congruence generated by a relation
> For $R \subseteq A \times A$, the **congruence generated by $R$** is
>
> $$
> \operatorname{Cg}_{\mathbf{A}}(R) := \bigcap \{\, \theta \in \operatorname{Con}(\mathbf{A}) : R \subseteq \theta \,\},
> $$
>
> the least congruence containing $R$ (well-defined since intersections of congruences are congruences). Bottom-up, $\operatorname{Cg}_{\mathbf{A}}(R)$ is obtained by closing $R \cup R^{-1} \cup \Delta_A$ under transitivity and under simultaneous application of each $f^{\mathbf{A}}$, with stabilization at stage $\omega$ in the finitary setting. The derivational description for syntax algebras appears as Theorem 18.3.

Compatibility is precisely the condition that quotients require (Warning 2.13): it says the relation cannot distinguish elements that the operations are about to merge. Equivalently, congruences are the equivalence relations closed under all **contexts** — replacing equals by equals inside any syntactic surrounding preserves the relation — a reformulation proved in Chapter 15 (Proposition 15.9). No congruence-lattice theory is developed.

#### 2.2.3. Kernel Congruences

> [!proposition] Proposition 2.11: Kernels are congruences
> For every homomorphism $h : \mathbf{A} \to \mathbf{B}$, the kernel $\ker h$ is a congruence on $\mathbf{A}$.

> [!proof-sketch] Proof Sketch 2.11
> $\ker h$ is an equivalence relation since equality in $B$ is one. For compatibility, if $h(a_i) = h(b_i)$ for all $i$, the preservation equation gives $h\big(f^{\mathbf{A}}(\vec{a})\big) = f^{\mathbf{B}}\big(h(a_1),\dots,h(a_n)\big) = f^{\mathbf{B}}\big(h(b_1),\dots,h(b_n)\big) = h\big(f^{\mathbf{A}}(\vec{b})\big)$.

In particular, for every valuation $g$ the evaluation kernel $\ker(\operatorname{ev}_g)$ is a congruence on the term algebra (Theorem 17.8): semantic collapse is always operation-compatible, never an arbitrary equivalence. This single fact is what makes the quotient description of generated algebras possible.

### 2.3. Quotients and First Isomorphism

#### 2.3.1. Quotient Algebra

> [!definition] Definition 2.12: Quotient algebra
> Let $\theta \in \operatorname{Con}(\mathbf{A})$. The **quotient algebra** $\mathbf{A}/\theta$ has carrier $A/\theta := \{[a]_\theta : a \in A\}$ and operations defined on representatives:
>
> $$
> f^{\mathbf{A}/\theta}\big([a_1]_\theta, \dots, [a_n]_\theta\big) := \big[\, f^{\mathbf{A}}(a_1, \dots, a_n) \,\big]_\theta \qquad (f \in \Omega_n).
> $$
>
> **Well-definedness**: if $[a_i]_\theta = [b_i]_\theta$ for all $i$, then compatibility of $\theta$ gives $\big[f^{\mathbf{A}}(\vec{a})\big]_\theta = \big[f^{\mathbf{A}}(\vec{b})\big]_\theta$; the right side is therefore independent of the chosen representatives. Compatibility is also necessary: well-definedness of all the displayed operations implies $\theta$ is a congruence.

> [!warning] Warning 2.13: Arbitrary equivalence relations do not suffice
> For a mere equivalence relation $\theta$, the representative formula of Definition 2.12 generally assigns different classes to different representatives of the same input, and no algebra structure on $A/\theta$ makes the projection a homomorphism. Compatibility is exactly the well-definedness condition. This is the prototype of every later **descent** condition: quotient recursion (Proposition 18.6), quotient evaluation (Theorem 18.8), and quotient substitution (Theorem 18.10) each impose a kernel-containment hypothesis whose role is identical to compatibility here.

#### 2.3.2. Quotient Projection

> [!definition] Definition 2.14: Canonical projection
> For $\theta \in \operatorname{Con}(\mathbf{A})$, the **quotient projection** (canonical surjection) is
>
> $$
> \operatorname{nat}_\theta : \mathbf{A} \to \mathbf{A}/\theta, \qquad \operatorname{nat}_\theta(a) := [a]_\theta.
> $$
>
> It is a surjective homomorphism with $\ker(\operatorname{nat}_\theta) = \theta$.

When $\mathbf{A}$ is a syntax algebra, $\operatorname{nat}_\theta$ is the basic **syntax-to-classes** map: it carries a raw term to its identification class, and is the central object of Chapter 18 (quotient syntax).

> [!theorem] Theorem 2.15: Universal property of the quotient
> Let $\theta \in \operatorname{Con}(\mathbf{A})$ and let $h : \mathbf{A} \to \mathbf{B}$ be a homomorphism with $\theta \subseteq \ker h$. Then there is a **unique** homomorphism $\bar{h} : \mathbf{A}/\theta \to \mathbf{B}$ with
>
> $$
> \bar{h} \circ \operatorname{nat}_\theta = h, \qquad \bar{h}\big([a]_\theta\big) = h(a).
> $$
>
> The hypothesis $\theta \subseteq \ker h$ is exactly the well-definedness of $\bar{h}$ on classes.

> [!proof-sketch] Proof Sketch 2.15
> If $[a]_\theta = [a']_\theta$ then $(a,a') \in \theta \subseteq \ker h$, so $h(a) = h(a')$; hence $[a]_\theta \mapsto h(a)$ is a function. It is homomorphic because $h$ and $\operatorname{nat}_\theta$ are and $\operatorname{nat}_\theta$ is surjective; uniqueness holds because the value on every class is forced by surjectivity of $\operatorname{nat}_\theta$.

#### 2.3.3. First Isomorphism Theorem

> [!theorem] Theorem 2.16: First Isomorphism Theorem
> Let $h : \mathbf{A} \to \mathbf{B}$ be a homomorphism of $\Omega$-algebras. Then $\ker h \in \operatorname{Con}(\mathbf{A})$, $\operatorname{im}(h) \leq \mathbf{B}$, and there is a **unique** isomorphism
>
> $$
> \bar{h} : \mathbf{A}/\ker h \ \xrightarrow{\ \cong\ }\ \operatorname{im}(h), \qquad \bar{h}\big([a]_{\ker h}\big) = h(a),
> $$
>
> giving the canonical factorization of $h$ as surjection, isomorphism, inclusion:
>
> $$
> \mathbf{A} \ \twoheadrightarrow\ \mathbf{A}/\ker h \ \xrightarrow{\ \cong\ }\ \operatorname{im}(h) \ \hookrightarrow\ \mathbf{B}.
> $$

> [!proof-sketch] Proof Sketch 2.16
> $\ker h$ is a congruence (Proposition 2.11) and $\operatorname{im}(h)$ a subalgebra (Proposition 2.7). Apply Theorem 2.15 with $\theta = \ker h$ to obtain $\bar h$; it is surjective onto $\operatorname{im}(h)$ by construction and injective because $\bar h([a]) = \bar h([a'])$ means $(a,a') \in \ker h$, i.e. $[a] = [a']$. Uniqueness follows from the uniqueness clause of Theorem 2.15.

> [!remark] Remark 2.17: The factorization as master template
> The only form of the theorem used later is the instantiation $h = \operatorname{ev}_g : \mathbf{T}_{\Omega}(X) \to \mathbf{B}$: the image is the generated subalgebra $\langle g[X] \rangle_{\mathbf{B}}$, the kernel is the congruence of semantic identifications, and the factorization reads **every generated target algebra is a quotient of free syntax by the evaluation kernel** (Theorem 17.9). Freeness of the generated structure is exactly triviality of that kernel. The second and third isomorphism theorems are not needed and are omitted.

### 2.4. Examples

> [!example] Example 2.18: A generated subalgebra computed by stages
> Let $\mathbf{B} = (\mathbb{N}, +, 0)$ (monoid signature) and $S = \{2\}$. Construction 2.5 gives $S^{(0)} = \{2, 0\}$, $S^{(1)} = \{0, 2, 4\}$, $S^{(2)} = \{0, 2, 4, 6, 8\}$, and in the limit
>
> $$
> \langle \{2\} \rangle_{\mathbf{B}} = 2\mathbb{N} = \{0, 2, 4, 6, \dots\},
> $$
>
> the least subset containing $2$ and the constant $0$ and closed under $+$. Every element appears at a finite stage; the entry stage anticipates the construction rank of Definition 5.6.

> [!example] Example 2.19: Kernel, congruence, quotient, first isomorphism
> Let $h : (\mathbb{Z}, +, -, 0) \to (\mathbb{Z}/2\mathbb{Z}, +, -, 0)$ be the parity homomorphism. Then $\ker h = \{(a, b) : a \equiv b \ (\mathrm{mod}\ 2)\}$ is a congruence (Proposition 2.11): sums and negatives of congruent pairs remain congruent. The quotient $\mathbb{Z}/\ker h$ has two classes $[0], [1]$ with representative-wise operations (Definition 2.12), and Theorem 2.16 supplies the unique isomorphism $\mathbb{Z}/\ker h \cong \mathbb{Z}/2\mathbb{Z}$, $[a] \mapsto h(a)$. By contrast, the equivalence relation "same sign or both zero" on $\mathbb{Z}$ is **not** a congruence for $+$: the pairs $(1, 5)$ and $(-1, -1)$ are related componentwise, but the sums $0$ and $4$ are unrelated — so no quotient algebra exists for it (Warning 2.13).

---

# Part II — Abstract Free Syntax
## 3. Absolutely Free $\Omega$-Algebras

The free $\Omega$-algebra on a set of generators is defined here **abstractly**, by its universal mapping property, before any concrete carrier is exhibited. The order is deliberate: the UMP is the invariant content of "syntax," and trees, tuples, strings, and expressions are later recognized as realizations of it. Existence is deferred to Chapter 4 (canonical construction) and Chapter 5 (general construction criteria).

### 3.1. Generator Maps

#### 3.1.1. Generator Set

> [!definition] Definition 3.1: Generator set
> Fix a signature $\Omega$. A **generator set** is a set $X$ with $X \cap \Omega = \varnothing$. Elements of $X$ are called **generators** or **variables**; they are the freely variable atoms of syntax. $X$ is external to the signature: no arity is assigned to a generator, no algebra is required to interpret one, and no homomorphism is required to preserve one (Warning 1.4). In the application to first-order logic, $X$ is the set of individual variables of the language and $\Omega$ its function-symbol signature.

#### 3.1.2. Generator Insertion

> [!definition] Definition 3.2: Generator insertion
> Let $\mathbf{F}$ be an $\Omega$-algebra. A **generator insertion** for $X$ into $\mathbf{F}$ is a function
>
> $$
> \eta : X \to F
> $$
>
> designating, for each generator $x$, the element $\eta(x) \in F$ that represents it. Freeness (Definition 3.4) is a property of the **pair** $(\mathbf{F}, \eta)$, never of the algebra $\mathbf{F}$ alone: the same carrier can be free with respect to one insertion and not another, and all uniqueness statements below are relative to the insertion. The phrase "$\mathbf{F}$ is free on $X$" always presupposes a fixed $\eta$.

#### 3.1.3. Assignments into Algebras

> [!definition] Definition 3.3: Assignment
> Let $\mathbf{A}$ be an $\Omega$-algebra. An **assignment** (synonyms: **valuation**, **environment**) of $X$ in $\mathbf{A}$ is an arbitrary function
>
> $$
> g : X \to A.
> $$
>
> No preservation condition is imposed or meaningful: $X$ carries no operations. The entire mapping-theoretic content of freeness is that such structureless data extends canonically to structured data — a homomorphism out of $\mathbf{F}$.

### 3.2. Universal Mapping Property

#### 3.2.1. Existence of Extension

> [!definition] Definition 3.4: Free $\Omega$-algebra (UMP)
> A pair $(\mathbf{F}, \eta)$, with $\mathbf{F}$ an $\Omega$-algebra and $\eta : X \to F$ a generator insertion, is a **free $\Omega$-algebra on $X$** (synonym: **absolutely free**) if it satisfies the **universal mapping property**: for every $\Omega$-algebra $\mathbf{A}$ and every assignment $g : X \to A$ there exists a **unique** homomorphism
>
> $$
> \widehat{g} : \mathbf{F} \to \mathbf{A} \qquad \text{with} \qquad \widehat{g} \circ \eta = g.
> $$
>
> The homomorphism $\widehat{g}$ is the **homomorphic extension** of $g$ along $\eta$. Equivalently: for every $\mathbf{A}$, the restriction map
>
> $$
> \operatorname{Hom}_{\Omega}(\mathbf{F}, \mathbf{A}) \longrightarrow A^{X}, \qquad h \longmapsto h \circ \eta,
> $$
>
> is a bijection.

The **existence** half of the UMP is the assertion that every way of giving the generators semantic values extends to a semantic interpretation of *all* of syntax; it will be consumed as term evaluation (Chapter 17) and as substitution (Chapter 14).

#### 3.2.2. Uniqueness of Extension

The **uniqueness** half is the distinctive feature of freeness, and it is the half that does the work in every later argument. Uniqueness asserts that a homomorphism out of $\mathbf{F}$ is completely determined by its values on $\eta[X]$; consequently any two constructions that both extend the same generator data coincide, and recursively specified maps are not merely existent but **canonical**. Every coherence statement in this treatise — uniqueness of comparison maps, uniqueness of transfer isomorphisms, the substitution composition law, the evaluation–substitution compatibility — is an instance of two homomorphisms out of a free algebra agreeing on generators.

> [!lemma] Lemma 3.5: Rigidity over $X$
> Let $(\mathbf{F}, \eta)$ be free on $X$ and let $h, k : \mathbf{F} \to \mathbf{A}$ be homomorphisms with $h \circ \eta = k \circ \eta$. Then $h = k$. In particular the only endomorphism of $\mathbf{F}$ fixing the inserted generators is $\mathrm{id}_F$.

> [!proof-sketch] Proof Sketch 3.5
> Both $h$ and $k$ are homomorphic extensions of the common assignment $g := h \circ \eta$; the uniqueness clause of Definition 3.4 forces $h = k$. The endomorphism statement is the case $\mathbf{A} = \mathbf{F}$, $g = \eta$, for which $\mathrm{id}_F$ is one extension.

#### 3.2.3. Free Algebra as Abstract Object

The free algebra is *defined* by the UMP; no commitment is made at this stage to what its elements are. Concrete carriers (trees, tuples, strings, expressions) enter only as realizations in Part III, each certified by the criteria of Chapter 5. This abstraction is not pedantry: it is what makes "the term algebra" well-defined talk. All structure developed later — induction, recursion, substitution, contexts, clones, evaluation — depends only on the UMP and therefore applies verbatim to every realization.

> [!proposition] Proposition 3.6: Injectivity of the insertion
> Suppose some $\Omega$-algebra has at least two elements. If $(\mathbf{F}, \eta)$ is free on $X$, then $\eta$ is injective.

> [!proof-sketch] Proof Sketch 3.6
> Let $x \neq y$ in $X$ and pick $\mathbf{A}$ with $|A| \geq 2$ and an assignment $g$ with $g(x) \neq g(y)$. Then $\widehat{g}(\eta(x)) = g(x) \neq g(y) = \widehat{g}(\eta(y))$, so $\eta(x) \neq \eta(y)$.

### 3.3. Consequences of Freeness

#### 3.3.1. Generatedness

> [!proposition] Proposition 3.7: Free algebras are generated by their generators
> If $(\mathbf{F}, \eta)$ is free on $X$, then $\langle \eta[X] \rangle_{\mathbf{F}} = F$.

> [!proof-sketch] Proof Sketch 3.7
> Let $\mathbf{C} \leq \mathbf{F}$ be the subalgebra on $C := \langle \eta[X] \rangle_{\mathbf{F}}$ and let $\iota : \mathbf{C} \hookrightarrow \mathbf{F}$ be the inclusion. The corestriction $\eta' : X \to C$ of $\eta$ is an assignment into $\mathbf{C}$; its extension $\widehat{\eta'} : \mathbf{F} \to \mathbf{C}$ satisfies $\iota \circ \widehat{\eta'} \circ \eta = \eta$, so by Lemma 3.5, $\iota \circ \widehat{\eta'} = \mathrm{id}_{\mathbf{F}}$. Hence $\iota$ is surjective and $C = F$.

Generatedness is strictly weaker than freeness: it provides reachability of every element from the generators, but not uniqueness of the construction path. The comparison-map formulation (Chapter 5, Theorem 5.12) makes the gap quantitative: generatedness is surjectivity of the canonical comparison homomorphism out of the term algebra; freeness adds its injectivity.

#### 3.3.2. Uniqueness up to Unique Isomorphism

> [!theorem] Theorem 3.8: Uniqueness of the free algebra up to unique isomorphism over $X$
> Let $(\mathbf{F}, \eta)$ and $(\mathbf{F}', \eta')$ both be free $\Omega$-algebras on the same set $X$. Then there is a **unique** isomorphism $\varphi : \mathbf{F} \to \mathbf{F}'$ over $X$, i.e. with
>
> $$
> \varphi \circ \eta = \eta'.
> $$

> [!proof-sketch] Proof Sketch 3.8
> By the UMP of $(\mathbf{F}, \eta)$ applied to the assignment $\eta' : X \to F'$, obtain $\varphi := \widehat{\eta'} : \mathbf{F} \to \mathbf{F}'$ with $\varphi \circ \eta = \eta'$; symmetrically obtain $\psi : \mathbf{F}' \to \mathbf{F}$ with $\psi \circ \eta' = \eta$. Then $\psi \circ \varphi$ is an endomorphism of $\mathbf{F}$ fixing the generators, so $\psi \circ \varphi = \mathrm{id}_{\mathbf{F}}$ by Lemma 3.5, and symmetrically $\varphi \circ \psi = \mathrm{id}_{\mathbf{F}'}$. Uniqueness of $\varphi$ among over-$X$ homomorphisms is again Lemma 3.5.

> [!remark] Remark 3.9: Canonical, not arbitrary, isomorphism
> Theorem 3.8 delivers more than abstract isomorphy: between two free objects there is exactly **one** generator-preserving isomorphism, with no choices made. This canonicity is what licenses the transfer machinery of Chapter 11 — operations and proofs are transported along *the* isomorphism, so transported objects are well-defined. An isomorphism that merely exists (e.g. one permuting generators) would not suffice. Note also that Theorem 3.8 gives **uniqueness, not existence**; existence is the content of Theorem 4.6.

#### 3.3.3. Absolute Freeness versus Quotient Freeness

> [!remark] Remark 3.10: Absolutely free means no equations
> The algebras of Definition 3.4 are **absolutely** free: free in the class of *all* $\Omega$-algebras, with no equations imposed. Distinct formal combinations of generators remain distinct (unique readability, Theorem 4.7). Two weaker notions are deliberately deferred: (i) **quotient syntax** $\mathbf{T}_{\Omega}(X)/\theta$, syntax modulo a congruence of identifications, developed in Chapter 18; (ii) **relative freeness** — freeness within an equationally defined class, e.g. the free monoid — which arises from quotients by fully invariant congruences and is only touched upon (Definition 18.11, Warning 18.13). Birkhoff-style variety theory lies outside the scope of this note. When "free" appears unqualified below, it means absolutely free.

> [!example] Example 3.11: The free algebra on no generators
> Take $X = \varnothing$. A free algebra $(\mathbf{F}, \eta)$ on $\varnothing$ has the unique empty insertion, and the UMP reads: **for every $\Omega$-algebra $\mathbf{A}$ there is exactly one homomorphism $\mathbf{F} \to \mathbf{A}$** — freeness on no generators is initiality. Its canonical realization is the algebra of **ground terms** $T_{\Omega}(\varnothing)$ (terms built from constants alone; Definition 4.1 with empty clause (V)). Two degenerate regimes: if $\Omega_0 = \varnothing$ there are no ground terms and $\mathbf{F}$ is the empty algebra; if $\Omega_0 \neq \varnothing$, the ground-term algebra is nonempty and every algebra receives its canonical interpretation of ground terms through the unique homomorphism (Corollary 17.14).

> [!proposition] Proposition 3.12: Cardinality of free algebras
> Let $(\mathbf{F}, \eta)$ be free on $X$ and suppose $X \cup \Omega_0 \neq \varnothing$. Then
>
> $$
> |F| \;=\; \max\big(\, |X|,\ |\Omega|,\ \aleph_0 \,\big)
> $$
>
> provided $\Omega$ contains at least one symbol of positive arity; if all symbols are nullary, $|F| = |X| + |\Omega_0|$. In particular free algebras on finite data over finite signatures with a positive-arity symbol are countably infinite, and freeness is never realized by a finite algebra in that situation.

> [!proof-sketch] Proof Sketch 3.12
> Upper bound: each stage of Construction 5.4 has cardinality at most $\kappa := \max(|X|, |\Omega|, \aleph_0)$ (finite sequences over a $\kappa$-sized set), and there are countably many stages. Lower bound: with a positive-arity $f$, the terms $f(t, \dots, t)$ iterated on any atom give infinitely many distinct elements by unique readability (Theorem 4.7), and the atoms are pairwise distinct by Proposition 3.6 and Definition 5.8(D1) in the canonical realization.

---
## 4. The Canonical Term Algebra

This chapter constructs the canonical witness to the existence of free algebras: the term algebra $\mathbf{T}_{\Omega}(X)$. Its carrier is the least set closed under formal term formation; its operations are formal constructor applications; its freeness packages structural recursion. The chapter closes with the two structural principles — unique readability, and induction/recursion — that all concrete presentations must reproduce.

### 4.1. Formal Term Formation

#### 4.1.1. Variable Terms

> [!definition] Definition 4.1: Terms over $\Omega$ with variables $X$
> Fix a signature $\Omega$ and a generator set $X$ with $X \cap \Omega = \varnothing$. The set $T_{\Omega}(X)$ of **$\Omega$-terms over $X$** is the least set $T$ satisfying the three formation clauses
>
> $$
> \textbf{(V)} \quad X \subseteq T;
> $$
>
> $$
> \textbf{(C)} \quad \Omega_0 \subseteq T;
> $$
>
> $$
> \textbf{(O)} \quad \text{for all } n \geq 1,\ f \in \Omega_n,\ t_1, \dots, t_n \in T: \quad f(t_1, \dots, t_n) \in T.
> $$
>
> "Least" means: $T_{\Omega}(X) = \bigcap \{\, T : T \text{ satisfies (V), (C), (O)} \,\}$, an intersection over the closed subsets of any ambient set closed under the formation clauses. In all three clauses the displayed expressions denote values of **formal constructors**: in term position, $x$ denotes the *variable term of* $x$, $c$ the *constant term of* $c$, and $f(t_1, \dots, t_n)$ the compound term — and which set-theoretic objects these are is a representation choice constrained only by the freeness criteria of Chapter 5. The **official choice** adopted by this treatise is fixed in Construction 4.13 (prefix expressions over the term alphabet): there $x$ denotes the singleton sequence $(x)$, $c$ the singleton $(c)$, and $f(t_1, \dots, t_n)$ the concatenation $(f)^{\frown} t_1^{\frown} \cdots^{\frown} t_n$. Part III studies the alternatives as further presentations.

Clause (V) inserts the generators as **variable terms** — atomic syntax whose only content is its identity as a generator. Variables enter syntax by clause (V) alone; they are not nullary symbols, and the disjointness $X \cap \Omega = \varnothing$ keeps the two clauses from interacting.

#### 4.1.2. Nullary Terms

Clause (C) inserts each constant symbol $c \in \Omega_0$ as an atomic **constant term**, written $c$ rather than $c()$. A constant term and a variable term are both atomic (no immediate subterms), but their **formal origin** differs and remains visible: under any evaluation, a variable goes to its assigned value $g(x)$, whereas a constant goes to its forced interpretation $c^{\mathbf{B}}$ (Construction 17.3).

> [!warning] Warning 4.2: Atomic does not mean interchangeable
> Conflating clauses (V) and (C) — e.g. treating variables as "constants without interpretation" or adjoining $X$ to $\Omega_0$ — produces a different and unusable object: every homomorphism preserves nullary symbols, so the resulting algebra admits no nontrivial reassignment of the would-be generators and fails the UMP. The pair of base clauses must stay separated in every concrete presentation; the engine of Chapter 5 enforces this through its disjointness conditions.

#### 4.1.3. Compound Terms

Clause (O) produces **compound terms** by arity-correct constructor application: an $n$-ary symbol consumes exactly $n$ previously formed terms, in order. The **immediate subterms** of $f(t_1, \dots, t_n)$ are $t_1, \dots, t_n$; atomic terms have none. Arity-correctness is part of formation, not an afterthought: there is no term $f(t_1)$ for binary $f$. Unique decomposition of compound terms (Theorem 4.7) is the central structural fact about clause (O), and it is what every concrete presentation must verify.

### 4.2. Term Algebra Structure

#### 4.2.1. Carrier of Terms

The set $T_{\Omega}(X)$ is so far only a set of syntax objects. The next two items equip it with algebra structure and a generator insertion; the triple of data $(T_{\Omega}(X), \text{operations}, \eta_X)$ is what carries the universal property. The separation between carrier and structure is maintained notationally: $T_{\Omega}(X)$ is the carrier, $\mathbf{T}_{\Omega}(X)$ the algebra.

#### 4.2.2. Formal Operations

> [!construction] Construction 4.3: The term algebra $\mathbf{T}_{\Omega}(X)$
> Define an $\Omega$-algebra $\mathbf{T}_{\Omega}(X)$ with carrier $T_{\Omega}(X)$ and, for each $f \in \Omega_n$ with $n \geq 1$, the **formal operation**
>
> $$
> f^{\mathbf{T}}(t_1, \dots, t_n) := f(t_1, \dots, t_n),
> $$
>
> and for each $c \in \Omega_0$ the distinguished element $c^{\mathbf{T}} := c$. Totality of the operations is clauses (C) and (O) of Definition 4.1. The formal operation **records** its arguments inside a new syntactic object; it computes nothing. This is the syntax-side meaning of $f$ (Warning 1.9), to be contrasted with interpreted operations $f^{\mathbf{B}}$, which may merge distinct argument tuples.

#### 4.2.3. Generator Map

> [!construction] Construction 4.4: Insertion of variables
> The **canonical generator insertion** is
>
> $$
> \eta_X : X \to T_{\Omega}(X), \qquad \eta_X(x) := x \quad (\text{the variable term of } x),
> $$
>
> provided by clause (V); under the official coding of Construction 4.13 this is the singleton sequence $(x)$, so the insertion is injective but not a literal inclusion. The pair $(\mathbf{T}_{\Omega}(X), \eta_X)$ — algebra together with insertion — is the **canonical term algebra on $X$**, and it is this pair, not the bare algebra, that is asserted to be free.

> [!proposition] Proposition 4.5: Generation of the term algebra
> $\langle \eta_X[X] \rangle_{\mathbf{T}_{\Omega}(X)} = T_{\Omega}(X)$: the term algebra is generated by its inserted variables.

> [!proof-sketch] Proof Sketch 4.5
> The carrier of the generated subalgebra contains $X$ (clause V data), contains each constant (nullary closure), and is closed under all formal operations; hence it satisfies (V), (C), (O) and contains the least such set $T_{\Omega}(X)$. This is the algebraic content of "least set."

### 4.3. Freeness and Unique Readability

#### 4.3.1. Term Algebra Freeness

> [!theorem] Theorem 4.6: The term algebra is free on $X$
> $(\mathbf{T}_{\Omega}(X), \eta_X)$ is a free $\Omega$-algebra on $X$: for every $\Omega$-algebra $\mathbf{A}$ and every assignment $g : X \to A$ there is a unique homomorphism $\widehat{g} : \mathbf{T}_{\Omega}(X) \to \mathbf{A}$ with $\widehat{g} \circ \eta_X = g$, and $\widehat{g}$ is determined by the **recursive clauses**
>
> $$
> \widehat{g}(x) = g(x) \quad (x \in X), \qquad \widehat{g}(c) = c^{\mathbf{A}} \quad (c \in \Omega_0),
> $$
>
> $$
> \widehat{g}\big(f(t_1, \dots, t_n)\big) = f^{\mathbf{A}}\big(\widehat{g}(t_1), \dots, \widehat{g}(t_n)\big) \quad (f \in \Omega_n,\ n \geq 1).
> $$
>
> Consequently free $\Omega$-algebras exist on every generator set, and by Theorem 3.8 every free algebra on $X$ is isomorphic to $\mathbf{T}_{\Omega}(X)$ by a unique isomorphism over $X$.

> [!proof-sketch] Proof Sketch 4.6
> *Existence.* The displayed clauses are an instance of structural recursion, whose validity for $\mathbf{T}_{\Omega}(X)$ is established by the construction-engine theorem (Theorem 5.13) applied to the canonical constructor system, using generation (Proposition 4.5) for totality and unique readability (Theorem 4.7) for single-valuedness; the resulting function is a homomorphism by inspection of the clauses. *Uniqueness.* Any homomorphism $h$ with $h \circ \eta_X = g$ satisfies the same clauses (preservation equation), and two functions satisfying the clauses agree on every term by structural induction (Theorem 4.9). The two halves use exactly generation and unique decomposition, the two components of freeness isolated in Chapter 5.

Recursive evaluation and homomorphic extension are thus one mechanism viewed twice: the clauses of Theorem 4.6 *are* the definition of evaluation (Chapter 17), the definition of substitution when $\mathbf{A}$ is itself a term algebra (Chapter 14), and the existence half of structural recursion (Chapter 13). $\mathbf{T}_{\Omega}(X)$ is henceforth the **canonical syntax model**, the hub of all comparisons.

#### 4.3.2. Constructor Injectivity

> [!theorem] Theorem 4.7: Unique readability of terms
> In $\mathbf{T}_{\Omega}(X)$:
>
> 1. the sets $\eta_X[X]$ (variable terms), $\{ c^{\mathbf{T}} : c \in \Omega_0 \}$ (constant terms), and $\operatorname{im}(f^{\mathbf{T}})$ for each $f \in \Omega_n$, $n \geq 1$ (compound terms with outer symbol $f$), are pairwise disjoint and jointly exhaust $T_{\Omega}(X)$;
> 2. each formal operation is injective:
>
> $$
> f^{\mathbf{T}}(s_1, \dots, s_m) = g^{\mathbf{T}}(t_1, \dots, t_n) \;\Longrightarrow\; f = g,\ m = n,\ s_i = t_i \ (1 \leq i \leq n).
> $$
>
> Equivalently, every term is **exactly one** of: a unique variable, a unique constant, or $f(t_1, \dots, t_n)$ for a unique symbol $f$ and a unique tuple of immediate subterms. The outer constructor and the immediate subterms of a term are recoverable from the term.

> [!proof-sketch] Proof Sketch 4.7
> The statement is representation-sensitive only in appearance: any realization of the formation clauses satisfying the disjointness and injectivity conditions of Definition 5.8 has these properties (Theorem 5.11), and the canonical term algebra is such a realization by its official coding (Construction 4.13), where heads and lengths separate the three classes and unique splitting (Lemma 4.14) gives clause 2. The content is therefore delegated to the construction engine; what is recorded here is the *invariant* statement, which transfers along all isomorphisms over $X$ (Theorem 11.6).

> [!remark] Remark 4.8: Unique readability is the concrete face of freeness
> Unique readability is exactly what an arbitrary algebra lacks: interpreted operations need not be injective, and their ranges need not avoid each other or the generator values. The kernel of evaluation (Chapter 17) measures the failure of Theorem 4.7 in the image. The implications run both ways: a generated algebra whose internal constructors satisfy clause 1 and clause 2 is free on its generators (Theorem 17.10).

#### 4.3.3. Structural Induction and Recursion

> [!theorem] Theorem 4.9: Structural induction on terms
> Let $\Phi \subseteq T_{\Omega}(X)$ be a property of terms. If
>
> $$
> \textbf{(base-V)} \quad x \in \Phi \ \text{for all } x \in X; \qquad \textbf{(base-C)} \quad c \in \Phi \ \text{for all } c \in \Omega_0;
> $$
>
> $$
> \textbf{(step)} \quad t_1, \dots, t_n \in \Phi \implies f(t_1, \dots, t_n) \in \Phi \quad \text{for all } f \in \Omega_n,\ n \geq 1,
> $$
>
> then $\Phi = T_{\Omega}(X)$.

> [!proof-sketch] Proof Sketch 4.9
> The hypotheses say $\Phi$ satisfies the formation clauses (V), (C), (O); the least set $T_{\Omega}(X)$ is contained in every such set.

> [!theorem] Theorem 4.10: Structural recursion on terms
> Let $V$ be a set together with **recursion data**: $h_X : X \to V$, $h_C : \Omega_0 \to V$, and for each $f \in \Omega_n$ ($n \geq 1$) a function $h_f : V^{n} \to V$. Then there is a **unique** function $\Psi : T_{\Omega}(X) \to V$ with
>
> $$
> \Psi(x) = h_X(x), \qquad \Psi(c) = h_C(c), \qquad \Psi\big(f(t_1, \dots, t_n)\big) = h_f\big(\Psi(t_1), \dots, \Psi(t_n)\big).
> $$

> [!proof-sketch] Proof Sketch 4.10
> Equip $V$ with the $\Omega$-algebra structure $\mathbf{A}_V$ defined by $c^{\mathbf{A}_V} := h_C(c)$ and $f^{\mathbf{A}_V} := h_f$; then the required $\Psi$ is exactly the homomorphic extension $\widehat{h_X} : \mathbf{T}_{\Omega}(X) \to \mathbf{A}_V$ of Theorem 4.6, and conversely the clauses of Theorem 4.6 are the displayed equations. Recursion into a set and freeness are interdefinable.

Both principles are *consequences of term formation plus freeness*: induction expresses minimality of the carrier (generation), recursion expresses unique extension (the UMP read through Proof Sketch 4.10). Chapter 13 develops both systematically and transports them to all concrete presentations; Chapter 5 isolates the set-theoretic mechanism that proves them for arbitrary constructor systems.

### 4.4. Worked Example

> [!example] Example 4.11: Terms over the monoid signature
> Let $\Omega = \{\cdot, e\}$ with arities $2, 0$, and $X = \{x, y\}$, writing $\cdot$ infix with full parentheses for display. The atomic terms are $x$, $y$ (variables) and $e$ (constant). The terms of height $\leq 1$ are the $3$ atoms together with the $9$ compounds $(u \cdot v)$ for $u, v$ atoms. Unique readability (Theorem 4.7) keeps all of
>
> $$
> (x \cdot e), \qquad x, \qquad (e \cdot x), \qquad ((x \cdot y) \cdot e), \qquad (x \cdot (y \cdot e))
> $$
>
> pairwise **distinct** as terms: no unit law and no associativity is available in absolutely free syntax. The outer constructor of $((x \cdot y) \cdot e)$ is $\cdot$ with immediate subterms $(x \cdot y)$ and $e$; atoms have none. Under evaluation in $(\mathbb{N}, +, 0)$ with $g(x) = g(y) = 1$, the five displayed terms take values $1, 1, 1, 2, 2$ — the collapse recorded by the evaluation kernel (Example 17.11).

> [!example] Example 4.12: The successor term algebra
> For $\Omega = \{\mathsf{0}, \mathsf{s}\}$ (arities $0, 1$) and $X = \varnothing$, the ground terms are exactly $\mathsf{0}, \mathsf{s}(\mathsf{0}), \mathsf{s}(\mathsf{s}(\mathsf{0})), \dots$, one for each $k \in \mathbb{N}$, with no collisions (Theorem 4.7). The UMP on the empty generator set (Example 3.11) states: for every set $B$ with a point $b_0$ and a map $h : B \to B$ there is exactly one map $\mathbb{N}$-indexed by syntax with $\mathsf{0} \mapsto b_0$ and $\mathsf{s}(t) \mapsto h(\text{value of } t)$ — the iteration principle. The term algebra here is the initial algebra whose concrete avatar is $(\mathbb{N}, 0, +1)$ (Example 17.11(i)); Dedekind-style definition of arithmetic by recursion is the special case of Theorem 4.10 over this signature.

### 4.5. The Official Carrier

> [!construction] Construction 4.13: Official coding of the term algebra (prefix expressions)
> The **term alphabet** is
>
> $$
> \operatorname{Alph}_{\Omega}(X) := X \ \sqcup\ \coprod_{n \in \omega} \Omega_n,
> $$
>
> disjointness holding by the standing conventions ($X \cap \Omega = \varnothing$; the $\Omega_n$ pairwise disjoint), with **alphabet rank** $\rho(x) := 0$ for $x \in X$ and $\rho(f) := \operatorname{ar}(f)$ for $f \in \Omega$. The **ambient expression set** is
>
> $$
> B := \operatorname{Alph}_{\Omega}(X)^{<\omega},
> $$
>
> the set of length-aware finite sequences of alphabet symbols, with concatenation $u^{\frown} v$ and singleton sequences $(a)$. For each $f \in \Omega_n$ define the total **prefix constructor**
>
> $$
> F_f : B^{n} \to B, \qquad F_f(e_1, \dots, e_n) := (f)^{\frown} e_1^{\frown} \cdots^{\frown} e_n, \qquad F_c() := (c) \quad (c \in \Omega_0),
> $$
>
> and the **insertion** $\eta_X(x) := (x)$. **Officially define** the carrier as the generated closure: with the one-step operator $\Gamma_{\Omega}(Y) := Y \cup \bigcup_{n \in \omega} \bigcup_{f \in \Omega_n} F_f[Y^{n}]$ (the monotone operator of Remark 5.17 for the constructor system $\mathcal{K}_{\mathrm{pre}} := (B, \eta_X, (F_f)_f)$),
>
> $$
> T_0 := \eta_X[X] \cup \{\, (c) : c \in \Omega_0 \,\}, \qquad T_{m+1} := \Gamma_{\Omega}(T_m), \qquad T_{\Omega}(X) := \bigcup_{m < \omega} T_m,
> $$
>
> the least subset of $B$ containing the atomic singletons and closed under all prefix constructors (starting instead from $T_0 = \eta_X[X]$ alone merely delays the constants to stage $1$ through the nullary constructors and yields the same union). The algebra structure is by restriction, $f^{\mathbf{T}} := F_f \!\restriction T_{\Omega}(X)^{n}$, so that
>
> $$
> f^{\mathbf{T}}(t_1, \dots, t_n) = (f)^{\frown} t_1^{\frown} \cdots^{\frown} t_n, \qquad c^{\mathbf{T}} = (c), \qquad \eta_X(x) = (x).
> $$
>
> From here on, $T_{\Omega}(X)$ **denotes this set**, $f(t_1, \dots, t_n)$ is notation for the displayed concatenation, and a term is literally a finite symbol sequence in Polish (prefix) form; $\mathbf{T}_{\Omega}(X)$ is a genuine ZF object, and the pair $(\mathbf{T}_{\Omega}(X), \eta_X)$ — not the bare carrier, not the bare algebra — is what Theorem 4.6 asserts to be free.

> [!lemma] Lemma 4.14: Slot counter, prefix-freeness, unique splitting
> For $s = (a_0, \dots, a_{\ell - 1}) \in B$ define the **slot counter**
>
> $$
> q_s(j) := 1 + \sum_{i < j} \big( \rho(a_i) - 1 \big) \qquad (0 \leq j \leq \ell).
> $$
>
> Then:
>
> 1. every $t \in T_{\Omega}(X)$ of length $\ell$ satisfies $q_t(j) > 0$ for all $j < \ell$ and $q_t(\ell) = 0$;
> 2. **(prefix-freeness)** no proper nonempty initial segment of an element of $T_{\Omega}(X)$ lies in $T_{\Omega}(X)$;
> 3. **(unique splitting)** if $t_1^{\frown} \cdots^{\frown} t_n = s_1^{\frown} \cdots^{\frown} s_n$ with all $t_i, s_i \in T_{\Omega}(X)$, then $t_i = s_i$ for every $i$;
> 4. **(characterization)** conversely, every $s \in B$ satisfying the condition in clause 1 lies in $T_{\Omega}(X)$; the slot counter decides membership in the carrier inside the ambient expression set.

> [!proof-sketch] Proof Sketch 4.14
> (1) Induction on the construction stage: an atomic singleton has counter values $(1, 0)$; for $F_f(t_1, \dots, t_n)$ the head symbol moves the counter from $1$ to $n$, and each block $t_i$, by the induction hypothesis shifted by the running offset, stays positive internally and lowers the count by exactly $1$, so the counter is $n - i > 0$ after block $i < n$ and $0$ exactly at the end. (2) A proper nonempty initial segment ends with counter value $> 0$ by clause 1, violating the terminal condition. (3) Induction on $n$: the first block on each side ends at the first position where the counter returns to one less than its starting offset; by clauses 1 and 2 this boundary is the same on both sides, forcing $t_1 = s_1$; cancel and recurse. (4) Strong induction on $\ell$: the head $a_0$ fixes the case — if $\rho(a_0) = 0$ clause 1 forces $\ell = 1$ and $s$ is an atomic singleton; if $\rho(a_0) = n \geq 1$, the successive counter returns split the remainder into $n$ shorter segments each satisfying clause 1, each a term by induction, so $s = F_{a_0}(\cdots) \in T_{\Omega}(X)$. All inductions run on sequence length and stage; **no term-level recursion is presupposed**, so the lemma is available before Theorem 4.6 without circularity.

> [!remark] Remark 4.15: Why this choice, and what must be watched
> **(i) Concreteness and alignment.** Terms are literally finite symbol sequences — one data type, no nesting — assembled from exactly the finite-sequence and concatenation apparatus of the set-theoretic companion; the slot counter is an arithmetically checkable (indeed primitive-recursive) predicate, which makes the official carrier Gödel-arithmetization-ready. **(ii) The insertion is the wrapper.** Generators enter as singleton sequences $(x)$, never as raw elements, so an arbitrary generator set $X$ is safe with no further hypotheses; what is load-bearing is alphabet-level only: $X \cap \Omega = \varnothing$, and **one fixed arity per symbol** (Remark 1.2) — overloading makes $\rho$ ill-defined and destroys unique splitting. **(iii) Carrier-relative injectivity.** The prefix constructors are *not* injective on the ambient $B^{n}$: concatenation of arbitrary sequences splits many ways. Conditions (D1)–(D3), (I) of Definition 5.8 hold on the generated carrier: variables and constants are the length-$1$ terms, separated by their single entry; compounds have length $\geq 2$ and head symbol identifying the producing constructor and its arity; and injectivity on $T_{\Omega}(X)^{n}$ is Lemma 4.14(3). This realization is the standard illustration of why the engine demands its conditions only on $C_{\mathcal{K}}$, never on the ambient set. The destructors are boundary scans supplied by Lemma 4.14(4): read the head, then split at the counter returns. **(iv) Cost comparison.** Nested symbol-headed tuples $\langle f, t_1, \dots, t_n \rangle$ certify freeness by tuple projection with no lemma; the prefix realization pays one lemma (4.14) and buys flatness, textbook alignment, and arithmetizability. Fully tagged tuples (Chapter 8), Gödel codes, and labelled trees are equally legitimate official choices; all are free constructor systems, pairwise canonically isomorphic over $X$ (Theorem 11.10). The official status of the prefix realization is a **convention adopted after its freeness proof**, not a metaphysical privilege of strings. **(v) Neutrality.** Downstream of this section nothing consults the coding except through the destructor interface $(\operatorname{case}, \operatorname{root}, \operatorname{comp}_i)$ of Chapter 12, so replacing Construction 4.13 by any other free constructor system changes no statement and no proof. Relation to Part III: the hub is a *delimiter-free, fixed-arity Polish* string algebra; Chapter 9 develops the *delimited* string presentation, whose hygiene mechanism (parentheses, commas) is independent of arity bookkeeping; Proposition 10.2 is Lemma 4.14 in weight form; Chapter 8 develops the nested, fully tagged alternative.

---
## 5. Set-Theoretic Construction Engine for Freeness

This chapter isolates, once and for all, the set-theoretic mechanism by which a **candidate concrete carrier** (a data structure: expressions, trees, tuples, strings) is certified to realize the free algebra. The engine has three movements: a **generated closure** construction producing the carrier in finite stages; **free-generation criteria** (disjointness and injectivity of constructors) yielding unique decomposition; and the **comparison-map method**, which converts these two ingredients into surjectivity and injectivity of a canonical homomorphism from the term algebra. Every freeness theorem of Part III is an application of this chapter. The development parallels the general theory of generation and free generation by families of constructor relations on an ambient set; constructors here are total functions, the single-valued special case.

### 5.1. Constructor Systems

#### 5.1.1. Base Data

> [!definition] Definition 5.1: Constructor system
> Fix a signature $\Omega$ and generator set $X$. A **constructor system** for $(\Omega, X)$ is a triple
>
> $$
> \mathcal{K} = \big( U,\ \iota,\ (\Phi_f)_{f \in \Omega} \big)
> $$
>
> consisting of: an **ambient set** $U$; an **atom insertion** $\iota : X \to U$ designating which elements of $U$ represent the generators; and for each $f \in \Omega_n$ a **constructor map**
>
> $$
> \Phi_f : U^{n} \to U,
> $$
>
> total on $U^{n}$. For $c \in \Omega_0$, $\Phi_c$ is determined by the single element $\Phi_c() \in U$, the **constant representative** of $c$. The base data thus comprise three classes: generator representatives $\iota[X]$, constant representatives $\{\Phi_c() : c \in \Omega_0\}$, and constructor outputs.

#### 5.1.2. Constructor Maps

> [!remark] Remark 5.2: Relational provenance and totality
> In the general set-theoretic theory of inductive generation, a constructor is a relation $R \subseteq U^{k} \times U$, with **relational image notation** $R[\![ W^{k} ]\!] := \{ u : \exists \vec{w} \in W^{k},\ (\vec{w}, u) \in R \}$, and generation proceeds by closing a base set under all such images. A constructor *map* $\Phi_f$ is the special case in which $R$ is the graph of a total function — for every premise tuple, exactly one conclusion. Ordinary term syntax uses total, single-valued constructors exclusively; partial or multivalued constructors belong to relational generation and are outside the present scope. Totality on all of $U^{n}$ is a harmless normalization: only the restriction of $\Phi_f$ to the generated carrier (Definition 5.3) ever matters, and a map defined only on syntax can be extended arbitrarily outside it.

#### 5.1.3. Candidate Syntax Carrier

> [!definition] Definition 5.3: Generated carrier and candidate syntax algebra
> Let $\mathcal{K} = (U, \iota, (\Phi_f)_f)$ be a constructor system. The **generated carrier** of $\mathcal{K}$ is
>
> $$
> C_{\mathcal{K}} := \bigcap \big\{\, W \subseteq U \ :\ \iota[X] \subseteq W,\ \ \Phi_f\big[W^{n}\big] \subseteq W \ \text{for all } f \in \Omega_n,\ n \in \mathbb{N} \,\big\},
> $$
>
> the least subset of $U$ containing the generator representatives and closed under all constructor maps (the $n = 0$ clause puts each $\Phi_c()$ into $W$). The **candidate syntax algebra** is
>
> $$
> \mathbf{C}_{\mathcal{K}} := \big( C_{\mathcal{K}},\ (\Phi_f\!\restriction_{C_{\mathcal{K}}^{\,n}})_{f \in \Omega} \big)
> $$
>
> with generator map the corestriction $\iota : X \to C_{\mathcal{K}}$; closure of $C_{\mathcal{K}}$ makes the restricted operations well-defined, so $\mathbf{C}_{\mathcal{K}}$ is an $\Omega$-algebra generated by $\iota[X]$.

A defined data structure is thereby separated from a verified free algebra: every constructor system yields a *candidate*; only systems passing the criteria of §5.3 yield a *presentation* of free syntax. The verification obligations are exactly the disjointness and injectivity conditions below.

### 5.2. Generated Closure

#### 5.2.1. Stage Construction

> [!construction] Construction 5.4: Stages of a constructor system
> Define subsets $C^{(k)} \subseteq U$ by
>
> $$
> C^{(0)} := \iota[X] \cup \{\, \Phi_c() : c \in \Omega_0 \,\},
> $$
>
> $$
> C^{(k+1)} := C^{(k)} \cup \bigcup_{n \geq 1} \bigcup_{f \in \Omega_n} \Phi_f\big[ (C^{(k)})^{n} \big].
> $$
>
> The sequence is $\subseteq$-increasing, and since every constructor is finitary,
>
> $$
> C_{\mathcal{K}} = \bigcup_{k < \omega} C^{(k)}.
> $$

> [!proof-sketch] Proof Sketch 5.4
> The union is closed: arguments of a constructor application drawn from the union lie in a common stage (finitely many arguments, increasing stages), so the output lies in the next stage. Hence the union contains the least closed set $C_{\mathcal{K}}$. Conversely each $C^{(k)} \subseteq C_{\mathcal{K}}$ by induction on $k$, since $C_{\mathcal{K}}$ contains the base and is closed.

#### 5.2.2. Generatedness

> [!proposition] Proposition 5.5: Finite reachability
> Every element of $C_{\mathcal{K}}$ is obtained from atoms and constant representatives by finitely many constructor applications: explicitly, $c \in C_{\mathcal{K}}$ iff $c \in C^{(k)}$ for some $k < \omega$, and membership in $C^{(k)}$ is witnessed by a finite construction history of depth at most $k$. Consequently $\mathbf{C}_{\mathcal{K}}$ is generated by $\iota[X]$ in the sense of Definition 2.4, and any homomorphism into $\mathbf{C}_{\mathcal{K}}$ whose image contains $C^{(0)}$ and is closed under the restricted constructors is surjective.

> [!proof-sketch] Proof Sketch 5.5
> The first claim is Construction 5.4 read elementwise, by induction on the entry stage. Generatedness follows since $\langle \iota[X] \rangle_{\mathbf{C}_{\mathcal{K}}}$ is closed and contains the base, hence contains (and is contained in) $C_{\mathcal{K}}$. The surjectivity criterion restates minimality: a closed subset containing the base exhausts the carrier.

Generatedness delivers the **existence of representations** — every concrete syntactic object is reachable, so the comparison map of §5.4 will be surjective. It says nothing yet about uniqueness; stages can in general be reached along several construction paths.

#### 5.2.3. Finite Construction Rank

> [!definition] Definition 5.6: Construction rank
> For $c \in C_{\mathcal{K}}$, the **construction rank** is
>
> $$
> \operatorname{rk}(c) := \min \{\, k < \omega : c \in C^{(k)} \,\},
> $$
>
> well-defined by Proposition 5.5. Elements of rank $0$ are exactly the base elements; an element of rank $k + 1$ lies in $C^{(k+1)} \setminus C^{(k)}$ and is a constructor output with arguments in $C^{(k)}$.

> [!proposition] Proposition 5.7: Rank bound and rank identity
> For every $f \in \Omega_n$ ($n \geq 1$) and $c_1, \dots, c_n \in C_{\mathcal{K}}$,
>
> $$
> \operatorname{rk}\big(\Phi_f(c_1, \dots, c_n)\big) \;\leq\; 1 + \max_i \operatorname{rk}(c_i).
> $$
>
> If moreover $\mathcal{K}$ satisfies the free-generation conditions of Definition 5.8, then for constructor outputs not in the base,
>
> $$
> \operatorname{rk}\big(\Phi_f(c_1, \dots, c_n)\big) \;=\; 1 + \max_i \operatorname{rk}(c_i),
> $$
>
> and each argument has strictly smaller rank than the output. Rank is the well-founded measure on which all engine recursions and inductions run; no ordinal recursion beyond $\omega$ is required in the finitary setting.

> [!proof-sketch] Proof Sketch 5.7
> The bound: arguments lie in stage $N := \max_i \operatorname{rk}(c_i)$, so the output lies in $C^{(N+1)}$. The identity: if the output had rank $M + 1 \leq N$, it would equal some constructor output with arguments of rank $\leq M$; unique decomposition (Theorem 5.11) forces those arguments to be $c_1, \dots, c_n$ themselves, giving $\max_i \operatorname{rk}(c_i) \leq M < N$, a contradiction.

### 5.3. Free-Generation Criteria

#### 5.3.1. Disjointness Conditions

> [!definition] Definition 5.8: Free constructor system
> A constructor system $\mathcal{K} = (U, \iota, (\Phi_f)_f)$ is **free** if, writing $C := C_{\mathcal{K}}$, the following hold.
>
> **(D1) Atom faithfulness.** $\iota$ is injective, and $\iota(x) \neq \Phi_c()$ for all $x \in X$, $c \in \Omega_0$, and $\Phi_c() \neq \Phi_{c'}()$ for $c \neq c'$ in $\Omega_0$.
>
> **(D2) Base–output disjointness.** $\big(\iota[X] \cup \{\Phi_c() : c \in \Omega_0\}\big) \cap \Phi_f\big[C^{n}\big] = \varnothing$ for every $f \in \Omega_n$ with $n \geq 1$.
>
> **(D3) Range disjointness.** $\Phi_f\big[C^{m}\big] \cap \Phi_g\big[C^{n}\big] = \varnothing$ for all distinct $f \in \Omega_m$, $g \in \Omega_n$ with $m, n \geq 1$.
>
> **(I) Injectivity.** Each $\Phi_f$ with $\operatorname{ar}(f) = n \geq 1$ is injective on $C^{n}$.
>
> Conditions (D1)–(D3) say that the representation does not collide distinct atoms, atoms with outputs, or outputs of distinct constructors; condition (I) says each constructor **remembers its inputs**: the immediate components of an output are recoverable. All four conditions are required only on the generated carrier $C$, not on the ambient $U$.

> [!warning] Warning 5.9: Typical collision failures
> Each condition excludes a real failure mode. (D1) fails if two variables are encoded by the same object, or a variable by the same object as a constant. (D2) fails for "optimizing" encodings in which a constructor applied to certain arguments returns an atom (e.g. a string encoding where a unary symbol applied to a variable yields a one-character string also used for another variable). (D3) fails when two operation symbols share an output format (e.g. untagged pairs encoding both $f(t)$ and $g(t)$ as $(t)$). (I) fails for forgetful encodings, e.g. flattening to strings without delimiters on a non-fixed-arity signature (Warning 9.9), or any encoding with normalization built in (hash-consing that identifies $f(x, y)$ with $f(y, x)$, Chapter 10). A candidate system violating any condition still generates a carrier, but the carrier presents a **quotient** of syntax, not syntax.

#### 5.3.2. Injectivity Conditions

> [!lemma] Lemma 5.10: Case partition of the generated carrier
> Let $\mathcal{K}$ be a free constructor system. Then $C_{\mathcal{K}}$ is the disjoint union
>
> $$
> C_{\mathcal{K}} \;=\; \iota[X] \ \sqcup\ \{\, \Phi_c() : c \in \Omega_0 \,\} \ \sqcup\ \bigsqcup_{\substack{f \in \Omega_n \\ n \geq 1}} \Phi_f\big[ C_{\mathcal{K}}^{\,n} \big],
> $$
>
> i.e. every element belongs to exactly one of: the atoms, the constant representatives, or the output set of exactly one positive-arity constructor.

> [!proof-sketch] Proof Sketch 5.10
> Coverage: the right side contains the base and is closed under all constructors (an output of $\Phi_f$ lies in the displayed $f$-summand), hence contains the least closed set; conversely each summand consists of elements of $C_{\mathcal{K}}$. Disjointness is exactly (D1)–(D3).

#### 5.3.3. Unique Decomposition

> [!theorem] Theorem 5.11: Unique decomposition in a free constructor system
> Let $\mathcal{K}$ be a free constructor system. Then every $c \in C_{\mathcal{K}}$ satisfies **exactly one** of the following, with all data unique:
>
> $$
> c = \iota(x) \ \text{for a unique } x \in X; \qquad c = \Phi_{c_0}() \ \text{for a unique } c_0 \in \Omega_0;
> $$
>
> $$
> c = \Phi_f(c_1, \dots, c_n) \ \text{for a unique } f \in \Omega_n \ (n \geq 1) \ \text{and a unique tuple } (c_1, \dots, c_n) \in C_{\mathcal{K}}^{\,n}.
> $$
>
> In particular the **outer constructor** and the **immediate components** of every non-atomic element are well-defined functions of the element.

> [!proof-sketch] Proof Sketch 5.11
> The case trichotomy and uniqueness of the case is Lemma 5.10; uniqueness of $x$ and of $c_0$ within their cases is (D1). In the compound case, the producing symbol is unique by (D3), and for fixed $f$ the argument tuple is unique by injectivity (I). 

### 5.4. Comparison Map Method

#### 5.4.1. Defining the Comparison Map

> [!theorem] Theorem 5.12: Freeness criterion via the comparison map
> Let $\mathcal{K}$ be a constructor system for $(\Omega, X)$ with candidate algebra $(\mathbf{C}_{\mathcal{K}}, \iota)$, and let
>
> $$
> r_{\mathcal{K}} := \widehat{\iota} \, : \, \mathbf{T}_{\Omega}(X) \longrightarrow \mathbf{C}_{\mathcal{K}}, \qquad r_{\mathcal{K}} \circ \eta_X = \iota,
> $$
>
> be the **comparison map**: the unique homomorphism extending the atom insertion, supplied by the UMP of the term algebra (Theorem 4.6). Then:
>
> 1. $r_{\mathcal{K}}$ is always surjective (**generatedness**);
> 2. $r_{\mathcal{K}}$ is injective iff $\mathbf{C}_{\mathcal{K}}$ has the unique-decomposition property of Theorem 5.11; in particular if $\mathcal{K}$ is a free constructor system, $r_{\mathcal{K}}$ is injective;
> 3. consequently $(\mathbf{C}_{\mathcal{K}}, \iota)$ is a free $\Omega$-algebra on $X$ **iff** $r_{\mathcal{K}}$ is bijective **iff** $\mathcal{K}$ satisfies unique decomposition; in that case $r_{\mathcal{K}}$ is the unique isomorphism $\mathbf{T}_{\Omega}(X) \cong \mathbf{C}_{\mathcal{K}}$ over $X$.

> [!proof-sketch] Proof Sketch 5.12
> (1) $\operatorname{im}(r_{\mathcal{K}})$ is a subalgebra containing $\iota[X]$ and all constant representatives (Proposition 2.7), hence contains the least closed set $C_{\mathcal{K}}$ (Proposition 5.5). (2, $\Leftarrow$) By induction on the pair of terms using Theorem 4.7 on the source and Theorem 5.11 on the target: if $r_{\mathcal{K}}(s) = r_{\mathcal{K}}(t)$, the unique decompositions on the target force $s, t$ into the same case with the same outer symbol, and injectivity of the target constructors propagates equality to immediate subterms; structural induction concludes $s = t$. (2, $\Rightarrow$) If decomposition fails — a collision among atoms, constants, or outputs — the colliding elements are images of distinct terms, so $r_{\mathcal{K}}$ is not injective. (3) A bijective homomorphism is an isomorphism (Proposition 1.14); freeness transports along isomorphisms over $X$; uniqueness of the isomorphism is Theorem 3.8.

#### 5.4.2. Surjectivity by Generatedness

Clause 1 of Theorem 5.12 converts the stage construction into **representation existence**: every concrete object is the image of at least one formal term, namely any term tracking one of its construction histories. This half needs no hypotheses beyond the constructor-system format and is the precise sense in which "generated" means "everything is some term's value." The generated/free distinction of §0.3.2 is now located exactly at clause 2.

#### 5.4.3. Injectivity by Unique Decomposition

Clause 2 converts unique decomposition into **representation uniqueness**: no two formal terms denote the same concrete object. The engine therefore reduces every concrete freeness proof in Part III to two finite checklists — the disjointness conditions (D1)–(D3) and the injectivity condition (I) — after which Theorem 5.12 yields the canonical isomorphism with $\mathbf{T}_{\Omega}(X)$ and, through it, with every other presentation.

> [!theorem] Theorem 5.13: Structural recursion for free constructor systems
> Let $\mathcal{K}$ be a free constructor system with carrier $C := C_{\mathcal{K}}$, let $V$ be a set, and let recursion data be given: $h_X : X \to V$, $h_C : \Omega_0 \to V$, and $h_f : V^{n} \to V$ for each $f \in \Omega_n$, $n \geq 1$. Then there exists a **unique** function $\bar{h} : C \to V$ such that
>
> $$
> \bar{h}(\iota(x)) = h_X(x), \qquad \bar{h}(\Phi_c()) = h_C(c),
> $$
>
> $$
> \bar{h}\big(\Phi_f(c_1, \dots, c_n)\big) = h_f\big(\bar{h}(c_1), \dots, \bar{h}(c_n)\big) \qquad (f \in \Omega_n,\ n \geq 1,\ c_i \in C).
> $$

> [!proof-sketch] Proof Sketch 5.13
> *Existence.* Define $\bar{h}_k : C^{(k)} \to V$ by recursion on $k < \omega$: $\bar{h}_0$ by the base clauses (well-defined on $C^{(0)}$ by (D1)); $\bar{h}_{k+1}$ extends $\bar{h}_k$, assigning to each $c \in C^{(k+1)} \setminus C^{(k)}$ the value $h_f(\bar{h}_k(c_1), \dots, \bar{h}_k(c_n))$ for *the* decomposition $c = \Phi_f(\vec{c})$ supplied by Theorem 5.11, whose arguments lie in $C^{(k)}$ by the rank identity (Proposition 5.7). The family is compatible ($\bar{h}_{k+1}\!\restriction_{C^{(k)}} = \bar{h}_k$), so $\bar{h} := \bigcup_k \bar{h}_k$ is a function on $C$ satisfying the clauses. *Uniqueness.* The set $\{ c \in C : \bar{h}(c) = \bar{h}'(c) \}$ for two solutions contains the base and is closed under all constructors, hence equals $C$ by minimality (Proposition 5.5). Unique decomposition is indispensable for existence: without it, the recursive clause could assign conflicting values to one element along different decompositions.

> [!remark] Remark 5.14: Non-circularity and division of labor
> The engine is logically self-contained: Construction 5.4, Theorem 5.11, and Theorem 5.13 use only ZF set theory (stages, ranks, minimality), never the UMP of the term algebra. The freeness of $\mathbf{T}_{\Omega}(X)$ itself (Theorem 4.6) is obtained by exhibiting **one** free constructor system realizing the formation clauses — the official prefix coding of Construction 4.13, whose conditions (D1)–(D3), (I) are certified by the slot-counter lemma (Lemma 4.14) using only induction on sequences and stages — and reading existence/uniqueness of homomorphic extensions off Theorem 5.13 with algebra-valued data. Once the term algebra is in hand, all *other* candidate systems are certified by the comparison map (Theorem 5.12) rather than by re-running the recursion argument. Closure theory beyond what is used here (transfinite stages, non-finitary rules, fixed-point calculi) is deliberately not developed.

### 5.5. Consolidated Freeness Criteria

> [!theorem] Theorem 5.15: Equivalent formulations of freeness for a generated pair
> Let $(\mathbf{C}, \iota)$ be an $\Omega$-algebra with $\iota : X \to C$ such that $\iota[X]$ generates $\mathbf{C}$, and let $r : \mathbf{T}_{\Omega}(X) \to \mathbf{C}$ be the comparison map (necessarily surjective, Theorem 5.12). The following are equivalent:
>
> $$
> \textbf{(UMP)} \quad (\mathbf{C}, \iota) \ \text{satisfies the universal mapping property of Definition 3.4};
> $$
>
> $$
> \textbf{(REC)} \quad \text{every recursion data on } (X, \Omega) \ \text{determines a unique function out of } C;
> $$
>
> $$
> \textbf{(INJ)} \quad \text{the internal constructor system of } \mathbf{C} \ \text{satisfies (D1)–(D3) and (I) of Definition 5.8};
> $$
>
> $$
> \textbf{(UR)} \quad \text{unique decomposition holds in } \mathbf{C} \ \text{(the trichotomy of Theorem 5.11)};
> $$
>
> $$
> \textbf{(CMP)} \quad r \ \text{is injective}; \qquad \textbf{(KER)} \quad \ker r = \Delta.
> $$

> [!proof-sketch] Proof Sketch 5.15
> (INJ) $\Leftrightarrow$ (UR) is Lemma 5.10 with Theorem 5.11 and its converse reading; (UR) $\Leftrightarrow$ (CMP) is Theorem 5.12(2); (CMP) $\Leftrightarrow$ (KER) is Definition 2.8; (CMP) $\Rightarrow$ (UMP) transports freeness along the isomorphism $r$ (Proposition 1.14, Theorem 3.8); (UMP) $\Rightarrow$ (REC) is Proof Sketch 4.10 transferred; (REC) $\Rightarrow$ (CMP): recursion into $T_{\Omega}(X)$ with the formal-constructor data builds a left inverse of $r$. Each of (INJ), (UR), (REC) is one face of the injectivity that freeness adds to generatedness.

> [!example] Example 5.16: A constructor system failing injectivity
> Let $\Omega = \{f\}$ (binary), $X = \{x, y, z\}$, $U$ the set of strings over $X \cup \{f\}$, $\iota$ the one-character strings, and the **delimiter-free** constructor $\Phi_f(w_1, w_2) := w_1 \, f \, w_2$. The generated carrier contains the string $x\,f\,y\,f\,z$, which arises in two ways:
>
> $$
> \Phi_f\big(\Phi_f(x, y),\, z\big) \;=\; x\,f\,y\,f\,z \;=\; \Phi_f\big(x,\, \Phi_f(y, z)\big),
> $$
>
> so $\Phi_f$ is not injective on the carrier and condition (I) fails. Unique decomposition fails (two outer decompositions of one object), the comparison map identifies the distinct terms $f(f(x, y), z)$ and $f(x, f(y, z))$, and the candidate presents the quotient of syntax by an associativity-like congruence — not free syntax. Restoring delimiters (Construction 9.7) repairs (I); this is Warning 9.9 seen from the engine side.

> [!remark] Remark 5.17: Monotone-operator formulation and the relational generalization
> The generated carrier is the least fixed point of the monotone operator
>
> $$
> \Gamma_{\mathcal{K}}(W) \;:=\; \iota[X] \ \cup\ \bigcup_{f \in \Omega} \Phi_f\big[ W^{\operatorname{ar}(f)} \big] \qquad (W \subseteq U),
> $$
>
> on the power set of $U$: $C_{\mathcal{K}} = \bigcap \{ W : \Gamma_{\mathcal{K}}(W) \subseteq W \}$, and the stages of Construction 5.4 are the iterates $\Gamma_{\mathcal{K}}^{k}(\varnothing)$ up to the base. Finitarity of the constructors makes $\Gamma_{\mathcal{K}}$ finitely accessible, whence stabilization at $\omega$. The same operator format with **relations** $R \subseteq U^{k} \times U$ in place of function graphs yields relationally generated closures, where an element may have several derivations; there, freeness generalizes to *unique derivability*, the comparison map runs from a syntax of derivation trees, and the present chapter is recovered exactly when every rule is total and single-valued. That generalization — needed for proof systems rather than for term syntax — is left to the set-theoretic companion.

---

# Part III — Concrete Syntax Algebras
## 6. Recursive Term-Expression Presentation

The first concrete presentation regularizes ordinary mathematical practice: terms written as displayed expressions $f(t_1, \dots, t_n)$. The point of the chapter is to convert this informal notation into an actual algebra — with a precisely specified carrier, constructor operations, and equality — and to certify it by the engine of Chapter 5. The expression presentation is deliberately close to the canonical term algebra; what it adds is an explicit commitment about what the displayed objects *are*.

### 6.1. Expression Formation

#### 6.1.1. Atomic Expressions

> [!definition] Definition 6.1: Atomic expressions
> Fix $(\Omega, X)$ with $X \cap \Omega = \varnothing$, and fix an injective **display function** $d$ assigning to each $x \in X$ and each $c \in \Omega_0$ a distinguished object $d(x)$ resp. $d(c)$ (its **displayed form**), with all displayed forms pairwise distinct. The **atomic expressions** are the objects $d(x)$ ($x \in X$), the **variable expressions**, and $d(c)$ ($c \in \Omega_0$), the **constant expressions**.

Typography is thereby separated from syntax: the displayed form is *data about the presentation*, not part of the abstract term. Two typographically distinct display conventions yield distinct (canonically isomorphic) expression algebras. Expression equality is equality of the underlying objects, not visual similarity.

#### 6.1.2. Compound Expressions

> [!definition] Definition 6.2: Compound expression formation
> For each $f \in \Omega_n$ ($n \geq 1$), fix an injective **application format** $\operatorname{app}_f$ assigning to each $n$-tuple $(e_1, \dots, e_n)$ of objects a new object $\operatorname{app}_f(e_1, \dots, e_n)$, displayed as
>
> $$
> f(e_1, \dots, e_n),
> $$
>
> subject to the **format discipline**: the assignments $\operatorname{app}_f$ are injective, have pairwise disjoint ranges, and their ranges avoid all atomic expressions. Parentheses and separating commas in the displayed form are part of the presentation discipline that realizes this injectivity; they carry no algebraic content of their own.

#### 6.1.3. Expression Carrier

> [!definition] Definition 6.3: Expression carrier
> The set $\operatorname{Expr}_{\Omega}(X)$ of **term expressions** is the least set containing all atomic expressions and closed under all application formats:
>
> $$
> \operatorname{Expr}_{\Omega}(X) := C_{\mathcal{K}_{\mathrm{expr}}}, \qquad \mathcal{K}_{\mathrm{expr}} := \big( U,\ x \mapsto d(x),\ (\operatorname{app}_f)_f \big),
> $$
>
> the generated carrier of the indicated constructor system inside any ambient set $U$ closed under the formats (with $\operatorname{app}_c() := d(c)$ for $c \in \Omega_0$). Membership in $\operatorname{Expr}_{\Omega}(X)$ is a stage-by-stage matter (Construction 5.4), not a matter of informal recognizability of notation.

### 6.2. Expression Algebra

#### 6.2.1. Constructor Operations

> [!construction] Construction 6.4: The expression algebra
> Define $\mathbf{Expr}_{\Omega}(X)$ as the candidate syntax algebra of $\mathcal{K}_{\mathrm{expr}}$ (Definition 5.3): carrier $\operatorname{Expr}_{\Omega}(X)$, operations
>
> $$
> f^{\mathrm{expr}}(e_1, \dots, e_n) := \operatorname{app}_f(e_1, \dots, e_n), \qquad c^{\mathrm{expr}} := d(c),
> $$
>
> and generator insertion $\eta^{\mathrm{expr}}(x) := d(x)$. Operation application *is* expression construction; nothing is evaluated.

#### 6.2.2. Unique Decomposition

> [!proposition] Proposition 6.5: Unique decomposition of expressions
> $\mathcal{K}_{\mathrm{expr}}$ is a free constructor system: conditions (D1)–(D3) and (I) of Definition 5.8 hold, and hence every expression is exactly one of a unique variable expression, a unique constant expression, or $\operatorname{app}_f(e_1, \dots, e_n)$ for a unique $f$ and unique immediate subexpressions $e_1, \dots, e_n$.

> [!proof-sketch] Proof Sketch 6.5
> (D1) is injectivity and distinctness of the display function; (D2), (D3), (I) are exactly the format discipline of Definition 6.2. Theorem 5.11 then yields unique decomposition.

> [!warning] Warning 6.6: Ambiguous display is a presentation failure
> If the format discipline is dropped — e.g. parentheses omitted so that the displayed string $f(g(x), y)$ and a differently structured expression coincide as objects — then (I) or (D3) fails, decomposition becomes non-unique, and the "expression algebra" presents a proper quotient of syntax. Ambiguity is not an aesthetic defect but a mathematical one: it changes the presented object. The string chapter (Chapter 9) studies exactly which display conventions are safe.

#### 6.2.3. Freeness of Expression Syntax

> [!theorem] Theorem 6.7: Expression presentation theorem
> $(\mathbf{Expr}_{\Omega}(X), \eta^{\mathrm{expr}})$ is a free $\Omega$-algebra on $X$, and the comparison map
>
> $$
> r_{\mathrm{expr}} : \mathbf{T}_{\Omega}(X) \longrightarrow \mathbf{Expr}_{\Omega}(X)
> $$
>
> is the unique isomorphism over $X$. Term expressions are one concrete presentation of abstract syntax among several, with no privileged status beyond familiarity.

> [!proof-sketch] Proof Sketch 6.7
> Proposition 6.5 verifies the hypotheses of Theorem 5.12; clauses 1–3 of that theorem give surjectivity, injectivity, and canonicity of $r_{\mathrm{expr}}$.

### 6.3. Worked Example

> [!example] Example 6.8: Expressions over the monoid signature
> For $\Omega = \{\cdot, e\}$, $X = \{x, y\}$, take displayed forms $d(x) = x$, $d(y) = y$, $d(e) = e$ and the fully parenthesized infix format $\operatorname{app}_{\cdot}(e_1, e_2) = (e_1 \cdot e_2)$. Then $((x \cdot y) \cdot e)$ and $(x \cdot (y \cdot e))$ are formed at stage $2$ and are **distinct expressions**: their outer decompositions return the different immediate-subexpression pairs $\big((x \cdot y),\, e\big)$ and $\big(x,\, (y \cdot e)\big)$. The format discipline (injectivity of $\operatorname{app}_{\cdot}$, ranges disjoint from atoms) is exactly what blocks the collision of Example 5.16; deleting the parentheses from the format would reproduce it verbatim.

---

## 7. Tree Syntax Algebra

Trees are the presentation that makes **positions** explicit: every node of a term tree has an address, so subterm occurrences, depth, and replacement become set-theoretically exact. This chapter constructs the algebra of labelled, ranked, arity-correct trees, proves it free, and develops the local tree operations (subtrees, height, immediate components) that the occurrence-sensitive theory of Part V will transfer to all presentations.

### 7.1. Addressed Tree Domains

#### 7.1.1. Address Space

> [!notation] Notation 7.1: Addresses
> Let $\mathbb{N}_{>0} := \{1, 2, 3, \dots\}$. The **address space** is $\mathbb{N}_{>0}^{<\omega}$, the set of finite sequences of positive integers; the empty sequence $\varepsilon$ is the **root address**. For $p, q$ in the address space: $p \preceq q$ ($p$ is a **prefix**, or **ancestor address**, of $q$) iff $q = p \cdot r$ for some sequence $r$; $p \cdot i$ denotes $p$ extended by $i \in \mathbb{N}_{>0}$, the address of the **$i$-th child** of the node at $p$; $|p|$ is the length of $p$, its **depth**.

#### 7.1.2. Prefix-Closed Domains

> [!definition] Definition 7.2: Tree domain
> A **tree domain** is a finite set $D \subseteq \mathbb{N}_{>0}^{<\omega}$ such that
>
> $$
> \textbf{(prefix closure)} \quad p \preceq q \in D \implies p \in D;
> $$
>
> $$
> \textbf{(left-sibling closure)} \quad p \cdot (i+1) \in D \implies p \cdot i \in D.
> $$
>
> Every nonempty tree domain contains the root $\varepsilon$; the **children** of $p \in D$ are the addresses $p \cdot 1, \dots, p \cdot k \in D$ without gaps; a $p \in D$ with no children is a **leaf address**. A tree domain is a concrete set-theoretic object recording pure tree *shape*: nodes, ancestry, and ordered branching, with no labels.

#### 7.1.3. Ordered Children

The left-sibling closure clause makes the children of every node an initial segment $\{1, \dots, k\}$ of positive integers, i.e. **ordered input places**. This ordering is what matches tree shape to operation arity: the $i$-th child position of a node will carry the $i$-th argument of the operation symbol labelling that node. Unordered trees do not present term syntax for non-commutative signatures, since the constructor $f(s, t)$ must remain distinguishable from $f(t, s)$.

### 7.2. Labelled Ranked Trees

#### 7.2.1. Labels

> [!definition] Definition 7.3: Ranked label alphabet
> The **label alphabet** for $(\Omega, X)$ is the disjoint union $L := X \sqcup \Omega$, equipped with the **rank function** $\rho : L \to \mathbb{N}$ given by $\rho(x) := 0$ for $x \in X$ and $\rho(f) := \operatorname{ar}(f)$ for $f \in \Omega$. Labels are syntax: a leaf labelled $x$ carries the *generator* $x$, not any value of $x$.

#### 7.2.2. Arity Correctness

> [!definition] Definition 7.4: Arity-correct labelled tree
> An **arity-correct labelled tree** over $(\Omega, X)$ is a pair $\mathsf{t} = (D, \ell)$ with $D$ a nonempty tree domain and $\ell : D \to L$ a **labelling** such that for every $p \in D$,
>
> $$
> \big| \{\, i \in \mathbb{N}_{>0} : p \cdot i \in D \,\} \big| \;=\; \rho(\ell(p)) :
> $$
>
> every node has exactly as many children as the rank of its label. Hence leaves carry variables or constant symbols, and an internal node with $n$ children carries an $n$-ary symbol. The set of arity-correct labelled trees is $\operatorname{Tree}_{\Omega}(X)$. Trees violating the displayed condition (e.g. a binary symbol with three children) are **malformed** and are excluded from the carrier.

#### 7.2.3. Tree Equality

> [!definition] Definition 7.5: Tree equality
> Two trees are equal iff they have the same domain and the same labelling:
>
> $$
> (D, \ell) = (D', \ell') \quad :\Longleftrightarrow \quad D = D' \ \text{and} \ \ell(p) = \ell'(p) \ \text{for all } p \in D.
> $$
>
> Because domains are sets of addresses, this **addressed equality** is finer than mere structural isomorphism of abstract graphs and needs no quotienting: two structurally isomorphic trees over the same alphabet with the same root-to-leaf address structure are literally the same pair. Equality is decided recursively by comparing root labels and the (equal-length) lists of immediate subtrees, by Theorem 7.8.

### 7.3. Tree Algebra

#### 7.3.1. Leaf Constructors

> [!construction] Construction 7.6: Leaf and constant-node constructors
> For $x \in X$ define the **leaf tree** $\eta^{\mathrm{tree}}(x) := (\{\varepsilon\},\ \varepsilon \mapsto x)$; for $c \in \Omega_0$ define the **constant node** $c^{\mathrm{tree}} := (\{\varepsilon\},\ \varepsilon \mapsto c)$. Both are single-node trees; they differ in their label and hence are distinct objects ($X \cap \Omega = \varnothing$). The map $\eta^{\mathrm{tree}} : X \to \operatorname{Tree}_{\Omega}(X)$ is the generator insertion of the tree presentation.

#### 7.3.2. Node Constructors

> [!construction] Construction 7.7: Node constructor
> For $f \in \Omega_n$ ($n \geq 1$) and trees $\mathsf{t}_i = (D_i, \ell_i)$, define
>
> $$
> f^{\mathrm{tree}}(\mathsf{t}_1, \dots, \mathsf{t}_n) := (D, \ell), \qquad D := \{\varepsilon\} \cup \bigcup_{i=1}^{n} \{\, i \cdot p : p \in D_i \,\},
> $$
>
> $$
> \ell(\varepsilon) := f, \qquad \ell(i \cdot p) := \ell_i(p).
> $$
>
> The construction adds a fresh root labelled $f$ and grafts $\mathsf{t}_1, \dots, \mathsf{t}_n$ as the ordered immediate subtrees, re-addressing each $\mathsf{t}_i$ under prefix $i$. The result is a tree domain (prefix and left-sibling closure are inherited) and is arity-correct. The resulting algebra is the **tree algebra** $\mathbf{Tree}_{\Omega}(X)$.

#### 7.3.3. Freeness of Tree Syntax

> [!theorem] Theorem 7.8: Tree presentation theorem
> The constructor system $\mathcal{K}_{\mathrm{tree}} := (\operatorname{Tree}_{\Omega}(X),\ \eta^{\mathrm{tree}},\ (f^{\mathrm{tree}})_f)$ is free, with generated carrier all of $\operatorname{Tree}_{\Omega}(X)$; hence $(\mathbf{Tree}_{\Omega}(X), \eta^{\mathrm{tree}})$ is a free $\Omega$-algebra on $X$ and the comparison map
>
> $$
> r_{\mathrm{tree}} : \mathbf{T}_{\Omega}(X) \longrightarrow \mathbf{Tree}_{\Omega}(X)
> $$
>
> is the unique isomorphism over $X$.

> [!proof-sketch] Proof Sketch 7.8
> *Generatedness.* By induction on $|D|$: a tree with one node is a leaf or constant node; a larger tree has root label $f \in \Omega_n$, $n \geq 1$, and equals $f^{\mathrm{tree}}$ of its immediate subtrees, which have strictly smaller domains. *(D1)–(D3).* Single-node trees are separated by their labels; an output of $f^{\mathrm{tree}}$ ($n \geq 1$) has root label $f$ of positive rank, hence is neither atomic nor an output of $g^{\mathrm{tree}}$ for $g \neq f$ (the root label identifies the producing constructor). *(I).* From $(D, \ell)$ with root label $f$, the immediate subtrees are recovered as the re-addressed restrictions $\mathsf{t} \downarrow i$ (Definition 7.9); hence $f^{\mathrm{tree}}$ is injective. Theorem 5.12 concludes.

### 7.4. Local Tree Operations

#### 7.4.1. Subtrees

> [!definition] Definition 7.9: Subtree at an address
> For $\mathsf{t} = (D, \ell)$ and $p \in D$, the **subtree of $\mathsf{t}$ at $p$** is
>
> $$
> \mathsf{t} \downarrow p := (D_p, \ell_p), \qquad D_p := \{\, q : p \cdot q \in D \,\}, \qquad \ell_p(q) := \ell(p \cdot q).
> $$
>
> $D_p$ is a tree domain and $\mathsf{t} \downarrow p$ is arity-correct. The subtree at $\varepsilon$ is $\mathsf{t}$ itself; subtrees at $p \neq \varepsilon$ are **proper subtrees**. The subtree operation realizes concrete decomposition of syntax by *position*; substitution and replacement are deferred to Chapters 14–15.

#### 7.4.2. Height and Depth

> [!definition] Definition 7.10: Height
> The **height** of $\mathsf{t} = (D, \ell)$ is
>
> $$
> \operatorname{ht}(\mathsf{t}) := \max \{\, |p| : p \in D \,\},
> $$
>
> so single-node trees have height $0$ and
>
> $$
> \operatorname{ht}\big(f^{\mathrm{tree}}(\mathsf{t}_1, \dots, \mathsf{t}_n)\big) = 1 + \max_i \operatorname{ht}(\mathsf{t}_i).
> $$
>
> The **depth** of a node $p \in D$ is $|p|$. Height strictly decreases from a tree to its proper subtrees, so height is a well-founded complexity measure supporting induction and recursion; under $r_{\mathrm{tree}}$ it coincides with the construction rank of Definition 5.6 computed in the tree system.

#### 7.4.3. Immediate Components

> [!proposition] Proposition 7.11: Tree destructors
> Let $\mathsf{t} = (D, \ell)$ with $\ell(\varepsilon) = f \in \Omega_n$, $n \geq 1$. Then the **root symbol** $f$ and the **immediate components** $\mathsf{t} \downarrow 1, \dots, \mathsf{t} \downarrow n$ are recoverable from $\mathsf{t}$, and
>
> $$
> \mathsf{t} = f^{\mathrm{tree}}\big( \mathsf{t} \downarrow 1, \dots, \mathsf{t} \downarrow n \big).
> $$
>
> The pair of maps (root label, list of immediate subtrees) is the concrete witness of constructor injectivity for the tree presentation: trees come equipped with *effective destructors*.

> [!proof-sketch] Proof Sketch 7.11
> Unfold Construction 7.7 and Definition 7.9: re-addressing under prefix $i$ and restriction at $i$ are mutually inverse on domains and labels.

Destructors are presentation-level assets: trees expose them by address arithmetic, tuples by projection (Chapter 8), strings only through parsing (Chapter 9). Their transfer to arbitrary presentations is part of the transfer machinery (Construction 11.7).

### 7.5. Worked Example

> [!example] Example 7.12: A tree in full data
> Let $\Omega = \{f, g, c\}$ with arities $2, 1, 0$ and $X = \{x\}$. The term $f(g(x), c)$ is presented by the tree $\mathsf{t} = (D, \ell)$ with
>
> $$
> D = \{\varepsilon,\ 1,\ 1{\cdot}1,\ 2\}, \qquad \ell(\varepsilon) = f, \quad \ell(1) = g, \quad \ell(1{\cdot}1) = x, \quad \ell(2) = c.
> $$
>
> Arity correctness: $\varepsilon$ has children $1, 2$ (and $\rho(f) = 2$); node $1$ has the single child $1{\cdot}1$ ($\rho(g) = 1$); $1{\cdot}1$ and $2$ are leaves ($\rho(x) = \rho(c) = 0$). Subtrees: $\mathsf{t} \downarrow 1$ presents $g(x)$, $\mathsf{t} \downarrow 2$ presents $c$, $\mathsf{t} \downarrow 1{\cdot}1$ presents $x$. Height $\operatorname{ht}(\mathsf{t}) = 2$, realized at the leaf $1{\cdot}1$. Root symbol $f$ and the immediate components $(\mathsf{t} \downarrow 1, \mathsf{t} \downarrow 2)$ recover the producing constructor application (Proposition 7.11).

---
## 8. Tagged Tuple Syntax Algebra

The tuple presentation encodes terms as nested set-theoretic tuples carrying explicit **tags**. It is the presentation of choice for foundational purposes: every object is a pure set built from ordered pairs, all disjointness conditions are enforced mechanically by the tags, and the freeness verification is the shortest of all presentations. The official carrier of $\mathbf{T}_{\Omega}(X)$ (Construction 4.13) is a **flat** realization: Polish symbol sequences whose decomposition is recovered by boundary scanning (Lemma 4.14). This chapter develops the orthogonal **nested** realization, in which every constructor class carries an explicit tag and decomposition is coordinate projection rather than scanning — the certification needs no analogue of the slot-counter lemma; $r_{\mathrm{tup}}$ is the canonical isomorphism between the two schemes, and the tag pair is left generic because tag choice is exactly the degree of freedom implementation codings exercise.

### 8.1. Tuple Codes

#### 8.1.1. Variable Codes

> [!definition] Definition 8.1: Tags and variable codes
> Fix two distinct objects $\mathsf{var} \neq \mathsf{op}$ (the **tags**), chosen so that neither is an element of $X \cup \Omega$ (e.g. $\mathsf{var} := 0$, $\mathsf{op} := 1$ under standard numeral coding, adjusted if these collide with $X \cup \Omega$). The **variable code** of $x \in X$ is the ordered pair
>
> $$
> \ulcorner x \urcorner := (\mathsf{var},\, x).
> $$
>
> The tag $\mathsf{var}$ marks the constructor class; the second coordinate carries the identity of the generator. Distinct variables have distinct codes (pair equality), and no variable code is an operation code (tag inequality).

#### 8.1.2. Operation Codes

> [!definition] Definition 8.2: Operation codes
> For $f \in \Omega_n$ ($n \geq 1$) and objects $u_1, \dots, u_n$, the **operation code** is the triple
>
> $$
> \operatorname{code}_f(u_1, \dots, u_n) := \big(\mathsf{op},\, f,\, (u_1, \dots, u_n)\big),
> $$
>
> recording the tag, the operation symbol, and the ordered tuple of immediate subcodes. Symbol identity and arity are preserved by the second and third coordinates: equality of triples forces equality of tags, of symbols, and of argument tuples componentwise.

#### 8.1.3. Nullary Codes

> [!definition] Definition 8.3: Nullary codes
> For $c \in \Omega_0$, the **constant code** is the operation code with empty tuple,
>
> $$
> \ulcorner c \urcorner := (\mathsf{op},\, c,\, ()).
> $$
>
> Constant codes are tagged $\mathsf{op}$, variable codes $\mathsf{var}$; hence the constants/generators distinction of Warning 1.4 is hard-coded into the representation and cannot be erased by any further construction.

### 8.2. Tuple Algebra

#### 8.2.1. Carrier by Recursive Closure

> [!definition] Definition 8.4: Tuple carrier
> The set $\operatorname{Tup}_{\Omega}(X)$ of **tuple terms** is the generated carrier of the constructor system
>
> $$
> \mathcal{K}_{\mathrm{tup}} := \big( U,\ x \mapsto (\mathsf{var}, x),\ (\operatorname{code}_f)_{f \in \Omega} \big)
> $$
>
> inside any set $U$ containing the atomic codes and closed under the coding maps (such $U$ exists by ordinary set-theoretic closure, e.g. inside the cumulative hierarchy above $X \cup \Omega$): the least set containing all variable codes and constant codes and closed under each $\operatorname{code}_f$. The recursive-closure definition replaces informal "nested tuple" talk by an exact stage construction (Construction 5.4) with finite ranks.

#### 8.2.2. Constructor Operations

> [!construction] Construction 8.5: The tuple algebra
> $\mathbf{Tup}_{\Omega}(X)$ is the candidate syntax algebra of $\mathcal{K}_{\mathrm{tup}}$: carrier $\operatorname{Tup}_{\Omega}(X)$, operations
>
> $$
> f^{\mathrm{tup}}(u_1, \dots, u_n) := (\mathsf{op}, f, (u_1, \dots, u_n)), \qquad c^{\mathrm{tup}} := (\mathsf{op}, c, ()),
> $$
>
> and generator insertion $\eta^{\mathrm{tup}}(x) := (\mathsf{var}, x)$. Constructor behavior is completely explicit: applying an operation literally forms the displayed triple.

#### 8.2.3. Freeness of Tuple Syntax

> [!theorem] Theorem 8.6: Tuple presentation theorem
> $\mathcal{K}_{\mathrm{tup}}$ is a free constructor system; hence $(\mathbf{Tup}_{\Omega}(X), \eta^{\mathrm{tup}})$ is a free $\Omega$-algebra on $X$ and the comparison map
>
> $$
> r_{\mathrm{tup}} : \mathbf{T}_{\Omega}(X) \longrightarrow \mathbf{Tup}_{\Omega}(X)
> $$
>
> is the unique isomorphism over $X$.

> [!proof-sketch] Proof Sketch 8.6
> All four conditions of Definition 5.8 are immediate from the coding. (D1): pair equality and injectivity of the identity coordinates. (D2): variable codes are tagged $\mathsf{var}$, outputs of positive-arity coders are tagged $\mathsf{op}$ with nonempty third coordinate, while constant codes have empty third coordinate. (D3): the second coordinate of an output identifies the producing symbol. (I): equality of triples gives equality of argument tuples, hence of arguments. Theorem 5.12 concludes. Unique decomposition here is literally case analysis on the tag followed by projection.

### 8.3. Use of Tuple Syntax

#### 8.3.1. Set-Theoretic Coding

The tuple presentation demonstrates that term syntax requires no primitive notion of "symbol string" or "diagram": ordered pairs suffice. For formal construction proofs — existence of the term algebra inside ZF, absoluteness considerations, arithmetization — tuple syntax is the appropriate presentation, because its equality is pair equality and its decomposition is projection, both available without any parsing theory. Visual tree intuition is never invoked; the engine's conditions are checked by coordinate bookkeeping.

#### 8.3.2. Implementation Use

Tuple syntax is the mathematical idealization of **tagged-union / algebraic-data-type** representations: the tag is the variant discriminator, the symbol coordinate the constructor name, the tuple the field list. It is serialization-friendly (a nested tuple linearizes canonically) and supports constant-time outer-constructor inspection (read the tag and symbol) without search. Parsing concerns arise only when tuple syntax is flattened to strings, which is the subject of Chapter 9.

#### 8.3.3. Comparison with Trees

> [!remark] Remark 8.7: Trees versus tuples
> The tree and tuple presentations are canonically isomorphic over $X$ (compose $r_{\mathrm{tree}}^{-1}$ with $r_{\mathrm{tup}}$; Chapter 11), but they expose different machinery. Trees make **positions** first-class: a node is an address, occurrences are addresses, and replacement is address surgery. Tuples make **construction** first-class: the outermost layer displays its own decomposition, and structural recursion is projection-driven. Neither is "the" syntax; both realize the polynomial fixed-point shape
>
> $$
> P \;\cong\; X \ \sqcup\ \coprod_{f \in \Omega} P^{\operatorname{ar}(f)},
> $$
>
> trees implementing the coproduct by root labels and addresses, tuples by tags. Statements about syntax should be proven on $\mathbf{T}_{\Omega}(X)$ and transferred (Chapter 11); presentation-internal notions (address, tag) do not transfer and must not appear in invariant statements.

### 8.4. Worked Example

> [!example] Example 8.8: A term as a tagged tuple
> With $\Omega = \{f, g, c\}$ (arities $2, 1, 0$) and $X = \{x\}$, the term $f(g(x), c)$ has tuple code
>
> $$
> \Big(\mathsf{op},\, f,\, \big(\, (\mathsf{op},\, g,\, (\,(\mathsf{var},\, x)\,)),\ \ (\mathsf{op},\, c,\, ())\, \big)\Big).
> $$
>
> Case analysis is coordinate inspection: the first coordinate $\mathsf{op}$ and nonempty third coordinate show the code is compound; the second coordinate names the outer symbol $f$; the third coordinate projects to the two immediate subcodes, of which the second, $(\mathsf{op}, c, ())$, is recognized as a constant by its empty tuple, and the inner $(\mathsf{var}, x)$ as a variable by its tag. Every step of unique decomposition is a pair-projection — no parsing, no address arithmetic.

---

## 9. String Syntax Algebra

Strings are the input/output presentation: terms as finite sequences of symbols over an alphabet. Under Construction 4.13 the hub itself is a (delimiter-free, fixed-arity) Polish string algebra; this chapter develops the **delimited** encoding, whose hygiene mechanism — parentheses and commas — carries the parse independently of arity bookkeeping and models notation systems in which delimiters rather than fixed arities secure readability. Unlike trees and tuples, strings do not wear their decomposition on their sleeve — recovering structure from a string is *parsing*, and the freeness of string syntax is a theorem **conditional on hygiene assumptions** about the encoding. This chapter develops well-formed strings, flattening and parsing, unique readability, and the resulting presentation theorem, and fixes the parser/evaluator distinction.

### 9.1. String Alphabet and Formation

#### 9.1.1. Alphabet

> [!definition] Definition 9.1: Alphabet and strings
> The **alphabet** for $(\Omega, X)$ is the disjoint union
>
> $$
> \mathcal{A} := X \ \sqcup\ \Omega \ \sqcup\ \{\, \mathtt{(}\,,\ \mathtt{)}\,,\ \mathtt{,} \,\},
> $$
>
> with the three **delimiters** (left parenthesis, right parenthesis, comma) assumed distinct from all elements of $X \cup \Omega$ (**lexical disjointness**). A **string** is an element of $\mathcal{A}^{<\omega}$; concatenation is written by juxtaposition and the empty string is $\varepsilon$. Each variable and each symbol is a one-character string under the evident inclusion. Lexical disjointness is the alphabet-level disjointness condition; in implementations it corresponds to tokenization, which is presupposed, not developed.

#### 9.1.2. Well-Formed Strings

> [!definition] Definition 9.2: String encoding and well-formedness
> Define the **string encoding** $s : T_{\Omega}(X) \to \mathcal{A}^{<\omega}$ by structural recursion (Theorem 4.10):
>
> $$
> s(x) := x, \qquad s(c) := c \quad (c \in \Omega_0),
> $$
>
> $$
> s\big(f(t_1, \dots, t_n)\big) := f \, \mathtt{(} \, s(t_1) \, \mathtt{,} \, \cdots \, \mathtt{,} \, s(t_n) \, \mathtt{)} \qquad (n \geq 1).
> $$
>
> A string is **well-formed** iff it lies in $\operatorname{im}(s) =: W_{\Omega}(X)$. Only well-formed strings count as string syntax; arbitrary strings (e.g. $\mathtt{)}x\mathtt{,,}$) are not terms in any sense, and the grammar implicit in the recursion is part of the presentation.

#### 9.1.3. Hygiene Conditions

> [!definition] Definition 9.3: Hygiene conditions
> The **hygiene conditions** for the delimited encoding are: (i) lexical disjointness of variables, operation symbols, and delimiters (Definition 9.1); (ii) each alphabet element is a single, atomic character of strings — no element of $\mathcal{A}$ is a nontrivial concatenation of others; (iii) every symbol has a unique arity (Remark 1.2). Variant encodings (Chapter 10) replace (iii) or the delimiters by other devices; the role of hygiene in every variant is the same: to make the parse of a well-formed string recoverable, i.e. to secure the injectivity and disjointness conditions of Definition 5.8 for string constructors.

### 9.2. Flattening and Parsing

#### 9.2.1. Flattening

> [!construction] Construction 9.4: Flattening
> The **flattening map** is the string encoding read as a map out of any syntax presentation; canonically, $\operatorname{fl} := s \circ r_{\mathrm{tree}}^{-1} : \operatorname{Tree}_{\Omega}(X) \to W_{\Omega}(X)$, the preorder traversal of a tree emitting symbols and delimiters. Flattening is **representation output**: it converts structured syntax into a linear record. Its injectivity is *not* automatic; it is exactly what the hygiene conditions purchase (Theorem 9.6).

#### 9.2.2. Parsing

> [!definition] Definition 9.5: Parsing
> A **parser** for the encoding $s$ is a partial function
>
> $$
> \operatorname{pa} : \mathcal{A}^{<\omega} \rightharpoonup T_{\Omega}(X)
> $$
>
> with domain $W_{\Omega}(X)$ such that $\operatorname{pa}(s(t)) = t$ for every term $t$. Parsing is **partial by design**: malformed strings have no parse and are rejected. Parsing converts representations into syntax; it assigns no meaning. The existence of a (unique, total-on-$W$) parser is equivalent to injectivity of $s$ (Theorem 9.6); algorithmic aspects of computing $\operatorname{pa}$ are deferred (Chapter 10).

#### 9.2.3. Unique Readability

> [!theorem] Theorem 9.6: Unique readability of well-formed strings
> Under the hygiene conditions of Definition 9.3, the encoding $s : T_{\Omega}(X) \to \mathcal{A}^{<\omega}$ is injective; equivalently, flattening and parsing are mutually inverse bijections between $T_{\Omega}(X)$ and $W_{\Omega}(X)$, and every well-formed string has exactly one parse.

> [!proof-sketch] Proof Sketch 9.6
> By induction on term structure, using two auxiliary facts established by induction on string length: (a) every well-formed string has balanced parentheses, and no proper nonempty prefix of an encoded term is an encoded term (the prefix property, proved by tracking the parenthesis excess, which is $0$ exactly at the end); (b) the first character of $s(t)$ determines the case of $t$ — a variable, a constant, or an $n$-ary symbol followed by $\mathtt{(}$. Given $s(f(\vec{t}\,)) = s(g(\vec{u}))$, fact (b) forces $f = g$ and hence equal arities; the prefix property then splits the delimited argument lists identically, and the induction hypothesis gives $t_i = u_i$ componentwise.

### 9.3. String Algebra

#### 9.3.1. Constructor Operations on Strings

> [!construction] Construction 9.7: The string algebra
> Define operations on $W_{\Omega}(X)$ by **grammar-controlled concatenation**:
>
> $$
> f^{\mathrm{str}}(w_1, \dots, w_n) := f \, \mathtt{(} \, w_1 \, \mathtt{,} \, \cdots \, \mathtt{,} \, w_n \, \mathtt{)}, \qquad c^{\mathrm{str}} := c, \qquad \eta^{\mathrm{str}}(x) := x.
> $$
>
> Each operation prepends the symbol and re-delimits; outputs of well-formed inputs are well-formed (they are encodings of the corresponding compound terms), so the operations restrict to $W_{\Omega}(X)$ and yield the **string algebra** $\mathbf{Str}_{\Omega}(X)$. Raw concatenation without the delimiter discipline does **not** define operations on well-formed strings and is never used.

#### 9.3.2. Freeness of String Syntax

> [!theorem] Theorem 9.8: String presentation theorem
> Under the hygiene conditions, $(\mathbf{Str}_{\Omega}(X), \eta^{\mathrm{str}})$ is a free $\Omega$-algebra on $X$; the comparison map equals the string encoding, $r_{\mathrm{str}} = s : \mathbf{T}_{\Omega}(X) \xrightarrow{\ \cong\ } \mathbf{Str}_{\Omega}(X)$, and is the unique isomorphism over $X$.

> [!proof-sketch] Proof Sketch 9.8
> The comparison map extending $\eta^{\mathrm{str}}$ satisfies the recursion clauses defining $s$, hence equals $s$ by uniqueness of structural recursion (Theorem 4.10). Surjectivity onto $W_{\Omega}(X)$ holds by definition of well-formedness; injectivity is Theorem 9.6. Theorem 5.12(3) concludes. Equivalently one checks Definition 5.8 directly for $\mathcal{K}_{\mathrm{str}}$: the leading character separates the constructor classes ((D2), (D3)), and the prefix property gives (I).

> [!warning] Warning 9.9: Failure without hygiene
> If delimiters are dropped and arities are not fixed (overloaded symbols), injectivity of $s$ fails: distinct terms flatten to the same string, the string "algebra" presents a proper quotient of syntax, and *no* parser exists (the parse relation is multivalued). Ambiguity of a grammar is precisely failure of condition (I)/(D3) for the string constructor system, hence failure of the presentation, not a benign notational variance. Determinate variants without parentheses exist (Polish notation, Chapter 10) but trade delimiters for fixed-arity information; some hygiene assumption is always load-bearing.

#### 9.3.3. Parser versus Evaluator

> [!remark] Remark 9.10: The map taxonomy at the string boundary
> Three maps with distinct types meet at strings and must not be conflated:
>
> $$
> \operatorname{pa} : W_{\Omega}(X) \to T_{\Omega}(X) \quad \text{(parser: representation} \to \text{syntax)},
> $$
>
> $$
> \operatorname{ev}_g : T_{\Omega}(X) \to B \quad \text{(evaluator: syntax} \to \text{semantics, Chapter 17)},
> $$
>
> $$
> \operatorname{ev}_g \circ \operatorname{pa} : W_{\Omega}(X) \to B \quad \text{(interpreter: their composite)}.
> $$
>
> The parser is a presentation-level isomorphism (under hygiene) and loses nothing; the evaluator is a homomorphism that may collapse drastically. Properties of the composite (e.g. non-injectivity) must be attributed to the correct factor. In the first-order setting the same trichotomy recurs: reading a formula, versus evaluating a term, versus computing a truth value.

### 9.4. Worked Example

> [!example] Example 9.11: Delimited and Polish encodings
> With $\Omega = \{f, g, c\}$ (arities $2, 1, 0$), $X = \{x\}$, the term $f(g(x), c)$ has delimited encoding and Polish encoding
>
> $$
> s\big(f(g(x), c)\big) = f \mathtt{(} g \mathtt{(} x \mathtt{)} \mathtt{,} c \mathtt{)}, \qquad s'\big(f(g(x), c)\big) = f\, g\, x\, c.
> $$
>
> For the Polish string $f g x c$: weights are $1 - \rho$, i.e. $f \mapsto -1$, $g \mapsto 0$, $x \mapsto 1$, $c \mapsto 1$; total $= 1$ and every proper prefix has total $\leq 0$ ($-1, -1, 0$), confirming well-formedness (Proposition 10.2). If a second symbol $f'$ with the **same display letter** $f$ but arity $1$ were admitted (overloading), the string $f g x c$ would also parse as $f'(g(x))$ followed by a stray $c$ or as other splits — the parse relation becomes multivalued and the encoding ceases to be injective, the concrete face of Warning 9.9.

> [!lemma] Lemma 9.12: Balance and prefix property of the delimited encoding
> Define the **parenthesis balance** $\beta(w)$ of a string $w$ as the number of occurrences of $\mathtt{(}$ minus the number of occurrences of $\mathtt{)}$. Under the hygiene conditions: (i) every well-formed string $w$ has $\beta(w) = 0$, and every proper nonempty prefix $u$ of a well-formed string that ends inside the argument zone has $\beta(u) \geq 1$ when the prefix has consumed the opening parenthesis of the outermost compound; (ii) **prefix property**: no well-formed string is a proper prefix of another well-formed string; (iii) in the concatenation $s(t_1) \, \mathtt{,} \, \cdots \, \mathtt{,} \, s(t_n)$ the splitting commas of the outermost argument list are exactly the commas at balance $0$ relative to the list, so the argument segmentation is unique.

> [!proof-sketch] Proof Sketch 9.12
> (i) by structural induction: atoms have balance $0$; the compound clause adds one matched pair. (ii): a proper prefix of $s(f(\vec{t}\,))$ either stops before the closing parenthesis (balance $\geq 1$, but well-formed strings have balance $0$) or is atomic while the whole string is compound (excluded by the leading character). (iii) follows from (i) applied to each argument. These three facts are the inductive core of Theorem 9.6 and are exactly what fails in the delimiter-free encoding of Example 5.16.

---

## 10. Additional and Implementation-Oriented Presentations

This chapter surveys further presentations — notation systems and machine representations — and fixes the conceptual boundary between a *mathematical presentation* of syntax (which must be free on $X$) and an *implementation* (which must specify an abstraction map to syntax and may deliberately not be free). No parsing algorithms or data-structure theory are developed; only the distinctions needed later are retained.

### 10.1. Prefix and Infix Systems

#### 10.1.1. Prefix Notation

> [!definition] Definition 10.1: Polish (pure prefix) encoding
> The **Polish encoding** over alphabet $X \sqcup \Omega$ (no delimiters) is defined by recursion:
>
> $$
> s'(x) := x, \qquad s'(c) := c, \qquad s'\big(f(t_1, \dots, t_n)\big) := f \, s'(t_1) \cdots s'(t_n).
> $$

> [!proposition] Proposition 10.2: Determinism of Polish notation under fixed arities
> If every symbol has a unique arity (no overloading) and lexical disjointness holds, then $s'$ is injective, and well-formedness is decided by a single left-to-right scan. Precisely, assign each character $a$ the **weight** $1 - \rho(a)$, where $\rho$ is the rank function of Definition 7.3; a nonempty string $w$ is well-formed iff its total weight equals $1$ while every proper nonempty prefix of $w$ has total weight $\leq 0$. The parse is then reconstructed deterministically, each symbol consuming the next $\rho(a)$ complete subterm encodings.

> [!proof-sketch] Proof Sketch 10.2
> The balance argument establishes the prefix property (no encoded term is a proper prefix of another); injectivity then follows by the induction of Theorem 9.6 with the leading symbol determining the case and the arity determining the number of arguments to read. If a symbol had two arities, the number of arguments to read would be undetermined and injectivity fails (failure mode of Warning 9.9). The weight criterion is the slot counter of Lemma 4.14 in additive form ($q_s(j) = 1 - \sum_{i<j}(1 - \rho(a_i))$), where it certifies the official hub itself.

#### 10.1.2. Fully Parenthesized Infix

For binary signatures, the **fully parenthesized infix** encoding $s''\big(f(t_1, t_2)\big) := \mathtt{(}\, s''(t_1) \, f \, s''(t_2) \,\mathtt{)}$ is injective under lexical disjointness: the parentheses encode the tree shape outright, each matched pair delimiting one compound subterm. It satisfies the hygiene conditions and presents free syntax exactly as Theorem 9.8.

#### 10.1.3. Bare Infix Notation

> [!warning] Warning 10.3: Bare infix is ambiguous without grammar data
> Bare infix $s(t_1)\, f\, s(t_2)$ without parentheses is not injective: $x \cdot y \cdot z$ is the image of two distinct terms. **Precedence and associativity conventions** are additional grammar data that restore injectivity on the strings they govern; they belong to the presentation layer, not to the algebra. In particular, an associativity *convention* ("read $x \cdot y \cdot z$ left-nested") must not be confused with an associativity *law* ($(x \cdot y) \cdot z \approx x \cdot (y \cdot z)$): the former chooses a parse among distinct terms, the latter is an equation identifying terms, which lives in quotient syntax (Chapter 18). Absolutely free syntax validates no laws.

### 10.2. DAG and Shared-Subterm Representations

#### 10.2.1. Term DAGs

> [!definition] Definition 10.4: Term DAG and unfolding
> A **term DAG** over $(\Omega, X)$ is a finite directed acyclic graph with ordered out-edges, each node labelled in $X \sqcup \Omega$ with out-degree equal to the label's rank, together with a designated root from which all nodes are reachable. The **unfolding** of a term DAG is the tree obtained by duplicating shared nodes along all paths from the root; it is a well-defined element of $\operatorname{Tree}_{\Omega}(X)$ by acyclicity and finiteness (every path terminates, so the unfolding is finite). A DAG **represents** the term corresponding to its unfolding.

DAGs are *compressed representations*: a subterm occurring $k$ times may be stored once with $k$ in-edges. The map DAG $\mapsto$ unfolding is many-to-one; sharing structure is representation data invisible to syntax.

#### 10.2.2. Sharing versus Occurrence

> [!warning] Warning 10.5: One shared node is not one occurrence
> In the unfolded tree, a subterm $s$ may **occur** at many addresses; in the DAG those occurrences may be one shared node. Occurrence-sensitive operations — counting occurrences, replacing *one* occurrence, tracking positions (Chapter 12) — are defined on syntax, i.e. on the unfolding, and a DAG implementation must simulate them (e.g. by path-copying); performing them naively on the shared node changes *all* occurrences simultaneously and computes a different syntactic operation. Formula-occurrence bookkeeping in first-order logic inherits exactly this distinction.

#### 10.2.3. Cyclic Graphs

> [!warning] Warning 10.6: Cycles leave finite term syntax
> A labelled graph with a cycle has no finite unfolding: it represents no element of $T_{\Omega}(X)$. Cyclic "terms" model **infinite regular trees**, the carrier of a different (final-coalgebra-style) construction with its own theory; that material is deferred entirely. The present treatise is finitary: all terms are finite, all stage constructions stabilize at $\omega$, all ranks are natural numbers.

### 10.3. Implementation versus Mathematical Presentation

#### 10.3.1. Representation Fidelity

> [!definition] Definition 10.7: Faithful representation, abstraction map
> Let $R$ be a set of machine representations. An **abstraction map** is a (possibly partial) surjection $\alpha : R \rightharpoonup T_{\Omega}(X)$ assigning to each valid representation the term it represents. The representation is **faithful** as a presentation iff $\alpha$ is a bijection on its domain commuting with constructors — equivalently, iff the induced constructor system is free (Definition 5.8). Otherwise $R$ is a legitimate *implementation* but not a *presentation*: equality of representations and equality of terms diverge, and only the $\alpha$-image carries algebraic meaning. A data-structure design is validated by specifying $\alpha$ and locating it in this dichotomy, never by assuming implementation equality is syntactic equality.

#### 10.3.2. Canonicalization

> [!remark] Remark 10.8: Hash-consing and normalization are implementation choices
> **Hash-consing** (maximal sharing: each term value stored once) makes the abstraction map injective on stored nodes and renders syntactic equality a pointer comparison; it is a DAG discipline, subject to Warning 10.5. **Normalizing** representations (e.g. storing arguments of a commutative symbol in sorted order) deliberately identify distinct terms: their abstraction maps are not injective, and what they faithfully present is a *quotient* of syntax by the normalization congruence (Chapter 18). Both are optimizations in the implementation layer; neither alters the mathematical syntax object, and proofs about syntax must not depend on them.

#### 10.3.3. Deferred Implementation Theory

Parsing algorithms (recursive descent, shift-reduce), complexity of equality testing, balanced representations, and serialization formats are outside scope. What this chapter retains for later use is exactly: (i) a representation is usable as syntax iff its constructor system is free; (ii) sharing and canonicalization live below the abstraction map; (iii) notational conventions are grammar data, not equations. With these distinctions fixed, the mathematical development proceeds entirely on the invariant object.

### 10.4. Worked Example

> [!example] Example 10.9: Precedence as grammar data
> Let $\Omega = \{+, \cdot\}$ (both binary) with bare infix display and the usual convention "$\cdot$ binds tighter than $+$, both associate to the left." The string $x + y \cdot z$ is assigned the unique parse $+(x, \cdot(y, z))$, and $x + y + z$ the parse $+(+(x, y), z)$. The convention is a function from convention-governed strings to terms — added grammar data restoring injectivity on its domain — and **not** an algebraic statement: the term $+(x, +(y, z))$ still exists, is distinct from $+(+(x, y), z)$, and is simply displayed differently (with explicit parentheses). Conventions select parses; equations identify terms; the two layers never interact in absolutely free syntax.

---

# Part IV — Transfer Between Concrete Syntax Algebras
## 11. Transfer of Structure Across Presentations

Part III produced four certified presentations of free syntax. This chapter organizes them into a single coherent system and proves the **master transfer theorem**: all correct presentations are connected by unique generator-preserving isomorphisms, all invariant constructions transport along them, and the choice of presentation is thereafter a matter of convenience. After this chapter, the treatise develops every syntax operation exactly once.

### 11.1. Presentation Data

#### 11.1.1. Concrete Presentation Triple

> [!definition] Definition 11.1: Presentation of free syntax
> A **presentation** of the free $\Omega$-algebra on $X$ is a triple
>
> $$
> \mathcal{P} = \big( \mathbf{P},\ \eta_P,\ r_P \big)
> $$
>
> where $\mathbf{P}$ is an $\Omega$-algebra, $\eta_P : X \to P$ a generator insertion such that $(\mathbf{P}, \eta_P)$ is free on $X$, and
>
> $$
> r_P : \mathbf{T}_{\Omega}(X) \xrightarrow{\ \cong\ } \mathbf{P}, \qquad r_P \circ \eta_X = \eta_P,
> $$
>
> the **representation map**: the unique isomorphism over $X$ supplied by Theorem 3.8 (equivalently, the comparison map of Theorem 5.12 when $\mathbf{P}$ arises from a free constructor system). The isomorphism is **part of the data**: a presentation is not merely an algebra that happens to be free, but an algebra together with its canonical identification with the hub. Informal identification of carriers ("a term *is* a string") is replaced by explicit reference to $r_P$.

The certified presentations of Part III are $\mathcal{P}_{\mathrm{expr}}, \mathcal{P}_{\mathrm{tree}}, \mathcal{P}_{\mathrm{tup}}, \mathcal{P}_{\mathrm{str}}$ with representation maps $r_{\mathrm{expr}}, r_{\mathrm{tree}}, r_{\mathrm{tup}}, r_{\mathrm{str}} = s$.

#### 11.1.2. Generator-Preserving Isomorphism

> [!proposition] Proposition 11.2: Unique isomorphism between presentations
> Let $\mathcal{P}, \mathcal{Q}$ be presentations of free syntax on the same $X$. Then there is exactly one isomorphism $\mathbf{P} \to \mathbf{Q}$ over $X$ (i.e. carrying $\eta_P(x)$ to $\eta_Q(x)$ for every $x$), namely $r_Q \circ r_P^{-1}$. An isomorphism not required to preserve generators need not be unique, and a generator-permuting isomorphism is useless for transfer.

> [!proof-sketch] Proof Sketch 11.2
> Both $\mathbf{P}$ and $\mathbf{Q}$ are free on $X$; Theorem 3.8 applied to the pair gives existence and uniqueness of the over-$X$ isomorphism. The displayed composite is over $X$ since each factor is; uniqueness identifies it with the isomorphism of Theorem 3.8.

#### 11.1.3. Presentation Diagram

> [!remark] Remark 11.3: Hub-and-spoke discipline
> All presentations are organized as spokes around the canonical term algebra:
>
> $$
> \mathbf{Expr}_{\Omega}(X) \ \xleftarrow{\ r_{\mathrm{expr}}\ } \ \mathbf{T}_{\Omega}(X) \ \xrightarrow{\ r_{\mathrm{tree}}\ } \ \mathbf{Tree}_{\Omega}(X), \qquad \mathbf{Tup}_{\Omega}(X) \ \xleftarrow{\ r_{\mathrm{tup}}\ } \ \mathbf{T}_{\Omega}(X) \ \xrightarrow{\ r_{\mathrm{str}}\ } \ \mathbf{Str}_{\Omega}(X),
> $$
>
> all maps being isomorphisms over $X$. The diagram controls the **direction** of every transfer: presentation-to-presentation maps are always *defined through the hub* (Construction 11.4), never by ad hoc recursion on the concrete carriers, so that coherence (compatibility of all composites) is automatic rather than a proof obligation.

### 11.2. Transfer Maps

#### 11.2.1. Definition by Conjugation

> [!construction] Construction 11.4: Transfer maps and their coherence
> For presentations $\mathcal{P}, \mathcal{Q}$, the **transfer map** is
>
> $$
> \tau_{P,Q} := r_Q \circ r_P^{-1} : \mathbf{P} \xrightarrow{\ \cong\ } \mathbf{Q},
> $$
>
> the unique isomorphism over $X$ (Proposition 11.2). The family $(\tau_{P,Q})$ is **coherent**:
>
> $$
> \tau_{P,P} = \mathrm{id}_{\mathbf{P}}, \qquad \tau_{Q,R} \circ \tau_{P,Q} = \tau_{P,R}, \qquad \tau_{Q,P} = \tau_{P,Q}^{-1},
> $$
>
> each identity holding by uniqueness of over-$X$ homomorphisms between free objects (Lemma 3.5). Transfer is canonical: no choices enter, and any diagram built from transfer maps commutes.

Concrete instances: $\tau_{\mathrm{tree}, \mathrm{str}} = s \circ r_{\mathrm{tree}}^{-1}$ is the flattening map of Construction 9.4, and $\tau_{\mathrm{str}, \mathrm{tree}} = r_{\mathrm{tree}} \circ \operatorname{pa}$ is parsing followed by tree building.

#### 11.2.2. Operation Transfer

> [!proposition] Proposition 11.5: Transfer commutes with constructors
> For all presentations $\mathcal{P}, \mathcal{Q}$, every $f \in \Omega_n$, and all $p_1, \dots, p_n \in P$,
>
> $$
> \tau_{P,Q}\big( f^{\mathbf{P}}(p_1, \dots, p_n) \big) \;=\; f^{\mathbf{Q}}\big( \tau_{P,Q}(p_1), \dots, \tau_{P,Q}(p_n) \big),
> $$
>
> and $\tau_{P,Q}(c^{\mathbf{P}}) = c^{\mathbf{Q}}$, $\tau_{P,Q}(\eta_P(x)) = \eta_Q(x)$. Building syntax and then transferring equals transferring and then building: transferred objects remain syntax-homomorphic images, and constructor expressions may be computed in whichever presentation is convenient.

> [!proof-sketch] Proof Sketch 11.5
> $\tau_{P,Q}$ is a homomorphism over $X$; the displayed equations are the preservation equations and the over-$X$ condition.

#### 11.2.3. Equality Transfer

> [!theorem] Theorem 11.6: Equality and invariant-statement transfer
> Let $\mathcal{P}, \mathcal{Q}$ be presentations. For all $p, p' \in P$:
>
> $$
> p = p' \quad \Longleftrightarrow \quad \tau_{P,Q}(p) = \tau_{P,Q}(p').
> $$
>
> More generally, every property or relation defined from the algebra structure and the generator insertion alone (a **generator-preserving invariant**: e.g. "is atomic," "has outer symbol $f$," "is an immediate subterm of," "has height $k$," unique readability itself) holds of elements of $\mathbf{P}$ iff it holds of their transfers in $\mathbf{Q}$. Properties referring to the internal encoding (string length, tuple tag, address set) are **not** invariant and do not transfer.

> [!proof-sketch] Proof Sketch 11.6
> Equality transfer is injectivity plus functionality of the bijection $\tau_{P,Q}$. For invariants: a structure-and-insertion–defined predicate is preserved by every isomorphism over $X$, by induction on its defining formula, since $\tau_{P,Q}$ preserves operations, constants, and generator representatives (Proposition 11.5). The non-transfer of encoding-level properties is witnessed by examples: the string $s(f(x,y))$ has length $6$ while the corresponding tree has no length.

Equality transfer licenses *translation* of statements, not *identification* of carriers: writing $\mathbf{Tree}_{\Omega}(X) = \mathbf{Str}_{\Omega}(X)$ is false, while "trees and strings correspond under the canonical isomorphism, hence we work with trees" is the correct and complete discipline. Identification without an explicit isomorphism invites precisely the encoding-level leaks excluded in Theorem 11.6.

### 11.3. Transfer of Syntax Machinery

#### 11.3.1. Destructor Transfer

> [!construction] Construction 11.7: Transport of destructors
> Let $\mathcal{P}$ be a presentation equipped with **destructors** — e.g. the tree presentation's root-symbol map and immediate-component maps (Proposition 7.11), jointly inverting the constructors per Theorem 5.11. For any presentation $\mathcal{Q}$, define destructors on $\mathbf{Q}$ by conjugation: the outer-symbol map of $\mathbf{Q}$ is $q \mapsto$ (outer symbol of $\tau_{Q,P}(q)$ in $\mathbf{P}$), and the $i$-th immediate component of $q$ is
>
> $$
> \operatorname{comp}_i^{\mathbf{Q}}(q) := \tau_{P,Q}\big( \operatorname{comp}_i^{\mathbf{P}}( \tau_{Q,P}(q) ) \big).
> $$
>
> The transported maps satisfy the same specification (they invert the $\mathbf{Q}$-constructors) because the specification is a generator-preserving invariant (Theorem 11.6). Existence of destructors is thus presentation-independent, while their *effectiveness* is not: for strings, the transported destructor routes through parsing, and a presentation given by a non-computable abstraction map has destructors only in the abstract sense.

#### 11.3.2. Induction and Recursion Transfer

> [!theorem] Theorem 11.8: Transfer of induction and recursion
> Let $\mathcal{P}$ be any presentation of free syntax on $X$. Then:
>
> 1. **(Induction.)** If $\Phi \subseteq P$ contains $\eta_P[X]$ and all $c^{\mathbf{P}}$ and is closed under all $f^{\mathbf{P}}$, then $\Phi = P$.
> 2. **(Recursion.)** For every set $V$ and recursion data $h_X : X \to V$, $h_C : \Omega_0 \to V$, $h_f : V^{n} \to V$, there is a unique $\Psi_{\mathbf{P}} : P \to V$ satisfying the recursion clauses with respect to $\eta_P$ and the $\mathbf{P}$-constructors; moreover $\Psi_{\mathbf{P}} = \Psi \circ \tau_{P,T}$, where $\Psi$ is the canonical solution on $T_{\Omega}(X)$ (Theorem 4.10) and $\tau_{P,T} = r_P^{-1}$.
>
> Hence neither induction nor recursion need be re-proved per presentation: both transport along the canonical isomorphisms, and a recursively defined map may be specified in one presentation and used in all.

> [!proof-sketch] Proof Sketch 11.8
> (1) $r_P^{-1}[\Phi] \subseteq T_{\Omega}(X)$ satisfies the hypotheses of Theorem 4.9 by Proposition 11.5, hence equals $T_{\Omega}(X)$; apply $r_P$. (2) $\Psi \circ r_P^{-1}$ satisfies the $\mathbf{P}$-clauses by Proposition 11.5; uniqueness follows from (1) applied to the agreement set of two solutions. For strings, clause (1) is usable only because parsing (Theorem 9.6) exposes the immediate subterms that the inductive step quantifies over — string induction presupposes unique readability.

#### 11.3.3. Evaluation Transfer

> [!proposition] Proposition 11.9: Evaluation from any presentation
> Let $\mathbf{B}$ be an $\Omega$-algebra and $g : X \to B$ an assignment. For each presentation $\mathcal{P}$, define
>
> $$
> \operatorname{ev}_g^{\mathbf{P}} := \operatorname{ev}_g \circ\, r_P^{-1} : \mathbf{P} \to \mathbf{B},
> $$
>
> where $\operatorname{ev}_g := \widehat{g}$ is the evaluation homomorphism on the hub (Theorem 4.6; Chapter 17). Then $\operatorname{ev}_g^{\mathbf{P}}$ is the unique homomorphism $\mathbf{P} \to \mathbf{B}$ with $\operatorname{ev}_g^{\mathbf{P}} \circ \eta_P = g$, and for all presentations $\mathcal{P}, \mathcal{Q}$,
>
> $$
> \operatorname{ev}_g^{\mathbf{Q}} \circ \tau_{P,Q} = \operatorname{ev}_g^{\mathbf{P}}.
> $$
>
> Evaluating a tree, a tuple, an expression, or a well-formed string yields the same element of $B$: semantic interpretation is representation-independent.

> [!proof-sketch] Proof Sketch 11.9
> $\operatorname{ev}_g^{\mathbf{P}}$ is a composite of homomorphisms extending $g$ along $\eta_P$; uniqueness is Lemma 3.5 (with $(\mathbf{P}, \eta_P)$ free). The compatibility square follows by canceling $r_P^{-1} = \tau_{Q,P} \circ r_Q^{-1}$ through coherence (Construction 11.4).

### 11.4. Master Transfer Theorem

#### 11.4.1. Statement

> [!theorem] Theorem 11.10: Master transfer theorem
> Let $\Omega$ be a signature and $X$ a generator set.
>
> 1. **(Uniqueness.)** Any two presentations of the free $\Omega$-algebra on $X$ are isomorphic by a unique isomorphism over $X$, and the family of all such isomorphisms is coherent (all composites compatible).
> 2. **(Transport.)** Every construction, operation, relation, or theorem formulated invariantly — i.e. in terms of the algebra structure and the generator insertion, without reference to internal encoding — transports along these isomorphisms: structural operations and destructors, induction and recursion principles and recursively defined maps, substitution and contexts (Chapters 14–15), syntactic clone structure (Chapter 16), evaluation, kernels, and quotients (Chapters 17–18).
> 3. **(Convenience.)** Consequently the choice of concrete presentation has no mathematical content: it affects only which machinery is *exposed* (positions for trees, coding for tuples, input/output for strings) and the computational cost of destructors.

> [!proof-sketch] Proof Sketch 11.10
> (1) is Proposition 11.2 and Construction 11.4. (2) is Theorem 11.6 (invariant statements), Construction 11.7 and Theorem 11.8 (machinery), and Proposition 11.9 (evaluation); each later chapter defines its operations on the hub by universal properties, so transport is the composite with $\tau$-maps and preservation is Proposition 11.5. (3) summarizes (1) and (2).

#### 11.4.2. Scope

> [!warning] Warning 11.11: What transfer does not cover
> The theorem applies to term expressions, trees, tagged tuples, and hygienic strings — to every system certified free by Theorem 5.12 — and to all invariantly formulated material. It does **not** apply to: malformed candidates (ambiguous strings, untagged tuples, normalizing representations), whose comparison maps are not injective and which present quotients rather than syntax; encoding-level properties (lengths, tags, addresses), which are not invariant; or computational properties (cost of parsing or equality), which are genuinely presentation-dependent. Claims transported outside this scope are unsound.

#### 11.4.3. Strategic Role

> [!remark] Remark 11.12: The pivot of the treatise
> Theorem 11.10 marks the transition from *building* presentations (Parts II–III) to *using* syntax (Parts V–VI). From this point on, definitions are stated once over $\mathbf{T}_{\Omega}(X)$ — or, when convenient, in the presentation that exposes the relevant structure (trees for occurrences, tuples for coding) — and invoked in all presentations through the transfer maps. The invariant viewpoint is not a stylistic preference: it is what guarantees that "substitution," "context," "evaluation," and "quotient" denote single well-defined operations on syntax rather than families of coincidentally similar manipulations of strings and trees.

### 11.5. Worked Example

> [!example] Example 11.13: One term across four presentations
> Let $\Omega = \{f, g, c\}$ (arities $2, 1, 0$), $X = \{x\}$, and let $t := f(g(x), c) \in T_{\Omega}(X)$. Its four canonical images are: the expression $f(g(x), c)$ (Example 6.8 format), the tree $(\{\varepsilon, 1, 1{\cdot}1, 2\}, \ell)$ of Example 7.12, the tuple of Example 8.8, and the string of Example 9.11. The transfer maps connect them through the hub; e.g. $\tau_{\mathrm{tree}, \mathrm{str}}$ is flattening, and computing the substitution $[x \mapsto g(c)]$ on the tree (graft a $g$-over-$c$ tree at address $1{\cdot}1$) then flattening gives the same string as parsing the string, substituting on the hub, and re-flattening:
>
> $$
> f \mathtt{(} g \mathtt{(} g \mathtt{(} c \mathtt{)} \mathtt{)} \mathtt{,} c \mathtt{)},
> $$
>
> as guaranteed by Proposition 14.6. No statement in this example mentions addresses, tags, or characters except inside a single presentation; everything cross-presentation routes through $\tau$-maps.

> [!construction] Construction 11.14: Transport of structure along a bijection
> Let $\mathbf{A}$ be an $\Omega$-algebra and $b : A \to Q$ a bijection onto a set $Q$. The **transported algebra** $b_{*}\mathbf{A}$ has carrier $Q$ and operations
>
> $$
> f^{b_{*}\mathbf{A}}(q_1, \dots, q_n) \;:=\; b\big( f^{\mathbf{A}}( b^{-1}(q_1), \dots, b^{-1}(q_n) ) \big),
> $$
>
> the unique structure making $b : \mathbf{A} \to b_{*}\mathbf{A}$ an isomorphism. Applied to $\mathbf{A} = \mathbf{T}_{\Omega}(X)$ and a coding bijection $b$, transport produces a presentation with $\eta := b \circ \eta_X$ and $r := b$; conversely every presentation arises this way up to isomorphism (compose $r_P$ with the identity). Transport is the degenerate, choice-laden cousin of transfer: it manufactures presentations from arbitrary bijections, whereas the transfer maps of Construction 11.4 are forced. It is recorded because implementation-level encodings (Chapter 10) are exactly transports along their abstraction bijections when faithful.

---

# Part V — Operations on Syntax Algebras
## 12. Structural Operations on Syntax

With transfer available, syntax operations are defined once, invariantly, and computed in whatever presentation is convenient. This chapter develops the **non-binding structural layer**: case analysis and decomposition, subterms and occurrence-sensitive positions, and complexity measures. These are the raw materials for induction and recursion (Chapter 13) and for the occurrence bookkeeping that first-order formula manipulation will require.

### 12.1. Decomposition Operations

#### 12.1.1. Outer Constructor

> [!definition] Definition 12.1: Case and outer symbol
> By unique readability (Theorem 4.7), every $t \in T_{\Omega}(X)$ falls under exactly one **case**:
>
> $$
> \operatorname{case}(t) \in \{\mathsf{var}\} \sqcup \{\mathsf{const}\} \sqcup \{\, \mathsf{op}_f : f \in \Omega_n,\ n \geq 1 \,\},
> $$
>
> according as $t = x$ for a (unique) variable, $t = c$ for a (unique) constant, or $t = f(t_1, \dots, t_n)$ for a (unique) $f$ and tuple. For compound $t$, the **outer symbol** $\operatorname{root}(t) := f$ is well-defined. Both maps are generator-preserving invariants, hence presentation-independent through transfer (Theorem 11.6); their concrete computation is label inspection on trees, tag-and-coordinate inspection on tuples, and leading-character inspection (after parse) on strings.

#### 12.1.2. Immediate Components

> [!definition] Definition 12.2: Immediate subterm destructors
> For compound $t = f(t_1, \dots, t_n)$, the **immediate components** are the uniquely determined arguments, retrieved by the destructors
>
> $$
> \operatorname{comp}_i(t) := t_i \qquad (1 \leq i \leq n = \operatorname{ar}(\operatorname{root}(t))),
> $$
>
> well-defined by constructor injectivity. Input places are **ordered**: $\operatorname{comp}_1(f(s,t)) = s$ regardless of any symmetry the symbol may later acquire semantically. Atomic terms have no components. The triple $(\operatorname{case}, \operatorname{root}, (\operatorname{comp}_i)_i)$ is the complete destructor kit; structural recursion (Theorem 13.4) is exactly recursion through this kit.

#### 12.1.3. Atomic versus Compound Syntax

The case partition separates **base cases** (variables, constants — recursion data $h_X$, $h_C$) from **recursive cases** (compound terms — clause functions $h_f$). The two kinds of atoms remain formally distinct even though both are leaves: under evaluation a variable consults the valuation while a constant consults the signature interpretation, and under substitution a variable is replaced while a constant is fixed (Theorem 14.4). Induction proofs must always carry both base cases; omitting the constant case is the syntactic analogue of Warning 2.2.

### 12.2. Subterms and Positions

#### 12.2.1. Subterm Relation

> [!definition] Definition 12.3: Subterm relations
> Define on $T_{\Omega}(X)$: $s \prec_1 t$ ($s$ is an **immediate subterm** of $t$) iff $t$ is compound and $s = \operatorname{comp}_i(t)$ for some $i$; the **proper subterm** relation $\prec$ is the transitive closure of $\prec_1$; the **reflexive subterm** relation $\preceq$ is $\prec \cup \Delta$. The set of subterms of $t$ is $\operatorname{Sub}(t) := \{ s : s \preceq t \}$, finite for every $t$.

> [!proposition] Proposition 12.4: Well-foundedness of the subterm relation
> $\prec$ is a well-founded strict partial order on $T_{\Omega}(X)$: there is no infinite descending chain $\cdots \prec t_2 \prec t_1 \prec t_0$, and every nonempty set of terms has a $\prec$-minimal element. Moreover $s \prec_1 t$ implies $\operatorname{ht}(s) < \operatorname{ht}(t)$.

> [!proof-sketch] Proof Sketch 12.4
> Height (Definition 12.8) strictly decreases along $\prec_1$ by its recursive clause; a descending chain would yield a strictly decreasing sequence in $\mathbb{N}$. Minimal elements exist by taking an element of minimal height. Well-foundedness is what licenses strong structural induction (Theorem 13.2).

#### 12.2.2. Occurrence-Sensitive Positions

> [!definition] Definition 12.5: Positions and occurrences
> The **position set** of $t$ is defined invariantly through the tree presentation: $\operatorname{Pos}(t) := D$, the tree domain of $r_{\mathrm{tree}}(\widetilde{t}\,)$ where $\widetilde{t}$ is the hub element corresponding to $t$; equivalently, by recursion,
>
> $$
> \operatorname{Pos}(x) = \operatorname{Pos}(c) = \{\varepsilon\}, \qquad \operatorname{Pos}\big(f(t_1, \dots, t_n)\big) = \{\varepsilon\} \cup \bigcup_{i=1}^{n} \{\, i \cdot p : p \in \operatorname{Pos}(t_i) \,\}.
> $$
>
> The **subterm at position** $p \in \operatorname{Pos}(t)$ is $t|_p$, defined by $t|_{\varepsilon} := t$ and $f(t_1, \dots, t_n)|_{i \cdot p} := t_i|_p$. An **occurrence** of $s$ in $t$ is a position $p$ with $t|_p = s$; the same subterm value may have many occurrences.

> [!warning] Warning 12.6: Term values versus occurrences
> The subterm *relation* (Definition 12.3) is occurrence-blind: $x \preceq f(x, x)$ holds once, while $x$ has two *occurrences* in $f(x,x)$, at positions $1$ and $2$. Operations on values (substitution, Chapter 14) act on all occurrences uniformly; operations on occurrences (single-occurrence replacement, rewriting at a position) require position data and are mediated by contexts (Chapter 15). Conflating the two produces wrong counts and wrong replacements; DAG sharing (Warning 10.5) is the implementation-level shadow of this distinction, and bound-variable bookkeeping in first-order logic is its successor.

#### 12.2.3. Replacement Preview

> [!definition] Definition 12.7: Replacement at a position
> For $t \in T_{\Omega}(X)$, $p \in \operatorname{Pos}(t)$, and $s \in T_{\Omega}(X)$, the **replacement** $t[s]_p$ ("$t$ with the subterm at $p$ replaced by $s$") is defined by recursion on $p$:
>
> $$
> t[s]_{\varepsilon} := s, \qquad f(t_1, \dots, t_n)[s]_{i \cdot p} := f\big(t_1, \dots, t_{i-1},\ t_i[s]_p,\ t_{i+1}, \dots, t_n\big).
> $$
>
> Replacement is an operation **on one occurrence**; its conceptual home is the theory of one-hole contexts (Proposition 15.7), where $t[s]_p = C_p[s]$ for the context obtained by hollowing position $p$. Equational rewriting and formula-level substitution are later organized through this operation.

### 12.3. Complexity Measures

#### 12.3.1. Height and Depth

> [!definition] Definition 12.8: Height
> The **height** $\operatorname{ht} : T_{\Omega}(X) \to \mathbb{N}$ is defined by structural recursion:
>
> $$
> \operatorname{ht}(x) := 0, \qquad \operatorname{ht}(c) := 0, \qquad \operatorname{ht}\big(f(t_1, \dots, t_n)\big) := 1 + \max_{1 \leq i \leq n} \operatorname{ht}(t_i).
> $$
>
> Under $r_{\mathrm{tree}}$, height agrees with the tree-presentation height (Definition 7.10) and with the construction rank of the canonical constructor system (Proposition 5.7). Induction on height is induction on $\mathbb{N}$ applied to a syntactic measure and is interchangeable with structural induction for properties monotone under the subterm relation.

#### 12.3.2. Symbol and Constructor Counts

> [!definition] Definition 12.9: Size
> The **size** $\operatorname{sz} : T_{\Omega}(X) \to \mathbb{N}$ counts all symbol occurrences:
>
> $$
> \operatorname{sz}(x) := 1, \qquad \operatorname{sz}(c) := 1, \qquad \operatorname{sz}\big(f(t_1, \dots, t_n)\big) := 1 + \sum_{i=1}^{n} \operatorname{sz}(t_i).
> $$
>
> Size equals $|\operatorname{Pos}(t)|$ and strictly decreases to immediate subterms, so it serves as a termination measure for recursions consuming syntax. Computational complexity of algorithms on terms is *not* treated; size and height are proof-theoretic measures only.

#### 12.3.3. Variable Occurrence Data

> [!definition] Definition 12.10: Variable set and occurrence count
> Define by structural recursion the **variable set** $\operatorname{var} : T_{\Omega}(X) \to \mathcal{P}(X)$,
>
> $$
> \operatorname{var}(x) := \{x\}, \qquad \operatorname{var}(c) := \varnothing, \qquad \operatorname{var}\big(f(t_1, \dots, t_n)\big) := \bigcup_{i=1}^{n} \operatorname{var}(t_i),
> $$
>
> and, for each $x \in X$, the **occurrence count** $\#_x(t) := |\{ p \in \operatorname{Pos}(t) : t|_p = x \}|$. Then $\operatorname{var}(t) = \{x : \#_x(t) \geq 1\}$ is finite, and a term with $\operatorname{var}(t) = \varnothing$ is a **ground term**. The set-of-variables datum governs which assignments affect a term's value (Lemma 17.4); the occurrence counts govern substitution growth and, later, first-order free-variable analysis, where the set/occurrence distinction becomes the free/bound occurrence distinction. The two data are deliberately kept separate.

### 12.4. Worked Example

> [!example] Example 12.11: Structural data of a term
> Let $\Omega = \{f, g, c\}$ (arities $2, 1, 0$), $X = \{x\}$, and $t := f\big(g(x),\, f(x, c)\big)$. Then:
>
> $$
> \operatorname{Pos}(t) = \{\varepsilon,\ 1,\ 1{\cdot}1,\ 2,\ 2{\cdot}1,\ 2{\cdot}2\}, \qquad \operatorname{sz}(t) = 6, \qquad \operatorname{ht}(t) = 2,
> $$
>
> $$
> \operatorname{var}(t) = \{x\}, \qquad \#_x(t) = 2 \ \ (\text{occurrences at } 1{\cdot}1 \text{ and } 2{\cdot}1).
> $$
>
> Subterms: $\operatorname{Sub}(t) = \{t,\ g(x),\ f(x, c),\ x,\ c\}$ — five **values**, six **positions**: the value $x$ occurs twice. The case data: $\operatorname{root}(t) = f$, $\operatorname{comp}_1(t) = g(x)$, $\operatorname{comp}_2(t) = f(x, c)$. Replacement at one occurrence: $t[c]_{1 \cdot 1} = f(g(c), f(x, c))$ changes the first occurrence of $x$ only — an operation invisible to the occurrence-blind subterm relation.

> [!proposition] Proposition 12.12: Height–size bounds
> Let $b := \max \{ \operatorname{ar}(f) : f \text{ occurs in } t \} \geq 1$ for a compound term $t$. Then
>
> $$
> \operatorname{ht}(t) + 1 \;\leq\; \operatorname{sz}(t) \;\leq\; \frac{b^{\,\operatorname{ht}(t) + 1} - 1}{b - 1} \quad (b \geq 2), \qquad \operatorname{sz}(t) = \operatorname{ht}(t) + 1 \quad (b = 1),
> $$
>
> and both bounds are attained: the left by unary chains, the right by full $b$-ary trees. Hence height and size are interchangeable as termination measures but not as growth measures; induction on either is available, and statements about "small" terms must specify which measure is meant.

> [!proof-sketch] Proof Sketch 12.12
> Both inequalities by structural induction: a path of length $\operatorname{ht}(t)$ contributes $\operatorname{ht}(t) + 1$ positions; the upper bound sums the geometric series of the maximal number of positions per depth level.

---

## 13. Structural Induction and Structural Recursion

This chapter consolidates the two structural principles as theorems about the invariant syntax object, in the generality used later: induction (including the strong form), recursion into sets and into algebras, transfer to presentations, and the precise relationship between recursion and evaluation, ending with the preview of why these principles fail on quotient syntax.

### 13.1. Structural Induction

#### 13.1.1. Induction on Canonical Terms

> [!theorem] Theorem 13.1: Structural induction (restated)
> Let $\Phi \subseteq T_{\Omega}(X)$ with: (base-V) $X \subseteq \Phi$; (base-C) $\Omega_0 \subseteq \Phi$; (step) for every $f \in \Omega_n$ ($n \geq 1$), if $t_1, \dots, t_n \in \Phi$ then $f(t_1, \dots, t_n) \in \Phi$. Then $\Phi = T_{\Omega}(X)$. (Theorem 4.9; recorded here as the head of the chapter.) The principle is equivalent to generatedness of the term algebra by its atoms: it *is* the minimality clause of Definition 4.1.

#### 13.1.2. Induction on Presentations

By Theorem 11.8(1), the same principle holds verbatim in every presentation, with the $\mathbf{P}$-constructors in the step clause. Two practical notes. For **strings**, the step clause quantifies over the immediate subterms of a well-formed string, which are accessible only through the parse; induction on strings therefore presupposes unique readability (Theorem 9.6), and "induction on string length" is a different (cruder) principle that frequently forces re-proving the prefix property inline. For **trees**, structural induction coincides with induction on the well-founded subtree relation (Proposition 12.4 transferred), and induction on height is available as a coarsening. No induction theorem is ever re-proved per carrier; all are instances of Theorem 13.1 through transfer.

#### 13.1.3. Strong Structural Induction

> [!theorem] Theorem 13.2: Strong structural induction
> Let $\Phi \subseteq T_{\Omega}(X)$ satisfy: for every $t$, if $s \in \Phi$ for **all** proper subterms $s \prec t$, then $t \in \Phi$. Then $\Phi = T_{\Omega}(X)$.

> [!proof-sketch] Proof Sketch 13.2
> Well-founded induction along $\prec$ (Proposition 12.4): a $\prec$-minimal counterexample has all (none) of its proper subterms in $\Phi$, hence lies in $\Phi$. Atomic terms are handled vacuously (no proper subterms), so the single hypothesis subsumes both base and step of Theorem 13.1. The strong form is needed when a recursive definition or proof consults subterms deeper than the immediate ones.

### 13.2. Structural Recursion

#### 13.2.1. Recursion Data

> [!definition] Definition 13.3: Recursion data and fold notation
> **Recursion data** for $(\Omega, X)$ with value set $V$ is a triple
>
> $$
> \mathcal{D} = \big( h_X : X \to V,\quad h_C : \Omega_0 \to V,\quad (h_f : V^{n} \to V)_{f \in \Omega_n,\, n \geq 1} \big).
> $$
>
> The induced map (Theorem 13.4) is written $\operatorname{fold}_{\mathcal{D}} : T_{\Omega}(X) \to V$. The definition of a function by recursion data is **determined by syntax shape**: one value per atom, one clause per constructor, no other degrees of freedom.

#### 13.2.2. Existence and Uniqueness

> [!theorem] Theorem 13.4: Structural recursion (restated with provenance)
> For every recursion data $\mathcal{D}$ there is exactly one function $\Psi = \operatorname{fold}_{\mathcal{D}} : T_{\Omega}(X) \to V$ satisfying
>
> $$
> \Psi(x) = h_X(x), \qquad \Psi(c) = h_C(c), \qquad \Psi\big(f(t_1, \dots, t_n)\big) = h_f\big(\Psi(t_1), \dots, \Psi(t_n)\big).
> $$
>
> Existence rests on generatedness plus unique decomposition (the engine, Theorem 5.13); **uniqueness** rests on generatedness alone (induction on the agreement set) and is the property consumed by every canonicity argument in this treatise. Examples already in use: $\operatorname{ht}$, $\operatorname{sz}$, $\operatorname{var}$, $\operatorname{Pos}$, the string encoding $s$.

#### 13.2.3. Presentation Transfer

By Theorem 11.8(2), recursion data determine a unique solution on every presentation, and the solutions correspond under transfer: $\operatorname{fold}_{\mathcal{D}}^{\mathbf{P}} = \operatorname{fold}_{\mathcal{D}} \circ\, \tau_{P,T}$. The practical workflow is: *define* in the presentation whose destructors make the clauses natural (usually trees or tuples), *use* everywhere. A recursive function on strings is computed by parsing, folding, and (if string output is wanted) flattening; defining it by direct string manipulation re-derives the parser implicitly and is avoided.

### 13.3. Evaluation as Recursion

#### 13.3.1. Set-Valued Recursion versus Algebra-Valued Recursion

> [!proposition] Proposition 13.5: The two recursion formats coincide
> (i) If the value set carries an algebra structure $\mathbf{B}$ and the data are the **algebra-valued data** $h_C(c) := c^{\mathbf{B}}$, $h_f := f^{\mathbf{B}}$, then $\operatorname{fold}_{\mathcal{D}} = \operatorname{ev}_{h_X}$ is precisely the evaluation homomorphism extending $h_X$ (Theorem 4.6), and conversely every homomorphism out of $\mathbf{T}_{\Omega}(X)$ arises this way from its generator restriction. (ii) Every set-valued recursion is algebra-valued in disguise: equip $V$ with $c^{\mathbf{A}_V} := h_C(c)$, $f^{\mathbf{A}_V} := h_f$; then $\operatorname{fold}_{\mathcal{D}} = \operatorname{ev}_{h_X}^{\mathbf{A}_V}$.

> [!proof-sketch] Proof Sketch 13.5
> (i) The recursion clauses for algebra-valued data are the homomorphism clauses of Theorem 4.6; uniqueness on both sides matches them bijectively. (ii) is Proof Sketch 4.10. The moral: *an arbitrary recursive map does not respect any pre-given structure on $V$; an evaluation respects the target's operations by definition.* The two coincide because recursion data freely **install** the needed structure on $V$.

#### 13.3.2. Folds

> [!remark] Remark 13.6: Fold as organizing language
> The notation $\operatorname{fold}_{\mathcal{D}}$ packages structural recursion as a single higher-order operation: syntax is the initial recipient of constructor data, and folding replays a term's construction with $h$-clauses in place of constructors. This language is used below purely as bookkeeping (e.g. "substitution is the fold with clauses given by formal constructors," Theorem 14.4); the categorical apparatus of initial algebras for polynomial functors, of which fold is the universal arrow, is acknowledged (compare Remark 8.7) but not developed.

#### 13.3.3. Recursion Failure on Quotients

> [!warning] Warning 13.7: Quotient syntax does not support unconditional recursion
> On quotient syntax $\mathbf{T}_{\Omega}(X)/\theta$ (Chapter 18), elements are equivalence classes and need not have unique constructor decompositions: a class may be presented as $[f(\vec{s}\,)]$ and as $[g(\vec{u})]$ with $f \neq g$. Recursion data then assign conflicting values along different presentations, and $\operatorname{fold}_{\mathcal{D}}$ on representatives is well-defined **only if** the data respect $\theta$ — the **descent condition** $\theta \subseteq \ker(\operatorname{fold}_{\mathcal{D}})$ (Theorem 18.5). On raw syntax descent is vacuous because $\theta = \Delta$; this is the precise sense in which free recursion is automatic and quotient recursion is constrained. Chapter 18 develops the calculus.

### 13.4. Extensions and Worked Examples

> [!example] Example 13.8: Three folds
> Over $\Omega = \{f, g, c\}$ (arities $2, 1, 0$): (i) the **mirror map** $M$ with data $h_X(x) = x$, $h_C(c) = c$, $h_g(v) = g(v)$, $h_f(v_1, v_2) = f(v_2, v_1)$ reverses all $f$-arguments; e.g. $M\big(f(g(x), c)\big) = f(c, g(x))$, and $M \circ M = \mathrm{id}$ by uniqueness of the fold satisfying the identity clauses. (ii) The **groundness test** with values in $\{0, 1\}$: $h_X = 0$, $h_C = 1$, $h_g(v) = v$, $h_f(v_1, v_2) = \min(v_1, v_2)$ computes whether a term is ground. (iii) The **string encoder** $s$ of Definition 9.2 is the fold into $\mathcal{A}^{<\omega}$ with concatenation clauses. Each map is *defined* by its data and *characterized* by its clauses — no separate well-definedness argument is ever required on raw syntax.

> [!theorem] Theorem 13.9: Recursion with access to subterms
> Let $V$ be a set with data $h_X : X \to V$, $h_C : \Omega_0 \to V$, and for each $f \in \Omega_n$ ($n \geq 1$) a function
>
> $$
> h_f : \big( T_{\Omega}(X) \times V \big)^{n} \to V.
> $$
>
> Then there is a unique $\Psi : T_{\Omega}(X) \to V$ with $\Psi(x) = h_X(x)$, $\Psi(c) = h_C(c)$, and
>
> $$
> \Psi\big(f(t_1, \dots, t_n)\big) = h_f\big( (t_1, \Psi(t_1)), \dots, (t_n, \Psi(t_n)) \big),
> $$
>
> i.e. the clause for a compound term may consult the immediate subterms **themselves**, not only their recursive values.

> [!proof-sketch] Proof Sketch 13.9
> Run plain structural recursion (Theorem 13.4) with value set $T_{\Omega}(X) \times V$, computing the pair $(t, \Psi(t))$: base clauses pair the atom with its $h$-value; the constructor clause rebuilds the term in the first coordinate by the formal constructor and applies $h_f$ in the second. The first coordinate of the resulting fold is $\mathrm{id}$ (by uniqueness, comparing with the identity fold), so the second coordinate satisfies the displayed clauses; uniqueness by structural induction. This **paired-value device** converts subterm-consulting recursions (e.g. one-step rewriting, capture-avoiding definitions later in logic) into ordinary folds.

> [!theorem] Theorem 13.10: Simultaneous (mutual) structural recursion
> Let $V_1, \dots, V_r$ be sets and suppose recursion data are given for the product $V := V_1 \times \cdots \times V_r$, i.e. clause functions whose components may depend on **all** coordinates of the recursive values. Then there exist unique functions $\Psi_j : T_{\Omega}(X) \to V_j$ ($1 \leq j \leq r$) jointly satisfying the clauses. Mutually dependent recursive definitions (e.g. simultaneous computation of $\operatorname{var}$ and a normal-form flag, or of value and auxiliary bookkeeping) therefore require no new principle.

> [!proof-sketch] Proof Sketch 13.10
> Apply Theorem 13.4 with value set $V$ and read off the coordinate projections $\Psi_j := \pi_j \circ \operatorname{fold}$; uniqueness of the tuple map gives joint uniqueness of the components. The paired-value device of Theorem 13.9 is the case $r = 2$ with first coordinate the identity fold.

---
## 14. Substitution as Syntax-to-Syntax Evaluation

Substitution is the first major operation defined by the universal property rather than by symbol manipulation: a substitution is an assignment of **terms** to variables, and its action on all of syntax is the unique homomorphic extension — evaluation whose target happens to be another syntax algebra. This chapter fixes the definitions, derives the recursive clauses as theorems, establishes the algebraic laws (identity, composition, associativity), and proves the compatibility identity linking substitution to semantic evaluation.

### 14.1. Substitution Assignments

#### 14.1.1. Variables to Terms

> [!definition] Definition 14.1: Substitution
> Let $X, Y$ be generator sets for $\Omega$. A **substitution** from $X$ to $Y$ is a function
>
> $$
> \sigma : X \to T_{\Omega}(Y),
> $$
>
> assigning to each variable $x$ a term $\sigma(x)$ over $Y$. Substitution is **simultaneous by default**: all variables are replaced at once, with no sequencing. One-variable substitution is the derived special case $\sigma = [x \mapsto s]$ with $\sigma(x) := s$ and $\sigma(y) := y$ for $y \neq x$; it is *not* the primitive notion, and iterating one-variable substitutions does not in general reproduce a simultaneous one (replacements can capture later replacement sites), which is why the simultaneous form is primitive.

#### 14.1.2. Codomain Term Algebra

> [!remark] Remark 14.2: Substitution is a valuation into syntax
> A substitution is *literally* an assignment in the sense of Definition 3.3 with target algebra $\mathbf{T}_{\Omega}(Y)$. Everything proved about assignments and evaluation applies verbatim with this codomain; substitution theory is evaluation theory specialized to syntax-valued values. The family of constructions $X \mapsto T_{\Omega}(X)$, with insertion $\eta_X$ and the extension operation of Theorem 14.4, in fact constitutes a monad on sets whose Kleisli composition is the substitution composite of Definition 14.8; this packaging is recorded for orientation only and is not used.

#### 14.1.3. Endosubstitutions

> [!definition] Definition 14.3: Endosubstitution, renaming, ground substitution
> Fix a **variable reservoir** $V$. An **endosubstitution** is a substitution $\sigma : V \to T_{\Omega}(V)$ from the reservoir to itself; its extension $\widehat{\sigma}$ (Theorem 14.4) is an endomorphism of $\mathbf{T}_{\Omega}(V)$, and every endomorphism of $\mathbf{T}_{\Omega}(V)$ arises this way from its restriction to variables. A **variable renaming** is a substitution with $\sigma(x) \in \eta_Y[Y]$ for all $x$ (variables to variables); a **ground substitution** has $\operatorname{var}(\sigma(x)) = \varnothing$ for all $x$. Endosubstitutions are the maps under which **fully invariant congruences** are stable (Definition 18.11), the syntactic transformations relevant to equational logic.

### 14.2. Substitution Homomorphism

#### 14.2.1. Unique Extension

> [!theorem] Theorem 14.4: Substitution extension
> Every substitution $\sigma : X \to T_{\Omega}(Y)$ extends to a unique homomorphism
>
> $$
> \widehat{\sigma} : \mathbf{T}_{\Omega}(X) \longrightarrow \mathbf{T}_{\Omega}(Y), \qquad \widehat{\sigma} \circ \eta_X = \sigma,
> $$
>
> namely the evaluation homomorphism $\operatorname{ev}_{\sigma}$ with target $\mathbf{T}_{\Omega}(Y)$ (Theorem 4.6). For $t \in T_{\Omega}(X)$ write
>
> $$
> t[\sigma] := \widehat{\sigma}(t),
> $$
>
> the **result of applying $\sigma$ to $t$**. Defining substitution by the UMP — rather than by ad hoc recursion on a chosen presentation — makes its homomorphy, its presentation-independence, and its laws automatic.

#### 14.2.2. Recursive Clauses

> [!proposition] Proposition 14.5: Computation rules for substitution
> The extension $\widehat{\sigma}$ satisfies, and is uniquely determined by, the clauses
>
> $$
> x[\sigma] = \sigma(x), \qquad c[\sigma] = c \quad (c \in \Omega_0),
> $$
>
> $$
> f(t_1, \dots, t_n)[\sigma] = f\big( t_1[\sigma], \dots, t_n[\sigma] \big) \quad (f \in \Omega_n,\ n \geq 1).
> $$
>
> Substitution commutes with all syntax formation: it replaces variables, fixes constants, and is transparent to constructors. Consequently $\operatorname{var}(t[\sigma]) = \bigcup_{x \in \operatorname{var}(t)} \operatorname{var}(\sigma(x))$, and if $\sigma$ agrees with $\sigma'$ on $\operatorname{var}(t)$ then $t[\sigma] = t[\sigma']$.

> [!proof-sketch] Proof Sketch 14.5
> The clauses are the homomorphism conditions for $\widehat{\sigma}$ together with $\widehat{\sigma} \circ \eta_X = \sigma$; uniqueness is Theorem 13.4. The variable identity and the agreement property follow by structural induction using the clauses.

#### 14.2.3. Substitution on Presentations

> [!proposition] Proposition 14.6: Transfer of substitution
> For presentations $\mathcal{P}$ of syntax on $X$ and $\mathcal{Q}$ on $Y$, the **transferred substitution** is $\widehat{\sigma}^{\,P,Q} := r_Q \circ \widehat{\sigma} \circ r_P^{-1} : \mathbf{P} \to \mathbf{Q}$; it is the unique homomorphism carrying $\eta_P(x)$ to the $\mathbf{Q}$-representative of $\sigma(x)$, and all transferred versions correspond under the transfer maps. On trees, it is simultaneous leaf grafting (replace each $x$-leaf by the tree for $\sigma(x)$, re-addressing under the leaf's position); on tuples, recursive code rewriting. On strings, substitution **must** route through parse and flatten: textual replacement of the character $x$ inside an unparsed string is not the transferred operation and corrupts well-formedness or meaning whenever lexical boundaries or structure interfere.

> [!proof-sketch] Proof Sketch 14.6
> Conjugation of a homomorphism by isomorphisms over the generator sets; uniqueness by Lemma 3.5. The tree description satisfies the clauses of Proposition 14.5 transferred along $r_{\mathrm{tree}}$, hence equals the transfer by uniqueness.

### 14.3. Laws of Substitution

#### 14.3.1. Identity

> [!proposition] Proposition 14.7: Identity substitution
> The insertion $\eta_X : X \to T_{\Omega}(X)$, read as the substitution $x \mapsto x$, extends to the identity:
>
> $$
> \widehat{\eta_X} = \mathrm{id}_{\mathbf{T}_{\Omega}(X)}, \qquad t[\eta_X] = t.
> $$
>
> Variables are neutral for substitution; this is the syntactic root of the projection identities of the syntactic clone (Theorem 16.5).

> [!proof-sketch] Proof Sketch 14.7
> $\mathrm{id}$ is a homomorphic extension of $\eta_X$ along $\eta_X$; uniqueness (Lemma 3.5) identifies it with $\widehat{\eta_X}$.

#### 14.3.2. Composition

> [!definition] Definition 14.8: Composite substitution
> For $\sigma : X \to T_{\Omega}(Y)$ and $\tau : Y \to T_{\Omega}(Z)$, the **composite substitution** is
>
> $$
> \tau \star \sigma \;:\; X \to T_{\Omega}(Z), \qquad (\tau \star \sigma)(x) := \widehat{\tau}\big(\sigma(x)\big) = \sigma(x)[\tau].
> $$

> [!theorem] Theorem 14.9: Functoriality and associativity of substitution
> For all $\sigma : X \to T_{\Omega}(Y)$, $\tau : Y \to T_{\Omega}(Z)$, $\upsilon : Z \to T_{\Omega}(W)$:
>
> $$
> \widehat{\tau \star \sigma} \;=\; \widehat{\tau} \circ \widehat{\sigma}, \qquad\text{hence}\qquad t[\tau \star \sigma] = \big( t[\sigma] \big)[\tau] \quad \text{for all } t \in T_{\Omega}(X);
> $$
>
> $$
> \upsilon \star (\tau \star \sigma) = (\upsilon \star \tau) \star \sigma, \qquad \eta_Y \star \sigma = \sigma = \sigma \star \eta_X.
> $$
>
> Substitutions thus compose associatively with the insertions as two-sided units, and extension $\sigma \mapsto \widehat{\sigma}$ converts $\star$ into ordinary composition of homomorphisms.

> [!proof-sketch] Proof Sketch 14.9
> Both $\widehat{\tau \star \sigma}$ and $\widehat{\tau} \circ \widehat{\sigma}$ are homomorphisms $\mathbf{T}_{\Omega}(X) \to \mathbf{T}_{\Omega}(Z)$ agreeing on generators (both send $x$ to $\widehat\tau(\sigma(x))$); Lemma 3.5 gives equality. Associativity and the unit laws follow by applying this identity twice resp. with Proposition 14.7 — each is an agreement-on-generators argument, never a computation on concrete carriers.

#### 14.3.3. Evaluation-Substitution Compatibility

> [!theorem] Theorem 14.10: Substitution lemma
> Let $\sigma : X \to T_{\Omega}(Y)$ be a substitution, $\mathbf{B}$ an $\Omega$-algebra, and $w : Y \to B$ an assignment. Define the **pulled-back assignment**
>
> $$
> w \star \sigma \;:\; X \to B, \qquad (w \star \sigma)(x) := \operatorname{ev}_w\big(\sigma(x)\big).
> $$
>
> Then
>
> $$
> \operatorname{ev}_w \circ \widehat{\sigma} \;=\; \operatorname{ev}_{\,w \star \sigma} \;:\; \mathbf{T}_{\Omega}(X) \to \mathbf{B},
> $$
>
> i.e. for every term $t$: **evaluating after substituting equals evaluating under the pulled-back valuation**,
>
> $$
> \operatorname{ev}_w\big( t[\sigma] \big) \;=\; \operatorname{ev}_{\,w \star \sigma}(t).
> $$

> [!proof-sketch] Proof Sketch 14.10
> Both sides are homomorphisms $\mathbf{T}_{\Omega}(X) \to \mathbf{B}$; on a generator $x$ both yield $\operatorname{ev}_w(\sigma(x))$. Lemma 3.5 concludes. The statement is the first bridge between the syntax-to-syntax and syntax-to-semantics map families of §0.3.3, and it is the engine of soundness arguments once logic is added.

> [!corollary] Corollary 14.11: Kernel pullback along substitution
> With the data of Theorem 14.9,
>
> $$
> \ker\big( \operatorname{ev}_{\,w \star \sigma} \big) \;=\; \big( \widehat{\sigma} \times \widehat{\sigma} \big)^{-1} \big[ \ker( \operatorname{ev}_w ) \big],
> $$
>
> i.e. two terms are semantically equal under the pulled-back valuation iff their $\sigma$-images are semantically equal under $w$. In particular $\widehat{\sigma}$ descends from the $(w \star \sigma)$-kernel quotient to the $w$-kernel quotient (Theorem 18.10).

> [!proof-sketch] Proof Sketch 14.11
> Unfold both sides with Theorem 14.10: $\operatorname{ev}_{w\star\sigma}(s) = \operatorname{ev}_{w\star\sigma}(t)$ iff $\operatorname{ev}_w(s[\sigma]) = \operatorname{ev}_w(t[\sigma])$.

### 14.4. Worked Example and Renamings

> [!example] Example 14.12: Simultaneous versus sequential substitution
> Over $\Omega = \{f, g, c\}$ (arities $2, 1, 0$), $X = Y = \{x, y\}$, let $\sigma(x) := g(y)$, $\sigma(y) := c$, and $t := f(x, y)$. Simultaneous application gives
>
> $$
> t[\sigma] = f\big(g(y),\, c\big).
> $$
>
> Sequential one-variable substitution in the order "first $x$, then $y$" gives $\big(t[x \mapsto g(y)]\big)[y \mapsto c] = f(g(c), c) \neq t[\sigma]$: the $y$ introduced by the first step is **captured** by the second. The opposite order happens to agree with $\sigma$ here, but no uniform ordering works for all $\sigma$ (consider the swap $\sigma(x) = y$, $\sigma(y) = x$, where both orders fail). This is the formal reason simultaneous substitution is primitive (Definition 14.1).

> [!proposition] Proposition 14.13: Renamings
> Let $\rho : X \to Y$ be a function and $\sigma_\rho := \eta_Y \circ \rho : X \to T_{\Omega}(Y)$ the induced renaming substitution. Then: (i) $\widehat{\sigma_\rho}$ maps variable terms to variable terms and preserves $\operatorname{case}$, $\operatorname{root}$, height, size, and positions; (ii) if $\rho$ is injective, $\widehat{\sigma_\rho}$ is an embedding; (iii) if $\rho$ is bijective, $\widehat{\sigma_\rho}$ is an isomorphism $\mathbf{T}_{\Omega}(X) \cong \mathbf{T}_{\Omega}(Y)$ with inverse $\widehat{\sigma_{\rho^{-1}}}$ — an isomorphism **over the bijection $\rho$**, not over a common generator set; renaming changes which syntax object one has, unlike the over-$X$ transfers of Chapter 11.

> [!proof-sketch] Proof Sketch 14.13
> (i) by the computation rules (Proposition 14.5): structure is rebuilt verbatim with relabelled leaves. (ii) and (iii): $\widehat{\sigma_{\rho^{-1}}} \circ \widehat{\sigma_\rho}$ extends $\eta_X \circ \rho^{-1} \circ \rho = \eta_X$, hence is the identity (Lemma 3.5); injectivity in (ii) follows by factoring $\rho$ through a bijection onto its image.

> [!proposition] Proposition 14.14: Quantitative behavior of substitution
> For every $t \in T_{\Omega}(X)$ and substitution $\sigma : X \to T_{\Omega}(Y)$:
>
> $$
> \operatorname{sz}\big( t[\sigma] \big) \;=\; \operatorname{sz}(t) \;+\; \sum_{x \in \operatorname{var}(t)} \#_x(t) \cdot \big( \operatorname{sz}(\sigma(x)) - 1 \big),
> $$
>
> $$
> \operatorname{ht}\big( t[\sigma] \big) \;\leq\; \operatorname{ht}(t) + \max_{x \in \operatorname{var}(t)} \operatorname{ht}(\sigma(x)),
> $$
>
> with equality in the height bound when some deepest leaf of $t$ is a variable realizing the maximum. Substitution growth is thus linear in occurrence counts — the quantitative shadow of the value/occurrence distinction (Warning 12.6), and the reason occurrence data, not just variable sets, are tracked.

> [!proof-sketch] Proof Sketch 14.14
> Structural induction on $t$ via the computation rules (Proposition 14.5): each occurrence of $x$ contributes $\operatorname{sz}(\sigma(x))$ in place of $1$; heights compose along root-to-leaf paths.

---

## 15. Contexts as Derived Syntax Operations

A context is a term with designated **holes**; plugging terms into the holes is itself substitution in an enlarged syntax algebra. This chapter constructs hole-extended syntax, defines one- and multi-hole contexts and plugging, identifies replacement-at-a-position as context plugging, and proves the closure fact that explains why congruences are exactly the equivalences stable under all syntactic surroundings.

### 15.1. Hole-Extended Syntax

#### 15.1.1. Hole Symbols

> [!definition] Definition 15.1: Holes and hole-extended syntax
> Fix a countable set $H = \{ \Box_1, \Box_2, \Box_3, \dots \}$ of **hole symbols**, disjoint from $X \cup \Omega$, and write $H_k := \{\Box_1, \dots, \Box_k\}$ and $\Box := \Box_1$. The **hole-extended syntax algebra** with $k$ holes is the free algebra
>
> $$
> \mathbf{T}_{\Omega}(X \sqcup H_k),
> $$
>
> i.e. ordinary term syntax over the enlarged generator set. Holes are **extra generators**, not new operation symbols: they are atomic, freely assignable, and preserved by nothing except over-$(X \sqcup H_k)$ maps. They are kept disjoint from the ordinary variables so that plugging can target holes while leaving variables intact.

#### 15.1.2. One-Hole Contexts

> [!definition] Definition 15.2: One-hole context
> A **one-hole context over $X$** is a term $C \in T_{\Omega}(X \sqcup \{\Box\})$ such that $\Box$ has **exactly one occurrence** in $C$, i.e. $\#_{\Box}(C) = 1$ (Definition 12.10). The unique $p \in \operatorname{Pos}(C)$ with $C|_p = \Box$ is the **hole position** $p_{\Box}(C)$. The trivial context is $\Box$ itself ($p_\Box = \varepsilon$). The context **object** $C$ — an element of an enlarged syntax algebra — is distinguished from the **operation** it induces (Definition 15.8); the object is data, the operation is its action.

#### 15.1.3. Multi-Hole Contexts

> [!definition] Definition 15.3: Multi-hole context
> A **$k$-hole context over $X$** is a term $C \in T_{\Omega}(X \sqcup H_k)$; it is **exact** if each of $\Box_1, \dots, \Box_k$ occurs at least once, and **linear** if each occurs exactly once. Hole indices carry the **input-place order**: $\Box_i$ marks the $i$-th plug position class. Non-linear contexts (a hole occurring several times) induce diagonalized operations — the same argument is inserted at all occurrences of that hole — and are permitted; the linear case corresponds to position-disjoint replacement. $k$-hole contexts are the syntactic form of derived $k$-ary operations on syntax (Definition 15.8), polynomial-style operations built from constructors and fixed side terms.

### 15.2. Plugging and Replacement

#### 15.2.1. Plugging as Substitution

> [!construction] Construction 15.4: Plugging
> Let $C \in T_{\Omega}(X \sqcup H_k)$ and $s_1, \dots, s_k \in T_{\Omega}(X)$. The **plugging** of $\vec{s}$ into $C$ is
>
> $$
> C[s_1, \dots, s_k] := C\big[\, \sigma_{\vec{s}} \,\big], \qquad \sigma_{\vec{s}}(x) := x \ (x \in X), \qquad \sigma_{\vec{s}}(\Box_i) := s_i \ (1 \leq i \leq k),
> $$
>
> i.e. the image of $C$ under the substitution homomorphism $\widehat{\sigma_{\vec{s}}} : \mathbf{T}_{\Omega}(X \sqcup H_k) \to \mathbf{T}_{\Omega}(X)$ fixing the ordinary variables and sending each hole to its plug. No new definitional apparatus is introduced: plugging inherits well-definedness, homomorphy, and all laws from the substitution machinery of Chapter 14.

#### 15.2.2. Multi-Hole Plugging

> [!proposition] Proposition 15.5: Plugging laws
> For $C \in T_{\Omega}(X \sqcup H_k)$, plugs $\vec{s} \in T_{\Omega}(X)^k$, and a one-hole context decomposition where applicable:
>
> 1. (variables and constants) $\operatorname{var}\big(C[\vec{s}\,]\big) \subseteq \big(\operatorname{var}(C) \cap X\big) \cup \bigcup_i \operatorname{var}(s_i)$, with equality when $C$ is exact;
> 2. (nesting) plugging composes: if $D \in T_{\Omega}(X \sqcup H_m)$ and each $s_i = D_i[\vec{u}\,]$, then $C[\vec{s}\,]$ equals the plugging of $\vec{u}$ into the composite context $C[D_1, \dots, D_k]$ formed in $T_{\Omega}(X \sqcup H_m)$ — an instance of Theorem 14.9;
> 3. (order and arity) the induced map $\vec{s} \mapsto C[\vec{s}\,]$ is a $k$-ary operation $T_{\Omega}(X)^k \to T_{\Omega}(X)$ whose argument places are indexed by the hole order, with repetitions of a hole producing diagonal argument use.

> [!proof-sketch] Proof Sketch 15.5
> All three clauses unfold to substitution facts: (1) is the variable identity of Proposition 14.5; (2) is associativity $\widehat{\sigma_{\vec u}} \circ \widehat{\sigma_{\vec D}} = \widehat{\sigma_{\vec u} \star \sigma_{\vec D}}$ (Theorem 14.9) applied to $C$; (3) is bookkeeping of $\sigma_{\vec{s}}$.

#### 15.2.3. Replacement via Context Decomposition

> [!proposition] Proposition 15.7: Context decomposition and replacement
> Let $t \in T_{\Omega}(X)$ and $p \in \operatorname{Pos}(t)$. There is a unique one-hole context $C_p^t \in T_{\Omega}(X \sqcup \{\Box\})$ with hole position $p$ such that
>
> $$
> t = C_p^t\big[\, t|_p \,\big],
> $$
>
> namely the term obtained from $t$ by replacing the subterm at $p$ with $\Box$ (Definition 12.7 over the extended variable set). Moreover, for every $s$,
>
> $$
> t[s]_p = C_p^t[\, s \,] :
> $$
>
> replacement at a position is plugging into the hollowed context. Every occurrence-level operation on syntax thus factors through the pair (context, filler), which is the formal interface that rewriting and, later, formula-occurrence substitution will use.

> [!proof-sketch] Proof Sketch 15.7
> Existence: induction on $p$, hollowing along the path. Uniqueness: a one-hole context with hole position $p$ and $C[t|_p] = t$ is determined at every position off the path by $t$ and at the path positions by the constructors of $t$ (unique readability). The displayed identity is proved by the same induction on $p$, comparing the recursive clauses of Definition 12.7 and Construction 15.4.

### 15.3. Context Closure

#### 15.3.1. Contexts and Congruences

> [!definition] Definition 15.8: Derived context operation
> Each $k$-hole context $C$ induces the **derived syntax operation**
>
> $$
> C[\,\cdot\,] : T_{\Omega}(X)^k \to T_{\Omega}(X), \qquad \vec{s} \mapsto C[\vec{s}\,].
> $$
>
> Derived context operations are precisely the operations on syntax built from formal constructors, fixed parameter terms (subterms of $C$ without holes), and argument places — the syntax-algebra analogue of polynomial operations on an algebra (compare Definition 16.15), with holes playing the role of argument variables and the $X$-part of $C$ the role of parameters.

> [!proposition] Proposition 15.9: Congruences are exactly context-closed equivalences
> Let $\theta$ be an equivalence relation on $T_{\Omega}(X)$. The following are equivalent:
>
> 1. $\theta$ is a congruence on $\mathbf{T}_{\Omega}(X)$ (compatible with all basic constructors);
> 2. $\theta$ is closed under all one-hole contexts: $(s, t) \in \theta$ implies $\big(C[s],\, C[t]\big) \in \theta$ for every one-hole context $C$;
> 3. $\theta$ is closed under all derived context operations applied argumentwise: $(s_i, t_i) \in \theta$ for $i \leq k$ implies $\big(C[\vec{s}\,],\, C[\vec{t}\,]\big) \in \theta$ for every $k$-hole context $C$.

> [!proof-sketch] Proof Sketch 15.9
> (1 $\Rightarrow$ 3) by structural induction on $C$: at a hole, the hypothesis; at a variable or constant, reflexivity; at a constructor node, compatibility. (3 $\Rightarrow$ 2) is the case $k = 1$ with transitivity handling argumentwise versus simultaneous change. (2 $\Rightarrow$ 1) constructor compatibility is the special case of contexts $f(t_1, \dots, \Box, \dots, t_n)$ changing one argument, composed transitively across argument places. The equivalence explains the slogan *compatible = stable under all syntactic surroundings* and yields the derivational description of generated congruences (Theorem 18.3).

#### 15.3.2. Contexts as Derived Operations

The identification of Definition 15.8 places contexts inside the operational hierarchy: basic constructors are the operations named by $\Omega$; derived context operations add parameters and composite shapes; the syntactic clone (Chapter 16) is the parameter-free, variable-indexed organization of the same material. Congruence closure (Proposition 15.9) and clone superposition (Construction 16.4) are the two systematic uses.

#### 15.3.3. Presentation Transfer of Contexts

> [!remark] Remark 15.10: Where to compute with contexts
> Contexts, plugging, and context decomposition are defined invariantly (they are terms and substitutions over enlarged generator sets), hence transfer to every presentation by Theorem 11.10 applied to $(\Omega, X \sqcup H_k)$. Occurrence-sensitive work — locating $p$, hollowing $C_p^t$, replacing one occurrence — is most conveniently performed in the **tree** presentation, where positions are addresses and hollowing is address surgery; invariant statements about the results are then stated over $\mathbf{T}_{\Omega}(X)$. The division of labor is the standard one: trees for computation with occurrences, the hub for statements.

### 15.4. Worked Example

> [!example] Example 15.11: Context decomposition in data
> Let $t := f\big(g(x),\, f(x, c)\big)$ (Example 12.11) and $p := 2{\cdot}1$, so $t|_p = x$. The hollowed context is
>
> $$
> C_p^t = f\big(g(x),\, f(\Box, c)\big) \in T_{\Omega}\big(X \sqcup \{\Box\}\big),
> $$
>
> with hole position $2{\cdot}1$, and indeed $C_p^t[x] = t$ and $C_p^t[c] = t[c]_p = f(g(x), f(c, c))$. Note that the *other* occurrence of $x$ (at $1{\cdot}1$) survives inside the context as an ordinary variable: contexts freeze everything except the designated occurrence. The two-hole context $D := f(g(\Box_1), f(\Box_2, c))$ induces the derived binary operation $(s_1, s_2) \mapsto f(g(s_1), f(s_2, c))$, and $t = D[x, x]$ exhibits $t$ as a diagonal value of $D$.

> [!proposition] Proposition 15.12: Positions under plugging
> Let $C$ be a one-hole context over $X$ with hole position $q := p_{\Box}(C)$, and let $s \in T_{\Omega}(X)$. Then
>
> $$
> \operatorname{Pos}\big( C[s] \big) \;=\; \big( \operatorname{Pos}(C) \setminus \{q\} \big) \ \cup\ \{\, q \cdot p \;:\; p \in \operatorname{Pos}(s) \,\},
> $$
>
> and for positions $p'$ in the first part, $C[s]\,|_{p'} = C|_{p'}$ whenever $q \not\preceq p'$, while $C[s]\,|_{q \cdot p} = s|_p$. Plugging translates the addresses of the filler by the hole address and leaves the remainder of the context untouched — the address arithmetic that makes occurrence-sensitive rewriting compositional.

> [!proof-sketch] Proof Sketch 15.12
> Induction on $q$ along the recursive clauses of Definition 12.7 and Construction 15.4, mirroring Proof Sketch 15.7.

---
## 16. Syntactic Clones and Derived Term Operations

Terms have so far been **elements** of a free algebra. This chapter reorganizes them as **arity-indexed formal operations**: a term in $n$ fixed variables is a delayed $n$-ary operation, awaiting a carrier. The resulting structure — projections plus formal superposition — is the **syntactic clone** of the signature. Interpretation in a concrete algebra maps it onto the algebra's term clone, the kernel of that interpretation is the algebra's equational data, and the valuation kernel is recognized as the strictly weaker, single-assignment relation. The chapter is deliberately preparatory: clone theory proper (clone lattices, Galois connections with invariant relations) is excluded.

### 16.1. Arity-Indexed Terms

#### 16.1.1. Fixed Variable Contexts

> [!notation] Notation 16.1: Standard variable contexts
> Fix a countable supply of **standard variables** $x_1, x_2, x_3, \dots$ and set, for $n \geq 1$,
>
> $$
> X_n := \{x_1, \dots, x_n\}, \qquad T_{\Omega}(n) := T_{\Omega}(X_n).
> $$
>
> Elements of $T_{\Omega}(n)$ are **$n$-ary formal terms** (terms in context $X_n$). The inclusions $X_n \subseteq X_{n+1}$ induce injections $T_{\Omega}(n) \hookrightarrow T_{\Omega}(n+1)$ (renaming-free widening); a term of $T_{\Omega}(n)$ need not use all of $x_1, \dots, x_n$, so "$n$-ary" records the declared context, not the variables actually occurring.

#### 16.1.2. Projections

> [!definition] Definition 16.2: Projection terms
> For $n \geq 1$ and $1 \leq i \leq n$, the **$i$-th $n$-ary projection term** is the variable term $x_i \in T_{\Omega}(n)$. Under interpretation (Definition 16.9) it induces the concrete projection operation $\pi_i^n : A^n \to A$, $\pi_i^n(\vec{a}) = a_i$. The identity substitution law (Proposition 14.7) is the syntactic germ of the projection identities (Theorem 16.5): variables act as do-nothing operations.

#### 16.1.3. Terms as Delayed Operations

> [!remark] Remark 16.3: Delayed evaluation
> An $n$-ary term is an operation **held in syntactic form**: it can be composed with other such terms, stored, transported across presentations, and only later applied to elements of a chosen carrier. The discipline of working in $T_{\Omega}(n)$ before choosing $\mathbf{A}$ is what makes "the same polynomial over every ring," "the same propositional scheme over every Boolean algebra," and, later, "the same first-order term in every structure" meaningful single objects. Theorem 16.11 (interpretation commutes with superposition) is the statement that delayed and eager composition agree.

### 16.2. Formal Superposition

#### 16.2.1. Simultaneous Substitution in Fixed Arity

> [!construction] Construction 16.4: Formal superposition
> For $t \in T_{\Omega}(m)$ and $s_1, \dots, s_m \in T_{\Omega}(n)$, the **formal superposition** is
>
> $$
> t[s_1, \dots, s_m] := \widehat{\sigma}(t) \in T_{\Omega}(n), \qquad \sigma : X_m \to T_{\Omega}(n), \quad \sigma(x_i) := s_i,
> $$
>
> i.e. simultaneous substitution of the $n$-ary terms $s_i$ for the variables of the $m$-ary term $t$ (Theorem 14.4 with $X = X_m$, $Y = X_n$). Superposition is the composition operation of formal operations: an $m$-ary operation applied to $m$ operations of common arity $n$ yields an $n$-ary operation.

#### 16.2.2. Associativity

> [!theorem] Theorem 16.5: Clone laws of formal superposition
> For all $t \in T_{\Omega}(m)$, $s_1, \dots, s_m \in T_{\Omega}(n)$, $u_1, \dots, u_n \in T_{\Omega}(k)$:
>
> $$
> \textbf{(assoc)} \qquad t[s_1, \dots, s_m]\,[u_1, \dots, u_n] \;=\; t\big[\, s_1[u_1, \dots, u_n],\ \dots,\ s_m[u_1, \dots, u_n] \,\big];
> $$
>
> $$
> \textbf{(proj-right)} \qquad t[x_1, \dots, x_m] = t; \qquad \textbf{(proj-left)} \qquad x_i[s_1, \dots, s_m] = s_i.
> $$

> [!proof-sketch] Proof Sketch 16.5
> (assoc) is the substitution composition law $t[\tau \star \sigma] = (t[\sigma])[\tau]$ (Theorem 14.9) with $\sigma(x_i) = s_i$, $\tau(x_j) = u_j$, unwound through Definition 14.8. (proj-right) is the identity law (Proposition 14.7); (proj-left) is the generator clause $x_i[\sigma] = \sigma(x_i)$ of Proposition 14.5. No new computation occurs: the clone laws *are* the substitution laws in fixed-arity dress.

#### 16.2.3. Projection Identities

The two projection identities state that variables are formal projections behaving as left and right units for superposition. Together with associativity they constitute the **abstract clone axioms**; no further clone theory (e.g. the lattice of clones on a carrier) is invoked anywhere in this treatise.

### 16.3. Syntactic Clone

#### 16.3.1. Definition

> [!definition] Definition 16.6: Syntactic clone
> The **syntactic clone** of $\Omega$ is the arity-indexed family
>
> $$
> \operatorname{Syn}_{\Omega} := \big( T_{\Omega}(n) \big)_{n \geq 1}
> $$
>
> equipped with the projection terms $x_i \in T_{\Omega}(n)$ ($1 \leq i \leq n$) and the superposition operations of Construction 16.4. By Theorem 16.5, $\operatorname{Syn}_{\Omega}$ is an abstract clone: the **operation algebra of raw syntax**, existing prior to any choice of carrier.

#### 16.3.2. Scope

> [!remark] Remark 16.7: Restricted role
> $\operatorname{Syn}_{\Omega}$ is used here for exactly two purposes: to organize substitution-as-composition (this chapter) and to state the kernel comparison preparing first-order local/global semantic distinctions (§16.5). Nullary terms can be accommodated by adjoining $T_{\Omega}(0) := T_{\Omega}(\varnothing)$ (ground terms) with the evident superposition; the positive-arity convention above is the default. Clone lattices, Mal'cev conditions, and polymorphism Galois theory are out of scope.

#### 16.3.3. Relation to Term Algebra

> [!remark] Remark 16.8: Two readings of one syntax
> The term algebra $\mathbf{T}_{\Omega}(X)$ treats terms as **elements**, with the formal constructors as operations and arbitrary generator sets; the syntactic clone $\operatorname{Syn}_{\Omega}$ treats terms as **arity-indexed formal operations**, with superposition as composition and standardized contexts $X_n$. They are two organizations of the same underlying syntax, linked by: $T_{\Omega}(n) = T_{\Omega}(X_n)$ as sets; superposition = substitution (Construction 16.4); and, after interpretation, evaluation at a point versus the induced operation (Definition 16.9). Neither subsumes the other: element-style supports evaluation kernels at a fixed assignment, operation-style supports identities across all assignments.

### 16.4. Interpretation in Concrete Algebras

#### 16.4.1. Term Operations

> [!definition] Definition 16.9: Term operation induced by a term
> Let $\mathbf{A}$ be an $\Omega$-algebra, $n \geq 1$, and $t \in T_{\Omega}(n)$. The **$n$-ary term operation induced by $t$ on $\mathbf{A}$** is
>
> $$
> t^{\mathbf{A}} : A^{n} \to A, \qquad t^{\mathbf{A}}(a_1, \dots, a_n) := \operatorname{ev}_{a}(t), \quad \text{where } a : X_n \to A,\ a(x_i) := a_i.
> $$
>
> The **syntax/operation distinction** is strict: $t$ is a term, $t^{\mathbf{A}}$ a function; distinct terms may induce equal functions (Definition 16.13). Basic operations arise as $f^{\mathbf{A}} = \big(f(x_1, \dots, x_n)\big)^{\mathbf{A}}$, and projections as $x_i^{\mathbf{A}} = \pi_i^n$.

> [!construction] Construction 16.10: Clone interpretation map
> For each $n \geq 1$ define
>
> $$
> \Theta_{\mathbf{A}, n} : T_{\Omega}(n) \to \operatorname{Op}_n(A) := A^{A^{n}}, \qquad \Theta_{\mathbf{A}, n}(t) := t^{\mathbf{A}},
> $$
>
> and write $\Theta_{\mathbf{A}} := (\Theta_{\mathbf{A}, n})_{n \geq 1} : \operatorname{Syn}_{\Omega} \to \operatorname{Op}(A)$ for the arity-indexed family, the **clone interpretation** of syntax in $\mathbf{A}$.

#### 16.4.2. Interpretation Commutes with Superposition

> [!theorem] Theorem 16.11: Interpretation is a clone homomorphism
> For every $\Omega$-algebra $\mathbf{A}$, all $t \in T_{\Omega}(m)$ and $s_1, \dots, s_m \in T_{\Omega}(n)$:
>
> $$
> \Theta_{\mathbf{A}, n}\big( t[s_1, \dots, s_m] \big) \;=\; \Theta_{\mathbf{A}, m}(t) \big[ \Theta_{\mathbf{A}, n}(s_1), \dots, \Theta_{\mathbf{A}, n}(s_m) \big],
> $$
>
> where the right-hand bracket is concrete generalized composition of operations, $p[q_1, \dots, q_m](\vec{a}) := p(q_1(\vec{a}), \dots, q_m(\vec{a}))$; moreover $\Theta_{\mathbf{A}}$ sends projection terms to projection operations. **Interpreting after superposing equals composing the interpretations**: delayed evaluation is sound.

> [!proof-sketch] Proof Sketch 16.11
> Fix $\vec{a} \in A^n$ with associated assignment $a$. The left side at $\vec{a}$ is $\operatorname{ev}_a(t[\sigma])$ for $\sigma(x_i) = s_i$; by the substitution lemma (Theorem 14.10) this equals $\operatorname{ev}_{a \star \sigma}(t)$, and $(a \star \sigma)(x_i) = \operatorname{ev}_a(s_i) = s_i^{\mathbf{A}}(\vec{a})$, which is the right side at $\vec{a}$. Projections: the generator clause of evaluation.

#### 16.4.3. Term Clone

> [!definition] Definition 16.12: Term clone of an algebra
> The **term clone** of $\mathbf{A}$ is the image of the clone interpretation,
>
> $$
> \operatorname{Clo}(\mathbf{A}) := \operatorname{im}(\Theta_{\mathbf{A}}), \qquad \operatorname{Clo}_n(\mathbf{A}) := \{\, t^{\mathbf{A}} : t \in T_{\Omega}(n) \,\},
> $$
>
> the family of all **term-definable operations** of $\mathbf{A}$. By Theorem 16.11 it contains the projections and is closed under generalized composition (it is a concrete clone, and indeed the least one containing the basic operations $F_{\mathbf{A}}$); the treatise uses it only as *the homomorphic image of the syntactic clone*, the operation-level analogue of the generated subalgebra of Chapter 17.

### 16.5. Kernels and Parameters

#### 16.5.1. Clone Kernel

> [!definition] Definition 16.13: Clone kernel (equational kernel)
> The **clone kernel** of $\mathbf{A}$ is the arity-indexed family $\ker(\Theta_{\mathbf{A}}) = \big( \equiv_{\mathbf{A}}^{(n)} \big)_{n \geq 1}$, where for $s, t \in T_{\Omega}(n)$:
>
> $$
> s \equiv_{\mathbf{A}}^{(n)} t \quad :\Longleftrightarrow \quad s^{\mathbf{A}} = t^{\mathbf{A}} \ \text{as functions } A^{n} \to A \quad \Longleftrightarrow \quad \operatorname{ev}_a(s) = \operatorname{ev}_a(t) \ \text{for all assignments } a : X_n \to A.
> $$
>
> The pairs in the clone kernel are the **identities** (valid equations) of $\mathbf{A}$ in $n$ variables. The clone kernel is compatible with superposition on both sides (a clone congruence), and on each $T_{\Omega}(n)$ it is a fully invariant-style congruence under context widening; the quotient of $\operatorname{Syn}_{\Omega}$ by it is canonically isomorphic to $\operatorname{Clo}(\mathbf{A})$.

#### 16.5.2. Valuation Kernel

> [!proposition] Proposition 16.14: Clone kernel versus valuation kernel
> For a fixed assignment $a : X_n \to A$, the **valuation kernel** $\ker(\operatorname{ev}_a)$ (Definition 17.7 restricted to $T_{\Omega}(n)$) and the clone kernel satisfy
>
> $$
> \equiv_{\mathbf{A}}^{(n)} \;=\; \bigcap_{a \,:\, X_n \to A} \ker(\operatorname{ev}_a) \;\subseteq\; \ker(\operatorname{ev}_a) \quad \text{for each } a,
> $$
>
> and the inclusion is strict in general: $s \equiv t$ under one assignment is **single-point collapse**, while $s \equiv_{\mathbf{A}} t$ is **identity validity**. Example: in $\mathbf{A} = (\mathbb{N}, +)$ with $a(x_1) = a(x_2) = 0$, the terms $x_1$ and $x_1 + x_2$ are valuation-kernel related at $a$ but are not an identity of $\mathbf{A}$. The valuation kernel is moreover *not* substitution-stable, while the clone kernel is; this is the local/global distinction that recurs in first-order semantics as satisfaction-at-an-assignment versus validity.

> [!proof-sketch] Proof Sketch 16.14
> The displayed equality restates Definition 16.13 pointwise; the inclusion is immediate. Strictness and instability are witnessed by the example and by substituting $x_2 \mapsto x_1$ resp. a fresh assignment.

#### 16.5.3. Polynomial Operations, Briefly

> [!definition] Definition 16.15: Polynomial operations
> An $n$-ary **polynomial operation** of $\mathbf{A}$ is an operation $p : A^{n} \to A$ for which there exist $m \in \mathbb{N}$, a term $t \in T_{\Omega}(n + m)$, and **parameters** $c_1, \dots, c_m \in A$ with
>
> $$
> p(a_1, \dots, a_n) = t^{\mathbf{A}}(a_1, \dots, a_n, c_1, \dots, c_m) \quad \text{for all } \vec{a} \in A^{n}.
> $$
>
> The family of polynomial operations is denoted $\operatorname{PolOp}(\mathbf{A})$; it contains $\operatorname{Clo}(\mathbf{A})$ (the parameter-free case $m = 0$).

> [!warning] Warning 16.16: Three kinds of atoms
> Polynomial operations mix three distinct atom classes, which must not be conflated: **variables** (syntax, freely assignable argument places), **constant symbols** (signature, interpreted in every algebra), and **semantic parameters** (elements of one fixed carrier $A$, not syntax at all unless the signature is expanded by new constant symbols naming them). The syntax-side analogue of parameters is the $X$-part of a context (Definition 15.8). Polynomial clone theory — translations, congruence generation via unary polynomials, affine completeness — is deferred; only the definition and the atom trichotomy are retained for the first-order preparation.

### 16.6. Examples

> [!example] Example 16.17: Term operations and the clone kernel of $(\mathbb{N}, +)$
> Let $\Omega = \{+\}$ (binary) and $\mathbf{A} = (\mathbb{N}, +)$. In $T_{\Omega}(2)$, the terms $x_1 + x_2$ and $x_2 + x_1$ are distinct syntax but induce the same operation, so
>
> $$
> \big(x_1 + x_2,\ x_2 + x_1\big) \in\ \equiv_{\mathbf{A}}^{(2)},
> $$
>
> as do all reassociations of $(x_1 + x_2) + x_3$ in $T_{\Omega}(3)$: commutativity and associativity are identities of $\mathbf{A}$, i.e. clone-kernel pairs. By contrast $x_1$ and $x_1 + x_1$ induce the distinct operations $a \mapsto a$ and $a \mapsto 2a$, so they are separated by the clone kernel although the single assignment $a(x_1) = 0$ relates them in the valuation kernel — Proposition 16.14 in numbers.

> [!example] Example 16.18: A polynomial operation that is not a term operation
> In $\mathbf{A} = (\mathbb{N}, +)$, the operation $p(a) := a + 2$ is polynomial: $p(a) = t^{\mathbf{A}}(a, 2)$ for $t := x_1 + x_2 \in T_{\Omega}(2)$ with parameter $2$. It is not a term operation: every $t \in T_{\Omega}(1)$ over the signature $\{+\}$ induces $a \mapsto k a$ for some $k \geq 1$, and no such map is $a \mapsto a + 2$. Hence $\operatorname{Clo}_1(\mathbf{A}) \subsetneq \operatorname{PolOp}_1(\mathbf{A})$: parameters genuinely extend definability, and they do so with semantic data, not syntax (Warning 16.16).

> [!proposition] Proposition 16.19: The term clone is the least clone containing the basic operations
> For every $\Omega$-algebra $\mathbf{A}$, $\operatorname{Clo}(\mathbf{A})$ is the least arity-indexed family of operations on $A$ that contains all projections and all basic operations $f^{\mathbf{A}}$ and is closed under generalized composition.

> [!proof-sketch] Proof Sketch 16.19
> Containment of $\operatorname{Clo}(\mathbf{A})$ in any such family by structural induction on the defining term, using Theorem 16.11 to mirror each constructor application as a composition step. Conversely $\operatorname{Clo}(\mathbf{A})$ itself contains projections (variable terms), the basic operations ($f(x_1, \dots, x_n)$), and is composition-closed (image of a clone homomorphism, Theorem 16.11); minimality follows.

---

# Part VI — Evaluation, Quotients, and Descent
## 17. Evaluation into Target Algebras

Evaluation is the semantic consumption of syntax: a valuation of the generators in a target algebra extends uniquely to a homomorphism on all terms. This chapter develops the evaluation homomorphism, identifies its image with the generated subalgebra (representation existence), its kernel with the relation of semantic collapse, and the quotient $\mathbf{T}_{\Omega}(X)/\ker$ with the generated structure itself — culminating in the criterion that a concrete generated algebra is free exactly when evaluation is injective.

### 17.1. Valuations and Evaluation

#### 17.1.1. Target Algebra

> [!definition] Definition 17.1: Target algebra
> A **target algebra** is an arbitrary $\Omega$-algebra $\mathbf{B}$, fixed as the semantic destination of evaluation. Nothing relates $\mathbf{B}$ to syntax a priori: its elements are not terms, its operations may collapse arguments, and its constants $c^{\mathbf{B}}$ are forced interpretations. The subalgebras of $\mathbf{B}$ generated by chosen elements (Definition 2.4) are the concrete structures that evaluation will present as quotients of syntax.

#### 17.1.2. Valuation

> [!definition] Definition 17.2: Valuation
> A **valuation** of $X$ in $\mathbf{B}$ is an assignment $g : X \to B$ (Definition 3.3). The valuation controls exactly the **generators**; the **constant symbols** are outside its authority, being interpreted by $\mathbf{B}$ itself. The pair $(\mathbf{B}, g)$ is the complete semantic datum: signature interpretation from the algebra, generator values from the valuation.

#### 17.1.3. Evaluation Homomorphism

> [!construction] Construction 17.3: Evaluation homomorphism
> Given $(\mathbf{B}, g)$, the **evaluation homomorphism** is the unique homomorphic extension of $g$ supplied by the UMP (Theorem 4.6):
>
> $$
> \operatorname{ev}_g := \widehat{g} : \mathbf{T}_{\Omega}(X) \longrightarrow \mathbf{B}, \qquad \operatorname{ev}_g \circ \eta_X = g,
> $$
>
> computed by the recursive clauses
>
> $$
> \operatorname{ev}_g(x) = g(x), \qquad \operatorname{ev}_g(c) = c^{\mathbf{B}}, \qquad \operatorname{ev}_g\big(f(t_1, \dots, t_n)\big) = f^{\mathbf{B}}\big(\operatorname{ev}_g(t_1), \dots, \operatorname{ev}_g(t_n)\big).
> $$
>
> The element $\operatorname{ev}_g(t) \in B$ is the **value** of $t$ under $g$ in $\mathbf{B}$. Evaluation is representation-independent: by Proposition 11.9 every presentation evaluates through its transfer map to the same values, so "the value of the term" is well-defined without reference to trees, tuples, or strings. The homomorphism condition is exactly **compositionality**: the value of a compound term is a function of the values of its immediate subterms and the outer symbol.

> [!lemma] Lemma 17.4: Coincidence lemma
> Let $g, g' : X \to B$ be valuations and $t \in T_{\Omega}(X)$. If $g(x) = g'(x)$ for all $x \in \operatorname{var}(t)$, then $\operatorname{ev}_g(t) = \operatorname{ev}_{g'}(t)$: the value of a term depends only on the valuation's restriction to the finitely many variables occurring in it.

> [!proof-sketch] Proof Sketch 17.4
> Structural induction on $t$ using the recursive clauses and the recursive description of $\operatorname{var}$ (Definition 12.10); constants are valuation-independent outright.

### 17.2. Evaluation Image

#### 17.2.1. Image Subalgebra

> [!proposition] Proposition 17.5: The image of evaluation is a subalgebra
> $\operatorname{im}(\operatorname{ev}_g) \leq \mathbf{B}$, and it contains $g[X]$ and every $c^{\mathbf{B}}$.

> [!proof-sketch] Proof Sketch 17.5
> Homomorphic images are subalgebras (Proposition 2.7(i)); $g[X] = \operatorname{ev}_g[\eta_X[X]]$ and $c^{\mathbf{B}} = \operatorname{ev}_g(c)$.

#### 17.2.2. Generated Subalgebra Theorem

> [!theorem] Theorem 17.6: Evaluation image equals generated subalgebra
> For every valuation $g : X \to B$,
>
> $$
> \operatorname{im}(\operatorname{ev}_g) \;=\; \big\langle\, g[X] \,\big\rangle_{\mathbf{B}}.
> $$
>
> Consequently: a subalgebra $\mathbf{C} \leq \mathbf{B}$ is generated by $g[X]$ iff $\mathbf{C} = \operatorname{im}(\operatorname{ev}_g)$; the whole of $\mathbf{B}$ is generated by $g[X]$ iff $\operatorname{ev}_g$ is surjective; and every element of a generated algebra is the value of at least one term — **generatedness is representation existence**.

> [!proof-sketch] Proof Sketch 17.6
> Apply Proposition 2.7(ii) to $h = \operatorname{ev}_g$ and $S = \eta_X[X]$, using generation of the term algebra (Proposition 4.5): $\operatorname{ev}_g[T_{\Omega}(X)] = \operatorname{ev}_g[\langle \eta_X[X] \rangle] = \langle g[X] \rangle_{\mathbf{B}}$. Equivalently, stagewise: stage $k$ of the generated subalgebra consists of values of terms of height $\leq k$.

#### 17.2.3. Evaluation on Presentations

Evaluation from a concrete presentation is the composite with the inverse representation map (Proposition 11.9): $\operatorname{ev}_g^{\mathbf{P}} = \operatorname{ev}_g \circ r_P^{-1}$, and all presentations yield the same values, images, and kernels. For strings the pipeline factors as **parse, then evaluate** — $\operatorname{ev}_g^{\mathbf{Str}} = \operatorname{ev}_g \circ \operatorname{pa}$ — and the two factors must be kept distinct (Remark 9.10): parse failure is a syntax error (no term), evaluation never fails (total operations) but may collapse.

### 17.3. Evaluation Kernels and Quotients

#### 17.3.1. Evaluation Kernel

> [!definition] Definition 17.7: Evaluation kernel
> The **evaluation kernel** of $(\mathbf{B}, g)$ is
>
> $$
> \ker(\operatorname{ev}_g) \;=\; \big\{\, (s, t) \in T_{\Omega}(X)^2 \;:\; \operatorname{ev}_g(s) = \operatorname{ev}_g(t) \,\big\},
> $$
>
> the relation of **semantic equality under $g$**: the set of equations between terms that $(\mathbf{B}, g)$ validates. It contains the diagonal (syntactic equality implies semantic equality); every pair beyond the diagonal is a **semantic collapse** — two distinct pieces of syntax with one value.

> [!theorem] Theorem 17.8: The evaluation kernel is a congruence
> $\ker(\operatorname{ev}_g) \in \operatorname{Con}(\mathbf{T}_{\Omega}(X))$: semantic collapse is compatible with all constructors, hence closed under all contexts (Proposition 15.9). In particular, identified subterms may be exchanged inside any term without changing its value.

> [!proof-sketch] Proof Sketch 17.8
> Proposition 2.11 applied to the homomorphism $\operatorname{ev}_g$; context closure is then Proposition 15.9.

#### 17.3.2. Quotient Theorem

> [!theorem] Theorem 17.9: Generated subalgebras are quotients of syntax
> For every valuation $g : X \to B$, the first isomorphism theorem applied to $\operatorname{ev}_g$ yields a unique isomorphism
>
> $$
> \mathbf{T}_{\Omega}(X) \big/ \ker(\operatorname{ev}_g) \;\xrightarrow{\ \cong\ }\; \big\langle g[X] \big\rangle_{\mathbf{B}}, \qquad [t] \longmapsto \operatorname{ev}_g(t),
> $$
>
> and the canonical factorization
>
> $$
> \mathbf{T}_{\Omega}(X) \ \twoheadrightarrow\ \mathbf{T}_{\Omega}(X)/\ker(\operatorname{ev}_g) \ \xrightarrow{\ \cong\ }\ \big\langle g[X] \big\rangle_{\mathbf{B}} \ \hookrightarrow\ \mathbf{B}.
> $$
>
> Every generated target algebra is **syntax modulo semantic identification**, and the kernel is the exact measure of the identification: nothing is collapsed except what the kernel records, and everything the kernel records is collapsed.

> [!proof-sketch] Proof Sketch 17.9
> Theorem 2.16 with $h = \operatorname{ev}_g$, composed with Theorem 17.6 to identify the image.

#### 17.3.3. Concrete Freeness Criterion

> [!theorem] Theorem 17.10: Freeness criterion for generated subalgebras
> Let $\mathbf{C} := \langle g[X] \rangle_{\mathbf{B}}$ with evaluation corestricted to $\operatorname{ev}_g : \mathbf{T}_{\Omega}(X) \to \mathbf{C}$. The following are equivalent:
>
> 1. $(\mathbf{C}, g)$ is a free $\Omega$-algebra on $X$;
> 2. $\operatorname{ev}_g$ is injective (hence bijective onto $\mathbf{C}$);
> 3. $\ker(\operatorname{ev}_g) = \Delta$ (trivial kernel: no accidental identifications);
> 4. every element of $C$ is the value of exactly one term (unique representation);
> 5. the restricted operations of $\mathbf{C}$ are injective with pairwise disjoint ranges, disjoint from $g[X]$, and $g$ is injective (internal unique decomposition, Definition 5.8 for the internal constructor system).
>
> Surjectivity holds always (Theorem 17.6); freeness is the addition of injectivity:
>
> $$
> \text{freeness} \;=\; \text{generatedness} \;+\; \text{trivial kernel}.
> $$

> [!proof-sketch] Proof Sketch 17.10
> (2) $\Leftrightarrow$ (3) is Proposition 2.11/Definition 2.8; (2) $\Leftrightarrow$ (4) is surjectivity plus injectivity read elementwise; (2) $\Rightarrow$ (1) transports freeness along the isomorphism $\operatorname{ev}_g$ over $X$; (1) $\Rightarrow$ (2) by Theorem 3.8 comparing $(\mathbf{C}, g)$ with $(\mathbf{T}_{\Omega}(X), \eta_X)$: the comparison is mutually inverse with $\operatorname{ev}_g$. (5) $\Leftrightarrow$ (2) is Theorem 5.12 applied to the internal constructor system of $\mathbf{C}$.

> [!example] Example 17.11: A free and a non-free generated structure
> (i) Let $\Omega = \{\mathsf{s}\}$ with $\operatorname{ar}(\mathsf{s}) = 1$, $X = \{x\}$, $\mathbf{B} = (\mathbb{N}, n \mapsto n + 1)$, $g(x) = 0$. Then $\operatorname{ev}_g(\mathsf{s}^k(x)) = k$; evaluation is a bijection onto $\langle \{0\} \rangle = \mathbb{N}$, the kernel is trivial, and $(\mathbb{N}, +1)$ with basepoint $0$ is free on one generator — the Peano successor structure. (ii) Let $\Omega = \{\cdot\,, e\}$ (binary, nullary), $\mathbf{B} = (\mathbb{N}, +, 0)$, $X = \{x\}$, $g(x) = 1$. Then $(x \cdot e,\ x) \in \ker(\operatorname{ev}_g)$ and $\big((x \cdot x) \cdot x,\ x \cdot (x \cdot x)\big) \in \ker(\operatorname{ev}_g)$ although the terms are distinct: the kernel is nontrivial, $\langle \{1\} \rangle = \mathbb{N}$ is *not* free on $\{1\}$ in this signature, and Theorem 17.9 exhibits it as term syntax modulo the unit and associativity (and commutativity-instances) collapses.

> [!warning] Warning 17.12: Injectivity of the valuation does not give freeness
> Injectivity of $g$ is necessary for freeness (distinct generators with equal values collapse immediately) but far from sufficient: the generators may be pairwise distinct yet satisfy relations, as in Example 17.11(ii) where the single generator value $1$ satisfies unit laws it never asked for. Freeness requires injectivity of the **entire** evaluation map, i.e. algebraic independence of the generator values, not merely their distinctness.

### 17.4. Naturality and Consequences

> [!proposition] Proposition 17.13: Naturality of evaluation along homomorphisms
> Let $h : \mathbf{B} \to \mathbf{C}$ be a homomorphism of $\Omega$-algebras and $g : X \to B$ a valuation. Then
>
> $$
> h \circ \operatorname{ev}_g \;=\; \operatorname{ev}_{\,h \circ g\,} \;:\; \mathbf{T}_{\Omega}(X) \to \mathbf{C} :
> $$
>
> evaluating and then mapping equals evaluating under the pushed-forward valuation. Together with the substitution lemma (Theorem 14.10), evaluation is natural in both available directions: precomposition with syntax maps and postcomposition with algebra maps.

> [!proof-sketch] Proof Sketch 17.13
> Both sides are homomorphisms agreeing on generators ($h(g(x))$); Lemma 3.5.

> [!corollary] Corollary 17.14: Canonical interpretation of ground terms
> For ground terms the valuation is irrelevant: the restriction of every $\operatorname{ev}_g$ to $T_{\Omega}(\varnothing) \subseteq T_{\Omega}(X)$ is the unique homomorphism $\mathbf{T}_{\Omega}(\varnothing) \to \mathbf{B}$ (initiality, Example 3.11), and every homomorphism $\mathbf{B} \to \mathbf{C}$ commutes with these canonical interpretations. A ground term thus has a well-defined value in every algebra before any assignment is chosen.

> [!proof-sketch] Proof Sketch 17.14
> Lemma 17.4 with $\operatorname{var}(t) = \varnothing$ gives valuation-independence; uniqueness is the UMP on the empty generator set; the commutation square is Proposition 17.13 restricted.

> [!corollary] Corollary 17.15: Every algebra is a quotient of free syntax
> For every $\Omega$-algebra $\mathbf{B}$ there exist a generator set $X$ and a valuation $g$ with $\operatorname{ev}_g$ surjective — e.g. $X := B$ and $g := \mathrm{id}_B$ — whence $\mathbf{B} \cong \mathbf{T}_{\Omega}(B)/\ker(\operatorname{ev}_{\mathrm{id}})$. The class of $\Omega$-algebras coincides with the class of quotients of absolutely free $\Omega$-algebras; syntax-plus-identification exhausts algebra.

> [!proof-sketch] Proof Sketch 17.15
> $\langle \mathrm{id}[B] \rangle_{\mathbf{B}} = B$ since the generated subalgebra contains every element; apply Theorem 17.9.

> [!remark] Remark 17.16: The Boolean target and the propositional preview
> Taking $\Omega$ to be the Boolean signature $\{\vee, \wedge, \neg, \mathbf{0}, \mathbf{1}\}$, $X$ a set of propositional letters, and the two-element target $\mathbf{2}$, the present chapter *is* the semantics of propositional formulas: a valuation $g : X \to \{0, 1\}$ is a truth assignment, $\operatorname{ev}_g$ is the truth-value computation (compositionality = homomorphy), the evaluation kernel under $g$ relates formulas with equal truth value at $g$, and the intersection of all such kernels — the clone-kernel analogue — is logical equivalence. The first-order development will replace $\mathbf{2}$ by structures and add quantifiers; the algebraic skeleton of "evaluate by unique homomorphic extension, measure collapse by the kernel" is unchanged. This instance also calibrates expectations: the kernel is enormous (only $2^{2^{|X|}}$ many classes for finite $X$ against infinitely many formulas), illustrating how far evaluation is from injective in logical practice.

---
## 18. Quotient Syntax and Descent

Raw syntax never identifies; identification is imposed by passing to a quotient by a congruence — typically the congruence generated by a set of equations. Quotient syntax loses unique decomposition, and with it the unconditional recursion principle; what survives is a **descent calculus**: a map on raw syntax passes to the quotient exactly when its kernel contains the congruence. This chapter develops quotient syntax, the descent condition, and its three instantiations (recursion, evaluation, substitution), closing with fully invariant congruences and the local/global kernel distinction.

### 18.1. Quotient Syntax

#### 18.1.1. Congruence on Syntax

> [!definition] Definition 18.1: Equations and the congruence they generate
> An **equation** over $(\Omega, X)$ is an ordered pair $(s, t) \in T_{\Omega}(X)^2$, written $s \approx t$. For a set $E \subseteq T_{\Omega}(X)^2$ of equations, the **syntactic congruence generated by $E$** is
>
> $$
> \theta_E := \operatorname{Cg}_{\mathbf{T}_{\Omega}(X)}(E),
> $$
>
> the least congruence on the term algebra containing $E$ (Construction 2.10). Equations are here read as **ground relations on the fixed generators** — no substitution instances are taken; the substitution-stable reading is Definition 18.11. Full equational logic (derivation systems, completeness) is deferred beyond this treatise.

#### 18.1.2. Quotient Projection

> [!definition] Definition 18.2: Quotient syntax
> For $\theta \in \operatorname{Con}(\mathbf{T}_{\Omega}(X))$, the **quotient syntax algebra** is $\mathbf{T}_{\Omega}(X)/\theta$ (Definition 2.12), with **quotient projection**
>
> $$
> \operatorname{nat}_\theta : \mathbf{T}_{\Omega}(X) \longrightarrow \mathbf{T}_{\Omega}(X)/\theta, \qquad t \longmapsto [t]_\theta,
> $$
>
> and generator map $\overline{\eta} := \operatorname{nat}_\theta \circ \eta_X$. Quotient syntax is **syntax modulo equations**: its elements are classes of interprovably identified terms, its operations act on representatives, and $\operatorname{nat}_\theta$ is the canonical syntax-to-classes map. For $\theta = \theta_E$ one writes $s =_E t$ for $(s,t) \in \theta_E$.

> [!theorem] Theorem 18.3: Derivational description of $\theta_E$
> $\theta_E$ is the least relation on $T_{\Omega}(X)$ containing $E$ and closed under
>
> $$
> \textbf{(refl)}\ s \approx s; \qquad \textbf{(sym)}\ \frac{s \approx t}{t \approx s}; \qquad \textbf{(trans)}\ \frac{s \approx t \quad t \approx u}{s \approx u};
> $$
>
> $$
> \textbf{(cong)}\ \frac{s_1 \approx t_1 \ \cdots \ s_n \approx t_n}{f(s_1, \dots, s_n) \approx f(t_1, \dots, t_n)} \quad (f \in \Omega_n).
> $$
>
> Equivalently, $\theta_E$ is the least equivalence relation containing $E$ and closed under **replacement of equals in arbitrary contexts**: $(s, t) \in \theta_E$ implies $(C[s], C[t]) \in \theta_E$ for every one-hole context $C$. There is **no substitution rule**: this is ground derivability.

> [!proof-sketch] Proof Sketch 18.3
> The relation closed under the four rules is an equivalence compatible with all constructors, hence a congruence containing $E$; conversely every congruence containing $E$ is closed under the rules. The context formulation is Proposition 15.9. Stabilization of the bottom-up closure at stage $\omega$ uses finitary arity.

#### 18.1.3. Loss of Raw Unique Decomposition

> [!warning] Warning 18.4: Quotient classes have no unique decomposition
> In $\mathbf{T}_{\Omega}(X)/\theta$ the unique-readability trichotomy fails in general: a class may contain a variable and a compound term ($[x] = [f(y)]$ if $\theta$ identifies them), or compound terms with different outer symbols, and the operations of the quotient need not be injective or have disjoint ranges. Consequently the quotient is **not** free on $\overline{\eta}[X]$ unless $\theta = \Delta$, and any definition that begins "by recursion on the structure of the class" is ill-formed as stated: classes have no canonical structure, only representatives do. The repair is the descent condition below; the convenient sufficient situations are normal-form systems (a canonical representative per class), which belong to rewriting theory and are outside scope.

### 18.2. Descent

#### 18.2.1. Descent Condition

> [!theorem] Theorem 18.5: Descent along the quotient projection
> Let $\theta \in \operatorname{Con}(\mathbf{T}_{\Omega}(X))$, $V$ a set, and $\Psi : T_{\Omega}(X) \to V$ any function. There exists a function $\widetilde{\Psi} : T_{\Omega}(X)/\theta \to V$ with
>
> $$
> \widetilde{\Psi} \circ \operatorname{nat}_\theta = \Psi
> $$
>
> iff $\Psi$ is constant on $\theta$-classes, i.e. iff
>
> $$
> \theta \subseteq \ker \Psi,
> $$
>
> and $\widetilde{\Psi}$ is then unique. If moreover $V = B$ for an algebra $\mathbf{B}$ and $\Psi$ is a homomorphism, then $\widetilde{\Psi}$ is a homomorphism (Theorem 2.15). **Kernel containment is the universal well-definedness test** for passing from raw syntax to quotient syntax.

> [!proof-sketch] Proof Sketch 18.5
> Necessity: $\widetilde{\Psi}([s]) = \widetilde{\Psi}([t])$ whenever $[s] = [t]$. Sufficiency: define $\widetilde{\Psi}([t]) := \Psi(t)$; constancy on classes is exactly well-definedness; uniqueness by surjectivity of $\operatorname{nat}_\theta$. The homomorphism clause is the quotient UMP.

#### 18.2.2. Recursion Modulo Equations

> [!proposition] Proposition 18.6: Recursion on quotient syntax
> Let $\mathcal{D}$ be recursion data with induced $\operatorname{fold}_{\mathcal{D}} : T_{\Omega}(X) \to V$ (Theorem 13.4), and let $\theta = \theta_E$. The clauses of $\mathcal{D}$ define a function on $\mathbf{T}_{\Omega}(X)/\theta_E$ (via representatives) iff
>
> $$
> \theta_E \subseteq \ker(\operatorname{fold}_{\mathcal{D}}),
> $$
>
> and it suffices to check the generating equations: if $\operatorname{fold}_{\mathcal{D}}(s) = \operatorname{fold}_{\mathcal{D}}(t)$ for every $(s, t) \in E$, then the containment holds.

> [!proof-sketch] Proof Sketch 18.6
> The first clause is Theorem 18.5. For the sufficiency of generators: $\ker(\operatorname{fold}_{\mathcal{D}})$ is a congruence (kernel of the homomorphism onto the installed algebra $\mathbf{A}_V$, Proposition 13.5), and a congruence containing $E$ contains the least such, $\theta_E$.

> [!warning] Warning 18.7: Free recursion is automatic; quotient recursion is conditional
> On raw syntax every recursion datum defines a function ($\theta = \Delta$ makes descent vacuous); on quotient syntax only $E$-respecting data do, and the respect condition is a genuine proof obligation discharged equation by equation. Treating "define by induction on equivalence classes" as automatic is the standard error flagged in Warning 13.7; the corrected workflow is **lift to representatives, define by free recursion, verify descent**. Equational rewriting (orienting $E$ into reduction rules with unique normal forms) is the systematic technology for producing canonical representatives and is deferred.

#### 18.2.3. Evaluation Through Quotients

> [!theorem] Theorem 18.8: Factorization of evaluation through quotient syntax
> Let $\theta \in \operatorname{Con}(\mathbf{T}_{\Omega}(X))$ and let $(\mathbf{B}, g)$ be a target with evaluation $\operatorname{ev}_g$. The evaluation factors through quotient syntax,
>
> $$
> \operatorname{ev}_g = \widetilde{\operatorname{ev}_g} \circ \operatorname{nat}_\theta \quad \text{for a (unique) homomorphism} \quad \widetilde{\operatorname{ev}_g} : \mathbf{T}_{\Omega}(X)/\theta \to \mathbf{B},
> $$
>
> iff $\theta \subseteq \ker(\operatorname{ev}_g)$; for $\theta = \theta_E$ this holds iff $(\mathbf{B}, g)$ **validates every equation of $E$** (i.e. $\operatorname{ev}_g(s) = \operatorname{ev}_g(t)$ for all $(s,t) \in E$). In that case the image and kernel of $\widetilde{\operatorname{ev}_g}$ are the image of $\operatorname{ev}_g$ and $\ker(\operatorname{ev}_g)/\theta$ respectively, and the quotient-syntax algebra evaluates wherever its equations hold.

> [!proof-sketch] Proof Sketch 18.8
> Theorem 18.5 (homomorphism clause) plus Proposition 18.6's generator reduction applied to $\ker(\operatorname{ev}_g)$, which is a congruence (Theorem 17.8). The image claim is surjectivity of $\operatorname{nat}_\theta$; the kernel claim is direct computation with classes.

> [!corollary] Corollary 18.9: Universal property of presented quotient syntax
> Let $E \subseteq T_{\Omega}(X)^2$ and write $\langle X \mid E \rangle := \mathbf{T}_{\Omega}(X)/\theta_E$ with generator map $\overline{\eta}$. For every $\Omega$-algebra $\mathbf{B}$ and every valuation $g : X \to B$ validating $E$, there is a **unique** homomorphism $g^{\sharp} : \langle X \mid E \rangle \to \mathbf{B}$ with $g^{\sharp} \circ \overline{\eta} = g$. The quotient syntax algebra is thus universal among algebras-with-valuations satisfying the prescribed ground equations; the case $E = \varnothing$ recovers the UMP of free syntax.

> [!proof-sketch] Proof Sketch 18.9
> Existence is Theorem 18.8 ($g^{\sharp} = \widetilde{\operatorname{ev}_g}$); uniqueness follows from surjectivity of $\operatorname{nat}_{\theta_E}$ and the uniqueness clause of the raw UMP.

Semantic validity of equations is thereby converted into a factorization property — the form in which "models of a theory" will enter the first-order development: a structure validating the equations of a presentation receives a canonical homomorphism from the presented (quotient) syntax.

### 18.3. Substitution on Quotients

#### 18.3.1. Substitution Compatibility

> [!theorem] Theorem 18.10: Quotient substitution criterion
> Let $\theta \in \operatorname{Con}(\mathbf{T}_{\Omega}(X))$, $\psi \in \operatorname{Con}(\mathbf{T}_{\Omega}(Y))$, and $\sigma : X \to T_{\Omega}(Y)$ with extension $\widehat{\sigma}$. There is a (unique) homomorphism
>
> $$
> \overline{\sigma} : \mathbf{T}_{\Omega}(X)/\theta \longrightarrow \mathbf{T}_{\Omega}(Y)/\psi, \qquad \overline{\sigma}\big([t]_\theta\big) = \big[\widehat{\sigma}(t)\big]_\psi,
> $$
>
> iff $\widehat{\sigma}$ carries identified terms to identified terms:
>
> $$
> (s, t) \in \theta \;\Longrightarrow\; \big(\widehat{\sigma}(s),\, \widehat{\sigma}(t)\big) \in \psi, \qquad \text{i.e.} \qquad \theta \subseteq (\widehat{\sigma} \times \widehat{\sigma})^{-1}[\psi].
> $$

> [!proof-sketch] Proof Sketch 18.10
> Apply Theorem 18.5 to $\Psi := \operatorname{nat}_\psi \circ \widehat{\sigma}$, whose kernel is $(\widehat{\sigma} \times \widehat{\sigma})^{-1}[\psi]$. The criterion is the well-definedness test for substitution between quotient syntaxes; Corollary 14.11 is the special case $\theta = \ker(\operatorname{ev}_{w \star \sigma})$, $\psi = \ker(\operatorname{ev}_w)$, where the containment holds with equality.

#### 18.3.2. Fully Invariant Congruences

> [!definition] Definition 18.11: Fully invariant congruence
> Let $V$ be a variable reservoir. A congruence $\theta \in \operatorname{Con}(\mathbf{T}_{\Omega}(V))$ is **fully invariant** if it is stable under every endosubstitution (Definition 14.3):
>
> $$
> (s, t) \in \theta \;\Longrightarrow\; \big(\widehat{\sigma}(s),\, \widehat{\sigma}(t)\big) \in \theta \qquad \text{for every } \sigma : V \to T_{\Omega}(V).
> $$
>
> Equivalently: $\theta$ is closed under substitution of arbitrary terms for variables, i.e. under taking **substitution instances** of its pairs. The fully invariant congruences form a closure system, so every equation set $E$ generates a least fully invariant congruence $\theta_E^{\mathrm{fi}} \supseteq \theta_E$.

> [!corollary] Corollary 18.12: Endosubstitutions descend on fully invariant quotients
> If $\theta$ is fully invariant, every endosubstitution $\widehat{\sigma}$ of $\mathbf{T}_{\Omega}(V)$ descends to an endomorphism of $\mathbf{T}_{\Omega}(V)/\theta$. Fully invariant congruences are exactly the congruences for which **all** substitutions are automatically legitimate on the quotient — the design requirement of equational logic, where equations are schemata closed under instantiation.

> [!proof-sketch] Proof Sketch 18.12
> Theorem 18.10 with $\psi = \theta$ and the stability hypothesis discharging the criterion; conversely, descent of all endosubstitutions forces stability by applying the descended maps to generating pairs.

#### 18.3.3. Valuation Kernels versus Equational Theories

> [!warning] Warning 18.13: Local kernels are not theories
> Three identification relations on syntax must be kept apart.
>
> 1. The **valuation kernel** $\ker(\operatorname{ev}_g)$: equality under **one** assignment into **one** algebra. A congruence, but in general *not* fully invariant — $x \cdot y \approx y \cdot x$ may hold under $g$ with $g(x) = g(y)$ while a substitution instance fails.
> 2. The **clone kernel / identity relation** of an algebra (Definition 16.13): equality under **all** assignments into one algebra. Fully invariant.
> 3. An **equational theory** $\theta_E^{\mathrm{fi}}$: the substitution-stable congruence generated by postulated equations, the syntactic side of validity in **all** models of $E$.
>
> Reading a ground relation set $E$ as a schematic theory (or conversely) changes the quotient: $\theta_E \subseteq \theta_E^{\mathrm{fi}}$ with strictness typical — e.g. the single ground equation $x \approx y$ on two fixed generators collapses only terms along that pair under $\theta_E$, while as a schema it collapses everything to a point. Quotients by relations of kind 2 and 3 are the **relatively free algebras** (free in an equational class); their theory — Birkhoff's variety theorem, completeness of equational deduction — is the natural continuation of this chapter and is deliberately deferred, as is the analogous local/global distinction in first-order semantics (satisfaction under an assignment versus validity).

### 18.4. Examples

> [!example] Example 18.14: Ground equation versus schematic equation
> Let $\Omega = \{\cdot\}$ (binary), $X \supseteq \{x, y, z\}$, and $E := \{\, x \cdot y \approx y \cdot x \,\}$ — one ground equation on the two fixed generators $x, y$. Then $\theta_E$ relates $C[x \cdot y]$ to $C[y \cdot x]$ for every context $C$ (Theorem 18.3) but does **not** relate $x \cdot z$ to $z \cdot x$: no rule of ground derivability instantiates variables. The fully invariant congruence $\theta_E^{\mathrm{fi}}$ additionally contains every substitution instance $\big(s \cdot t,\, t \cdot s\big)$ — the schematic, "law of commutativity" reading. The two quotients differ: $\mathbf{T}_{\Omega}(X)/\theta_E$ still distinguishes $x \cdot z$ from $z \cdot x$, while $\mathbf{T}_{\Omega}(X)/\theta_E^{\mathrm{fi}}$ is the free commutative magma. Choosing the wrong reading silently changes the presented object (Warning 18.13).

> [!example] Example 18.15: Descent succeeding and failing
> Take $\theta := \theta^{\mathrm{fi}}_{\{x \cdot y \approx y \cdot x\}}$ on $\mathbf{T}_{\Omega}(V)$, $\Omega = \{\cdot\}$. (i) The fold $\operatorname{var}$ (variable set, Definition 12.10) satisfies $\operatorname{var}(s \cdot t) = \operatorname{var}(t \cdot s)$ on the generating pairs and its clauses are symmetric, so $\theta \subseteq \ker(\operatorname{var})$ and $\operatorname{var}$ descends to commutative quotient syntax (Proposition 18.6). (ii) The fold "leftmost variable" $L$ with $L(s \cdot t) := L(s)$ does **not** descend: $L(x \cdot y) = x \neq y = L(y \cdot x)$ on a generating pair, so $\theta \not\subseteq \ker L$ and the would-be definition "$L$ of a class" assigns two values to $[x \cdot y]_\theta$. The descent condition is exactly the boundary between the two cases.

> [!remark] Remark 18.16: Existence of the quotient versus decidability of its equality
> For every equation set $E$ the quotient $\mathbf{T}_{\Omega}(X)/\theta_E$ exists as a set-theoretic object (Definition 18.2): existence is unconditional. **Effectivity is a separate matter**: there is in general no algorithm deciding $s =_E t$ from $s, t, E$ — for suitable finite $E$ the relation $\theta_E^{\mathrm{fi}}$ (and already $\theta_E$ in expanded signatures) is undecidable, the word-problem phenomenon. The treatise's standing distinction between *existence of an object* and *effective construction or decision* is sharpest here: quotient syntax always exists, canonical representatives need not be computable, and the rewriting technology that sometimes supplies them (orientation of equations, confluence, normal forms) is deferred to a companion development. No statement in this chapter asserts computability.

---

# Part VII — Synthesis
## 19. Synthesis: The Algebraic Syntax Schemes

This closing chapter compresses the treatise into its architecture: three levels of objects, four families of maps, three master diagrams, and a table of reusable construction schemes. Nothing new is proved; every entry points back to its formal home.

### 19.1. Three-Level Architecture

#### 19.1.1. Abstract Syntax Object

At the center stands the invariant syntax object $\mathbf{T}_{\Omega}(X)$ — the free $\Omega$-algebra on $X$, defined by the universal mapping property (Definition 3.4), realized canonically by formal terms (Theorem 4.6), and unique up to a unique isomorphism over $X$ (Theorem 3.8). The UMP supplies, as instances of one mechanism: structural induction (generation, Theorem 4.9), structural recursion (unique extension, Theorem 4.10), substitution (syntax-valued extension, Theorem 14.4), and evaluation (target-valued extension, Construction 17.3). Every other object in the treatise is a realization, a reorganization, an image, or a quotient of this one.

#### 19.1.2. Concrete Presentations

Around the hub sit the certified realizations: term expressions (Theorem 6.7), labelled ranked trees (Theorem 7.8), tagged tuples (Theorem 8.6), and hygienic strings (Theorem 9.8) — each verified by the construction engine's two checklists (generated closure, Construction 5.4; disjointness and injectivity, Definition 5.8) through the comparison-map criterion (Theorem 5.12). They are canonically isomorphic over $X$, **not** literally identical (Theorem 11.10, Warning 11.11); presentation choice is use-case-driven: trees for positions and occurrences, tuples for set-theoretic coding, strings for input/output under parsing, expressions for human notation.

#### 19.1.3. Semantic Target Algebras

Below the syntax levels sit arbitrary target algebras $\mathbf{B}$, receiving syntax through evaluation: the image of evaluation is the generated subalgebra (Theorem 17.6), the kernel is the record of semantic identification (Definition 17.7, Theorem 17.8), the first isomorphism theorem exhibits every generated target structure as syntax modulo its kernel (Theorem 17.9), and freeness of a concrete structure is triviality of the kernel (Theorem 17.10).

### 19.2. Fundamental Maps

#### 19.2.1. Representation-Level Maps

Representation maps $r_P : \mathbf{T}_{\Omega}(X) \to \mathbf{P}$ identify concrete carriers with abstract syntax (Definition 11.1); transfer maps $\tau_{P,Q} = r_Q \circ r_P^{-1}$ move between presentations coherently (Construction 11.4); parsers $\operatorname{pa} : W_{\Omega}(X) \to T_{\Omega}(X)$ carry external linear representations into syntax, partially and with failure on malformed input (Definition 9.5). All are generator-preserving, and the parser is the inverse of a representation map under hygiene (Theorem 9.6).

#### 19.2.2. Syntax-Level Maps

Substitutions $\widehat{\sigma} : \mathbf{T}_{\Omega}(X) \to \mathbf{T}_{\Omega}(Y)$ carry syntax to syntax by the UMP (Theorem 14.4), with identity and associative composition (Proposition 14.7, Theorem 14.9). Contexts induce derived syntax operations by hole-substitution (Construction 15.4, Definition 15.8), with replacement-at-a-position as their occurrence-level instance (Proposition 15.7). The syntactic clone $\operatorname{Syn}_{\Omega}$ organizes arity-indexed terms under formal superposition with projection units (Definition 16.6, Theorem 16.5).

#### 19.2.3. Semantic and Quotient Maps

Evaluations $\operatorname{ev}_g : \mathbf{T}_{\Omega}(X) \to \mathbf{B}$ carry syntax to semantics (Construction 17.3); clone interpretations $\Theta_{\mathbf{A}} : \operatorname{Syn}_{\Omega} \to \operatorname{Op}(A)$ carry formal operations to term operations, commuting with superposition (Construction 16.10, Theorem 16.11); quotient projections $\operatorname{nat}_\theta : \mathbf{T}_{\Omega}(X) \to \mathbf{T}_{\Omega}(X)/\theta$ carry raw syntax to syntax modulo identifications (Definition 18.2), with descent governed by kernel containment (Theorem 18.5).

### 19.3. Master Diagrams

#### 19.3.1. Presentation Transfer Diagram

All presentations connect through the hub by unique isomorphisms over $X$:

$$
\mathbf{Expr}_{\Omega}(X) \ \overset{r_{\mathrm{expr}}}{\cong} \ \mathbf{T}_{\Omega}(X) \ \overset{r_{\mathrm{tree}}}{\cong} \ \mathbf{Tree}_{\Omega}(X), \qquad \mathbf{Tup}_{\Omega}(X) \ \overset{r_{\mathrm{tup}}}{\cong} \ \mathbf{T}_{\Omega}(X) \ \overset{r_{\mathrm{str}}}{\cong} \ \mathbf{Str}_{\Omega}(X),
$$

$$
\tau_{P,Q} := r_Q \circ r_P^{-1}, \qquad \tau_{Q,R} \circ \tau_{P,Q} = \tau_{P,R}, \qquad \tau_{P,Q} \circ \eta_P = \eta_Q.
$$

The transfer principle (Theorem 11.10): every generator-preserving invariant — operations, destructors, induction, recursion, substitution, contexts, evaluation, kernels, quotients — transports along these maps; encoding-level data do not.

#### 19.3.2. Substitution and Evaluation Diagrams

Substitution extends syntax-to-syntax data; evaluation extends syntax-to-semantics data; the substitution lemma makes the triangle commute:

$$
\sigma : X \to T_{\Omega}(Y) \ \leadsto\ \widehat{\sigma} : \mathbf{T}_{\Omega}(X) \to \mathbf{T}_{\Omega}(Y), \qquad w : Y \to B \ \leadsto\ \operatorname{ev}_w : \mathbf{T}_{\Omega}(Y) \to \mathbf{B},
$$

$$
\operatorname{ev}_w \circ \widehat{\sigma} \;=\; \operatorname{ev}_{\,w \star \sigma}, \qquad (w \star \sigma)(x) = \operatorname{ev}_w(\sigma(x)) \qquad \text{(Theorem 14.10)}.
$$

At the clone level the same compatibility reads: interpretation after superposition equals composition of interpretations (Theorem 16.11).

#### 19.3.3. Quotient Descent Diagram

A map out of raw syntax factors through quotient syntax exactly under kernel containment:

$$
\Psi : \mathbf{T}_{\Omega}(X) \to V \ \text{factors as} \ \widetilde{\Psi} \circ \operatorname{nat}_\theta \quad \Longleftrightarrow \quad \theta \subseteq \ker \Psi \qquad \text{(Theorem 18.5)},
$$

with the three standing instantiations: recursion data descend iff they respect the generating equations (Proposition 18.6); evaluation descends iff the target validates the equations (Theorem 18.8); substitution descends between quotients iff identified terms map to identified terms, automatically for fully invariant congruences (Theorem 18.10, Corollary 18.12).

### 19.4. Master Table of Schemes

#### 19.4.1. Construction Schemes

| Scheme | Input | Output | Mechanism | Home |
|---|---|---|---|---|
| Free syntax | $(\Omega, X)$ | $(\mathbf{T}_{\Omega}(X), \eta_X)$ | least set under formation clauses; UMP | Def. 4.1, Thm. 4.6 |
| Concrete presentation | constructor system $\mathcal{K}$ | candidate $(\mathbf{C}_{\mathcal{K}}, \iota)$ | stage closure + (D1)–(D3), (I) | Def. 5.3, Def. 5.8 |
| Certification | candidate | freeness verdict | comparison map bijective | Thm. 5.12 |
| Transfer | two presentations | unique iso over $X$ | conjugation through hub | Thm. 3.8, Constr. 11.4 |

#### 19.4.2. Operation Schemes

| Scheme | Source of validity | Statement | Home |
|---|---|---|---|
| Structural induction | generatedness (least set) | closed property exhausts syntax | Thm. 4.9 / 13.1 |
| Structural recursion | unique decomposition | recursion data $\Rightarrow$ unique fold | Thm. 4.10 / 13.4, Thm. 5.13 |
| Substitution | UMP into syntax | $\widehat{\sigma}$, laws $\star$, identity | Thm. 14.4, Thm. 14.9 |
| Contexts | substitution over $X \sqcup H_k$ | plugging, replacement, derived ops | Constr. 15.4, Prop. 15.7 |
| Syntactic clone | arity-indexed substitution | superposition, projections, clone laws | Constr. 16.4, Thm. 16.5 |

#### 19.4.3. Semantic Schemes

| Scheme | Input | Output | Governing condition | Home |
|---|---|---|---|---|
| Evaluation | valuation $g : X \to B$ | $\operatorname{ev}_g$ | UMP (none) | Constr. 17.3 |
| Generated image | $(\mathbf{B}, g)$ | $\langle g[X] \rangle_{\mathbf{B}}$ | image = generated | Thm. 17.6 |
| Kernel | $(\mathbf{B}, g)$ | $\ker(\operatorname{ev}_g)$ | semantic equality; congruence | Def. 17.7, Thm. 17.8 |
| Quotient | congruence $\theta$ | $\mathbf{T}_{\Omega}(X)/\theta$ | compatibility = well-definedness | Def. 2.12, Def. 18.2 |
| Descent | $\Psi$, $\theta$ | $\widetilde{\Psi}$ | $\theta \subseteq \ker \Psi$ | Thm. 18.5 |
| Freeness test | generated $(\mathbf{C}, g)$ | free / not free | $\ker(\operatorname{ev}_g) = \Delta$ | Thm. 17.10 |

### 19.5. Final Compression

#### 19.5.1. Single-Sentence Theorem

> [!theorem] Theorem 19.1: The algebraic syntax theorem
> Every correct syntax presentation for $(\Omega, X)$ — every generated carrier with injective, range-disjoint constructors separating atoms — is a free $\Omega$-algebra on $X$; consequently any two are isomorphic by a unique generator-preserving isomorphism, and every invariant syntax operation (decomposition, induction, recursion, substitution, contexts, clone structure, evaluation, kernels, quotients, descent) is defined once on the free object and transfers to all presentations.

> [!proof-sketch] Proof Sketch 19.1
> Concatenation of the spine: Theorem 5.12 (certification), Theorem 3.8 (unique isomorphism), Theorem 11.10 (transfer), with the operation layer supplied by Theorems 13.4, 14.4, 16.5, Construction 17.3, and the quotient layer by Theorems 18.5–18.10.

#### 19.5.2. Bridge to FOL

> [!remark] Remark 19.2: What first-order logic will add
> For a first-order language $\mathcal{L}$ with function symbols $\mathcal{F}$ (with arities) and relation symbols $\mathcal{R}$, the **term layer** is exactly the present theory with $\Omega := \mathcal{F}$ and $X$ the set of individual variables: $\operatorname{Term}_{\mathcal{L}} = T_{\mathcal{F}}(X)$, free, with substitution, evaluation in the algebraic reduct of an $\mathcal{L}$-structure, and the substitution lemma already proved. The forthcoming layers add: **atomic formulas** (relation symbols and equality applied to terms — a new sorted formation layer over the term algebra), **connectives** (a further free-algebra layer over atomic formulas), **quantifiers and binding** (constructors that bind variables, breaking full freeness of substitution and requiring capture-avoidance — the first genuinely new phenomenon), **satisfaction** (evaluation into two-valued or general structures, extending the valuation-kernel theory), and **theories and deduction** (quotient and descent phenomena at the formula level). The term backbone is closed; the relational and binding superstructure is the next development.

#### 19.5.3. What Has Been Achieved

> [!remark] Remark 19.3: Closing inventory
> The syntax backbone is now precise: raw terms exist as an absolutely free algebra characterized by the UMP; four concrete presentations are certified and interchangeable only up to canonical isomorphism; parsing, substitution, evaluation, and quotienting are separated into typed map families with no remaining ambiguity; substitution, contexts, and clones are governed by the UMP rather than by symbol manipulation; generated target structures are quotients of syntax with kernels measuring collapse; and the descent calculus controls every passage to syntax-modulo-equations. The transition to first-order logic can therefore concentrate on relation symbols, satisfaction, binding, and proof systems — the syntax engine itself need never be rebuilt.

---

## Appendix: Symbol Index

| Symbol | Meaning | Defined in |
|---|---|---|
| $\Omega$, $\Omega_n$, $\operatorname{ar}$ | signature, arity classes, arity function | Def. 1.1 |
| $\mathbf{A}$, $A$, $f^{\mathbf{A}}$ | algebra, carrier, interpreted operation | Def. 1.5 |
| $\operatorname{Hom}_{\Omega}$, $\cong$ | homomorphisms, isomorphism | Def. 1.11, 1.13 |
| $\langle S \rangle_{\mathbf{A}}$ | generated subalgebra | Def. 2.4 |
| $\ker h$, $\Delta$, $\nabla$ | kernel, diagonal, total relation | Def. 2.8, 2.9 |
| $\operatorname{Con}(\mathbf{A})$, $\operatorname{Cg}(R)$ | congruences, generated congruence | Def. 2.9, Constr. 2.10 |
| $\mathbf{A}/\theta$, $\operatorname{nat}_\theta$, $[a]_\theta$ | quotient, projection, class | Def. 2.12, 2.14 |
| $\eta$, $\widehat{g}$ | generator insertion, homomorphic extension | Def. 3.2, 3.4 |
| $T_{\Omega}(X)$, $\mathbf{T}_{\Omega}(X)$, $\eta_X$ | term carrier, term algebra, insertion; official prefix coding | Def. 4.1, Constr. 4.3, 4.4, 4.13, Lem. 4.14 |
| $\mathcal{K}$, $C_{\mathcal{K}}$, $\operatorname{rk}$ | constructor system, generated carrier, rank | Def. 5.1, 5.3, 5.6 |
| $r_P$, $\tau_{P,Q}$ | representation map, transfer map | Def. 11.1, Constr. 11.4 |
| $\mathbf{Expr}$, $\mathbf{Tree}$, $\mathbf{Tup}$, $\mathbf{Str}$ | the four presentations | Ch. 6–9 |
| $\operatorname{pa}$, $\operatorname{fl}$, $W_{\Omega}(X)$ | parser, flattening, well-formed strings | Def. 9.5, Constr. 9.4, Def. 9.2 |
| $\operatorname{case}$, $\operatorname{root}$, $\operatorname{comp}_i$ | destructors | Def. 12.1, 12.2 |
| $\operatorname{Pos}(t)$, $t|_p$, $t[s]_p$ | positions, subterm at, replacement | Def. 12.5, 12.7 |
| $\operatorname{ht}$, $\operatorname{sz}$, $\operatorname{var}$, $\#_x$ | height, size, variables, occurrence count | Def. 12.8–12.10 |
| $\sigma$, $\widehat{\sigma}$, $t[\sigma]$, $\tau \star \sigma$ | substitution, extension, application, composite | Def. 14.1, Thm. 14.4, Def. 14.8 |
| $\Box_i$, $H_k$, $C[\vec{s}\,]$, $C_p^t$ | holes, hole sets, plugging, hollowed context | Def. 15.1, Constr. 15.4, Prop. 15.7 |
| $T_{\Omega}(n)$, $t[s_1, \dots, s_m]$, $\operatorname{Syn}_{\Omega}$ | arity-indexed terms, superposition, syntactic clone | Not. 16.1, Constr. 16.4, Def. 16.6 |
| $t^{\mathbf{A}}$, $\Theta_{\mathbf{A}}$, $\operatorname{Clo}(\mathbf{A})$, $\operatorname{PolOp}(\mathbf{A})$ | term operation, interpretation, term clone, polynomial ops | Def. 16.9–16.15 |
| $\equiv_{\mathbf{A}}^{(n)}$ | clone kernel (identities) | Def. 16.13 |
| $\operatorname{ev}_g$ | evaluation homomorphism | Constr. 17.3 |
| $s \approx t$, $E$, $\theta_E$, $=_E$ | equation, equation set, generated congruence | Def. 18.1, 18.2 |
| $\theta_E^{\mathrm{fi}}$ | fully invariant congruence generated by $E$ | Def. 18.11 |
| $\langle X \mid E \rangle$ | presented quotient syntax | Cor. 18.9 |
