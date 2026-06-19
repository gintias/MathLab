---
title: "Sorted Syntax, Binding, Effective Equational Reasoning, and the Coalgebraic Dual"
subtitle: "A Companion Treatise to the Free–Forgetful Architecture of Universal Algebra"
tags: [universal-algebra, many-sorted, order-sorted, partial-algebra, binding, alpha-equivalence, de-bruijn, nominal-sets, algebraic-logic, cylindric-algebra, unification, term-rewriting, knuth-bendix, tree-automata, coalgebra, coinduction, varieties, clones, lawvere-theories]
---

# Sorted Syntax, Binding, Effective Equational Reasoning, and the Coalgebraic Dual

## 0. Orientation

This treatise is a companion to a prior development (hereafter the **base treatise**) that constructs, for a fixed signature $\Omega$ and generator set $X$, the free $\Omega$-algebra $\mathbf{T}_\Omega(X)$ by its universal mapping property, realizes it as the term algebra, presents its concrete carriers (trees, tuples, strings), defines evaluation $\operatorname{ev}_g : \mathbf{T}_\Omega(X)\to B$, derives the quotient theory of generated subalgebras and presentations $\langle X\mid E\rangle$, develops substitution and equational logic, generalizes to relational generation, specializes to logic, and repackages everything categorically as a free–forgetful adjunction $F\dashv U$ and a term monad. The single invariant of that development is the equation

$$
\textbf{freeness} \;=\; \textbf{generatedness} \;+\; \textbf{injectivity (unique decomposition).}
$$

The present companion develops the bodies of theory that the base treatise states and defers, or that sit dual to its constructions. It is organized around four refinements of the same architecture:

- **Richer carriers of syntax.** The base treatise fixes a single-sorted, total signature. Part I generalizes the carrier of syntax along three axes — *sorts* (many-sorted and order-sorted signatures), and *partiality* (partial $\Omega$-algebras) — and rebuilds the term algebra, congruence, quotient, and equational-logic layers in each.
- **Variable binding.** The base treatise proves (its Warning 10.4.2) that quantifiers and other binders are not operation symbols and that first-order syntax "exceeds bare universal algebra." Part II supplies the missing apparatus: $\alpha$-equivalence, de Bruijn presentations, nominal sets, and binding signatures with their initial-algebra (presheaf) semantics.
- **Re-algebraization of logic.** Part III continues the deferred thread by exhibiting the standard algebraic treatments of quantification — cylindric and polyadic algebras — which recover an equational-algebraic description of first-order logic at the cost of infinite-dimensional structure.
- **Effectivity and its dual.** The base treatise isolates *abstract* freeness from *effective* parsing and notes that the word problem may be undecidable, but it does not develop the algorithmic theory. Parts IV–V supply unification, term rewriting (termination orderings, critical pairs, completion), narrowing, and the recognizability theory of tree automata. Part VI develops the coalgebraic and infinitary **dual** of the initial-algebra/recursion theory: infinite terms, final coalgebras, corecursion, and coinduction. Part VII fills in the structure theory of equational classes (the full Birkhoff theorem, clones, Lawvere theories, finitary monads, quasivarieties) of which the base treatise states only the headline.

The companion preserves the base treatise's conventions: numbered, labeled, callout-boxed formal items form the spine; running prose records only structural relationships; **no proofs are given**. Each definition states its data and conditions; each theorem states its hypotheses before its conclusion; each construction states its well-definedness requirements. The document is self-contained relative to its scope: §1 recapitulates exactly the prerequisites used below, after which all new objects are defined before use.

> [!remark] Remark 0.1: Relationship to the base treatise and reading conventions
> Cross-references of the form "(base treatise §5.5)" point to the prior document; all internal references "(§7.2)", "Theorem 12.2.2" point within this companion. Where a base-treatise object is needed, §1 restates it compactly with a fresh internal label so that the companion can be read independently. The default ambient set theory is $\mathsf{ZFC}$ with a Grothendieck universe $\mathcal U$ available for size control; departures (choice principles, large cardinals, constructive readings) are flagged in remarks where they matter.

---

## 1. Recapitulation of Prerequisites

This part fixes notation and restates, without proof and in the precise form used below, the base-treatise material on which the companion depends. Nothing here is new; readers of the base treatise may skim to §1.5.

### 1.1. Set-Theoretic Conventions

> [!notation] Notation 1.1.1: Ambient conventions
> Work in $\mathsf{ZFC}$. $\mathbb N=\{0,1,2,\dots\}$; $n\in\mathbb N$ is identified with $\{0,\dots,n-1\}$ when convenient; $\omega$ is the first infinite ordinal. For sets, $S^T$ is the set of functions $T\to S$, $S^n=S^{\{0,\dots,n-1\}}$, $S^{<\omega}=\bigcup_{n\in\mathbb N}S^n$ the finite sequences over $S$ (empty sequence $\varepsilon$, concatenation $u\cdot v$), $\mathcal P(S)$ the power set, $|S|$ the cardinality, and $\coprod$ the disjoint (tagged) union. Function composition $g\circ f$ applies $f$ first; $\mathrm{id}_S$ is the identity; $f[U]$ the image of $U\subseteq\operatorname{dom}(f)$; $\operatorname{im}(f)=f[\operatorname{dom}(f)]$. Set equality is $=$, isomorphism $\cong$, definitional equality $:=$.

> [!notation] Notation 1.1.2: Indexed families and dependent products
> For an index set $I$ and sets $(S_i)_{i\in I}$, $\prod_{i\in I}S_i$ is the set of choice functions $i\mapsto s_i\in S_i$ and $\coprod_{i\in I}S_i=\{(i,s):i\in I,\,s\in S_i\}$. An $I$-**indexed family of sets** is a function $i\mapsto S_i$; an $I$-**indexed family of functions** $(h_i:S_i\to T_i)_{i\in I}$ acts componentwise.

### 1.2. Signatures and Algebras

> [!definition] Definition 1.2.1: Single-sorted signature and $\Omega$-algebra
> A **(single-sorted) signature** is a pair $\Omega=(\Sigma,\operatorname{ar})$ with $\Sigma$ a set of **operation symbols** and $\operatorname{ar}:\Sigma\to\mathbb N$ the **arity function**; $\Omega_n:=\{f\in\Sigma:\operatorname{ar}(f)=n\}$, and $\Omega_0$ is the set of **constant symbols**. An **$\Omega$-algebra** is a pair $A=(|A|,(f^A)_{f\in\Sigma})$ with carrier $|A|$ and, for each $f\in\Omega_n$, an interpretation $f^A:|A|^n\to|A|$ (so $c^A\in|A|$ for $c\in\Omega_0$). A **homomorphism** $h:A\to B$ satisfies $h(f^A(a_1,\dots,a_n))=f^B(h(a_1),\dots,h(a_n))$ for all $f,a_i$. The category of $\Omega$-algebras is $\mathbf{Alg}(\Omega)$.

> [!definition] Definition 1.2.2: Subalgebras, products, generated subalgebra
> $C\subseteq|A|$ is **closed** if it contains $c^A$ for $c\in\Omega_0$ and is closed under each $f^A$; closed sets carry the **subalgebra** structure $C\le A$. The **direct product** $\prod_{i\in I}A_i$ has carrier $\prod_i|A_i|$ with coordinatewise operations and is the categorical product. For $S\subseteq|A|$, the **generated subalgebra** $\langle S\rangle_A$ is the least closed superset of $S$.

### 1.3. Term Algebra and Universal Mapping Property

> [!definition] Definition 1.3.1: Term algebra and freeness
> For a signature $\Omega$ and a set $X$ with $X\cap\Sigma=\varnothing$, the set $T_\Omega(X)$ of **terms** is the least set containing $X$ and $\Omega_0$ and closed under $f(t_1,\dots,t_n)$ for $f\in\Omega_n$ ($n\ge1$). The **term algebra** $\mathbf T_\Omega(X)$ has carrier $T_\Omega(X)$, formal operations $f^{\mathbf T}(t_1,\dots,t_n):=f(t_1,\dots,t_n)$, and insertion $\eta_X:X\to T_\Omega(X)$, $x\mapsto x$. A pair $(F,\eta)$ with $\eta:X\to|F|$ is **free on $X$** if every $g:X\to|A|$ extends uniquely to a homomorphism $\widehat g:F\to A$ with $\widehat g\circ\eta=g$.

> [!theorem] Theorem 1.3.2: The term algebra is free; evaluation
> $(\mathbf T_\Omega(X),\eta_X)$ is free on $X$, and any free algebra on $X$ is uniquely isomorphic to it compatibly with the insertion. For an $\Omega$-algebra $B$ and $g:X\to|B|$, the **evaluation homomorphism** $\operatorname{ev}_g:\mathbf T_\Omega(X)\to B$ is the unique homomorphic extension, satisfying $\operatorname{ev}_g(x)=g(x)$, $\operatorname{ev}_g(c)=c^B$, $\operatorname{ev}_g(f(t_1,\dots,t_n))=f^B(\operatorname{ev}_g(t_1),\dots,\operatorname{ev}_g(t_n))$.

> [!definition] Definition 1.3.3: Subterms, positions, contexts
> The set of **positions** (addresses) of a term $t$ is the finite prefix-closed set $\operatorname{Pos}(t)\subseteq\mathbb N_{>0}^{<\omega}$ defined by $\operatorname{Pos}(x)=\operatorname{Pos}(c)=\{\varepsilon\}$ and $\operatorname{Pos}(f(t_1,\dots,t_n))=\{\varepsilon\}\cup\bigcup_{i=1}^n\{i\cdot p:p\in\operatorname{Pos}(t_i)\}$. The **subterm** at $p$ is $t|_p$; the symbol at $p$ is $t(p)$. A **context** $C[\,]$ is a term over $\Omega$ and $X\sqcup\{\Box\}$ with a single occurrence of a fresh nullary hole $\Box$; $C[s]$ replaces the hole by $s$. $\operatorname{var}(t)\subseteq X$ is the set of variables occurring in $t$.

### 1.4. Congruences, Quotients, Equational Logic

> [!definition] Definition 1.4.1: Congruence and quotient
> A **congruence** on $A$ is an equivalence relation $\theta\subseteq|A|^2$ compatible with every operation: $(a_i,b_i)\in\theta$ for all $i$ implies $(f^A(\bar a),f^A(\bar b))\in\theta$. The **quotient** $A/\theta$ has carrier $|A|/\theta$ and operations $f^{A/\theta}([\bar a])=[f^A(\bar a)]$, well-defined exactly because $\theta$ is a congruence; $\operatorname{nat}_\theta:A\to A/\theta$ is the canonical surjection. The **kernel** of $h:A\to B$ is $\ker h=\{(a,a'):h(a)=h(a')\}\in\operatorname{Con}(A)$, and the **First Isomorphism Theorem** gives a unique iso $A/\ker h\cong\operatorname{im}(h)$.

> [!definition] Definition 1.4.2: Equations, presentations, identities
> An **equation** over $(\Omega,X)$ is a pair $s\approx t\in T_\Omega(X)^2$. For $E\subseteq T_\Omega(X)^2$, $\theta_E:=\operatorname{Cg}(E)$ is the least congruence containing $E$ and $\langle X\mid E\rangle:=\mathbf T_\Omega(X)/\theta_E$ the **presented algebra**. $s\approx t$ is an **identity of $A$**, written $A\models s\approx t$, if $\operatorname{ev}_v(s)=\operatorname{ev}_v(t)$ for every $v:X\to|A|$. The least congruence containing $E$ and closed also under substitution is the **fully invariant congruence** $\theta_E^{\mathrm{fi}}$, and **Birkhoff completeness** gives $E\vdash s\approx t\iff E\models s\approx t$, with derivability the closure under reflexivity, symmetry, transitivity, congruence (replacement in contexts), and substitution.

> [!definition] Definition 1.4.3: Substitution as evaluation into syntax
> A **substitution** $\sigma:X\to T_\Omega(Y)$ induces the homomorphism $\widehat\sigma=\operatorname{ev}_\sigma:\mathbf T_\Omega(X)\to\mathbf T_\Omega(Y)$, written $t\mapsto t\sigma$ (postfix), with $x\sigma=\sigma(x)$, $c\sigma=c$, $f(\bar t)\sigma=f(\overline{t\sigma})$. The composite of $\sigma:X\to T_\Omega(Y)$ and $\tau:Y\to T_\Omega(Z)$ is $(\sigma;\tau)(x)=(\sigma(x))\tau$, giving $t(\sigma;\tau)=(t\sigma)\tau$; this is the Kleisli composition of the **term monad** $(T,\eta,\mu)$ with $T(X)=T_\Omega(X)$.

### 1.5. Companion Notation

> [!notation] Notation 1.5.1: Conventions specific to this companion
> Substitutions act on the right ($t\sigma$), composition of substitutions is written $\sigma;\tau$ ("first $\sigma$, then $\tau$"), and $\{x_1\mapsto t_1,\dots,x_k\mapsto t_k\}$ denotes the substitution sending the listed variables as shown and every other variable to itself; its **domain** is $\{x_i:x_i\ne t_i\}$ and its **range variables** are $\bigcup_i\operatorname{var}(t_i)$. Rewrite relations are written $\to$, their reflexive–transitive closure $\to^{*}$, symmetric closure $\leftrightarrow$, and the generated equivalence $\leftrightarrow^{*}$. For a poset/preorder the strict part is decorated with $<$. The Greek letter $\theta$ is reserved for congruences, $\sigma,\tau,\rho$ for substitutions, $\varrho$ for rules, and $\mathcal A,\mathcal B$ for automata.

> [!remark] Remark 1.5.2: Standing finiteness hypotheses
> Unless a clause says otherwise, every signature in Parts I–V is **finitary** (all arities in $\mathbb N$) and every term, derivation, and tree is **finite**. Infinitary arities, infinite terms, and transfinite stage constructions appear only where explicitly invoked, chiefly in Part VI. Finiteness is what makes the stage closure stabilize at $\omega$, makes structural induction available, and makes the rewriting and automata algorithms terminate.

---

# Part I — Sorted and Partial Carriers of Syntax

## 2. Many-Sorted Algebra

The base treatise is single-sorted: one carrier, operations of shape $|A|^n\to|A|$. Many computational and logical signatures are intrinsically **typed**: a function symbol consumes arguments of prescribed sorts and returns a value of a prescribed sort. This part rebuilds the entire free-algebra/term/congruence/quotient/equational-logic apparatus over a fixed set of sorts. The single-sorted theory is the case $|S|=1$.

### 2.1. Sorted Signatures

> [!definition] Definition 2.1.1: Many-sorted signature
> Fix a set $S$ of **sorts**. An **$S$-sorted signature** is a pair $\Sigma=(\mathrm{Op},\operatorname{type})$ where $\mathrm{Op}$ is a set of **operation symbols** and
> $$
> \operatorname{type}:\mathrm{Op}\to S^{<\omega}\times S
> $$
> assigns to each $f$ an **input arity** $w\in S^{<\omega}$ and an **output sort** $s\in S$, written $f:w\to s$ or $f:s_1\cdots s_n\to s$. A symbol with $w=\varepsilon$ is a **constant of sort $s$**, written $f:{\to}\,s$. Equivalently $\Sigma$ is an $(S^{<\omega}\times S)$-indexed family $(\Sigma_{w,s})_{w\in S^{<\omega},\,s\in S}$ of pairwise-disjoint symbol sets, $\Sigma_{w,s}:=\{f:f:w\to s\}$.

> [!notation] Notation 2.1.2: Sort words and arity
> For $w=s_1\cdots s_n\in S^{<\omega}$, the **length** $|w|=n$ is the **arity** of any $f:w\to s$. The sort word $w$ is the **input profile** and $s$ the **result sort**. A signature is **finitary** when every profile is finite (the standing assumption). For $S=\{\ast\}$, profiles reduce to natural numbers and Definition 2.1.1 reduces to the single-sorted Definition 1.2.1.

> [!example] Example 2.1.3: Sorted signatures
> (i) **Stacks** over a sort of elements: sorts $S=\{\mathsf{elt},\mathsf{stack}\}$, operations $\mathsf{empty}:{\to}\,\mathsf{stack}$, $\mathsf{push}:\mathsf{elt}\,\mathsf{stack}\to\mathsf{stack}$, $\mathsf{top}:\mathsf{stack}\to\mathsf{elt}$, $\mathsf{pop}:\mathsf{stack}\to\mathsf{stack}$. (ii) **Modules** over a ring: sorts $\{\mathsf{r},\mathsf{m}\}$ with ring operations on $\mathsf r$, abelian-group operations on $\mathsf m$, and scalar multiplication $\cdot:\mathsf r\,\mathsf m\to\mathsf m$. (iii) **Typed $\lambda$-terms** (without binding, just the applicative skeleton): one sort per simple type, with $\mathrm{app}_{\sigma\to\tau}:(\sigma{\to}\tau)\,\sigma\to\tau$.

### 2.2. Sorted Algebras and Homomorphisms

> [!definition] Definition 2.2.1: $\Sigma$-algebra (many-sorted)
> A **$\Sigma$-algebra** $A$ consists of an $S$-indexed family of **carrier sets** $(|A|_s)_{s\in S}$ and, for each $f:s_1\cdots s_n\to s$ in $\mathrm{Op}$, a function
> $$
> f^A:|A|_{s_1}\times\cdots\times|A|_{s_n}\to|A|_s,
> $$
> (so a constant $f:{\to}\,s$ is an element $f^A\in|A|_s$). The family $(|A|_s)_s$ is the **carrier**; sorts with $|A|_s=\varnothing$ are **empty sorts**.

> [!definition] Definition 2.2.2: Sorted homomorphism
> A **homomorphism** $h:A\to B$ of $\Sigma$-algebras is an $S$-indexed family $(h_s:|A|_s\to|B|_s)_{s\in S}$ of functions such that for every $f:s_1\cdots s_n\to s$ and all $a_i\in|A|_{s_i}$,
> $$
> h_s\big(f^A(a_1,\dots,a_n)\big)=f^B\big(h_{s_1}(a_1),\dots,h_{s_n}(a_n)\big).
> $$
> Identities and composition are sortwise; the category of $\Sigma$-algebras is $\mathbf{Alg}(\Sigma)$. A homomorphism is an **embedding** if each $h_s$ is injective, an **isomorphism** if each $h_s$ is a bijection (equivalently a homomorphism with a two-sided inverse homomorphism).

> [!definition] Definition 2.2.3: Sorted subalgebras and products
> A **sorted subset** $C=(C_s)_{s}$ with $C_s\subseteq|A|_s$ is **closed** if $f^A(\bar a)\in C_s$ whenever $f:w\to s$ and the $a_i$ lie in the corresponding $C_{s_i}$ (including $f^A\in C_s$ for constants). Closed sorted subsets carry subalgebra structure $C\le A$. The **direct product** $\prod_{i\in I}A_i$ has carrier $(\prod_i|A_i|_s)_s$ and coordinatewise operations and is the categorical product in $\mathbf{Alg}(\Sigma)$. For $S$-sorted $G=(G_s)_s\subseteq|A|$ the **generated subalgebra** $\langle G\rangle_A$ is the least closed sorted superset.

> [!remark] Remark 2.2.4: Everything is indexed, nothing else changes
> $\mathbf{Alg}(\Sigma)$ is, formally, the category of models of a single-sorted theory in the slice over $S$: it equals the category of $\Sigma$-algebras internal to $\mathbf{Set}^S$. Limits, the subalgebra lattice, the congruence lattice, and the isomorphism theorems all transfer verbatim from the single-sorted case by performing every construction sortwise. The genuinely new phenomena are confined to (a) **empty sorts**, which break some equational-logic statements (§2.6), and (b) the interaction of sorts with subsorts (§3) and partiality (§4).

### 2.3. Sorted Terms and the Sorted Term Algebra

> [!definition] Definition 2.3.1: Sorted variables and sorted terms
> A **sorted variable family** is an $S$-indexed family $X=(X_s)_s$ of pairwise-disjoint sets, disjoint from $\mathrm{Op}$. The $S$-indexed family $T_\Sigma(X)=(T_\Sigma(X)_s)_s$ of **sorted terms** is the least family closed under:
> $$
> \textbf{(var)}\ x\in T_\Sigma(X)_s \text{ for } x\in X_s;\qquad \textbf{(op)}\ \frac{t_1\in T_\Sigma(X)_{s_1}\ \cdots\ t_n\in T_\Sigma(X)_{s_n}}{f(t_1,\dots,t_n)\in T_\Sigma(X)_s}\ \ (f:s_1\cdots s_n\to s).
> $$
> Each term has a **unique sort**: the families $T_\Sigma(X)_s$ are pairwise disjoint. Constants $f:{\to}\,s$ enter via (op) with $n=0$.

> [!construction] Construction 2.3.2: Sorted term algebra
> $\mathbf T_\Sigma(X)$ is the $\Sigma$-algebra with carrier $(T_\Sigma(X)_s)_s$, formal operations $f^{\mathbf T}(t_1,\dots,t_n):=f(t_1,\dots,t_n)$, and sorted insertion $\eta_X=(\eta_{X,s})_s$, $\eta_{X,s}(x):=x$ for $x\in X_s$.

> [!theorem] Theorem 2.3.3: Sorted universal mapping property
> $(\mathbf T_\Sigma(X),\eta_X)$ is the **free $\Sigma$-algebra on the sorted set $X$**: for every $\Sigma$-algebra $A$ and every **sorted assignment** $g=(g_s:X_s\to|A|_s)_s$ there is a unique homomorphism $\operatorname{ev}_g:\mathbf T_\Sigma(X)\to A$ with $\operatorname{ev}_g\circ\eta_X=g$, given sortwise by the recursive clauses of Theorem 1.3.2. Consequently $\mathbf T_\Sigma(-):\mathbf{Set}^S\to\mathbf{Alg}(\Sigma)$ is left adjoint to the forgetful functor $\mathbf{Alg}(\Sigma)\to\mathbf{Set}^S$.

> [!definition] Definition 2.3.4: Sorted polynomial functor
> The **sorted signature endofunctor** $H_\Sigma:\mathbf{Set}^S\to\mathbf{Set}^S$ is
> $$
> \big(H_\Sigma Y\big)_s \;:=\; \coprod_{f:\,s_1\cdots s_n\to s}\ Y_{s_1}\times\cdots\times Y_{s_n}\qquad(s\in S).
> $$
> An $H_\Sigma$-algebra $(Y,\alpha:H_\Sigma Y\to Y)$ is the same as a $\Sigma$-algebra; the initial $H_\Sigma$-algebra is $\mathbf T_\Sigma(\varnothing)$ (ground terms), and the free $H_\Sigma$-algebra on $X$ is $\mathbf T_\Sigma(X)$. Structural recursion over sorted terms is the unique-catamorphism property of this initial/free algebra.

> [!warning] Warning 2.3.5: Empty carriers and non-inhabited sorts
> If some sort $s$ has $X_s=\varnothing$ and no ground term of sort $s$ exists (no constant of sort $s$ and no way to build one), then $T_\Sigma(X)_s=\varnothing$. Empty term-sorts are legitimate but interact subtly with equational deduction (Warning 2.6.3). A $\Sigma$-algebra may also have empty carriers; the single-sorted convention "algebras are nonempty when $\Omega_0\ne\varnothing$" has no many-sorted analogue forcing *all* sorts nonempty.

### 2.4. Sorted Congruences and Quotients

> [!definition] Definition 2.4.1: Sorted congruence and quotient
> A **(sorted) congruence** on $A$ is an $S$-indexed family $\theta=(\theta_s)_s$ with each $\theta_s$ an equivalence relation on $|A|_s$, compatible with every operation: for $f:s_1\cdots s_n\to s$, $(a_i,b_i)\in\theta_{s_i}$ for all $i$ implies $(f^A(\bar a),f^A(\bar b))\in\theta_s$. The **quotient** $A/\theta$ has carrier $(|A|_s/\theta_s)_s$ with operations on classes, well-defined exactly by compatibility; $\operatorname{nat}_\theta:A\to A/\theta$ is the sortwise canonical surjection. The congruences form a complete lattice $\operatorname{Con}(A)$ under sortwise inclusion.

> [!theorem] Theorem 2.4.2: Sorted isomorphism theorems
> For $h:A\to B$, $\ker h:=(\{(a,a'):h_s(a)=h_s(a')\})_s$ is a sorted congruence, $\operatorname{im}(h)\le B$, and there is a unique isomorphism $A/\ker h\cong\operatorname{im}(h)$ with $[a]\mapsto h(a)$. The correspondence theorem and the second/third isomorphism theorems hold sortwise. Every $\Sigma$-algebra is a homomorphic image of a free $\Sigma$-algebra, and the class of $\Sigma$-algebras is exactly the class of quotients of sorted term algebras.

### 2.5. Sorted Substitution and the Sorted Term Monad

> [!definition] Definition 2.5.1: Sorted substitution
> A **sorted substitution** $\sigma:X\to T_\Sigma(Y)$ is a sort-respecting family $(\sigma_s:X_s\to T_\Sigma(Y)_s)_s$; its induced homomorphism $\widehat\sigma:\mathbf T_\Sigma(X)\to\mathbf T_\Sigma(Y)$ is the evaluation of Theorem 2.3.3 with target $\mathbf T_\Sigma(Y)$. Composition $\sigma;\tau$ is Kleisli composition, and $(T_\Sigma,\eta,\mu)$ is a monad on $\mathbf{Set}^S$, the **sorted term monad**, whose Eilenberg–Moore category is $\mathbf{Alg}(\Sigma)$.

> [!remark] Remark 2.5.2: Sort discipline is a typing discipline on substitution
> A sorted substitution may replace a variable only by a term of the **same sort**. This is precisely the typing constraint that makes substitution sort-preserving and the substitution lemma (base treatise Theorem 8.3.1) hold sortwise. Sort mismatches are not "ill-defined substitutions"; they are simply not substitutions of the sorted signature.

### 2.6. Sorted Equational Logic and the Empty-Carrier Anomaly

> [!definition] Definition 2.6.1: Sorted equation and satisfaction
> A **sorted equation** is a triple $(\Gamma,s,t)$ — usually written $\Gamma\vdash s\approx t$ or $(\forall\Gamma)\,s\approx t$ — where $\Gamma$ is a finite sorted set of variables (the **explicit context**), $s,t\in T_\Sigma(\Gamma)_\sigma$ are terms of a common sort $\sigma$. A $\Sigma$-algebra $A$ **satisfies** $(\Gamma,s,t)$ if $\operatorname{ev}_v(s)=\operatorname{ev}_v(t)$ for every assignment $v:\Gamma\to|A|$. The context $\Gamma$ is part of the equation, not metadata.

> [!theorem] Theorem 2.6.2: Sound and complete sorted equational calculus
> With equations carrying explicit contexts as in Definition 2.6.1, the rules reflexivity, symmetry, transitivity, congruence, and substitution — each respecting sorts and contexts — are **sound and complete** for many-sorted equational consequence: $E\vdash(\Gamma,s,t)\iff E\models(\Gamma,s,t)$. The free algebra of the variety defined by $E$ on a sorted set $X$ is $\mathbf T_\Sigma(X)/\theta^{\mathrm{fi}}_E$ with $\theta^{\mathrm{fi}}_E$ the least fully invariant sorted congruence containing $E$.

> [!warning] Warning 2.6.3: Unsound deduction when contexts are dropped over empty sorts
> If equations are written **without** explicit contexts (the naive single-sorted style), many-sorted equational deduction becomes **unsound** in the presence of empty sorts. The classic failure: from $x_s\approx y_s$ (variables of an empty-in-some-model sort $s$) one cannot soundly infer an equation at another sort, yet the contextless calculus permits an instantiation that assumes an element of $s$. Concretely, a derivation may use a variable of a sort that is empty in the target algebra, validating a conclusion that fails there. The standard repairs are: (i) **carry explicit contexts** (Definition 2.6.1, Theorem 2.6.2); (ii) restrict to signatures where **every sort is inhabited** (has a ground term); or (iii) work in the variant calculus of Goguen–Meseguer. This empty-carrier anomaly has no single-sorted counterpart and is the principal pitfall of many-sorted equational logic.

> [!example] Example 2.6.4: Inhabitation removes the anomaly
> If every sort $s$ has at least one ground term (e.g. each sort has a constant), then $T_\Sigma(\varnothing)_s\ne\varnothing$ for all $s$, all algebras of interest can be taken nonempty in every sort, and contextless deduction coincides with context-carrying deduction. Inhabitation is automatic for the signatures of stacks (via $\mathsf{empty}$ plus an element constant), Booleans, and natural numbers, which is why the anomaly is rarely seen in practice yet must be stated.

> [!remark] Remark 2.6.5: Birkhoff for many sorts
> The HSP theorem (developed single-sorted in §19) holds many-sorted: a class of $\Sigma$-algebras is a **variety** (closed under sorted homomorphic images, subalgebras, and products) iff it is the class of models of a set of context-carrying equations. Quasivarieties and the lattice of subvarieties likewise transfer. The translation device is uniform: replace $\mathbf{Set}$ by $\mathbf{Set}^S$ throughout.

---

## 3. Order-Sorted Algebra

Order-sorted algebra refines the many-sorted theory by a **partial order on sorts** modeling subtype/inclusion (e.g. $\mathsf{nat}\le\mathsf{int}\le\mathsf{rat}$). It is the standard semantics for subtyping, partial functions made total on subsorts, and overloaded operators in algebraic specification. The added data is a sort order; the added obligations are coherence conditions ensuring that terms have **least sorts** and that interpretations agree on overlaps.

### 3.1. Sort Orders and Order-Sorted Signatures

> [!definition] Definition 3.1.1: Sort poset and order-sorted signature
> An **order-sorted signature** is a triple $\Sigma=(S,\le,\mathrm{Op})$ where $(S,\le)$ is a poset of **sorts** (with $\le$ read as **subsort inclusion**) and $\mathrm{Op}$ is an $S$-sorted operation-symbol family (Definition 2.1.1) on the underlying set $S$. A symbol $f$ may be **overloaded**: it may carry several declarations $f:w_1\to s_1$, $f:w_2\to s_2$, $\dots$ with different profiles.

> [!definition] Definition 3.1.2: Subsort-overloading coherence (monotonicity)
> A signature is **monotone** (subsort-monotone) if whenever $f:w_1\to s_1$ and $f:w_2\to s_2$ are declarations with $w_1\le w_2$ componentwise (same length, $i$-th sorts comparable), then $s_1\le s_2$. Monotonicity ensures that narrowing the input sorts never widens the output sort and is the basic compatibility condition relating overloaded declarations along $\le$.

> [!definition] Definition 3.1.3: Regularity
> $\Sigma$ is **regular** if for every symbol $f$ and every input profile $w_0\in S^{<\omega}$ that is below some declared profile of $f$, the set $\{(w,s):f:w\to s,\ w_0\le w\}$ has a **least element**. Regularity guarantees that each well-typed application has a least output sort; it is the order-sorted prerequisite for least-sort assignment (Theorem 3.3.2).

### 3.2. Order-Sorted Algebras

> [!definition] Definition 3.2.1: Order-sorted $\Sigma$-algebra
> An **order-sorted $\Sigma$-algebra** $A$ is a many-sorted algebra for the underlying sorted signature (Definition 2.2.1) such that:
> $$
> \textbf{(subsort inclusion)}\quad s\le s'\ \Longrightarrow\ |A|_s\subseteq|A|_{s'},
> $$
> $$
> \textbf{(operation agreement)}\quad f:w_1\to s_1,\ f:w_2\to s_2,\ \bar a\in|A|^{w_1}\cap|A|^{w_2}\ \Longrightarrow\ f^{A}_{w_1}(\bar a)=f^{A}_{w_2}(\bar a).
> $$
> Thus smaller sorts denote subsets of larger ones, and overloaded interpretations of $f$ agree wherever their domains overlap. A **homomorphism** is a many-sorted homomorphism whose components are **compatible with inclusions**: $h_{s}$ and $h_{s'}$ agree on $|A|_s$ when $s\le s'$.

> [!remark] Remark 3.2.2: Carriers form a presheaf on the sort poset
> The subsort-inclusion condition says the carrier is a functor $(S,\le)\to\mathbf{Set}$ landing in inclusions, i.e. a coherent system of subsets; operation agreement says each (possibly overloaded) symbol is interpreted by a single partial function on the union of carriers, restricting correctly. Order-sorted algebra is therefore many-sorted algebra constrained so that sorts are *subsets* rather than independent sets.

### 3.3. Order-Sorted Terms and Least Sorts

> [!definition] Definition 3.3.1: Order-sorted terms
> Fix a sorted variable family $X$ with $x\in X_s$ having declared sort $s$. The **order-sorted terms** are generated by: every $x\in X_s$ is a term of sort $s$; and if $t_i$ is a term of some sort $s_i'\le s_i$ for a declaration $f:s_1\cdots s_n\to s$, then $f(t_1,\dots,t_n)$ is a term of sort $s$. A term is **well-formed** if it has at least one sort under these rules. Because of subsorting, a single term may have **several** sorts.

> [!theorem] Theorem 3.3.2: Least-sort theorem
> If $\Sigma$ is regular (Definition 3.1.3), every well-formed order-sorted term $t$ has a **least sort** $\mathrm{ls}(t)\in S$: the set of sorts of $t$ has a minimum, and $\mathrm{ls}(t)\le s$ for every sort $s$ of $t$. Least sorts are computed bottom-up: $\mathrm{ls}(x)=s$ for $x\in X_s$, and $\mathrm{ls}(f(\bar t))$ is the least result sort among declarations of $f$ whose input profile dominates $(\mathrm{ls}(t_i))_i$.

> [!construction] Construction 3.3.3: Order-sorted term algebra and freeness
> The **order-sorted term algebra** $\mathbf T_\Sigma(X)$ assigns to each sort $s$ the set of well-formed terms of some sort $\le s$ (so subsort inclusion holds), with formal operations and insertion as before. It is the free order-sorted $\Sigma$-algebra on $X$: every sort-respecting assignment $g$ extends uniquely to an order-sorted homomorphism $\operatorname{ev}_g$. Regularity is what makes evaluation well-defined despite overloading (operation agreement, Definition 3.2.1, resolves the overload).

### 3.4. Retracts, Sort Constraints, and Errors

> [!definition] Definition 3.4.1: Retracts
> When a term is well-formed only after a sort can be **lowered** (e.g. dividing two integers and asserting the result is a natural), specification languages add **retract** symbols $r_{s'\!,s}:s'\to s$ for $s\le s'$, interpreted as partial inclusions (identity on $|A|_s\subseteq|A|_{s'}$, undefined elsewhere). Retracts turn ill-sorted-but-intended applications into terms with explicit, checkable sort-lowering obligations, evaluated by the partial-algebra machinery of §4.

> [!warning] Warning 3.4.2: Ad hoc vs subsort overloading; loss of least sorts
> Two distinct phenomena share the word "overloading." **Subsort overloading** (declarations related along $\le$, constrained by monotonicity and agreement) is semantically coherent. **Ad hoc overloading** (a symbol reused at incomparable profiles with unrelated meanings) is *not* governed by Definition 3.2.1 and generally destroys regularity, so least sorts fail and the term algebra is no longer free. Mixing the two without preregularity checks is the principal order-sorted error; the repair is to require **preregular** (regular) signatures and to disambiguate ad hoc overloads by distinct symbols.

> [!remark] Remark 3.4.3: Reduction to many-sorted algebra
> Every order-sorted signature can be **encoded** into a many-sorted signature with explicit coercion (inclusion) functions and equations forcing them to be injective and coherent; order-sorted algebras correspond to the resulting many-sorted models satisfying these equations. The order-sorted formalism is therefore not strictly more expressive, but it is markedly more economical and supports least-sort parsing, which the encoded many-sorted version does not provide directly.

---

## 4. Partial Algebras

The base treatise uses only **total** operations and notes (its Warning 1.4.3) that bijective homomorphisms need not be isomorphisms once partiality enters. A **partial $\Omega$-algebra** interprets each operation by a partial function. Partiality is unavoidable for $\mathsf{top}/\mathsf{pop}$ on the empty stack, for division, for the destructors of free presentations, and for any "definedness-sensitive" specification. The equational logic must then track **definedness**, which is the substance of this part.

### 4.1. Partial Operations and Homomorphisms

> [!definition] Definition 4.1.1: Partial $\Omega$-algebra
> For a (single- or many-sorted) signature $\Omega$, a **partial $\Omega$-algebra** $A$ assigns to each $f\in\Omega_n$ a **partial function** $f^A:|A|^n\rightharpoonup|A|$ with domain of definition $\operatorname{dom}(f^A)\subseteq|A|^n$. A constant may be **undefined**. The algebra is **total** iff every $\operatorname{dom}(f^A)=|A|^n$.

