---
title: Clones and Term Operations – The Fundamental Galois Connections of Universal Algebra
subtitle: A Companion Treatise on Derived Operations, Invariant Relations, Equational Theories, and Descent Along Evaluation Kernels
tags:
  - universal-algebra
  - clones
  - term-operations
  - polynomial-operations
  - invariant-relations
  - equational-logic
  - fully-invariant-congruence
  - galois-connection
  - syntax-semantics
---

# Clones, Term Operations, and the Two Galois Connections of Universal Algebra

## 0. Orientation

This treatise is the operational companion to *Free Algebras, Term Syntax, and Relational Generation* (cited throughout as **FTS**). FTS develops the *element-level* architecture: the term algebra $\mathbf T_\Omega(X)$, its universal mapping property, evaluation $\operatorname{ev}_g$ into a concrete algebra, the kernel of evaluation, and the quotient description of generated subalgebras. The present treatise develops the *operation-level* architecture above the same foundation: not the elements that syntax denotes, but the **operations** that syntax induces.

The central objects are:

- the **clone** $\operatorname{Clo}(\mathbf A)$ of term operations and the **polynomial clone** $\operatorname{Pol}(\mathbf A)$ of an algebra $\mathbf A$ — the closure of the basic operations under composition with projections (and, for polynomials, constants);
- the **compatibility relations** between operations and the structural apparatus of FTS: subuniverses, homomorphisms, and congruences are exactly the objects *invariant* under all term (equivalently polynomial) operations;
- the **Pol–Inv Galois connection** between operations and relations on a fixed carrier, whose closed sets on the operation side are clones and on the relation side are relational clones;
- the **Id–Mod Galois connection** between equations and algebras, whose closed sets are equational theories — equivalently, **fully invariant congruences** on the term algebra — and varieties;
- the **descent calculus** along evaluation kernels: writing $\kappa_g := \ker(\operatorname{ev}_g)$ for the congruence of semantic identifications forced by a generator assignment $g : X \to |B|$ (FTS Definition 5.4.1), the syntactic clone of polynomial/context operations on raw terms descends to the quotient $\mathbf T_\Omega(X)/\kappa_g \cong \langle g[X]\rangle_B$, and an arbitrary operation on raw syntax descends **exactly** when it sends $\kappa_g$-equivalent input tuples to $\kappa_g$-equivalent outputs.

The last item is the treatise's worked spine (Sections 6–7). It makes precise the navigation problem the whole subject solves: one may *build first and evaluate second* (apply a syntactic context to raw terms, then evaluate), or *evaluate first and build second* (evaluate the inputs, then apply the corresponding concrete polynomial operation), or *work in the quotient throughout*; all three routes agree, and the agreement is precisely the conjunction of the substitution lemma (FTS Theorem 8.3.1) with compatibility of congruences with polynomial operations. Operations outside the polynomial clone enjoy no such guarantee, and the failure is witnessed by explicit case-analysis operations on syntax that are well-defined on terms but not on their $\kappa_g$-classes.

Proofs are omitted by design, as in FTS. Every item states its data and side conditions; warnings isolate precise failure modes. Section 10 collects the two Galois connections and the descent calculus in tabular form.

> [!remark] Remark 0.1: Citation and dependency conventions
> "FTS §$n$" and "FTS Theorem $a.b.c$" refer to the companion treatise; its numbering ($a.b.c$ = section.subsection.item) is also used here. The present treatise is self-contained at the level of *statements*: every imported definition is restated (often in compressed form) before use, with its FTS source cited. Order-theoretic background (complete lattices, closure systems, algebraic lattices, Galois connections and polarities) is used in the standard formulations; the relevant facts are restated where needed.

## 1. Ambient Setting and Notation

### 1.1. Imports from the Companion Treatise

> [!notation] Notation 1.1.1: Set-theoretic ambient
> Work in ZFC, as in FTS Notation 1.1.1. $\mathbb N = \{0,1,2,\dots\}$; $n \in \mathbb N$ is identified with $\{0,\dots,n-1\}$ or with the index set $\{1,\dots,n\}$ as context dictates (tuples are written $(a_1,\dots,a_n)$). For sets: $\mathcal P(S)$, $S^T$, $S^n$, $S^{<\omega}$ as in FTS. Classes appear only in Section 8 (the class of all $\Omega$-algebras) and are handled as in FTS Notation 1.1.1.