> [!notation] Notation 4.1.2: Kleene equality and definedness
> For terms/expressions $u,v$ with values in $|A|$ under an assignment, write $u{\downarrow}$ ("$u$ is **defined**") if its value exists, $u{\uparrow}$ if undefined, and use **Kleene (strong) equality** $u\simeq v$ meaning "either both undefined, or both defined and equal." **Existence (weak) equality** $u\stackrel{e}{=}v$ means "both defined and equal." Evaluation is **strict**: $f^A(\bar u){\downarrow}$ requires every $u_i{\downarrow}$ and $(\,\text{their values}\,)\in\operatorname{dom}(f^A)$.

> [!definition] Definition 4.1.3: Weak, closed, and strong homomorphisms
> Let $h:|A|\to|B|$ between partial algebras. Then $h$ is a:
> $$
> \textbf{weak homomorphism: } f^A(\bar a){\downarrow}\ \Longrightarrow\ h(f^A(\bar a))=f^B(h\bar a)\ \text{(in particular }f^B(h\bar a){\downarrow}\text{)};
> $$
> $$
> \textbf{closed homomorphism: weak, and } f^B(h\bar a){\downarrow}\ \Longrightarrow\ f^A(\bar a){\downarrow}\ \text{(reflects definedness on the image)};
> $$
> $$
> \textbf{strong (full) homomorphism: weak, and } h\bar a\in\operatorname{dom}(f^B)\ \Longrightarrow\ \bar a\in\operatorname{dom}(f^A).
> $$
> The three notions coincide for total algebras and give three different categories of partial algebras otherwise.

> [!warning] Warning 4.1.4: Bijective weak homomorphisms are not isomorphisms
> A bijective **weak** homomorphism need not be an isomorphism: it may map an undefined application to a defined one (it preserves but does not reflect definedness). Isomorphisms of partial algebras are the bijective **closed** homomorphisms whose inverse is also a homomorphism, equivalently the bijections that match domains of definition exactly. This is the precise content of the base treatise's Warning 1.4.3 in the partial setting.

### 4.2. Existence Equations and Conditional Axioms

> [!definition] Definition 4.2.1: Existence equation and ECE-equation
> An **existence equation (e-equation)** over $X$ is a formula $s\stackrel{e}{=}t$ asserting both sides defined and equal; the special case $t\stackrel{e}{=}t$, abbreviated $\mathrm{def}(t)$ or $t{\downarrow}$, asserts mere definedness. An **existentially conditioned existence equation (ECE-equation)** has the form
> $$
> \big(\textstyle\bigwedge_{j} \mathrm{def}(r_j)\big)\ \Rightarrow\ s\stackrel{e}{=}t,
> $$
> a finite conjunction of definedness premises implying an e-equation. ECE-equations are the standard axiom format for partial algebras: strong enough to specify destructors and partial operations, weak enough to retain an initial-model semantics.

> [!theorem] Theorem 4.2.2: Existence and structure of initial partial models
> For any signature $\Omega$ and any set $E$ of ECE-equations, the category of partial $\Omega$-algebras satisfying $E$ (with closed homomorphisms) has an **initial object**, constructed as a quotient of the partial term algebra (Construction 4.3.2) by the least **closed congruence** (Definition 4.3.1) generated by $E$. The Birkhoff-style characterization holds: ECE-definable classes are exactly those closed under suitable products, closed subalgebras, and closed-homomorphic images (Andréka–Németi / Burmeister theory).

### 4.3. Partial Term Algebras and Closed Congruences

> [!definition] Definition 4.3.1: Closed congruence
> A **closed congruence** on a partial algebra $A$ is an equivalence $\theta$ on the **defined elements** that is compatible with each $f^A$ in the strict sense: if $\bar a,\bar b\in\operatorname{dom}(f^A)$ and $a_i\mathbin\theta b_i$ then $f^A(\bar a)\mathbin\theta f^A(\bar b)$, with no requirement when an application is undefined. The quotient $A/\theta$ is a partial algebra whose operations are defined exactly on classes of defined applications.

> [!construction] Construction 4.3.2: Free partial algebra
> The **free total** term algebra $\mathbf T_\Omega(X)$ is also the free *partial* algebra on $X$ in which every operation is total; the free partial algebra subject to a definedness specification is its quotient by the least closed congruence enforcing the prescribed undefinedness. Evaluation $\operatorname{ev}_g:\mathbf T_\Omega(X)\rightharpoonup A$ into a partial algebra is the **partial** homomorphic extension, defined on $t$ iff every operation applied in $t$ stays within the relevant $\operatorname{dom}(f^A)$ under $g$ (strictness).

> [!warning] Warning 4.3.3: Substitution can change definedness
> In a partial algebra, $\operatorname{ev}_g(t)$ may be undefined for some $g$ and defined for others; substitution into a term may turn a defined value undefined or conversely. The clean substitution lemma of the total case (base treatise Theorem 8.3.1) holds only up to **Kleene equality** $\simeq$ and requires strictness bookkeeping: $\operatorname{ev}_w(t\sigma)\simeq\operatorname{ev}_{w\ast\sigma}(t)$ where definedness of either side entails definedness of the other. Treating partial evaluation as if total is the standard error.

> [!example] Example 4.3.4: Stacks as a partial algebra
> Over the stack signature (Example 2.1.3), $\mathsf{top}$ and $\mathsf{pop}$ are partial with $\mathsf{top}^A(\mathsf{empty}^A){\uparrow}$ and $\mathsf{pop}^A(\mathsf{empty}^A){\uparrow}$. The ECE-axioms $\mathrm{def}(\mathsf{top}(\mathsf{push}(e,s)))\Rightarrow\mathsf{top}(\mathsf{push}(e,s))\stackrel{e}{=}e$ and $\mathsf{pop}(\mathsf{push}(e,s))\stackrel{e}{=}s$ specify the intended partial behavior; the initial model is the algebra of finite stacks with $\mathsf{top}/\mathsf{pop}$ undefined exactly on $\mathsf{empty}$.

> [!remark] Remark 4.3.5: Three routes from total to partial
> Partiality can be modeled (i) **directly**, as here, with partial functions and definedness logic; (ii) by **error elements/bottoms**, adjoining $\bot$ to each carrier and making operations total but strict in $\bot$ (the route taken by continuous algebras, §17.3); or (iii) by **order-sorted retracts** (Definition 3.4.1), confining partiality to coercions. The three are interdefinable for many purposes but differ in their natural notion of homomorphism and in whether the resulting algebra is free; ECE-logic is the most expressive and the route with a clean initial-model theorem (Theorem 4.2.2).

---

# Part II — Syntax with Binding

## 5. The Binding Problem

The base treatise establishes (its Warning 10.4.2) that quantifiers $\forall x,\exists x$ — and equally $\lambda$-abstraction, integration $\int\,dx$, summation $\sum_x$, $\mu$-recursion, and set-builder $\{x\mid -\}$ — are **not** finitary operation symbols, because they **bind** a variable: they change the free/bound status of $x$ in their body, so that the "syntax with binders" is not a free $\Omega$-algebra over the variables. This part supplies the theory the base treatise defers. The recurring discipline is the separation of three objects: **raw (pre-)terms**, the relation of **$\alpha$-equivalence**, and the genuine object of interest, the **$\alpha$-equivalence class**, on which capture-avoiding substitution and structural recursion are actually well-defined.

### 5.1. Raw Terms with Binders

> [!definition] Definition 5.1.1: Binding signature
> A **binding signature** is a set $\mathcal O$ of **operators** together with a **binding arity** for each: $o:(k_1,\dots,k_m)$ assigns to $o$ a finite list of natural numbers, where $o$ takes $m$ arguments and **binds $k_i$ variables in its $i$-th argument**. An ordinary $n$-ary operation symbol is the case $(0,\dots,0)$ ($n$ zeros). The paradigmatic non-trivial arities: application $\mathrm{app}:(0,0)$ and abstraction $\mathrm{lam}:(1)$ for the untyped $\lambda$-calculus; $\forall,\exists:(1)$ acting on a formula; $\mu:(1)$ for recursion.

> [!definition] Definition 5.1.2: Raw terms (pre-terms)
> Fix a countably infinite set $\mathbb A$ of **atoms** (variable names). The set $\mathrm{Raw}_{\mathcal O}(\mathbb A)$ of **raw terms** is the least set with $a\in\mathrm{Raw}$ for $a\in\mathbb A$ and, for $o:(k_1,\dots,k_m)$ and raw terms $t_1,\dots,t_m$ together with binder-name lists $\vec a_i\in\mathbb A^{k_i}$,
> $$
> o\big((\vec a_1)t_1,\ \dots,\ (\vec a_m)t_m\big)\in\mathrm{Raw}_{\mathcal O}(\mathbb A),
> $$
> where $(\vec a_i)t_i$ denotes that the names in $\vec a_i$ are **bound** in $t_i$. Raw terms are an ordinary free algebra (the binder-name lists are just extra data); they are *not* the intended syntax.

> [!definition] Definition 5.1.3: Free variables and binding scope
> The **free-variable** map $\mathrm{fv}:\mathrm{Raw}_{\mathcal O}(\mathbb A)\to\mathcal P_{\mathrm{fin}}(\mathbb A)$ is defined by recursion: $\mathrm{fv}(a)=\{a\}$ and
> $$
> \mathrm{fv}\big(o((\vec a_1)t_1,\dots,(\vec a_m)t_m)\big)=\bigcup_{i=1}^m\big(\mathrm{fv}(t_i)\setminus\{\text{names in }\vec a_i\}\big).
> $$
> An occurrence of $a$ in $t_i$ is **bound** by the operator if $a$ appears in $\vec a_i$ and is not re-bound deeper; otherwise **free**. A raw term with $\mathrm{fv}(t)=\varnothing$ is **closed**.

### 5.2. $\alpha$-Equivalence

> [!definition] Definition 5.2.1: $\alpha$-equivalence
> **$\alpha$-equivalence** $=_\alpha$ is the least equivalence relation on $\mathrm{Raw}_{\mathcal O}(\mathbb A)$ that is compatible with all operators and identifies terms differing only by a **consistent renaming of bound names by fresh names**. For a single binder, the generating clause is: if $c$ does not occur free in $t$ and is not captured, then
> $$
> o(\dots,(a)\,t,\dots)\ =_\alpha\ o(\dots,(c)\,t[a{:=}c],\dots),
> $$
> where $t[a{:=}c]$ is the (capture-respecting) renaming of free $a$ to $c$. Equivalently, $=_\alpha$ is generated by the **swapping** presentation of §7.

> [!definition] Definition 5.2.2: The syntax with binding
> The **abstract syntax with binding** generated by $\mathcal O$ over atoms $\mathbb A$ is the quotient set
> $$
> \Lambda_{\mathcal O}(\mathbb A)\ :=\ \mathrm{Raw}_{\mathcal O}(\mathbb A)\big/=_\alpha.
> $$
> Its elements are **terms** (as opposed to raw terms); $\mathrm{fv}$ descends to $\alpha$-classes (it is $\alpha$-invariant), so closedness and free-variable sets are well-defined on terms. This quotient — not the raw term algebra — is the object on which logic and the $\lambda$-calculus operate.

> [!warning] Warning 5.2.3: $\alpha$-equivalence is not a congruence of a free $\Omega$-algebra
> $=_\alpha$ is **not** the kernel of an evaluation into some fixed $\Omega$-algebra over $\mathbb A$, and $\Lambda_{\mathcal O}(\mathbb A)$ is **not** a free $\Omega$-algebra on $\mathbb A$: the binder makes the "constructor" $(a)t\mapsto o((a)t)$ ill-defined on raw terms up to $=_\alpha$ unless one proves $\alpha$-compatibility of the operation, and the would-be generators (atoms) are acted on by name-permutations in a way no free-algebra structure records. This is exactly the obstruction the base treatise flags. The three presentations below (de Bruijn, nominal, presheaf) each *repair* freeness, but each changes the carrier.

> [!warning] Warning 5.2.4: Naive substitution captures
> Define **naive substitution** $t[a{:=}s]$ by blind textual replacement of free $a$ by $s$. It is **not** $\alpha$-invariant and commits **variable capture**: e.g. with $\mathrm{lam}$ written $\lambda a.\,t$, naive $(\lambda b.\,a)[a{:=}b]=\lambda b.\,b$ wrongly captures the substituted $b$. Capture makes the substitution lemma false and the $\beta$-rule unsound. The correct operation is capture-avoiding substitution (Definition 5.3.1), well-defined only on $\alpha$-classes.

### 5.3. Capture-Avoiding Substitution

> [!definition] Definition 5.3.1: Capture-avoiding substitution
> **Capture-avoiding substitution** $t[a{:=}s]$ on $\Lambda_{\mathcal O}(\mathbb A)$ is defined on representatives by: $a[a{:=}s]=s$; $b[a{:=}s]=b$ for $b\ne a$; commutation with non-binding operators; and, for a binder,
> $$
> \big(o(\dots,(b)\,t,\dots)\big)[a{:=}s]\ =\ o\big(\dots,(b')\,(t[b{:=}b'])[a{:=}s],\dots\big),
> $$
> where $b'$ is chosen **fresh** for $a$, $s$, and $t$ (renaming the bound name to avoid capturing $\mathrm{fv}(s)$). The result is independent of the choice of $b'$ up to $=_\alpha$, so $[a{:=}s]$ is well-defined on $\Lambda_{\mathcal O}(\mathbb A)$.

> [!theorem] Theorem 5.3.2: Substitution lemma for binding syntax
> On $\Lambda_{\mathcal O}(\mathbb A)$, for distinct atoms $a\ne b$ with $a\notin\mathrm{fv}(u)$,
> $$
> t[a{:=}s][b{:=}u]\ =\ t[b{:=}u]\,[a{:=}s[b{:=}u]],
> $$
> and renaming, weakening, and the identity $t[a{:=}a]=t$ hold. These laws make $\Lambda_{\mathcal O}(\mathbb A)$ a model of substitution; they hold **only** for capture-avoiding substitution on $\alpha$-classes, and fail for naive substitution on raw terms (Warning 5.2.4).

> [!remark] Remark 5.3.3: What a correct treatment must deliver
> A satisfactory account of binding must provide, on the genuine object $\Lambda_{\mathcal O}(\mathbb A)$: (i) well-defined **constructors** including the binder; (ii) a structural **induction/recursion** principle; (iii) capture-avoiding **substitution** with the substitution lemma; and (iv) ideally, a **freeness/initiality** statement recovering the universal-property style of the base treatise. The naive raw-term quotient supplies none of (i)–(iv) directly. §§6–8 supply all four by three different means.

---

## 6. De Bruijn Presentation

The de Bruijn presentation eliminates bound names entirely, replacing each bound occurrence by a **numeric index** counting the binders between the occurrence and its binder. Two raw terms are $\alpha$-equivalent iff they have **equal** de Bruijn encodings, so the quotient by $=_\alpha$ becomes ordinary equality on nameless terms — at the cost of arithmetic on indices in the substitution operation.

### 6.1. Nameless Terms

> [!definition] Definition 6.1.1: De Bruijn terms
> Fix a binding signature $\mathcal O$. The set $\mathrm{DB}_{\mathcal O}$ of **de Bruijn terms** is the least set with $\underline n\in\mathrm{DB}_{\mathcal O}$ for every **index** $n\in\mathbb N$ and, for $o:(k_1,\dots,k_m)$ and $u_1,\dots,u_m\in\mathrm{DB}_{\mathcal O}$,
> $$
> o(u_1,\dots,u_m)\in\mathrm{DB}_{\mathcal O},
> $$
> where the $i$-th argument is understood to be **under $k_i$ additional binders**. An index $\underline n$ refers to the variable bound by the $n$-th enclosing binder (counting from $0$); an index too large to be bound is **free** and denotes a free variable position.

> [!definition] Definition 6.1.2: Shifting (lifting)
> The **shift** $\uparrow^d_c:\mathrm{DB}_{\mathcal O}\to\mathrm{DB}_{\mathcal O}$ with **cutoff** $c$ and **amount** $d$ adds $d$ to every free index $\ge c$, recursing under binders by raising the cutoff:
> $$
> \uparrow^d_c(\underline n)=\begin{cases}\underline n & n<c\\ \underline{n+d} & n\ge c\end{cases},\qquad \uparrow^d_c\big(o(\dots,u_i,\dots)\big)=o\big(\dots,\uparrow^d_{\,c+k_i}(u_i),\dots\big).
> $$
> Shifting adjusts indices when a term is moved under additional binders, preventing accidental capture or release.

### 6.2. De Bruijn Substitution

> [!definition] Definition 6.2.1: Index substitution
> The substitution of de Bruijn term $s$ for index $j$ in $u$, written $u\{j\mapsto s\}$, is
> $$
> \underline n\{j\mapsto s\}=\begin{cases}\underline n & n<j\\ s & n=j\\ \underline{n-1} & n>j\end{cases},\qquad o(\dots,u_i,\dots)\{j\mapsto s\}=o\big(\dots,u_i\{\,j+k_i\mapsto\ \uparrow^{k_i}_{0}s\,\},\dots\big),
> $$
> with the replacement term shifted by the number of binders crossed. The $\beta$-redex contraction for the $\lambda$-calculus is $\mathrm{app}(\mathrm{lam}(u),s)\to u\{0\mapsto s\}$ with the outer indices renumbered by the $n>j$ clause.

> [!theorem] Theorem 6.2.2: Adequacy of the de Bruijn encoding
> Fix an enumeration of $\mathbb A$. The encoding $\llbracket-\rrbracket:\mathrm{Raw}_{\mathcal O}(\mathbb A)\to\mathrm{DB}_{\mathcal O}$ that replaces each bound occurrence by its binder distance and each free atom by a fixed index satisfies
> $$
> s\ =_\alpha\ t\quad\Longleftrightarrow\quad \llbracket s\rrbracket=\llbracket t\rrbracket,
> $$
> and induces a bijection $\Lambda_{\mathcal O}(\mathbb A)\cong\mathrm{DB}_{\mathcal O}$ (for closed terms; in general onto the de Bruijn terms whose free indices respect the chosen free-variable enumeration). Capture-avoiding substitution corresponds to index substitution (Definition 6.2.1) under this bijection.

> [!warning] Warning 6.2.3: Indices trade name-bookkeeping for arithmetic-bookkeeping
> The de Bruijn presentation makes $\alpha$-equivalence into syntactic equality but moves the entire difficulty into **shift/cutoff arithmetic**: every substitution and every move under a binder must renumber indices, and an off-by-one error silently changes scope. The presentation is canonical and machine-friendly but loses readability and is a frequent source of formalization bugs. It does not, by itself, restore a *named* induction principle.

### 6.3. Terms-in-Context and the Presheaf View

> [!definition] Definition 6.3.1: The category of contexts
> Let $\mathbb F$ be the category whose objects are natural numbers $n$ (read as a context of $n$ free de Bruijn variables $\underline 0,\dots,\underline{n-1}$) and whose morphisms $n\to n'$ are **functions** $\{0,\dots,n-1\}\to\{0,\dots,n'-1\}$ (variable renamings/reindexings); the subcategory $\mathbb I$ uses only **injections**. A **presheaf** $P:\mathbb F^{\mathrm{op}}\to\mathbf{Set}$ (or $P:\mathbb I^{\mathrm{op}}\to\mathbf{Set}$) is a family $(P(n))_n$ of "terms with at most $n$ free variables" with functorial reindexing.

> [!construction] Construction 6.3.2: The de Bruijn term presheaf
> Define $\mathbf{Db}_{\mathcal O}:\mathbb F^{\mathrm{op}}\to\mathbf{Set}$ by $\mathbf{Db}_{\mathcal O}(n)=\{u\in\mathrm{DB}_{\mathcal O}:\text{all free indices of }u\text{ are }<n\}$, with reindexing along $\rho:n\to n'$ acting on free indices. The **variable** presheaf is $V$ with $V(n)=\{0,\dots,n-1\}$. Each operator $o:(k_1,\dots,k_m)$ becomes a natural transformation using the **context-extension** functor $(-)+k_i$, and $\mathbf{Db}_{\mathcal O}$ is the initial algebra of the resulting endofunctor on $\mathbf{Set}^{\mathbb F^{\mathrm{op}}}$ (developed abstractly in §8).

> [!remark] Remark 6.3.3: Why a presheaf and not a set
> Binding is intrinsically **context-dependent**: whether $\underline 2$ is bound or free depends on how many binders enclose it. Indexing terms by their context $n$ records exactly this dependence, and reindexing (a functorial action) is exactly variable renaming/weakening. The move from $\mathbf{Set}$ to the presheaf category $\mathbf{Set}^{\mathbb F^{\mathrm{op}}}$ is the categorical content of "syntax with binding is not an ordinary algebra": the carrier is a *functor*, and substitution is *monoid structure* on that functor (§8.3).

---

## 7. Nominal Sets

The nominal approach (Gabbay–Pitts) keeps names explicit but makes the *symmetry group of name permutations* a first-class structural ingredient. Its central technical notion is **finite support**, which underwrites a canonical notion of **freshness** and a binder ("atom abstraction") for which $\alpha$-equivalence becomes literal equality, all while retaining a **named** structural recursion principle absent from the de Bruijn presentation.

### 7.1. Permutation Actions, Support, Freshness

> [!definition] Definition 7.1.1: The permutation group and $G$-sets
> Fix a countably infinite set $\mathbb A$ of **atoms**. Let $\mathbb S=\mathrm{Sym}_{\mathrm{fin}}(\mathbb A)$ be the group of **finite permutations** of $\mathbb A$ (bijections moving only finitely many atoms), generated by the **transpositions (swaps)** $(a\ b)$. An **$\mathbb S$-set** is a set $Z$ with a group action $\mathbb S\times Z\to Z$, $(\pi,z)\mapsto\pi\cdot z$.

> [!definition] Definition 7.1.2: Support and finite support
> For an $\mathbb S$-set $Z$ and $z\in Z$, a set $A\subseteq\mathbb A$ **supports** $z$ if every $\pi$ fixing $A$ pointwise satisfies $\pi\cdot z=z$. $z$ is **finitely supported** if some finite $A$ supports it; then there is a **least** finite support $\operatorname{supp}(z)$. A **nominal set** is an $\mathbb S$-set in which every element is finitely supported.

> [!definition] Definition 7.1.3: Freshness
> For $a\in\mathbb A$ and $z$ in a nominal set, $a$ is **fresh for** $z$, written $a\mathbin\#z$, iff $a\notin\operatorname{supp}(z)$. Freshness abstracts "$a$ does not occur free in $z$": it is the support-theoretic, representation-independent form of non-occurrence. For a tuple, $a\#(z_1,\dots,z_k)$ iff $a\#z_i$ for all $i$.

> [!definition] Definition 7.1.4: Equivariance and the freshness quantifier
> A map $f:Z\to W$ of nominal sets is **equivariant** if $f(\pi\cdot z)=\pi\cdot f(z)$ for all $\pi,z$; equivariant maps preserve support ($\operatorname{supp}(f(z))\subseteq\operatorname{supp}(z)$). The **freshness quantifier** "$\mathsf{N}a.\,\Phi(a)$" ("**for some/any fresh $a$**") asserts that $\Phi(a)$ holds for all but finitely many $a\in\mathbb A$; on finitely supported predicates "for some fresh $a$" and "for all fresh $a$" coincide, which is the defining property of $\mathsf{N}$.

### 7.2. Atom Abstraction and the Nominal Binder