> [!notation] Notation 1.1.2: Signature, algebras, terms, evaluation
> Throughout, $\Omega = (\Sigma, \operatorname{ar})$ is a fixed single-sorted signature with finite arities (FTS Definition 1.2.1), $\Omega_n$ its $n$-ary part. Algebras $\mathbf A = (A, (f^{\mathbf A})_{f \in \Omega})$ are written in boldface with carrier $A = |\mathbf A|$ in lightface (a compression of FTS's $|A|$ notation, adopted because carriers and algebras must be distinguished constantly below). Homomorphisms, subalgebras $\operatorname{Sub}(\mathbf A)$, congruences $\operatorname{Con}(\mathbf A)$, quotients, kernels, and the isomorphism theorems are as in FTS §1. The term algebra on a variable set $X$ is $\mathbf T_\Omega(X)$ with carrier $T_\Omega(X)$ and insertion $\eta_X$ (FTS Construction 2.3.1); for a valuation $g : X \to B$, the evaluation homomorphism is $\operatorname{ev}_g : \mathbf T_\Omega(X) \to \mathbf B$ (FTS Construction 5.2.1). Substitutions $\sigma : X \to T_\Omega(Y)$, their extensions $\overline\sigma$, the composite $\tau \bullet \sigma$, and the substitution lemma are as in FTS §8.

> [!notation] Notation 1.1.3: The evaluation kernel $\kappa_g$
> For a target algebra $\mathbf B$ and a generator assignment $g : X \to B$, write
>
> $$
> \kappa_g \;:=\; \ker(\operatorname{ev}_g) \;=\; \{\, (s,t) \in T_\Omega(X)^2 : \operatorname{ev}_g(s) = \operatorname{ev}_g(t) \,\} \;\in\; \operatorname{Con}\big(\mathbf T_\Omega(X)\big),
> $$
>
> the **evaluation kernel** of $(\mathbf B, g)$ (FTS Definition 5.4.1, there written $\ker(\operatorname{ev}_g)$; the symbol $\kappa_g$ is adopted here for the central role the object plays). The defining facts imported from FTS: $\kappa_g$ is a congruence on $\mathbf T_\Omega(X)$; $\operatorname{ev}_g$ is injective iff $\kappa_g = \Delta$; and the first isomorphism theorem yields the canonical isomorphism
>
> $$
> \mathbf T_\Omega(X)\big/\kappa_g \;\xrightarrow{\ \cong\ }\; \big\langle g[X] \big\rangle_{\mathbf B}, \qquad [t]_{\kappa_g} \mapsto \operatorname{ev}_g(t)
> $$
>
> (FTS Theorem 5.5.1). When $\mathbf B$ is generated by $g[X]$, the right-hand side is $\mathbf B$ itself.

> [!notation] Notation 1.1.4: Standard variable supplies
> Fix once and for all the **standard variables** $x_1, x_2, x_3, \dots$ (pairwise distinct, disjoint from $\Omega$), and set
>
> $$
> X_n := \{x_1, \dots, x_n\} \quad (n \in \mathbb N), \qquad X_\omega := \{x_1, x_2, \dots\}.
> $$
>
> Terms in $T_\Omega(X_n)$ are called **$n$-ary terms**; $T_\Omega(X_\omega)$ is the **standard term algebra**. An arbitrary generator set $X$ remains in play for the descent theory of Sections 6–7; the standard supplies are used wherever operations are indexed by arity. The convention $X_n \subseteq X_{n+1} \subseteq X_\omega$ is in force, with the induced inclusions $T_\Omega(X_n) \subseteq T_\Omega(X_{n+1}) \subseteq T_\Omega(X_\omega)$ (a term over fewer variables is a term over more).

### 1.2. Conventions on Operations

> [!definition] Definition 1.2.1: Finitary operations on a set
> Let $A$ be a set and $n \in \mathbb N$. An **$n$-ary operation on $A$** is a function $F : A^n \to A$. The set of all $n$-ary operations is $\mathcal O_A^{(n)} := A^{A^n}$, and the set of all finitary operations is
>
> $$
> \mathcal O_A := \bigcup_{n \in \mathbb N} \mathcal O_A^{(n)}.
> $$
>
> A $0$-ary operation is a function $A^0 = \{()\} \to A$, identified with its unique value, i.e. with an element of $A$. Operations of different arities are distinct objects even when they "ignore" arguments; the arity is part of the data.

> [!definition] Definition 1.2.2: Projections, composition (superposition)
> For $1 \le i \le n$, the **$i$-th $n$-ary projection** on $A$ is
>
> $$
> \pi_i^n : A^n \to A, \qquad \pi_i^n(a_1, \dots, a_n) := a_i.
> $$
>
> For $F \in \mathcal O_A^{(n)}$ and $G_1, \dots, G_n \in \mathcal O_A^{(m)}$ (all of the **same** arity $m$), the **composition** (**superposition**) is
>
> $$
> F(G_1, \dots, G_n) \in \mathcal O_A^{(m)}, \qquad F(G_1,\dots,G_n)(\bar a) := F\big(G_1(\bar a), \dots, G_n(\bar a)\big) \quad (\bar a \in A^m).
> $$
>
> Composition with projections subsumes the **variable manipulations**: permutation of arguments, identification of arguments (diagonalization), and addition of dummy (fictitious) arguments are all of the form $F(\pi_{j_1}^m, \dots, \pi_{j_n}^m)$.

> [!definition] Definition 1.2.3: Essential and fictitious arguments
> Let $F \in \mathcal O_A^{(n)}$. The $i$-th argument of $F$ is **fictitious** (**inessential**) iff $F(\bar a) = F(\bar b)$ whenever $a_j = b_j$ for all $j \neq i$; otherwise it is **essential**. The **essential arity** of $F$ is the number of essential arguments. A constant operation has essential arity $0$; a projection $\pi_i^n$ has essential arity $1$ (provided $|A| \ge 2$).

> [!warning] Warning 1.2.4: Operations versus the functions they induce
> Two distinct formal objects must be kept separate from the outset: a **term** $t \in T_\Omega(X_n)$ (raw syntax, an element of the free algebra, FTS §2) and the **operation** $t^{\mathbf A} \in \mathcal O_A^{(n)}$ it induces on a given algebra (Definition 3.1.1 below). Distinct terms routinely induce the same operation; the discrepancy is governed by the equational theory of $\mathbf A$ (Theorem 3.2.4) and is the operation-level shadow of FTS Warning 2.4.3 (syntactic distinctness vs. semantic equality). The discipline of FTS Notation 1.1.3 — never conflate canonical isomorphism or induced equality with identity — applies to operations exactly as to elements.
## 2. Clones of Operations

### 2.1. The Clone Axioms

> [!definition] Definition 2.1.1: Clone
> Let $A$ be a set. A **clone on $A$** is a subset $\mathcal C \subseteq \mathcal O_A$ such that:
>
> 1. **(projections)** $\pi_i^n \in \mathcal C$ for all $n \ge 1$ and $1 \le i \le n$;
> 2. **(composition)** for all $n, m \ge 1$: if $F \in \mathcal C \cap \mathcal O_A^{(n)}$ and $G_1, \dots, G_n \in \mathcal C \cap \mathcal O_A^{(m)}$, then $F(G_1, \dots, G_n) \in \mathcal C \cap \mathcal O_A^{(m)}$.
>
> Write $\mathcal C^{(n)} := \mathcal C \cap \mathcal O_A^{(n)}$ for the **$n$-ary part**. Two conventions for nullary operations coexist in the literature: clones-with-nullaries close condition 2 under $n$-ary $F$ composed with $0$-ary arguments, while the **default convention here excludes nullary operations from clones** and represents would-be constants by their unary constant counterparts $a^{\flat}(x) := a$. The convention is fixed so that every clone is nonempty in every arity $\ge 1$ and the Pol–Inv theory of Section 5 takes its standard form; statements sensitive to the convention are flagged.

> [!example] Example 2.1.2: First examples of clones
> 1. The **full clone** $\mathcal O_A$ and the **trivial clone** $\mathcal J_A := \{\pi_i^n : n \ge 1,\ 1 \le i \le n\}$ of projections only.
> 2. All **monotone** operations with respect to a fixed partial order $\le$ on $A$ (operations $F$ with $F(\bar a) \le F(\bar b)$ whenever $a_i \le b_i$ for all $i$).
> 3. All operations preserving a fixed subset $S \subseteq A$ (i.e. $F[S^n] \subseteq S$); all operations commuting with a fixed unary bijection.
> 4. All **idempotent** operations: $F(a, a, \dots, a) = a$ for all $a \in A$.
> 5. On $A = \{0,1\}$: the clone of monotone Boolean functions; the clone of linear (affine over $\mathbb F_2$) functions; the clone of self-dual functions. Each is of the form "all operations preserving a relation" — the uniform source of examples is Construction 5.1.3.

> [!proposition] Proposition 2.1.3: Clones form an algebraic closure system
> The set of clones on $A$, ordered by inclusion, is a closure system on $\mathcal O_A$: $\mathcal O_A$ is a clone and arbitrary intersections of clones are clones. The associated closure operator
>
> $$
> F \;\longmapsto\; \langle F \rangle_{\mathrm{clone}} := \bigcap \{\, \mathcal C : F \subseteq \mathcal C,\ \mathcal C \text{ a clone on } A \,\}
> $$
>
> is **finitary** (each element of $\langle F\rangle_{\mathrm{clone}}$ arises by finitely many compositions from finitely many members of $F$ and projections). Consequently the **lattice of clones** $\mathsf{Clones}(A)$ is an algebraic lattice, with compact elements the finitely generated clones; meets are intersections and joins are generated clones, not unions.

> [!remark] Remark 2.1.4: Size of the clone lattice
> On $|A| = 2$ the clone lattice is countable and completely classified (**Post's lattice**: every clone on $\{0,1\}$ is finitely generated, and the lattice is explicitly drawn). For $|A| \ge 3$ the clone lattice has cardinality $2^{\aleph_0}$ (Janov–Mučnik), contains infinite descending and ascending chains, and is not fully classified; its coatoms (the **maximal clones**) are classified for finite $A$ by Rosenberg's theorem. These facts delimit how much explicit description can be expected; the treatise uses only the lattice structure, not the classification.

### 2.2. Clones as Composition-Closed Multisorted Structures

> [!remark] Remark 2.2.1: Abstract clones
> The data $(\mathcal C^{(n)})_{n \ge 1}$ with the distinguished projections and the composition maps satisfies associativity and projection-unit identities making it an **abstract clone** (equivalently: a one-object cartesian multicategory; equivalently, via $n \mapsto \mathcal C^{(n)}$, a finitary algebraic theory in the sense of Lawvere, with $\mathcal C^{(n)} = \operatorname{Hom}(n, 1)$). Every abstract clone is isomorphic to a concrete clone of operations on some set. This treatise works concretely; the abstract formulation is recorded because **clone homomorphisms** (Definition 9.2.1) are most cleanly stated at this level, paralleling the FTS policy of defining free algebras by UMP and only then choosing concrete carriers.

> [!definition] Definition 2.2.2: Clone generated by an indexed family; algebras present clones
> Let $\mathbf A = (A, (f^{\mathbf A})_{f \in \Omega})$ be an $\Omega$-algebra. The **clone of $\mathbf A$** is
>
> $$
> \operatorname{Clo}(\mathbf A) := \big\langle \{ f^{\mathbf A} : f \in \Omega,\ \operatorname{ar}(f) \ge 1 \} \cup \{ (c^{\mathbf A})^{\flat} : c \in \Omega_0 \} \big\rangle_{\mathrm{clone}},
> $$
>
> the clone generated by the basic operations (nullary basic operations entering via their unary constant avatars $(c^{\mathbf A})^\flat$). Conversely, every clone $\mathcal C$ on $A$ is $\operatorname{Clo}(\mathbf A_{\mathcal C})$ for the (generally infinite-signature) algebra $\mathbf A_{\mathcal C} := (A, (F)_{F \in \mathcal C})$ whose basic operations are all members of $\mathcal C$. Thus *clones on $A$ = clones of algebras with carrier $A$*; the signature is a presentation device, the clone is the presentation-invariant content (Definition 9.1.3).

> [!warning] Warning 2.2.3: The clone does not remember the signature
> Different signatures and different basic-operation choices can generate the same clone (e.g. Boolean algebras vs. Boolean rings on the same carrier, Example 9.1.5). Properties defined through the signature (e.g. "is a homomorphism with respect to the listed operations") coincide for all presentations generating the same clone (Proposition 4.1.4), and notions stable under change of presentation are exactly the clone-level notions. Conversely, properties of the *signature presentation itself* — number of operations, their arities, equational axiomatizability by particular laws — are not clone-invariant in any syntax-free sense and must not be transported blindly.
## 3. Term Operations and Polynomial Operations

### 3.1. Term Operations

> [!definition] Definition 3.1.1: Term operation induced by an $n$-ary term
> Let $\mathbf A$ be an $\Omega$-algebra, $n \ge 1$, and $t \in T_\Omega(X_n)$. The **term operation** $t^{\mathbf A} \in \mathcal O_A^{(n)}$ is defined by
>
> $$
> t^{\mathbf A}(a_1, \dots, a_n) := \operatorname{ev}_{v_{\bar a}}(t), \qquad \text{where } v_{\bar a} : X_n \to A,\ v_{\bar a}(x_i) := a_i,
> $$
>
> i.e. the value of $t$ under the valuation sending $x_i$ to $a_i$ (FTS Construction 5.2.1). Explicitly, by the recursive evaluation clauses: $x_i^{\mathbf A} = \pi_i^n$, $c^{\mathbf A}$-the-term induces the constant $(c^{\mathbf A})^\flat$ (as an $n$-ary operation, all arguments fictitious), and $\big(f(t_1,\dots,t_m)\big)^{\mathbf A} = f^{\mathbf A}\big(t_1^{\mathbf A}, \dots, t_m^{\mathbf A}\big)$. By the Coincidence Lemma (FTS Lemma 8.1.2), $t^{\mathbf A}$ is well defined and depends only on the variables occurring in $t$; reading $t \in T_\Omega(X_n) \subseteq T_\Omega(X_m)$ for $m \ge n$ changes $t^{\mathbf A}$ only by addition of fictitious arguments.

> [!theorem] Theorem 3.1.2: The clone of term operations
> For every $\Omega$-algebra $\mathbf A$ and $n \ge 1$,
>
> $$
> \operatorname{Clo}_n(\mathbf A) := \{\, t^{\mathbf A} : t \in T_\Omega(X_n) \,\}, \qquad \operatorname{Clo}(\mathbf A) = \bigcup_{n \ge 1} \operatorname{Clo}_n(\mathbf A),
> $$
>
> i.e. the clone generated by the basic operations (Definition 2.2.2) consists **exactly** of the term operations: closure of the basic operations under projections and superposition produces all $t^{\mathbf A}$ and nothing else. Superposition of term operations is governed by substitution: for $t \in T_\Omega(X_n)$ and $s_1, \dots, s_n \in T_\Omega(X_m)$,
>
> $$
> t^{\mathbf A}\big(s_1^{\mathbf A}, \dots, s_n^{\mathbf A}\big) \;=\; \big(t[x_i \mapsto s_i]\big)^{\mathbf A},
> $$
>
> where $t[x_i \mapsto s_i] := \overline\sigma(t)$ for the substitution $\sigma(x_i) := s_i$ (FTS Definition 8.2.1). This identity is an instance of the substitution lemma (FTS Theorem 8.3.1) and says: **the syntactic substitution calculus presents the composition structure of the clone.**

> [!construction] Construction 3.1.3: The evaluation-of-operations map
> For each $n \ge 1$, define
>
> $$
> \mathsf{op}_n^{\mathbf A} : T_\Omega(X_n) \longrightarrow \operatorname{Clo}_n(\mathbf A), \qquad \mathsf{op}_n^{\mathbf A}(t) := t^{\mathbf A}.
> $$
>
> **Source and target structure:** $T_\Omega(X_n)$ is the carrier of the free algebra $\mathbf T_\Omega(X_n)$; $\operatorname{Clo}_n(\mathbf A) \subseteq A^{A^n}$ is the carrier of a subalgebra of the direct power $\mathbf A^{A^n}$ (operations applied pointwise), since basic operations applied pointwise to term operations are term operations. With this structure, $\mathsf{op}_n^{\mathbf A}$ **is itself an evaluation homomorphism**: it equals $\operatorname{ev}_{v}$ for the valuation $v : X_n \to A^{A^n}$, $v(x_i) := \pi_i^n$. The kernel of $\mathsf{op}_n^{\mathbf A}$ is computed in Theorem 3.2.4; surjectivity holds by Theorem 3.1.2.

> [!example] Example 3.1.4: Term operations computed
> 1. $\mathbf A = (\mathbb Z, +, -, 0)$ (group signature): $\operatorname{Clo}_n(\mathbf A) = \{\, (a_1,\dots,a_n) \mapsto k_1 a_1 + \cdots + k_n a_n : k_i \in \mathbb Z \,\}$, the $\mathbb Z$-linear maps; e.g. the terms $x_1 + (x_2 + x_3)$ and $(x_1 + x_2) + x_3$ induce the same ternary operation.
> 2. $\mathbf 2 = (\{0,1\}, \vee, \wedge, \neg, 0, 1)$: $\operatorname{Clo}_n(\mathbf 2) = \mathcal O_{\{0,1\}}^{(n)}$ — every Boolean function is a term operation (functional completeness); the map $\mathsf{op}_n^{\mathbf 2}$ is far from injective (truth-table collapse).
> 3. $\mathbf A = (\mathbb N, s)$ with $s(n) = n+1$ (FTS Example 5.6.3): $\operatorname{Clo}_n(\mathbf A) = \{\, \bar a \mapsto a_i + k : 1 \le i \le n,\ k \in \mathbb N \,\}$, and $\mathsf{op}_n^{\mathbf A}$ is **injective**: distinct unary-signature terms induce distinct operations (the algebra is free, so no collapse occurs).
> 4. $\mathbf A = (\mathbb F_p, +, \cdot, 0, 1)$: the term $x_1^p$ and the term $x_1$ induce the **same** unary operation (Fermat), while as raw terms they are distinct — the standard reminder that $\mathsf{op}$ is not injective even on familiar algebras.

### 3.2. Identities and the Kernel of $\mathsf{op}$

> [!definition] Definition 3.2.1: Identity (equation valid in an algebra)
> An **equation** over $X_n$ is a pair $(s,t) \in T_\Omega(X_n)^2$, written $s \approx t$ (FTS Definition 7.1.1). The algebra $\mathbf A$ **satisfies** $s \approx t$, written $\mathbf A \models s \approx t$, iff $\operatorname{ev}_v(s) = \operatorname{ev}_v(t)$ for **every** valuation $v : X_n \to A$ (FTS Definition 8.4.1). The **$n$-ary equational theory** of $\mathbf A$ is
>
> $$
> \operatorname{Id}_n(\mathbf A) := \{\, (s,t) \in T_\Omega(X_n)^2 : \mathbf A \models s \approx t \,\},
> $$
>
> and $\operatorname{Id}(\mathcal K) := \bigcap_{\mathbf A \in \mathcal K} \operatorname{Id}(\mathbf A)$ for a class $\mathcal K$, with $\operatorname{Id}(\mathbf A)$ the corresponding theory over $X_\omega$.

> [!proposition] Proposition 3.2.2: Identities as intersections of evaluation kernels
> For every algebra $\mathbf A$ and every variable set $X$,
>
> $$
> \operatorname{Id}_X(\mathbf A) \;=\; \bigcap_{v \,:\, X \to A} \kappa_v \;=\; \bigcap_{v} \ker(\operatorname{ev}_v),
> $$
>
> the intersection over **all** valuations of their evaluation kernels. Each $\kappa_v$ is a single semantic experiment (one assignment of values to generators); the equational theory is the residue invariant under all experiments. In particular $\operatorname{Id}_X(\mathbf A) \subseteq \kappa_v$ for every $v$, and $\operatorname{Id}_X(\mathbf A)$ is a congruence on $\mathbf T_\Omega(X)$ as an intersection of congruences.

> [!remark] Remark 3.2.3: Two distinguished congruences on syntax
> The pair $(\kappa_g, \operatorname{Id}_X(\mathbf A))$ separates two collapse regimes on the same raw syntax: $\kappa_g$ records identifications forced by **one** valuation into one target ("these two terms happen to denote the same element under $g$"); $\operatorname{Id}_X(\mathbf A)$ records identifications forced by **all** valuations into the target ("these two terms denote the same operation"). The first is the element-level kernel of FTS §5.4; the second is the operation-level kernel (Theorem 3.2.4). The containment $\operatorname{Id}_X(\mathbf A) \subseteq \kappa_g$ is generally strict: in $\mathbf A = (\mathbb N, +, 0)$ with $X = \{x, y\}$ and $g(x) = g(y) = 2$, the pair $(x, y)$ lies in $\kappa_g$ (both sides evaluate to $2$) but not in $\operatorname{Id}_X(\mathbf A)$ (the valuation $x \mapsto 0, y \mapsto 1$ separates them): a *coincidence* of values under one assignment, not a *law*.

> [!theorem] Theorem 3.2.4: Kernel of the operation map; free algebras in $\operatorname{\mathbf{HSP}}(\mathbf A)$
> For every $\Omega$-algebra $\mathbf A$ and $n \ge 1$:
>
> $$
> \ker\big(\mathsf{op}_n^{\mathbf A}\big) \;=\; \operatorname{Id}_n(\mathbf A), \qquad \text{i.e.} \qquad s^{\mathbf A} = t^{\mathbf A} \iff \mathbf A \models s \approx t.
> $$
>
> Consequently, by the first isomorphism theorem (FTS Theorem 1.8.3),
>
> $$
> \mathbf T_\Omega(X_n)\big/ \operatorname{Id}_n(\mathbf A) \;\cong\; \operatorname{\mathbf{Clo}}_n(\mathbf A),
> $$
>
> where $\operatorname{\mathbf{Clo}}_n(\mathbf A)$ denotes $\operatorname{Clo}_n(\mathbf A)$ with the pointwise $\Omega$-structure of Construction 3.1.3. This quotient is the **free algebra on $n$ generators in the variety generated by $\mathbf A$** (Section 8): the $n$-ary part of the clone, as an algebra, *is* the relatively free algebra $\mathbf F_{\mathbb V(\mathbf A)}(X_n)$, with free generators the projections $\pi_1^n, \dots, \pi_n^n$. Freeness of $\mathbf T_\Omega(X_n)$ collapses along exactly the laws of $\mathbf A$ — no more, no less.

### 3.3. Polynomial Operations

> [!definition] Definition 3.3.1: Constant expansion and polynomial clone
> Let $\mathbf A$ be an $\Omega$-algebra. The **constant expansion** $\mathbf A_A$ is the algebra over the signature $\Omega \sqcup \{\,\underline a : a \in A\,\}$ (a fresh nullary symbol $\underline a$ for each element) with $f^{\mathbf A_A} := f^{\mathbf A}$ and $\underline a^{\mathbf A_A} := a$. The **polynomial clone** of $\mathbf A$ is
>
> $$
> \operatorname{Pol}(\mathbf A) := \operatorname{Clo}(\mathbf A_A), \qquad \operatorname{Pol}_n(\mathbf A) := \operatorname{Clo}_n(\mathbf A_A);
> $$
>
> its members are the **polynomial operations** of $\mathbf A$. Equivalently (eliminating the expanded signature): $P \in \operatorname{Pol}_n(\mathbf A)$ iff there exist $m \ge 0$, a term $t \in T_\Omega(X_{n+m})$, and **parameters** $b_1, \dots, b_m \in A$ with
>
> $$
> P(a_1, \dots, a_n) \;=\; t^{\mathbf A}(a_1, \dots, a_n, b_1, \dots, b_m) \qquad (\bar a \in A^n).
> $$
>
> Thus polynomial operations are term operations with some argument places frozen at elements. $\operatorname{Clo}(\mathbf A) \subseteq \operatorname{Pol}(\mathbf A)$, with equality in general failing; unary members of $\operatorname{Pol}_1(\mathbf A)$ are called **polynomials** or, in the congruence-theoretic tradition, **translations** are the special unary polynomials of Definition 4.3.1.

> [!warning] Warning 3.3.2: "Polynomial" — formal object vs. induced function; and a notation clash
> 1. In ring theory, "polynomial" means a *formal* object (an element of $R[x_1,\dots,x_n]$, itself a term-algebra-style construction), while Definition 3.3.1 defines polynomial *operations* (functions). The map formal-polynomial $\mapsto$ polynomial-function is exactly an instance of $\mathsf{op}$ with parameters, and it is **not injective** in general: over $\mathbf A = \mathbb F_p$, the formal polynomials $x^p$ and $x$ induce the same function (Example 3.1.4). For infinite integral domains the map is injective. The two readings of "polynomial" stand in the same relation as term and term operation; conflating them repeats FTS Warning 2.4.3 one level up.
> 2. **Notation clash:** in the Pol–Inv literature (Section 5), $\operatorname{Pol}(Q)$ with $Q$ a set of **relations** denotes the *polymorphism clone* of $Q$. Both usages are standard. In this treatise the argument disambiguates: $\operatorname{Pol}(\mathbf A)$ — boldface algebra — is the polynomial clone of Definition 3.3.1; $\operatorname{Pol}(Q)$ — set of relations — is the polymorphism clone of Definition 5.1.4. The two are related but distinct (Remark 5.2.5).

> [!example] Example 3.3.3: Polynomial clones computed
> 1. $\mathbf A = (\mathbb Z, +, -, 0)$: $\operatorname{Pol}_n(\mathbf A) = \{\, \bar a \mapsto k_1 a_1 + \cdots + k_n a_n + c : k_i \in \mathbb Z,\ c \in \mathbb Z \,\}$ — affine maps; compare the linear maps of $\operatorname{Clo}_n$.
> 2. $\mathbf A = (R, +, \cdot, -, 0, 1)$ a commutative unital ring: $\operatorname{Pol}_n(\mathbf A)$ = the functions induced by formal polynomials in $R[x_1, \dots, x_n]$ — the origin of the name.
> 3. A bounded lattice $\mathbf L$: unary polynomials include $x \mapsto (x \vee a) \wedge b$; iterates of such maps drive the Mal'cev description of lattice congruences (Theorem 4.3.3).
> 4. Any $\mathbf A$ with $|A| \ge 2$ and empty signature: $\operatorname{Clo}(\mathbf A) = \mathcal J_A$ (projections only), $\operatorname{Pol}(\mathbf A)$ = projections and "constants substituted into projections", i.e. all operations with at most one essential argument that are either projections or constant. The gap $\operatorname{Pol} \setminus \operatorname{Clo}$ is exactly the parameter effect.

> [!remark] Remark 3.3.4: Which notions see parameters
> The dichotomy $\operatorname{Clo}$ vs. $\operatorname{Pol}$ tracks the dichotomy *identities vs. congruences*: equational/variety-theoretic notions (identities, free algebras, Birkhoff's theorem — Section 8) are governed by $\operatorname{Clo}$, since identities quantify over all values of all variables; congruence-theoretic and commutator-theoretic notions are governed by $\operatorname{Pol}$, since congruence classes are stabilized pointwise by parameters (Theorem 4.4.2, Corollary 4.4.4). Subuniverses and homomorphisms sit on the $\operatorname{Clo}$ side (parameters break them: a polynomial operation need not preserve a subuniverse that omits its parameters).
## 4. Compatibility: What Term and Polynomial Operations Preserve

The structural objects of FTS §1 — subuniverses, homomorphisms, congruences — are characterized by their interaction with $\operatorname{Clo}$ and $\operatorname{Pol}$. This section records the three compatibility theorems and the Mal'cev description of congruence generation, which is the engine behind the descent results of Section 7.

### 4.1. Subuniverses and Homomorphisms

> [!theorem] Theorem 4.1.1: Subuniverses are closed under all term operations
> Let $\mathbf A$ be an $\Omega$-algebra and $C \subseteq A$. Then $C$ is a subuniverse of $\mathbf A$ (closed under all basic operations, FTS Definition 1.5.1) **iff** $C$ is closed under every term operation: $t^{\mathbf A}(c_1, \dots, c_n) \in C$ for all $n$, all $t \in T_\Omega(X_n)$, all $\bar c \in C^n$. Moreover the generated subuniverse is the set of term values with parameters from the generating set:
>
> $$
> \langle S \rangle_{\mathbf A} \;=\; \{\, t^{\mathbf A}(s_1, \dots, s_n) : n \ge 0,\ t \in T_\Omega(X_n),\ \bar s \in S^n \,\}
> $$
>
> (for $\Omega_0 = \varnothing$ and $S = \varnothing$ read the right side as $\varnothing$). This is the operation-level restatement of FTS Theorem 5.3.1: the generated subalgebra is the image of evaluation, and term values are evaluations.

> [!theorem] Theorem 4.1.2: Homomorphisms commute with all term operations
> Let $h : \mathbf A \to \mathbf B$ be a homomorphism of $\Omega$-algebras. Then for every $n \ge 1$, every $t \in T_\Omega(X_n)$, and all $\bar a \in A^n$:
>
> $$
> h\big( t^{\mathbf A}(a_1, \dots, a_n) \big) \;=\; t^{\mathbf B}\big( h(a_1), \dots, h(a_n) \big).
> $$
>
> Conversely, a function $h : A \to B$ satisfying the displayed identity for all basic operations (the case $t = f(x_1,\dots,x_n)$) is a homomorphism; commutation with basic operations already implies commutation with the whole clone.

> [!remark] Remark 4.1.3: Reading of Theorem 4.1.2
> The identity says that each term $t$ induces a **natural family** of operations $(t^{\mathbf A})_{\mathbf A}$ indexed by all $\Omega$-algebras, with homomorphisms intertwining the family. In categorical terms the family is a natural transformation $U^n \Rightarrow U$ on the forgetful functor $U : \mathbf{Alg}(\Omega) \to \mathbf{Set}$; this is the implicit-operation viewpoint and is not needed below, but explains why term operations transport along *every* homomorphism while polynomial operations transport only along surjective ones (Proposition 4.4.5).

> [!proposition] Proposition 4.1.4: Homomorphism, subuniverse, and congruence notions are clone-invariant
> Let $\mathbf A_1, \mathbf A_2$ be algebras (possibly of different signatures) on the **same carrier** $A$ with $\operatorname{Clo}(\mathbf A_1) = \operatorname{Clo}(\mathbf A_2)$ (**term-equivalent algebras**). Then $\mathbf A_1$ and $\mathbf A_2$ have the same subuniverses and the same congruences, and for any set-map into a similar situation the homomorphism property holds for $\mathbf A_1$-structure iff for $\mathbf A_2$-structure. If merely $\operatorname{Pol}(\mathbf A_1) = \operatorname{Pol}(\mathbf A_2)$ (**polynomially equivalent algebras**), the congruences still coincide (Corollary 4.4.4), but the subuniverses and homomorphism notions may differ.

### 4.2. Congruences and the Compatibility Theorem

> [!theorem] Theorem 4.2.1: Congruences are compatible with all term operations
> Let $\theta \in \operatorname{Con}(\mathbf A)$ (FTS Definition 1.7.2: an equivalence relation compatible with all **basic** operations). Then $\theta$ is compatible with every term operation: for all $n$, $t \in T_\Omega(X_n)$, and $(a_i, b_i) \in \theta$ ($1 \le i \le n$),
>
> $$
> \big( t^{\mathbf A}(a_1, \dots, a_n),\; t^{\mathbf A}(b_1, \dots, b_n) \big) \in \theta.
> $$
>
> Equivalently: $\theta$ is a subuniverse of $\mathbf A \times \mathbf A$ (FTS Proposition 1.7.3), and Theorem 4.1.1 applies to it. Compatibility with the generating operations propagates to the generated clone.

> [!theorem] Theorem 4.2.2: Congruences are compatible with all polynomial operations
> Let $\theta \in \operatorname{Con}(\mathbf A)$ and $P \in \operatorname{Pol}_n(\mathbf A)$, say $P(\bar a) = t^{\mathbf A}(\bar a, \bar b)$ with parameters $\bar b \in A^m$. Then for $(a_i, a_i') \in \theta$:
>
> $$
> \big( P(a_1, \dots, a_n),\, P(a_1', \dots, a_n') \big) \in \theta.
> $$
>
> (Apply Theorem 4.2.1 to $t$ with the parameter pairs $(b_j, b_j) \in \theta$ supplied by reflexivity.) Consequently $\operatorname{Con}(\mathbf A) = \operatorname{Con}(\mathbf A_A)$: **passing to the constant expansion does not change the congruence lattice**. This reflexivity-driven upgrade from $\operatorname{Clo}$ to $\operatorname{Pol}$ is what makes congruence theory a polynomial-level theory (Remark 3.3.4).

> [!warning] Warning 4.2.3: Subuniverses are not polynomial-compatible
> The analogue of Theorem 4.2.2 for subuniverses is false: a subuniverse need not be closed under polynomial operations whose parameters lie outside it. Example: $2\mathbb Z$ is a subuniverse of $(\mathbb Z, +, -, 0)$ but not closed under the polynomial $x \mapsto x + 1$. The asymmetry — congruences see $\operatorname{Pol}$, subuniverses see only $\operatorname{Clo}$ — is the precise reason the descent theory of Section 7 (a congruence phenomenon) works for arbitrary parameters, while image/generation statements (Theorem 4.1.1) must track parameters explicitly.

### 4.3. Translations and Mal'cev's Description of Congruence Generation

> [!definition] Definition 4.3.1: Basic translations and translations
> Let $\mathbf A$ be an $\Omega$-algebra. A **basic translation** of $\mathbf A$ is a unary operation of the form
>
> $$
> a \;\longmapsto\; f^{\mathbf A}(b_1, \dots, b_{i-1},\, a,\, b_{i+1}, \dots, b_n)
> $$
>
> for some $f \in \Omega_n$ ($n \ge 1$), some position $1 \le i \le n$, and some parameters $b_j \in A$. A **translation** is a finite composite of basic translations (including the empty composite $\mathrm{id}_A$). Every translation is a unary polynomial operation; in general not every unary polynomial is a translation (a polynomial may use its argument several times), but translations suffice for congruence generation (Theorem 4.3.3).

> [!proposition] Proposition 4.3.2: Compatibility via translations
> An equivalence relation $\theta$ on $A$ is a congruence of $\mathbf A$ **iff** $\theta$ is invariant under every basic translation: $(a, b) \in \theta \Rightarrow (p(a), p(b)) \in \theta$ for every basic translation $p$. (One argument at a time suffices, by composing single-coordinate replacements.) This is the algebra-side counterpart of the closure of $\theta_E$ under **replacement in contexts** (FTS Theorem 7.2.1): contexts on syntax are translations of the term algebra (Theorem 6.2.3).

> [!theorem] Theorem 4.3.3: Mal'cev's congruence-generation lemma
> Let $\mathbf A$ be an $\Omega$-algebra and $R \subseteq A \times A$. Then $(a, b) \in \operatorname{Cg}_{\mathbf A}(R)$ (the congruence generated by $R$, FTS Construction 1.7.5) **iff** there exist $k \ge 0$, elements $a = z_0, z_1, \dots, z_k = b$ of $A$, pairs $(c_j, d_j) \in R \cup R^{-1}$, and translations $p_j$ of $\mathbf A$ ($1 \le j \le k$) such that
>
> $$
> \{ z_{j-1}, z_j \} \;=\; \{ p_j(c_j),\, p_j(d_j) \} \qquad (1 \le j \le k).
> $$
>
> In words: the generated congruence is the reflexive–transitive closure of the set of translated instances of the generating pairs. The three layers of FTS Construction 1.7.5 (symmetrize, translate, chain) are here made explicit, with translation images replacing the abstract closure under operations.

> [!remark] Remark 4.3.4: Congruence lattices through unary polynomials only
> Proposition 4.3.2 and Theorem 4.3.3 show that $\operatorname{Con}(\mathbf A)$ is fully determined by the **monoid of translations** of $\mathbf A$ — a unary trace of the polynomial clone. This is the deep reason congruence lattices of algebras are exactly congruence lattices of unary algebras, and the reason context-closure alone generates the syntactic congruences $\theta_E$ in FTS Theorem 7.2.1 with no need for simultaneous multi-position replacement.

### 4.4. Congruence-Preserving Operations

> [!definition] Definition 4.4.1: Compatible (congruence-preserving) operations
> Let $\mathbf A$ be an algebra and $F \in \mathcal O_A^{(n)}$ an arbitrary operation on its carrier. $F$ is **compatible with** $\theta \in \operatorname{Con}(\mathbf A)$ iff $(a_i, b_i) \in \theta$ for all $i$ implies $(F(\bar a), F(\bar b)) \in \theta$. $F$ is **congruence-preserving** (for $\mathbf A$) iff $F$ is compatible with every $\theta \in \operatorname{Con}(\mathbf A)$. The set of congruence-preserving operations is a clone containing $\operatorname{Pol}(\mathbf A)$.

> [!theorem] Theorem 4.4.2: Polynomial operations are congruence-preserving; the converse fails
> For every algebra $\mathbf A$: $\operatorname{Pol}(\mathbf A) \subseteq \{\text{congruence-preserving operations of } \mathbf A\}$ (Theorem 4.2.2). The inclusion is strict in general. **Counterexample:** $\mathbf A = (\mathbb Z_p, +)$ for a prime $p \ge 3$: $\mathbf A$ is simple ($\operatorname{Con}(\mathbf A) = \{\Delta, \nabla\}$, since congruences of a group correspond to subgroups and $\mathbb Z_p$ has none proper nontrivial), hence **every** operation on $\mathbb Z_p$ is congruence-preserving; but $\operatorname{Pol}_n(\mathbf A)$ consists only of the affine maps $\bar a \mapsto \sum_i k_i a_i + c$, a proper subset of $\mathcal O_{\mathbb Z_p}^{(n)}$. An algebra for which the inclusion is an equality is called **affine complete**; Boolean algebras are affine complete (Grätzer), while $(\mathbb Z_p, +)$ is not.

> [!remark] Remark 4.4.3: The three-clone hierarchy
> Every algebra $\mathbf A$ carries the chain of clones
>
> $$
> \mathcal J_A \;\subseteq\; \operatorname{Clo}(\mathbf A) \;\subseteq\; \operatorname{Pol}(\mathbf A) \;\subseteq\; \{\text{congruence-preserving ops}\} \;\subseteq\; \mathcal O_A,
> $$
>
> each inclusion strict for suitable $\mathbf A$. Section 7 locates the descent-along-$\kappa_g$ property at the congruence-preserving level when a single $\kappa_g$ is fixed, and shows that demanding descent along **all** evaluation kernels simultaneously lands exactly at congruence-preservation, with $\operatorname{Pol}$ as the guaranteed, syntax-definable core.

> [!corollary] Corollary 4.4.4: Polynomially equivalent algebras share congruences
> If $\operatorname{Pol}(\mathbf A_1) = \operatorname{Pol}(\mathbf A_2)$ for algebras on the same carrier, then $\operatorname{Con}(\mathbf A_1) = \operatorname{Con}(\mathbf A_2)$. (Both lattices are determined by compatibility with the common polynomial clone, via Proposition 4.3.2 applied to its translations.)

> [!proposition] Proposition 4.4.5: Transport of polynomial operations along surjections
> Let $h : \mathbf A \to \mathbf B$ be a **surjective** homomorphism and $P \in \operatorname{Pol}_n(\mathbf A)$, $P = t^{\mathbf A}(-, \bar b)$. Then $P^h := t^{\mathbf B}(-, h(\bar b)) \in \operatorname{Pol}_n(\mathbf B)$ satisfies $h(P(\bar a)) = P^h(h(\bar a))$, and every member of $\operatorname{Pol}_n(\mathbf B)$ arises this way from some member of $\operatorname{Pol}_n(\mathbf A)$ (surjectivity supplies preimages for parameters). The assignment depends on the chosen presentation $(t, \bar b)$ only up to the identification of Theorem 3.2.4. For non-surjective $h$ the transport may fail: parameters in $B$ need not be hit. This proposition, specialized to $h = \operatorname{ev}_g$, is the surjectivity half of the clone surjection of Corollary 7.2.3.
## 5. Invariant Relations and the Pol–Inv Galois Connection

The first of the two Galois connections: operations against relations on a fixed carrier. Its closed sets organize the entire local theory — clones on the operation side, relational clones on the relation side — and exhibit subuniverses-of-powers and congruences as the invariants of term and polynomial operations respectively.

### 5.1. Preservation

> [!definition] Definition 5.1.1: Finitary relations on a set
> Let $A$ be a set and $m \ge 1$. An **$m$-ary relation** on $A$ is a subset $\rho \subseteq A^m$. The set of all finitary relations on $A$ is
>
> $$
> \mathcal R_A := \bigcup_{m \ge 1} \mathcal P(A^m).
> $$
>
> Tuples $\bar r \in \rho$ are written as columns when preservation is computed; $\rho$ may be empty. Distinguished relations: the **diagonal** $\Delta_A = \{(a,a) : a \in A\}$; for an algebra $\mathbf A$, its congruences and the graphs of its operations.

> [!definition] Definition 5.1.2: Preservation of a relation by an operation
> Let $F \in \mathcal O_A^{(n)}$ and $\rho \subseteq A^m$. $F$ **preserves** $\rho$ (synonyms: $\rho$ is **invariant** under $F$; $F$ is a **polymorphism** of $\rho$), written $F \triangleright \rho$, iff for all tuples $\bar r^1, \dots, \bar r^n \in \rho$:
>
> $$
> \Big( F\big(r^1_1, \dots, r^n_1\big),\; F\big(r^1_2, \dots, r^n_2\big),\; \dots,\; F\big(r^1_m, \dots, r^n_m\big) \Big) \in \rho,
> $$
>
> i.e. applying $F$ **coordinatewise** to any $n$ members of $\rho$ yields a member of $\rho$. Equivalently: $\rho$, viewed as a subset of $A^m$, is closed under the operation $F$ acting componentwise on $(A^m)^n$; equivalently, $F^{(m)} : (A^m)^n \to A^m$ (the $m$-th direct power of $F$) maps $\rho^n$ into $\rho$.

> [!remark] Remark 5.1.3: Preservation as subuniverse membership
> $F \triangleright \rho$ says exactly that $\rho$ is a subuniverse of the $m$-th direct power of the algebra $(A, F)$. Preservation is therefore not a new primitive: the Pol–Inv theory is the theory of subuniverses of finite powers, organized as a polarity. This identification drives Theorem 5.3.1.

> [!definition] Definition 5.1.4: The operators $\operatorname{Inv}$ and $\operatorname{Pol}$
> For sets $F \subseteq \mathcal O_A$ of operations and $Q \subseteq \mathcal R_A$ of relations, define
>
> $$
> \operatorname{Inv}(F) := \{\, \rho \in \mathcal R_A : \forall F' \in F,\ F' \triangleright \rho \,\}, \qquad \operatorname{Pol}(Q) := \{\, G \in \mathcal O_A : \forall \rho \in Q,\ G \triangleright \rho \,\}.
> $$
>
> $\operatorname{Inv}(F)$ is the set of **invariant relations** (invariants) of $F$; $\operatorname{Pol}(Q)$ is the set of **polymorphisms** of $Q$. (For the clash with the polynomial clone $\operatorname{Pol}(\mathbf A)$ see Warning 3.3.2; the argument type — boldface algebra vs. set of relations — disambiguates throughout.)

### 5.2. The Galois Connection and Its Closed Sets

> [!theorem] Theorem 5.2.1: Pol–Inv is the polarity of the preservation relation
> The pair $(\operatorname{Inv}, \operatorname{Pol})$ is the antitone Galois connection (polarity) induced by the relation ${\triangleright} \subseteq \mathcal O_A \times \mathcal R_A$: for all $F \subseteq \mathcal O_A$, $Q \subseteq \mathcal R_A$,
>
> $$
> Q \subseteq \operatorname{Inv}(F) \quad \Longleftrightarrow \quad F \subseteq \operatorname{Pol}(Q),
> $$
>
> both sides asserting $F' \triangleright \rho$ for all pairs. Consequently: both composites $\operatorname{Pol} \circ \operatorname{Inv}$ and $\operatorname{Inv} \circ \operatorname{Pol}$ are closure operators; the Galois-closed sets of operations and of relations form dually isomorphic complete lattices; and $\operatorname{Pol}(Q) = \operatorname{Pol}(\operatorname{Inv}(\operatorname{Pol}(Q)))$, $\operatorname{Inv}(F) = \operatorname{Inv}(\operatorname{Pol}(\operatorname{Inv}(F)))$.

> [!proposition] Proposition 5.2.2: Elementary closure properties
> For every $Q \subseteq \mathcal R_A$, $\operatorname{Pol}(Q)$ is a **clone** on $A$ (projections preserve everything; preservation is stable under superposition). For every $F \subseteq \mathcal O_A$, $\operatorname{Inv}(F)$ contains $\Delta_A$ and $A^m$ for all $m$, and is closed under all **primitive positive constructions** in the sense of Definition 5.2.3: finite intersections, Cartesian products, permutation and identification of coordinates, and projection (existential quantification over coordinates). Hence every Galois-closed operation set is a clone, and every Galois-closed relation set is a relational clone; the converses are exactly the content of Theorem 5.3.2 (finite case) and Warning 5.3.4 (infinite case).

> [!definition] Definition 5.2.3: Primitive positive definability; relational clone
> Let $Q \subseteq \mathcal R_A$. A relation $\rho \subseteq A^m$ is **primitively positively (pp-) definable** from $Q$ iff there is a first-order formula
>
> $$
> \varphi(y_1, \dots, y_m) \;=\; \exists z_1 \cdots \exists z_k\; \bigwedge_{j} \alpha_j,
> $$
>
> in which each atom $\alpha_j$ is either an application $\varrho(w_1, \dots, w_{m_j})$ of some $\varrho \in Q$ to variables among $\{\bar y, \bar z\}$ or an equality $w = w'$ of such variables, with
>
> $$
> \rho = \{\, (a_1, \dots, a_m) \in A^m : \varphi(a_1, \dots, a_m) \text{ holds in } (A; Q) \,\}.
> $$
>
> A **relational clone** (**co-clone**) on $A$ is a subset of $\mathcal R_A$ containing $\Delta_A$ and closed under pp-definability (equivalently: closed under finite intersections of cylindrified copies, Cartesian products, coordinate permutation/identification, and projection/existential quantification). The relational clone generated by $Q$ is denoted $\langle Q \rangle_{\mathrm{rel}}$.

### 5.3. Closed Sets: Subpowers, the Finite-Carrier Theorem, Examples

> [!theorem] Theorem 5.3.1: The invariants of an algebra are its subpower subuniverses
> For every $\Omega$-algebra $\mathbf A$:
>
> $$
> \operatorname{Inv}\big(\operatorname{Clo}(\mathbf A)\big) \;=\; \operatorname{Inv}\big(\{ f^{\mathbf A} : f \in \Omega \}\big) \;=\; \bigcup_{m \ge 1} \operatorname{Sub}\big(\mathbf A^m\big),
> $$
>
> the subuniverses of the finite direct powers of $\mathbf A$ (with the conventions of Definition 2.1.1 on nullaries). In particular, for the polynomial clone:
>
> $$
> \operatorname{Inv}\big(\operatorname{Pol}(\mathbf A)\big) \;=\; \{\, \rho \in \operatorname{Inv}(\operatorname{Clo}(\mathbf A)) : \rho = \varnothing \text{ or } \rho \supseteq \Delta^{(m)}_A \,\},
> $$
>
> where $\Delta^{(m)}_A := \{(a, \dots, a) : a \in A\} \subseteq A^m$: invariance under the constant unary polynomials forces every nonempty invariant relation to contain all constant tuples. Specializing to binary equivalence relations:
>
> $$
> \operatorname{Con}(\mathbf A) \;=\; \{\, \theta \in \operatorname{Inv}(\operatorname{Clo}(\mathbf A)) : \theta \text{ an equivalence relation} \,\} \;=\; \{\, \theta \in \operatorname{Inv}(\operatorname{Pol}(\mathbf A)) : \theta \text{ an equivalence relation} \,\},
> $$
>
> recovering Theorem 4.2.2: congruences are precisely the equivalence-relation-shaped invariants, and they do not distinguish $\operatorname{Clo}$ from $\operatorname{Pol}$.

> [!theorem] Theorem 5.3.2: Geiger / Bodnarčuk–Kalužnin–Kotov–Romov (finite carrier)
> Let $A$ be **finite**. Then the Galois-closed sets of the Pol–Inv connection are exactly the clones on the operation side and exactly the relational clones on the relation side:
>
> $$
> \operatorname{Pol}\big(\operatorname{Inv}(F)\big) = \langle F \rangle_{\mathrm{clone}}, \qquad \operatorname{Inv}\big(\operatorname{Pol}(Q)\big) = \langle Q \rangle_{\mathrm{rel}},
> $$
>
> for all $F \subseteq \mathcal O_A$, $Q \subseteq \mathcal R_A$. Hence the lattice of clones on a finite set is dually isomorphic to the lattice of relational clones, and every clone on a finite set is an intersection of polymorphism clones of single relations.

> [!corollary] Corollary 5.3.3: Mutual determination on a finite carrier
> Let $A$ be finite and $\mathbf A_1, \mathbf A_2$ algebras on $A$. Then $\operatorname{Clo}(\mathbf A_1) = \operatorname{Clo}(\mathbf A_2)$ iff $\mathbf A_1$ and $\mathbf A_2$ have the same subuniverses of all finite powers (Theorems 5.3.1–5.3.2): term-equivalence is a relationally detectable property. In particular a clone on a finite set is determined by, and determines, its invariant relations — the local syntax-free analogue of the determination of a variety by its equational theory (Theorem 8.3.2).

> [!warning] Warning 5.3.4: The finite hypothesis is essential
> For infinite $A$, $\operatorname{Pol}(\operatorname{Inv}(F))$ is in general strictly larger than $\langle F\rangle_{\mathrm{clone}}$: it equals the **local closure** of the generated clone (all operations interpolated on every finite subset by members of the clone). The corrected statement: Galois-closed operation sets are exactly the locally closed clones, and Galois-closed relation sets are the relational clones closed under arbitrary intersections and directed unions of definability — the infinitary pp-calculus. Transporting finite-carrier intuition ("clone = polymorphisms of its invariants") to infinite carriers without local closure is a standard error.

> [!example] Example 5.3.5: Clones as polymorphism clones
> 1. **Monotone operations**: for a poset $(A, \le)$, the clone of monotone operations is $\operatorname{Pol}(\{\le\})$, with $\le$ viewed as a binary relation.
> 2. **Idempotent operations**: $\operatorname{Pol}(\{\,\{a\} : a \in A\,\})$ — preserving all singletons.
> 3. **Affine operations on $\mathbb Z_p$**: $\operatorname{Pol}(\{\rho_{\mathrm{aff}}\})$ where $\rho_{\mathrm{aff}} = \{(a,b,c,d) : a - b + c = d\} \subseteq \mathbb Z_p^4$; this exhibits the polynomial clone of $(\mathbb Z_p, +)$ from Theorem 4.4.2 as a polymorphism clone.
> 4. **Post's lattice** is the full description of all $\operatorname{Pol}(Q)$ on $|A| = 2$; each of the countably many clones is $\operatorname{Pol}$ of finitely many relations.
> 5. In constraint-satisfaction theory, $\operatorname{Pol}(Q)$ for a finite constraint language $Q$ controls the complexity of $\mathrm{CSP}(Q)$; the pp-definability closure $\langle Q\rangle_{\mathrm{rel}}$ is the class of constraints simulable by $Q$. This application is recorded for orientation only.

> [!remark] Remark 5.3.6: The two Galois connections, first comparison
> Pol–Inv is a polarity **on a fixed carrier**: it classifies what a given underlying set can support, with syntax absent. The Id–Mod connection of Section 8 is a polarity **between syntax and the class of all algebras**: carriers vary, terms are the operation-side currency. The bridge between them is the clone-of-term-operations construction $\mathsf{op}$ (Construction 3.1.3), which converts syntactic objects into carrier-level operations, and Theorem 3.2.4, which computes the loss exactly: $\operatorname{Id}(\mathbf A)$. Section 10 tabulates the parallel.
## 6. The Syntax-Side Clone: Term, Polynomial, and Context Operations on Raw Syntax

The general theory of Sections 3–4 is now instantiated on the term algebra itself: $\mathbf A := \mathbf T_\Omega(X)$. The result is a complete description of the syntactic operation calculus — substitution maps, templates, and contexts — and the recognition that the context-closure rules of FTS §7.2 are exactly the translation calculus of Section 4.3 applied to syntax.

Throughout this section and the next, $X$ is an arbitrary variable set, $\mathbf T := \mathbf T_\Omega(X)$ with carrier $T := T_\Omega(X)$, and the standard variables $x_1, x_2, \dots$ of Notation 1.1.4 are assumed **disjoint from $X$** (rename if necessary; the choice is immaterial by FTS §3 representation-independence).

### 6.1. Term Operations on the Term Algebra Are Substitutions

> [!proposition] Proposition 6.1.1: Term operations of $\mathbf T$ = substitution instances
> Let $t \in T_\Omega(X_n)$. The term operation $t^{\mathbf T} \in \mathcal O_T^{(n)}$ is the substitution map
>
> $$
> t^{\mathbf T}(s_1, \dots, s_n) \;=\; t[x_1 \mapsto s_1, \dots, x_n \mapsto s_n] \qquad (s_1, \dots, s_n \in T),
> $$
>
> i.e. $\overline\sigma(t)$ for the substitution $\sigma : X_n \to T_\Omega(X)$, $\sigma(x_i) := s_i$ (FTS Definition 8.2.1). This is Definition 3.1.1 read with target the term algebra: evaluation into syntax **is** substitution (FTS Proposition 8.2.3). Superposition of such operations is the substitution composite $\bullet$, and the clone laws for $\operatorname{Clo}(\mathbf T)$ are the associativity and unit laws of substitution (FTS Proposition 8.2.3; monad laws, FTS Theorem 8.5.2).

> [!theorem] Theorem 6.1.2: Rigidity of syntax: the term algebra satisfies no laws
> Suppose $|X| \ge n$ (in particular: $X$ infinite). Then the operation map $\mathsf{op}_n^{\mathbf T} : T_\Omega(X_n) \to \operatorname{Clo}_n(\mathbf T)$ is **injective**:
>
> $$
> s^{\mathbf T} = t^{\mathbf T} \quad \Longleftrightarrow \quad s = t \qquad (s, t \in T_\Omega(X_n)),
> $$
>
> equivalently $\operatorname{Id}_n(\mathbf T_\Omega(X)) = \Delta$: the term algebra satisfies **no nontrivial identities in $\le n$ variables**. (Witness: evaluate both operations at $n$ distinct generators; injectivity is then unique readability, FTS Proposition 2.4.2.) Hence
>
> $$
> \operatorname{Clo}_n\big(\mathbf T_\Omega(X)\big) \;\cong\; T_\Omega(X_n) \qquad (|X| \ge n):
> $$
>
> **syntax is its own clone of term operations** — the free algebra and its $n$-ary derived-operation algebra are canonically identified. For $|X| < n$ the statement can fail (e.g. $X = \varnothing$ with a single constant symbol: $\mathbf T_\Omega(\varnothing)$ is trivial and satisfies $x_1 \approx x_2$ vacuously of values); the hypothesis supplies enough distinct generic inputs.

> [!remark] Remark 6.1.3: The free clone
> $\operatorname{Clo}(\mathbf T_\Omega(X_\omega))$, with $n$-ary parts $T_\Omega(X_n)$ and composition by substitution, is the **clone of $\Omega$-terms**: the free object on the signature in the category of abstract clones (Remark 2.2.1), equivalently the Lawvere theory of the variety of all $\Omega$-algebras. For every algebra $\mathbf A$, the family $(\mathsf{op}_n^{\mathbf A})_n$ is the unique clone homomorphism from the term clone onto $\operatorname{Clo}(\mathbf A)$ (Definition 9.2.1) — the operation-level restatement of the UMP of $\mathbf T_\Omega$: free on elements (FTS Theorem 2.5.1) and free on operations (here) are two faces of one freeness.

### 6.2. Syntactic Polynomial Operations: Templates and Contexts

> [!definition] Definition 6.2.1: Template and its polynomial operation on syntax
> A **template in $n$ holes over $X$** is a term
>
> $$
> u \;\in\; T_\Omega\big( X_n \sqcup X \big),
> $$
>
> the standard variables $x_1, \dots, x_n$ serving as **holes** and the elements of $X$ as frozen **parameters** (alongside any constants of $\Omega$). The **syntactic polynomial operation** of $u$ is
>
> $$
> P_u : T^n \to T, \qquad P_u(s_1, \dots, s_n) := u[x_1 \mapsto s_1, \dots, x_n \mapsto s_n,\ y \mapsto y \ (y \in X)],
> $$
>
> substitution into the holes, identity on parameters. (Well-definedness: $P_u(\bar s) \in T_\Omega(X)$ because all variables of the substituted result lie in $X$.)

> [!theorem] Theorem 6.2.2: $\operatorname{Pol}(\mathbf T)$ = template operations
> For every $n \ge 1$:
>
> $$
> \operatorname{Pol}_n\big(\mathbf T_\Omega(X)\big) \;=\; \{\, P_u : u \in T_\Omega(X_n \sqcup X) \,\},
> $$
>
> and, when $|X| \ge $ the number of standard variables in play (in particular for infinite $X$), the assignment $u \mapsto P_u$ is a **bijection**: distinct templates give distinct operations ($\operatorname{Id}(\mathbf T_{\Omega}(X)_{T}) = \Delta$ for the constant expansion, by the same rigidity as Theorem 6.1.2). Under the general parameter description of Definition 3.3.1, the template $u$ is $t[x_{n+j} \mapsto p_j]$ for a term $t \in T_\Omega(X_{n+m})$ and parameters $p_j \in T$; absorbing parameters into the template is lossless precisely because the parameters are themselves syntax.

> [!proposition] Proposition 6.2.3: Contexts are the one-occurrence unary templates; translations are context chains
> Let $n = 1$.
>
> 1. A **context** $C[\cdot]$ in the sense of FTS Definition 4.4.2 (one-hole tree, hole occurring exactly once) is exactly a template $u \in T_\Omega(\{x_1\} \sqcup X)$ in which $x_1$ occurs **exactly once**; context application $s \mapsto C[s]$ is its $P_u$.
> 2. The **basic translations** of $\mathbf T$ (Definition 4.3.1) are the depth-one contexts $s \mapsto f(p_1, \dots, p_{i-1}, s, p_{i+1}, \dots, p_k)$ with $f \in \Omega_k$ and parameters $p_j \in T$.
> 3. The **translations** of $\mathbf T$ (composites of basic translations) are exactly the context applications $s \mapsto C[s]$, $C$ ranging over all contexts: grafting a one-hole context is a composite of depth-one graftings along the hole address.
> 4. General unary templates ($x_1$ occurring $k \neq 1$ times, including $k = 0$) are unary polynomials that are **not** context applications: $k = 0$ gives constants, $k \ge 2$ gives duplicating polynomials such as $s \mapsto s \cdot s$.

> [!theorem] Theorem 6.2.4: The congruence calculus of syntax is the context calculus
> Let $E \subseteq T \times T$. Mal'cev's lemma (Theorem 4.3.3) applied to $\mathbf A = \mathbf T$ with generating set $E$, together with Proposition 6.2.3, yields: $(s, t) \in \theta_E = \operatorname{Cg}_{\mathbf T}(E)$ iff there is a finite chain
>
> $$
> s = w_0,\ w_1,\ \dots,\ w_k = t, \qquad \{w_{j-1}, w_j\} = \{ C_j[\ell_j],\, C_j[r_j] \} \quad \text{with } (\ell_j, r_j) \in E \cup E^{-1},\ C_j \text{ a context}.
> $$
>
> This is precisely the **replacement-of-equals-in-any-context** description of FTS Theorem 7.2.1, now derived as the syntax instance of the general translation lemma rather than postulated. Adding closure under all substitution endomorphisms (FTS rule (subst)) passes from $\theta_E$ to the fully invariant congruence $\theta_E^{\mathrm{fi}}$ (Section 8.2).

> [!example] Example 6.2.5: Templates in the monoid signature
> $\Omega = \{\cdot, e\}$, $X \supseteq \{y\}$, holes $x_1, x_2$:
>
> 1. $u = (x_1 \cdot y) \cdot x_1$: $P_u(s) = (s \cdot y) \cdot s$ — unary, duplicating, not a context.
> 2. $u = x_1 \cdot (y \cdot x_2)$: binary template; $P_u(s, t) = s \cdot (y \cdot t)$.
> 3. $u = (x_1 \cdot e)$: a context; $P_u$ is the basic translation $s \mapsto s \cdot e$. Note $P_u(s) \neq s$ in **raw syntax** for every $s$ — the unit law is not a law of $\mathbf T$ (Theorem 6.1.2); it becomes one only after collapse (Section 7).
> 4. $u = y$: the constant unary polynomial at the parameter $y$; holes need not occur.

> [!warning] Warning 6.2.6: Most operations on syntax are not polynomial
> $\mathcal O_T$ contains natural operations far outside $\operatorname{Pol}(\mathbf T)$, definable by structural recursion (FTS Theorem 6.2.1) but not by templates. Standard specimens, fixed here for reuse in Section 7:
>
> 1. **head-case operation**: $H(s) := \begin{cases} s & \text{if } s = f(\dots) \text{ for some } f \in \Omega_{\ge 1} \\ e^{\mathbf T} & \text{if } s \text{ is atomic} \end{cases}$ (defined for signatures with a chosen constant $e$);
> 2. **height-parity operation**: $G(s) := s$ if $\operatorname{ht}(s)$ is even, $G(s) := e^{\mathbf T}$ otherwise;
> 3. **leftmost-variable extraction**, **symbol count threshold**, and every other case-analysis on constructors.
>
> Membership in $\operatorname{Pol}(\mathbf T)$ forces *uniform* behavior — one fixed template applied to all inputs; case analysis on the input's shape is exactly what templates cannot do. These operations are legitimate on **raw** syntax (where unique readability licenses the case split, FTS Theorem 4.3.1) and are the canonical witnesses of descent failure in Theorem 7.3.2.
## 7. Descent Along Evaluation Kernels: Navigating Between Syntax and Concrete Instances

This is the worked spine of the treatise. Fix a target $(\mathbf B, g)$ with $g : X \to B$, the evaluation $\operatorname{ev}_g : \mathbf T \to \mathbf B$, the kernel $\kappa_g = \ker(\operatorname{ev}_g)$, and the canonical isomorphism $\mathbf T/\kappa_g \cong \langle g[X]\rangle_{\mathbf B}$ of Notation 1.1.3. Evaluation collapses **elements** of syntax along $\kappa_g$; the question is which **operations** on syntax survive the collapse.

### 7.1. The Descent Problem for Operations

> [!definition] Definition 7.1.1: Descent of an operation along a congruence
> Let $\theta \in \operatorname{Con}(\mathbf T)$ and $F \in \mathcal O_T^{(n)}$ an arbitrary operation on raw terms. $F$ **descends along $\theta$** iff $F$ is compatible with $\theta$ (Definition 4.4.1):
>
> $$
> (s_1, t_1), \dots, (s_n, t_n) \in \theta \quad \Longrightarrow \quad \big( F(s_1, \dots, s_n),\, F(t_1, \dots, t_n) \big) \in \theta.
> $$
>
> In that case the **descended operation**
>
> $$
> \widetilde F : (T/\theta)^n \to T/\theta, \qquad \widetilde F\big([s_1]_\theta, \dots, [s_n]_\theta\big) := \big[ F(s_1, \dots, s_n) \big]_\theta
> $$
>
> is well defined (independence of representatives is exactly the displayed condition) and is the unique operation on $T/\theta$ with $\operatorname{nat}_\theta \circ F = \widetilde F \circ (\operatorname{nat}_\theta)^n$. If $F$ is not compatible with $\theta$, **no** operation on the quotient commutes with $\operatorname{nat}_\theta$ in this way.

> [!remark] Remark 7.1.2: Relation to FTS descent of functions
> FTS Theorem 6.4.2 treats maps $\Psi : T \to V$ into a fixed set and requires $\theta \subseteq \ker\Psi$ ($\Psi$ constant on classes). Definition 7.1.1 is the operation-shaped variant: the target is also quotiented, so the requirement weakens from *constancy* on classes to *compatibility* with classes. The two coincide for $n$-ary $F$ followed by $\operatorname{nat}_\theta$: $F$ descends along $\theta$ iff $\operatorname{nat}_\theta \circ F : T^n \to T/\theta$ satisfies the FTS condition $\theta^{(n)} \subseteq \ker(\operatorname{nat}_\theta \circ F)$, where $\theta^{(n)}$ is the componentwise congruence on $T^n$.

> [!theorem] Theorem 7.1.3: Exact descent criterion along $\kappa_g$
> Let $F \in \mathcal O_T^{(n)}$ and let $(\mathbf B, g)$ be a target. The following are equivalent:
>
> 1. $F$ descends along $\kappa_g$: every tuple of $\kappa_g$-equivalent raw-term inputs is sent to $\kappa_g$-equivalent outputs;
> 2. $\operatorname{ev}_g \circ F : T^n \to B$ factors through $(\operatorname{ev}_g)^n : T^n \to B^n$ on the image: there exists an operation $\overline F : \langle g[X]\rangle_{\mathbf B}^{\,n} \to \langle g[X]\rangle_{\mathbf B}$ with
>
> $$
> \operatorname{ev}_g\big( F(s_1, \dots, s_n) \big) \;=\; \overline F\big( \operatorname{ev}_g(s_1), \dots, \operatorname{ev}_g(s_n) \big) \qquad (\bar s \in T^n);
> $$
>
> 3. the value of $\operatorname{ev}_g(F(\bar s))$ depends only on the values $\operatorname{ev}_g(s_1), \dots, \operatorname{ev}_g(s_n)$, not on the chosen syntactic representatives.
>
> When these hold, $\overline F$ is unique, and under the canonical isomorphism $\mathbf T/\kappa_g \cong \langle g[X]\rangle_{\mathbf B}$ it is the descended operation $\widetilde F$ of Definition 7.1.1. **This is the precise sense in which "an operation on raw syntax collapses correctly under evaluation": descent holds exactly when $\kappa_g$-equivalent inputs are mapped to $\kappa_g$-equivalent outputs.**

### 7.2. Automatic Descent of the Polynomial Clone

> [!theorem] Theorem 7.2.1: Every syntactic polynomial operation descends along every congruence
> Let $u \in T_\Omega(X_n \sqcup X)$ be a template and $P_u \in \operatorname{Pol}_n(\mathbf T)$ its syntactic polynomial operation (Theorem 6.2.2). Then for **every** $\theta \in \operatorname{Con}(\mathbf T)$ — in particular for every evaluation kernel $\kappa_g$ — $P_u$ descends along $\theta$ (Theorem 4.2.2: congruences are compatible with all polynomial operations). The descended operation is itself polynomial:
>
> $$
> \widetilde{P_u} \;=\; \text{the polynomial operation of } \mathbf T/\theta \text{ with template } \operatorname{nat}_\theta\text{-image parameters},
> $$
>
> i.e. $\widetilde{P_u} = t^{\mathbf T/\theta}\big( -, [\bar p]_\theta \big)$ when $P_u = t^{\mathbf T}(-, \bar p)$ per Definition 3.3.1. In particular all context applications $s \mapsto C[s]$, all substitutions, and all term operations descend. **No hypothesis on $\theta$ or on the template is required**: descent of the polynomial clone is unconditional.

> [!theorem] Theorem 7.2.2: The navigation theorem (build-then-evaluate = evaluate-then-build)
> Let $(\mathbf B, g)$ be a target, $t \in T_\Omega(X_{n+m})$, parameters $\bar p \in T^m$, and $P := t^{\mathbf T}(-, \bar p) \in \operatorname{Pol}_n(\mathbf T)$. Then for all $\bar s \in T^n$:
>
> $$
> \operatorname{ev}_g\Big( t^{\mathbf T}\big( s_1, \dots, s_n,\ p_1, \dots, p_m \big) \Big) \;=\; t^{\mathbf B}\Big( \operatorname{ev}_g(s_1), \dots, \operatorname{ev}_g(s_n),\ \operatorname{ev}_g(p_1), \dots, \operatorname{ev}_g(p_m) \Big),
> $$
>
> i.e. the square
>
> $$
> \begin{array}{ccc}
> T^{\,n} & \xrightarrow{\ P\ } & T \\[2pt]
> {\scriptstyle (\operatorname{ev}_g)^n} \big\downarrow & & \big\downarrow {\scriptstyle \operatorname{ev}_g} \\[2pt]
> B^{\,n} & \xrightarrow{\ P^{g}\ } & B
> \end{array}
> \qquad
> P^{g} := t^{\mathbf B}\big( -,\ \operatorname{ev}_g(\bar p) \big) \in \operatorname{Pol}_n(\mathbf B)
> $$
>
> commutes. The identity is the conjunction of Theorem 4.1.2 (homomorphisms commute with term operations, applied to $h = \operatorname{ev}_g$) with the substitution lemma (FTS Theorem 8.3.1: evaluating a substitution instance equals evaluating under the pulled-back valuation — the case where $P$ is a substitution). Consequently the following three computation routes agree for every template and all raw inputs:
>
> 1. **syntax-first**: assemble $P(\bar s)$ in raw syntax, evaluate once at the end;
> 2. **semantics-first**: evaluate the inputs and parameters, then apply the concrete polynomial operation $P^{g}$ of $\mathbf B$;
> 3. **quotient-resident**: work in $\mathbf T/\kappa_g$ with the descended operation $\widetilde P$ of Theorem 7.2.1, transporting along $\mathbf T/\kappa_g \cong \langle g[X]\rangle_{\mathbf B}$.

> [!corollary] Corollary 7.2.3: The clone surjection induced by evaluation
> Let $\mathbf C := \langle g[X]\rangle_{\mathbf B}$ (so $\operatorname{ev}_g : \mathbf T \twoheadrightarrow \mathbf C$). The assignment $P \mapsto P^{g}$ of Theorem 7.2.2 is a well-defined surjection
>
> $$
> \operatorname{Pol}_n\big( \mathbf T_\Omega(X) \big) \;\twoheadrightarrow\; \operatorname{Pol}_n(\mathbf C) \qquad (n \ge 1),
> $$
>
> compatible with superposition and projections (a clone homomorphism in the sense of Definition 9.2.1, restricted to polynomial clones): surjectivity holds because every parameter of $\mathbf C$ is an evaluation $\operatorname{ev}_g(p)$ of some raw term (Proposition 4.4.5 with $h = \operatorname{ev}_g$). **The entire polynomial calculus of the concrete generated algebra is the descended image of the syntactic template calculus.**

> [!proposition] Proposition 7.2.4: Collapse of operations, measured
> Two templates $u, u' \in T_\Omega(X_n \sqcup X)$ descend to the **same** operation on $\mathbf C = \langle g[X]\rangle_{\mathbf B}$ iff
>
> $$
> \big( u[\,\bar x \mapsto \bar s\,],\; u'[\,\bar x \mapsto \bar s\,] \big) \in \kappa_g \qquad \text{for all } \bar s \in T^n,
> $$
>
> equivalently iff the expansion $(\mathbf C, \operatorname{ev}_g(p))_{p}$ of $\mathbf C$ by the evaluated parameters satisfies the identity obtained from $u \approx u'$ by reading holes as variables and parameters as constants. Thus: **elements** of syntax collapse along $\kappa_g$; **operations** of syntax collapse along the identities-with-parameters of the target. The two collapses are related but distinct strata (Remark 3.2.3), and the operation-level collapse kernel contains the image of $\operatorname{Id}$-level collapse under parameter freezing.

> [!example] Example 7.2.5: Collapse computed in $(\mathbb N, +, 0)$
> $\Omega = \{\cdot, e\}$ (monoid signature), $X = \{x\}$, $\mathbf B = (\mathbb N, +, 0)$, $g(x) := 1$; $\operatorname{ev}_g$ is surjective ($\mathbb N = \langle 1 \rangle$), so $\mathbf C = \mathbf B$ and $\mathbf T/\kappa_g \cong \mathbf B$ (FTS Example 5.4.3).
>
> 1. **Element collapse**: $x \cdot e$, $x$, $e \cdot x$ are three raw terms in one $\kappa_g$-class (value $1$).
> 2. **Operation collapse**: the unary templates $u_1 = x_1 \cdot (x \cdot e)$ and $u_2 = x_1 \cdot x$ are distinct raw templates with $\kappa_g$-equivalent parameters; both descend to $s \mapsto s + 1$ on $\mathbb N$. The binary templates $(x_1 \cdot x_2) \cdot x_1$ and $x_1 \cdot (x_1 \cdot x_2)$ descend to the same operation $(a, b) \mapsto 2a + b$ — associativity and commutativity of the target collapse syntactically distinct templates.
> 3. **Navigation**: to compute $\operatorname{ev}_g\big( ((x \cdot e) \cdot x) \cdot x \big)$ one may build the raw term and evaluate ($1 + 1 + 1 = 3$), or recognize the term as $P_u(x)$ for the template $u = ((x_1 \cdot e) \cdot x_1) \cdot x_1$, whose descended operation on $\mathbb N$ is $a \mapsto 3a$, and apply it to $\operatorname{ev}_g(x) = 1$. Routes agree by Theorem 7.2.2.

### 7.3. Exactness: Which Operations Survive Which Collapses

> [!theorem] Theorem 7.3.1: The exact boundary for a fixed target
> Fix $(\mathbf B, g)$. The set of operations on $T$ that descend along $\kappa_g$ is a clone on $T$ containing $\operatorname{Pol}(\mathbf T)$:
>
> $$
> \operatorname{Pol}\big(\mathbf T_\Omega(X)\big) \;\subseteq\; \mathcal D_{\kappa_g} := \{\, F \in \mathcal O_T : F \text{ compatible with } \kappa_g \,\} \;\subseteq\; \mathcal O_T,
> $$
>
> and membership in $\mathcal D_{\kappa_g}$ is **exactly** the condition of Theorem 7.1.3: $F$ sends $\kappa_g$-equivalent input tuples to $\kappa_g$-equivalent outputs. Both inclusions are strict in general. The right inclusion $\mathcal D_{\kappa_g} \subsetneq \mathcal O_T$ holds **whenever** $\Delta \subsetneq \kappa_g \subsetneq \nabla$: choosing $(a, b) \in \kappa_g$ with $a \neq b$ and $(c, d) \notin \kappa_g$, the unary operation with $F(a) = c$ and $F(s) = d$ for $s \neq a$ is incompatible (Theorem 7.3.2 exhibits natural rather than artificial witnesses). The left inclusion is strict e.g. for $\kappa_g = \nabla$ (trivial target), where $\mathcal D_\nabla = \mathcal O_T$. In the opposite extreme $\kappa_g = \Delta$ (free target: $\operatorname{ev}_g$ injective, FTS Theorem 5.6.1) every operation descends, $\mathcal D_\Delta = \mathcal O_T$: **on genuinely free syntax, arbitrary structural case analysis is harmless**, which is exactly why FTS §6 recursion is unconditional there.

> [!theorem] Theorem 7.3.2: Failure of descent for case-analysis operations
> Let $\Omega = \{\cdot, e\}$, $X = \{x\}$, $\mathbf B = (\mathbb N, +, 0)$, $g(x) = 1$ as in Example 7.2.5, and let $H \in \mathcal O_T^{(1)}$ be the head-case operation of Warning 6.2.6: $H(s) := e$ if $s$ is atomic, $H(s) := s$ otherwise. Then $H$ does **not** descend along $\kappa_g$:
>
> $$
> (x,\ x \cdot e) \in \kappa_g, \qquad \big( H(x), H(x \cdot e) \big) = (e,\ x \cdot e) \notin \kappa_g \quad (\text{values } 0 \neq 1).
> $$
>
> The same argument defeats the height-parity operation $G$ and every operation whose output value depends on a constructor-level property not invariant under the target's laws. This is the operation-level form of FTS Warning 6.3.2 (ill-defined recursion on collapsed structures): *pattern matching is a right of the free; quotients revoke it except where compatibility is proved.*

> [!theorem] Theorem 7.3.3: Descent along all targets simultaneously
> For $F \in \mathcal O_T^{(n)}$ the following are equivalent:
>
> 1. $F$ descends along $\kappa_g$ for **every** target $(\mathbf B, g)$ (every algebra, every generator assignment);
> 2. $F$ is compatible with **every** congruence of $\mathbf T_\Omega(X)$, i.e. $F$ is congruence-preserving (Definition 4.4.1).
>
> (1 ⇒ 2 because **every** congruence is an evaluation kernel: $\theta = \kappa_{g_\theta}$ for the target $\mathbf B := \mathbf T/\theta$ and $g_\theta := \operatorname{nat}_\theta \circ \eta_X$, since every homomorphism out of $\mathbf T$ is the evaluation of its own generator restriction — the UMP read backwards, FTS Theorem 2.5.1. 2 ⇒ 1 is immediate.) Combining with Theorem 4.4.2:
>
> $$
> \operatorname{Pol}\big(\mathbf T_\Omega(X)\big) \;\subseteq\; \{\, F : F \text{ descends along every } \kappa_g \,\} \;=\; \{\, F : F \text{ congruence-preserving on } \mathbf T \,\}.
> $$
>
> The polynomial clone is the **syntax-definable, certificate-carrying core** of universally descending operations: a template *is* a proof of universal descent. Whether the inclusion is an equality for term algebras (affine completeness of $\mathbf T_\Omega(X)$) depends on $(\Omega, X)$ and is not asserted here; what the treatise uses is only the displayed inclusion and its exactness target-by-target (Theorem 7.1.3).

> [!remark] Remark 7.3.4: Navigating from different starting points
> The descent calculus organizes the three entry points to a concrete computation:
>
> 1. **From raw syntax.** Build with templates/contexts in $\mathbf T$; evaluate once at the end. Always correct for polynomial operations (Theorem 7.2.1); correct for a non-polynomial $F$ only against targets with $\kappa_g$-compatibility certified (Theorem 7.1.3).
> 2. **From a presentation.** Work in $\langle X \mid E\rangle = \mathbf T/\theta_E$ (FTS §7) with $\theta_E \subseteq \kappa_g$ (soundness of the presentation for the target). Operations descend $\mathbf T \to \mathbf T/\theta_E$ by $\theta_E$-compatibility, then further along $\kappa_g/\theta_E$ by the third isomorphism theorem (FTS Theorem 1.8.4); for **complete** presentations ($\theta_E = \kappa_g$, FTS Definition 7.3.2) the second step is an isomorphism and the presented algebra computes the target exactly.
> 3. **From the concrete algebra.** Work in $\mathbf B$ with $\operatorname{Pol}(\mathbf B)$ directly; lift to syntax when a derivation, a normal form, or a rewriting argument is needed (FTS §7.4), using Corollary 7.2.3's surjection to choose any template representative.
>
> The substitution lemma guarantees route-independence wherever all routes are defined; the descent criteria delimit where they are defined. This is the full operational content of "syntax modulo semantic identification" (FTS Theorem 5.5.1).

> [!warning] Warning 7.3.5: Quantifier order in collapse statements
> "$F$ descends along $\kappa_g$ for the given $g$" (Theorem 7.1.3), "$F$ descends along $\kappa_v$ for every valuation $v$ into a fixed $\mathbf B$", and "$F$ descends along every $\kappa_g$ into every target" (Theorem 7.3.3) are strictly increasingly demanding. The middle condition relates to $\operatorname{Id}_X(\mathbf B) = \bigcap_v \kappa_v$ (Proposition 3.2.2) but is **not** equivalent to compatibility with $\operatorname{Id}_X(\mathbf B)$ alone: compatibility with each member of a family of congruences neither follows from nor implies compatibility with the intersection in general; only the implication "compatible with each $\kappa_v$ ⇒ compatible with $\bigcap_v \kappa_v$" holds. Collapse claims must always name their quantifier prefix.
## 8. Equational Theories, Fully Invariant Congruences, and the Id–Mod Galois Connection

The second Galois connection: equations against algebras. Its operation-side closed sets are the equational theories, which are exactly the fully invariant congruences of the term algebra; its class-side closed sets are the varieties. The section also locates $\kappa_g$, $\operatorname{Id}$, and $\theta_E^{\mathrm{fi}}$ in one stratified picture.

### 8.1. Endomorphism Invariance and Full Invariance

> [!definition] Definition 8.1.1: Fully invariant congruence (general algebra)
> Let $\mathbf A$ be an $\Omega$-algebra. A congruence $\theta \in \operatorname{Con}(\mathbf A)$ is **fully invariant** iff it is invariant under every endomorphism $h : \mathbf A \to \mathbf A$:
>
> $$
> (a, b) \in \theta \quad \Longrightarrow \quad \big( h(a), h(b) \big) \in \theta \qquad (\forall h \in \operatorname{End}(\mathbf A)).
> $$
>
> For $\mathbf A = \mathbf T_\Omega(X)$, the endomorphisms are exactly the extensions $\overline\sigma$ of substitutions $\sigma : X \to T_\Omega(X)$ (every endomorphism is the evaluation of its generator restriction, FTS Theorem 2.5.1), so full invariance coincides with closure under the substitution rule, recovering FTS Definition 8.4.2. The set of fully invariant congruences of $\mathbf A$ is denoted $\operatorname{Con}^{\mathrm{fi}}(\mathbf A)$.

> [!proposition] Proposition 8.1.2: The lattice of fully invariant congruences
> $\operatorname{Con}^{\mathrm{fi}}(\mathbf A)$ is a closure system inside $\operatorname{Con}(\mathbf A)$: it contains $\nabla_{\mathbf A}$ and is closed under arbitrary intersections; hence it is a complete lattice, and the **fully invariant congruence generated by** $R \subseteq A \times A$,
>
> $$
> \operatorname{Cg}^{\mathrm{fi}}_{\mathbf A}(R) := \bigcap \{\, \theta \in \operatorname{Con}^{\mathrm{fi}}(\mathbf A) : R \subseteq \theta \,\},
> $$
>
> exists for every $R$. For finitary signatures the generation operator is finitary (a pair enters by finitely many applications of operations, translations, transitivity, and endomorphisms), so $\operatorname{Con}^{\mathrm{fi}}(\mathbf A)$ is an **algebraic lattice**. On $\mathbf T_\Omega(X)$: $\operatorname{Cg}^{\mathrm{fi}}(E) = \theta_E^{\mathrm{fi}}$, the congruence of derivable equations of FTS Theorem 7.2.2.

> [!remark] Remark 8.1.3: The invariance hierarchy on syntax
> On $\mathbf T = \mathbf T_\Omega(X)$ three nested closure regimes govern a set $E$ of equations: closure under **contexts only** (translations; gives $\theta_E$, the *ground* reading, FTS Theorem 7.2.1 and Theorem 6.2.4 above); closure under contexts **and substitutions** (endomorphisms; gives $\theta_E^{\mathrm{fi}}$, the *schematic* reading); and intermediate regimes (closure under renamings only) that occur in rewriting theory. The strictness of $\theta_E \subseteq \theta_E^{\mathrm{fi}}$ is FTS Warning 8.4.5. In clone terms: $\theta_E$ is the $\operatorname{Pol}(\mathbf T)$-compatible closure, $\theta_E^{\mathrm{fi}}$ additionally the $\operatorname{End}(\mathbf T)$-closure — compatibility with operations vs. invariance under morphisms are independent closure demands, and only their conjunction axiomatizes "laws".

### 8.2. Equational Theories as Fully Invariant Congruences

> [!theorem] Theorem 8.2.1: Identities of a class form a fully invariant congruence
> For every class $\mathcal K$ of $\Omega$-algebras and every variable set $X$, the identity set $\operatorname{Id}_X(\mathcal K) = \{(s,t) : \forall \mathbf A \in \mathcal K,\ \mathbf A \models s \approx t\}$ is a fully invariant congruence on $\mathbf T_\Omega(X)$ (FTS Theorem 8.4.3). Congruence-hood is Proposition 3.2.2 (intersection of kernels); **full invariance is the substitution lemma** (FTS Theorem 8.3.1): a law survives substitution because evaluating a substitution instance is evaluating under a pulled-back valuation, and laws quantify over all valuations.

> [!theorem] Theorem 8.2.2: Equational theories = fully invariant congruences (Birkhoff completeness)
> Fix $X = X_\omega$. For $\Theta \subseteq T_\Omega(X_\omega)^2$ the following are equivalent:
>
> 1. $\Theta = \operatorname{Id}_{X_\omega}(\mathcal K)$ for some class $\mathcal K$ of $\Omega$-algebras (**equational theory**);
> 2. $\Theta$ is deductively closed: $\Theta \vdash s \approx t$ implies $(s,t) \in \Theta$, for the calculus (refl), (sym), (trans), (cong), (subst) of FTS Theorem 7.2.2;
> 3. $\Theta \in \operatorname{Con}^{\mathrm{fi}}\big(\mathbf T_\Omega(X_\omega)\big)$.
>
> The countably infinite variable supply in item 1 is essential: over a finite $X_n$, the fully invariant congruences correspond to **$n$-variable fragments** of equational theories, and distinct theories can have identical $n$-variable fragments.

> [!warning] Warning 8.2.3: Evaluation kernels are not fully invariant
> A single evaluation kernel $\kappa_g$ is a congruence but in general **not** fully invariant: with $\mathbf B = (\mathbb N, +, 0)$, $X = \{x, y\}$, $g(x) = g(y) = 2$ (Remark 3.2.3), the pair $(x, y) \in \kappa_g$, but the substitution $\sigma : x \mapsto x,\ y \mapsto x \cdot x$ gives $(\overline\sigma(x), \overline\sigma(y)) = (x, x \cdot x) \notin \kappa_g$ (values $2 \neq 4$). Coincidences are not laws, and substitution detects the difference. The fully invariant **interior** of $\kappa_g$ — the largest fully invariant congruence contained in it, which exists since $\operatorname{Con}^{\mathrm{fi}}$ is closed under joins of all members below a bound — always contains $\operatorname{Id}_X\big(\langle g[X]\rangle_{\mathbf B}\big)$ but need not equal $\operatorname{Id}_X(\mathbf B)$; the unconditionally safe identities are $\operatorname{Id}_X(\mathbf B) = \bigcap_{v : X \to B} \kappa_v$ (Proposition 3.2.2) and $\operatorname{Id}_X(\mathbf B) \subseteq \kappa_g$ for each particular $g$.

### 8.3. The Id–Mod Galois Connection and Birkhoff's Theorem

> [!construction] Construction 8.3.1: The satisfaction polarity
> Let $\mathrm{Eq} := T_\Omega(X_\omega)^2$ (the set of equations) and let $\mathrm{Alg}(\Omega)$ be the class of all $\Omega$-algebras. The **satisfaction relation** ${\models} \subseteq \mathrm{Alg}(\Omega) \times \mathrm{Eq}$ ($\mathbf A \models s \approx t$ per Definition 3.2.1) induces the polarity
>
> $$
> \operatorname{Mod}(E) := \{\, \mathbf A : \forall (s,t) \in E,\ \mathbf A \models s \approx t \,\}, \qquad \operatorname{Id}(\mathcal K) := \{\, (s,t) : \forall \mathbf A \in \mathcal K,\ \mathbf A \models s \approx t \,\},
> $$
>
> for $E \subseteq \mathrm{Eq}$ and $\mathcal K \subseteq \mathrm{Alg}(\Omega)$. **Size caveat:** $\mathrm{Alg}(\Omega)$ is a proper class; the polarity formalism applies verbatim with classes on one side (or within a Grothendieck universe, FTS Notation 1.1.1), since only memberships $\mathbf A \in \operatorname{Mod}(E)$ and intersections over set-indexed data are used. $\operatorname{Mod}(E)$ is the **equational class** (class of models) of $E$.

> [!theorem] Theorem 8.3.2: Closed sets of the satisfaction polarity (Birkhoff)
> The pair $(\operatorname{Id}, \operatorname{Mod})$ is an antitone Galois connection, and:
>
> 1. the Galois-closed equation sets ($E = \operatorname{Id}(\operatorname{Mod}(E))$) are exactly the equational theories, i.e. the fully invariant congruences of $\mathbf T_\Omega(X_\omega)$ (Theorem 8.2.2);
> 2. the Galois-closed classes ($\mathcal K = \operatorname{Mod}(\operatorname{Id}(\mathcal K))$) are exactly the **varieties**: the classes closed under homomorphic images ($\mathbf H$), subalgebras ($\mathbf S$), and arbitrary direct products ($\mathbf P$); moreover $\operatorname{Mod}(\operatorname{Id}(\mathcal K)) = \mathbf{HSP}(\mathcal K) =: \mathbb V(\mathcal K)$ for every class $\mathcal K$ (**Birkhoff's HSP theorem**);
> 3. the two closed-set lattices are dually isomorphic complete lattices: the lattice of equational theories over $\Omega$ (algebraic, by Proposition 8.1.2) and the lattice of varieties of $\Omega$-algebras.

> [!theorem] Theorem 8.3.3: Free algebras in varieties
> Let $\mathcal V = \operatorname{Mod}(\Theta)$ be a variety with theory $\Theta = \operatorname{Id}(\mathcal V)$, and let $X$ be any set. Then
>
> $$
> \mathbf F_{\mathcal V}(X) := \mathbf T_\Omega(X) \big/ \operatorname{Id}_X(\mathcal V)
> $$
>
> lies in $\mathcal V$, and with the generator map $\overline\eta := \operatorname{nat} \circ \eta_X$ it satisfies the **relative UMP**: every map $g : X \to A$ with $\mathbf A \in \mathcal V$ extends uniquely to a homomorphism $\mathbf F_{\mathcal V}(X) \to \mathbf A$ (FTS Example 2.6.4, Theorem 8.4.4). For $X = X_n$ and $\mathcal V = \mathbb V(\mathbf A)$ this is Theorem 3.2.4: $\mathbf F_{\mathbb V(\mathbf A)}(X_n) \cong \operatorname{\mathbf{Clo}}_n(\mathbf A)$ — **the relatively free algebras are the clones in algebra form**, and the tower $(\mathbf F_{\mathcal V}(X_n))_n$ with substitution is the clone of the variety (its Lawvere theory).

> [!example] Example 8.3.4: Theories, varieties, and free objects computed
> 1. $E_{\mathrm{mon}}$ = associativity and unit laws: $\operatorname{Mod}(E_{\mathrm{mon}})$ = monoids; $\mathbf F(X)$ = the free monoid $X^*$ (words), the quotient of raw $\{\cdot, e\}$-syntax by $\theta^{\mathrm{fi}}_{E_{\mathrm{mon}}}$ (FTS Example 2.6.3).
> 2. $E_{\mathrm{ab}}$ = abelian-group laws: free objects $\mathbb Z^{(X)}$; $\operatorname{Clo}_n = \mathbb Z$-linear maps (Example 3.1.4).
> 3. $E_{\mathrm{BA}}$ = Boolean-algebra laws: $\mathbf F(X_n)$ = the $2^{2^n}$-element free Boolean algebra $\cong$ $\operatorname{Clo}_n(\mathbf 2)$ = all $n$-ary truth functions — Theorem 3.2.4 in its most familiar instance.
> 4. The **lattice of all varieties** of a given signature is dually the lattice of equational theories; e.g. the varieties of bands (idempotent semigroups) form a countably infinite, completely described lattice, while the lattice of group varieties is uncountable. Recorded to calibrate expectations, as in Remark 2.1.4.

> [!remark] Remark 8.3.5: The two polarities compared
> Pol–Inv (Section 5) and Id–Mod are structurally parallel — both are polarities with closure systems on each side and a dual isomorphism of closed-set lattices — but live at different addresses: Pol–Inv fixes one carrier and pairs *operations against relations*; Id–Mod fixes the signature and pairs *syntax against the class of all algebras*. The clone construction connects them: an equational theory $\Theta$ determines the abstract clone $(\,T_\Omega(X_n)/\Theta_n\,)_n$, and each model $\mathbf A \in \operatorname{Mod}(\Theta)$ realizes that abstract clone concretely as $\operatorname{Clo}(\mathbf A) \subseteq \mathcal O_A$, where Pol–Inv takes over. Syntax-side collapse ($\Theta$) and carrier-side closure (Galois closure of $\operatorname{Clo}(\mathbf A)$) are independent coordinates of one situation; conflating them is the operation-level form of conflating $\operatorname{Id}$ with $\kappa_g$.
## 9. Interpretations and Substitution Operations Between Algebras

The final layer of structure: maps that change the signature or the algebra while respecting derived operations. These are the morphisms *between* the clones and term calculi of different algebras, completing the navigation begun in Section 7 (which fixed one signature and one target).

### 9.1. Derived Structure and Interpretations

> [!definition] Definition 9.1.1: Interpretation of a signature in an algebra
> Let $\Omega'$ be a second signature and $\mathbf A$ an $\Omega$-algebra. An **interpretation of $\Omega'$ in $\mathbf A$** is an arity-preserving map
>
> $$
> \iota : \Omega' \longrightarrow \operatorname{Clo}(\mathbf A), \qquad \iota(f') \in \operatorname{Clo}_{\operatorname{ar}(f')}(\mathbf A),
> $$
>
> (nullary $f'$ interpreted by elements named by unary-constant members, per the convention of Definition 2.1.1). The **derived algebra** $\mathbf A^\iota$ is the $\Omega'$-algebra with carrier $A$ and $f'^{\mathbf A^\iota} := \iota(f')$. Choosing instead $\iota : \Omega' \to \operatorname{Pol}(\mathbf A)$ yields a **polynomially derived algebra**. Specifying $\iota$ by terms — $\iota(f') = t_{f'}^{\mathbf A}$ for chosen $t_{f'} \in T_\Omega(X_{\operatorname{ar}(f')})$ — is the syntactic presentation of an interpretation; by Theorem 3.2.4 the operation $\iota(f')$ determines $t_{f'}$ only up to $\operatorname{Id}(\mathbf A)$.

> [!proposition] Proposition 9.1.2: Translation of terms along an interpretation
> Fix a term-presented interpretation $f' \mapsto t_{f'}$ as above. There is a unique family of **translation maps**
>
> $$
> \tau_n : T_{\Omega'}(X_n) \longrightarrow T_\Omega(X_n) \qquad (n \ge 1),
> $$
>
> defined by structural recursion (FTS Theorem 6.2.1): $\tau_n(x_i) = x_i$ and $\tau_n\big(f'(s_1, \dots, s_k)\big) = t_{f'}[x_j \mapsto \tau_n(s_j)]$, such that for every $s \in T_{\Omega'}(X_n)$:
>
> $$
> s^{\mathbf A^\iota} \;=\; \big( \tau_n(s) \big)^{\mathbf A}.
> $$
>
> Consequently $\operatorname{Clo}(\mathbf A^\iota) \subseteq \operatorname{Clo}(\mathbf A)$, with equality iff every basic operation of $\mathbf A$ is a term operation of $\mathbf A^\iota$; and identities transfer contravariantly: $\mathbf A^\iota \models s \approx s'$ iff $\mathbf A \models \tau(s) \approx \tau(s')$.

> [!definition] Definition 9.1.3: Term equivalence, polynomial equivalence, definitional equivalence
> Algebras $\mathbf A_1$ ($\Omega_1$-algebra) and $\mathbf A_2$ ($\Omega_2$-algebra) **on the same carrier** $A$ are:
>
> 1. **term-equivalent** iff $\operatorname{Clo}(\mathbf A_1) = \operatorname{Clo}(\mathbf A_2)$;
> 2. **polynomially equivalent** iff $\operatorname{Pol}(\mathbf A_1) = \operatorname{Pol}(\mathbf A_2)$.
>
> Two varieties $\mathcal V_1, \mathcal V_2$ are **definitionally equivalent** iff there are term-presented interpretations in both directions whose derived-algebra constructions are mutually inverse on models up to equality of algebras (not mere isomorphism), in which case the model categories are isomorphic over $\mathbf{Set}$. Term equivalence of algebras is the object-level trace of definitional equivalence of the varieties they generate. By Proposition 4.1.4, term-equivalent algebras share subuniverses, congruences, and homomorphism notions; by Corollary 4.4.4, polynomially equivalent ones share congruences.

> [!example] Example 9.1.4: Classical term equivalences
> 1. **Boolean algebras ↔ Boolean rings**: on any carrier, from $(B, \vee, \wedge, \neg, 0, 1)$ define $x + y := (x \wedge \neg y) \vee (\neg x \wedge y)$, $x \cdot y := x \wedge y$; from a Boolean ring $(B, +, \cdot, 0, 1)$ define $x \vee y := x + y + xy$, $x \wedge y := xy$, $\neg x := 1 + x$. The two derived-algebra passages are mutually inverse, the clones coincide, and the varieties are definitionally equivalent.
> 2. **Abelian groups ↔ $\mathbb Z$-modules**: each scalar action $x \mapsto kx$ is a term operation of $(A, +, -, 0)$; adjoining all of them changes the signature (to an infinite one) but not the clone.
> 3. **Groups in signatures $\{\cdot, ^{-1}, e\}$ vs. $\{/ \}$** (division $x / y := x \cdot y^{-1}$): term-equivalent on every group; a one-binary-operation presentation of the same clone.
> 4. **Non-example**: $(\mathbb Z_p, +)$ and the full structure $(\mathbb Z_p, +, \cdot)$ are **not** term-equivalent ($\cdot \notin \operatorname{Clo}(\mathbb Z_p, +)$, Theorem 4.4.2) although they are simple algebras on one carrier with equal congruence lattices — congruence data does not determine the clone.

### 9.2. Clone Homomorphisms and the Four-Corner Calculus

> [!definition] Definition 9.2.1: Clone homomorphism
> Let $\mathcal C$, $\mathcal D$ be clones (concrete or abstract, Remark 2.2.1). A **clone homomorphism** $\varphi : \mathcal C \to \mathcal D$ is a family $(\varphi_n : \mathcal C^{(n)} \to \mathcal D^{(n)})_{n \ge 1}$ preserving projections and superposition:
>
> $$
> \varphi_n(\pi_i^n) = \pi_i^n, \qquad \varphi_m\big( F(G_1, \dots, G_n) \big) = \varphi_n(F)\big( \varphi_m(G_1), \dots, \varphi_m(G_n) \big),
> $$
>
> for all $n$-ary $F \in \mathcal C^{(n)}$ and $m$-ary $G_1, \dots, G_n \in \mathcal C^{(m)}$. Interpretations of varieties correspond to clone homomorphisms between their clones; the operation maps $\mathsf{op}^{\mathbf A}$ are the canonical examples.

> [!theorem] Theorem 9.2.2: The term clone is free; algebras = clone homomorphisms into $\mathcal O_B$
> Let $\mathcal T_\Omega$ denote the term clone $\big( T_\Omega(X_n) \big)_{n \ge 1}$ with substitution as superposition (Remark 6.1.3). For every set $B$ there is a bijection between:
>
> 1. $\Omega$-algebra structures $\mathbf B$ on the carrier $B$, and
> 2. clone homomorphisms $\varphi : \mathcal T_\Omega \to \mathcal O_B$,
>
> given by $\mathbf B \mapsto (\mathsf{op}_n^{\mathbf B})_n$ and, conversely, by reading off $f^{\mathbf B} := \varphi(f(x_1, \dots, x_n))$. Under this bijection, $\operatorname{Clo}(\mathbf B) = \operatorname{im}(\varphi)$ and $\operatorname{Id}(\mathbf B) = \ker(\varphi)$ (arity-wise). This is the operation-level UMP of the term algebra: **free on generators at the element level (FTS Theorem 2.5.1), free on the signature at the clone level.**

> [!proposition] Proposition 9.2.3: The four-corner navigation identities
> Let $X, Y$ be variable sets and $\mathbf A, \mathbf B$ be $\Omega$-algebras. The four corners $\mathbf T_\Omega(X)$, $\mathbf T_\Omega(Y)$, $\mathbf A$, $\mathbf B$ are connected by: substitutions $\overline\sigma : \mathbf T_\Omega(X) \to \mathbf T_\Omega(Y)$ (syntax → syntax); evaluations $\operatorname{ev}_v : \mathbf T_\Omega(Y) \to \mathbf A$ (syntax → semantics); homomorphisms $h : \mathbf A \to \mathbf B$ (semantics → semantics). All composition laws reduce to two identities, each an instance of uniqueness in the UMP:
>
> $$
> \textbf{(S)} \quad \operatorname{ev}_v \circ \overline\sigma = \operatorname{ev}_{\,\overline v \circ \sigma} \qquad \text{(substitution lemma, FTS Theorem 8.3.1)};
> $$
>
> $$
> \textbf{(H)} \quad h \circ \operatorname{ev}_g = \operatorname{ev}_{\,h \circ g} \qquad \text{(homomorphism absorption: both sides extend } h \circ g \text{)}.
> $$
>
> Together with $\overline{\tau \bullet \sigma} = \overline\tau \circ \overline\sigma$ (FTS Proposition 8.2.3) and $k \circ h$ composition of homomorphisms, every path between corners normalizes to the form $h \circ \operatorname{ev}_g \circ \overline\sigma = \operatorname{ev}_{\text{(pulled-back valuation)}}$: **every composite of substitutions, evaluations, and homomorphisms is a single evaluation.** This is the complete calculus of "substitution operations between algebras"; the Kleisli/Eilenberg–Moore formulation is FTS §8.5 and §13.4.

> [!warning] Warning 9.2.4: No homomorphic section from semantics back to syntax
> The navigation calculus is one-directional: there is in general no homomorphism $\mathbf B \to \mathbf T_\Omega(X)$ splitting $\operatorname{ev}_g$. A set-theoretic section (choice of syntactic representative for each value) exists by surjectivity onto the image and the Axiom of Choice, but it is a homomorphism **iff** $\kappa_g = \Delta$ (freeness, FTS Theorem 5.6.1). A *canonical computable* section is exactly a **normal-form function**, which exists when a convergent rewriting presentation is available (FTS §7.4) and may fail to exist at all effectively (undecidable word problems, FTS Warning 7.3.3). "Lifting an element of $\mathbf B$ to syntax" is therefore an act of *presentation*, not of structure, and any construction depending on the lift must be checked for $\kappa_g$-independence — which is once more the descent condition of Theorem 7.1.3.

> [!remark] Remark 9.2.5: Summary of the morphism landscape
> Three independent morphism layers now coexist, and must not be conflated: (i) **homomorphisms of algebras** (fixed signature, FTS Definition 1.4.1) — compare elements; (ii) **clone homomorphisms / interpretations** (signature may change) — compare derived-operation calculi; (iii) **descent maps along congruences** (Section 7) — compare an algebra with its collapses. The operation map $\mathsf{op}^{\mathbf A}$ is simultaneously: an evaluation (layer i, Construction 3.1.3), the universal clone homomorphism (layer ii, Theorem 9.2.2), and the universal descent of syntax along $\operatorname{Id}(\mathbf A)$ (layer iii, Theorem 3.2.4). The three readings of one map are the precise content of the syntax–semantics correspondence at the operation level.
## 10. Synthesis

### 10.1. The Architecture in One Diagram

The element level (FTS) and the operation level (this treatise) are connected by one commuting scheme. For a target $(\mathbf B, g)$ with $\mathbf C := \langle g[X]\rangle_{\mathbf B}$:

$$
\begin{array}{ccccc}
\text{templates } u \in T_\Omega(X_n \sqcup X) & \xrightarrow{\ u \mapsto P_u\ } & \operatorname{Pol}_n\big(\mathbf T_\Omega(X)\big) & \xrightarrow{\ \text{descent along } \kappa_g\ } & \operatorname{Pol}_n(\mathbf C) \\[4pt]
& & \text{acts on } T_\Omega(X) & & \text{acts on } C \\[4pt]
& & \Big\downarrow {\scriptstyle \operatorname{ev}_g} & & \Big\| \\[4pt]
& & C \cong T_\Omega(X)/\kappa_g & = & C
\end{array}
$$

Elements collapse along $\kappa_g$ (FTS Theorem 5.5.1); operations descend along $\kappa_g$ exactly when they map $\kappa_g$-equivalent tuples to $\kappa_g$-equivalent values (Theorem 7.1.3); the polynomial clone descends unconditionally and surjectively (Theorems 7.2.1, Corollary 7.2.3); operations outside the descending clone are syntax-only (Theorem 7.3.2).

### 10.2. The Stratification of Collapse

| Congruence on $\mathbf T_\Omega(X)$ | Quantifier content | Closure regime | Quotient object |
|---|---|---|---|
| $\Delta$ | no identifications | — | raw syntax $\mathbf T_\Omega(X)$ (absolutely free) |
| $\theta_E$ | the listed ground relations | contexts/translations (Thm. 6.2.4) | presented algebra $\langle X \mid E\rangle$ (FTS §7) |
| $\theta_E^{\mathrm{fi}}$ | $E$ as schematic laws | contexts + substitutions (§8.1) | relatively free algebra $\mathbf F_{\operatorname{Mod}(E)}(X)$ |
| $\operatorname{Id}_X(\mathbf B)$ | all valuations into $\mathbf B$ | fully invariant (Thm. 8.2.1) | free algebra in $\mathbb V(\mathbf B)$; $n$-ary case $\cong \operatorname{\mathbf{Clo}}_n(\mathbf B)$ |
| $\kappa_g$ | one valuation $g$ | congruence only (Warn. 8.2.3) | generated subalgebra $\langle g[X]\rangle_{\mathbf B}$ |
| $\nabla$ | everything identified | — | trivial algebra |

with $\Delta \subseteq \theta_E \subseteq \theta_E^{\mathrm{fi}}$ and $\operatorname{Id}_X(\mathbf B) = \bigcap_{v} \kappa_v \subseteq \kappa_g \subseteq \nabla$; the chains interleave according to the soundness/completeness of $E$ for $(\mathbf B, g)$ (FTS Definition 7.3.2).

### 10.3. The Two Galois Connections

| | Pol–Inv (Section 5) | Id–Mod (Section 8) |
|---|---|---|
| ambient sides | operations $\mathcal O_A$ / relations $\mathcal R_A$, fixed carrier $A$ | algebras $\mathrm{Alg}(\Omega)$ / equations $T_\Omega(X_\omega)^2$, fixed signature |
| pairing | preservation $F \triangleright \rho$ | satisfaction $\mathbf A \models s \approx t$ |
| closure, operation side | clones (finite $A$: Thm. 5.3.2; infinite: locally closed clones, Warn. 5.3.4) | equational theories = fully invariant congruences (Thm. 8.2.2) |
| closure, other side | relational clones (pp-definability) | varieties = $\mathbf{HSP}$-closed classes (Thm. 8.3.2) |
| invariants of one algebra | $\operatorname{Inv}(\operatorname{Clo}(\mathbf A)) = \bigcup_m \operatorname{Sub}(\mathbf A^m)$ (Thm. 5.3.1) | $\operatorname{Id}(\mathbf A) = \ker(\mathsf{op}^{\mathbf A}) = \bigcap_v \kappa_v$ (Thm. 3.2.4, Prop. 3.2.2) |
| congruences appear as | equivalence-shaped invariant relations (Thm. 5.3.1) | kernels; fully invariant ones = theories (Thm. 8.2.2) |
| free/universal object | term clone $\mathcal T_\Omega$, free on the signature (Thm. 9.2.2) | $\mathbf T_\Omega(X)$, free on generators (FTS Thm. 2.3.3) |

### 10.4. Operation Classes on One Algebra

$$
\mathcal J_A \;\subseteq\; \operatorname{Clo}(\mathbf A) \;\subseteq\; \operatorname{Pol}(\mathbf A) \;\subseteq\; \{\text{congruence-preserving}\} \;\subseteq\; \mathcal O_A
$$

| class | preserves subuniverses? | commutes with homomorphisms? | compatible with congruences? | syntax certificate |
|---|---|---|---|---|
| $\operatorname{Clo}(\mathbf A)$ | yes (Thm. 4.1.1) | yes, all (Thm. 4.1.2) | yes (Thm. 4.2.1) | a term |
| $\operatorname{Pol}(\mathbf A)$ | no (Warn. 4.2.3) | along surjections (Prop. 4.4.5) | yes (Thm. 4.2.2) | a template (term + parameters) |
| congruence-preserving | no | no | yes, by definition | none in general (Thm. 4.4.2) |
| $\mathcal O_A$ | no | no | no | — |

### 10.5. Failure-Mode Checklist

1. **Term vs. term operation** (Warning 1.2.4, Theorem 3.2.4): $\mathsf{op}$ is not injective; equality of induced operations is $\operatorname{Id}(\mathbf A)$, not syntactic equality. Formal polynomials vs. polynomial functions is the same distinction (Warning 3.3.2).
2. **$\kappa_g$ vs. $\operatorname{Id}$** (Remark 3.2.3, Warning 7.3.5): one valuation's coincidences vs. all valuations' laws; quantifier prefixes in collapse statements are mandatory.
3. **$\kappa_g$ is not fully invariant** (Warning 8.2.3): substitution destroys coincidences; only laws survive.
4. **$\theta_E$ vs. $\theta_E^{\mathrm{fi}}$** (Remark 8.1.3, FTS Warning 8.4.5): ground relations vs. schematic identities; context-closure vs. context-plus-substitution closure.
5. **Descent is not free** (Theorems 7.1.3, 7.3.2): case analysis on constructors does not survive collapse; pattern matching is legitimate only on free syntax ($\kappa_g = \Delta$) or with a compatibility certificate.
6. **Polynomial parameters break subuniverses and non-surjective transport** (Warning 4.2.3, Proposition 4.4.5): $\operatorname{Pol}$-level facts hold for congruences, not for subalgebras or general homomorphisms.
7. **Congruence-preserving $\ne$ polynomial** (Theorem 4.4.2): simple algebras make every operation congruence-preserving; affine completeness is special.
8. **Finite-carrier Galois closure fails on infinite carriers** (Warning 5.3.4): local closure is required; $\operatorname{Pol}(\operatorname{Inv}(F)) \neq \langle F\rangle_{\mathrm{clone}}$ in general.
9. **$\operatorname{Pol}(\mathbf A)$ vs. $\operatorname{Pol}(Q)$** (Warning 3.3.2): polynomial clone of an algebra vs. polymorphism clone of relations — one symbol, two operators, disambiguated by argument type.
10. **The clone forgets the signature** (Warning 2.2.3): presentation-dependent properties do not transfer between term-equivalent presentations; congruence data does not determine the clone (Example 9.1.4, item 4).
11. **No homomorphic return from semantics to syntax** (Warning 9.2.4): representative choice is a section only set-theoretically; canonical sections are normal-form functions and exist only under convergent rewriting.
12. **Variable-supply hypotheses matter** (Theorems 6.1.2, 8.2.2): rigidity of syntax needs enough generators; equational theories need $X_\omega$.

### 10.6. Closing Statement

The companion treatise established that every concrete generated algebra is syntax modulo semantic identification: $\langle g[X]\rangle_{\mathbf B} \cong \mathbf T_\Omega(X)/\kappa_g$. The present treatise establishes the operation-level half of that dictionary. The derived operations of any algebra form its clone, presented by raw terms through the operation map $\mathsf{op}$, whose kernel is the equational theory — so the clone is syntax modulo laws, exactly as the carrier of a generated algebra is syntax modulo $\kappa_g$. Compatibility theorems identify the structural objects of universal algebra as invariants: subuniverses and homomorphisms are the invariants of the term clone, congruences the invariants of the polynomial clone, and the two Galois connections — Pol–Inv on a fixed carrier, Id–Mod across all carriers — organize these invariants into dually isomorphic lattices of clones and relational clones, theories and varieties. The descent calculus along $\kappa_g$ is where the levels meet: polynomial and context operations on raw syntax descend to every collapse, unconditionally and surjectively, because congruences are by nature polynomial-compatible; arbitrary syntactic operations descend exactly when they send $\kappa_g$-equivalent inputs to $\kappa_g$-equivalent outputs; and demanding descent everywhere is demanding congruence-preservation, of which the template calculus is the certified core. Building in syntax and evaluating, evaluating and building concretely, or residing in a presented quotient are therefore three routes through one commuting diagram — interchangeable precisely on the polynomial clone, and beyond it only where compatibility has been proved.