> [!construction] Construction 7.2.1: Atom-abstraction
> For a nominal set $Z$, the **atom-abstraction** $[\mathbb A]Z$ has underlying set the quotient of $\mathbb A\times Z$ by
> $$
> (a,z)\sim(b,w)\quad\Longleftrightarrow\quad \big(a=b\wedge z=w\big)\ \text{ or }\ \big(a\#w\ \wedge\ (a\ b)\cdot w=z\big),
> $$
> with class of $(a,z)$ written $\langle a\rangle z$ and the swap action $\pi\cdot\langle a\rangle z=\langle\pi a\rangle(\pi\cdot z)$. $[\mathbb A]Z$ is a nominal set with $\operatorname{supp}(\langle a\rangle z)=\operatorname{supp}(z)\setminus\{a\}$. The class $\langle a\rangle z$ is the **abstraction of $a$ in $z$** and models the binder "$(a)z$" with $\alpha$-equivalence built in.

> [!theorem] Theorem 7.2.2: Abstraction realizes $\alpha$-equivalence as equality
> The construction $[\mathbb A](-)$ is functorial on nominal sets, and for the syntax of a binding signature it satisfies the defining binder law
> $$
> \langle a\rangle z=\langle b\rangle w\quad\Longleftrightarrow\quad \big(a=b\wedge z=w\big)\vee\big(a\#w\wedge z=(a\ b)\cdot w\big),
> $$
> which is exactly $\alpha$-equivalence of single binders. Hence in the nominal term algebra (Construction 7.3.1) $\alpha$-equivalent terms are **equal**, with no encoding and no index arithmetic.

### 7.3. The Nominal Term Algebra and Recursion

> [!construction] Construction 7.3.1: Nominal term algebra
> Given a binding signature $\mathcal O$, the **nominal abstract syntax** $\Lambda^{\mathrm{nom}}_{\mathcal O}$ is the initial algebra, in the category $\mathbf{Nom}$ of nominal sets, of the functor
> $$
> T(Z)\ =\ \mathbb A\ +\ \coprod_{o:(k_1,\dots,k_m)}\ \prod_{i=1}^m [\mathbb A]^{k_i}Z,
> $$
> where $\mathbb A$ is the nominal set of atoms (with $\operatorname{supp}(a)=\{a\}$) and $[\mathbb A]^{k}$ iterates abstraction $k$ times. Its elements are exactly the $\alpha$-equivalence classes of raw terms (Definition 5.2.2): $\Lambda^{\mathrm{nom}}_{\mathcal O}\cong\Lambda_{\mathcal O}(\mathbb A)$ as sets, now with explicit permutation action and finite support $=\mathrm{fv}$.

> [!theorem] Theorem 7.3.2: Nominal structural recursion (Pitts)
> Let $Z$ be a nominal set equipped with: an equivariant **variable map** $f_{\mathrm{var}}:\mathbb A\to Z$; and for each operator $o:(k_1,\dots,k_m)$ an equivariant **operator map** $f_o$ defined on tuples of (abstractions of) elements of $Z$, satisfying the **freshness condition for binders (FCB)**: the bound atoms are fresh for the result of $f_o$. Then there is a **unique** equivariant homomorphism $h:\Lambda^{\mathrm{nom}}_{\mathcal O}\to Z$ respecting all constructors, defined by recursion **using bound names directly** (choosing them fresh). The FCB is exactly the side condition making the binder clause well-defined on $\alpha$-classes.

> [!warning] Warning 7.3.3: The freshness condition for binders is mandatory
> Nominal recursion is **not** unconditional. Without the FCB, a recursive clause that inspects a bound name may fail to be $\alpha$-invariant — the same failure as naive substitution (Warning 5.2.4) — and no well-defined $h$ exists. The FCB ("the binder's atom is fresh for the output") is the nominal counterpart of the de Bruijn shift discipline and of the substitution lemma's freshness side conditions. Recursion principles that omit it are unsound on binding syntax.

> [!example] Example 7.3.4: Capture-avoiding substitution by nominal recursion
> Capture-avoiding substitution $-[a{:=}s]$ is defined by nominal recursion: on atoms as in Definition 5.3.1; on operators by the operator maps; and on the binder clause, choosing the bound name fresh for $a$ and $s$ (which is exactly the FCB). The substitution lemma (Theorem 5.3.2) and equivariance $\pi\cdot(t[a{:=}s])=(\pi\cdot t)[\pi a{:=}\pi\cdot s]$ follow from uniqueness of the recursively defined map.

> [!remark] Remark 7.3.5: Nominal logic and the new-quantifier
> The freshness quantifier $\mathsf{N}$ (Definition 7.1.4) is self-dual on finitely supported predicates and supports a first-order **nominal logic** in which "$\mathsf{N}a.\,\Phi$" formalizes the ubiquitous informal phrase "choose a fresh name." The Gabbay–Pitts framework thereby internalizes the freshness side conditions that, in the named presentation, must be discharged by hand at every binder.

---

## 8. Binding Signatures and Second-Order Abstract Syntax

The de Bruijn presheaf (§6.3) and the nominal initial algebra (§7.3) are two models of one abstract structure: **abstract syntax with variable binding** as initial algebra of a binding-signature functor on a category of "objects varying over contexts," equipped with a **substitution monoid** structure. This is the Fiore–Plotkin–Turi account, the binding analogue of the base treatise's polynomial-functor and term-monad picture.

### 8.1. The Substitution Tensor and Monoids

> [!definition] Definition 8.1.1: Context category and presheaf category
> Let $\mathbb F$ be the category of finite cardinals and all functions (Definition 6.3.1); the presheaf category is $\widehat{\mathbb F}:=\mathbf{Set}^{\mathbb F}$ (covariant) or $\mathbf{Set}^{\mathbb F^{\mathrm{op}}}$ depending on convention. The **presheaf of variables** is $V\in\widehat{\mathbb F}$ with $V(n)=\{0,\dots,n-1\}$ (the representable on $1$). Objects of $\widehat{\mathbb F}$ are "families indexed by contexts" with functorial renaming.

> [!definition] Definition 8.1.2: Substitution tensor product
> The **substitution tensor** $\otimes$ on $\widehat{\mathbb F}$ is
> $$
> (P\otimes Q)(n)\ :=\ \int^{m\in\mathbb F} P(m)\times Q(n)^{m},
> $$
> a coend identifying "a $P$-term in $m$ variables together with an assignment of a $Q$-term (in context $n$) to each of those $m$ variables." The variable presheaf $V$ is the **unit**: $P\otimes V\cong P\cong V\otimes P$. $\otimes$ is (non-symmetric) monoidal and models simultaneous substitution.

> [!definition] Definition 8.1.3: Monoid = object with substitution
> A **monoid** $(P,\nu:V\to P,\varsigma:P\otimes P\to P)$ in $(\widehat{\mathbb F},\otimes,V)$ is an object $P$ ("terms") with a **variable-inclusion** $\nu$ (the unit, "a variable is a term") and a **substitution** $\varsigma$ (the multiplication) satisfying associativity and unit laws. This is exactly an internal model of substitution: $\varsigma$ takes a term over $m$ variables and an $m$-tuple of terms and returns the simultaneous substitution. The base treatise's term monad on $\mathbf{Set}$ is the binder-free special case.

### 8.2. Binding-Signature Functors and Initiality

> [!definition] Definition 8.2.1: The binding-signature endofunctor
> For a binding signature $\mathcal O$, define $\Sigma_{\mathcal O}:\widehat{\mathbb F}\to\widehat{\mathbb F}$ by
> $$
> \Sigma_{\mathcal O}(P)\ :=\ \coprod_{o:(k_1,\dots,k_m)}\ \prod_{i=1}^m \delta^{k_i}P,\qquad (\delta P)(n):=P(n+1),
> $$
> where the **context-extension (derivative)** functor $\delta$ shifts the context by one fresh variable, modeling "argument under one more binder." A **$(\Sigma_{\mathcal O}+V)$-algebra** is an object with operator structure and a variable inclusion.

> [!theorem] Theorem 8.2.2: Initial-algebra abstract syntax (Fiore–Plotkin–Turi)
> The endofunctor $V+\Sigma_{\mathcal O}$ on $\widehat{\mathbb F}$ has an **initial algebra** $\mathbf{Syn}_{\mathcal O}$, the **abstract syntax with binding** of $\mathcal O$. It carries a canonical monoid structure (Definition 8.1.3): the unit is variable inclusion and the multiplication is **capture-avoiding simultaneous substitution**, which is the unique monoid structure compatible with the operators. The de Bruijn presheaf (Construction 6.3.2) and the nominal initial algebra (Construction 7.3.1) are two presentations of $\mathbf{Syn}_{\mathcal O}$.

> [!theorem] Theorem 8.2.3: Initiality is structural recursion with binding
> For any $(V+\Sigma_{\mathcal O})$-algebra $A$ in $\widehat{\mathbb F}$ there is a unique algebra homomorphism $\mathbf{Syn}_{\mathcal O}\to A$. This is the **structural recursion principle** for binding syntax: specifying an action on variables and on each operator (in extended contexts) determines a unique context-respecting map out of the syntax. Compatibility with substitution (a **strength**/monoid-morphism condition) is the categorical form of the freshness condition for binders (Warning 7.3.3).

### 8.3. Second-Order Syntax, Equations, and HOAS

> [!definition] Definition 8.3.1: Second-order equational logic
> A **second-order equation** is an equation between terms-in-context with **metavariables** that may themselves take arguments (representing terms with holes for bound variables). The associated deduction system extends Birkhoff's calculus with rules for substitution under binders. Models are monoids in $\widehat{\mathbb F}$ satisfying the equations; the free such model on a set of metavariables is the quotient of $\mathbf{Syn}_{\mathcal O}$ by the least **substitution-and-binding-invariant** congruence generated by the equations. The $\beta$- and $\eta$-laws of the $\lambda$-calculus are the canonical example.

> [!definition] Definition 8.3.2: Higher-order abstract syntax (HOAS)
> **HOAS** represents object-level binders by meta-level functions: e.g. $\mathrm{lam}:(\mathrm{tm}\to\mathrm{tm})\to\mathrm{tm}$, so an object binder becomes a meta-level function space. This makes object-level substitution into meta-level application and reuses the meta-language's $\alpha$-renaming. The presheaf/initial-algebra account (Theorem 8.2.2) is the mathematically controlled form of this idea, with $\delta$ playing the role of the function space $\mathrm{tm}\to(-)$ restricted to **parametric** (natural) dependence.

> [!warning] Warning 8.3.3: Exotic terms and negative occurrences
> Naive HOAS using the **full** meta-level function space $\mathrm{tm}\to\mathrm{tm}$ is ill-behaved: (i) the binder argument occurs **negatively**, so the would-be datatype is not a legitimate initial algebra (no inductive definition, no recursion principle); and (ii) the function space contains **exotic terms** — functions performing case analysis on their argument — that correspond to no object-language term. The repair is to restrict to a presheaf/parametric function space ($\delta$, naturality) as in §8.1–8.2, which excludes exotic terms and restores initiality. Treating object binders as arbitrary meta-functions is unsound for structural recursion.

> [!remark] Remark 8.3.4: The four presentations compared
> The same object $\mathbf{Syn}_{\mathcal O}$ admits four standard presentations: **named** raw terms modulo $=_\alpha$ (readable, but constructors and recursion need $\alpha$-compatibility proofs); **de Bruijn** indices (canonical, machine-friendly, index arithmetic, no named recursion); **nominal** sets (named recursion with the FCB, explicit permutation action, finite support $=\mathrm{fv}$); and **presheaf/initial-algebra** (uniform universal property, substitution as monoid multiplication, the binding analogue of the base treatise's term monad). They are equivalent as presentations of one initial algebra, differing exactly as the base treatise's tree/tuple/string presentations of $\mathbf T_\Omega(X)$ differ — canonically isomorphic, not literally equal, with presentation-dependent costs and recursion principles. The comparison table appears in §21.2.

---

# Part III — Algebraic Logic

## 9. From Lindenbaum–Tarski to Algebraic Logic

The base treatise shows that **propositional** logic is the equational theory of the variety of Boolean algebras: the Lindenbaum–Tarski algebra $\mathbf{Form}/{\equiv}$ is the free Boolean algebra on the propositional variables, tautologies are the top class, and tautological consequence is the order of the algebra. It then halts at first-order logic, where quantifiers resist this treatment (its Theorem 10.5.2). **Algebraic logic** is the program that recovers an equational-algebraic description of quantified logics; this part develops its first-order core.

### 9.1. The Lindenbaum–Tarski Construction Abstractly

> [!definition] Definition 9.1.1: Lindenbaum–Tarski algebra of a logic
> For a logic $\mathcal L$ with formula set $\mathrm{Fm}$ and a consequence/provability relation determining an equivalence "interprovability" $\dashv\vdash$, the **Lindenbaum–Tarski algebra** is $\mathrm{Fm}/{\dashv\vdash}$, equipped with operations induced by the connectives (well-defined iff $\dashv\vdash$ is a congruence for them). For classical propositional logic this is a Boolean algebra; for intuitionistic, a Heyting algebra; for modal $\mathbf K$, a modal (Boolean-with-operator) algebra.

> [!definition] Definition 9.1.2: Algebraizable logic (schematic)
> A logic is **algebraizable** (Blok–Pigozzi) when there are translations $\tau$ (formulas to equations) and $\rho$ (equations to formulas) and an equivalent quasivariety $\mathsf K$ such that provability $\vdash_{\mathcal L}$ corresponds to equational consequence $\models_{\mathsf K}$ and the two translations are mutually inverse modulo the respective consequence relations. Classical propositional logic is algebraizable with $\mathsf K=$ Boolean algebras and $\tau(\varphi)=(\varphi\approx\top)$; the algebraic counterpart is then governed entirely by §19's variety theory.

> [!remark] Remark 9.1.3: What breaks for first-order logic
> First-order logic is **not** algebraizable as a propositional logic, for two compounding reasons: (i) **variables and quantifiers** — formulas live in contexts and quantifiers bind, so the formula "algebra" is binding syntax (Part II), not a free $\Omega$-algebra; and (ii) **substitution and equality interact with quantification** in ways no Boolean operation captures. The resolution is to add algebraic operators modeling quantification and variable-management directly: **cylindrifications** (cylindric algebras, §10) or **quantifier-plus-substitution operators** (polyadic algebras, §11). Both restore an equational presentation, at the price of an operation **for each variable**, hence infinite-dimensional signatures.

### 9.2. The Need for Dimension

> [!definition] Definition 9.2.1: Dimension
> The **dimension** of an algebraic-logic structure is an ordinal $\alpha$ indexing the variables $\{v_i:i<\alpha\}$ of the logic; the signature contains one cylindrification (or quantifier) operator and a family of diagonal/substitution operators **per index** (or per pair of indices). First-order logic over a countable variable supply has dimension $\omega$. Finite dimension $\alpha=n$ corresponds to $n$-variable fragments.

> [!warning] Warning 9.2.2: Quantifiers cost an operation per variable
> There is no finite-signature equational algebraization of full first-order logic: the cylindric/polyadic signatures are **infinite** (one cylindrification $\mathsf c_i$ per variable $v_i$), and even then the equationally **axiomatized** class (cylindric algebras, $\mathsf{CA}_\alpha$) is strictly larger than the class of set-theoretically **representable** ones ($\mathsf{RCA}_\alpha$) for $\alpha\ge 2$ (Theorem 10.3.3). This irreducible gap — and the non-finite-axiomatizability of $\mathsf{RCA}_\alpha$ — is the precise algebraic shadow of the base treatise's Theorem 10.5.2.

---

## 10. Cylindric Algebras

Cylindric algebras (Tarski) model first-order logic with equality by augmenting a Boolean algebra with a **cylindrification** $\mathsf c_i$ for each variable index (the algebraic counterpart of $\exists v_i$) and **diagonal** constants $\mathsf d_{ij}$ (the counterpart of the equality atom $v_i\doteq v_j$).

### 10.1. The Cylindric Axioms

> [!definition] Definition 10.1.1: Cylindric algebra
> Fix an ordinal $\alpha$ (the dimension). A **cylindric algebra of dimension $\alpha$** is a structure
> $$
> \mathfrak A=\big(A,\ +,\ \cdot,\ -,\ 0,\ 1,\ (\mathsf c_i)_{i<\alpha},\ (\mathsf d_{ij})_{i,j<\alpha}\big)
> $$
> where $(A,+,\cdot,-,0,1)$ is a Boolean algebra, each **cylindrification** $\mathsf c_i:A\to A$ is a unary operator, and each **diagonal** $\mathsf d_{ij}\in A$ is a constant, satisfying for all $i,j,k<\alpha$:
> $$
> \textbf{(C1)}\ \mathsf c_i 0=0;\qquad \textbf{(C2)}\ x\le \mathsf c_i x;\qquad \textbf{(C3)}\ \mathsf c_i(x\cdot \mathsf c_i y)=\mathsf c_i x\cdot \mathsf c_i y;
> $$
> $$
> \textbf{(C4)}\ \mathsf c_i\mathsf c_j x=\mathsf c_j\mathsf c_i x;\qquad \textbf{(C5)}\ \mathsf d_{ii}=1;
> $$
> $$
> \textbf{(C6)}\ i\notin\{j,k\}\ \Rightarrow\ \mathsf d_{jk}=\mathsf c_i(\mathsf d_{ji}\cdot \mathsf d_{ik});\qquad \textbf{(C7)}\ i\ne j\ \Rightarrow\ \mathsf c_i(\mathsf d_{ij}\cdot x)\cdot \mathsf c_i(\mathsf d_{ij}\cdot -x)=0.
> $$
> The class of all such is $\mathsf{CA}_\alpha$, a **variety** (defined by the above equations).

> [!remark] Remark 10.1.2: Reading the axioms logically
> Under "$\mathsf c_i\leftrightarrow\exists v_i$", "$\mathsf d_{ij}\leftrightarrow (v_i\doteq v_j)$": (C1) $\exists v_i\bot\equiv\bot$; (C2) $\varphi\to\exists v_i\varphi$; (C3) the distribution $\exists v_i(\varphi\wedge\exists v_i\psi)\equiv\exists v_i\varphi\wedge\exists v_i\psi$; (C4) commuting quantifiers $\exists v_i\exists v_j\equiv\exists v_j\exists v_i$; (C5)–(C7) the laws of equality and its interaction with quantifiers (reflexivity, substitution, and the functionality of equality). $\mathsf{CA}_\alpha$ is the **equational** theory generated by these readings.

### 10.2. Set Cylindric Algebras and Representation

> [!construction] Construction 10.2.1: Cylindric set algebra
> Let $U$ be a set and $\alpha$ an ordinal; consider subsets of $U^\alpha$ ($\alpha$-ary relations). The **cylindric set algebra** on $U$ has carrier a Boolean subalgebra of $\mathcal P(U^\alpha)$ closed under the operations
> $$
> \mathsf c_i R=\{s\in U^\alpha:\exists u\in U,\ s(i{:=}u)\in R\}\quad(\text{cylindrification along axis }i),
> $$
> $$
> \mathsf d_{ij}=\{s\in U^\alpha:s_i=s_j\}\quad(\text{diagonal}),
> $$
> where $s(i{:=}u)$ is $s$ with the $i$-th coordinate reset to $u$. Geometrically $\mathsf c_iR$ is the **cylinder** generated by $R$ along the $i$-th axis — the source of the name.

> [!definition] Definition 10.2.2: Representable cylindric algebras
> A cylindric algebra is **representable** if it embeds into a product of cylindric set algebras; $\mathsf{RCA}_\alpha$ is the class of representable algebras of dimension $\alpha$. $\mathsf{RCA}_\alpha$ is exactly the class arising from genuine $\alpha$-ary relations, i.e. the algebras that "are" Boolean algebras of definable relations on structures.

> [!theorem] Theorem 10.2.3: The representation gap (Monk, Tarski)
> For $\alpha\ge 2$:
> $$
> \mathsf{RCA}_\alpha\ \subsetneq\ \mathsf{CA}_\alpha,
> $$
> i.e. there exist cylindric algebras satisfying all finitely many schematic axioms (C1)–(C7) that are **not** representable. Moreover $\mathsf{RCA}_\alpha$ is a variety (closed under $H,S,P$) but is **not finitely axiomatizable** for $2\le\alpha$, and for $3\le\alpha<\omega$ not axiomatizable by any set of equations using finitely many variables. The abstract equational theory $\mathsf{CA}_\alpha$ provably undershoots the intended semantics, and no finite repair exists.

### 10.3. The Lindenbaum Cylindric Algebra of First-Order Logic

> [!construction] Construction 10.3.1: Cylindric algebra of a first-order theory
> For a first-order theory $\Theta$ in a language with variables $\{v_i:i<\omega\}$, define the **Lindenbaum–Tarski cylindric algebra** $\mathfrak{Lt}(\Theta)$: carrier the formulas modulo $\Theta$-provable equivalence, Boolean operations from the connectives, $\mathsf c_i=[\exists v_i\,(-)]$, $\mathsf d_{ij}=[v_i\doteq v_j]$. The axioms (C1)–(C7) hold because they are provable schemata of first-order logic with equality; $\mathfrak{Lt}(\Theta)\in\mathsf{CA}_\omega$.

> [!theorem] Theorem 10.3.2: Locally finite-dimensional algebras correspond to first-order theories
> An element $x$ of a $\mathsf{CA}_\omega$ has **dimension set** $\Delta x=\{i:\mathsf c_i x\ne x\}$ (the indices that "matter"); the algebra is **locally finite-dimensional** ($\mathsf{Lf}_\omega$) if every element has finite dimension set (the algebraic form of "each formula has finitely many free variables"). The Lindenbaum algebras $\mathfrak{Lt}(\Theta)$ are exactly (up to isomorphism) the locally finite-dimensional, **representable** cylindric algebras of dimension $\omega$ with countably many generators; this is the precise sense in which first-order logic **is** an equational theory of cylindric algebras.

> [!remark] Remark 10.3.3: What algebraization buys and costs
> Cylindric algebra makes quantifiers and equality into ordinary algebraic operations, bringing the full machinery of §19 (varieties, congruences, free algebras, HSP) to bear on first-order logic, and converting Gödel's completeness theorem into a representation theorem ($\mathfrak{Lt}(\Theta)$ is representable). The cost is exactly Warning 9.2.2: an infinite signature, a non-finitely-axiomatizable representable class, and the strict gap $\mathsf{RCA}_\alpha\subsetneq\mathsf{CA}_\alpha$. The base treatise's "logic exceeds equational algebra" becomes the precise statement that the *representable* class is not equationally finitely capturable.

---

## 11. Polyadic and Quantifier Algebras

Halmos's **polyadic algebras** algebraize first-order logic (originally without equality) using, in place of per-axis cylindrifications and diagonals, a single existential-quantifier operator parameterized by **sets of variables** together with operators for **substitutions** (transformations of the variable indices).

### 11.1. Polyadic Algebras

> [!definition] Definition 11.1.1: Polyadic algebra
> Fix a set $I$ of variables. A **polyadic algebra** of degree $I$ is a Boolean algebra $A$ equipped with:
> $$
> \textbf{quantifiers}\quad \exists(J):A\to A\ \ (J\subseteq I),\qquad \textbf{substitutions}\quad \mathsf S(\sigma):A\to A\ \ (\sigma:I\to I),
> $$
> such that $\exists(\varnothing)=\mathrm{id}$, $\exists(J)$ is an additive closure operator with $\exists(J\cup K)=\exists(J)\exists(K)$, each $\mathsf S(\sigma)$ is a Boolean endomorphism, $\mathsf S$ is functorial ($\mathsf S(\sigma\tau)=\mathsf S(\sigma)\mathsf S(\tau)$, $\mathsf S(\mathrm{id})=\mathrm{id}$), and the **quantifier–substitution commutation laws** hold (substitutions that agree off $J$ commute appropriately with $\exists(J)$). With an added family of **equality** elements one obtains **polyadic equality algebras**.

> [!remark] Remark 11.1.2: Reading the operators
> $\exists(J)$ algebraizes simultaneous quantification over all variables in $J$; $\mathsf S(\sigma)$ algebraizes the renaming/substitution of variables by $\sigma$. Packaging substitution as a first-class operator (rather than deriving it, as in cylindric algebra) makes polyadic algebra the more **functorial** formulation: the substitutions form a representation of the monoid $I^I$ of transformations on the Boolean algebra.

### 11.2. Comparison and Upshot

> [!theorem] Theorem 11.2.1: Equivalence of the formalisms
> For infinite degree, polyadic equality algebras and cylindric algebras are intertranslatable: cylindrifications are recovered as $\exists(\{i\})$, diagonals from the equality elements, and substitutions $\mathsf S(\sigma)$ are definable in cylindric algebras for finitely-supported $\sigma$ via compositions of cylindrifications and diagonals. The representable subclasses correspond, so both formalisms algebraize first-order logic with equality, differing in primitive choice (per-axis vs transformation-indexed).

> [!warning] Warning 11.2.2: Substitution operators do not eliminate the infinity
> Replacing per-axis operators by transformation-indexed operators repackages but does not remove the essential infinity (Warning 9.2.2): the substitution operators are indexed by the infinite transformation monoid $I^I$, and the representable polyadic algebras are likewise not finitely axiomatizable. No reformulation makes full first-order logic the equational theory of a **finitely presented** variety; algebraic logic explains *why* by exhibiting the obstruction as a representation/axiomatizability gap rather than a defect of presentation.

> [!remark] Remark 11.2.3: Place in the companion's architecture
> Parts II and III treat the same deferral — "logic exceeds bare universal algebra" — from two angles. Part II keeps logic as **syntax with binding** and supplies the correct term/recursion/substitution theory (de Bruijn, nominal, presheaf). Part III instead **re-algebraizes** the semantics, trading binding syntax for an infinite-dimensional but genuinely equational (variety-theoretic) structure. The two are complementary: binding syntax is the proof-theoretic/term-level repair; cylindric/polyadic algebra is the model-theoretic/semantic repair. Both confirm the base treatise's diagnosis with a precise theorem (non-initiality of binding syntax as an $\Omega$-algebra; non-finite-axiomatizability of $\mathsf{RCA}_\alpha$).

---

# Part IV — Effective Equational Reasoning: Unification and Rewriting

## 12. Unification

The base treatise develops substitution and the word problem but not the **inverse** question: given two terms, find a substitution making them equal. This is **unification**, the engine of automated deduction, type inference, logic programming, and the critical-pair test of §13. The basic theory is the existence and computation of **most general unifiers** in the free term algebra; the advanced theory is unification **modulo** an equational theory.

### 12.1. The Unification Problem

> [!definition] Definition 12.1.1: Unification problem and unifier
> Fix $\Omega$ and a variable set $X$. A **unification problem** is a finite set of **equations** $\{s_1\stackrel{?}{=}t_1,\dots,s_k\stackrel{?}{=}t_k\}$ with $s_i,t_i\in T_\Omega(X)$. A substitution $\sigma:X\to T_\Omega(X)$ is a **unifier** (solution) if $s_i\sigma=t_i\sigma$ (syntactic equality in $\mathbf T_\Omega(X)$) for all $i$. The problem is **unifiable** if a unifier exists. A unifier of the single equation $s\stackrel{?}{=}t$ is a substitution making $s,t$ identical.

> [!definition] Definition 12.1.2: Subsumption preorder on substitutions
> For substitutions $\sigma,\tau$, $\sigma$ is **more general than** $\tau$ (on a variable set $W$), written $\sigma\lesssim_W\tau$, iff there is $\rho$ with $\tau=_W(\sigma;\rho)$ (i.e. $x\tau=(x\sigma)\rho$ for $x\in W$). This is a **preorder**; its symmetric part is **equivalence up to renaming**: $\sigma\equiv\tau$ iff each is more general than the other, which holds iff they differ by a bijective variable renaming.

> [!definition] Definition 12.1.3: Idempotent substitution
> $\sigma$ is **idempotent** if $\sigma;\sigma=\sigma$, equivalently if $\operatorname{dom}(\sigma)$ is disjoint from the range variables of $\sigma$ (no introduced variable is itself replaced). Idempotent unifiers are the canonical representatives: every unifiable problem has an idempotent most general unifier.

### 12.2. Most General Unifiers

> [!definition] Definition 12.2.1: Most general unifier
> A unifier $\sigma$ of a problem $\mathcal P$ is a **most general unifier (mgu)** if $\sigma\lesssim\tau$ for every unifier $\tau$ of $\mathcal P$. By Definition 12.1.2 an mgu is unique up to renaming.

> [!theorem] Theorem 12.2.2: Unification theorem (Robinson)
> In the free term algebra $\mathbf T_\Omega(X)$ over a finitary signature:
> $$
> \text{every unification problem is either non-unifiable or has a most general unifier,}
> $$
> and in the latter case an **idempotent** mgu exists and is computable. Consequently the set of unifiers, when nonempty, is exactly $\{\sigma;\rho:\rho\text{ a substitution}\}$ for any fixed mgu $\sigma$ — there is a single most general solution from which all solutions are instances. Syntactic unification is therefore **unitary** (at most one mgu up to renaming).

> [!definition] Definition 12.2.3: The occurs check
> The **occurs check** is the side condition, when solving $x\stackrel{?}{=}t$ with $x\ne t$, that **$x$ does not occur in $t$**. If $x\in\operatorname{var}(t)$ and $t\ne x$, the equation $x\stackrel{?}{=}t$ has **no** unifier in the finite term algebra (any $\sigma$ would need $x\sigma=t\sigma$ with $t\sigma$ strictly larger than $x\sigma$). Omitting the occurs check is unsound over finite terms (it "solves" $x\stackrel{?}{=}f(x)$ by an infinite/rational term; see §17.2).

### 12.3. The Unification Algorithm

> [!construction] Construction 12.3.1: Martelli–Montanari transformation rules
> Represent the problem as a set of equations and apply the following rules until none applies or **failure** is signaled (here $f,g\in\Omega$, $x\in X$):
> $$
> \textbf{(decompose)}\quad \{f(s_1,\dots,s_n)\stackrel{?}{=}f(t_1,\dots,t_n)\}\cup P\ \rightsquigarrow\ \{s_1\stackrel{?}{=}t_1,\dots,s_n\stackrel{?}{=}t_n\}\cup P,
> $$
> $$
> \textbf{(conflict)}\quad \{f(\dots)\stackrel{?}{=}g(\dots)\}\cup P\ \rightsquigarrow\ \bot\quad(f\ne g\ \text{or differing arity}),
> $$
> $$
> \textbf{(delete)}\quad \{t\stackrel{?}{=}t\}\cup P\ \rightsquigarrow\ P,\qquad \textbf{(swap)}\quad \{t\stackrel{?}{=}x\}\cup P\ \rightsquigarrow\ \{x\stackrel{?}{=}t\}\cup P\ (t\notin X),
> $$
> $$
> \textbf{(eliminate)}\quad \{x\stackrel{?}{=}t\}\cup P\ \rightsquigarrow\ \{x\stackrel{?}{=}t\}\cup P[x{:=}t]\quad(x\notin\operatorname{var}(t),\ x\in\operatorname{var}(P)),
> $$
> $$
> \textbf{(occurs-fail)}\quad \{x\stackrel{?}{=}t\}\cup P\ \rightsquigarrow\ \bot\quad(x\in\operatorname{var}(t),\ t\ne x).
> $$

> [!theorem] Theorem 12.3.2: Correctness and termination of Martelli–Montanari
> The transformation system of Construction 12.3.1: (i) **terminates** on every input (a multiset measure on numbers of unsolved variables and term sizes strictly decreases); (ii) preserves the set of unifiers at each step; and (iii) ends either in $\bot$ (the problem is non-unifiable) or in a **solved form** $\{x_1\stackrel{?}{=}u_1,\dots,x_r\stackrel{?}{=}u_r\}$ with the $x_i$ distinct and not occurring in any $u_j$, which reads off the idempotent mgu $\{x_1\mapsto u_1,\dots,x_r\mapsto u_r\}$.

> [!remark] Remark 12.3.3: Complexity
> Naive unification with (eliminate) can be **exponential** in time and space because substitution duplicates subterms (e.g. $\{x_1\stackrel{?}{=}f(x_0,x_0),x_2\stackrel{?}{=}f(x_1,x_1),\dots\}$). Using **term DAGs with sharing** (base treatise §12.3 hash-consing) and union–find on variable classes yields **almost-linear** time (inverse-Ackermann factor); truly **linear-time** unification (Paterson–Wegman) is achievable. The mgu's *representation* can stay polynomial even when its fully expanded form is exponential — the distinction between a substitution and its expansion mirrors the base treatise's syntax-versus-presentation theme.

### 12.4. Matching, and the Categorical View

> [!definition] Definition 12.4.1: Matching
> A **matching problem** $s\stackrel{?}{\le}t$ asks for a substitution $\sigma$ with $s\sigma=t$ where $\sigma$ may instantiate only the variables of $s$ (the **pattern**) and $t$ (the **subject**) is treated as fixed/ground for the unknowns. Matching is one-sided unification; it is decidable in linear time and has a **unique** matcher when one exists (no most-general issue), and is the operation used to fire a rewrite rule (§13).

> [!theorem] Theorem 12.4.2: Unifiers as equalizers; mgu as most general equalizer
> In the Kleisli category of the term monad (objects sets, morphisms substitutions $X\to T_\Omega(Y)$), a unifier of $s,t:1\to T_\Omega(X)$ is a substitution $\sigma$ coequalizing them, and an **mgu is the coequalizer** of the pair $(s,t)$ in this category when it exists. Thus "most general unifier" is "the universal solution" — the same universal-property pattern as free algebras and quotients in the base treatise, here instantiated in the category of substitutions.

### 12.5. Unification Modulo Equations

> [!definition] Definition 12.5.1: $E$-unification
> For an equational theory $E$, an **$E$-unifier** of $s\stackrel{?}{=}_E t$ is a substitution $\sigma$ with $s\sigma\,=_E\,t\sigma$ (equal modulo $\theta_E^{\mathrm{fi}}$). A set $U$ of $E$-unifiers is **complete** if every $E$-unifier is an $E$-instance of some member of $U$; a **minimal complete set** $\mu U$ removes redundancies. The **unification type** of $E$ classifies the minimal complete sets:
> $$
> \textbf{unitary}\ (\le 1),\quad \textbf{finitary}\ (\text{finite}),\quad \textbf{infinitary}\ (\text{infinite, minimal exists}),\quad \textbf{nullary}\ (\text{no minimal complete set}).
> $$

> [!theorem] Theorem 12.5.2: Landscape of $E$-unification
> (i) **Syntactic** ($E=\varnothing$) unification is unitary (Theorem 12.2.2). (ii) **Commutativity** is finitary. (iii) **Associativity** ($A$) is infinitary; **associativity–commutativity** ($AC$) is finitary and decidable (the Stickel/Livesey–Siekmann algorithms), reducing to solving linear Diophantine systems. (iv) **Associativity–commutativity–identity** and many combinations remain finitary; some theories (e.g. associativity–idempotence variants) are **nullary**. (v) **General $E$-unifiability is undecidable** (it subsumes the word problem and Hilbert's tenth problem for suitable $E$).

> [!warning] Warning 12.5.3: Decidability of $E$-equality does not give decidability of $E$-unification
> Even when $=_E$ is decidable (e.g. $E$ has a convergent rewrite system, §13), **$E$-unification may be undecidable**, and even when decidable it may be of higher type than syntactic unification (finitary/infinitary/nullary). Conversely, a decidable, finitary $E$-unification does not imply a finite convergent presentation. Effectivity of equality (the word problem) and effectivity of solving equations ($E$-unification) are independent properties, paralleling the base treatise's separation of abstract freeness from effective parsing.

> [!example] Example 12.5.4: $AC$-unification is finitary but explosive
> For a single $AC$ symbol $+$, unifying $x+y\stackrel{?}{=}_{AC}u+v$ has a finite minimal complete set whose size grows rapidly (related to the number of solutions of an associated linear Diophantine equation / set partitions). $AC$-unification is decidable and finitary, but the minimal complete set can be exponentially large — the source of much of the cost in $AC$-rewriting and Knuth–Bendix completion modulo $AC$ (§13.5).

---

## 13. Term Rewriting Systems in Depth

The base treatise introduces rewrite systems, termination, confluence, Newman's Lemma, and the decision of the word problem by normalization, but stops short of the machinery that makes rewriting usable: **how to prove termination**, **how to test confluence**, and **how to construct a convergent system** from equations. This part supplies the three, organized as: abstract reduction (§13.1), termination orderings (§13.2), critical pairs and the Critical Pair Lemma (§13.3), and Knuth–Bendix completion (§13.4).

### 13.1. Abstract Reduction Systems

> [!definition] Definition 13.1.1: Abstract reduction system
> An **abstract reduction system (ARS)** is a pair $(\mathcal S,\to)$ with $\to\subseteq\mathcal S\times\mathcal S$. Write $\to^{*}$ for reflexive–transitive closure, $\to^{=}$ for reflexive closure, $\leftrightarrow$ for $\to\cup\to^{-1}$, $\leftrightarrow^{*}$ for the generated equivalence. An element is **normal (irreducible)** if it has no $\to$-successor; $a\to^{!}b$ means $a\to^{*}b$ and $b$ normal. Two elements are **joinable**, $a\downarrow b$, if $\exists c$ with $a\to^{*}c\,{}^{*}{\leftarrow}\,b$.

> [!definition] Definition 13.1.2: Termination, confluence, convergence
> $(\mathcal S,\to)$ is **terminating (strongly normalizing, $\mathsf{SN}$)** if there is no infinite chain $a_0\to a_1\to\cdots$; **normalizing (weakly, $\mathsf{WN}$)** if every element has a normal form; **confluent (Church–Rosser, $\mathsf{CR}$)** if $a\,{}^{*}{\leftarrow}\,\cdot\to^{*}b\Rightarrow a\downarrow b$; **locally confluent (weakly Church–Rosser, $\mathsf{WCR}$)** if $a\leftarrow\cdot\to b\Rightarrow a\downarrow b$; **convergent** if $\mathsf{SN}\wedge\mathsf{CR}$.

> [!theorem] Theorem 13.1.3: Church–Rosser, Newman, and unique normal forms
> (i) Confluence is equivalent to the **Church–Rosser property** $a\leftrightarrow^{*}b\Rightarrow a\downarrow b$. (ii) **Newman's Lemma**: a terminating ARS is confluent iff locally confluent. (iii) A convergent ARS has **unique normal forms**: every $a$ has a unique $a{\downarrow}$, and $a\leftrightarrow^{*}b\iff a{\downarrow}=b{\downarrow}$. For a term rewrite system this decides $\leftrightarrow^{*}$ (the equational theory) by normalization.

> [!definition] Definition 13.1.4: Term rewrite system
> A **term rewrite system (TRS)** over $(\Omega,X)$ is a set $R$ of **rules** $\ell\to r$ with $\ell\notin X$ and $\operatorname{var}(r)\subseteq\operatorname{var}(\ell)$ (the two standard rule conditions). The induced rewrite relation is the closure of $R$ under substitution instances inside contexts:
> $$
> C[\ell\sigma]\ \to_R\ C[r\sigma]\qquad(\ell\to r\in R,\ \sigma\text{ a substitution},\ C[\,]\text{ a context}).
> $$
> A redex is an occurrence $C[\ell\sigma]$; firing it uses **matching** (Definition 12.4.1) of $\ell$ against the subterm.

> [!warning] Warning 13.1.5: The two rule conditions are not optional
> Dropping $\ell\notin X$ permits a rule $x\to r$ matching everywhere, destroying termination and well-definedness; dropping $\operatorname{var}(r)\subseteq\operatorname{var}(\ell)$ permits a rule whose right side introduces fresh variables, so $\to_R$ ceases to be a function of the redex (the fresh variables are unconstrained) and the system no longer presents an equational theory. Both conditions are part of the definition of a TRS.

### 13.2. Termination by Reduction Orderings

> [!definition] Definition 13.2.1: Reduction ordering
> A **reduction ordering** is a strict partial order $>$ on $T_\Omega(X)$ that is (i) **well-founded** (no infinite descending chain), (ii) **monotone (closed under contexts)**: $s>t\Rightarrow C[s]>C[t]$, and (iii) **stable (closed under substitution)**: $s>t\Rightarrow s\sigma>t\sigma$. A TRS $R$ **terminates** iff there is a reduction ordering $>$ with $\ell>r$ for every rule $\ell\to r\in R$ — checking finitely many rule inequalities suffices.

> [!definition] Definition 13.2.2: Simplification orderings and the subterm property
> A **simplification ordering** is a reduction ordering with the **subterm property** $C[t]>t$ for nonempty contexts (a term dominates its proper subterms). By **Kruskal's Tree Theorem** (the finite trees over a finite signature are **well-quasi-ordered** by homeomorphic embedding), every simplification ordering is well-founded automatically — well-foundedness need not be checked separately. This is the theoretical engine behind the syntactic orderings below.

> [!definition] Definition 13.2.3: Recursive/lexicographic path orderings
> Fix a **precedence** $>_{\mathcal F}$ (a strict order on $\Omega$). The **recursive path ordering (RPO)** and its lexicographic variant **LPO** are defined by mutual recursion: $s=f(s_1,\dots,s_m)>_{\mathrm{lpo}}t$ iff one of
> $$
> \textbf{(1)}\ \exists i,\ s_i\ge_{\mathrm{lpo}}t;\qquad \textbf{(2)}\ t=g(t_1,\dots,t_n),\ f>_{\mathcal F}g,\ \text{and}\ s>_{\mathrm{lpo}}t_j\ \forall j;
> $$
> $$
> \textbf{(3)}\ t=f(t_1,\dots,t_m),\ (s_1,\dots,s_m)>^{\mathrm{lex}}_{\mathrm{lpo}}(t_1,\dots,t_m),\ \text{and}\ s>_{\mathrm{lpo}}t_j\ \forall j.
> $$
> RPO uses a multiset comparison in clause (3) instead of lexicographic. Both are simplification orderings; a TRS terminates if some precedence makes every $\ell>_{\mathrm{lpo}}r$ (resp. RPO).

> [!definition] Definition 13.2.4: Knuth–Bendix ordering and polynomial interpretations
> The **Knuth–Bendix ordering (KBO)** fixes a weight function $w$ on symbols and compares terms first by total weight, breaking ties by precedence and recursively — a simplification ordering well-suited to systems where size dominates. A **polynomial interpretation** assigns to each $f\in\Omega_n$ a monotone polynomial $[f]:\mathbb N^n\to\mathbb N$ (with values $\ge$ a positive bound), extends to terms, and yields termination if $[\ell]>[r]$ as polynomials for every rule; well-foundedness is inherited from $(\mathbb N,>)$.

> [!theorem] Theorem 13.2.5: Dependency pairs (statement)
> The **dependency pair** method reduces termination of $R$ to the absence of infinite **chains** of dependency pairs (pairs derived from the recursive calls in right-hand sides). Termination of $R$ holds iff there is no infinite minimal chain, and this is established by exhibiting a **reduction pair** (a weakly monotone, stable order plus a compatible well-founded order) orienting the dependency pairs. The method is **complete** (captures all terminating systems in principle) and is the basis of modern automated termination provers, subsuming the path/weight orderings as components.

> [!warning] Warning 13.2.6: Termination is undecidable
> Whether an arbitrary finite TRS terminates is **undecidable** (it can encode Turing-machine halting); likewise whether a single rule terminates. The orderings above are **sound** sufficient criteria, not decision procedures: failure to find an ordering does not prove non-termination, and no algorithm decides termination in general. Automated provers succeed on large practical classes but cannot be complete.

### 13.3. Critical Pairs and Local Confluence

> [!definition] Definition 13.3.1: Overlap and critical pair
> Let $\ell_1\to r_1$ and $\ell_2\to r_2$ be rules of $R$ (renamed to share no variables). Suppose a **non-variable** subterm $\ell_1|_p$ (at a non-variable position $p$ of $\ell_1$) unifies with $\ell_2$ via mgu $\sigma=\mathrm{mgu}(\ell_1|_p,\ell_2)$. The **critical pair** generated by this **overlap** is
> $$
> \big\langle\, (\ell_1\sigma)[\,r_2\sigma\,]_p,\ \ r_1\sigma\,\big\rangle,
> $$
> the two results of reducing the overlapped redex $\ell_1\sigma$ by the inner rule (at $p$) and by the outer rule (at the root). A critical pair $\langle u,v\rangle$ is **joinable** if $u\downarrow_R v$. (Overlaps of a rule with a renamed copy of itself at the root are excluded as trivial.)

> [!theorem] Theorem 13.3.2: Critical Pair Lemma
> A TRS $R$ is **locally confluent** iff **all** its critical pairs are joinable:
> $$
> \mathsf{WCR}(R)\quad\Longleftrightarrow\quad \forall\ \langle u,v\rangle\in\mathrm{CP}(R):\ u\downarrow_R v.
> $$
> Since a finitary $R$ has only finitely many critical pairs (finitely many rule pairs and non-variable positions), local confluence is **decidable** by computing and joining critical pairs. Divergences not arising from an overlap (disjoint redexes, or a redex inside a variable's image) are always joinable and need not be checked.

> [!corollary] Corollary 13.3.3: Decidable confluence for terminating systems
> If $R$ is terminating, then by Newman's Lemma (Theorem 13.1.3) and the Critical Pair Lemma, $R$ is **confluent iff all critical pairs are joinable**, and this is **decidable**: normalize each critical pair's two components and compare. Hence convergence of a terminating finite TRS is a decidable property — the practical test underlying completion.

> [!warning] Warning 13.3.4: Critical-pair joinability needs termination for the upgrade to confluence
> The Critical Pair Lemma gives only **local** confluence. Local confluence does **not** imply confluence without termination (the standard counterexample $b\leftarrow a\to c$, $b\to b$, $c\to b$-style systems with $b\rightleftarrows c$). Joinable critical pairs yield full confluence only via Newman's Lemma, i.e. only for terminating systems. For non-terminating systems, confluence requires other criteria (e.g. orthogonality / left-linear non-overlapping).

> [!definition] Definition 13.3.5: Orthogonal systems
> A TRS is **left-linear** if no rule's left side repeats a variable, and **non-overlapping** if it has no (non-trivial) critical pairs. **Orthogonal** = left-linear + non-overlapping. Orthogonal systems are **confluent without any termination hypothesis** (a syntactic, decidable sufficient condition), covering the $\lambda$-calculus-style and many functional-program rewrite systems where termination fails but confluence holds.

### 13.4. Knuth–Bendix Completion

> [!construction] Construction 13.4.1: Knuth–Bendix completion procedure
> **Input:** a finite equation set $E$ and a reduction ordering $>$. **State:** a pair $(E_i,R_i)$ of pending equations and oriented rules, initially $(E,\varnothing)$. Repeatedly apply inference rules:
> $$
> \textbf{(orient)}\ \text{remove } s\approx t\in E_i,\ \text{if } s>t\ \text{add } s\to t\ \text{to } R_i\ (\text{or } t\to s\ \text{if } t>s);
> $$
> $$
> \textbf{(deduce)}\ \text{add to } E_i\ \text{each critical pair of } R_i;\qquad \textbf{(simplify)}\ \text{normalize sides of equations and rules by } R_i;
> $$
> $$
> \textbf{(delete)}\ \text{remove trivial } s\approx s;\qquad \textbf{(collapse/compose)}\ \text{rewrite rule sides, discarding subsumed rules.}
> $$

> [!theorem] Theorem 13.4.2: Outcomes of completion
> Run on $(E,>)$, Knuth–Bendix completion has exactly three possible behaviors:
> $$
> \textbf{success:}\ \text{halts with a finite convergent } R\ \text{such that } {\leftrightarrow^{*}_R}={=_E};
> $$
> $$
> \textbf{failure:}\ \text{produces an equation } s\approx t\ \text{with } s\not> t\ \text{and } t\not> s\ (\text{unorientable});
> $$
> $$
> \textbf{divergence:}\ \text{runs forever, generating infinitely many rules.}
> $$
> On **success**, the word problem for $E$ is decided by $R$-normalization (Theorem 13.1.3). The procedure is **correct** (any rule added is an $E$-consequence) and, under a fair strategy, **complete** in the sense that a persistent rule set forms a convergent presentation if completion does not fail.

> [!remark] Remark 13.4.3: Completion as proof ordering; unfailing completion
> Completion is best understood via a **well-founded proof ordering**: each inference replaces an equational proof by a smaller one, and a convergent system is reached exactly when every proof reduces to a **rewrite proof** (a valley $s\to^{*}\cdot{}^{*}{\leftarrow}t$). **Unfailing (ordered) completion** avoids the failure outcome by keeping unorientable equations and using **ordered rewriting** (rewriting only in the $>$-decreasing direction of an instance), yielding a **ground-convergent** system that decides the word problem on ground terms even when no finite convergent TRS exists. This is the form used in equational theorem proving.

> [!warning] Warning 13.4.4: Completion does not always exist or terminate
> Some finitely based theories admit **no finite convergent TRS** for **any** reduction ordering (so completion must diverge or fail), and confluence/termination being undecidable (Warnings 13.2.6, and confluence of non-terminating systems undecidable) means there is no algorithm that always produces a decision procedure. Success of completion is therefore a **fortunate outcome**, not a guarantee; for theories with undecidable word problem (Novikov–Boone, base treatise) no completion can succeed. Effective equational reasoning is a property to be achieved on a case-by-case basis.

> [!example] Example 13.4.5: Group axioms complete to a convergent system
> Starting from the group equations with an LPO precedence $\cdot>{}^{-1}>e$, completion terminates with the classical ten-rule convergent system (including $e\cdot x\to x$, $x^{-1}\cdot x\to e$, $(x\cdot y)\cdot z\to x\cdot(y\cdot z)$, $(x\cdot y)^{-1}\to y^{-1}\cdot x^{-1}$, $x^{-1}{}^{-1}\to x$, and the derived rules from critical pairs). Its normal forms are the reduced words, recovering the decidability of the **free**-group word problem — while general finitely presented groups (with extra ground relations) retain an undecidable word problem, exactly delimiting where completion can help.

---

## 14. Narrowing

Rewriting computes the normal form of a **given** term; **narrowing** generalizes rewriting by *instantiating* variables on the fly so as to enable a rule to fire, thereby **solving** equations rather than merely evaluating them. It is the operational mechanism behind $E$-unification for convergent $E$ and behind functional-logic programming.

> [!definition] Definition 14.1.1: Narrowing relation
> Let $R$ be a TRS. A term $s$ **narrows** to $t$ with substitution $\sigma$, written $s\rightsquigarrow_{\sigma}t$, if there is a non-variable position $p$ in $s$, a rule $\ell\to r\in R$ (renamed apart), and $\sigma=\mathrm{mgu}(s|_p,\ell)$ such that
> $$
> t=(s[\,r\,]_p)\sigma=(s\sigma)[\,r\sigma\,]_p.
> $$
> Narrowing is rewriting preceded by the **most general instantiation** making $s|_p$ a redex; ordinary rewriting is the special case where $s|_p$ already matches $\ell$ (so $\sigma$ is a matcher, not a proper unifier).

> [!definition] Definition 14.1.2: Narrowing derivation and computed substitution
> A **narrowing derivation** $s_0\rightsquigarrow_{\sigma_1}s_1\rightsquigarrow_{\sigma_2}\cdots\rightsquigarrow_{\sigma_n}s_n$ has **computed substitution** $\sigma=\sigma_1;\cdots;\sigma_n$ restricted to $\operatorname{var}(s_0)$. To solve $s\stackrel{?}{=}_E t$ one narrows the term $\mathrm{eq}(s,t)$ (or $s$ and $t$ jointly) toward a term recognizably true (e.g. reducible to a common normal form), collecting $\sigma$ as the solution.

> [!theorem] Theorem 14.1.3: Completeness of narrowing for convergent systems
> If $R$ is a **convergent** TRS presenting $E$, then narrowing is **sound and complete for $E$-unification**: for every $E$-unifier $\tau$ of $s\stackrel{?}{=}_E t$ there is a narrowing derivation from $s\stackrel{?}{=}t$ to a syntactically unifiable pair whose computed substitution $\sigma$ is more general than $\tau$ (modulo $E$). Thus the set of computed substitutions of all narrowing derivations is a **complete set of $E$-unifiers**. The **Lifting Lemma** (every rewrite sequence on an instance is mirrored by a narrowing sequence on the pattern) is the technical core.

> [!definition] Definition 14.1.4: Refinements
> Unrestricted narrowing has a vast search space; standard refinements preserve completeness while pruning: **basic narrowing** (never narrow within subterms introduced by previous substitutions), **innermost/needed narrowing** (narrow at strategically chosen positions, optimal for left-linear constructor systems), and **narrowing modulo** an underlying $AC$ theory. Needed narrowing is the operational semantics of modern functional-logic languages.

> [!warning] Warning 14.1.5: Narrowing need not terminate even when rewriting does
> Convergence of $R$ guarantees that **rewriting** terminates, but **narrowing** explores instantiations and may produce an **infinite** search tree (since each step may introduce new variables and new redexes). Completeness is about covering all solutions in the limit, not about termination of the search. Decidability of $E$-unification (Theorem 12.5.2) is therefore a separate question from the existence of a convergent $R$; narrowing enumerates solutions but does not by itself decide unifiability.

> [!remark] Remark 14.1.6: Narrowing unifies the two directions
> Rewriting is evaluation (the base treatise's $\operatorname{ev}$ made effective); unification (§12) is equation solving in the free algebra; narrowing is **equation solving modulo a rewrite theory**, combining both. In the categorical picture, where unification computes coequalizers in the Kleisli category (Theorem 12.4.2), narrowing computes the analogous universal solutions in the Kleisli category of the **quotient** theory — the effective counterpart of the base treatise's quotient/presentation layer.

---

# Part V — Recognizability: Tree Automata

## 15. Finite Tree Automata

The base treatise presents trees as a concrete carrier of the free algebra and studies unique decomposition, but not which **sets** of trees are finitely describable. **Tree automata** are finite $\Omega$-algebras used as acceptors; the recognizable tree languages they define are exactly the **finite-index** congruence classes of the term algebra (Theorem 15.4.2) — a Myhill–Nerode theorem lifting regular-language theory from strings to terms. This is the recognizability theory of $\mathbf T_\Omega(\varnothing)$.

### 15.1. Bottom-Up Tree Automata

> [!definition] Definition 15.1.1: Finite bottom-up tree automaton
> Fix a finite ranked signature $\Omega$. A **(nondeterministic) finite bottom-up tree automaton (NFTA)** is $\mathcal A=(Q,\Omega,Q_f,\Delta)$ with $Q$ a finite set of **states**, $Q_f\subseteq Q$ the **accepting (final) states**, and $\Delta$ a set of **transition rules**
> $$
> f(q_1,\dots,q_n)\to q\qquad(f\in\Omega_n,\ q_1,\dots,q_n,q\in Q),
> $$
> including, for constants, $c\to q$. A **run** on a ground term $t\in T_\Omega(\varnothing)$ is a labeling of the positions of $t$ by states consistent with $\Delta$; the run is **accepting** if the root is labeled by a state in $Q_f$.

> [!definition] Definition 15.1.2: Recognized language; determinism
> The **language recognized** by $\mathcal A$ is $L(\mathcal A)=\{t\in T_\Omega(\varnothing):\mathcal A\text{ has an accepting run on }t\}$. $\mathcal A$ is **deterministic (DFTA)** if for each $f$ and state tuple $(q_1,\dots,q_n)$ there is **at most one** rule $f(q_1,\dots,q_n)\to q$; then each $t$ has at most one run. $\mathcal A$ is **complete** if "at most one" is "exactly one." A tree language is **recognizable** if some NFTA recognizes it.

> [!remark] Remark 15.1.3: A DFTA is a finite $\Omega$-algebra plus an accepting set
> A complete DFTA is exactly a finite $\Omega$-algebra $\mathcal Q=(Q,(f^{\mathcal Q})_{f})$ with $f^{\mathcal Q}(q_1,\dots,q_n)=q$ the transition value, together with $Q_f\subseteq Q$. Its run on $t$ is the **evaluation homomorphism** $\operatorname{ev}:\mathbf T_\Omega(\varnothing)\to\mathcal Q$ (base treatise Theorem 1.3.2), and $L(\mathcal A)=\operatorname{ev}^{-1}(Q_f)$. Tree recognizability is thus literally "$L$ is the preimage of a subset under a homomorphism to a finite algebra" — the algebraic definition of recognizability.

### 15.2. Top-Down Automata and the Determinism Asymmetry

> [!definition] Definition 15.2.1: Top-down tree automaton
> A **top-down** tree automaton has initial states and rules $q\to f(q_1,\dots,q_n)$ read root-to-frontier: a run assigns the root an initial state and propagates state tuples down to the leaves. Nondeterministic top-down automata recognize exactly the recognizable languages (same class as NFTA).

> [!warning] Warning 15.2.2: Deterministic top-down automata are strictly weaker
> Unlike the string case, **deterministic top-down** tree automata recognize a **proper subclass** of the recognizable languages (the "path-closed" languages). For example, the finite language $\{f(a,b),f(b,a)\}$ is recognizable but not accepted by any deterministic top-down automaton, because a deterministic top-down run fixes each child's state from the parent's alone and cannot correlate sibling choices. Determinization is available **bottom-up** (Theorem 15.3.2) but **not** top-down. The canonical model for trees is therefore the bottom-up deterministic automaton.

### 15.3. Closure Properties and Determinization

> [!theorem] Theorem 15.3.1: Boolean and projection closure
> The recognizable tree languages over $\Omega$ are an effective **Boolean algebra**: closed under union, intersection, and complement, with automata constructible from the inputs (product automaton for $\cap$, $\cup$; complementation via a complete DFTA by complementing $Q_f$). They are also closed under **tree homomorphisms** and inverse homomorphisms, under **projection** (relabeling), and under intersection with the set of terms of a given shape.

> [!theorem] Theorem 15.3.2: Determinization
> Every NFTA is equivalent to a complete DFTA obtained by the **subset construction**: states are subsets of $Q$, with $f(\mathbf{S}_1,\dots,\mathbf{S}_n)\to\{q:\exists q_i\in \mathbf S_i,\ f(q_1,\dots,q_n)\to q\in\Delta\}$ and accepting subsets those meeting $Q_f$. The blow-up is at most exponential ($2^{|Q|}$). Consequently NFTA and DFTA recognize the same languages, and recognizability is a robust class.

> [!theorem] Theorem 15.3.3: Minimal automaton
> Every recognizable tree language $L$ has a **unique minimal complete DFTA** (up to isomorphism), the quotient of any complete DFTA for $L$ by the **state-equivalence** relation (states indistinguishable by all accepting contexts). Minimization is effective and the minimal automaton is canonical, exactly as in the string case.

### 15.4. Myhill–Nerode for Trees

> [!definition] Definition 15.4.1: Syntactic congruence of a tree language
> For $L\subseteq T_\Omega(\varnothing)$, the **syntactic (Myhill–Nerode) congruence** $\equiv_L$ on $T_\Omega(\varnothing)$ is
> $$
> s\equiv_L t\quad\Longleftrightarrow\quad \forall\ \text{contexts } C[\,]:\ \big(C[s]\in L\Leftrightarrow C[t]\in L\big),
> $$
> where $C[\,]$ ranges over one-hole contexts (base treatise Definition 1.3.3 / 4.4.2). $\equiv_L$ is a congruence on $\mathbf T_\Omega(\varnothing)$.

> [!theorem] Theorem 15.4.2: Myhill–Nerode theorem for trees
> For $L\subseteq T_\Omega(\varnothing)$ the following are equivalent:
> $$
> \textbf{(a)}\ L\ \text{is recognizable};\quad \textbf{(b)}\ \equiv_L\ \text{has finite index};\quad \textbf{(c)}\ L\ \text{is a union of classes of some finite-index congruence on } \mathbf T_\Omega(\varnothing).
> $$
> The minimal DFTA (Theorem 15.3.3) is the quotient algebra $\mathbf T_\Omega(\varnothing)/{\equiv_L}$ with accepting set the classes contained in $L$. Recognizability is exactly **finite-index congruence saturation** — the term-algebra form of the classical string Myhill–Nerode theorem.

> [!theorem] Theorem 15.4.3: Decidability of basic problems
> For NFTA the following are **decidable**: **membership** ($t\in L(\mathcal A)$, in polynomial time by a bottom-up run), **emptiness** ($L(\mathcal A)=\varnothing$, by reachability of an accepting state, linear time), **finiteness** ($L(\mathcal A)$ finite, by detecting productive loops), **inclusion** and **equivalence** (via complement and intersection, $\mathsf{EXPTIME}$-complete for NFTA, polynomial for DFTA). A **pumping lemma** holds: sufficiently tall accepted trees contain an iterable context $C[\,]$ with $C^k[\,]$ preserving acceptance.

### 15.5. Recognizable versus Equational; Logic on Trees

> [!definition] Definition 15.5.1: Regular tree grammar and equational tree language
> A **regular tree grammar** has nonterminals, a start symbol, and productions $A\to f(B_1,\dots,B_n)$; the generated language is the set of ground terms derivable. **Regular tree languages** (grammar-generated) coincide with the **recognizable** ones. The larger class of **equational (context-free) tree languages** is generated by allowing nonterminals of higher rank (parameters); these correspond to least solutions of systems of equations over tree-language operations and strictly extend the recognizable class.

> [!theorem] Theorem 15.5.2: Recognizable = MSO-definable (Thatcher–Wright, Doner)
> A tree language $L\subseteq T_\Omega(\varnothing)$ is recognizable iff it is definable in **monadic second-order logic (MSO)** over the tree (with the child relations and label predicates):
> $$
> L\ \text{recognizable}\quad\Longleftrightarrow\quad L=\{t:t\models\varphi\}\ \text{for some MSO sentence }\varphi.
> $$
> This is the tree generalization of the Büchi–Elgot–Trakhtenbrot theorem for strings and links automata, algebra (finite-index congruences), grammars, and logic into a single notion of regularity. The translation in both directions is effective, so MSO satisfiability over finite trees is decidable.

> [!remark] Remark 15.5.3: Four faces of tree regularity
> Recognizable tree languages have four equivalent descriptions — **automata** (finite bottom-up DFTA), **algebra** (preimages of subsets under homomorphisms to finite $\Omega$-algebras; finite-index congruences), **grammars** (regular tree grammars), and **logic** (MSO). This fourfold equivalence is the tree-level analogue of the base treatise's representation-independence theme: one robust class, many presentations. It also connects to §13: the set of $R$-normal forms of a left-linear TRS is recognizable, so confluence and reachability questions can be attacked with tree-automata techniques (tree automata completion).

---

# Part VI — The Coalgebraic and Infinitary Dual

## 16. Infinitary Terms and Continuous Algebras

The base treatise's term algebra is the **initial** algebra: its elements are **finite**, **well-founded** trees, and its governing principle is structural **induction/recursion**. This part develops the **dual** object — infinite terms — obtained by completing the finite term algebra, preparing the coalgebraic treatment of §17. Two completions are standard: a **metric** completion (infinite trees of finite branching) and an **order-theoretic** completion (partial terms with a bottom element).

### 16.1. Partial Terms and the Tree Order

> [!definition] Definition 16.1.1: Partial terms
> Adjoin to $\Omega$ a fresh nullary symbol $\bot$ ("undefined"). The **partial terms** $T^\bot_\Omega(X)$ are the (finite) terms over $\Omega\cup\{\bot\}$ and $X$. The **approximation order** $\sqsubseteq$ is the least partial order with $\bot\sqsubseteq t$ for all $t$ and $f(s_1,\dots,s_n)\sqsubseteq f(t_1,\dots,t_n)$ whenever $s_i\sqsubseteq t_i$; thus $s\sqsubseteq t$ means "$t$ refines $s$ by replacing some $\bot$-leaves with subterms." $(T^\bot_\Omega(X),\sqsubseteq)$ is a poset with least element $\bot$.

> [!definition] Definition 16.1.2: Ideal completion and infinite terms
> The **ideal completion** of $(T^\bot_\Omega(X),\sqsubseteq)$ is the set of $\sqsubseteq$-directed downward-closed sets (ideals) of partial terms, ordered by inclusion; it is an **algebraic complete partial order (CPO)** whose **compact** elements are the finite partial terms. Its maximal elements are the **(possibly infinite) total terms**. The set $T^\infty_\Omega(X)$ of **finite-and-infinite terms** is obtained by taking all directed suprema; an infinite term is the supremum of its finite approximations.

> [!definition] Definition 16.1.3: Metric on terms
> Alternatively, define the **distance** $d(s,t)=2^{-k}$ where $k$ is the least depth at which $s$ and $t$ differ ($d(s,t)=0$ if $s=t$). $(T_\Omega(X),d)$ is an **ultrametric** space; its **Cauchy completion** $\widehat T_\Omega(X)$ is the set of all finite and infinite $\Omega$-trees of the given (finite) branching. The metric and the order completion agree on **total** infinite terms.

### 16.2. Rational and Algebraic Infinite Terms

> [!definition] Definition 16.2.1: Rational terms
> An infinite term is **rational (regular)** if it has only **finitely many distinct subterms**, equivalently if it is the **unfolding** of a finite **cyclic** term graph, equivalently if it is the unique solution of a finite system of **guarded** recursion equations $x_i=f_i(\dots)$. Rational terms are the infinite-term analogue of regular trees and are exactly the terms denotable by finite cyclic data structures.

> [!theorem] Theorem 16.2.2: Solutions of guarded equations
> In $\widehat T_\Omega(X)$, every **guarded** recursive system (each right side has a constructor at the head before any recursive variable) has a **unique** solution. In particular $x=f(x)$ has the unique solution $f(f(f(\cdots)))=f^\omega$, the infinite term that finite unification rejects by the occurs check (Definition 12.2.3). **Rational-tree unification** drops the occurs check and computes mgus in $\widehat T_\Omega(X)$; it underlies cyclic-structure unification in some Prolog systems.

> [!warning] Warning 16.2.3: The occurs check is exactly the finite/infinite boundary
> Removing the occurs check is **unsound** over finite terms $T_\Omega(X)$ (Definition 12.2.3) but **sound and complete** over rational terms $\widehat T_\Omega(X)$: there, $x\stackrel{?}{=}f(x)$ has the solution $x\mapsto f^\omega$. The choice of term universe — initial (finite, occurs check) versus final/completed (infinite, no occurs check) — determines which unification is correct. This is the most concrete appearance of the algebra/coalgebra duality (§17).

### 16.3. Continuous Algebras

> [!definition] Definition 16.3.1: Continuous (ordered) $\Omega$-algebra
> A **continuous $\Omega$-algebra** (in the sense of the ADJ group) is an $\Omega$-algebra whose carrier is a CPO with least element $\bot$ and whose operations $f^A$ are **continuous** (monotone and preserving directed suprema). A **continuous homomorphism** is a continuous, $\bot$- and operation-preserving map.

> [!theorem] Theorem 16.3.2: Initial continuous algebra
> The completed term algebra $T^\infty_\Omega(X)$ (with $\bot$ and the constructors extended continuously) is the **initial continuous $\Omega$-algebra** on $X$: every map $g:X\to|A|$ into a continuous algebra extends to a **unique continuous homomorphism** $T^\infty_\Omega(X)\to A$. This is the order-theoretic counterpart of the base treatise's freeness, and it underwrites **recursion with non-termination**: partial and infinite computations receive values as directed suprema of their finite approximations, the basis of denotational semantics of recursive programs.

> [!remark] Remark 16.3.3: Three universes of terms
> The companion now has three term universes over $(\Omega,X)$: the **finite** terms $\mathbf T_\Omega(X)$ (initial algebra; induction/recursion; finite unification with occurs check); the **continuous** terms $T^\infty_\Omega(X)$ (initial *continuous* algebra; recursion through $\bot$; denotational fixpoints); and the **infinite** terms $\widehat T_\Omega(X)$ (final coalgebra, §17; coinduction/corecursion; rational-tree unification). The base treatise occupies only the first. The next section gives the third its universal property.

---

## 17. Coalgebra and the Final Coalgebra

Where an **algebra** $\alpha:H_\Omega A\to A$ packages **constructors** (how to **build** elements) and is governed by **initiality/induction**, a **coalgebra** $\gamma:C\to H_\Omega C$ packages **destructors/observations** (how to **observe** one layer of an element) and is governed by **finality/coinduction**. The final coalgebra is the universe of **infinite** behaviors; corecursion defines maps **into** it, and bisimulation proves equality **of** its elements. This is the systematic dual of the base treatise's §13 (polynomial functors and initial algebras).

### 17.1. Coalgebras of the Signature Functor

> [!definition] Definition 17.1.1: $H_\Omega$-coalgebra
> Recall the signature endofunctor $H_\Omega(Y)=\coprod_{f\in\Omega}Y^{\operatorname{ar}(f)}$ (base treatise §13.3; sorted version Definition 2.3.4). An **$H_\Omega$-coalgebra** is a pair $(C,\gamma)$ with $\gamma:C\to H_\Omega C$; the map $\gamma$ assigns to each state $c$ a **single top constructor** together with its **immediate successor states**. A **coalgebra homomorphism** $h:(C,\gamma)\to(D,\delta)$ is $h:C\to D$ with $\delta\circ h=H_\Omega(h)\circ\gamma$ (it preserves one-step observations).

> [!remark] Remark 17.1.2: Coalgebra = transition structure
> An $H_\Omega$-coalgebra is exactly a deterministic transition system whose every state emits one labeled tuple of successor states — a (possibly infinite, possibly cyclic) generation process. Reading $\gamma$ "forward" repeatedly unfolds a state into an infinite tree. Coalgebra is the mathematics of **process, observation, and ongoing behavior**, dual to algebra's **construction, value, and well-founded structure**.

### 17.2. The Final Coalgebra and Corecursion

> [!theorem] Theorem 17.2.1: Existence and form of the final coalgebra
> The polynomial endofunctor $H_\Omega$ has a **final coalgebra** $(\nu H_\Omega,\ \mathrm{out})$. Its carrier is the set of **finite-and-infinite $\Omega$-trees** (the metric completion of ground terms, Definition 16.1.3): $\nu H_\Omega\cong T^\infty_\Omega(\varnothing)$ restricted to **total** trees $\widehat T_\Omega(\varnothing)$. The structure map $\mathrm{out}:\nu H_\Omega\to H_\Omega(\nu H_\Omega)$ is the **root-and-immediate-subtrees** destructor and is, by **Lambek's Lemma (dual form)**, an **isomorphism** — the coalgebraic statement of unique decomposition for infinite trees.

> [!theorem] Theorem 17.2.2: Corecursion (anamorphism)
> Finality means: for **every** coalgebra $(C,\gamma)$ there is a **unique** coalgebra homomorphism
> $$
> \mathrm{unfold}_\gamma:\ (C,\gamma)\ \longrightarrow\ (\nu H_\Omega,\mathrm{out}),
> $$
> the **anamorphism**, defined by $\mathrm{out}\circ\mathrm{unfold}_\gamma=H_\Omega(\mathrm{unfold}_\gamma)\circ\gamma$. This is **definition by corecursion**: to define a function **into** infinite trees it suffices to specify, for each input, the **one top layer** of output and the recursive arguments; finality guarantees a unique total function producing the infinite unfolding. Corecursion is the exact dual of the base treatise's structural recursion (its Theorem 6.2.1 / 13.3.3).

> [!definition] Definition 17.2.3: Guardedness and productivity
> A corecursive definition is **guarded (productive)** if every recursive call is **beneath at least one constructor**, so each unfolding step emits genuine output. Guardedness is the corecursive counterpart of well-foundedness for recursion: it guarantees the anamorphism is total and that each finite prefix of the output is computed in finitely many steps. Unguarded corecursion (a recursive call at the head, $x:=x$) is non-productive and ill-defined, dual to non-terminating unbounded recursion.

### 17.3. Bisimulation and the Coinduction Principle

> [!definition] Definition 17.3.1: Bisimulation
> A **bisimulation** between $H_\Omega$-coalgebras $(C,\gamma)$ and $(D,\delta)$ is a relation $R\subseteq C\times D$ that lifts to a coalgebra structure on $R$ making the two projections coalgebra homomorphisms; concretely, $(c,d)\in R$ implies $c$ and $d$ have the **same top constructor** and their corresponding immediate successors are again $R$-related. Two states are **bisimilar**, $c\sim d$, if some bisimulation relates them.

> [!theorem] Theorem 17.3.2: Coinduction proof principle
> On the final coalgebra $\nu H_\Omega$, **bisimilarity coincides with equality**:
> $$
> c\sim d\quad\Longleftrightarrow\quad c=d.
> $$
> Hence the **coinduction principle**: to prove two infinite trees (or two states' unfoldings) **equal**, exhibit a **bisimulation** relating them. This replaces, for infinite/observational data, the base treatise's proof-by-structural-induction; one reasons about equality of non-well-founded objects without ever decomposing them to a base case.

> [!warning] Warning 17.3.3: Induction and coinduction are not interchangeable
> Structural induction proves properties of **all finite** terms by descending to constructors; it is **invalid** on infinite terms (there is no base case to reach). Coinduction proves **equalities/observational properties** of **possibly infinite** behaviors by exhibiting invariant relations; it does **not** prove arbitrary predicates and is **invalid** as a substitute for induction on finite data (it can "prove" false universal statements if misapplied to least fixpoints). The correct discipline: **induction for initial-algebra (least, well-founded) data; coinduction for final-coalgebra (greatest, observational) data**. Mixing them is a category error.

### 17.4. Algebra–Coalgebra Duality and Bialgebras

> [!theorem] Theorem 17.4.1: The duality, summarized
> For the polynomial functor $H_\Omega$:
> $$
> \begin{array}{lll}
> \textbf{initial algebra }\mu H_\Omega & \quad\text{vs.}\quad & \textbf{final coalgebra }\nu H_\Omega\\
> \text{finite well-founded terms} & & \text{finite-and-infinite terms}\\
> \text{constructors }H_\Omega(\mu)\xrightarrow{\cong}\mu & & \text{destructors }\nu\xrightarrow{\cong}H_\Omega(\nu)\\
> \text{recursion (catamorphism, unique out of }\mu) & & \text{corecursion (anamorphism, unique into }\nu)\\
> \text{induction} & & \text{coinduction (bisimulation)}\\
> \text{occurs check holds; finite unification} & & \text{occurs check dropped; rational-tree unification}
> \end{array}
> $$
> The canonical comparison $\mu H_\Omega\hookrightarrow\nu H_\Omega$ embeds finite terms as the well-founded elements of the infinite-term coalgebra; it is an isomorphism iff $\Omega$ has no operation of arity $\ge1$ (only then are all trees finite).

> [!definition] Definition 17.4.2: Bialgebras and structured operational semantics
> A **bialgebra** for a functor pair combines an $H_\Omega$-algebra (syntax/constructors) and a $B$-coalgebra (behavior/transitions) on a common carrier, related by a **distributive law** $\lambda:H_\Omega B\Rightarrow B H_\Omega$. A distributive law is exactly a **well-behaved structural operational semantics** (the **GSOS** rule format): it guarantees that **bisimilarity is a congruence** for the syntax, so observational equivalence is compositional. This unifies the base treatise's syntax-algebra with behavioral semantics in one structure.

> [!remark] Remark 17.4.3: Where the dual completes the base treatise
> The base treatise builds, exhaustively, the **initial/algebraic/inductive** side: free term algebras, structural recursion, finite unification, the term monad. Part VI supplies the systematically **dual** side: final coalgebras, corecursion, coinduction/bisimulation, rational-tree unification, and (via bialgebras) compositional behavioral semantics. The two sides meet at the polynomial functor $H_\Omega$, whose least and greatest fixpoints are the two term universes; the occurs check is the visible seam between them. Together they give the full fixpoint theory of a signature, of which the base treatise developed precisely the least-fixpoint half.

---

# Part VII — Structure Theory of Varieties

## 18. Varieties and the HSP Theorem

The base treatise states Birkhoff's HSP theorem and the completeness of equational logic as headline results (its Theorem 8.4.3). This part develops the surrounding **structure theory of equational classes**: the closure operators, the variety theorem with all hypotheses, the precise relationship between equational theories and fully invariant congruences, and the construction of free algebras inside a variety. Throughout, $\Omega$ is a fixed (possibly infinite) finitary signature and "class" means a class of $\Omega$-algebras closed under isomorphism.

### 18.1. The Class Operators

> [!definition] Definition 18.1.1: The operators $H, S, P, P_{\!S}, P_{\!U}$
> For a class $\mathcal K$ of $\Omega$-algebras:
> $$
> H\mathcal K\ :=\ \{\text{homomorphic images of members of }\mathcal K\};\qquad S\mathcal K\ :=\ \{\text{subalgebras of members of }\mathcal K\};
> $$
> $$
> P\mathcal K\ :=\ \{\text{direct products }\textstyle\prod_{i\in I}A_i:\ A_i\in\mathcal K,\ I\ \text{any set}\}\ \ (\text{including the empty product, the trivial algebra});
> $$
> $$
> P_{\!S}\mathcal K\ :=\ \{\text{subdirect products of members of }\mathcal K\};\qquad P_{\!U}\mathcal K\ :=\ \{\text{ultraproducts of members of }\mathcal K\}.
> $$
> Each is a **closure-like operator** (extensive and monotone); $H,S,P$ are idempotent on the classes they produce but do not individually commute.

> [!definition] Definition 18.1.2: Variety
> A class $\mathcal V$ is a **variety** (equational class) if it is closed under $H$, $S$, and $P$: $H\mathcal V\subseteq\mathcal V$, $S\mathcal V\subseteq\mathcal V$, $P\mathcal V\subseteq\mathcal V$. Equivalently $\mathcal V=HSP\,\mathcal V$. The trivial (one-element) algebra lies in every nonempty variety (as the empty product).

> [!proposition] Proposition 18.1.3: $HSP$ is the variety closure
> For any class $\mathcal K$, the smallest variety containing $\mathcal K$ is
> $$
> V(\mathcal K)\ =\ HSP\,\mathcal K,
> $$
> and the operator composition stabilizes after this single application: $H(SP\mathcal K)\subseteq HSP\mathcal K$, $S(HSP\mathcal K)\subseteq HSP\mathcal K$, $P(HSP\mathcal K)\subseteq HSP\mathcal K$. In particular $SP\mathcal K\subseteq PS\mathcal K$ and $PH\mathcal K\subseteq HP\mathcal K$ and $SH\mathcal K\subseteq HS\mathcal K$ hold as the commutation lemmas making the three-operator word collapse.

### 18.2. Identities and the Galois Connection

> [!definition] Definition 18.2.1: The satisfaction relation and its polars
> Fix a countably infinite variable set $X_\omega$. For a class $\mathcal K$ and a set $\Theta\subseteq T_\Omega(X_\omega)^2$ of identities, define the **Galois polars** of the relation $A\models s\approx t$:
> $$
> \operatorname{Id}(\mathcal K)\ :=\ \{(s,t):\forall A\in\mathcal K,\ A\models s\approx t\};\qquad \operatorname{Mod}(\Theta)\ :=\ \{A:\forall (s,t)\in\Theta,\ A\models s\approx t\}.
> $$
> $\operatorname{Id}$ sends classes to identity-sets; $\operatorname{Mod}$ sends identity-sets to classes; $(\operatorname{Id},\operatorname{Mod})$ is a **Galois connection** between classes and theories.

> [!theorem] Theorem 18.2.2: Birkhoff's variety (HSP) theorem
> The Galois-closed classes are exactly the varieties, and the Galois-closed theories are exactly the **fully invariant congruences** on $\mathbf T_\Omega(X_\omega)$:
> $$
> \mathcal V=\operatorname{Mod}(\operatorname{Id}(\mathcal V))\ \Longleftrightarrow\ \mathcal V\ \text{is a variety}\ \Longleftrightarrow\ \mathcal V=HSP\,\mathcal V,
> $$
> $$
> \Theta=\operatorname{Id}(\operatorname{Mod}(\Theta))\ \Longleftrightarrow\ \Theta\ \text{is a fully invariant congruence on }\mathbf T_\Omega(X_\omega).
> $$
> Hence a class is definable by a set of equations iff it is closed under homomorphic images, subalgebras, and products.

> [!corollary] Corollary 18.2.3: Equational theories $\leftrightarrow$ fully invariant congruences
> The lattice of equational theories of signature $\Omega$ (sets of identities closed under deduction) is **dually isomorphic** to the lattice of subvarieties of $\mathbf{Alg}(\Omega)$, and **isomorphic** to the lattice of fully invariant congruences on the countably generated free algebra $\mathbf T_\Omega(X_\omega)$. Bigger theories cut out smaller varieties; the trivial variety corresponds to the all-relation, the whole class to the diagonal.

### 18.3. Free Algebras in a Variety

> [!construction] Construction 18.3.1: Relatively free algebra
> Let $\mathcal V=\operatorname{Mod}(E)$ be a variety with fully invariant congruence $\theta^{\mathrm{fi}}_E=\operatorname{Id}(\mathcal V)$. The **$\mathcal V$-free algebra on $X$** is
> $$
> \mathbf F_{\mathcal V}(X)\ :=\ \mathbf T_\Omega(X)\big/\theta^{\mathrm{fi}}_E\restriction_X,
> $$
> where $\theta^{\mathrm{fi}}_E\restriction_X$ is the restriction to $T_\Omega(X)^2$ of the fully invariant congruence. It is characterized by the **relative universal property**: $\mathbf F_{\mathcal V}(X)\in\mathcal V$ and every map $X\to|A|$ with $A\in\mathcal V$ extends uniquely to a homomorphism $\mathbf F_{\mathcal V}(X)\to A$.

> [!theorem] Theorem 18.3.2: Free algebras generate the variety
> For any variety $\mathcal V$ and infinite $X$:
> $$
> \mathcal V\ =\ HSP(\{\mathbf F_{\mathcal V}(X)\})\ =\ H(\{\mathbf F_{\mathcal V}(Y):Y\ \text{a set}\}),
> $$
> i.e. every member of $\mathcal V$ is a homomorphic image of a relatively free algebra, and $\mathbf F_{\mathcal V}(X_\omega)$ alone generates $\mathcal V$ as a variety. Identities of $\mathcal V$ in $n$ variables are read off from $\mathbf F_{\mathcal V}(X_n)$: $\mathcal V\models s\approx t\iff s,t$ map to the same element of $\mathbf F_{\mathcal V}(\operatorname{var}(s)\cup\operatorname{var}(t))$.

> [!example] Example 18.3.3: Relatively free vs absolutely free
> (i) The absolutely free algebra is $\mathbf F_{\mathbf{Alg}(\Omega)}(X)=\mathbf T_\Omega(X)$ ($E=\varnothing$). (ii) The free group on $X$ is $\mathbf F_{\mathsf{Grp}}(X)$, with carrier the reduced words. (iii) The free Boolean algebra on $X$ is $\mathbf F_{\mathsf{BA}}(X)$, finite of order $2^{2^{n}}$ when $|X|=n$, isomorphic to the algebra of $n$-ary Boolean functions. (iv) The free semilattice on $X$ is the finite-nonempty-subsets algebra $(\mathcal P_{\mathrm{fin}}^{+}(X),\cup)$. Each is $\mathbf T_\Omega(X)$ quotiented by the relevant fully invariant congruence.

> [!warning] Warning 18.3.4: Relatively free is not free in the bare signature
> $\mathbf F_{\mathcal V}(X)$ has the universal property **only with respect to algebras in $\mathcal V$**; it is generally **not** free in $\mathbf{Alg}(\Omega)$ (its constructors collapse, so unique readability fails — base treatise Warning 2.3.4). Conflating "free group" with "absolutely free algebra of group signature" is the standard error: the former satisfies the group laws and has reduced-word normal forms, the latter satisfies none and keeps all terms distinct.

### 18.4. Subvarieties and the Lattice of Varieties

> [!definition] Definition 18.4.1: Lattice of subvarieties
> The subvarieties of a variety $\mathcal V$, ordered by inclusion, form a complete lattice $L(\mathcal V)$: meets are intersections, joins are $V(\cdot)$ of unions. By Corollary 18.2.3 this is dually isomorphic to the lattice of equational theories extending $\operatorname{Id}(\mathcal V)$. The bottom is the trivial variety; the top is $\mathcal V$.

> [!example] Example 18.4.2: Some subvariety lattices
> (i) The lattice of varieties of **groups** is uncountable and richly structured (Neumann); abelian groups form a single coatom-free chain of varieties $\mathcal A_n$ (exponent-$n$ abelian groups) plus their joins. (ii) The lattice of varieties of **lattices** has the trivial, distributive, and modular varieties at the bottom; distributive lattices are the unique atom. (iii) The lattice of varieties of **semigroups** is uncountable. The size and complexity of $L(\mathcal V)$ is itself an invariant of $\mathcal V$.

> [!remark] Remark 18.4.3: Maltsev product and decomposition
> Beyond the lattice operations, varieties admit a **Mal'cev product** $\mathcal U\circ\mathcal W$ (algebras with a congruence whose classes are in $\mathcal U$ and quotient in $\mathcal W$), which is generally not a variety but generates one and underlies decomposition theorems. These refinements organize the otherwise unwieldy lattice $L(\mathcal V)$ and connect to the congruence-theoretic invariants of §21.

---

## 19. Subdirect Representation, Quasivarieties, and Ultraproducts

Birkhoff's variety theorem classifies equationally definable classes; the present part supplies the two complementary structure theorems the base treatise omits: the **subdirect decomposition** of every algebra into "irreducible" pieces, and the **quasivariety** theory governing classes defined by **implications** rather than equations. The latter requires the **ultraproduct** construction and Łoś's theorem, which also underlie the model-theoretic half of universal algebra.

### 19.1. Subdirectly Irreducible Algebras

> [!definition] Definition 19.1.1: Subdirect product and subdirect embedding
> $A$ is a **subdirect product** of $(A_i)_{i\in I}$ if $A\le\prod_i A_i$ and every projection $\pi_i\restriction_A:A\to A_i$ is **surjective**. A **subdirect embedding** is an embedding $A\hookrightarrow\prod_i A_i$ with all projections surjective; equivalently a family of surjections $(\,A\twoheadrightarrow A_i\,)$ whose kernels intersect to the diagonal: $\bigcap_i\ker(\pi_i\restriction_A)=\Delta_A$.

> [!definition] Definition 19.1.2: Subdirectly irreducible algebra
> $A$ (nontrivial) is **subdirectly irreducible (SI)** if in every subdirect embedding $A\hookrightarrow\prod_i A_i$ some projection $\pi_i\restriction_A$ is an isomorphism; equivalently, the congruence lattice $\operatorname{Con}(A)$ has a **least nonzero element** (a **monolith** $\mu_A$), i.e. the intersection of all nondiagonal congruences is itself nondiagonal. **Simple** algebras (only $\Delta_A,\nabla_A$ as congruences) are SI.

> [!theorem] Theorem 19.1.3: Birkhoff's subdirect representation theorem
> Every algebra $A$ is (isomorphic to) a **subdirect product of subdirectly irreducible algebras**, each a quotient of $A$:
> $$
> A\ \hookrightarrow\ \prod_{i}\ A/\theta_i\qquad(\text{each }A/\theta_i\ \text{SI},\ \textstyle\bigcap_i\theta_i=\Delta_A).
> $$
> Consequently every variety $\mathcal V$ is determined by its subdirectly irreducible members: $\mathcal V=SP(\,\mathcal V_{\mathrm{SI}}\,)$, and to verify an identity in $\mathcal V$ it suffices to verify it in all SI members. SI algebras are the "primes" of the subdirect decomposition.

> [!example] Example 19.1.4: SI algebras in familiar varieties
> (i) In **Boolean algebras** the only SI (indeed simple) member is the two-element algebra $\mathbf 2$; hence $\mathsf{BA}=SP(\mathbf 2)$, recovering the base treatise's truth-value semantics as a structure theorem. (ii) In **distributive lattices** the only SI is the two-element chain. (iii) In **abelian groups** the SI members are the cyclic $p$-groups $\mathbb Z_{p^k}$ and the Prüfer groups $\mathbb Z_{p^\infty}$. (iv) In **vector spaces over a field $k$** the only SI is $k$ itself.

### 19.2. Ultraproducts and Łoś's Theorem

> [!definition] Definition 19.2.1: Filter, ultrafilter, ultraproduct
> A **filter** on a set $I$ is a nonempty $\mathcal F\subseteq\mathcal P(I)$ closed under supersets and finite intersections with $\varnothing\notin\mathcal F$; an **ultrafilter** is a maximal filter (for every $J\subseteq I$, exactly one of $J,I\setminus J$ is in $\mathcal F$). For algebras $(A_i)_{i\in I}$ and an ultrafilter $\mathcal U$, the **ultraproduct** $\prod_{\mathcal U}A_i$ is the quotient $\big(\prod_i A_i\big)/{\sim_{\mathcal U}}$ where $a\sim_{\mathcal U}b\iff\{i:a_i=b_i\}\in\mathcal U$ ("equal on a $\mathcal U$-large set"). The existence of nonprincipal ultrafilters uses the **Axiom of Choice**.

> [!theorem] Theorem 19.2.2: Łoś's theorem
> For any first-order formula $\varphi(x_1,\dots,x_n)$ and elements $[a^1],\dots,[a^n]$ of $\prod_{\mathcal U}A_i$,
> $$
> \prod_{\mathcal U}A_i\ \models\ \varphi\big([a^1],\dots,[a^n]\big)\quad\Longleftrightarrow\quad \{\,i\in I:\ A_i\models\varphi(a^1_i,\dots,a^n_i)\,\}\in\mathcal U.
> $$
> "A first-order property holds in the ultraproduct iff it holds on a $\mathcal U$-large set of factors." In particular ultraproducts preserve **all** first-order sentences true in $\mathcal U$-almost-all factors, hence preserve every identity and every quasi-identity.

> [!corollary] Corollary 19.2.3: Compactness via ultraproducts
> The **compactness theorem** of first-order logic follows: a set of sentences with every finite subset satisfiable has a model (an ultraproduct of the finite-subset models over a suitable ultrafilter). For universal algebra, the relevant consequence is that classes axiomatized by first-order sentences are closed under $P_{\!U}$, and the operator $P_{\!U}$ measures the gap between syntactic and "limit" behavior of an algebra class.

### 19.3. Quasivarieties

> [!definition] Definition 19.3.1: Quasi-identity and quasivariety
> A **quasi-identity** (strict universal Horn sentence) over $X$ has the form
> $$
> \Big(\bigwedge_{j=1}^{k} s_j\approx t_j\Big)\ \Rightarrow\ s\approx t,
> $$
> a finite conjunction of equations implying an equation (the case $k=0$ is an ordinary identity). A **quasivariety** is a class axiomatized by a set of quasi-identities. Quasivarieties include all varieties and are the natural setting for **cancellative**, **torsion-free**, and **embeddability** conditions, none of which is equational.

> [!theorem] Theorem 19.3.2: Mal'cev's quasivariety theorem
> A class $\mathcal K$ closed under isomorphism is a **quasivariety** iff it is closed under $S$, $P$, $P_{\!U}$, and contains the trivial algebra:
> $$
> \mathcal K\ \text{is a quasivariety}\quad\Longleftrightarrow\quad \mathcal K=SPP_{\!U}\,\mathcal K\ \text{(and }\mathcal K\ni\text{trivial)}.
> $$
> Equivalently $\mathcal K=ISP_{\!R}\mathcal K$ using reduced products. The smallest quasivariety containing $\mathcal K$ is $SPP_{\!U}\mathcal K$. This is the implicational counterpart of Birkhoff's HSP: quasivarieties drop closure under $H$ (homomorphic images) and add closure under ultraproducts.

> [!definition] Definition 19.3.3: Relatively free algebras and the lattice of quasivarieties
> Each quasivariety $\mathcal Q$ has **relatively free** algebras $\mathbf F_{\mathcal Q}(X)$, defined by the universal property relative to $\mathcal Q$ as in Construction 18.3.1 but using the least **relative congruence** ($\mathcal Q$-congruence) rather than the fully invariant one. The subquasivarieties of $\mathcal Q$ form a complete (algebraic) lattice $L_q(\mathcal Q)$, generally **larger and more complex** than the subvariety lattice, and dually isomorphic to the lattice of **relative congruences** on $\mathbf F_{\mathcal Q}(X_\omega)$.

> [!warning] Warning 19.3.4: Three closure profiles
> The three principal class types are distinguished exactly by their closure operators:
> $$
> \textbf{variety}=HSP\ (\text{equations});\quad \textbf{quasivariety}=SPP_{\!U}\ (\text{quasi-identities});\quad \textbf{elementary (axiomatic) class}=\text{closed under }\equiv\ \&\ P_{\!U}\ (\text{first-order}).
> $$
> A class can be a quasivariety but not a variety (e.g. **cancellative monoids**, **torsion-free abelian groups**, **integral domains** — not closed under homomorphic images), and a first-order class but not a quasivariety (e.g. **fields** — not closed under products). Misclassifying a class (assuming a quasivariety has free algebras with equational presentations, say) is a frequent error; the closure profile determines which structure theorems apply.

> [!example] Example 19.3.5: Cancellative semigroups
> The class of **cancellative semigroups** is defined by the quasi-identities $xz\approx yz\Rightarrow x\approx y$ and $zx\approx zy\Rightarrow x\approx y$ together with associativity. It is closed under $S,P,P_{\!U}$ but **not** under $H$ (a homomorphic image can fail cancellation), so it is a quasivariety that is not a variety. Its relatively free algebras exist but differ from the absolutely free semigroup quotients of the variety of all semigroups.

---

## 20. Clones, Lawvere Theories, and Finitary Monads

The base treatise identifies $\Omega$-algebras with Eilenberg–Moore algebras of the term monad and with $H_\Omega$-algebras. This part completes the "presentation-independent" theory of an algebraic structure by exhibiting **three equivalent descriptions of a variety that mention no signature at all**: the **clone** of term operations, the **Lawvere theory**, and the **finitary monad**. The signature and equations are a *presentation*; the clone/theory/monad is the *invariant*.

### 20.1. Term and Polynomial Operations; Clones

> [!definition] Definition 20.1.1: Term operation
> For an $\Omega$-algebra $A$ and a term $t\in T_\Omega(X_n)$ in variables $x_1,\dots,x_n$, the **term operation** $t^A:|A|^n\to|A|$ is $\bar a\mapsto\operatorname{ev}_{\bar a}(t)$ (evaluate $t$ with $x_i:=a_i$). The term operations of all arities form a set of finitary operations on $|A|$ closed under projections and composition.

> [!definition] Definition 20.1.2: Clone
> A **clone** on a set $S$ is a family $\mathcal C=(\mathcal C_n)_{n\in\mathbb N}$ with $\mathcal C_n\subseteq S^{(S^n)}$ (n-ary operations) such that: $\mathcal C$ contains all **projections** $\pi^n_i(\bar a)=a_i$; and $\mathcal C$ is closed under **superposition** (generalized composition) $ (g;h_1,\dots,h_m)(\bar a)=g(h_1(\bar a),\dots,h_m(\bar a))$. The **clone of $A$**, $\mathrm{Clo}(A)$, is the clone of term operations of $A$; it is the closure of the basic operations $\{f^A\}$ under projections and superposition.

> [!definition] Definition 20.1.3: Polynomial operations
> The **polynomial operations** of $A$ are the term operations of the algebra $A_{|A|}$ obtained by adjoining a constant for each element of $|A|$; equivalently term operations allowing parameters from $|A|$. $\mathrm{Pol}(A)\supseteq\mathrm{Clo}(A)$, and the polynomial clone governs the **congruence** structure (a relation is a congruence iff it is compatible with all polynomial operations, equivalently with all basic operations — base treatise Definition 1.4.1).

> [!definition] Definition 20.1.4: Abstract clone and the clone of a variety
> An **abstract clone** is a clone presented without reference to an underlying set: a family of "operation symbols of each arity" with formal projections and a formal superposition satisfying the clone identities (a cartesian operad / a single-sorted algebraic theory). The **clone of a variety $\mathcal V$** is $\mathrm{Clo}(\mathcal V):=\mathrm{Clo}(\mathbf F_{\mathcal V}(X_\omega))$, equivalently $\mathcal C_n=\mathbf F_{\mathcal V}(X_n)$ with superposition given by substitution: the $n$-ary clone elements are exactly the **$\mathcal V$-equivalence classes of $n$-variable terms**.

### 20.2. Lawvere Theories

> [!definition] Definition 20.2.1: Lawvere theory
> A **(single-sorted) Lawvere theory** is a small category $\mathcal T$ with objects the natural numbers $0,1,2,\dots$ such that each $n$ is the **$n$-fold categorical product** of $1$: $n\cong 1\times\cdots\times 1$, with chosen product projections. Morphisms $n\to 1$ are the **$n$-ary operations** of the theory; morphisms $n\to m$ are $m$-tuples of $n$-ary operations. Composition is superposition. The **theory of $\mathcal V$**, $\mathcal T_{\mathcal V}$, has $\operatorname{Hom}(n,1)=\mathbf F_{\mathcal V}(X_n)$ — the opposite of the category of finitely generated free $\mathcal V$-algebras.

> [!definition] Definition 20.2.2: Models of a Lawvere theory
> A **model** (algebra) of a Lawvere theory $\mathcal T$ in $\mathbf{Set}$ is a **finite-product-preserving functor** $M:\mathcal T\to\mathbf{Set}$. Then $M(1)$ is the carrier, $M(n)\cong M(1)^n$, and each operation $\omega:n\to1$ is interpreted as $M(\omega):M(1)^n\to M(1)$; functoriality and product-preservation force exactly the equational laws of $\mathcal T$. A **homomorphism** of models is a natural transformation.

> [!theorem] Theorem 20.2.3: Varieties are categories of theory-models
> For every variety $\mathcal V$ there is an equivalence of categories
> $$
> \mathcal V\ \simeq\ \mathbf{Mod}(\mathcal T_{\mathcal V},\mathbf{Set})\ =\ \mathbf{Prod}(\mathcal T_{\mathcal V},\mathbf{Set}),
> $$
> between $\mathcal V$ and the category of finite-product-preserving functors $\mathcal T_{\mathcal V}\to\mathbf{Set}$. Conversely every Lawvere theory arises as $\mathcal T_{\mathcal V}$ for a variety $\mathcal V$. The theory $\mathcal T_{\mathcal V}$ is a **signature- and presentation-free** encoding of $\mathcal V$: different signatures presenting the same variety yield isomorphic theories.

> [!remark] Remark 20.2.4: What the theory forgets and keeps
> $\mathcal T_{\mathcal V}$ remembers exactly the **clone** — all derived operations and all equations between them — and forgets the arbitrary choice of generating operations (the signature). Two varieties are **term-equivalent** (definitionally equivalent) iff their Lawvere theories are isomorphic, e.g. Boolean algebras presented with $\{\wedge,\neg\}$ versus $\{\vee,\to,\bot\}$ versus the Boolean-ring signature all share one theory. The Lawvere theory is the precise invariant separating a structure from its presentations — the structural-algebra analogue of the base treatise's "object vs presentation" discipline.

### 20.3. Finitary Monads and the Triangle of Equivalences

> [!definition] Definition 20.3.1: Finitary monad
> A monad $(T,\eta,\mu)$ on $\mathbf{Set}$ is **finitary** if $T$ preserves **filtered colimits**, equivalently if $T(X)=\bigcup\{T(X_0):X_0\subseteq X\ \text{finite}\}$ — every element of $T(X)$ uses only finitely many elements of $X$. The term monad $T_\Omega$ of a finitary signature, and its quotients by equational theories, are finitary; conversely finitary monads are exactly the "substitution structures" of finitary algebraic theories.

> [!theorem] Theorem 20.3.2: The triangle: varieties $\simeq$ Lawvere theories $\simeq$ finitary monads
> There are equivalences, all natural and mutually compatible,
> $$
> \{\text{varieties}\}\ \simeq\ \{\text{Lawvere theories}\}\ \simeq\ \{\text{finitary monads on }\mathbf{Set}\},
> $$
> under which a variety $\mathcal V$ corresponds to its theory $\mathcal T_{\mathcal V}$ and to the monad $T_{\mathcal V}$ with $T_{\mathcal V}(X)=|\mathbf F_{\mathcal V}(X)|$; the category $\mathcal V$ is recovered as $\mathbf{Mod}(\mathcal T_{\mathcal V})$ and as the Eilenberg–Moore category $\mathbf{Set}^{T_{\mathcal V}}$. The free–forgetful adjunction of the base treatise is the monadic adjunction of $T_{\mathcal V}$, and **Beck's monadicity theorem** certifies that the comparison functor $\mathcal V\to\mathbf{Set}^{T_{\mathcal V}}$ is an equivalence.

> [!remark] Remark 20.3.3: Beyond $\mathbf{Set}$ and beyond finitary
> Dropping "finitary" gives **infinitary** Lawvere theories / arbitrary monads (modeling, e.g., complete lattices, compact Hausdorff spaces as algebras for the ultrafilter monad). Replacing $\mathbf{Set}$ by another category gives **enriched** or **internal** algebraic theories. The base treatise's single-sorted finitary setting is one corner of this landscape; many-sorted theories (§2) correspond to Lawvere theories on $\mathbf{Set}^S$ and to finitary monads on $\mathbf{Set}^S$, and order-sorted/partial settings to suitably enriched or partial variants. The monad/theory abstraction is what makes these generalizations uniform.

> [!example] Example 20.3.4: The same monad, many presentations
> The monad $T$ with $T(X)=$ free monoid $X^{*}$ presents the variety of monoids; its Lawvere theory is the category of finitely generated free monoids (opposite), and its $\mathbf{Set}^T$ is $\mathsf{Mon}$. The list/free-monoid monad, the monoid Lawvere theory, and the variety $\mathsf{Mon}$ are three faces of one object, exactly as the term monad, the polynomial functor's free algebra, and $\mathbf{Alg}(\Omega)$ were three faces in the base treatise's §13.

---

## 21. Congruence Conditions and the Finite Basis Problem

The deepest structural invariants of a variety are properties of the **congruence lattices** of its members, captured by **Mal'cev conditions** — the existence of certain derived term operations satisfying certain identities. This part records the principal congruence conditions, Jónsson's lemma, and the finite basis problem, completing the structure theory begun in §§18–20.

### 21.1. Mal'cev Conditions

> [!definition] Definition 21.1.1: Congruence-permutable, -distributive, -modular varieties
> A variety $\mathcal V$ is:
> $$
> \textbf{congruence-permutable}\quad \text{if}\ \theta\circ\psi=\psi\circ\theta\ \text{for all}\ \theta,\psi\in\operatorname{Con}(A),\ A\in\mathcal V;
> $$
> $$
> \textbf{congruence-distributive}\quad \text{if}\ \operatorname{Con}(A)\ \text{is a distributive lattice for all}\ A\in\mathcal V;
> $$
> $$
> \textbf{congruence-modular}\quad \text{if}\ \operatorname{Con}(A)\ \text{is a modular lattice for all}\ A\in\mathcal V.
> $$
> Permutability implies modularity; distributivity implies modularity. These are properties of the whole variety, read off (by the theorems below) from the existence of special terms.

> [!theorem] Theorem 21.1.2: Mal'cev's permutability theorem
> $\mathcal V$ is congruence-permutable iff there is a ternary term $m(x,y,z)$ (a **Mal'cev term**) with
> $$
> \mathcal V\ \models\ m(x,x,y)\approx y\quad\text{and}\quad m(x,y,y)\approx x.
> $$
> Groups have $m(x,y,z)=x\cdot y^{-1}\cdot z$; rings, modules, quasigroups, and Heyting/Boolean algebras (via $x-y+z$ analogues) are congruence-permutable. The condition is the prototype of a **strong Mal'cev condition** (existence of finitely many terms satisfying finitely many identities).

> [!theorem] Theorem 21.1.3: Jónsson and Pixley terms
> (i) **Jónsson (congruence-distributivity):** $\mathcal V$ is congruence-distributive iff there are ternary terms $d_0,\dots,d_n$ (**Jónsson terms**) with $d_0(x,y,z)\approx x$, $d_n(x,y,z)\approx z$, $d_i(x,y,x)\approx x$, and the linking identities $d_i(x,x,z)\approx d_{i+1}(x,x,z)$ ($i$ even), $d_i(x,z,z)\approx d_{i+1}(x,z,z)$ ($i$ odd). (ii) **Pixley (arithmeticity = permutable + distributive):** $\mathcal V$ is **arithmetical** iff there is a single term $p(x,y,z)$ with $p(x,y,x)\approx x$, $p(x,y,y)\approx x$, $p(x,x,y)\approx y$. Lattices are congruence-distributive (via the lattice operations) but not permutable.

> [!remark] Remark 21.1.4: Mal'cev conditions as a classification axis
> A **Mal'cev condition** is a property of a variety expressible as "there exist terms satisfying these identities"; it is automatically preserved by term-equivalence and is therefore a property of the **Lawvere theory** (§20.2), not the presentation. Congruence permutability, distributivity, modularity, congruence $n$-permutability, and the existence of a **near-unanimity** or **Taylor term** stratify all varieties and are the entry point to **tame congruence theory** (the local structure theory of finite algebras) and to the algebraic approach to the **constraint satisfaction problem** (CSP) dichotomy, where the presence of a Taylor term separates tractable from $\mathsf{NP}$-complete CSPs.

### 21.2. Jónsson's Lemma and Subdirectly Irreducibles

> [!theorem] Theorem 21.2.1: Jónsson's Lemma
> If $\mathcal V=V(\mathcal K)$ is **congruence-distributive**, then every subdirectly irreducible algebra in $\mathcal V$ lies in $HSP_{\!U}(\mathcal K)$:
> $$
> \mathcal V_{\mathrm{SI}}\ \subseteq\ HSP_{\!U}(\mathcal K).
> $$
> In particular, if $\mathcal K$ is a finite set of finite algebras, the subdirectly irreducibles of $V(\mathcal K)$ are (up to isomorphism) among the homomorphic images of subalgebras of members of $\mathcal K$ (ultrapowers being harmless for finite $\mathcal K$), hence **finite and finitely many**. This gives strong control over congruence-distributive varieties generated by finite algebras.

> [!corollary] Corollary 21.2.2: Finite lattices of subvarieties
> If a congruence-distributive variety is generated by a finite algebra, it has only finitely many subdirectly irreducibles and a well-understood (often finite) lattice of subvarieties. This is why varieties of lattices and of many lattice-based structures (Heyting, Boolean, Kleene algebras) are far more tractable than the wild varieties of semigroups or groups, which are not congruence-distributive.

### 21.3. The Finite Basis Problem

> [!definition] Definition 21.3.1: Finitely based algebra/variety
> A variety $\mathcal V$ is **finitely based** if $\operatorname{Id}(\mathcal V)$ is generated, as a fully invariant congruence, by a **finite** set of identities. A finite algebra $A$ is **finitely based** if $V(A)$ is. Equivalently, $A$ is finitely based iff its equational theory is finitely axiomatizable.

> [!theorem] Theorem 21.3.2: Positive finite-basis results
> (i) **Birkhoff:** every variety of **finite type** that is generated by a finite algebra and is **congruence-distributive** is finitely based when... — more precisely, **Baker's Finite Basis Theorem:** every finite algebra of finite type generating a **congruence-distributive** variety is finitely based. (ii) **Oates–Powell:** every finite **group** is finitely based. (iii) **Lyndon:** every finite algebra with a **two-element** universe is finitely based. (iv) **McKenzie:** every finite algebra generating a **congruence-modular** variety with certain residual bounds is finitely based.

> [!theorem] Theorem 21.3.3: Negative results — Lyndon, Murskiı̆, McKenzie
> (i) **Lyndon:** there is a **seven-element** algebra that is **not** finitely based; **Murskiı̆** reduced this to a **three-element** algebra. (ii) **Tarski's finite basis problem** asked whether finite basedness of a finite algebra is **decidable**; **McKenzie** answered **no**: there is no algorithm deciding, given a finite algebra, whether it is finitely based. Finite basedness is therefore a genuinely undecidable structural property, the deepest negative result of the area.

> [!warning] Warning 21.3.4: Finiteness of the algebra does not imply finiteness of its theory
> A finite algebra can have a **non-finitely-axiomatizable** equational theory (Theorem 21.3.3): finitely many elements, infinitely many essentially different laws. This is the structure-theoretic analogue of the base treatise's separation of *existence* of a quotient from *decidability* of its word problem, and of §13's warning that a finitely based theory may admit no finite convergent rewrite system. Finiteness of data never automatically transfers to finiteness or effectivity of the induced theory.

---

## 22. Clones on Finite Sets and Functional Completeness

The clone $\mathrm{Clo}(A)$ (Definition 20.1.2) is the presentation-free invariant of an algebra. On a **finite** carrier the lattice of clones is a rich, classically studied object whose top is governed by **functional completeness** and whose global structure (for the two-element case) is **Post's lattice**. This part records the **Pol–Inv Galois connection** linking clones to relations, Rosenberg's classification of maximal clones, and the resulting completeness criteria — the finite-set face of §20.

### 22.1. The Pol–Inv Galois Connection

> [!definition] Definition 22.1.1: Preservation, polymorphisms, invariants
> Fix a finite set $S$. An $n$-ary operation $g:S^n\to S$ **preserves** an $m$-ary relation $R\subseteq S^m$ (is a **polymorphism** of $R$) if applying $g$ coordinatewise to any $n$ tuples in $R$ yields a tuple in $R$. For a set $\mathcal R$ of relations, $\mathrm{Pol}(\mathcal R)$ is the set of operations preserving all of them; for a set $F$ of operations, $\mathrm{Inv}(F)$ is the set of relations preserved by all of them.

> [!theorem] Theorem 22.1.2: The Galois connection and its closed objects
> On a finite set $S$, $(\mathrm{Pol},\mathrm{Inv})$ is a Galois connection between operations and relations whose closed sets are exactly:
> $$
> \mathrm{Pol}(\mathrm{Inv}(F))=\langle F\rangle\ (\text{the clone generated by }F);\qquad \mathrm{Inv}(\mathrm{Pol}(\mathcal R))=[\mathcal R]\ (\text{the relational clone / co-clone generated by }\mathcal R).
> $$
> Thus **clones** on a finite set are precisely the sets of operations of the form $\mathrm{Pol}(\mathcal R)$ — the operations preserving some set of relations. The clone of an algebra is the set of operations preserving all its **subuniverses, congruences, and definable relations** ($\mathrm{Inv}$ of its basic operations).

> [!remark] Remark 22.1.3: Clones as symmetry, relations as structure
> The Galois connection makes precise a duality already implicit in the base treatise: an algebra's **operations** and its **invariant relations** (subalgebras, congruences, compatible relations) determine each other. Term operations are exactly the operations compatible with all compatible relations; congruences are exactly the relations compatible with all operations. This is the finite-set, two-variable-free sharpening of "structure-preserving."

### 22.2. Maximal Clones and Functional Completeness

> [!definition] Definition 22.2.1: Functional completeness
> A set $F$ of operations on a finite $S$ is **functionally complete (Sheffer)** if $\langle F\rangle$ is the clone of **all** finitary operations on $S$, i.e. $\mathrm{Clo}=S^{(S^n)}$ for every $n$. An algebra $A$ on a finite carrier is **primal** if its basic operations are functionally complete (every operation on $|A|$ is a term operation).

> [!theorem] Theorem 22.2.2: Rosenberg's classification of maximal clones
> On a finite set $S$ ($|S|\ge2$) there are **finitely many maximal clones**, and Rosenberg's theorem classifies them as the polymorphism clones $\mathrm{Pol}(R)$ of six explicitly described families of relations $R$: (i) **bounded partial orders**; (ii) **prime-affine** (graphs of $p$-ary affine operations over $\mathbb Z_p$); (iii) **prime-permutation** relations (fixed-point-free permutations of prime order); (iv) **non-trivial equivalence relations**; (v) **central relations**; (vi) **regular $h$-ary relations**. A clone is contained in some maximal clone iff it is not the full clone.

> [!corollary] Corollary 22.2.3: Completeness criterion
> $F$ is functionally complete on $S$ iff $F$ is contained in **none** of the maximal clones of Theorem 22.2.2; equivalently, iff $F$ violates each of the six Rosenberg relation families. On the two-element set this specializes to **Post's criterion**: $F$ is complete iff it is not entirely contained in any of the five "Post classes" (monotone, affine, self-dual, $0$-preserving, $1$-preserving). The Sheffer stroke (NAND) and the Peirce arrow (NOR) are each singly complete.

> [!theorem] Theorem 22.2.4: Post's lattice
> The clones on the **two-element** set $\{0,1\}$ form a **countably infinite, completely described** lattice (**Post's lattice**), with each clone finitely generated and dual-atom structure given by the five maximal Post classes. In contrast, for $|S|\ge3$ the lattice of clones has the **cardinality of the continuum** and is not fully classifiable, although the maximal (Theorem 22.2.2) and minimal clones are known.

> [!warning] Warning 22.2.5: Finite carrier does not tame the clone lattice for $|S|\ge3$
> The complete description of Post's lattice is special to the two-element case. For three or more elements there are $2^{\aleph_0}$ clones, including continuum-many minimal-above-trivial and intricate intermediate structure; "list all clones" is impossible. The maximal clones (hence completeness) remain finite and decidable, but the global lattice is wild — a finite-set echo of the wildness of general variety lattices (Example 18.4.2).

> [!remark] Remark 22.2.6: Polymorphisms and computational complexity
> The Pol–Inv connection is the foundation of the **algebraic theory of constraint satisfaction**: the complexity of the CSP over a fixed finite relational template depends only on the **clone of polymorphisms** of the template, and the **Bulatov–Zhuk dichotomy theorem** states that the CSP is in $\mathsf P$ if the polymorphism clone contains a **Taylor term** (equivalently a weak near-unanimity term) and is $\mathsf{NP}$-complete otherwise. The structural invariants of §21.1 (Mal'cev conditions) thereby acquire a direct complexity-theoretic meaning, closing the loop between universal algebra and effective computation.

---

# Part VIII — Further Effective Methods

## 23. Congruence Closure and Ground Decision Procedures

The base treatise establishes that the word problem $s=_E t$ is undecidable in general but decidable when $E$ admits a convergent rewrite system. There is a large, practically central fragment it does not isolate: the **ground (uniform) word problem**, where the equations $E$ and the query are **variable-free** (or where variables are treated as uninterpreted constants). This fragment is **decidable in near-linear time** by **congruence closure**, the algorithm at the heart of $\mathsf{SMT}$ solvers and proof assistants.

### 23.1. The Ground Word Problem

> [!definition] Definition 23.1.1: Ground equational theory and the uniform word problem
> Let $\Sigma$ be a signature and $C$ a finite set of constants (and other ground subterms). A **ground equation** is a pair $a\approx b$ of ground terms. The **uniform word problem** is: given a **finite** set $E$ of ground equations and a ground query $s\approx t$, decide whether $E\models s\approx t$ (equivalently $s=_E t$, equivalently $(s,t)$ lies in the congruence on ground terms generated by $E$). Variables in a query may be treated as fresh constants, reducing the variable case with no axioms to this setting.

> [!theorem] Theorem 23.1.2: Decidability of the ground word problem
> The uniform word problem for ground equations over a finite signature is **decidable**. Unlike the general word problem (Novikov–Boone, undecidable), the ground case is tractable because no rule may be instantiated: the relevant congruence is generated by finitely many ground pairs closed under reflexivity, symmetry, transitivity, and the **congruence rule restricted to the finitely many subterms that occur**.

### 23.2. The Congruence Closure Algorithm

> [!definition] Definition 23.2.1: Subterm graph and congruence closure
> Let $G$ be the finite set of all subterms occurring in $E\cup\{s,t\}$ (the **term universe**, closed under subterms). The **congruence closure** of $E$ on $G$ is the least equivalence $\sim$ on $G$ containing $E$ and satisfying the **local congruence rule**:
> $$
> f(u_1,\dots,u_n),\ f(v_1,\dots,v_n)\in G\ \wedge\ u_i\sim v_i\ (\forall i)\ \Longrightarrow\ f(u_1,\dots,u_n)\sim f(v_1,\dots,v_n).
> $$
> Because $G$ is finite, $\sim$ is computed by fixpoint iteration; $E\models s\approx t\iff s\sim t$.

> [!construction] Construction 23.2.2: Union–find with congruence propagation
> Maintain a **union–find** structure over $G$ with classes, plus, for each class, the set of **parent** terms (terms having a member of the class as an immediate argument). Process each input equation $a\approx b$ by $\mathrm{union}(a,b)$; after each merge, **propagate**: for every pair of parents that have become congruent (equal head, argument-classes now equal), merge them too, cascading. Using union–find with path compression and a use-list of parents, the algorithm runs in $O(m\log m)$ (Downey–Sethi–Tarjan / Nelson–Oppen), essentially the cost of the term DAG.

> [!theorem] Theorem 23.2.3: Correctness and the e-graph
> The data structure of Construction 23.2.2 computes exactly the congruence closure $\sim$ (Definition 23.2.1), so membership queries $s\sim t$ are answered by comparing class representatives. The maintained structure — a term DAG quotiented by the running congruence — is the **e-graph (equivalence graph)** of modern solvers, supporting incremental assertion of equations, backtracking, and querying, and combining with other decision procedures by **Nelson–Oppen** equality sharing.

### 23.3. Scope, Combination, and Limits

> [!definition] Definition 23.3.1: Theory combination
> The **Nelson–Oppen** method decides the union of two **stably-infinite**, **signature-disjoint** decidable theories by congruence closure over the shared (equality) signature: each theory propagates **entailed equalities between shared constants** to the other until closure or contradiction. This lifts ground decidability of the equational fragment to combined theories (uninterpreted functions $+$ linear arithmetic $+$ arrays, etc.), the architecture of $\mathsf{SMT}$.

> [!warning] Warning 23.3.2: Ground decidability does not extend to the general word problem
> Congruence closure decides the **ground** word problem; it does **not** decide $s=_E t$ when $E$ contains **non-ground** equations (universally quantified laws), which is undecidable in general (Theorem 12.5.2 / base treatise). Solvers handle universal axioms by **instantiation heuristics** (e-matching), which are sound but incomplete. The sharp line is: **no variables in axioms** $\Rightarrow$ decidable in near-linear time; **variables in axioms** $\Rightarrow$ in general undecidable. Conflating the two — expecting congruence closure to discharge quantified lemmas — is the standard misuse.

> [!remark] Remark 23.3.3: Where this sits relative to rewriting
> Congruence closure is **completion specialized to ground equations**: on ground input, Knuth–Bendix completion (§13.4) always terminates and yields a convergent ground system, and congruence closure is the efficient direct realization of that fact (no orientation choices needed because every ground equation between distinct normal forms can be oriented by a fixed term order). The two effective theories — rewriting/completion (§13) and congruence closure (§23) — meet exactly here: the ground fragment where completion is guaranteed to succeed.

---

## 24. Anti-Unification

Unification (§12) finds a **most general common instance** of two terms; **anti-unification** (Plotkin, Reynolds) finds the dual: a **least general common generalization**. It computes the "common pattern" of two or more terms and is the basis of inductive generalization, analogy, and learning from examples.

> [!definition] Definition 24.1.1: Generalization and least general generalization
> A term $g$ is a **generalization** of $s$ and $t$ if there are substitutions $\sigma,\tau$ with $g\sigma=s$ and $g\tau=t$. A generalization $g$ is a **least general generalization (lgg)** (most specific generalization) if every generalization $g'$ of $s,t$ is more general than $g$ ($g'\lesssim g$): $g$ is $\le$-greatest in the subsumption preorder among common generalizations. The lgg is the **infimum** of $s,t$ in the subsumption order, dual to the mgu's role as supremum (Theorem 12.4.2).

> [!theorem] Theorem 24.1.2: Existence and uniqueness of the lgg
> In the free term algebra over a finitary signature, **every** finite set of terms has a **least general generalization**, **unique up to variable renaming**, and computable in polynomial time. Hence syntactic anti-unification, like syntactic unification, is **unitary** — but with no failure case: the lgg always exists (in the worst case it is a bare variable).

> [!construction] Construction 24.1.3: The anti-unification algorithm
> Compute the lgg of $s,t$ by simultaneous top-down traversal, maintaining a map from already-seen mismatched pairs to variables:
> $$
> \mathrm{lgg}(f(s_1,\dots,s_n),\,f(t_1,\dots,t_n))=f(\mathrm{lgg}(s_1,t_1),\dots,\mathrm{lgg}(s_n,t_n)),
> $$
> $$
> \mathrm{lgg}(s,t)=z_{(s,t)}\ \text{(a fresh variable, reused for repeated pairs)}\quad\text{when heads differ.}
> $$
> Reusing the same variable for identical mismatched pairs is what makes the result **least** general; a naive version using a fresh variable each time produces an over-general result.

> [!example] Example 24.1.4: lgg in practice
> $\mathrm{lgg}\big(f(a,g(a)),\,f(b,g(b))\big)=f(z,g(z))$ (one variable, because the $(a,b)$ mismatch recurs), whereas $\mathrm{lgg}\big(f(a,g(c)),\,f(b,g(d))\big)=f(z_1,g(z_2))$ (two variables). The first captures the structural invariant "second argument is $g$ of the first"; the second captures only "an $f$ of something and $g$ of something."

> [!warning] Warning 24.1.5: Equational anti-unification is hard and non-unitary
> Like $E$-unification, anti-unification **modulo an equational theory** loses the good properties of the syntactic case: the lgg modulo $E$ need not be unique, minimal complete sets of generalizations can be infinite, and computing them is undecidable for general $E$. The unitary, total, polynomial behavior (Theorem 24.1.2) is a feature of the **free** term algebra, paralleling the base treatise's recurring theme that freeness is exactly what makes the effective theory clean.

> [!remark] Remark 24.1.6: The subsumption lattice
> Together, unification and anti-unification make the set of terms (up to renaming) a **lattice** under the subsumption order: the **mgu** is the join (most general common instance, when it exists) and the **lgg** is the meet (least general common generalization, always existing). This lattice — the **subsumption lattice** — is the order-theoretic skeleton underlying both deductive (instance-finding) and inductive (pattern-finding) reasoning over the free algebra.

---

## 25. Higher-Order Unification and Rewriting

Parts II (binding) and IV (unification) meet in **higher-order unification**: solving equations between terms **with binders** ($\lambda$-terms modulo $\alpha\beta\eta$). This is the engine of higher-order theorem provers, type inference for polymorphic and dependent systems, and logical frameworks. Its theory is markedly worse-behaved than the first-order case — a precise measure of the cost of binding.

### 25.1. The Higher-Order Unification Problem

> [!definition] Definition 25.1.1: Higher-order unification
> Fix a simply-typed $\lambda$-calculus over base types, with terms taken modulo $\alpha\beta\eta$-equivalence (Part II; $\beta\eta$ as the equational theory of §8.3). A **higher-order unification problem** is a finite set of equations $\{s_i\stackrel{?}{=}t_i\}$ between typed $\lambda$-terms; a **solution** is a (capture-avoiding, type-preserving) substitution $\sigma$ of $\lambda$-terms for free variables with $s_i\sigma=_{\beta\eta}t_i\sigma$ for all $i$. Variables standing for functions may be instantiated by $\lambda$-abstractions.

> [!theorem] Theorem 25.1.2: Undecidability and the type hierarchy
> Higher-order unification is **undecidable** (Huet, Goldfarb): already **second-order** unification is undecidable (Goldfarb's reduction from Hilbert's tenth problem), and even with a single second-order variable. The problem is **infinitary** in unification type: solution sets need not have finite complete sets and need not have most general unifiers. **First-order** unification (the base case) is the unique fully tractable level.

> [!construction] Construction 25.1.3: Huet's preunification procedure
> **Huet's algorithm** searches for unifiers by alternating: **simplification** (decompose **rigid–rigid** equations, whose heads are constants/bound variables, exactly as first-order decomposition) and **projection/imitation** for **flexible–rigid** equations (head a free variable on one side): the flexible variable is guessed to either **imitate** the rigid head or **project** onto one of its arguments. The procedure is **complete** (enumerates a complete set of unifiers in the limit) but may not terminate; it postpones unsolvable **flex–flex** pairs as a **preunifier**, since flex–flex pairs are always solvable.

### 25.2. Patterns: the Decidable Fragment

> [!definition] Definition 25.2.1: Miller patterns
> A **(Miller) pattern** is a $\lambda$-term in which every free (meta)variable is applied only to **distinct bound variables** ($F\,x_1\cdots x_k$ with the $x_i$ distinct and bound). The **higher-order pattern unification** problem restricts all equations to patterns.

> [!theorem] Theorem 25.2.2: Decidability and unitarity of pattern unification
> Higher-order **pattern** unification is **decidable**, and a unifiable pattern problem has a **most general unifier** (it is **unitary**), computable by a Martelli–Montanari-style procedure extended with rules for the flexible cases (where the distinct-bound-variable restriction makes imitation/projection deterministic). Pattern unification recovers, inside the higher-order world, the good first-order behavior of Theorem 12.2.2 and is the fragment used in practice by logical frameworks and dependently-typed languages.

> [!warning] Warning 25.2.3: Leaving the pattern fragment loses all guarantees
> The decidability, unitarity, and termination of pattern unification depend on the **distinct-bound-variable** restriction. A single equation outside the fragment (a metavariable applied to a non-variable, or to a repeated variable) can reintroduce undecidability and infinitary solution sets. Implementations therefore either restrict to patterns by design, postpone non-pattern constraints, or fall back to incomplete heuristic search. The pattern restriction is the binding-aware analogue of the occurs-check and rule conditions: a syntactic discipline that buys back effectivity.

### 25.3. Higher-Order Rewriting

> [!definition] Definition 25.3.1: Higher-order rewrite system
> A **higher-order rewrite system (HRS)** (Nipkow's format / combinatory reduction systems) consists of rules $\ell\to r$ between typed $\lambda$-terms with metavariables, where matching is performed **modulo $\alpha\beta\eta$** (typically restricted so left sides are **patterns**, making matching decidable and unitary by Theorem 25.2.2). Rewriting fires a rule by pattern-matching a subterm and replacing it, with capture handled by the $\lambda$-calculus substitution.

> [!theorem] Theorem 25.3.2: Critical pairs and confluence for HRSs
> For pattern HRSs there is a higher-order **Critical Pair Lemma**: critical pairs are computed by higher-order pattern unification of left-hand sides, and a terminating pattern HRS is confluent iff all its critical pairs are joinable (Mayr–Nipkow), generalizing Theorem 13.3.2. Termination is established by higher-order reduction orderings (e.g. the higher-order recursive path ordering, HORPO). The first-order rewriting theory of §13 lifts to binding syntax **provided** one stays within the pattern fragment.

> [!remark] Remark 25.3.3: The price of binding, quantified
> Across §§24–25 the pattern is consistent: every clean first-order effective result — unitary unification, decidable matching, computable critical pairs, anti-unification — **survives the addition of binders only on a restricted (pattern) fragment**, and **fails (undecidable, infinitary) in general**. This is the algorithmic counterpart of Part II's structural result (binding syntax is not a free $\Omega$-algebra) and Part III's semantic result (first-order logic is not finitely equationally axiomatizable). The base treatise's clean term-syntax effectivity is precisely the **binder-free** corner of a landscape that degrades sharply, but controllably, as binding is admitted.

---

# Part IX — Unifying and Advanced Frameworks

## 26. Combinatory Algebra and the Elimination of Binding

Part II keeps binding as primitive and builds the apparatus ($\alpha$-equivalence, de Bruijn, nominal, presheaf) to manage it. There is a complementary strategy: **eliminate binding entirely**, replacing $\lambda$-abstraction by a finite set of constant **combinators** with ordinary (binder-free) equational axioms. This recovers a **genuine $\Omega$-algebra** (an equational variety) at the cost of an exotic combinatorial structure, and exposes precisely which equational laws the move preserves and which it breaks.

### 26.1. Applicative Structures and Combinatory Algebras

> [!definition] Definition 26.1.1: Applicative structure
> An **applicative structure** is a set $A$ with a single binary operation $\cdot:A\times A\to A$ (**application**), written by juxtaposition and associating to the **left**: $xyz:=(xy)z$. It is an $\Omega$-algebra for the signature with one binary symbol — no binders.

> [!definition] Definition 26.1.2: Combinatory algebra
> A **combinatory algebra** is an applicative structure with two distinguished constants $\mathsf K,\mathsf S$ satisfying the **combinator equations**
> $$
> \mathsf K\,x\,y\approx x,\qquad \mathsf S\,x\,y\,z\approx (x\,z)\,(y\,z).
> $$
> These are ordinary identities over the signature $\{\cdot,\mathsf K,\mathsf S\}$; combinatory algebras form a **variety** $\mathsf{CA}$ in the sense of §18. Derived combinators include the identity $\mathsf I:=\mathsf S\,\mathsf K\,\mathsf K$ (with $\mathsf I\,x\approx x$).

> [!theorem] Theorem 26.1.3: Combinatory completeness (bracket abstraction)
> In any combinatory algebra, for every term $t$ built from variables and elements there is a term $\lambda^{*}x.\,t$ **not containing $x$** with
> $$
> (\lambda^{*}x.\,t)\,a\ \approx\ t[x{:=}a]\qquad\text{for all }a,
> $$
> constructed by **bracket abstraction**: $\lambda^{*}x.\,x:=\mathsf I$; $\lambda^{*}x.\,t:=\mathsf K\,t$ if $x\notin\operatorname{var}(t)$; $\lambda^{*}x.\,(t\,u):=\mathsf S\,(\lambda^{*}x.\,t)\,(\lambda^{*}x.\,u)$. Thus $\mathsf K,\mathsf S$ suffice to **define abstraction**: every function expressible with $\lambda$ is expressible combinatorially. Binding is eliminable.

### 26.2. The Cost: Weak Equality and Lambda Algebras

> [!warning] Warning 26.2.1: Combinatory completeness is operational, not equational
> Bracket abstraction satisfies the $\beta$-like law $(\lambda^{*}x.\,t)a\approx t[x{:=}a]$ **only for application to arguments**, not as a congruence: $\lambda^{*}x.\,t$ is **not** a well-behaved binder up to the combinator equations. In particular $\lambda^{*}$ does **not** validate the $\xi$-rule ("$t\approx u\Rightarrow\lambda^{*}x.\,t\approx\lambda^{*}x.\,u$"), so the combinatory equational theory is **weaker** than $\lambda$-calculus $\beta$-equality. Combinatory **completeness** (definability of abstraction) and combinatory **equality** capturing $\lambda\beta$ are different claims; the second fails.

> [!definition] Definition 26.2.2: Lambda algebras and lambda models
> A **lambda algebra** is a combinatory algebra additionally satisfying the finitely many **Curry axioms** that force bracket abstraction to model $\lambda\beta$-conversion (the equations making the two translations between combinators and $\lambda$-terms mutually inverse modulo the theory). A **lambda model** further satisfies the **weak extensionality** (Meyer–Scott) axiom internalizing the $\xi$-rule. These successive strengthenings measure exactly the gap between combinatory and $\lambda$-equational reasoning.

> [!theorem] Theorem 26.2.3: Algebraic status of the $\lambda$-calculus
> The $\lambda\beta$-calculus is **algebraizable** as the variety of **lambda algebras** (equivalently, $\lambda\beta$ is the equational theory of lambda algebras), and $\lambda\beta\eta$ as a stronger variety. Hence the untyped $\lambda$-calculus, unlike first-order logic (§10, Part III), **does** admit a binder-free equational presentation — but only via the indirect combinatory encoding, and the naive equational treatment "$\lambda$ as an operation symbol with $\beta$ as an identity" is **unsound** (it lacks the $\xi$/extensionality control). This is the binding-elimination analogue of cylindric algebra's quantifier-algebraization.

> [!remark] Remark 26.2.4: Two routes through the binding obstruction
> The companion now records **three** responses to "binders are not operation symbols": (i) **manage** binding with proper syntax (Part II); (ii) **re-algebraize** quantifier semantics with infinite-dimensional operators (Part III); (iii) **eliminate** binding via combinators, landing in an honest finitary variety (this section). The third is available for the $\lambda$-calculus (a calculus of functions) but **not** for first-order logic (where the quantifier is not a function on truth values), which is exactly why Part III needs infinite dimension while §26 needs only two constants. The applicability boundary of binding-elimination is itself informative.

---

## 27. Rewriting Logic and Membership Equational Logic

The frameworks of Part I (sorts, subsorts, partiality) and Part IV (rewriting) are unified and extended by two logics designed as **executable specification** formalisms: **membership equational logic (MEL)**, which subsumes many-sorted, order-sorted, and partial equational logic; and **rewriting logic (RWL)**, which adds **non-equational, directed** transitions to model concurrency and change. Together they are the logical basis of the Maude system.

### 27.1. Membership Equational Logic

> [!definition] Definition 27.1.1: Membership signature and atomic sentences
> A **membership signature** has a set $K$ of **kinds**, operation symbols typed by kinds, and a set $S$ of **sorts** each assigned to a kind. The **atomic sentences** are **equations** $t\approx t'$ (between terms of the same kind) and **memberships** $t:s$ ("$t$ has sort $s$"). Sorts thus become **unary predicates** on kinds rather than primitive carriers — a uniform treatment of typing.

> [!definition] Definition 27.1.2: Conditional axioms of MEL
> The axioms of MEL are **conditional**:
> $$
> \Big(\bigwedge_i u_i\approx v_i\ \wedge\ \bigwedge_j w_j:s_j\Big)\ \Rightarrow\ t\approx t'\ \ \text{or}\ \ t:s,
> $$
> a Horn theory over equations and memberships. Sort assignment, subsort inclusion ($x:s\Rightarrow x:s'$), and partiality (a term has a sort only when "defined") are all expressed by such clauses.

> [!theorem] Theorem 27.1.3: MEL subsumes the Part I frameworks
> Many-sorted, order-sorted, and partial equational specifications all translate **conservatively** into membership equational logic: sorts become membership predicates, subsorts become Horn implications between them, and partial operations become operations whose result has a sort only under definedness conditions. MEL has **initial models** (constructed as quotients of a term algebra by the least congruence-plus-membership relation satisfying the axioms) and a **sound and complete** deduction system, so the entire Part I apparatus is a fragment of one logic.

> [!remark] Remark 27.1.4: Why predicates beat carriers
> Treating sorts as predicates on kinds (rather than as primitive disjoint carriers) avoids the empty-carrier anomaly (Warning 2.6.3) uniformly, gives a single notion of term over a kind, and makes subsorting and partiality definitionally expressible instead of structurally built-in. MEL is the "carrier-light" reformulation in which all of Part I's variations are conditional axioms over a common term algebra.

### 27.2. Rewriting Logic

> [!definition] Definition 27.2.1: Rewrite theory
> A **rewrite theory** is $\mathcal R=(\Sigma,E,R)$ where $(\Sigma,E)$ is a (membership) equational theory and $R$ is a set of **rewrite rules** $\ell\to r$ (possibly conditional). Crucially, rules in $R$ are **not** equations: they are read as **one-directional transitions** modulo the equations $E$. A model is a category-like structure where objects are $E$-equivalence classes (states) and morphisms are **proofs of rewrites** (transitions).

> [!definition] Definition 27.2.2: Deduction and the two layers
> Rewriting-logic deduction derives sequents $t\to t'$ by reflexivity, transitivity, **congruence** (rewrite in context), and **replacement** (apply a rule under a substitution), all **modulo $E$** (rewrite up to equational equality of states). The **equational layer $E$** specifies the **static** data structure (what counts as the same state); the **rule layer $R$** specifies **dynamic** change (which states transition to which). Equations are symmetric and confluent-by-intent; rules are directed and need not be confluent.

> [!warning] Warning 27.2.3: Equations and rules must not be conflated
> The defining discipline of rewriting logic is the **strict separation** of $E$ (equality, symmetric, $\leftrightarrow$) from $R$ (transition, directed, $\to$, irreversible). Treating a rule as an equation collapses distinct concurrent states; treating an equation as a rule imposes spurious directionality on data. This is the base treatise's syntactic-vs-semantic distinction extended by a third register: **identity of states** ($E$) versus **evolution of states** ($R$). Concurrency, nondeterminism, and time live in $R$; data representation lives in $E$.

> [!remark] Remark 27.2.4: Relation to the base architecture
> Rewriting logic factors the base treatise's single equational congruence into two: the **kernel of evaluation** becomes the equational part $E$ (still a congruence, base treatise §5), while a **non-symmetric** relation $R$ is layered on top to model computation as deduction. The free-algebra/quotient picture supplies the state space $\mathbf T_\Sigma(X)/{=_E}$; rewriting logic adds a proof-relevant transition structure over it — the directed, coalgebraic-flavored counterpart (§17) of the symmetric equational theory.

---

## 28. Coalgebraic Modal Logic and Algebra–Coalgebra Duality

Part VI develops coalgebra as the dual of the base treatise's initial-algebra theory; Part III algebraizes logic with cylindric algebras. The two threads meet in **modal logic**, whose semantics is **coalgebraic** (transition systems) and whose algebra is **Boolean algebras with operators**, the two related by a **Stone-type duality**. This section records that meeting point.

### 28.1. Modal Algebras

> [!definition] Definition 28.1.1: Boolean algebra with operators; modal algebra
> A **modal algebra** is a Boolean algebra $(B,+,\cdot,-,0,1)$ with a unary operator $\Diamond:B\to B$ that is **normal and additive**: $\Diamond 0=0$ and $\Diamond(x+y)=\Diamond x+\Diamond y$ (dually $\Box=-\Diamond-$ preserves $1$ and meets). Modal algebras form a **variety** (equationally axiomatized), and stronger modal logics (T, S4, S5, K4, …) are subvarieties cut out by further equations ($\Diamond$ idempotency, increasingness, etc.). This is the algebraic semantics of modal logic, an instance of §18.

> [!definition] Definition 28.1.2: Kripke frames as coalgebras
> A **Kripke frame** is a set $W$ of worlds with an accessibility relation $\mathrel{\to}\subseteq W\times W$, i.e. a coalgebra $W\to\mathcal P(W)$ for the **powerset functor** $\mathcal P$. A **model** adds a valuation. The modal operators are interpreted by $\Diamond$ = "true at some successor," $\Box$ = "true at all successors" — operations defined **via the coalgebra structure**. Modal logic is thus the logic of $\mathcal P$-coalgebras.

### 28.2. Duality

> [!theorem] Theorem 28.2.1: Jónsson–Tarski duality
> The complex-algebra and ultrafilter-frame constructions form a **duality** between modal algebras and (descriptive general) Kripke frames, extending **Stone duality** between Boolean algebras and Stone spaces:
> $$
> \text{modal algebras}\ \xleftrightarrow{\ \text{dual equivalence}\ }\ \text{descriptive general frames},
> $$
> with the **algebra** side built from the **coalgebra** (frame) by taking the powerset Boolean algebra with $\Diamond$ the relational image, and the frame recovered from the algebra via its ultrafilters and the canonical relation. Validity of a modal formula on a frame corresponds to an equation holding in its complex algebra.

> [!theorem] Theorem 28.2.2: Coalgebraic modal logic (general functor)
> For a broad class of $\mathbf{Set}$-endofunctors $H$ (replacing $\mathcal P$), one obtains a **coalgebraic modal logic** whose models are $H$-coalgebras (§17), whose modalities are given by **predicate liftings** for $H$, and which is **sound and complete**, **expressive** (modally distinguishes non-bisimilar states up to behavioral equivalence), and dual to a variety of **$H$-modal algebras**. The base treatise's signature functor $H_\Omega$, the powerset functor, distribution functors (probabilistic logic), and others all instantiate this scheme. Bisimulation (Definition 17.3.1) is exactly the logical indistinguishability relation (Hennessy–Milner property).

> [!remark] Remark 28.2.3: The square of dualities
> The companion now exhibits a coherent square: **syntax algebra** (base treatise, initial $H_\Omega$-algebra) and **behavior coalgebra** (Part VI, final $H$-coalgebra) on one axis; **algebraic semantics** (modal/cylindric algebras, varieties) and **relational/coalgebraic semantics** (frames, transition systems) on the other; with **Stone/Jónsson–Tarski duality** linking the algebraic and coalgebraic sides, and **bisimulation/coinduction** (Part VI) matching **logical equivalence** (Part III/§28). This is the mature, unified picture toward which the base treatise's "logic as a specialization" and the companion's coalgebraic dual both point.

---

## 29. Institutions and Specification

The companion has presented many logical systems — single- and many-sorted equational logic, order-sorted, partial (MEL), first-order, modal, rewriting logic. **Institution theory** (Goguen–Burstall) is the abstract model theory that treats "a logical system" itself as a mathematical object, capturing exactly the structure needed for **modular specification** (signature changes, structuring, parameterization) **independently of the particular logic**. It is the meta-level synthesis of Parts I–III and VII.

### 29.1. The Definition of an Institution

> [!definition] Definition 29.1.1: Institution
> An **institution** consists of: a category $\mathbf{Sign}$ of **signatures**; a functor $\mathrm{Sen}:\mathbf{Sign}\to\mathbf{Set}$ giving, for each signature $\Sigma$, its set of **sentences** and, for each signature morphism, a **sentence-translation** map; a functor $\mathrm{Mod}:\mathbf{Sign}^{\mathrm{op}}\to\mathbf{Cat}$ giving the **category of models** and a **model-reduction** functor for each signature morphism; and, for each $\Sigma$, a **satisfaction relation** $\models_\Sigma\,\subseteq|\mathrm{Mod}(\Sigma)|\times\mathrm{Sen}(\Sigma)$.

> [!definition] Definition 29.1.2: The satisfaction condition
> The data must obey the **satisfaction condition**: for every signature morphism $\varphi:\Sigma\to\Sigma'$, model $M'$ of $\Sigma'$, and sentence $\psi$ of $\Sigma$,
> $$
> M'\ \models_{\Sigma'}\ \mathrm{Sen}(\varphi)(\psi)\quad\Longleftrightarrow\quad \mathrm{Mod}(\varphi)(M')\ \models_{\Sigma}\ \psi,
> $$
> "truth is invariant under change of notation": translating a sentence along $\varphi$ and checking it in $M'$ is the same as reducing $M'$ along $\varphi$ and checking the original sentence. This single axiom is the abstract essence of "semantics respects signature morphisms."

> [!example] Example 29.1.3: Equational logic as an institution
> Single-sorted equational logic is an institution: $\mathbf{Sign}=$ signatures and signature morphisms; $\mathrm{Sen}(\Omega)=$ equations over a fixed variable set; $\mathrm{Mod}(\Omega)=\mathbf{Alg}(\Omega)$ with reducts (base treatise Definition 1.3.3) as model reduction; $\models$ as identity satisfaction. Many-sorted (§2), order-sorted (§3), partial/MEL (§4, §27), first-order, and modal (§28) logics are each institutions; the satisfaction condition is, in each case, the reduct-translation compatibility of the corresponding logic.

### 29.2. Structured Specification

> [!definition] Definition 29.2.1: Specification-building operations
> Over **any** institution, specifications are built and combined by institution-independent operations: **union** (combine sentence sets over a pushout of signatures), **translation/renaming** (along a signature morphism), **hiding** (reduct along a morphism, exporting a sub-signature), and **parameterization** (a specification with a formal parameter signature, instantiated by pushout). The semantics of each is defined purely from $\mathrm{Sen}$, $\mathrm{Mod}$, and the satisfaction condition.

> [!theorem] Theorem 29.2.2: Institution-independence of structuring
> The soundness of the structuring operations — that a structured specification denotes a well-defined model class, that translation preserves consequence, and that parameterized specifications instantiate correctly by **amalgamation** (a pushout of signatures lifts to a pullback of model categories) — holds in **any** institution satisfying mild conditions (existence of signature pushouts, the amalgamation property). Hence the entire machinery of modular specification is developed **once**, abstractly, and applies to every logic of Parts I–III, VII, and §§27–28 simultaneously.

> [!warning] Warning 29.2.3: Amalgamation can fail
> The correctness of parameterization and module composition rests on the **amalgamation property** (model amalgamation along signature pushouts). It holds for many-sorted equational logic and many others but **can fail** (e.g. in some partial or constraint logics, and when signature morphisms are not injective on sorts). Where amalgamation fails, parameterized specification loses its expected semantics. Amalgamation is to institutions what the congruence property is to quotients (base treatise Warning 1.7.7) and what the satisfaction condition is to translation: the compatibility hypothesis without which the construction is ill-defined.

> [!remark] Remark 29.2.4: The top of the abstraction tower
> Institutions sit above every concrete logic in this companion: where §20 abstracts a single variety to its Lawvere theory/monad (forgetting the signature), institutions abstract an entire **logical system** to its signature/sentence/model/satisfaction data (forgetting the particular syntax and semantics). The base treatise's recurring discipline — separate an object from its presentations, identify the universal property, work morphism-invariantly — is here applied to logics themselves: a logic is characterized by how its sentences and models transform under signature change, exactly as an algebra was characterized by how maps out of it behave.

---

# Part X — Data Types, Domains, and Explicit Computation

## 30. W-Types, Containers, and Dependent Polynomial Functors

The base treatise's signature functor $H_\Omega(Y)=\coprod_{f\in\Omega}Y^{\operatorname{ar}(f)}$ presents a finitary, untyped, set-valued polynomial. This part records its standard generalizations — **containers** (the data-type form of a signature), **W-types** (the initial algebra of a container, the type-theoretic term algebra), and **dependent polynomial functors** (allowing sorts/indices to vary along the construction). These are the type-theoretic continuation of the base treatise's §13.3, and the precise framework in which "the inductive data type generated by constructors" is the free/initial algebra.

### 30.1. Containers and Polynomial Functors

> [!definition] Definition 30.1.1: Container
> A **container** (one-variable) is a pair $(\mathsf{Sh},\mathsf{Pos})$ with $\mathsf{Sh}$ a set of **shapes** and $\mathsf{Pos}:\mathsf{Sh}\to\mathbf{Set}$ a family of **position** sets, $\mathsf{Pos}(s)$ being the positions of shape $s$. Its **extension** is the endofunctor
> $$
> \llbracket\mathsf{Sh}\triangleleft\mathsf{Pos}\rrbracket(Y)\ :=\ \coprod_{s\in\mathsf{Sh}}\ Y^{\mathsf{Pos}(s)}.
> $$
> A finitary signature $\Omega$ is the container with $\mathsf{Sh}=\Omega$ and $\mathsf{Pos}(f)=\{1,\dots,\operatorname{ar}(f)\}$, recovering $H_\Omega$; allowing $\mathsf{Pos}(s)$ infinite gives **infinitary** signatures.

> [!definition] Definition 30.1.2: Polynomial functor (general)
> A **polynomial** is a diagram $I\xleftarrow{\,s\,}B\xrightarrow{\,f\,}A\xrightarrow{\,t\,}J$ in $\mathbf{Set}$ (or a locally cartesian closed category); its associated **dependent polynomial functor** $P:\mathbf{Set}/I\to\mathbf{Set}/J$ is the composite $\Sigma_t\circ\Pi_f\circ\Delta_s$ of reindexing, dependent product, and dependent sum. The one-object case ($I=J=1$) is a container; the case $I=J=S$ with $\Delta,\Sigma$ over $S$ is the **sorted** signature functor $H_\Sigma$ of §2. Dependent polynomial functors are closed under composition, sums, and products.

### 30.2. W-Types

> [!definition] Definition 30.2.1: W-type
> Given a container $(\mathsf{Sh},\mathsf{Pos})$, the **W-type** $\mathsf W_{s:\mathsf{Sh}}\,\mathsf{Pos}(s)$ is the **initial algebra** of $\llbracket\mathsf{Sh}\triangleleft\mathsf{Pos}\rrbracket$: the set of **well-founded trees** whose nodes are labeled by shapes $s$ with exactly $\mathsf{Pos}(s)$ children, one per position. Its single constructor is $\mathsf{sup}:\coprod_{s}\big(\mathsf{Pos}(s)\to\mathsf W\big)\to\mathsf W$, "a shape together with a child for each position." $\mathsf W$ is exactly the ground term algebra $\mathbf T_\Omega(\varnothing)$ when the container is a finitary signature.

> [!theorem] Theorem 30.2.2: W-types as initial algebras; induction and recursion
> $\mathsf W$ carries the structure of the **initial** $\llbracket\mathsf{Sh}\triangleleft\mathsf{Pos}\rrbracket$-algebra: for every algebra $(C,\theta)$ there is a unique homomorphism $\mathsf W\to C$ (**recursion**), and the corresponding **induction principle** holds (a predicate closed under $\mathsf{sup}$ holds of all trees). This is the base treatise's structural recursion/induction (its §6, §13.3) stated for arbitrary (possibly infinitary) containers; in dependent type theory, W-types are the single primitive from which all well-founded inductive types ($\mathbb N$, lists, finite and countably-branching trees, ordinals up to $\varepsilon_0$, syntax of an algebraic theory) are derived.

> [!remark] Remark 30.2.3: M-types as the dual
> Dually, the **M-type** is the **final coalgebra** of the container — the possibly **non-well-founded** trees — i.e. the infinitary-signature version of §17's $\nu H_\Omega$. The pair (W-type, M-type) is the type-theoretic name for the (initial algebra, final coalgebra) pair of a polynomial functor: least vs greatest fixpoint, induction vs coinduction, finite data vs infinite behavior. The companion's Part VI and this section are two presentations — coalgebraic and type-theoretic — of one duality.

### 30.3. Indexed and Dependent Inductive Types

> [!definition] Definition 30.3.1: Indexed container / inductive family
> An **indexed container** over an index set $I$ assigns to each $i\in I$ a set of shapes and to each shape a family of positions tagged by indices, yielding a dependent polynomial functor on $\mathbf{Set}/I$. Its initial algebra is an **inductive family** $(D_i)_{i\in I}$ — the dependent generalization of the sorted term algebra (§2.3) in which the index/sort of a subterm may **depend on data**, not merely on a fixed signature profile.

> [!example] Example 30.3.2: Length-indexed vectors and typed syntax
> (i) **Vectors** $\mathrm{Vec}(A,n)$ (lists of length $n$) form an inductive family indexed by $n\in\mathbb N$, with constructors $\mathrm{nil}:\mathrm{Vec}(A,0)$ and $\mathrm{cons}:A\times\mathrm{Vec}(A,n)\to\mathrm{Vec}(A,n+1)$. (ii) **Intrinsically typed syntax** of a typed calculus is an inductive family indexed by (context, type), so that only well-typed terms are representable; here the dependent-polynomial framework simultaneously handles binding (Part II, via the de Bruijn presheaf) and typing (indexing), unifying the two refinements.

> [!warning] Warning 30.3.3: Strict positivity is required for initiality
> A dependent inductive definition has an initial algebra (W/indexed-W) **only if the constructors are strictly positive** — the type being defined occurs only in **strictly positive** positions of constructor arguments (never to the left of an arrow, cf. Warning 8.3.3 on HOAS negative occurrences). A non-strictly-positive "definition" (e.g. a constructor taking $(D\to D)$) generally has **no** initial algebra and admits **no** induction principle; it may even be inconsistent. Strict positivity is the container-level form of the base treatise's requirement that constructors be genuine operations of a signature.

---

## 31. Initial-Algebra Semantics of Abstract Data Types

The base treatise constructs the free/initial algebra and the presented algebra $\langle X\mid E\rangle$; the **algebraic specification** of data types (ADJ group, Goguen–Thatcher–Wagner) applies this directly: the **meaning of a data-type specification is its initial algebra**. This part records the principle and its two governing slogans — **"no junk"** and **"no confusion"** — which are exactly generatedness and the kernel condition of the base treatise, read as design criteria.

### 31.1. Specifications and Their Initial Semantics

> [!definition] Definition 31.1.1: Algebraic specification
> An **algebraic specification** is a presentation $\mathrm{Spec}=(\Sigma,E)$: a (many-sorted, §2) signature $\Sigma$ of **constructors and operations** together with a set $E$ of equations (or conditional equations / MEL axioms, §27). Its **model class** is $\mathrm{Mod}(\Sigma,E)$, the algebras satisfying $E$; its **initial semantics** is the (up-to-isomorphism unique) **initial** model $\mathbf I_{\mathrm{Spec}}$.

> [!theorem] Theorem 31.1.2: Existence and form of the initial model
> Every algebraic specification $(\Sigma,E)$ has an **initial model**, namely the ground-term quotient
> $$
> \mathbf I_{\mathrm{Spec}}\ \cong\ \mathbf T_\Sigma(\varnothing)\big/\theta_E,
> $$
> with $\theta_E$ the congruence generated by $E$ on ground terms. There is a unique homomorphism from $\mathbf I_{\mathrm{Spec}}$ to every model (initiality), so $\mathbf I_{\mathrm{Spec}}$ is the **standard meaning** of the data type. This is the base treatise's quotient/presentation theorem (its §5.5, §7) used as a **definition** of semantics.

### 31.2. No Junk, No Confusion

> [!definition] Definition 31.2.1: No junk; no confusion
> Relative to a chosen set of **constructor** symbols $\mathcal C\subseteq\Sigma$, a model $A$ has:
> $$
> \textbf{no junk}\quad \text{if } A \text{ is generated by the constructors: } A=\langle\varnothing\rangle_A \text{ using } \mathcal C \text{ (every element is a constructor term value);}
> $$
> $$
> \textbf{no confusion}\quad \text{if distinct constructor ground terms denote distinct elements, except as forced by } E.
> $$
> The initial model is characterized by satisfying **both**: it is generated (no junk) and identifies ground terms **only** when $E$ requires (no confusion).

> [!theorem] Theorem 31.2.2: Initiality = no junk + no confusion
> A model $A\in\mathrm{Mod}(\Sigma,E)$ is **initial** iff it has **no junk** and **no confusion**:
> $$
> \textbf{no junk}\ \equiv\ \text{the unique homomorphism } \mathbf T_\Sigma(\varnothing)\to A \text{ is surjective (generatedness, base treatise §5.3);}
> $$
> $$
> \textbf{no confusion}\ \equiv\ \text{its kernel is exactly } \theta_E \text{ (no identifications beyond } E\text{, base treatise §5.4–5.5).}
> $$
> Thus the design slogans are precisely the base treatise's **freeness = generatedness + injectivity** specialized to ground terms modulo $E$: initiality is "as free as $E$ allows."

> [!warning] Warning 31.2.3: Initial vs loose vs final semantics
> Initial semantics ("no junk, no confusion") is one of three standard choices. **Loose semantics** takes the **whole** model class $\mathrm{Mod}(\Sigma,E)$ (admitting junk and confusion), appropriate for **requirements** where many implementations are acceptable. **Final (terminal) semantics** maximally **confuses** (identifies all elements not observably distinguishable), appropriate for **behavioral/observational** types (states distinguished only by observations — the coalgebraic view, §17). Choosing initial semantics for an observational type wrongly forbids valid implementations that differ on unobservable internals; choosing final semantics for a constructor type wrongly collapses distinct data. The semantics must match whether the type is **data** (initial) or **behavior** (final).

> [!remark] Remark 31.2.4: Sufficient completeness and protection
> For a specification with **constructors** $\mathcal C$ and **defined operations** $\Sigma\setminus\mathcal C$, **sufficient completeness** requires every defined operation applied to constructor terms to be provably equal to a constructor term (no junk at defined sorts), and **consistency/protection** requires the operations not to collapse the constructor data (no confusion among constructors). These are the proof obligations ensuring the initial model is the intended data type; they are checked by ground confluence/termination of the equations oriented as a TRS (§13) — the point where initial-algebra semantics and effective rewriting meet.

---

## 32. Continuous Algebras, Domains, and Denotational Fixpoints

§16.3 introduced continuous $\Omega$-algebras as the order-theoretic completion supporting recursion through $\bot$. This part develops the surrounding **domain theory** — the order-theoretic semantics of recursive definitions — making precise how non-terminating and infinite computations receive meanings as **least fixed points**, the denotational counterpart of the operational rewriting of §13.

### 32.1. Complete Partial Orders and Continuity

> [!definition] Definition 32.1.1: CPO and continuous map
> A **(pointed) complete partial order (CPO)** is a poset $(D,\sqsubseteq)$ with a least element $\bot$ in which every **directed** subset (every finite subset has an upper bound in the set) has a supremum $\bigsqcup$. A map $f:D\to E$ is **monotone** if order-preserving and **(Scott-)continuous** if it preserves directed suprema: $f(\bigsqcup S)=\bigsqcup f[S]$ for directed $S$. Continuous maps are monotone; continuity is the order-theoretic form of "determined by finite approximations."

> [!theorem] Theorem 32.1.2: Kleene fixed-point theorem
> Every Scott-continuous self-map $f:D\to D$ on a pointed CPO has a **least fixed point**
> $$
> \operatorname{lfp}(f)\ =\ \bigsqcup_{n\in\mathbb N} f^n(\bot)\ =\ \bigsqcup\,(\,\bot\sqsubseteq f(\bot)\sqsubseteq f(f(\bot))\sqsubseteq\cdots\,),
> $$
> the supremum of the ascending chain of finite approximations. This is the meaning of a **recursive definition** $x=f(x)$: not a syntactic unfolding but the limit of its finite approximants, defined even when no finite unfolding terminates.

### 32.2. Denotational Semantics of Recursion

> [!construction] Construction 32.2.1: Denotation of a recursive program
> Interpret types as CPOs and a recursive definition $F=\Phi(F)$ (where $\Phi$ is continuous in the function-space CPO, itself a CPO under the pointwise order with continuous functions) by $\llbracket F\rrbracket:=\operatorname{lfp}(\Phi)=\bigsqcup_n\Phi^n(\bot)$ (Theorem 32.1.2). Non-termination on an input $a$ is denoted by $\llbracket F\rrbracket(a)=\bot$; partial and infinite results are directed suprema in the completed term algebra (§16.2). The continuous term algebra (Theorem 16.3.2) is the free such interpretation domain.

> [!theorem] Theorem 32.2.2: Adequacy and full abstraction (schematic)
> For a typed functional language with denotational semantics $\llbracket-\rrbracket$ into domains and operational semantics by rewriting (§13), **computational adequacy** holds: a program **terminates operationally** iff its **denotation is $\ne\bot$** (at ground type, equals the computed value). The stronger **full abstraction** property — operational (observational) equivalence coincides with equality of denotations — is delicate and **fails** for the naive domain model of sequential higher-order languages (the **parallel-or** problem), repaired only by refined models (stable/sequential domains, games). Adequacy links the **denotational** (this section) and **operational** (§13) faces of recursion.

> [!warning] Warning 32.2.3: Domains require continuity, not mere monotonicity
> The Kleene fixed-point construction (Theorem 32.1.2) needs **continuity** (preservation of directed suprema), not just monotonicity: a monotone but non-continuous map on a CPO has a least fixed point (by ordinal iteration to a possibly transfinite stage, Knaster–Tarski) but **not** necessarily the $\omega$-limit $\bigsqcup_n f^n(\bot)$, and the latter may not be a fixed point. The base treatise's finitary stage construction (its §1.5) stabilizing at $\omega$ is exactly the continuity phenomenon; abandoning continuity reintroduces transfinite iteration (cf. base treatise Warning 1.5.7, and §9 here).

### 32.3. Algebraic and Bifinite Domains

> [!definition] Definition 32.3.1: Compact elements and algebraic domains
> An element $c$ of a CPO is **compact (finite)** if whenever $c\sqsubseteq\bigsqcup S$ for directed $S$, then $c\sqsubseteq s$ for some $s\in S$. A CPO is **algebraic** if every element is the directed supremum of the compact elements below it, and a **Scott domain** if additionally bounded-complete. The compact elements are the "finite approximations"; in the completed term algebra (§16.1) they are exactly the finite partial terms.

> [!remark] Remark 32.3.2: Domains as completions of finitary data
> An algebraic domain is determined by its poset of compact elements (its **basis**) via ideal completion — exactly the construction of §16.1 applied to an arbitrary partial order of finite data. Domain theory is therefore the systematic study of **completing finitary, freely/inductively generated structures to admit infinite and partial elements and least-fixed-point recursion**, the order-theoretic sibling of the coalgebraic completion of Part VI. The base treatise's free finite term algebra sits at the bottom (its compact elements); domains and final coalgebras are its two completions, supporting respectively fixpoint recursion and coinductive corecursion.

---

## 33. Explicit Substitution Calculi

The base treatise treats substitution as a **meta-level** total operation (its §8); the de Bruijn presentation (§6) makes it an arithmetic operation on indices. **Explicit substitution calculi** internalize substitution as **object-level constructors with rewrite rules**, bridging the abstract substitution of §8, the de Bruijn syntax of §6, and the rewriting theory of §13. They are the formal foundation of abstract machines and efficient $\lambda$-calculus implementations.

### 33.1. The $\lambda\sigma$-Calculus

> [!definition] Definition 33.1.1: Syntax of explicit substitutions
> The **$\lambda\sigma$-calculus** extends de Bruijn $\lambda$-terms (§6) with two syntactic categories — **terms** and **substitutions** — and constructors making substitution explicit:
> $$
> \textbf{terms}\quad a ::= \underline 1 \mid a\,b \mid \lambda a \mid a[s];\qquad \textbf{substitutions}\quad s ::= \mathrm{id} \mid {\uparrow} \mid a\cdot s \mid s\circ t,
> $$
> where $a[s]$ is the **suspended** application of substitution $s$ to term $a$, $\mathrm{id}$ is the identity, ${\uparrow}$ is shift, $a\cdot s$ is "cons" (extend a substitution), and $s\circ t$ is composition. Substitution is now **data**, not a meta-operation.

> [!definition] Definition 33.1.2: The $\sigma$-rules and $\mathrm{Beta}$
> The calculus has a set of **$\sigma$-rules** that **propagate** substitutions through term structure and compose them (e.g. $(a\,b)[s]\to a[s]\,b[s]$, $(\lambda a)[s]\to\lambda(a[\underline 1\cdot(s\circ{\uparrow})])$, $\underline 1[a\cdot s]\to a$, associativity/identity laws for $\circ$), together with the rule
> $$
> \mathrm{Beta}:\quad (\lambda a)\,b\ \to\ a[\,b\cdot\mathrm{id}\,]
> $$
> realizing $\beta$-reduction by **creating** an explicit substitution rather than performing it. Ordinary $\beta$-reduction is recovered by computing the substitution via the $\sigma$-rules.

### 33.2. Properties

> [!theorem] Theorem 33.2.1: The substitution sub-calculus is convergent
> The $\sigma$-rules **without** $\mathrm{Beta}$ form a **convergent** (terminating and confluent) rewrite system (§13): every term-with-explicit-substitutions has a unique $\sigma$-normal form, which is the corresponding pure de Bruijn term with all substitutions carried out. Thus the meta-level de Bruijn substitution (§6.2) is exactly **$\sigma$-normalization**, turning the base treatise's substitution operation into a terminating computation.

> [!warning] Warning 33.2.2: Explicit substitutions can break confluence and termination on open terms
> The full calculus ($\sigma + \mathrm{Beta}$) is subtle: the original $\lambda\sigma$ is **not confluent on terms with metavariables** (open terms), a defect repaired by variant calculi ($\lambda\sigma_{\Uparrow}$, $\lambda\upsilon$, suspension calculus) at the cost of more machinery. Moreover **preservation of strong normalization (PSN)** — that a strongly normalizing pure $\lambda$-term remains strongly normalizing with explicit substitutions — **can fail** (Melliès' counterexample), and recovering PSN is a principal design criterion. Internalizing substitution as rewriting does not automatically inherit the good properties of meta-level substitution; they must be re-established.

> [!remark] Remark 33.2.3: Where explicit substitution sits in the companion
> Explicit substitution calculi are the precise junction of three companion threads: the **de Bruijn** presentation of binding (§6) supplies the nameless syntax; the **substitution monad/laws** (base treatise §8, companion §8.1–8.2) supply the equations the $\sigma$-rules must satisfy; and **term rewriting** (§13) supplies the convergence/termination analysis. They show that the base treatise's atomic, meta-level "apply a substitution" is itself a **finitely presented, analyzable rewrite computation** — the operational decomposition of the monad multiplication $\mu$ (its flattening) into small steps. This is the most concrete realization of the slogan that substitution is evaluation made effective.

---

# Part XI — Refinements of the Effective Theory

## 34. Term Graph Rewriting and Sharing

The base treatise notes hash-consing and DAG representations (its §12.3) as implementation optimizations. **Term graph rewriting** elevates sharing to a primary object of study: terms are represented as **directed (acyclic or cyclic) graphs** in which equal subterms are shared, and rewriting acts on the graph. This changes the cost model and, for cyclic graphs, the very objects (finite graphs denoting infinite terms, §16).

### 34.1. Term Graphs

> [!definition] Definition 34.1.1: Term graph
> A **term graph** over $\Omega$ is a labeled graph: a finite set $N$ of **nodes**, a labeling $\mathrm{lab}:N\to\Omega\cup X$, a **successor** function giving each node labeled $f\in\Omega_n$ an ordered list of $n$ successor nodes, and a distinguished **root**. An **acyclic** term graph denotes a finite term by **unraveling** (the tree of paths from the root); a **cyclic** term graph denotes a **rational infinite term** (§16.2). Sharing means several paths reach one node.

> [!definition] Definition 34.1.2: Graph rewrite step
> A **term graph rewrite rule** is a pair of graphs (a redex pattern and a replacement) with an interface of shared nodes. A **rewrite step** matches the left pattern as a subgraph (a graph homomorphism), **redirects** edges to the replacement, and garbage-collects unreachable nodes. The **double-pushout (DPO)** and **single-pushout (SPO)** formalisms give this a precise category-theoretic semantics (pushouts in a category of graphs and partial graph morphisms).

### 34.2. Soundness and Speedups

> [!theorem] Theorem 34.2.1: Adequacy of acyclic term graph rewriting
> For an ordinary (left-linear) TRS, acyclic term graph rewriting is **sound and complete** with respect to term rewriting on the unravelings: a graph rewrite step corresponds to one-or-more parallel term rewrite steps on the denoted term, and every term rewrite sequence is realized by a graph rewrite sequence. Sharing can yield **exponential speedups** (one graph step effects many term steps on shared copies) and is what makes call-by-need evaluation efficient. Confluence and normalization results transfer under left-linearity.

> [!warning] Warning 34.2.2: Sharing changes equality and can change semantics
> Two distinct term graphs may unravel to the **same** term (different sharing of one term) — graph equality is **finer** than term equality, so a property must be checked **modulo unraveling** to be a property of terms. For **cyclic** graphs the unraveling is an **infinite** term (§16): cyclic graph rewriting computes on infinite/rational terms and is sound for term rewriting only under the infinitary semantics, where the occurs check is dropped (Warning 16.2.3). Treating a cyclic graph as a finite term, or graph equality as term equality, is the characteristic error.

> [!remark] Remark 34.2.3: Graphs interpolate finite and infinite terms
> Term graphs sit precisely between the base treatise's finite terms and the companion's infinite terms (§16): **acyclic** graphs are shared finite terms (same objects, smaller representation), while **cyclic** graphs are finite representations of **rational infinite** terms (a proper subclass of $\nu H_\Omega$, §17). The DAG/sharing optimization and the infinite-term coalgebra are thus two points on one spectrum of representations, with cyclicity the boundary the occurs check polices.

---

## 35. Modularity of Termination and Confluence

A recurring practical question is whether properties of rewrite systems are **modular**: preserved under combining systems. The answers sharply distinguish confluence (well-behaved) from termination (badly behaved), refining the base treatise's treatment of rewriting (its §7.4) with the combination theory.

> [!definition] Definition 35.1.1: Disjoint and constructor-sharing unions
> Two TRSs $R_1$ (over $\Omega_1$) and $R_2$ (over $\Omega_2$) form a **disjoint union** $R_1\uplus R_2$ if $\Omega_1\cap\Omega_2=\varnothing$; they form a **constructor-sharing union** if they share only **constructors** (symbols not occurring at the head of any left side). A property $\mathsf P$ is **modular** for a class of unions if $\mathsf P(R_1)\wedge\mathsf P(R_2)\Rightarrow\mathsf P(R_1\cup R_2)$.

> [!theorem] Theorem 35.1.2: Toyama's theorem (modularity of confluence)
> **Confluence is modular for disjoint unions:** if $R_1$ and $R_2$ are confluent and signature-disjoint, then $R_1\uplus R_2$ is confluent (Toyama). Confluence is robust under combination.

> [!warning] Warning 35.1.3: Termination is NOT modular
> **Termination is not modular for disjoint unions** (Toyama's counterexample): there exist terminating $R_1,R_2$ over disjoint signatures whose union $R_1\uplus R_2$ is **non-terminating** — interaction through shared variables in mixed terms creates infinite reductions absent from each system alone. Hence one cannot conclude termination of a combined specification from termination of its parts; this is among the most counterintuitive facts of rewriting and a frequent source of erroneous termination claims.

> [!theorem] Theorem 35.1.4: Conditions restoring modular termination
> Termination **is** modular for disjoint unions under additional hypotheses: if both systems are **non-collapsing** (no rule has a variable right side) **or** both are **non-duplicating** (no rule has more occurrences of a variable on the right than the left), the union terminates; likewise **completeness** (convergence) is modular for disjoint unions (Toyama–Klop–Barendregt), and there are refined results for constructor-sharing and hierarchical unions. The general failure (Warning 35.1.3) is repaired exactly by controlling collapsing and duplicating rules.

> [!remark] Remark 35.1.5: Why confluence and termination differ
> Confluence is a **local-to-global** property (Newman's Lemma, the Critical Pair Lemma, §13.3) that disjoint systems cannot make interact, because cross-signature critical pairs do not arise. Termination is a **global well-foundedness** property that the **layered structure** of mixed terms can destroy: a collapsing rule in one system can expose a redex of the other at a position that re-enables the first, threading an infinite descent through the layers. The modularity theory is the precise account of when the base treatise's local rewriting analysis survives composition.

---

## 36. Equational Theorem Proving: Paramodulation and Superposition

Knuth–Bendix completion (§13.4) decides **purely equational** theories. Reasoning in **first-order logic with equality** — clauses combining equations, predicates, and negation — requires lifting completion's ideas to clauses: **paramodulation** and its refinement **superposition**, the basis of modern saturation-based theorem provers. This continues the effective-equational thread into full first-order deduction.

### 36.1. Paramodulation

> [!definition] Definition 36.1.1: Clauses and the paramodulation rule
> A **clause** is a finite disjunction of literals (atoms or negated atoms), with equality $\approx$ a distinguished predicate. The **paramodulation** inference combines resolution with equational replacement: from clauses $C\vee s\approx t$ and $D[u]$ (with $u$ a subterm), if $\sigma=\mathrm{mgu}(s,u)$, derive
> $$
> \big(C\vee D[t]\big)\sigma,
> $$
> "use the equation $s\approx t$ to rewrite $u$ to $t$ inside $D$, unifying $s$ with $u$." Together with **resolution** and **equality factoring**, paramodulation is **refutation-complete** for first-order logic with equality (no separate equality axioms needed).

### 36.2. Superposition

> [!definition] Definition 36.2.1: Ordered superposition with selection
> **Superposition** is paramodulation **restricted** by a reduction ordering $>$ (§13.2) and a literal selection function: inferences are performed only into **maximal** terms of **maximal** literals and only in the $>$-decreasing direction (rewriting big to small), and rewriting **below variables** is forbidden (as in critical pairs, §13.3). These restrictions drastically prune the search space while preserving refutation completeness.

> [!theorem] Theorem 36.2.2: Completeness of superposition; completion as a special case
> The **superposition calculus** (ordered superposition + ordered resolution + equality factoring + redundancy elimination) is **sound and refutation-complete** for first-order logic with equality, and is **compatible with redundancy**: clauses subsumed or simplified by smaller ones may be deleted, making saturation practical. **Restricted to unit equations** (clauses that are single equations), superposition **coincides with unfailing Knuth–Bendix completion** (§13.4): completion is the equational special case of superposition. The same critical-pair/ordering machinery thus scales from the word problem to full first-order theorem proving.

> [!warning] Warning 36.2.3: Completeness is refutational and search is unbounded
> Superposition is **refutation**-complete: it derives the empty clause from an **unsatisfiable** set, but on a **satisfiable** set saturation may run forever (first-order validity with equality is semi-decidable, not decidable). The ordering and selection restrictions guarantee completeness only for **admissible** strategies; ad hoc restrictions can lose completeness. As throughout the effective theory, a complete procedure for an undecidable problem terminates on the "yes" instances (here, unsatisfiability) but not in general — the exact analogue of completion's success/divergence dichotomy (Theorem 13.4.2).

> [!remark] Remark 36.2.4: The unifying role of orderings and critical overlaps
> Across §§12–14, §23, §33, and §36 a single mechanism recurs: **unify left-hand sides, rewrite in the direction of a reduction ordering, and join the resulting overlaps**, with redundancy controlled by the ordering. Critical pairs (completion), congruence closure (ground case), narrowing ($E$-unification), and superposition (first-order) are all instances. The base treatise's static equational congruence becomes, effectively, a **saturation under ordered overlaps**; the ordering is what converts the symmetric, undirected congruence into a terminating, confluent computation wherever that is possible at all.

---

# Part XII — Behavioral Specification

## 37. Hidden Algebra and Observational Equivalence

Initial-algebra semantics (§31) is the theory of **data** (constructor-generated, no junk/no confusion). Its dual, for **state-based / object** systems, is **behavioral (hidden) algebra**: a specification of objects whose internal states matter only up to **observable behavior**. This is the coalgebraic (§17) counterpart of §31 in specification form, and it completes the companion's algebra/coalgebra symmetry at the level of software specification.

### 37.1. Hidden Signatures and Behavioral Equivalence

> [!definition] Definition 37.1.1: Hidden signature
> A **hidden signature** partitions sorts into **visible** sorts $V$ (data: Booleans, integers — interpreted by a fixed data algebra) and **hidden** sorts $H$ (states). Operations are classified as **attributes** (hidden input, visible output — observations), **methods** (hidden input and output — state changes), and data operations on $V$. An **experiment** is a visible-result term context built from attributes and methods applied to a state.

> [!definition] Definition 37.1.2: Behavioral (observational) equivalence
> Two states $a,b$ of a hidden algebra are **behaviorally equivalent**, $a\equiv b$, if **every experiment yields the same visible result**: for all visible-result contexts $C[\,]$ (built from the hidden operations), $C[a]=C[b]$ in the data algebra. $\equiv$ is the largest **hidden congruence** (congruence identical to equality on visible sorts); it is the **final/greatest** such relation, dual to the least congruence $\theta_E$ of initial semantics.

> [!theorem] Theorem 37.1.3: Behavioral satisfaction and final models
> A hidden specification is interpreted by **behavioral satisfaction**: an equation holds **behaviorally** if both sides are behaviorally equivalent (not necessarily equal). The model class admits a **final (terminal)** model in which states are identified exactly when behaviorally equivalent — the minimal-state realization, the coalgebraic dual (final coalgebra, §17.2) of the initial data algebra of §31. Behavioral equivalence corresponds to **bisimilarity** (Definition 17.3.1) of the associated coalgebra of attributes and methods.

> [!warning] Warning 37.1.4: Behavioral satisfaction is not ordinary satisfaction
> An equation may hold **behaviorally** while **failing** as ordinary (strict) equality: two stack implementations (array-with-pointer vs list) satisfy the stack axioms behaviorally but have unequal internal states, and operations like "push then pop" return the original behavior without restoring the original representation. Using **strict** equality (initial semantics) for such a type wrongly rejects correct implementations; the correct notion is behavioral equality (final semantics). Choosing the register — **strict/initial for data, behavioral/final for objects** — is the central design decision, the specification-level form of the induction-vs-coinduction discipline (Warning 17.3.3).

> [!remark] Remark 37.1.5: Coinduction as the proof method for behavioral equality
> To prove two states behaviorally equivalent one exhibits a **hidden congruence (bisimulation)** relating them and shows it is preserved by all methods and equated by all attributes — **coinduction** (Theorem 17.3.2), not induction. Hidden algebra is thus the specification methodology in which the companion's coalgebraic dual (Part VI) becomes a practical proof technique: data types are reasoned about by structural induction over constructors (base treatise, §31), objects by coinduction over observations. The two halves of the fixpoint theory of a signature correspond exactly to the two halves of software specification.

---

# Part XIII — Recursion Schemes and the Effectivity Map

## 38. Recursion Schemes

The base treatise's structural recursion (its Theorem 6.2.1) is the **catamorphism**: the unique map out of the initial algebra. Part VI's corecursion (§17.2) is the **anamorphism**: the unique map into the final coalgebra. Between and around them lies a small algebra of **recursion schemes**, each a controlled, total pattern of definition justified by a universal property. This part records the principal schemes, completing the recursion theory the base treatise opened.

### 38.1. Catamorphisms and Anamorphisms

> [!definition] Definition 38.1.1: Catamorphism (fold)
> For the signature functor $H_\Omega$ with initial algebra $(\mu H_\Omega,\mathrm{in})$ and any algebra $(C,\theta:H_\Omega C\to C)$, the **catamorphism** $(\!|\theta|\!):\mu H_\Omega\to C$ is the unique homomorphism with
> $$
> (\!|\theta|\!)\circ\mathrm{in}\ =\ \theta\circ H_\Omega(\!|\theta|\!).
> $$
> This is the base treatise's evaluation/recursion: $(\!|\theta|\!)$ folds a finite term by replacing each constructor with the corresponding operation of $C$.

> [!definition] Definition 38.1.2: Anamorphism (unfold)
> For the final coalgebra $(\nu H_\Omega,\mathrm{out})$ (§17.2) and any coalgebra $(C,\gamma:C\to H_\Omega C)$, the **anamorphism** $[\!(\gamma)\!]:C\to\nu H_\Omega$ is the unique coalgebra homomorphism with
> $$
> \mathrm{out}\circ[\!(\gamma)\!]\ =\ H_\Omega[\!(\gamma)\!]\circ\gamma,
> $$
> generating a (possibly infinite) tree by repeatedly observing one layer of $\gamma$. Catamorphism and anamorphism are exact duals (reverse the arrows, swap $\mu/\nu$, $\mathrm{in}/\mathrm{out}$).

> [!definition] Definition 38.1.3: Hylomorphism
> A **hylomorphism** is the composite of an anamorphism followed by a catamorphism, $(\!|\theta|\!)\circ[\!(\gamma)\!]$, computing through a (virtual) intermediate data structure that is built and consumed without being materialized. It models **divide-and-conquer** recursion (the call tree is the intermediate structure). It is well-defined and unique when the intermediate functor's initial algebra and final coalgebra coincide (e.g. for recursion controlled by a well-founded $\gamma$), and it satisfies the **deforestation** law eliminating the intermediate structure.

### 38.2. Parametrized and Course-of-Value Schemes

> [!definition] Definition 38.2.1: Paramorphism and apomorphism
> A **paramorphism** generalizes the catamorphism by giving each recursive step access to the **original substructure** as well as the recursively computed value (recursion "with the input in hand"), justified by the universal property of $\mu H_\Omega$ applied to the algebra on $C\times\mu H_\Omega$. Its dual, the **apomorphism**, generalizes the anamorphism by allowing each step to either continue corecursively **or** halt by supplying a whole final-coalgebra element (corecursion "with early termination"). Primitive recursion (e.g. the predecessor and factorial on $\mathbb N$ using $n$ itself) is the paramorphism scheme.

> [!definition] Definition 38.2.2: Histomorphism and futumorphism
> A **histomorphism** gives each step access to **all** previously computed values (course-of-value recursion, e.g. Fibonacci), justified via the **cofree comonad** on $H_\Omega$; its dual, the **futumorphism**, allows each corecursive step to produce **several** layers at once, via the **free monad**. These comonad/monad-justified schemes are the most general total recursion/corecursion patterns in common use.

> [!theorem] Theorem 38.2.3: Schemes as instances of (co)initiality with (co)monads
> Each recursion scheme is a uniquely-determined map guaranteed by a universal property: catamorphism/paramorphism/histomorphism by **initiality** of $\mu H_\Omega$ (possibly twisted by a comonad), anamorphism/apomorphism/futumorphism by **finality** of $\nu H_\Omega$ (possibly twisted by a monad). Their existence and uniqueness are corollaries of the base treatise's and §17's universal properties; their value is **guaranteed totality and termination/productivity** by construction, in contrast to general (possibly non-terminating) recursion.

> [!warning] Warning 38.2.4: General recursion is not a scheme
> Arbitrary recursive definitions (general fixpoints, §32) need **not** be catamorphisms or any structured scheme: they may fail to terminate and require the domain-theoretic least-fixed-point semantics (Theorem 32.1.2) rather than a universal property. The recursion schemes are exactly the **total, structurally-justified** fragment; identifying "recursion" with "structured recursion scheme" understates what general recursion can express (and at what cost — possible non-termination). The schemes trade expressive power for guaranteed totality.

---

## 39. The Decidability and Complexity Map

This part consolidates the **status of the principal decision problems** appearing across the companion and base treatise. The recurring lesson — *existence of a mathematical object does not entail an algorithm, and an algorithm need not be efficient* — is here made into a reference table with the governing hypotheses stated.

### 39.1. Core Problems and Their Status

> [!remark] Remark 39.1.1: Decidability/complexity summary
> The following collects the status of the central problems; each entry presupposes a **finite** signature and finite inputs unless noted, and "complexity" refers to the standard worst-case measure.
>
> | Problem | Status | Governing hypothesis |
> |---|---|---|
> | Structural (free) term equality | decidable, linear | $E=\varnothing$ (base treatise §12.3) |
> | Syntactic unification | decidable, almost-linear | free algebra; occurs check (Thm 12.2.2, 12.3.2) |
> | Matching | decidable, linear | one-sided (Def 12.4.1) |
> | Anti-unification (lgg) | decidable, polynomial, unitary | free algebra (Thm 24.1.2) |
> | Ground word problem | decidable, near-linear | no variables in $E$; congruence closure (Thm 23.1.2) |
> | General word problem $s=_E t$ | undecidable | finite $E$ with variables (Novikov–Boone) |
> | Word problem, convergent $E$ | decidable | $E$ has a convergent TRS (Thm 13.1.3) |
> | $E$-unifiability | undecidable in general | depends on $E$; types unitary→nullary (Thm 12.5.2) |
> | $AC$-unification | decidable, finitary | $E=AC$ (Thm 12.5.2) |
> | TRS termination | undecidable | sound criteria only (Warn 13.2.6) |
> | TRS confluence (terminating) | decidable | via critical pairs (Cor 13.3.3) |
> | TRS confluence (general) | undecidable | orthogonality is a sufficient criterion (Def 13.3.5) |
> | Knuth–Bendix completion | semi-procedure | success/failure/divergence (Thm 13.4.2) |
> | Higher-order unification | undecidable, infinitary | already 2nd-order (Thm 25.1.2) |
> | Higher-order pattern unification | decidable, unitary | Miller patterns (Thm 25.2.2) |
> | Tree-automaton membership | decidable, polynomial | NFTA run (Thm 15.4.3) |
> | Tree-automaton emptiness | decidable, linear | reachability (Thm 15.4.3) |
> | Tree-automaton equivalence | decidable, EXPTIME (NFTA) | via complement/intersection (Thm 15.4.3) |
> | MSO satisfiability over trees | decidable, non-elementary | recognizable = MSO (Thm 15.5.2) |
> | First-order validity with $\approx$ | undecidable, semi-decidable | superposition refutation-complete (Thm 36.2.2) |
> | Finite basedness of a finite algebra | undecidable | Tarski's problem (Thm 21.3.3) |

> [!warning] Warning 39.1.2: Three independent effectivity dimensions
> The table separates three properties that are routinely conflated: **(i) existence** of the relevant object (always assured for quotients, free algebras, least fixed points — base treatise §7.3); **(ii) decidability** of the associated decision problem (frequently fails — word problem, termination, finite basedness); and **(iii) complexity** of a decision procedure when one exists (ranges from linear to non-elementary). A positive answer at one level says nothing about the others. The single most common error across the subject is to infer an algorithm from a construction, or efficiency from decidability.

> [!remark] Remark 39.1.3: The freeness/effectivity correlation
> A pattern visible down the table: the **free / binder-free / variable-free / ordered** cases are the decidable, low-complexity, unitary ones (structural equality, syntactic unification, matching, anti-unification, ground word problem, pattern unification), while **quotients with variable axioms, binders, or unrestricted higher-order features** push toward undecidability and infinitary behavior. This is the effective-theoretic shadow of the base treatise's invariant: **freeness = generatedness + injectivity** is also, operationally, the boundary of clean computability. Each refinement the companion adds — equations (Part VII), binding (Part II), higher order (§25), sorts/partiality (Part I) — is a controlled retreat from that boundary, decidable again only on an identified fragment.

---

# Part XIV — Synthesis

## 40. Synthesis

This part consolidates the companion: its organizing spine, the principal comparison tables, the consolidated failure-mode checklist, and a master index of the formal items. It is designed for reference, not re-derivation.

### 40.1. The Companion's Spine

> [!remark] Remark 40.1.1: One signature, four refinements, two fixpoints
> The base treatise fixes a single-sorted finitary signature $\Omega$ and builds, over a generator set $X$, the free term algebra $\mathbf T_\Omega(X)$ (initial / least fixpoint of $H_\Omega$), with evaluation, quotients, presentations, equational logic, and the categorical repackaging. The companion varies this setup along **four axes** and supplies the **dual** fixpoint:
> $$
> \textbf{(carrier)}\quad \text{single sort}\ \rightsquigarrow\ \text{many sorts (§2), subsorts (§3), partiality (§4);}
> $$
> $$
> \textbf{(variables)}\quad \text{plain generators}\ \rightsquigarrow\ \text{binding (§§5–8); elimination via combinators (§26);}
> $$
> $$
> \textbf{(theory)}\quad \text{a single congruence}\ \rightsquigarrow\ \text{varieties, quasivarieties, clones, theories, monads (§§18–22);}
> $$
> $$
> \textbf{(effectivity)}\quad \text{abstract existence}\ \rightsquigarrow\ \text{unification, rewriting, completion, automata, decision (§§12–16, 23–25, 33–39);}
> $$
> $$
> \textbf{(fixpoint duality)}\quad \text{initial algebra / induction}\ \rightsquigarrow\ \text{final coalgebra / coinduction (§§16–17, 28, 30, 37, 38).}
> $$
> The unifying frameworks (rewriting logic, institutions, §§27–29) sit above all four axes; the semantics of data and recursion (§§31–32) and the effectivity map (§39) collect the consequences.

> [!remark] Remark 40.1.2: The persistent invariant, restated effectively
> The base treatise's invariant **freeness = generatedness + injectivity** reappears in every part: as **initiality = no junk + no confusion** for data types (§31.2); as **relational/observational freeness** (unique derivability / triviality of behavioral kernel); as the **boundary of clean computability** in §39 (free/binder-free/variable-free/ordered problems are the decidable, unitary ones). Dually, the companion adds the invariant of the **coalgebraic** side: **finality = fully abstract + observationally complete**, with **bisimulation = behavioral equality** (§17.3, §37). Induction governs the least fixpoint; coinduction governs the greatest; the occurs check and the strict/behavioral equality choice are the visible seams between them.

### 40.2. Comparison Tables

> [!remark] Remark 40.2.1: Carriers of syntax (Part I)
>
> | Framework | Carrier | New data | Term algebra free? | Characteristic pitfall |
> |---|---|---|---|---|
> | Single-sorted | one set | — | yes | constants vs generators |
> | Many-sorted | $S$-indexed sets | sorts, profiles | yes (sortwise) | empty-carrier unsoundness (Warn 2.6.3) |
> | Order-sorted | sorts as subsets | sort poset $\le$ | yes if regular | ad hoc vs subsort overloading (Warn 3.4.2) |
> | Partial | sets + domains | partial ops, definedness | free total exists | substitution changes definedness (Warn 4.3.3) |
> | Membership (MEL) | kinds + sort predicates | conditional memberships | initial model exists | — (subsumes the above) |

> [!remark] Remark 40.2.2: Presentations of binding syntax (Part II)
>
> | Presentation | $\alpha$-equivalence is | Recursion principle | Substitution | Cost |
> |---|---|---|---|---|
> | Named raw / $=_\alpha$ | a quotient relation | needs $\alpha$-compatibility proofs | capture-avoiding (Def 5.3.1) | readable; fiddly proofs |
> | De Bruijn | literal equality | index recursion, no names | index arithmetic (Def 6.2.1) | canonical; off-by-one bugs |
> | Nominal | equality of abstractions | named, with FCB (Thm 7.3.2) | nominal recursion (Ex 7.3.4) | explicit permutations |
> | Presheaf / initial algebra | built into the carrier | initiality (Thm 8.2.2–3) | monoid multiplication $\varsigma$ | abstract; uniform UMP |
> | Combinatory (eliminated) | n/a (no binders) | ordinary $\Omega$-algebra recursion | application | weak equality only (Warn 26.2.1) |

> [!remark] Remark 40.2.3: Algebra vs coalgebra (Parts VI, XIII)
>
> | Aspect | Initial algebra $\mu H_\Omega$ | Final coalgebra $\nu H_\Omega$ |
> |---|---|---|
> | Elements | finite well-founded terms | finite-and-infinite terms |
> | Structure map | constructors $\mathrm{in}$ (iso, Lambek) | destructors $\mathrm{out}$ (iso, dual Lambek) |
> | Universal property | initial (unique map out) | final (unique map in) |
> | Defining principle | recursion / catamorphism (Def 38.1.1) | corecursion / anamorphism (Def 38.1.2) |
> | Proof principle | structural induction | coinduction / bisimulation (Thm 17.3.2) |
> | Well-formedness side condition | well-foundedness | guardedness / productivity (Def 17.2.3) |
> | Unification | finite, occurs check (Thm 12.2.2) | rational, no occurs check (Warn 16.2.3) |
> | Type-theoretic name | W-type (Def 30.2.1) | M-type (Rem 30.2.3) |
> | Specification semantics | initial / no junk, no confusion (§31) | final / behavioral (§37) |

> [!remark] Remark 40.2.4: Closure profiles of algebra classes (Part VII)
>
> | Class type | Closure operators | Axioms | Free algebras? | Example that is this but not the previous |
> |---|---|---|---|---|
> | Variety | $H,S,P$ (Birkhoff, Thm 18.2.2) | identities | relatively free (Constr 18.3.1) | groups, lattices, Boolean algebras |
> | Quasivariety | $S,P,P_{\!U}$ (Mal'cev, Thm 19.3.2) | quasi-identities | relatively free | cancellative semigroups (Ex 19.3.5) |
> | Elementary class | $\equiv,P_{\!U}$ | first-order | not in general | fields |
> | Pseudo-elementary / other | weaker | $\mathcal L_{\infty\omega}$ etc. | — | classes needing infinitary logic |

> [!remark] Remark 40.2.5: The three faces of a variety (Part VII)
>
> | Face | Object | Recovers $\mathcal V$ as | Forgets |
> |---|---|---|---|
> | Variety | $\mathcal V\subseteq\mathbf{Alg}(\Omega)$ | itself | nothing (but fixes a signature) |
> | Lawvere theory | $\mathcal T_{\mathcal V}$ (Def 20.2.1) | product-preserving functors $\mathcal T_{\mathcal V}\to\mathbf{Set}$ | the signature/presentation |
> | Finitary monad | $T_{\mathcal V}$ on $\mathbf{Set}$ (Def 20.3.1) | Eilenberg–Moore algebras $\mathbf{Set}^{T_{\mathcal V}}$ | the signature/presentation |
> | Clone | $\mathrm{Clo}(\mathcal V)$ (Def 20.1.4) | term operations + their equations | the choice of generating operations |

### 40.3. Consolidated Failure-Mode Checklist

> [!warning] Warning 40.3.1: Master failure-mode checklist
> The principal failure modes introduced by the companion's extensions, each with its correct condition.
>
> | Failure mode | Where | Correct condition |
> |---|---|---|
> | Contextless deduction over empty sorts | Warn 2.6.3 | carry explicit contexts, or require inhabited sorts |
> | Ad hoc overloading destroys least sorts | Warn 3.4.2 | require regular/preregular signatures |
> | Treating partial evaluation as total | Warn 4.3.3 | track definedness; use Kleene equality $\simeq$ |
> | Bijective weak hom assumed iso | Warn 4.1.4 | use closed homomorphisms matching domains |
> | $\alpha$-classes as a free $\Omega$-algebra | Warn 5.2.3 | binding syntax is initial in a presheaf/nominal category |
> | Naive (capturing) substitution | Warn 5.2.4 | capture-avoiding substitution on $\alpha$-classes |
> | De Bruijn index off-by-one | Warn 6.2.3 | disciplined shift/cutoff arithmetic |
> | Nominal recursion without FCB | Warn 7.3.3 | impose the freshness condition for binders |
> | HOAS with full function space | Warn 8.3.3 | restrict to presheaf/parametric ($\delta$) positions |
> | Quantifiers as finitary operations | §9.1, base Warn 10.4.2 | binding syntax (Part II) or cylindric/polyadic algebra (Part III) |
> | Expecting finite equational FOL | Warn 9.2.2, 11.2.2 | $\mathsf{RCA}_\alpha$ not finitely axiomatizable |
> | Omitting the occurs check (finite terms) | Def 12.2.3 | occurs check; or move to rational terms (Warn 16.2.3) |
> | $E$-equality decidable ⇒ $E$-unification decidable | Warn 12.5.3 | independent properties |
> | Dropping TRS rule conditions | Warn 13.1.5 | $\ell\notin X$, $\operatorname{var}(r)\subseteq\operatorname{var}(\ell)$ |
> | Assuming termination decidable | Warn 13.2.6 | only sound sufficient criteria exist |
> | Local confluence ⇒ confluence | Warn 13.3.4 | needs termination (Newman) or orthogonality |
> | Expecting completion to succeed | Warn 13.4.4 | success is fortunate; may fail/diverge |
> | Narrowing assumed terminating | Warn 14.1.5 | completeness ≠ termination of search |
> | Deterministic top-down tree automata | Warn 15.2.2 | strictly weaker; use bottom-up |
> | Finite carrier ⇒ tame clone lattice | Warn 22.2.5 | only $|S|=2$ (Post); continuum for $|S|\ge3$ |
> | Finite algebra ⇒ finite equational basis | Warn 21.3.4 | false; finite basedness undecidable |
> | Induction on infinite data / coinduction on finite | Warn 17.3.3 | induction for $\mu$, coinduction for $\nu$ |
> | Equating equations and rules | Warn 27.2.3 | separate $E$ (identity) from $R$ (transition) |
> | $\lambda$ as op with $\beta$ as identity | Warn 26.2.1 | use lambda algebras (Curry axioms) |
> | Congruence closure for quantified axioms | Warn 23.3.2 | ground only; variables ⇒ undecidable |
> | Strict equality for object/state types | Warn 37.1.4 | behavioral (final) semantics + coinduction |
> | Graph equality as term equality | Warn 34.2.2 | reason modulo unraveling; cyclic ⇒ infinite |
> | Termination assumed modular | Warn 35.1.3 | fails; needs non-collapsing/non-duplicating |
> | Leaving the higher-order pattern fragment | Warn 25.2.3 | restrict to Miller patterns |
> | Inferring an algorithm from a construction | Warn 39.1.2 | existence ≠ decidability ≠ efficiency |

### 40.4. Master Index of Parts

> [!remark] Remark 40.4.1: Index of the development
>
> | Part | Sections | Central objects | Key results |
> |---|---|---|---|
> | I. Sorted & partial carriers | 2–4 | $S$-sorted / order-sorted / partial algebras | sorted UMP (Thm 2.3.3); least sort (Thm 3.3.2); initial partial models (Thm 4.2.2) |
> | II. Syntax with binding | 5–8 | $\Lambda_{\mathcal O}(\mathbb A)$, de Bruijn, nominal, presheaf | adequacy (Thm 6.2.2); nominal recursion (Thm 7.3.2); FPT initial algebra (Thm 8.2.2) |
> | III. Algebraic logic | 9–11 | cylindric & polyadic algebras | representation gap (Thm 10.2.3); FOL = locally finite RCA (Thm 10.3.2) |
> | IV. Unification & rewriting | 12–14 | mgu, TRS, completion, narrowing | Robinson (Thm 12.2.2); Critical Pair Lemma (Thm 13.3.2); completion (Thm 13.4.2) |
> | V. Tree automata | 15 | NFTA/DFTA, recognizable languages | Myhill–Nerode for trees (Thm 15.4.2); recognizable = MSO (Thm 15.5.2) |
> | VI. Coalgebra & infinitary | 16–17 | $T^\infty_\Omega(X)$, $\nu H_\Omega$ | final coalgebra (Thm 17.2.1); coinduction (Thm 17.3.2) |
> | VII. Varieties, clones, theories | 18–22 | varieties, quasivarieties, clones, monads | HSP (Thm 18.2.2); subdirect rep (Thm 19.1.3); the triangle (Thm 20.3.2); Mal'cev/Jónsson (Thm 21.1.2–3); Post/Rosenberg (Thm 22.2.2–4) |
> | VIII. Further effective methods | 23–25 | congruence closure, lgg, HOU | ground decidability (Thm 23.1.2); lgg (Thm 24.1.2); HOU undecidable (Thm 25.1.2), patterns (Thm 25.2.2) |
> | IX. Unifying frameworks | 26–29 | combinatory algebra, RWL/MEL, modal algebra, institutions | combinatory completeness (Thm 26.1.3); MEL subsumption (Thm 27.1.3); Jónsson–Tarski (Thm 28.2.1); satisfaction condition (Def 29.1.2) |
> | X. Data, domains, computation | 30–33 | W-types, ADTs, domains, $\lambda\sigma$ | W-type initiality (Thm 30.2.2); initiality = no junk/no confusion (Thm 31.2.2); Kleene fixpoint (Thm 32.1.2); $\sigma$-convergence (Thm 33.2.1) |
> | XI. Effective refinements | 34–36 | term graphs, modularity, superposition | acyclic adequacy (Thm 34.2.1); Toyama (Thm 35.1.2); superposition completeness (Thm 36.2.2) |
> | XII. Behavioral specification | 37 | hidden algebra | behavioral = final/bisimulation (Thm 37.1.3) |
> | XIII. Recursion schemes & effectivity | 38–39 | cata/ana/hylo/para/histo; decision map | schemes as (co)initiality (Thm 38.2.3); decidability/complexity table (Rem 39.1.1) |

### 40.5. Closing Synthesis

> [!remark] Remark 40.5.1: What the companion adds to the base architecture
> The base treatise constructs, for a single-sorted total finitary signature, the **least-fixpoint** half of the theory — free term algebras, evaluation, quotients, presentations, equational logic, substitution, relational generation, propositional logic, and the categorical adjunction — pivoting on **freeness = generatedness + injectivity**. The companion completes this architecture in five directions while keeping that pivot. It **enriches the carrier** (sorts, subsorts, partiality, with the empty-carrier, regularity, and definedness side conditions made explicit). It **handles variable binding**, the one place the base treatise declares its framework inadequate, via $\alpha$-equivalence and its de Bruijn, nominal, and presheaf presentations, plus the combinatory elimination of binders and the cylindric/polyadic re-algebraization of quantifiers. It **develops the structure theory of equational classes** — the full HSP and subdirect-representation theorems, quasivarieties, clones, Lawvere theories, finitary monads, Mal'cev conditions, and the finite-basis problem — showing the variety, its theory, and its monad to be three faces of one signature-free object. It supplies the **effective theory** the base treatise only gestured at: unification and its $E$-, higher-order, and anti-unification variants; term rewriting with termination orderings, critical pairs, and completion; narrowing; congruence closure; superposition; tree automata; explicit substitutions; and a consolidated decidability/complexity map whose lesson is that **existence, decidability, and efficiency are three independent properties**. Finally it builds the **coalgebraic dual** — infinite terms, final coalgebras, corecursion, coinduction, bisimulation, behavioral specification, and recursion schemes — so that the base treatise's induction-and-recursion theory acquires its mirror image. The single sentence that organizes both documents is this: a signature determines a polynomial functor whose **least fixpoint is finite syntax governed by induction and freeness**, whose **greatest fixpoint is infinite behavior governed by coinduction and finality**, whose **quotients are the algebras and the logics**, and whose **effective theory is decidable exactly to the extent that freeness, finiteness, and order are preserved**.

---

# Appendices

## Appendix A. Worked Instances

The appendices trace the companion's machinery through concrete signatures, exhibiting how the abstract items specialize. Each instance is mathematically explicit; no result is restated, only instantiated.

### A.1. Peano Naturals: Initial Algebra, Recursion, Coalgebraic Dual

> [!example] Example A.1.1: The natural numbers as a free/initial structure
> Let $\Omega=\{\mathsf z,\mathsf s\}$ with $\operatorname{ar}(\mathsf z)=0$, $\operatorname{ar}(\mathsf s)=1$, and $X=\varnothing$. The ground term algebra $\mathbf T_\Omega(\varnothing)$ has carrier $\{\mathsf z,\mathsf s(\mathsf z),\mathsf s(\mathsf s(\mathsf z)),\dots\}\cong\mathbb N$ and is the **initial** $\Omega$-algebra (base treatise §13.3; W-type of Def 30.2.1 with one nullary and one unary shape). Unique decomposition (every $n$ is $\mathsf z$ or $\mathsf s(m)$ for a unique $m$) is freeness; it is exactly the Peano third/fourth axioms ($\mathsf s$ injective, $\mathsf z\notin\operatorname{im}\mathsf s$).

> [!example] Example A.1.2: Primitive recursion as catamorphism and paramorphism
> Defining $f:\mathbb N\to C$ by $f(\mathsf z)=h_{\mathsf z}$, $f(\mathsf s(n))=h_{\mathsf s}(f(n))$ is the **catamorphism** $(\!|[h_{\mathsf z},h_{\mathsf s}]|\!)$ (Def 38.1.1): the unique homomorphism into the algebra $(C,h_{\mathsf z},h_{\mathsf s})$, i.e. the iterator. **Primitive recursion** (where the step sees $n$ itself, e.g. predecessor $\mathrm{pred}(\mathsf s(n))=n$ and factorial) is the **paramorphism** (Def 38.2.1), justified by initiality applied to $C\times\mathbb N$. Addition $+$, multiplication, and exponentiation are obtained by iterated catamorphisms; the variety they generate (commutative semirings without the absorbing/distributive laws imposed) is presented by the corresponding equations (Part VII).

> [!example] Example A.1.3: The coalgebraic dual — conatural numbers
> The final coalgebra $\nu H_\Omega$ for $H_\Omega(Y)=1+Y$ is the **conaturals** $\overline{\mathbb N}=\mathbb N\cup\{\infty\}$ (Def 17.2.1): a state either is $\mathsf z$ or has a predecessor, observed one step at a time, with $\infty=\mathsf s(\infty)$ the unique solution of the guarded equation $x=\mathsf s(x)$ (Thm 16.2.2; rejected over finite terms by the occurs check). The anamorphism (Def 38.1.2) generates a conatural by repeated observation; **coinduction** (Thm 17.3.2) proves $\overline{\mathbb N}$-equalities such as $\infty=\mathsf s(\infty)$. This is the §40.2.3 algebra/coalgebra table on its smallest nontrivial signature.

### A.2. Lists and the Sorted/Parametric Layer

> [!example] Example A.2.1: Lists over an element sort
> With sorts $S=\{\mathsf e,\mathsf l\}$ and operations $\mathsf{nil}:{\to}\,\mathsf l$, $\mathsf{cons}:\mathsf e\,\mathsf l\to\mathsf l$ (Part I), $\mathbf T_\Sigma(X)_{\mathsf l}$ over a set $X_{\mathsf e}$ of element-variables is the algebra of finite lists, free in the sorted sense (Thm 2.3.3). The catamorphism on lists is **fold**: $\mathrm{fold}(h_{\mathsf{nil}},h_{\mathsf{cons}})$ computes length ($h_{\mathsf{nil}}=0$, $h_{\mathsf{cons}}(e,k)=1+k$), sum, map, and append. The **final** coalgebra of the list functor $H(Y)=1+\mathsf e\times Y$ is the **streams and finite lists** (lists possibly infinite), with coinductive stream equality.

> [!example] Example A.2.2: Append-monoid as a presented algebra
> Imposing on lists the equations of a monoid for $(\mathrm{append},\mathsf{nil})$ yields the **free monoid** $\mathbf F_{\mathsf{Mon}}(X_{\mathsf e})=X_{\mathsf e}^{*}$ (Constr 18.3.1; base treatise Example 2.6.3): the relatively free monoid, the quotient of the term algebra by the fully invariant congruence of the monoid laws, with normal forms the flat sequences. Its Lawvere theory is the theory of monoids; its monad is the list monad $T(X)=X^{*}$ (Ex 20.3.4). Append-associativity is **directed** to a convergent TRS by orienting $(x\mathbin{+\!\!+}y)\mathbin{+\!\!+}z\to x\mathbin{+\!\!+}(y\mathbin{+\!\!+}z)$, deciding the word problem by right-nesting normal forms (§13).

### A.3. Boolean Algebra: Variety, SI, Recognizability

> [!example] Example A.3.1: The Boolean variety and its unique SI
> Boolean algebras form a variety $\mathsf{BA}$ (Part VII) whose **only** subdirectly irreducible (indeed simple) member is the two-element algebra $\mathbf 2$ (Ex 19.1.4); hence $\mathsf{BA}=SP(\mathbf 2)$ (Birkhoff subdirect representation, Thm 19.1.3) and an equation holds in $\mathsf{BA}$ iff it holds in $\mathbf 2$ — the algebraic content of truth-table verification (base treatise §10.2). The free Boolean algebra $\mathbf F_{\mathsf{BA}}(X_n)$ has $2^{2^n}$ elements, isomorphic to the algebra of $n$-ary Boolean functions, equivalently the Lindenbaum–Tarski algebra of $n$-variable propositional logic.

> [!example] Example A.3.2: Boolean terms and rewriting
> Reasoning in $\mathsf{BA}$ is decidable: $\mathbf 2$-evaluation decides any identity (finite check), and Boolean-ring normal forms (the $\mathsf{ZBDD}$/algebraic normal form, or BDDs as a canonical DAG representation, §34) give canonical representatives. As a rewrite theory, Boolean algebra does **not** admit a small convergent TRS in the $\{\wedge,\vee,\neg\}$ signature without $AC$-handling; completion **modulo $AC$** (§12.5, §13.5) or a Gröbner-basis treatment over $\mathbb F_2$ (Appendix B) is the practical route.

### A.4. The Untyped $\lambda$-Calculus: Binding, Rewriting, Algebra

> [!example] Example A.4.1: Three presentations of $\lambda$-syntax
> The untyped $\lambda$-calculus has binding signature $\{\mathrm{app}:(0,0),\ \mathrm{lam}:(1)\}$ (Def 5.1.1). Its terms are $\Lambda_{\mathcal O}(\mathbb A)$ — equivalently the de Bruijn terms $\mathrm{DB}$ (Thm 6.2.2), the nominal initial algebra $\Lambda^{\mathrm{nom}}$ (Constr 7.3.1), or the presheaf initial algebra $\mathbf{Syn}$ (Thm 8.2.2). Capture-avoiding substitution is the monoid multiplication; explicit-substitution calculi (§33) make it a convergent rewrite computation.

> [!example] Example A.4.2: $\beta$-reduction, confluence, and non-termination
> $\beta$-reduction $(\lambda x.M)N\to M[x{:=}N]$ is a higher-order rewrite rule (§25.3). It is **confluent** (Church–Rosser) but **non-terminating** ($\Omega=(\lambda x.xx)(\lambda x.xx)\to\Omega$); confluence holds by **orthogonality**-style arguments (the $\lambda$-calculus is an orthogonal higher-order system, Def 13.3.5), **not** via termination + Newman. Its operational semantics has the denotational counterpart of §32: a $\lambda$-term's meaning is a least fixed point in a reflexive domain $D\cong[D\to D]$, the Scott model.

> [!example] Example A.4.3: Algebraic status — combinatory and lambda algebras
> Bracket abstraction (Thm 26.1.3) translates $\lambda$-terms to combinators over $\{\mathsf S,\mathsf K\}$, presenting $\lambda\beta$ as the variety of **lambda algebras** (Thm 26.2.3) — a genuine equational class, with the caveat that the naive "$\lambda$ as operation, $\beta$ as identity" fails the $\xi$-rule (Warn 26.2.1). Thus the $\lambda$-calculus simultaneously instantiates Part II (binding syntax), Part IV/§25 (higher-order rewriting), Part VI/§32 (domains), and §26 (binder elimination) — the single richest worked instance in the companion.

---

## Appendix B. Gröbner Bases as Knuth–Bendix Completion

The Knuth–Bendix completion of §13.4 has a celebrated incarnation in commutative algebra: **Buchberger's algorithm** for **Gröbner bases** is completion for the equational theory of polynomial ideals, with **S-polynomials** the critical pairs. This appendix records the correspondence, deepening §13 with its most important classical instance.

> [!definition] Definition B.1: Polynomial reduction
> Fix a field $k$, variables $x_1,\dots,x_n$, and a **monomial order** $>$ (a reduction order on monomials, e.g. lexicographic or degree-reverse-lexicographic — an instance of §13.2). A polynomial $f$ **reduces** modulo a set $G$ of polynomials by repeatedly cancelling the **leading monomial** of $f$ using a $g\in G$ whose leading monomial divides it: $f\to_G f-\tfrac{\mathrm{lt}(f)}{\mathrm{lt}(g)}\,g$. This is term rewriting with rules $\mathrm{lt}(g)\to \mathrm{lt}(g)-g$ oriented by the monomial order.

> [!definition] Definition B.2: S-polynomial (critical pair)
> For $g_1,g_2\in G$ with leading terms $\mathrm{lt}(g_i)$, the **S-polynomial** is
> $$
> S(g_1,g_2)\ =\ \frac{L}{\mathrm{lt}(g_1)}\,g_1\ -\ \frac{L}{\mathrm{lt}(g_2)}\,g_2,\qquad L=\operatorname{lcm}(\mathrm{lt}(g_1),\mathrm{lt}(g_2)),
> $$
> the difference of the two reductions of the overlap monomial $L$ — exactly the **critical pair** (Def 13.3.1) of the two rules at their leading-monomial overlap. $S(g_1,g_2)$ is **joinable** iff it reduces to $0$ modulo $G$.

> [!theorem] Theorem B.3: Buchberger's criterion = the Critical Pair Lemma
> A finite set $G$ is a **Gröbner basis** of the ideal it generates iff **every S-polynomial reduces to $0$ modulo $G$**. This is the Critical Pair Lemma (Thm 13.3.2) for polynomial reduction: $G$ is **confluent** (every polynomial has a unique normal form) iff all critical pairs (S-polynomials) are joinable; termination is automatic from the monomial order (Dickson's lemma supplies well-foundedness, the polynomial analogue of Kruskal's theorem, Def 13.2.2).

> [!theorem] Theorem B.4: Buchberger's algorithm = Knuth–Bendix completion
> **Buchberger's algorithm** — repeatedly compute S-polynomials, reduce them modulo the current basis, and adjoin any nonzero remainders as new basis elements until all S-polynomials reduce to $0$ — is exactly **Knuth–Bendix completion** (Constr 13.4.1) for the equational theory of the ideal, with S-polynomials as deduced critical pairs and the monomial order as the reduction order. Unlike the general case (Warn 13.4.4), completion here **always terminates** (Dickson's lemma bounds the process), so a finite Gröbner basis always exists and the **ideal membership problem** ($f\in I$?) is decided by reduction to $0$ — the polynomial word problem, always solvable.

> [!remark] Remark B.5: Why this instance is decidable when the general case is not
> The general word problem is undecidable (base treatise; Thm 39.1.1) and completion may diverge (Warn 13.4.4); polynomial ideals escape both because **Dickson's lemma** makes every monomial order a well-quasi-order under which ascending chains of monomial ideals stabilize, guaranteeing termination of completion. Gröbner bases are thus the paradigm of a theory where the effective machinery of §13 **always succeeds** — the commutative-algebra counterpart of the free-group example (Ex 13.4.5), and a concrete demonstration that the decidability of an equational theory is a property of its specific structure, not of the general framework.

> [!remark] Remark B.6: The unifying overlap principle, once more
> Gröbner bases (this appendix), Knuth–Bendix completion (§13.4), congruence closure (§23), narrowing (§14), and superposition (§36) are five faces of one mechanism: **orient equations by a well-founded order, form critical overlaps, reduce them, and saturate**. The base treatise's static congruence becomes, wherever an order and a termination guarantee are available, a terminating confluent computation. The companion's effective theory is, in a single sentence, the study of when and how that conversion can be carried out — the operational completion of the base treatise's structural theory of free algebras and their quotients.

---

## Appendix C. Unification at Work: Type Inference and Logic Programming

Two of the most consequential applications of the unification theory of §12 are **Hindley–Milner type inference** and the operational semantics of **logic programming** (SLD-resolution), with **narrowing** (§14) the bridge to functional-logic programming. This appendix records them as instances, exhibiting the universal-property and effectivity themes in computational practice.

### C.1. Hindley–Milner Type Inference

> [!definition] Definition C.1.1: Types as a free algebra; type substitution
> Monomorphic types over base types and a binary function-space constructor $\to$ form the free algebra $\mathbf T_{\{\to,\dots\}}(\mathrm{TVar})$ on a set $\mathrm{TVar}$ of **type variables** (base treatise §2). A **type substitution** is a substitution in this algebra (Def 1.4.3); type-variable instantiation is its homomorphic action. The **principal type** of an expression is the most general type, the type-level analogue of the mgu.

> [!theorem] Theorem C.1.2: Principal types via unification (Hindley–Milner / Algorithm W)
> For the let-polymorphic $\lambda$-calculus, type inference reduces to **first-order unification** in the type algebra: each application node imposes an equation $\tau_{\mathrm{fun}}\stackrel{?}{=}\tau_{\mathrm{arg}}\to\beta$ (with $\beta$ fresh), and the **mgu** of the accumulated constraints (Thm 12.2.2) yields the **principal (most general) type**, of which every valid type of the expression is an instance (the subsumption order, Def 12.1.2). The occurs check (Def 12.2.3) rejects self-referential types such as $\alpha\to\alpha=\alpha$, which is exactly the failure of typing $\lambda x.xx$ without recursive types.

> [!remark] Remark C.1.3: Principal type = most general unifier = universal solution
> The existence of principal types is the **unitarity** of syntactic unification (Thm 12.2.2) read in the type algebra; it is, by Theorem 12.4.2, the universal-solution (coequalizer) property in the Kleisli category of the type-term monad. Polymorphic generalization (the **let** rule) quantifies the type variables not free in the environment, producing a **type scheme** — the move from a most general unifier to a family of instances. Hindley–Milner inference is therefore the base treatise's free-algebra/UMP architecture realized as a decidable, almost-linear (Rem 12.3.3) compiler phase.

> [!warning] Warning C.1.4: Beyond rank-1 polymorphism, unification stops sufficing
> Principal types and decidable inference are special to **rank-1 (let-)polymorphism**, where constraints are first-order equations. **System F** (rank-$n$, impredicative) type inference is **undecidable**, and inference for systems with type-level functions requires **higher-order unification** (§25), which is undecidable and infinitary — only the **pattern fragment** (Thm 25.2.2) restores decidable inference (as in dependently-typed elaborators). The decidability boundary of type inference is exactly the unification boundary of §12/§25: first-order/pattern decidable, full higher-order not.

### C.2. SLD-Resolution and Logic Programming

> [!definition] Definition C.2.1: Horn clauses and SLD-resolution
> A **definite (Horn) program** is a set of clauses $A\leftarrow B_1,\dots,B_k$ (atoms over a first-order term algebra). Given a **goal** $\leftarrow G_1,\dots,G_m$, an **SLD-resolution** step selects a goal atom $G_i$, chooses a (renamed) program clause $A\leftarrow \vec B$, computes $\sigma=\mathrm{mgu}(G_i,A)$ (Thm 12.2.2), and replaces the goal by $(\dots,G_{i-1},\vec B,G_{i+1},\dots)\sigma$. A derivation ending in the empty goal is a **refutation**; the composed mgus restricted to the query variables form the **computed answer substitution**.

> [!theorem] Theorem C.2.2: Soundness and completeness of SLD-resolution
> For definite programs, SLD-resolution is **sound** (every computed answer is a logical consequence) and **complete** (every correct answer is subsumed by a computed one), with the **least Herbrand model** — the ground atoms derivable, an initial-algebra-style least fixpoint (Thm 32.1.2 / §9) of the program's immediate-consequence operator — as declarative semantics. Unification supplies the single inference engine; the least fixpoint supplies the meaning. Logic programming is thus relational generation (base treatise §9) made operational by unification.

> [!remark] Remark C.2.3: Narrowing unifies functional and logic programming
> Where SLD-resolution uses **unification** to solve relational goals, **narrowing** (§14) uses unification-plus-rewriting to solve **equational** goals, and **needed narrowing** (Def 14.1.4) is the operational semantics of **functional-logic** languages combining both. The progression — matching (evaluate), unification (solve relations), narrowing (solve modulo equations) — is precisely the effectivity ladder of the companion: evaluation (base treatise $\operatorname{ev}$), then equation-solving in the free algebra (§12), then equation-solving modulo a rewrite theory (§14), each a more powerful, more expensive universal-solution computation.

---

## Appendix D. Index of Notation

> [!notation] Notation D.1: Principal symbols of the companion
> The recurring notation, with defining locations.
>
> | Symbol | Meaning | Defined |
> |---|---|---|
> | $\Omega,\Sigma$ | (single- / many-sorted) signature | Def 1.2.1, 2.1.1 |
> | $\mathbf T_\Omega(X)$, $\mathbf T_\Sigma(X)$ | (sorted) free term algebra | Def 1.3.1, Constr 2.3.2 |
> | $\operatorname{ev}_g$ | evaluation homomorphism | Thm 1.3.2 |
> | $\theta_E$, $\theta_E^{\mathrm{fi}}$ | congruence / fully invariant congruence of $E$ | Def 1.4.2 |
> | $\langle X\mid E\rangle$ | presented algebra | Def 1.4.2 |
> | $f:s_1\cdots s_n\to s$ | operation profile | Def 2.1.1 |
> | $\le$ (on sorts), $\mathrm{ls}(t)$ | subsort order, least sort | Def 3.1.1, Thm 3.3.2 |
> | $f^A:|A|^n\rightharpoonup|A|$, $u{\downarrow}$, $\simeq$ | partial operation, definedness, Kleene equality | Def 4.1.1–2 |
> | $=_\alpha$, $\Lambda_{\mathcal O}(\mathbb A)$ | $\alpha$-equivalence, binding syntax | Def 5.2.1–2 |
> | $\underline n$, $\uparrow^d_c$, $u\{j\mapsto s\}$ | de Bruijn index, shift, substitution | §6 |
> | $\mathbb S$, $\operatorname{supp}$, $a\#z$, $[\mathbb A]Z$ | permutations, support, freshness, abstraction | §7 |
> | $\widehat{\mathbb F}$, $\otimes$, $\delta$ | presheaf category, substitution tensor, context extension | §8 |
> | $\mathsf c_i$, $\mathsf d_{ij}$, $\mathsf{CA}_\alpha$, $\mathsf{RCA}_\alpha$ | cylindrification, diagonal, (representable) cylindric algebras | §10 |
> | $s\stackrel{?}{=}t$, $\mathrm{mgu}$, $\lesssim$ | unification problem, most general unifier, subsumption | §12 |
> | $\to_R$, $\downarrow$, $t{\downarrow}_R$ | rewrite step, joinability, normal form | §13.1 |
> | $>_{\mathrm{lpo}}$, RPO, KBO | path / weight reduction orderings | §13.2 |
> | $\mathrm{CP}(R)$, $S(g_1,g_2)$ | critical pairs, S-polynomial | §13.3, App B |
> | $\rightsquigarrow_\sigma$ | narrowing step | §14 |
> | $\mathcal A=(Q,\Omega,Q_f,\Delta)$, $\equiv_L$ | tree automaton, Myhill–Nerode congruence | §15 |
> | $\sqsubseteq$, $T^\infty_\Omega(X)$, $\widehat T_\Omega(X)$ | approximation order, continuous / metric completion | §16 |
> | $H_\Omega$, $\mu H_\Omega$, $\nu H_\Omega$, $\mathrm{out}$ | signature functor, initial algebra, final coalgebra | §17 |
> | $\sim$ (bisimilarity) | bisimulation equivalence | Def 17.3.1 |
> | $H,S,P,P_{\!U}$, $V(\mathcal K)$ | class operators, variety closure | §18.1 |
> | $\operatorname{Id},\operatorname{Mod}$, $\mathbf F_{\mathcal V}(X)$ | Galois polars, relatively free algebra | §18 |
> | $\mathrm{Clo}(A)$, $\mathcal T_{\mathcal V}$, $T_{\mathcal V}$ | clone, Lawvere theory, finitary monad | §20 |
> | $m(x,y,z)$, Jónsson/Pixley terms | Mal'cev / congruence-condition terms | §21.1 |
> | $\mathrm{Pol},\mathrm{Inv}$ | polymorphisms, invariant relations | §22.1 |
> | $\sim$ (congruence closure) | ground congruence closure | §23.2 |
> | $\mathrm{lgg}$ | least general generalization | §24 |
> | $\mathsf{Sh}\triangleleft\mathsf{Pos}$, $\mathsf W$ | container, W-type | §30 |
> | $(\!|\theta|\!)$, $[\!(\gamma)\!]$ | catamorphism, anamorphism | §38.1 |
> | $a\equiv b$ (behavioral) | observational equivalence | Def 37.1.2 |

---

## Appendix E. Further Worked Instances

This appendix runs the structure-theoretic and effective machinery (Parts IV, V, VII, and §28) through four additional concrete theories, each illustrating a distinct phenomenon: a clean decidable case, a non-finitely-axiomatizable case, a recognizability case, and a quantitative coalgebraic case.

### E.1. Groups: Decidable Free Case, Undecidable General Case

> [!example] Example E.1.1: The variety of groups and its congruences
> Groups form a variety (Part VII) presented by associativity, unit, and inverse laws. It is **congruence-permutable** via the Mal'cev term $m(x,y,z)=x\cdot y^{-1}\cdot z$ (Thm 21.1.2), so its congruences permute and correspond to **normal subgroups** (the classical isomorphism theorems are the base treatise's congruence theorems specialized through this correspondence). Groups are finitely based (Oates–Powell, Thm 21.3.2) but **not** congruence-distributive, so Jónsson's lemma does not apply and the lattice of group varieties is uncountable (Ex 18.4.2).

> [!example] Example E.1.2: Free groups — completion succeeds
> The free group $\mathbf F_{\mathsf{Grp}}(X)$ (Constr 18.3.1) has reduced words as normal forms; Knuth–Bendix completion of the group axioms terminates with a finite convergent TRS (base treatise Example; §13.4 Ex 13.4.5), so the **word problem for free groups is decidable** by reduction to reduced form. This is the fortunate-completion case (Warn 13.4.4): an order and a termination guarantee both exist.

> [!example] Example E.1.3: Finitely presented groups — undecidable
> Adjoining ground relations gives finitely **presented** groups $\langle X\mid E\rangle$ whose word problem is, by **Novikov–Boone**, **undecidable** (base treatise §7.3, §12.4): no completion can succeed, and the quotient $\mathbf T_{\mathsf{Grp}}(X)/\theta_E$ exists (always) without any decision procedure. Groups thereby exhibit, within one variety, both ends of §39's decidability map — the free case decidable, the presented case undecidable — exactly delimiting where the effective theory can help.

### E.2. Relation Algebras: A Non-Finitely-Axiomatizable Representable Class

> [!example] Example E.2.1: The algebra of binary relations
> Binary relations on a set $U$, under union, intersection, complement, **composition** $;$, **converse** ${}^{\smile}$, and the identity relation, form a **relation algebra** — a Boolean algebra with operators (cf. §28.1), axiomatized by Tarski's finitely many equations as the variety $\mathsf{RA}$. The intended models are the **representable** relation algebras $\mathsf{RRA}$ (subalgebras of full algebras of binary relations).

> [!example] Example E.2.2: The representation gap, again
> As with cylindric algebras (Thm 10.2.3), $\mathsf{RRA}\subsetneq\mathsf{RA}$ and **$\mathsf{RRA}$ is a variety that is not finitely axiomatizable** (Monk; Tarski–Givant): no finite set of equations cuts out the representable relation algebras, and Tarski's $\mathsf{RA}$-axioms provably undershoot. Relation algebras are the relational counterpart of Part III's cylindric phenomenon, and the equational theory of binary relations — hence a large fragment of first-order logic with three variables — inherits the same non-finitizability, a second precise form of the base treatise's "logic exceeds equational algebra."

### E.3. A Recognizable Tree Language and Its Minimal Automaton

> [!example] Example E.3.1: Well-formed Boolean terms with an even number of negations
> Over $\Omega=\{\mathsf t^{(0)},\mathsf f^{(0)},\neg^{(1)},\wedge^{(2)}\}$, the language $L$ of ground terms with an **even** number of $\neg$-nodes is recognizable: a complete DFTA with states $\{\mathrm{even},\mathrm{odd}\}$, transitions $\mathsf t,\mathsf f\to\mathrm{even}$, $\neg(\mathrm{even})\to\mathrm{odd}$, $\neg(\mathrm{odd})\to\mathrm{even}$, $\wedge(p,q)\to$ (parity sum of $p,q$), and $Q_f=\{\mathrm{even}\}$ (Def 15.1.1). The run is the evaluation homomorphism into the parity algebra $\mathbb Z_2$ (Rem 15.1.3), and $L=\operatorname{ev}^{-1}(0)$.

> [!example] Example E.3.2: Myhill–Nerode and minimality
> The syntactic congruence $\equiv_L$ (Def 15.4.1) has exactly **two** classes (even/odd parity of negations), so $L$ is recognizable with a **two-state minimal** automaton (Thm 15.4.2, 15.3.3), and $\mathbf T_\Omega(\varnothing)/{\equiv_L}\cong\mathbb Z_2$. By Theorem 15.5.2 $L$ is MSO-definable (parity is expressible in MSO via a set quantifier counting $\neg$-positions modulo 2). This is the tree-level instance of the regular/recognizable/algebraic/logical fourfold equivalence (Rem 15.5.3).

### E.4. A Quantitative Coalgebra: Streams and Probabilistic Transition Systems

> [!example] Example E.4.1: Streams as a final coalgebra
> For $H(Y)=A\times Y$, the final coalgebra is the set $A^\omega$ of **infinite streams** over $A$ with $\mathrm{out}=(\mathrm{head},\mathrm{tail})$ (Thm 17.2.1). Stream-defining equations (e.g. $\mathrm{ones}=1\!:\!\mathrm{ones}$, or the pointwise sum of two streams) are **anamorphisms** (Def 38.1.2); stream identities (e.g. commutativity of pointwise sum, or $\mathrm{merge}/\mathrm{split}$ inverses) are proved by **coinduction** exhibiting a bisimulation (Thm 17.3.2), not by induction — there is no base case.

> [!example] Example E.4.2: Probabilistic systems and behavioral equivalence
> For the (finite) **distribution functor** $\mathcal D$, a $\mathcal D$-coalgebra $c:C\to\mathcal D(C)$ is a **Markov chain**; for $\mathcal D(A\times(-))$ it is a labelled Markov process. **Behavioral equivalence** is **probabilistic bisimilarity** (Def 17.3.1 generalized to $\mathcal D$), and the coalgebraic modal logic (Thm 28.2.2) with predicate liftings "the probability of reaching a $\varphi$-state exceeds $q$" is **expressive** for it (a Hennessy–Milner property). This instantiates the companion's coalgebraic dual in the **quantitative** setting, showing that the algebra/coalgebra architecture (Rem 40.2.3) is not limited to the powerset/relational case but applies to any suitable functor $H$.

> [!remark] Remark E.4.3: One architecture across all instances
> Across Appendices A–E the same skeleton recurs on every signature and functor: a **least fixpoint** of finite syntax (term algebra, W-type) carrying induction/recursion and freeness; a **greatest fixpoint** of infinite behavior (final coalgebra, M-type, streams) carrying coinduction/corecursion and bisimulation; **quotients** giving the varieties, the logics, and the data types (no junk/no confusion); and an **effective theory** (unification, completion, automata, Gröbner bases, inference, resolution) that is decidable exactly where freeness, finiteness, and a well-founded order are preserved. The worked instances differ only in the chosen functor and equations; the architecture is invariant — which is the precise sense in which this companion and the base treatise describe a single theory.

---

## Appendix F. Algebraic Logic: Completeness, Finite Models, and Decidable Fragments

This appendix deepens Part III by recording how the algebraic reformulation converts the metatheorems of logic into structural statements, and where decidability is recovered by restricting dimension or invoking the finite model property.

> [!theorem] Theorem F.1: Completeness as representability
> Gödel's completeness theorem for first-order logic is equivalent, under the cylindric algebraization (§10.3), to the statement that the Lindenbaum cylindric algebra $\mathfrak{Lt}(\Theta)$ of every consistent theory is **representable** (embeds into a cylindric set algebra). "Provable $=$ valid" becomes "the syntactic algebra has a set-theoretic model," and the construction of a model from a consistent theory is the construction of a representation. Thus the central metatheorem of logic is a **representation theorem** in algebraic logic, parallel to Stone's theorem for Boolean algebras (§28.2).

> [!theorem] Theorem F.2: Finite model property and decidability
> A variety (or quasivariety) of algebras has the **finite model property (FMP)** if every non-identity is refuted in a finite member. FMP plus finite axiomatizability yields **decidability** of the equational theory: enumerate proofs and finite countermodels in parallel. Many modal varieties (e.g. those for $\mathbf K,\mathbf T,\mathbf{S4},\mathbf{S5}$) have FMP, giving decidability of the corresponding modal logics; by contrast $\mathsf{RCA}_\alpha$ for $\alpha\ge\omega$ lacks finite axiomatizability (Thm 10.2.3), matching the **undecidability** of first-order validity (§39).

> [!example] Example F.3: Low-dimensional fragments are decidable
> The cylindric algebras $\mathsf{CA}_n$ of finite dimension $n$ correspond to the **$n$-variable fragments** of first-order logic. The **two-variable fragment** $\mathrm{FO}^2$ is **decidable** (Mortimer; it has the finite model property), while $\mathrm{FO}^3$ is already **undecidable**. Algebraically, this is the transition at which $\mathsf{RCA}_n$ ceases to be finitely axiomatizable and well-behaved (the gap of Theorem 10.2.3 opens at $\alpha\ge 2$ for representability but the decidability cliff is at three variables). Dimension is therefore the precise algebraic parameter controlling decidability of quantified logic.

> [!remark] Remark F.4: The algebraic-logic dictionary
> The appendix completes a dictionary between logical and algebraic notions used throughout Part III and §28: **theory $\leftrightarrow$ filter/congruence**, **consistency $\leftrightarrow$ proper congruence (nontrivial quotient)**, **completeness theorem $\leftrightarrow$ representation theorem**, **finite model property $\leftrightarrow$ residual finiteness/FMP of the variety**, **decidable fragment $\leftrightarrow$ finite-dimensional or finitely axiomatizable representable subclass**, and **deduction $\leftrightarrow$ equational/quasi-equational derivation**. Under this dictionary the entire metatheory of a logic becomes the structure theory (Part VII) of its algebraic counterpart — the maximal realization of the base treatise's program of treating logic as a specialization of universal algebra, now extended to the quantified case that the base treatise left open.
