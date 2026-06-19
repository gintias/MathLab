---
title: "Theory Skeleton — Sorted Syntax, Binding, Effective Equational Reasoning, and the Coalgebraic Dual"
subtitle: "Bare formal spine: definitions, constructions, theorems; examples, remarks, warnings, and exposition removed"
tags: [universal-algebra, many-sorted, order-sorted, partial-algebra, binding, alpha-equivalence, de-bruijn, nominal-sets, algebraic-logic, cylindric-algebra, unification, term-rewriting, knuth-bendix, tree-automata, coalgebra, coinduction, varieties, clones, lawvere-theories]
---

# Sorted Syntax, Binding, Effective Equational Reasoning, and the Coalgebraic Dual

## 0. Orientation

> [!notation] Skeleton map
> $X \xrightarrow{\eta} T_\Sigma(X) \xrightarrow{\operatorname{ev}_g} A$; $T_\Sigma \dashv U$; $E \leadsto \theta_E \leadsto T_\Sigma(X)/\theta_E$.
> Binding: $\mathrm{Raw}\twoheadrightarrow \mathrm{Raw}/=_\alpha \cong \mathrm{DB} \simeq \mathrm{Nom} \simeq \widehat{\mathbb F}\text{-initial algebra}$.
> Rewriting: termination $+$ local confluence $\Rightarrow$ confluence $\Rightarrow$ unique NF; coalgebra: $\nu H$ gives corecursion/coinduction.

---

## 1. Recapitulation of Prerequisites

### 1.1. Set-Theoretic Conventions

> [!notation] Notation 1.1.1: Ambient conventions
> Work in $\mathsf{ZFC}$.

> [!notation] Notation 1.1.2: Indexed families and dependent products
> For an index set $I$ and sets $(S_i)_{i\in I}$, $\prod_{i\in I}S_i$ is the set of choice functions $i\mapsto s_i\in S_i$ and $\coprod_{i\in I}S_i=\{(i,s):i\in I,\,s\in S_i\}$.

### 1.2. Signatures and Algebras

> [!definition] Definition 1.2.1: Single-sorted signature and $\Omega$-algebra
> A **(single-sorted) sig.** is a pair $\Omega=(\Sigma,\operatorname{ar})$ with $\Sigma$ a set of **op. symbols** and $\operatorname{ar}:\Sigma\to\mathbb N$ the **arity function**; $\Omega_n:=\{f\in\Sigma:\operatorname{ar}(f)=n\}$, and $\Omega_0$ is the set of **constant symbols**. An **$\Omega$-algebra** is a pair $A=(|A|,(f^A)_{f\in\Sigma})$ with carrier $|A|$ and, for each $f\in\Omega_n$, an interpretation $f^A:|A|^n\to|A|$ (so $c^A\in|A|$ for $c\in\Omega_0$).

> [!definition] Definition 1.2.2: Subalgebras, products, generated subalgebra
> $C\subseteq|A|$ is **closed** if it contains $c^A$ for $c\in\Omega_0$ and is closed under each $f^A$; closed sets carry the **subalgebra** structure $C\le A$. The **direct product** $\prod_{i\in I}A_i$ has carrier $\prod_i|A_i|$ with coordinatewise ops. and is the categorical product.

### 1.3. Term Algebra and Universal Mapping Property

> [!definition] Definition 1.3.1: Term algebra and freeness
> For a sig. $\Omega$ and a set $X$ with $X\cap\Sigma=\varnothing$, the set $T_\Omega(X)$ of **terms** is the least set containing $X$ and $\Omega_0$ and closed under $f(t_1,\dots,t_n)$ for $f\in\Omega_n$ ($n\ge1$). The **term algebra** $\mathbf T_\Omega(X)$ has carrier $T_\Omega(X)$, formal ops. $f^{\mathbf T}(t_1,\dots,t_n):=f(t_1,\dots,t_n)$, and insertion $\eta_X:X\to T_\Omega(X)$, $x\mapsto x$.

> [!theorem] Theorem 1.3.2: The term algebra is free; evaluation
> $(\mathbf T_\Omega(X),\eta_X)$ is free on $X$, and any free algebra on $X$ is uniquely isomorphic to it compatibly with the insertion. For an $\Omega$-algebra $B$ and $g:X\to|B|$, the **evaluation hom.** $\operatorname{ev}_g:\mathbf T_\Omega(X)\to B$ is the unique homomorphic extension, satisfying $\operatorname{ev}_g(x)=g(x)$, $\operatorname{ev}_g(c)=c^B$, $\operatorname{ev}_g(f(t_1,\dots,t_n))=f^B(\operatorname{ev}_g(t_1),\dots,\operatorname{ev}_g(t_n))$.

> [!definition] Definition 1.3.3: Subterms, positions, contexts
> The set of **positions** (addresses) of a term $t$ is the finite prefix-closed set $\operatorname{Pos}(t)\subseteq\mathbb N_{>0}^{<\omega}$ defined by $\operatorname{Pos}(x)=\operatorname{Pos}(c)=\{\varepsilon\}$ and $\operatorname{Pos}(f(t_1,\dots,t_n))=\{\varepsilon\}\cup\bigcup_{i=1}^n\{i\cdot p:p\in\operatorname{Pos}(t_i)\}$. The **subterm** at $p$ is $t|_p$; the symbol at $p$ is $t(p)$.

### 1.4. Congruences, Quotients, Equational Logic

> [!definition] Definition 1.4.1: Congruence and quotient
> A **cong.** on $A$ is an equiv. rel. $\theta\subseteq|A|^2$ compatible with every op.: $(a_i,b_i)\in\theta$ for all $i$ implies $(f^A(\bar a),f^A(\bar b))\in\theta$. The **quotient** $A/\theta$ has carrier $|A|/\theta$ and ops. $f^{A/\theta}([\bar a])=[f^A(\bar a)]$, well-defined exactly because $\theta$ is a cong.; $\operatorname{nat}_\theta:A\to A/\theta$ is the canonical surjection.

> [!definition] Definition 1.4.2: Equations, presentations, identities
> An **equation** over $(\Omega,X)$ is a pair $s\approx t\in T_\Omega(X)^2$. For $E\subseteq T_\Omega(X)^2$, $\theta_E:=\operatorname{Cg}(E)$ is the least cong. containing $E$ and $\langle X\mid E\rangle:=\mathbf T_\Omega(X)/\theta_E$ the **presented algebra**.

> [!definition] Definition 1.4.3: Substitution as evaluation into syntax
> A **subst.** $\sigma:X\to T_\Omega(Y)$ induces the hom. $\widehat\sigma=\operatorname{ev}_\sigma:\mathbf T_\Omega(X)\to\mathbf T_\Omega(Y)$, written $t\mapsto t\sigma$ (postfix), with $x\sigma=\sigma(x)$, $c\sigma=c$, $f(\bar t)\sigma=f(\overline{t\sigma})$. The composite of $\sigma:X\to T_\Omega(Y)$ and $\tau:Y\to T_\Omega(Z)$ is $(\sigma;\tau)(x)=(\sigma(x))\tau$, giving $t(\sigma;\tau)=(t\sigma)\tau$; this is the Kleisli composition of the **term monad** $(T,\eta,\mu)$ with $T(X)=T_\Omega(X)$.

### 1.5. Companion Notation

> [!notation] Notation 1.5.1: Conventions specific to this companion
> Substitutions act on the right ($t\sigma$), composition of substs. is written $\sigma;\tau$ ("first $\sigma$, then $\tau$"), and $\{x_1\mapsto t_1,\dots,x_k\mapsto t_k\}$ denotes the subst. sending the listed variables as shown and every other variable to itself; its **domain** is $\{x_i:x_i\ne t_i\}$ and its **range variables** are $\bigcup_i\operatorname{var}(t_i)$.

---

# Part I — Sorted and Partial Carriers of Syntax

## 2. Many-Sorted Algebra

### 2.1. Sorted Signatures

> [!definition] Definition 2.1.1: Many-sorted signature
> Fix a set $S$ of **sorts**. An **$S$-sorted sig.** is a pair $\Sigma=(\mathrm{Op},\operatorname{type})$ where $\mathrm{Op}$ is a set of **op. symbols** and
> $$
> \operatorname{type}:\mathrm{Op}\to S^{<\omega}\times S
> $$

> [!notation] Notation 2.1.2: Sort words and arity
> For $w=s_1\cdots s_n\in S^{<\omega}$, the **length** $|w|=n$ is the **arity** of any $f:w\to s$.

### 2.2. Sorted Algebras and Homomorphisms

> [!definition] Definition 2.2.1: $\Sigma$-algebra (many-sorted)
> A **$\Sigma$-algebra** $A$ consists of an $S$-indexed family of **carrier sets** $(|A|_s)_{s\in S}$ and, for each $f:s_1\cdots s_n\to s$ in $\mathrm{Op}$, a function
> $$
> f^A:|A|_{s_1}\times\cdots\times|A|_{s_n}\to|A|_s,
> $$

> [!definition] Definition 2.2.2: Sorted homomorphism
> A **hom.** $h:A\to B$ of $\Sigma$-algebras is an $S$-indexed family $(h_s:|A|_s\to|B|_s)_{s\in S}$ of functions s.t. ∀ $f:s_1\cdots s_n\to s$ and all $a_i\in|A|_{s_i}$,
> $$
> h_s\big(f^A(a_1,\dots,a_n)\big)=f^B\big(h_{s_1}(a_1),\dots,h_{s_n}(a_n)\big).
> $$

> [!definition] Definition 2.2.3: Sorted subalgebras and products
> A **sorted subset** $C=(C_s)_{s}$ with $C_s\subseteq|A|_s$ is **closed** if $f^A(\bar a)\in C_s$ whenever $f:w\to s$ and the $a_i$ lie in the corresponding $C_{s_i}$ (including $f^A\in C_s$ for constants). Closed sorted subsets carry subalgebra structure $C\le A$.

### 2.3. Sorted Terms and the Sorted Term Algebra

> [!definition] Definition 2.3.1: Sorted variables and sorted terms
> A **sorted variable family** is an $S$-indexed family $X=(X_s)_s$ of pairwise-disjoint sets, disjoint from $\mathrm{Op}$. The $S$-indexed family $T_\Sigma(X)=(T_\Sigma(X)_s)_s$ of **sorted terms** is the least family closed under:
> $$
> \textbf{(var)}\ x\in T_\Sigma(X)_s \text{ for } x\in X_s;\qquad \textbf{(op)}\ \frac{t_1\in T_\Sigma(X)_{s_1}\ \cdots\ t_n\in T_\Sigma(X)_{s_n}}{f(t_1,\dots,t_n)\in T_\Sigma(X)_s}\ \ (f:s_1\cdots s_n\to s).
> $$

> [!construction] Construction 2.3.2: Sorted term algebra
> $\mathbf T_\Sigma(X)$ is the $\Sigma$-algebra with carrier $(T_\Sigma(X)_s)_s$, formal ops. $f^{\mathbf T}(t_1,\dots,t_n):=f(t_1,\dots,t_n)$, and sorted insertion $\eta_X=(\eta_{X,s})_s$, $\eta_{X,s}(x):=x$ for $x\in X_s$.

> [!theorem] Theorem 2.3.3: Sorted universal mapping property
> $(\mathbf T_\Sigma(X),\eta_X)$ is the **free $\Sigma$-algebra on the sorted set $X$**: ∀ $\Sigma$-algebra $A$ and every **sorted assignment** $g=(g_s:X_s\to|A|_s)_s$ there is a unique hom. $\operatorname{ev}_g:\mathbf T_\Sigma(X)\to A$ with $\operatorname{ev}_g\circ\eta_X=g$, given sortwise by the recursive clauses of Theorem 1.3.2. Consequently $\mathbf T_\Sigma(-):\mathbf{Set}^S\to\mathbf{Alg}(\Sigma)$ is left adjoint to the forgetful functor $\mathbf{Alg}(\Sigma)\to\mathbf{Set}^S$.

> [!definition] Definition 2.3.4: Sorted polynomial functor
> The **sorted sig. endofunctor** $H_\Sigma:\mathbf{Set}^S\to\mathbf{Set}^S$ is
> $$
> \big(H_\Sigma Y\big)_s \;:=\; \coprod_{f:\,s_1\cdots s_n\to s}\ Y_{s_1}\times\cdots\times Y_{s_n}\qquad(s\in S).
> $$

### 2.4. Sorted Congruences and Quotients

> [!definition] Definition 2.4.1: Sorted congruence and quotient
> A **(sorted) cong.** on $A$ is an $S$-indexed family $\theta=(\theta_s)_s$ with each $\theta_s$ an equiv. rel. on $|A|_s$, compatible with every op.: for $f:s_1\cdots s_n\to s$, $(a_i,b_i)\in\theta_{s_i}$ for all $i$ implies $(f^A(\bar a),f^A(\bar b))\in\theta_s$. The **quotient** $A/\theta$ has carrier $(|A|_s/\theta_s)_s$ with ops. on classes, well-defined exactly by compatibility; $\operatorname{nat}_\theta:A\to A/\theta$ is the sortwise canonical surjection.

> [!theorem] Theorem 2.4.2: Sorted isomorphism theorems
> For $h:A\to B$, $\ker h:=(\{(a,a'):h_s(a)=h_s(a')\})_s$ is a sorted cong., $\operatorname{im}(h)\le B$, and there is a unique isomorphism $A/\ker h\cong\operatorname{im}(h)$ with $[a]\mapsto h(a)$. The correspondence theorem and the second/third isomorphism theorems hold sortwise.

### 2.5. Sorted Substitution and the Sorted Term Monad

> [!definition] Definition 2.5.1: Sorted substitution
> A **sorted subst.** $\sigma:X\to T_\Sigma(Y)$ is a sort-respecting family $(\sigma_s:X_s\to T_\Sigma(Y)_s)_s$; its induced hom. $\widehat\sigma:\mathbf T_\Sigma(X)\to\mathbf T_\Sigma(Y)$ is the evaluation of Theorem 2.3.3 with target $\mathbf T_\Sigma(Y)$. Composition $\sigma;\tau$ is Kleisli composition, and $(T_\Sigma,\eta,\mu)$ is a monad on $\mathbf{Set}^S$, the **sorted term monad**, whose Eilenberg–Moore cat. is $\mathbf{Alg}(\Sigma)$.

### 2.6. Sorted Equational Logic and the Empty-Carrier Anomaly

> [!definition] Definition 2.6.1: Sorted equation and satisfaction
> A **sorted equation** is a triple $(\Gamma,s,t)$ — usually written $\Gamma\vdash s\approx t$ or $(\forall\Gamma)\,s\approx t$ — where $\Gamma$ is a finite sorted set of variables (the **explicit context**), $s,t\in T_\Sigma(\Gamma)_\sigma$ are terms of a common sort $\sigma$. A $\Sigma$-algebra $A$ **satisfies** $(\Gamma,s,t)$ if $\operatorname{ev}_v(s)=\operatorname{ev}_v(t)$ ∀ assignment $v:\Gamma\to|A|$.

> [!theorem] Theorem 2.6.2: Sound and complete sorted equational calculus
> With equations carrying explicit contexts as in Definition 2.6.1, the rules reflexivity, symmetry, transitivity, cong., and subst. — each respecting sorts and contexts — are **sound and complete** for many-sorted equational consequence: $E\vdash(\Gamma,s,t)\iff E\models(\Gamma,s,t)$. The free algebra of the variety defined by $E$ on a sorted set $X$ is $\mathbf T_\Sigma(X)/\theta^{\mathrm{fi}}_E$ with $\theta^{\mathrm{fi}}_E$ the least fully invariant sorted cong. containing $E$.

---

## 3. Order-Sorted Algebra

### 3.1. Sort Orders and Order-Sorted Signatures

> [!definition] Definition 3.1.1: Sort poset and order-sorted signature
> An **order-sorted sig.** is a triple $\Sigma=(S,\le,\mathrm{Op})$ where $(S,\le)$ is a poset of **sorts** (with $\le$ read as **subsort inclusion**) and $\mathrm{Op}$ is an $S$-sorted op.-symbol family (Definition 2.1.1) on the underlying set $S$. A symbol $f$ may be **overloaded**: it may carry several declarations $f:w_1\to s_1$, $f:w_2\to s_2$, $\dots$ with different profiles.

> [!definition] Definition 3.1.2: Subsort-overloading coherence (monotonicity)
> A sig. is **monotone** (subsort-monotone) if whenever $f:w_1\to s_1$ and $f:w_2\to s_2$ are declarations with $w_1\le w_2$ componentwise (same length, $i$-th sorts comparable), then $s_1\le s_2$. Monotonicity ensures that narrowing the input sorts never widens the output sort and is the basic compatibility condition relating overloaded declarations along $\le$.

> [!definition] Definition 3.1.3: Regularity
> $\Sigma$ is **regular** if ∀ symbol $f$ and every input profile $w_0\in S^{<\omega}$ that is below some declared profile of $f$, the set $\{(w,s):f:w\to s,\ w_0\le w\}$ has a **least element**. Regularity guarantees that each well-typed application has a least output sort; it is the order-sorted prerequisite for least-sort assignment (Theorem 3.3.2).

### 3.2. Order-Sorted Algebras

> [!definition] Definition 3.2.1: Order-sorted $\Sigma$-algebra
> An **order-sorted $\Sigma$-algebra** $A$ is a many-sorted algebra for the underlying sorted sig. (Definition 2.2.1) s.t.:
> $$
> \textbf{(subsort inclusion)}\quad s\le s'\ \Longrightarrow\ |A|_s\subseteq|A|_{s'},
> $$
> $$
> \textbf{(operation agreement)}\quad f:w_1\to s_1,\ f:w_2\to s_2,\ \bar a\in|A|^{w_1}\cap|A|^{w_2}\ \Longrightarrow\ f^{A}_{w_1}(\bar a)=f^{A}_{w_2}(\bar a).
> $$

### 3.3. Order-Sorted Terms and Least Sorts

> [!definition] Definition 3.3.1: Order-sorted terms
> Fix a sorted variable family $X$ with $x\in X_s$ having declared sort $s$. The **order-sorted terms** are generated by: every $x\in X_s$ is a term of sort $s$; and if $t_i$ is a term of some sort $s_i'\le s_i$ for a declaration $f:s_1\cdots s_n\to s$, then $f(t_1,\dots,t_n)$ is a term of sort $s$.

> [!theorem] Theorem 3.3.2: Least-sort theorem
> If $\Sigma$ is regular (Definition 3.1.3), every well-formed order-sorted term $t$ has a **least sort** $\mathrm{ls}(t)\in S$: the set of sorts of $t$ has a minimum, and $\mathrm{ls}(t)\le s$ ∀ sort $s$ of $t$. Least sorts are computed bottom-up: $\mathrm{ls}(x)=s$ for $x\in X_s$, and $\mathrm{ls}(f(\bar t))$ is the least result sort among declarations of $f$ whose input profile dominates $(\mathrm{ls}(t_i))_i$.

> [!construction] Construction 3.3.3: Order-sorted term algebra and freeness
> The **order-sorted term algebra** $\mathbf T_\Sigma(X)$ assigns to each sort $s$ the set of well-formed terms of some sort $\le s$ (so subsort inclusion holds), with formal ops. and insertion as before. It is the free order-sorted $\Sigma$-algebra on $X$: every sort-respecting assignment $g$ extends uniquely to an order-sorted hom. $\operatorname{ev}_g$.

### 3.4. Retracts, Sort Constraints, and Errors

> [!definition] Definition 3.4.1: Retracts
> When a term is well-formed only after a sort can be **lowered** (e.g. dividing two integers and asserting the result is a natural), specification languages add **retract** symbols $r_{s'\!,s}:s'\to s$ for $s\le s'$, interpreted as partial inclusions (identity on $|A|_s\subseteq|A|_{s'}$, undefined elsewhere). Retracts turn ill-sorted-but-intended applications into terms with explicit, checkable sort-lowering obligations, evaluated by the partial-algebra machinery of §4.

---

## 4. Partial Algebras

### 4.1. Partial Operations and Homomorphisms

> [!definition] Definition 4.1.1: Partial $\Omega$-algebra
> For a (single- or many-sorted) sig. $\Omega$, a **partial $\Omega$-algebra** $A$ assigns to each $f\in\Omega_n$ a **partial function** $f^A:|A|^n\rightharpoonup|A|$ with domain of definition $\operatorname{dom}(f^A)\subseteq|A|^n$. A constant may be **undefined**.

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

### 4.2. Existence Equations and Conditional Axioms

> [!definition] Definition 4.2.1: Existence equation and ECE-equation
> An **existence equation (e-equation)** over $X$ is a formula $s\stackrel{e}{=}t$ asserting both sides defined and equal; the special case $t\stackrel{e}{=}t$, abbreviated $\mathrm{def}(t)$ or $t{\downarrow}$, asserts mere definedness. An **existentially conditioned existence equation (ECE-equation)** has the form
> $$
> \big(\textstyle\bigwedge_{j} \mathrm{def}(r_j)\big)\ \Rightarrow\ s\stackrel{e}{=}t,
> $$

> [!theorem] Theorem 4.2.2: Existence and structure of initial partial models
> For any sig. $\Omega$ and any set $E$ of ECE-equations, the cat. of partial $\Omega$-algebras satisfying $E$ (with closed homs.) has an **initial object**, constructed as a quotient of the partial term algebra (Construction 4.3.2) by the least **closed cong.** (Definition 4.3.1) generated by $E$. The Birkhoff-style characterization holds: ECE-definable classes are exactly those closed under suitable products, closed subalgebras, and closed-homomorphic images (Andréka–Németi / Burmeister theory).

### 4.3. Partial Term Algebras and Closed Congruences

> [!definition] Definition 4.3.1: Closed congruence
> A **closed cong.** on a partial algebra $A$ is an equiv. $\theta$ on the **defined elements** that is compatible with each $f^A$ in the strict sense: if $\bar a,\bar b\in\operatorname{dom}(f^A)$ and $a_i\mathbin\theta b_i$ then $f^A(\bar a)\mathbin\theta f^A(\bar b)$, with no requirement when an application is undefined. The quotient $A/\theta$ is a partial algebra whose ops. are defined exactly on classes of defined applications.

> [!construction] Construction 4.3.2: Free partial algebra
> The **free total** term algebra $\mathbf T_\Omega(X)$ is also the free *partial* algebra on $X$ in which every op. is total; the free partial algebra subject to a definedness specification is its quotient by the least closed cong. enforcing the prescribed undefinedness. Evaluation $\operatorname{ev}_g:\mathbf T_\Omega(X)\rightharpoonup A$ into a partial algebra is the **partial** homomorphic extension, defined on $t$ iff every op. applied in $t$ stays within the relevant $\operatorname{dom}(f^A)$ under $g$ (strictness).

---

# Part II — Syntax with Binding

## 5. The Binding Problem

### 5.1. Raw Terms with Binders

> [!definition] Definition 5.1.1: Binding signature
> A **binding sig.** is a set $\mathcal O$ of **operators** together with a **binding arity** for each: $o:(k_1,\dots,k_m)$ assigns to $o$ a finite list of natural numbers, where $o$ takes $m$ arguments and **binds $k_i$ variables in its $i$-th argument**. An ordinary $n$-ary op. symbol is the case $(0,\dots,0)$ ($n$ zeros).

> [!definition] Definition 5.1.2: Raw terms (pre-terms)
> Fix a countably infinite set $\mathbb A$ of **atoms** (variable names). The set $\mathrm{Raw}_{\mathcal O}(\mathbb A)$ of **raw terms** is the least set with $a\in\mathrm{Raw}$ for $a\in\mathbb A$ and, for $o:(k_1,\dots,k_m)$ and raw terms $t_1,\dots,t_m$ together with binder-name lists $\vec a_i\in\mathbb A^{k_i}$,
> $$
> o\big((\vec a_1)t_1,\ \dots,\ (\vec a_m)t_m\big)\in\mathrm{Raw}_{\mathcal O}(\mathbb A),
> $$

> [!definition] Definition 5.1.3: Free variables and binding scope
> The **free-variable** map $\mathrm{fv}:\mathrm{Raw}_{\mathcal O}(\mathbb A)\to\mathcal P_{\mathrm{fin}}(\mathbb A)$ is defined by recursion: $\mathrm{fv}(a)=\{a\}$ and
> $$
> \mathrm{fv}\big(o((\vec a_1)t_1,\dots,(\vec a_m)t_m)\big)=\bigcup_{i=1}^m\big(\mathrm{fv}(t_i)\setminus\{\text{names in }\vec a_i\}\big).
> $$

### 5.2. $\alpha$-Equivalence

> [!definition] Definition 5.2.1: $\alpha$-equivalence
> **$\alpha$-equiv.** $=_\alpha$ is the least equiv. rel. on $\mathrm{Raw}_{\mathcal O}(\mathbb A)$ that is compatible with all operators and identifies terms differing only by a **consistent renaming of bound names by fresh names**. For a single binder, the generating clause is: if $c$ does not occur free in $t$ and is not captured, then
> $$
> o(\dots,(a)\,t,\dots)\ =_\alpha\ o(\dots,(c)\,t[a{:=}c],\dots),
> $$

> [!definition] Definition 5.2.2: The syntax with binding
> The **abstract syntax with binding** generated by $\mathcal O$ over atoms $\mathbb A$ is the quotient set
> $$
> \Lambda_{\mathcal O}(\mathbb A)\ :=\ \mathrm{Raw}_{\mathcal O}(\mathbb A)\big/=_\alpha.
> $$

### 5.3. Capture-Avoiding Substitution

> [!definition] Definition 5.3.1: Capture-avoiding substitution
> **Capture-avoiding subst.** $t[a{:=}s]$ on $\Lambda_{\mathcal O}(\mathbb A)$ is defined on representatives by: $a[a{:=}s]=s$; $b[a{:=}s]=b$ for $b\ne a$; commutation with non-binding operators; and, for a binder,
> $$
> \big(o(\dots,(b)\,t,\dots)\big)[a{:=}s]\ =\ o\big(\dots,(b')\,(t[b{:=}b'])[a{:=}s],\dots\big),
> $$

> [!theorem] Theorem 5.3.2: Substitution lemma for binding syntax
> On $\Lambda_{\mathcal O}(\mathbb A)$, for distinct atoms $a\ne b$ with $a\notin\mathrm{fv}(u)$,
> and renaming, weakening, and the identity $t[a{:=}a]=t$ hold.
> $$
> t[a{:=}s][b{:=}u]\ =\ t[b{:=}u]\,[a{:=}s[b{:=}u]],
> $$

---

## 6. De Bruijn Presentation

### 6.1. Nameless Terms

> [!definition] Definition 6.1.1: De Bruijn terms
> Fix a binding sig. $\mathcal O$. The set $\mathrm{DB}_{\mathcal O}$ of **de Bruijn terms** is the least set with $\underline n\in\mathrm{DB}_{\mathcal O}$ ∀ **index** $n\in\mathbb N$ and, for $o:(k_1,\dots,k_m)$ and $u_1,\dots,u_m\in\mathrm{DB}_{\mathcal O}$,
> $$
> o(u_1,\dots,u_m)\in\mathrm{DB}_{\mathcal O},
> $$

> [!definition] Definition 6.1.2: Shifting (lifting)
> The **shift** $\uparrow^d_c:\mathrm{DB}_{\mathcal O}\to\mathrm{DB}_{\mathcal O}$ with **cutoff** $c$ and **amount** $d$ adds $d$ to every free index $\ge c$, recursing under binders by raising the cutoff:
> $$
> \uparrow^d_c(\underline n)=\begin{cases}\underline n & n<c\\ \underline{n+d} & n\ge c\end{cases},\qquad \uparrow^d_c\big(o(\dots,u_i,\dots)\big)=o\big(\dots,\uparrow^d_{\,c+k_i}(u_i),\dots\big).
> $$

### 6.2. De Bruijn Substitution

> [!definition] Definition 6.2.1: Index substitution
> The subst. of de Bruijn term $s$ for index $j$ in $u$, written $u\{j\mapsto s\}$, is
> $$
> \underline n\{j\mapsto s\}=\begin{cases}\underline n & n<j\\ s & n=j\\ \underline{n-1} & n>j\end{cases},\qquad o(\dots,u_i,\dots)\{j\mapsto s\}=o\big(\dots,u_i\{\,j+k_i\mapsto\ \uparrow^{k_i}_{0}s\,\},\dots\big),
> $$

> [!theorem] Theorem 6.2.2: Adequacy of the de Bruijn encoding
> Fix an enumeration of $\mathbb A$. The encoding $\llbracket-\rrbracket:\mathrm{Raw}_{\mathcal O}(\mathbb A)\to\mathrm{DB}_{\mathcal O}$ that replaces each bound occurrence by its binder distance and each free atom by a fixed index satisfies
> $$
> s\ =_\alpha\ t\quad\Longleftrightarrow\quad \llbracket s\rrbracket=\llbracket t\rrbracket,
> $$

### 6.3. Terms-in-Context and the Presheaf View

> [!definition] Definition 6.3.1: The category of contexts
> Let $\mathbb F$ be the cat. whose objects are natural numbers $n$ (read as a context of $n$ free de Bruijn variables $\underline 0,\dots,\underline{n-1}$) and whose morphisms $n\to n'$ are **functions** $\{0,\dots,n-1\}\to\{0,\dots,n'-1\}$ (variable renamings/reindexings); the subcategory $\mathbb I$ uses only **injections**. A **presheaf** $P:\mathbb F^{\mathrm{op}}\to\mathbf{Set}$ (or $P:\mathbb I^{\mathrm{op}}\to\mathbf{Set}$) is a family $(P(n))_n$ of "terms with at most $n$ free variables" with functorial reindexing.

> [!construction] Construction 6.3.2: The de Bruijn term presheaf
> Define $\mathbf{Db}_{\mathcal O}:\mathbb F^{\mathrm{op}}\to\mathbf{Set}$ by $\mathbf{Db}_{\mathcal O}(n)=\{u\in\mathrm{DB}_{\mathcal O}:\text{all free indices of }u\text{ are }<n\}$, with reindexing along $\rho:n\to n'$ acting on free indices. The **variable** presheaf is $V$ with $V(n)=\{0,\dots,n-1\}$.

---

## 7. Nominal Sets

### 7.1. Permutation Actions, Support, Freshness

> [!definition] Definition 7.1.1: The permutation group and $G$-sets
> Fix a countably infinite set $\mathbb A$ of **atoms**. Let $\mathbb S=\mathrm{Sym}_{\mathrm{fin}}(\mathbb A)$ be the group of **finite permutations** of $\mathbb A$ (bijections moving only finitely many atoms), generated by the **transpositions (swaps)** $(a\ b)$.

> [!definition] Definition 7.1.2: Support and finite support
> For an $\mathbb S$-set $Z$ and $z\in Z$, a set $A\subseteq\mathbb A$ **supports** $z$ if every $\pi$ fixing $A$ pointwise satisfies $\pi\cdot z=z$. $z$ is **finitely supported** if some finite $A$ supports it; then there is a **least** finite support $\operatorname{supp}(z)$.

> [!definition] Definition 7.1.3: Freshness
> For $a\in\mathbb A$ and $z$ in a nominal set, $a$ is **fresh for** $z$, written $a\mathbin\#z$, iff $a\notin\operatorname{supp}(z)$. Freshness abstracts "$a$ does not occur free in $z$": it is the support-theoretic, representation-independent form of non-occurrence.

> [!definition] Definition 7.1.4: Equivariance and the freshness quantifier
> A map $f:Z\to W$ of nominal sets is **equivariant** if $f(\pi\cdot z)=\pi\cdot f(z)$ for all $\pi,z$; equivariant maps preserve support ($\operatorname{supp}(f(z))\subseteq\operatorname{supp}(z)$). The **freshness quantifier** "$\mathsf{N}a.\,\Phi(a)$" ("**for some/any fresh $a$**") asserts that $\Phi(a)$ holds for all but finitely many $a\in\mathbb A$; on finitely supported predicates "for some fresh $a$" and "for all fresh $a$" coincide, which is the defining property of $\mathsf{N}$.

### 7.2. Atom Abstraction and the Nominal Binder

> [!construction] Construction 7.2.1: Atom-abstraction
> For a nominal set $Z$, the **atom-abstraction** $[\mathbb A]Z$ has underlying set the quotient of $\mathbb A\times Z$ by
> $$
> (a,z)\sim(b,w)\quad\Longleftrightarrow\quad \big(a=b\wedge z=w\big)\ \text{ or }\ \big(a\#w\ \wedge\ (a\ b)\cdot w=z\big),
> $$

> [!theorem] Theorem 7.2.2: Abstraction realizes $\alpha$-equivalence as equality
> The constr. $[\mathbb A](-)$ is functorial on nominal sets, and for the syntax of a binding sig. it satisfies the defining binder law
> which is exactly $\alpha$-equiv. of single binders.
> $$
> \langle a\rangle z=\langle b\rangle w\quad\Longleftrightarrow\quad \big(a=b\wedge z=w\big)\vee\big(a\#w\wedge z=(a\ b)\cdot w\big),
> $$

### 7.3. The Nominal Term Algebra and Recursion

> [!construction] Construction 7.3.1: Nominal term algebra
> Given a binding sig. $\mathcal O$, the **nominal abstract syntax** $\Lambda^{\mathrm{nom}}_{\mathcal O}$ is the initial algebra, in the cat. $\mathbf{Nom}$ of nominal sets, of the functor
> $$
> T(Z)\ =\ \mathbb A\ +\ \coprod_{o:(k_1,\dots,k_m)}\ \prod_{i=1}^m [\mathbb A]^{k_i}Z,
> $$

> [!theorem] Theorem 7.3.2: Nominal structural recursion (Pitts)
> Let $Z$ be a nominal set equipped with: an equivariant **variable map** $f_{\mathrm{var}}:\mathbb A\to Z$; and for each operator $o:(k_1,\dots,k_m)$ an equivariant **operator map** $f_o$ defined on tuples of (abstractions of) elements of $Z$, satisfying the **freshness condition for binders (FCB)**: the bound atoms are fresh for the result of $f_o$. Then there is a **unique** equivariant hom. $h:\Lambda^{\mathrm{nom}}_{\mathcal O}\to Z$ respecting all constructors, defined by recursion **using bound names directly** (choosing them fresh).

---

## 8. Binding Signatures and Second-Order Abstract Syntax

### 8.1. The Substitution Tensor and Monoids

> [!definition] Definition 8.1.1: Context category and presheaf category
> Let $\mathbb F$ be the cat. of finite cardinals and all functions (Definition 6.3.1); the presheaf cat. is $\widehat{\mathbb F}:=\mathbf{Set}^{\mathbb F}$ (covariant) or $\mathbf{Set}^{\mathbb F^{\mathrm{op}}}$ depending on convention. The **presheaf of variables** is $V\in\widehat{\mathbb F}$ with $V(n)=\{0,\dots,n-1\}$ (the representable on $1$).

> [!definition] Definition 8.1.2: Substitution tensor product
> The **subst. tensor** $\otimes$ on $\widehat{\mathbb F}$ is
> $$
> (P\otimes Q)(n)\ :=\ \int^{m\in\mathbb F} P(m)\times Q(n)^{m},
> $$

> [!definition] Definition 8.1.3: Monoid = object with substitution
> A **monoid** $(P,\nu:V\to P,\varsigma:P\otimes P\to P)$ in $(\widehat{\mathbb F},\otimes,V)$ is an object $P$ ("terms") with a **variable-inclusion** $\nu$ (the unit, "a variable is a term") and a **subst.** $\varsigma$ (the multiplication) satisfying associativity and unit laws. This is exactly an internal model of subst.: $\varsigma$ takes a term over $m$ variables and an $m$-tuple of terms and returns the simultaneous subst..

### 8.2. Binding-Signature Functors and Initiality

> [!definition] Definition 8.2.1: The binding-signature endofunctor
> For a binding sig. $\mathcal O$, define $\Sigma_{\mathcal O}:\widehat{\mathbb F}\to\widehat{\mathbb F}$ by
> $$
> \Sigma_{\mathcal O}(P)\ :=\ \coprod_{o:(k_1,\dots,k_m)}\ \prod_{i=1}^m \delta^{k_i}P,\qquad (\delta P)(n):=P(n+1),
> $$

> [!theorem] Theorem 8.2.2: Initial-algebra abstract syntax (Fiore–Plotkin–Turi)
> The endofunctor $V+\Sigma_{\mathcal O}$ on $\widehat{\mathbb F}$ has an **initial algebra** $\mathbf{Syn}_{\mathcal O}$, the **abstract syntax with binding** of $\mathcal O$. It carries a canonical monoid structure (Definition 8.1.3): the unit is variable inclusion and the multiplication is **capture-avoiding simultaneous subst.**, which is the unique monoid structure compatible with the operators.

> [!theorem] Theorem 8.2.3: Initiality is structural recursion with binding
> For any $(V+\Sigma_{\mathcal O})$-algebra $A$ in $\widehat{\mathbb F}$ there is a unique algebra hom. $\mathbf{Syn}_{\mathcal O}\to A$. This is the **struc. recursion principle** for binding syntax: specifying an action on variables and on each operator (in extended contexts) determines a unique context-respecting map out of the syntax.

### 8.3. Second-Order Syntax, Equations, and HOAS

> [!definition] Definition 8.3.1: Second-order equational logic
> A **second-order equation** is an equation between terms-in-context with **metavariables** that may themselves take arguments (representing terms with holes for bound variables). The associated deduction system extends Birkhoff's calculus with rules for subst. under binders.

> [!definition] Definition 8.3.2: Higher-order abstract syntax (HOAS)
> **HOAS** represents object-level binders by meta-level functions: e.g. $\mathrm{lam}:(\mathrm{tm}\to\mathrm{tm})\to\mathrm{tm}$, so an object binder becomes a meta-level function space. This makes object-level subst. into meta-level application and reuses the meta-language's $\alpha$-renaming.

---

# Part III — Algebraic Logic

## 9. From Lindenbaum–Tarski to Algebraic Logic

### 9.1. The Lindenbaum–Tarski Construction Abstractly

> [!definition] Definition 9.1.1: Lindenbaum–Tarski algebra of a logic
> For a logic $\mathcal L$ with formula set $\mathrm{Fm}$ and a consequence/provability relation determining an equiv. "interprovability" $\dashv\vdash$, the **Lindenbaum–Tarski algebra** is $\mathrm{Fm}/{\dashv\vdash}$, equipped with ops. induced by the connectives (well-defined iff $\dashv\vdash$ is a cong. for them). For classical propositional logic this is a Boolean algebra; for intuitionistic, a Heyting algebra; for modal $\mathbf K$, a modal (Boolean-with-operator) algebra.

> [!definition] Definition 9.1.2: Algebraizable logic (schematic)
> A logic is **algebraizable** (Blok–Pigozzi) when there are translations $\tau$ (formulas to equations) and $\rho$ (equations to formulas) and an equivalent quasivariety $\mathsf K$ s.t. provability $\vdash_{\mathcal L}$ corresponds to equational consequence $\models_{\mathsf K}$ and the two translations are mutually inverse modulo the respective consequence relations. Classical propositional logic is algebraizable with $\mathsf K=$ Boolean algebras and $\tau(\varphi)=(\varphi\approx\top)$; the algebraic counterpart is then governed entirely by §19's variety theory.

### 9.2. The Need for Dimension

> [!definition] Definition 9.2.1: Dimension
> The **dimension** of an algebraic-logic structure is an ordinal $\alpha$ indexing the variables $\{v_i:i<\alpha\}$ of the logic; the sig. contains one cylindrification (or quantifier) operator and a family of diagonal/subst. operators **per index** (or per pair of indices). First-order logic over a countable variable supply has dimension $\omega$.

---

## 10. Cylindric Algebras

### 10.1. The Cylindric Axioms

> [!definition] Definition 10.1.1: Cylindric algebra
> Fix an ordinal $\alpha$ (the dimension). A **cylindric algebra of dimension $\alpha$** is a structure
> $$
> \mathfrak A=\big(A,\ +,\ \cdot,\ -,\ 0,\ 1,\ (\mathsf c_i)_{i<\alpha},\ (\mathsf d_{ij})_{i,j<\alpha}\big)
> $$
> $$
> \textbf{(C1)}\ \mathsf c_i 0=0;\qquad \textbf{(C2)}\ x\le \mathsf c_i x;\qquad \textbf{(C3)}\ \mathsf c_i(x\cdot \mathsf c_i y)=\mathsf c_i x\cdot \mathsf c_i y;
> $$
> $$
> \textbf{(C4)}\ \mathsf c_i\mathsf c_j x=\mathsf c_j\mathsf c_i x;\qquad \textbf{(C5)}\ \mathsf d_{ii}=1;
> $$
> $$
> \textbf{(C6)}\ i\notin\{j,k\}\ \Rightarrow\ \mathsf d_{jk}=\mathsf c_i(\mathsf d_{ji}\cdot \mathsf d_{ik});\qquad \textbf{(C7)}\ i\ne j\ \Rightarrow\ \mathsf c_i(\mathsf d_{ij}\cdot x)\cdot \mathsf c_i(\mathsf d_{ij}\cdot -x)=0.
> $$

### 10.2. Set Cylindric Algebras and Representation

> [!construction] Construction 10.2.1: Cylindric set algebra
> Let $U$ be a set and $\alpha$ an ordinal; consider subsets of $U^\alpha$ ($\alpha$-ary relations). The **cylindric set algebra** on $U$ has carrier a Boolean subalgebra of $\mathcal P(U^\alpha)$ closed under the ops.
> $$
> \mathsf c_i R=\{s\in U^\alpha:\exists u\in U,\ s(i{:=}u)\in R\}\quad(\text{cylindrification along axis }i),
> $$
> $$
> \mathsf d_{ij}=\{s\in U^\alpha:s_i=s_j\}\quad(\text{diagonal}),
> $$

> [!definition] Definition 10.2.2: Representable cylindric algebras
> A cylindric algebra is **representable** if it embeds into a product of cylindric set algebras; $\mathsf{RCA}_\alpha$ is the class of representable algebras of dimension $\alpha$. $\mathsf{RCA}_\alpha$ is exactly the class arising from genuine $\alpha$-ary relations, i.e. the algebras that "are" Boolean algebras of definable relations on structures.

> [!theorem] Theorem 10.2.3: The representation gap (Monk, Tarski)
> For $\alpha\ge 2$:
> i.e. there exist cylindric algebras satisfying all finitely many schematic axioms (C1)–(C7) that are **not** representable.
> $$
> \mathsf{RCA}_\alpha\ \subsetneq\ \mathsf{CA}_\alpha,
> $$

### 10.3. The Lindenbaum Cylindric Algebra of First-Order Logic

> [!construction] Construction 10.3.1: Cylindric algebra of a first-order theory
> For a first-order theory $\Theta$ in a language with variables $\{v_i:i<\omega\}$, define the **Lindenbaum–Tarski cylindric algebra** $\mathfrak{Lt}(\Theta)$: carrier the formulas modulo $\Theta$-provable equiv., Boolean ops. from the connectives, $\mathsf c_i=[\exists v_i\,(-)]$, $\mathsf d_{ij}=[v_i\doteq v_j]$. The axioms (C1)–(C7) hold because they are provable schemata of first-order logic with equality; $\mathfrak{Lt}(\Theta)\in\mathsf{CA}_\omega$.

> [!theorem] Theorem 10.3.2: Locally finite-dimensional algebras correspond to first-order theories
> An element $x$ of a $\mathsf{CA}_\omega$ has **dimension set** $\Delta x=\{i:\mathsf c_i x\ne x\}$ (the indices that "matter"); the algebra is **locally finite-dimensional** ($\mathsf{Lf}_\omega$) if every element has finite dimension set (the algebraic form of "each formula has finitely many free variables"). The Lindenbaum algebras $\mathfrak{Lt}(\Theta)$ are exactly (up to isomorphism) the locally finite-dimensional, **representable** cylindric algebras of dimension $\omega$ with countably many generators; this is the precise sense in which first-order logic **is** an equational theory of cylindric algebras.

---

## 11. Polyadic and Quantifier Algebras

### 11.1. Polyadic Algebras

> [!definition] Definition 11.1.1: Polyadic algebra
> Fix a set $I$ of variables. A **polyadic algebra** of degree $I$ is a Boolean algebra $A$ equipped with:
> $$
> \textbf{quantifiers}\quad \exists(J):A\to A\ \ (J\subseteq I),\qquad \textbf{substitutions}\quad \mathsf S(\sigma):A\to A\ \ (\sigma:I\to I),
> $$

### 11.2. Comparison and Upshot

> [!theorem] Theorem 11.2.1: Equivalence of the formalisms
> For infinite degree, polyadic equality algebras and cylindric algebras are intertranslatable: cylindrifications are recovered as $\exists(\{i\})$, diagonals from the equality elements, and substs. $\mathsf S(\sigma)$ are definable in cylindric algebras for finitely-supported $\sigma$ via compositions of cylindrifications and diagonals. The representable subclasses correspond, so both formalisms algebraize first-order logic with equality, differing in primitive choice (per-axis vs transformation-indexed).

---

# Part IV — Effective Equational Reasoning: Unification and Rewriting

## 12. Unification

### 12.1. The Unification Problem

> [!definition] Definition 12.1.1: Unification problem and unifier
> Fix $\Omega$ and a variable set $X$. A **unification problem** is a finite set of **equations** $\{s_1\stackrel{?}{=}t_1,\dots,s_k\stackrel{?}{=}t_k\}$ with $s_i,t_i\in T_\Omega(X)$.

> [!definition] Definition 12.1.2: Subsumption preorder on substitutions
> For substs. $\sigma,\tau$, $\sigma$ is **more general than** $\tau$ (on a variable set $W$), written $\sigma\lesssim_W\tau$, iff there is $\rho$ with $\tau=_W(\sigma;\rho)$ (i.e. $x\tau=(x\sigma)\rho$ for $x\in W$). This is a **preorder**; its symmetric part is **equiv. up to renaming**: $\sigma\equiv\tau$ iff each is more general than the other, which holds iff they differ by a bijective variable renaming.

> [!definition] Definition 12.1.3: Idempotent substitution
> $\sigma$ is **idempotent** if $\sigma;\sigma=\sigma$, equivalently if $\operatorname{dom}(\sigma)$ is disjoint from the range variables of $\sigma$ (no introduced variable is itself replaced). Idempotent unifiers are the canonical representatives: every unifiable problem has an idempotent most general unifier.

### 12.2. Most General Unifiers

> [!definition] Definition 12.2.1: Most general unifier
> A unifier $\sigma$ of a problem $\mathcal P$ is a **most general unifier (mgu)** if $\sigma\lesssim\tau$ ∀ unifier $\tau$ of $\mathcal P$. By Definition 12.1.2 an mgu is unique up to renaming.

> [!theorem] Theorem 12.2.2: Unification theorem (Robinson)
> In the free term algebra $\mathbf T_\Omega(X)$ over a finitary sig.:
> and in the latter case an **idempotent** mgu exists and is computable.
> $$
> \text{every unification problem is either non-unifiable or has a most general unifier,}
> $$

> [!definition] Definition 12.2.3: The occurs check
> The **occurs check** is the side condition, when solving $x\stackrel{?}{=}t$ with $x\ne t$, that **$x$ does not occur in $t$**. If $x\in\operatorname{var}(t)$ and $t\ne x$, the equation $x\stackrel{?}{=}t$ has **no** unifier in the finite term algebra (any $\sigma$ would need $x\sigma=t\sigma$ with $t\sigma$ strictly larger than $x\sigma$).

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

### 12.4. Matching, and the Categorical View

> [!definition] Definition 12.4.1: Matching
> A **matching problem** $s\stackrel{?}{\le}t$ asks for a subst. $\sigma$ with $s\sigma=t$ where $\sigma$ may instantiate only the variables of $s$ (the **pattern**) and $t$ (the **subject**) is treated as fixed/ground for the unknowns. Matching is one-sided unification; it is decidable in linear time and has a **unique** matcher when one exists (no most-general issue), and is the op. used to fire a rewrite rule (§13).

> [!theorem] Theorem 12.4.2: Unifiers as equalizers; mgu as most general equalizer
> In the Kleisli cat. of the term monad (objects sets, morphisms substs. $X\to T_\Omega(Y)$), a unifier of $s,t:1\to T_\Omega(X)$ is a subst. $\sigma$ coequalizing them, and an **mgu is the coequalizer** of the pair $(s,t)$ in this cat. when it exists. Thus "most general unifier" is "the universal solution" — the same universal-property pattern as free algebras and quotients in the base treatise, here instantiated in the cat. of substs..

### 12.5. Unification Modulo Equations

> [!definition] Definition 12.5.1: $E$-unification
> For an equational theory $E$, an **$E$-unifier** of $s\stackrel{?}{=}_E t$ is a subst. $\sigma$ with $s\sigma\,=_E\,t\sigma$ (equal modulo $\theta_E^{\mathrm{fi}}$). A set $U$ of $E$-unifiers is **complete** if every $E$-unifier is an $E$-instance of some member of $U$; a **minimal complete set** $\mu U$ removes redundancies.
> $$
> \textbf{unitary}\ (\le 1),\quad \textbf{finitary}\ (\text{finite}),\quad \textbf{infinitary}\ (\text{infinite, minimal exists}),\quad \textbf{nullary}\ (\text{no minimal complete set}).
> $$

> [!theorem] Theorem 12.5.2: Landscape of $E$-unification
> (i) **Syntactic** ($E=\varnothing$) unification is unitary (Theorem 12.2.2). (ii) **Commutativity** is finitary.

---

## 13. Term Rewriting Systems in Depth

### 13.1. Abstract Reduction Systems

> [!definition] Definition 13.1.1: Abstract reduction system
> An **abstract reduction system (ARS)** is a pair $(\mathcal S,\to)$ with $\to\subseteq\mathcal S\times\mathcal S$. Write $\to^{*}$ for reflexive–transitive closure, $\to^{=}$ for reflexive closure, $\leftrightarrow$ for $\to\cup\to^{-1}$, $\leftrightarrow^{*}$ for the generated equiv..

> [!definition] Definition 13.1.2: Termination, confluence, convergence
> $(\mathcal S,\to)$ is **terminating (strongly normalizing, $\mathsf{SN}$)** if there is no infinite chain $a_0\to a_1\to\cdots$; **normalizing (weakly, $\mathsf{WN}$)** if every element has a normal form; **confluent (Church–Rosser, $\mathsf{CR}$)** if $a\,{}^{*}{\leftarrow}\,\cdot\to^{*}b\Rightarrow a\downarrow b$; **locally confluent (weakly Church–Rosser, $\mathsf{WCR}$)** if $a\leftarrow\cdot\to b\Rightarrow a\downarrow b$; **convergent** if $\mathsf{SN}\wedge\mathsf{CR}$.

> [!theorem] Theorem 13.1.3: Church–Rosser, Newman, and unique normal forms
> (i) Confluence is equivalent to the **Church–Rosser property** $a\leftrightarrow^{*}b\Rightarrow a\downarrow b$. (ii) **Newman's Lemma**: a terminating ARS is confluent iff locally confluent.

> [!definition] Definition 13.1.4: Term rewrite system
> A **term rewrite system (TRS)** over $(\Omega,X)$ is a set $R$ of **rules** $\ell\to r$ with $\ell\notin X$ and $\operatorname{var}(r)\subseteq\operatorname{var}(\ell)$ (the two standard rule conditions). The induced rewrite relation is the closure of $R$ under subst. instances inside contexts:
> $$
> C[\ell\sigma]\ \to_R\ C[r\sigma]\qquad(\ell\to r\in R,\ \sigma\text{ a substitution},\ C[\,]\text{ a context}).
> $$

### 13.2. Termination by Reduction Orderings

> [!definition] Definition 13.2.1: Reduction ordering
> A **reduction ordering** is a strict partial order $>$ on $T_\Omega(X)$ that is (i) **well-founded** (no infinite descending chain), (ii) **monotone (closed under contexts)**: $s>t\Rightarrow C[s]>C[t]$, and (iii) **stable (closed under subst.)**: $s>t\Rightarrow s\sigma>t\sigma$. A TRS $R$ **terminates** iff there is a reduction ordering $>$ with $\ell>r$ ∀ rule $\ell\to r\in R$ — checking finitely many rule inequalities suffices.

> [!definition] Definition 13.2.2: Simplification orderings and the subterm property
> A **simplification ordering** is a reduction ordering with the **subterm property** $C[t]>t$ for nonempty contexts (a term dominates its proper subterms). By **Kruskal's Tree Theorem** (the finite trees over a finite sig. are **well-quasi-ordered** by homeomorphic embedding), every simplification ordering is well-founded automatically — well-foundedness need not be checked separately.

> [!definition] Definition 13.2.3: Recursive/lexicographic path orderings
> Fix a **precedence** $>_{\mathcal F}$ (a strict order on $\Omega$). The **recursive path ordering (RPO)** and its lexicographic variant **LPO** are defined by mutual recursion: $s=f(s_1,\dots,s_m)>_{\mathrm{lpo}}t$ iff one of
> $$
> \textbf{(1)}\ \exists i,\ s_i\ge_{\mathrm{lpo}}t;\qquad \textbf{(2)}\ t=g(t_1,\dots,t_n),\ f>_{\mathcal F}g,\ \text{and}\ s>_{\mathrm{lpo}}t_j\ \forall j;
> $$
> $$
> \textbf{(3)}\ t=f(t_1,\dots,t_m),\ (s_1,\dots,s_m)>^{\mathrm{lex}}_{\mathrm{lpo}}(t_1,\dots,t_m),\ \text{and}\ s>_{\mathrm{lpo}}t_j\ \forall j.
> $$

> [!definition] Definition 13.2.4: Knuth–Bendix ordering and polynomial interpretations
> The **Knuth–Bendix ordering (KBO)** fixes a weight function $w$ on symbols and compares terms first by total weight, breaking ties by precedence and recursively — a simplification ordering well-suited to systems where size dominates. A **polynomial interpretation** assigns to each $f\in\Omega_n$ a monotone polynomial $[f]:\mathbb N^n\to\mathbb N$ (with values $\ge$ a positive bound), extends to terms, and yields termination if $[\ell]>[r]$ as polynomials ∀ rule; well-foundedness is inherited from $(\mathbb N,>)$.

> [!theorem] Theorem 13.2.5: Dependency pairs (statement)
> The **dependency pair** method reduces termination of $R$ to the absence of infinite **chains** of dependency pairs (pairs derived from the recursive calls in right-hand sides). Termination of $R$ holds iff there is no infinite minimal chain, and this is established by exhibiting a **reduction pair** (a weakly monotone, stable order plus a compatible well-founded order) orienting the dependency pairs.

### 13.3. Critical Pairs and Local Confluence

> [!definition] Definition 13.3.1: Overlap and critical pair
> Let $\ell_1\to r_1$ and $\ell_2\to r_2$ be rules of $R$ (renamed to share no variables). Suppose a **non-variable** subterm $\ell_1|_p$ (at a non-variable position $p$ of $\ell_1$) unifies with $\ell_2$ via mgu $\sigma=\mathrm{mgu}(\ell_1|_p,\ell_2)$.
> $$
> \big\langle\, (\ell_1\sigma)[\,r_2\sigma\,]_p,\ \ r_1\sigma\,\big\rangle,
> $$

> [!theorem] Theorem 13.3.2: Critical Pair Lemma
> A TRS $R$ is **locally confluent** iff **all** its critical pairs are joinable:
> Since a finitary $R$ has only finitely many critical pairs (finitely many rule pairs and non-variable positions), local confluence is **decidable** by computing and joining critical pairs.
> $$
> \mathsf{WCR}(R)\quad\Longleftrightarrow\quad \forall\ \langle u,v\rangle\in\mathrm{CP}(R):\ u\downarrow_R v.
> $$

> [!corollary] Corollary 13.3.3: Decidable confluence for terminating systems
> If $R$ is terminating, then by Newman's Lemma (Theorem 13.1.3) and the Critical Pair Lemma, $R$ is **confluent iff all critical pairs are joinable**, and this is **decidable**: normalize each critical pair's two components and compare. Hence convergence of a terminating finite TRS is a decidable property — the practical test underlying completion.

> [!definition] Definition 13.3.5: Orthogonal systems
> A TRS is **left-linear** if no rule's left side repeats a variable, and **non-overlapping** if it has no (non-trivial) critical pairs. **Orthogonal** = left-linear + non-overlapping.

### 13.4. Knuth–Bendix Completion

> [!construction] Construction 13.4.1: Knuth–Bendix completion procedure
> **Input:** a finite equation set $E$ and a reduction ordering $>$. **State:** a pair $(E_i,R_i)$ of pending equations and oriented rules, initially $(E,\varnothing)$.
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
> On **success**, the word problem for $E$ is decided by $R$-normalization (Theorem 13.1.3).
> $$
> \textbf{success:}\ \text{halts with a finite convergent } R\ \text{such that } {\leftrightarrow^{*}_R}={=_E};
> $$
> $$
> \textbf{failure:}\ \text{produces an equation } s\approx t\ \text{with } s\not> t\ \text{and } t\not> s\ (\text{unorientable});
> $$
> $$
> \textbf{divergence:}\ \text{runs forever, generating infinitely many rules.}
> $$

---

## 14. Narrowing

> [!definition] Definition 14.1.1: Narrowing relation
> Let $R$ be a TRS. A term $s$ **narrows** to $t$ with subst. $\sigma$, written $s\rightsquigarrow_{\sigma}t$, if there is a non-variable position $p$ in $s$, a rule $\ell\to r\in R$ (renamed apart), and $\sigma=\mathrm{mgu}(s|_p,\ell)$ s.t.
> $$
> t=(s[\,r\,]_p)\sigma=(s\sigma)[\,r\sigma\,]_p.
> $$

> [!definition] Definition 14.1.2: Narrowing derivation and computed substitution
> A **narrowing derivation** $s_0\rightsquigarrow_{\sigma_1}s_1\rightsquigarrow_{\sigma_2}\cdots\rightsquigarrow_{\sigma_n}s_n$ has **computed subst.** $\sigma=\sigma_1;\cdots;\sigma_n$ restricted to $\operatorname{var}(s_0)$. To solve $s\stackrel{?}{=}_E t$ one narrows the term $\mathrm{eq}(s,t)$ (or $s$ and $t$ jointly) toward a term recognizably true (e.g. reducible to a common normal form), collecting $\sigma$ as the solution.

> [!theorem] Theorem 14.1.3: Completeness of narrowing for convergent systems
> If $R$ is a **convergent** TRS presenting $E$, then narrowing is **sound and complete for $E$-unification**: ∀ $E$-unifier $\tau$ of $s\stackrel{?}{=}_E t$ there is a narrowing derivation from $s\stackrel{?}{=}t$ to a syntactically unifiable pair whose computed subst. $\sigma$ is more general than $\tau$ (modulo $E$). Thus the set of computed substs. of all narrowing derivations is a **complete set of $E$-unifiers**.

> [!definition] Definition 14.1.4: Refinements
> Unrestricted narrowing has a vast search space; standard refinements preserve completeness while pruning: **basic narrowing** (never narrow within subterms introduced by previous substs.), **innermost/needed narrowing** (narrow at strategically chosen positions, optimal for left-linear constructor systems), and **narrowing modulo** an underlying $AC$ theory. Needed narrowing is the operational semantics of modern functional-logic languages.

---

# Part V — Recognizability: Tree Automata

## 15. Finite Tree Automata

### 15.1. Bottom-Up Tree Automata

> [!definition] Definition 15.1.1: Finite bottom-up tree automaton
> Fix a finite ranked sig. $\Omega$. A **(nondeterministic) finite bottom-up tree automaton (NFTA)** is $\mathcal A=(Q,\Omega,Q_f,\Delta)$ with $Q$ a finite set of **states**, $Q_f\subseteq Q$ the **accepting (final) states**, and $\Delta$ a set of **transition rules**
> $$
> f(q_1,\dots,q_n)\to q\qquad(f\in\Omega_n,\ q_1,\dots,q_n,q\in Q),
> $$

> [!definition] Definition 15.1.2: Recognized language; determinism
> The **language recognized** by $\mathcal A$ is $L(\mathcal A)=\{t\in T_\Omega(\varnothing):\mathcal A\text{ has an accepting run on }t\}$. $\mathcal A$ is **deterministic (DFTA)** if for each $f$ and state tuple $(q_1,\dots,q_n)$ there is **at most one** rule $f(q_1,\dots,q_n)\to q$; then each $t$ has at most one run.

### 15.2. Top-Down Automata and the Determinism Asymmetry

> [!definition] Definition 15.2.1: Top-down tree automaton
> A **top-down** tree automaton has initial states and rules $q\to f(q_1,\dots,q_n)$ read root-to-frontier: a run assigns the root an initial state and propagates state tuples down to the leaves. Nondeterministic top-down automata recognize exactly the recognizable languages (same class as NFTA).

### 15.3. Closure Properties and Determinization

> [!theorem] Theorem 15.3.1: Boolean and projection closure
> The recognizable tree languages over $\Omega$ are an effective **Boolean algebra**: closed under union, intersection, and complement, with automata constructible from the inputs (product automaton for $\cap$, $\cup$; complementation via a complete DFTA by complementing $Q_f$). They are also closed under **tree homs.** and inverse homs., under **projection** (relabeling), and under intersection with the set of terms of a given shape.

> [!theorem] Theorem 15.3.2: Determinization
> Every NFTA is equivalent to a complete DFTA obtained by the **subset constr.**: states are subsets of $Q$, with $f(\mathbf{S}_1,\dots,\mathbf{S}_n)\to\{q:\exists q_i\in \mathbf S_i,\ f(q_1,\dots,q_n)\to q\in\Delta\}$ and accepting subsets those meeting $Q_f$. The blow-up is at most exponential ($2^{|Q|}$).

> [!theorem] Theorem 15.3.3: Minimal automaton
> Every recognizable tree language $L$ has a **unique minimal complete DFTA** (up to isomorphism), the quotient of any complete DFTA for $L$ by the **state-equiv.** relation (states indistinguishable by all accepting contexts). Minimization is effective and the minimal automaton is canonical, exactly as in the string case.

### 15.4. Myhill–Nerode for Trees

> [!definition] Definition 15.4.1: Syntactic congruence of a tree language
> For $L\subseteq T_\Omega(\varnothing)$, the **syntactic (Myhill–Nerode) cong.** $\equiv_L$ on $T_\Omega(\varnothing)$ is
> $$
> s\equiv_L t\quad\Longleftrightarrow\quad \forall\ \text{contexts } C[\,]:\ \big(C[s]\in L\Leftrightarrow C[t]\in L\big),
> $$

> [!theorem] Theorem 15.4.2: Myhill–Nerode theorem for trees
> For $L\subseteq T_\Omega(\varnothing)$ the following are equivalent:
> The minimal DFTA (Theorem 15.3.3) is the quotient algebra $\mathbf T_\Omega(\varnothing)/{\equiv_L}$ with accepting set the classes contained in $L$.
> $$
> \textbf{(a)}\ L\ \text{is recognizable};\quad \textbf{(b)}\ \equiv_L\ \text{has finite index};\quad \textbf{(c)}\ L\ \text{is a union of classes of some finite-index congruence on } \mathbf T_\Omega(\varnothing).
> $$

> [!theorem] Theorem 15.4.3: Decidability of basic problems
> For NFTA the following are **decidable**: **membership** ($t\in L(\mathcal A)$, in polynomial time by a bottom-up run), **emptiness** ($L(\mathcal A)=\varnothing$, by reachability of an accepting state, linear time), **finiteness** ($L(\mathcal A)$ finite, by detecting productive loops), **inclusion** and **equiv.** (via complement and intersection, $\mathsf{EXPTIME}$-complete for NFTA, polynomial for DFTA). A **pumping lemma** holds: sufficiently tall accepted trees contain an iterable context $C[\,]$ with $C^k[\,]$ preserving acceptance.

### 15.5. Recognizable versus Equational; Logic on Trees

> [!definition] Definition 15.5.1: Regular tree grammar and equational tree language
> A **regular tree grammar** has nonterminals, a start symbol, and productions $A\to f(B_1,\dots,B_n)$; the generated language is the set of ground terms derivable. **Regular tree languages** (grammar-generated) coincide with the **recognizable** ones.

> [!theorem] Theorem 15.5.2: Recognizable = MSO-definable (Thatcher–Wright, Doner)
> A tree language $L\subseteq T_\Omega(\varnothing)$ is recognizable iff it is definable in **monadic second-order logic (MSO)** over the tree (with the child relations and label predicates):
> This is the tree generalization of the Büchi–Elgot–Trakhtenbrot theorem for strings and links automata, algebra (finite-index congs.), grammars, and logic into a single notion of regularity.
> $$
> L\ \text{recognizable}\quad\Longleftrightarrow\quad L=\{t:t\models\varphi\}\ \text{for some MSO sentence }\varphi.
> $$

---

# Part VI — The Coalgebraic and Infinitary Dual

## 16. Infinitary Terms and Continuous Algebras

### 16.1. Partial Terms and the Tree Order

> [!definition] Definition 16.1.1: Partial terms
> Adjoin to $\Omega$ a fresh nullary symbol $\bot$ ("undefined"). The **partial terms** $T^\bot_\Omega(X)$ are the (finite) terms over $\Omega\cup\{\bot\}$ and $X$.

> [!definition] Definition 16.1.2: Ideal completion and infinite terms
> The **ideal completion** of $(T^\bot_\Omega(X),\sqsubseteq)$ is the set of $\sqsubseteq$-directed downward-closed sets (ideals) of partial terms, ordered by inclusion; it is an **algebraic complete partial order (CPO)** whose **compact** elements are the finite partial terms. Its maximal elements are the **(possibly infinite) total terms**.

> [!definition] Definition 16.1.3: Metric on terms
> Alternatively, define the **distance** $d(s,t)=2^{-k}$ where $k$ is the least depth at which $s$ and $t$ differ ($d(s,t)=0$ if $s=t$). $(T_\Omega(X),d)$ is an **ultrametric** space; its **Cauchy completion** $\widehat T_\Omega(X)$ is the set of all finite and infinite $\Omega$-trees of the given (finite) branching.

### 16.2. Rational and Algebraic Infinite Terms

> [!definition] Definition 16.2.1: Rational terms
> An infinite term is **rational (regular)** if it has only **finitely many distinct subterms**, equivalently if it is the **unfolding** of a finite **cyclic** term graph, equivalently if it is the unique solution of a finite system of **guarded** recursion equations $x_i=f_i(\dots)$. Rational terms are the infinite-term analogue of regular trees and are exactly the terms denotable by finite cyclic data structures.

> [!theorem] Theorem 16.2.2: Solutions of guarded equations
> In $\widehat T_\Omega(X)$, every **guarded** recursive system (each right side has a constructor at the head before any recursive variable) has a **unique** solution. In particular $x=f(x)$ has the unique solution $f(f(f(\cdots)))=f^\omega$, the infinite term that finite unification rejects by the occurs check (Definition 12.2.3).

### 16.3. Continuous Algebras

> [!definition] Definition 16.3.1: Continuous (ordered) $\Omega$-algebra
> A **continuous $\Omega$-algebra** (in the sense of the ADJ group) is an $\Omega$-algebra whose carrier is a CPO with least element $\bot$ and whose ops. $f^A$ are **continuous** (monotone and preserving directed suprema). A **continuous hom.** is a continuous, $\bot$- and op.-preserving map.

> [!theorem] Theorem 16.3.2: Initial continuous algebra
> The completed term algebra $T^\infty_\Omega(X)$ (with $\bot$ and the constructors extended continuously) is the **initial continuous $\Omega$-algebra** on $X$: every map $g:X\to|A|$ into a continuous algebra extends to a **unique continuous hom.** $T^\infty_\Omega(X)\to A$. This is the order-theoretic counterpart of the base treatise's freeness, and it underwrites **recursion with non-termination**: partial and infinite computations receive values as directed suprema of their finite approximations, the basis of denotational semantics of recursive programs.

---

## 17. Coalgebra and the Final Coalgebra

### 17.1. Coalgebras of the Signature Functor

> [!definition] Definition 17.1.1: $H_\Omega$-coalgebra
> Recall the sig. endofunctor $H_\Omega(Y)=\coprod_{f\in\Omega}Y^{\operatorname{ar}(f)}$ (base treatise §13.3; sorted version Definition 2.3.4). An **$H_\Omega$-coalgebra** is a pair $(C,\gamma)$ with $\gamma:C\to H_\Omega C$; the map $\gamma$ assigns to each state $c$ a **single top constructor** together with its **immediate successor states**.

### 17.2. The Final Coalgebra and Corecursion

> [!theorem] Theorem 17.2.1: Existence and form of the final coalgebra
> The polynomial endofunctor $H_\Omega$ has a **final coalgebra** $(\nu H_\Omega,\ \mathrm{out})$. Its carrier is the set of **finite-and-infinite $\Omega$-trees** (the metric completion of ground terms, Definition 16.1.3): $\nu H_\Omega\cong T^\infty_\Omega(\varnothing)$ restricted to **total** trees $\widehat T_\Omega(\varnothing)$.

> [!theorem] Theorem 17.2.2: Corecursion (anamorphism)
> Finality means: for **every** coalgebra $(C,\gamma)$ there is a **unique** coalgebra hom.
> the **anamorphism**, defined by $\mathrm{out}\circ\mathrm{unfold}_\gamma=H_\Omega(\mathrm{unfold}_\gamma)\circ\gamma$.
> $$
> \mathrm{unfold}_\gamma:\ (C,\gamma)\ \longrightarrow\ (\nu H_\Omega,\mathrm{out}),
> $$

> [!definition] Definition 17.2.3: Guardedness and productivity
> A corecursive definition is **guarded (productive)** if every recursive call is **beneath at least one constructor**, so each unfolding step emits genuine output. Guardedness is the corecursive counterpart of well-foundedness for recursion: it guarantees the anamorphism is total and that each finite prefix of the output is computed in finitely many steps.

### 17.3. Bisimulation and the Coinduction Principle

> [!definition] Definition 17.3.1: Bisimulation
> A **bisimulation** between $H_\Omega$-coalgebras $(C,\gamma)$ and $(D,\delta)$ is a relation $R\subseteq C\times D$ that lifts to a coalgebra structure on $R$ making the two projections coalgebra homs.; concretely, $(c,d)\in R$ implies $c$ and $d$ have the **same top constructor** and their corresponding immediate successors are again $R$-related. Two states are **bisimilar**, $c\sim d$, if some bisimulation relates them.

> [!theorem] Theorem 17.3.2: Coinduction proof principle
> On the final coalgebra $\nu H_\Omega$, **bisimilarity coincides with equality**:
> Hence the **coinduction principle**: to prove two infinite trees (or two states' unfoldings) **equal**, exhibit a **bisimulation** relating them.
> $$
> c\sim d\quad\Longleftrightarrow\quad c=d.
> $$

### 17.4. Algebra–Coalgebra Duality and Bialgebras

> [!theorem] Theorem 17.4.1: The duality, summarized
> For the poly. functor $H_\Omega$:
> The canonical comparison $\mu H_\Omega\hookrightarrow\nu H_\Omega$ embeds finite terms as the well-founded elements of the infinite-term coalgebra; it is an isomorphism iff $\Omega$ has no op. of arity $\ge1$ (only then are all trees finite).
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

> [!definition] Definition 17.4.2: Bialgebras and structured operational semantics
> A **bialgebra** for a functor pair combines an $H_\Omega$-algebra (syntax/constructors) and a $B$-coalgebra (behavior/transitions) on a common carrier, related by a **distributive law** $\lambda:H_\Omega B\Rightarrow B H_\Omega$. A distributive law is exactly a **well-behaved structural operational semantics** (the **GSOS** rule format): it guarantees that **bisimilarity is a cong.** for the syntax, so observational equiv. is compositional.

---

# Part VII — Structure Theory of Varieties

## 18. Varieties and the HSP Theorem

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

> [!definition] Definition 18.1.2: Variety
> A class $\mathcal V$ is a **variety** (equational class) if it is closed under $H$, $S$, and $P$: $H\mathcal V\subseteq\mathcal V$, $S\mathcal V\subseteq\mathcal V$, $P\mathcal V\subseteq\mathcal V$. Equivalently $\mathcal V=HSP\,\mathcal V$.

> [!proposition] Proposition 18.1.3: $HSP$ is the variety closure
> For any class $\mathcal K$, the smallest variety containing $\mathcal K$ is
> and the operator composition stabilizes after this single application: $H(SP\mathcal K)\subseteq HSP\mathcal K$, $S(HSP\mathcal K)\subseteq HSP\mathcal K$, $P(HSP\mathcal K)\subseteq HSP\mathcal K$.
> $$
> V(\mathcal K)\ =\ HSP\,\mathcal K,
> $$

### 18.2. Identities and the Galois Connection

> [!definition] Definition 18.2.1: The satisfaction relation and its polars
> Fix a countably infinite variable set $X_\omega$. For a class $\mathcal K$ and a set $\Theta\subseteq T_\Omega(X_\omega)^2$ of identities, define the **Galois polars** of the relation $A\models s\approx t$:
> $$
> \operatorname{Id}(\mathcal K)\ :=\ \{(s,t):\forall A\in\mathcal K,\ A\models s\approx t\};\qquad \operatorname{Mod}(\Theta)\ :=\ \{A:\forall (s,t)\in\Theta,\ A\models s\approx t\}.
> $$

> [!theorem] Theorem 18.2.2: Birkhoff's variety (HSP) theorem
> The Galois-closed classes are exactly the varieties, and the Galois-closed theories are exactly the **fully invariant congs.** on $\mathbf T_\Omega(X_\omega)$:
> Hence a class is definable by a set of equations iff it is closed under homomorphic images, subalgebras, and products.
> $$
> \mathcal V=\operatorname{Mod}(\operatorname{Id}(\mathcal V))\ \Longleftrightarrow\ \mathcal V\ \text{is a variety}\ \Longleftrightarrow\ \mathcal V=HSP\,\mathcal V,
> $$
> $$
> \Theta=\operatorname{Id}(\operatorname{Mod}(\Theta))\ \Longleftrightarrow\ \Theta\ \text{is a fully invariant congruence on }\mathbf T_\Omega(X_\omega).
> $$

> [!corollary] Corollary 18.2.3: Equational theories $\leftrightarrow$ fully invariant congruences
> The lattice of equational theories of sig. $\Omega$ (sets of identities closed under deduction) is **dually isomorphic** to the lattice of subvarieties of $\mathbf{Alg}(\Omega)$, and **isomorphic** to the lattice of fully invariant congs. on the countably generated free algebra $\mathbf T_\Omega(X_\omega)$. Bigger theories cut out smaller varieties; the trivial variety corresponds to the all-relation, the whole class to the diagonal.

### 18.3. Free Algebras in a Variety

> [!construction] Construction 18.3.1: Relatively free algebra
> Let $\mathcal V=\operatorname{Mod}(E)$ be a variety with fully invariant cong. $\theta^{\mathrm{fi}}_E=\operatorname{Id}(\mathcal V)$. The **$\mathcal V$-free algebra on $X$** is
> $$
> \mathbf F_{\mathcal V}(X)\ :=\ \mathbf T_\Omega(X)\big/\theta^{\mathrm{fi}}_E\restriction_X,
> $$

> [!theorem] Theorem 18.3.2: Free algebras generate the variety
> For any variety $\mathcal V$ and infinite $X$:
> i.e. every member of $\mathcal V$ is a homomorphic image of a relatively free algebra, and $\mathbf F_{\mathcal V}(X_\omega)$ alone generates $\mathcal V$ as a variety.
> $$
> \mathcal V\ =\ HSP(\{\mathbf F_{\mathcal V}(X)\})\ =\ H(\{\mathbf F_{\mathcal V}(Y):Y\ \text{a set}\}),
> $$

### 18.4. Subvarieties and the Lattice of Varieties

> [!definition] Definition 18.4.1: Lattice of subvarieties
> The subvarieties of a variety $\mathcal V$, ordered by inclusion, form a complete lattice $L(\mathcal V)$: meets are intersections, joins are $V(\cdot)$ of unions. By Corollary 18.2.3 this is dually isomorphic to the lattice of equational theories extending $\operatorname{Id}(\mathcal V)$.

---

## 19. Subdirect Representation, Quasivarieties, and Ultraproducts

### 19.1. Subdirectly Irreducible Algebras

> [!definition] Definition 19.1.1: Subdirect product and subdirect embedding
> $A$ is a **subdirect product** of $(A_i)_{i\in I}$ if $A\le\prod_i A_i$ and every projection $\pi_i\restriction_A:A\to A_i$ is **surjective**. A **subdirect embedding** is an embedding $A\hookrightarrow\prod_i A_i$ with all projections surjective; equivalently a family of surjections $(\,A\twoheadrightarrow A_i\,)$ whose kernels intersect to the diagonal: $\bigcap_i\ker(\pi_i\restriction_A)=\Delta_A$.

> [!definition] Definition 19.1.2: Subdirectly irreducible algebra
> $A$ (nontrivial) is **subdirectly irreducible (SI)** if in every subdirect embedding $A\hookrightarrow\prod_i A_i$ some projection $\pi_i\restriction_A$ is an isomorphism; equivalently, the cong. lattice $\operatorname{Con}(A)$ has a **least nonzero element** (a **monolith** $\mu_A$), i.e. the intersection of all nondiagonal congs. is itself nondiagonal. **Simple** algebras (only $\Delta_A,\nabla_A$ as congs.) are SI.

> [!theorem] Theorem 19.1.3: Birkhoff's subdirect representation theorem
> Every algebra $A$ is (isomorphic to) a **subdirect product of subdirectly irreducible algebras**, each a quotient of $A$:
> Consequently every variety $\mathcal V$ is determined by its subdirectly irreducible members: $\mathcal V=SP(\,\mathcal V_{\mathrm{SI}}\,)$, and to verify an identity in $\mathcal V$ it suffices to verify it in all SI members.
> $$
> A\ \hookrightarrow\ \prod_{i}\ A/\theta_i\qquad(\text{each }A/\theta_i\ \text{SI},\ \textstyle\bigcap_i\theta_i=\Delta_A).
> $$

### 19.2. Ultraproducts and Łoś's Theorem

> [!definition] Definition 19.2.1: Filter, ultrafilter, ultraproduct
> A **filter** on a set $I$ is a nonempty $\mathcal F\subseteq\mathcal P(I)$ closed under supersets and finite intersections with $\varnothing\notin\mathcal F$; an **ultrafilter** is a maximal filter (∀ $J\subseteq I$, exactly one of $J,I\setminus J$ is in $\mathcal F$). For algebras $(A_i)_{i\in I}$ and an ultrafilter $\mathcal U$, the **ultraproduct** $\prod_{\mathcal U}A_i$ is the quotient $\big(\prod_i A_i\big)/{\sim_{\mathcal U}}$ where $a\sim_{\mathcal U}b\iff\{i:a_i=b_i\}\in\mathcal U$ ("equal on a $\mathcal U$-large set").

> [!theorem] Theorem 19.2.2: Łoś's theorem
> For any first-order formula $\varphi(x_1,\dots,x_n)$ and elements $[a^1],\dots,[a^n]$ of $\prod_{\mathcal U}A_i$,
> "A first-order property holds in the ultraproduct iff it holds on a $\mathcal U$-large set of factors." In particular ultraproducts preserve **all** first-order sentences true in $\mathcal U$-almost-all factors, hence preserve every identity and every quasi-identity.
> $$
> \prod_{\mathcal U}A_i\ \models\ \varphi\big([a^1],\dots,[a^n]\big)\quad\Longleftrightarrow\quad \{\,i\in I:\ A_i\models\varphi(a^1_i,\dots,a^n_i)\,\}\in\mathcal U.
> $$

> [!corollary] Corollary 19.2.3: Compactness via ultraproducts
> The **compactness theorem** of first-order logic follows: a set of sentences with every finite subset satisfiable has a model (an ultraproduct of the finite-subset models over a suitable ultrafilter). For universal algebra, the relevant consequence is that classes axiomatized by first-order sentences are closed under $P_{\!U}$, and the operator $P_{\!U}$ measures the gap between syntactic and "limit" behavior of an algebra class.

### 19.3. Quasivarieties

> [!definition] Definition 19.3.1: Quasi-identity and quasivariety
> A **quasi-identity** (strict universal Horn sentence) over $X$ has the form
> $$
> \Big(\bigwedge_{j=1}^{k} s_j\approx t_j\Big)\ \Rightarrow\ s\approx t,
> $$

> [!theorem] Theorem 19.3.2: Mal'cev's quasivariety theorem
> A class $\mathcal K$ closed under isomorphism is a **quasivariety** iff it is closed under $S$, $P$, $P_{\!U}$, and contains the trivial algebra:
> Equivalently $\mathcal K=ISP_{\!R}\mathcal K$ using reduced products.
> $$
> \mathcal K\ \text{is a quasivariety}\quad\Longleftrightarrow\quad \mathcal K=SPP_{\!U}\,\mathcal K\ \text{(and }\mathcal K\ni\text{trivial)}.
> $$

> [!definition] Definition 19.3.3: Relatively free algebras and the lattice of quasivarieties
> Each quasivariety $\mathcal Q$ has **relatively free** algebras $\mathbf F_{\mathcal Q}(X)$, defined by the universal property relative to $\mathcal Q$ as in Construction 18.3.1 but using the least **relative cong.** ($\mathcal Q$-cong.) rather than the fully invariant one. The subquasivarieties of $\mathcal Q$ form a complete (algebraic) lattice $L_q(\mathcal Q)$, generally **larger and more complex** than the subvariety lattice, and dually isomorphic to the lattice of **relative congs.** on $\mathbf F_{\mathcal Q}(X_\omega)$.

---

## 20. Clones, Lawvere Theories, and Finitary Monads

### 20.1. Term and Polynomial Operations; Clones

> [!definition] Definition 20.1.1: Term operation
> For an $\Omega$-algebra $A$ and a term $t\in T_\Omega(X_n)$ in variables $x_1,\dots,x_n$, the **term op.** $t^A:|A|^n\to|A|$ is $\bar a\mapsto\operatorname{ev}_{\bar a}(t)$ (evaluate $t$ with $x_i:=a_i$). The term ops. of all arities form a set of finitary ops. on $|A|$ closed under projections and composition.

> [!definition] Definition 20.1.2: Clone
> A **clone** on a set $S$ is a family $\mathcal C=(\mathcal C_n)_{n\in\mathbb N}$ with $\mathcal C_n\subseteq S^{(S^n)}$ (n-ary ops.) s.t.: $\mathcal C$ contains all **projections** $\pi^n_i(\bar a)=a_i$; and $\mathcal C$ is closed under **superposition** (generalized composition) $ (g;h_1,\dots,h_m)(\bar a)=g(h_1(\bar a),\dots,h_m(\bar a))$. The **clone of $A$**, $\mathrm{Clo}(A)$, is the clone of term ops. of $A$; it is the closure of the basic ops. $\{f^A\}$ under projections and superposition.

> [!definition] Definition 20.1.3: Polynomial operations
> The **polynomial ops.** of $A$ are the term ops. of the algebra $A_{|A|}$ obtained by adjoining a constant for each element of $|A|$; equivalently term ops. allowing parameters from $|A|$. $\mathrm{Pol}(A)\supseteq\mathrm{Clo}(A)$, and the polynomial clone governs the **cong.** structure (a relation is a cong. iff it is compatible with all polynomial ops., equivalently with all basic ops. — base treatise Definition 1.4.1).

> [!definition] Definition 20.1.4: Abstract clone and the clone of a variety
> An **abstract clone** is a clone presented without reference to an underlying set: a family of "op. symbols of each arity" with formal projections and a formal superposition satisfying the clone identities (a cartesian operad / a single-sorted algebraic theory). The **clone of a variety $\mathcal V$** is $\mathrm{Clo}(\mathcal V):=\mathrm{Clo}(\mathbf F_{\mathcal V}(X_\omega))$, equivalently $\mathcal C_n=\mathbf F_{\mathcal V}(X_n)$ with superposition given by subst.: the $n$-ary clone elements are exactly the **$\mathcal V$-equiv. classes of $n$-variable terms**.

### 20.2. Lawvere Theories

> [!definition] Definition 20.2.1: Lawvere theory
> A **(single-sorted) Lawvere theory** is a small cat. $\mathcal T$ with objects the natural numbers $0,1,2,\dots$ s.t. each $n$ is the **$n$-fold categorical product** of $1$: $n\cong 1\times\cdots\times 1$, with chosen product projections. Morphisms $n\to 1$ are the **$n$-ary ops.** of the theory; morphisms $n\to m$ are $m$-tuples of $n$-ary ops..

> [!definition] Definition 20.2.2: Models of a Lawvere theory
> A **model** (algebra) of a Lawvere theory $\mathcal T$ in $\mathbf{Set}$ is a **finite-product-preserving functor** $M:\mathcal T\to\mathbf{Set}$. Then $M(1)$ is the carrier, $M(n)\cong M(1)^n$, and each op. $\omega:n\to1$ is interpreted as $M(\omega):M(1)^n\to M(1)$; functoriality and product-preservation force exactly the equational laws of $\mathcal T$.

> [!theorem] Theorem 20.2.3: Varieties are categories of theory-models
> ∀ variety $\mathcal V$ there is an equiv. of cats.
> between $\mathcal V$ and the cat. of finite-product-preserving functors $\mathcal T_{\mathcal V}\to\mathbf{Set}$.
> $$
> \mathcal V\ \simeq\ \mathbf{Mod}(\mathcal T_{\mathcal V},\mathbf{Set})\ =\ \mathbf{Prod}(\mathcal T_{\mathcal V},\mathbf{Set}),
> $$

### 20.3. Finitary Monads and the Triangle of Equivalences

> [!definition] Definition 20.3.1: Finitary monad
> A monad $(T,\eta,\mu)$ on $\mathbf{Set}$ is **finitary** if $T$ preserves **filtered colimits**, equivalently if $T(X)=\bigcup\{T(X_0):X_0\subseteq X\ \text{finite}\}$ — every element of $T(X)$ uses only finitely many elements of $X$. The term monad $T_\Omega$ of a finitary sig., and its quotients by equational theories, are finitary; conversely finitary monads are exactly the "subst. structures" of finitary algebraic theories.

> [!theorem] Theorem 20.3.2: The triangle: varieties $\simeq$ Lawvere theories $\simeq$ finitary monads
> There are equivalences, all natural and mutually compatible,
> under which a variety $\mathcal V$ corresponds to its theory $\mathcal T_{\mathcal V}$ and to the monad $T_{\mathcal V}$ with $T_{\mathcal V}(X)=|\mathbf F_{\mathcal V}(X)|$; the cat. $\mathcal V$ is recovered as $\mathbf{Mod}(\mathcal T_{\mathcal V})$ and as the Eilenberg–Moore cat. $\mathbf{Set}^{T_{\mathcal V}}$.
> $$
> \{\text{varieties}\}\ \simeq\ \{\text{Lawvere theories}\}\ \simeq\ \{\text{finitary monads on }\mathbf{Set}\},
> $$

---

## 21. Congruence Conditions and the Finite Basis Problem

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

> [!theorem] Theorem 21.1.2: Mal'cev's permutability theorem
> $\mathcal V$ is cong.-permutable iff there is a ternary term $m(x,y,z)$ (a **Mal'cev term**) with
> Groups have $m(x,y,z)=x\cdot y^{-1}\cdot z$; rings, modules, quasigroups, and Heyting/Boolean algebras (via $x-y+z$ analogues) are cong.-permutable.
> $$
> \mathcal V\ \models\ m(x,x,y)\approx y\quad\text{and}\quad m(x,y,y)\approx x.
> $$

> [!theorem] Theorem 21.1.3: Jónsson and Pixley terms
> (i) **Jónsson (cong.-distributivity):** $\mathcal V$ is cong.-distributive iff there are ternary terms $d_0,\dots,d_n$ (**Jónsson terms**) with $d_0(x,y,z)\approx x$, $d_n(x,y,z)\approx z$, $d_i(x,y,x)\approx x$, and the linking identities $d_i(x,x,z)\approx d_{i+1}(x,x,z)$ ($i$ even), $d_i(x,z,z)\approx d_{i+1}(x,z,z)$ ($i$ odd). (ii) **Pixley (arithmeticity = permutable + distributive):** $\mathcal V$ is **arithmetical** iff there is a single term $p(x,y,z)$ with $p(x,y,x)\approx x$, $p(x,y,y)\approx x$, $p(x,x,y)\approx y$.

### 21.2. Jónsson's Lemma and Subdirectly Irreducibles

> [!theorem] Theorem 21.2.1: Jónsson's Lemma
> If $\mathcal V=V(\mathcal K)$ is **cong.-distributive**, then every subdirectly irreducible algebra in $\mathcal V$ lies in $HSP_{\!U}(\mathcal K)$:
> In particular, if $\mathcal K$ is a finite set of finite algebras, the subdirectly irreducibles of $V(\mathcal K)$ are (up to isomorphism) among the homomorphic images of subalgebras of members of $\mathcal K$ (ultrapowers being harmless for finite $\mathcal K$), hence **finite and finitely many**.
> $$
> \mathcal V_{\mathrm{SI}}\ \subseteq\ HSP_{\!U}(\mathcal K).
> $$

> [!corollary] Corollary 21.2.2: Finite lattices of subvarieties
> If a cong.-distributive variety is generated by a finite algebra, it has only finitely many subdirectly irreducibles and a well-understood (often finite) lattice of subvarieties. This is why varieties of lattices and of many lattice-based structures (Heyting, Boolean, Kleene algebras) are far more tractable than the wild varieties of semigroups or groups, which are not cong.-distributive.

### 21.3. The Finite Basis Problem

> [!definition] Definition 21.3.1: Finitely based algebra/variety
> A variety $\mathcal V$ is **finitely based** if $\operatorname{Id}(\mathcal V)$ is generated, as a fully invariant cong., by a **finite** set of identities. A finite algebra $A$ is **finitely based** if $V(A)$ is.

> [!theorem] Theorem 21.3.2: Positive finite-basis results
> (i) **Birkhoff:** every variety of **finite type** that is generated by a finite algebra and is **cong.-distributive** is finitely based when... — more precisely, **Baker's Finite Basis Theorem:** every finite algebra of finite type generating a **cong.-distributive** variety is finitely based. (ii) **Oates–Powell:** every finite **group** is finitely based.

> [!theorem] Theorem 21.3.3: Negative results — Lyndon, Murskiı̆, McKenzie
> (i) **Lyndon:** there is a **seven-element** algebra that is **not** finitely based; **Murskiı̆** reduced this to a **three-element** algebra. (ii) **Tarski's finite basis problem** asked whether finite basedness of a finite algebra is **decidable**; **McKenzie** answered **no**: there is no algorithm deciding, given a finite algebra, whether it is finitely based.

---

## 22. Clones on Finite Sets and Functional Completeness

### 22.1. The Pol–Inv Galois Connection

> [!definition] Definition 22.1.1: Preservation, polymorphisms, invariants
> Fix a finite set $S$. An $n$-ary op. $g:S^n\to S$ **preserves** an $m$-ary relation $R\subseteq S^m$ (is a **polymorphism** of $R$) if applying $g$ coordinatewise to any $n$ tuples in $R$ yields a tuple in $R$.

> [!theorem] Theorem 22.1.2: The Galois connection and its closed objects
> On a finite set $S$, $(\mathrm{Pol},\mathrm{Inv})$ is a Galois connection between ops. and relations whose closed sets are exactly:
> Thus **clones** on a finite set are precisely the sets of ops. of the form $\mathrm{Pol}(\mathcal R)$ — the ops. preserving some set of relations.
> $$
> \mathrm{Pol}(\mathrm{Inv}(F))=\langle F\rangle\ (\text{the clone generated by }F);\qquad \mathrm{Inv}(\mathrm{Pol}(\mathcal R))=[\mathcal R]\ (\text{the relational clone / co-clone generated by }\mathcal R).
> $$

### 22.2. Maximal Clones and Functional Completeness

> [!definition] Definition 22.2.1: Functional completeness
> A set $F$ of ops. on a finite $S$ is **functionally complete (Sheffer)** if $\langle F\rangle$ is the clone of **all** finitary ops. on $S$, i.e. $\mathrm{Clo}=S^{(S^n)}$ ∀ $n$. An algebra $A$ on a finite carrier is **primal** if its basic ops. are functionally complete (every op. on $|A|$ is a term op.).

> [!theorem] Theorem 22.2.2: Rosenberg's classification of maximal clones
> On a finite set $S$ ($|S|\ge2$) there are **finitely many maximal clones**, and Rosenberg's theorem classifies them as the polymorphism clones $\mathrm{Pol}(R)$ of six explicitly described families of relations $R$: (i) **bounded partial orders**; (ii) **prime-affine** (graphs of $p$-ary affine ops. over $\mathbb Z_p$); (iii) **prime-permutation** relations (fixed-point-free permutations of prime order); (iv) **non-trivial equiv. relations**; (v) **central relations**; (vi) **regular $h$-ary relations**. A clone is contained in some maximal clone iff it is not the full clone.

> [!corollary] Corollary 22.2.3: Completeness criterion
> $F$ is functionally complete on $S$ iff $F$ is contained in **none** of the maximal clones of Theorem 22.2.2; equivalently, iff $F$ violates each of the six Rosenberg relation families. On the two-element set this specializes to **Post's criterion**: $F$ is complete iff it is not entirely contained in any of the five "Post classes" (monotone, affine, self-dual, $0$-preserving, $1$-preserving).

> [!theorem] Theorem 22.2.4: Post's lattice
> The clones on the **two-element** set $\{0,1\}$ form a **countably infinite, completely described** lattice (**Post's lattice**), with each clone finitely generated and dual-atom structure given by the five maximal Post classes. In contrast, for $|S|\ge3$ the lattice of clones has the **cardinality of the continuum** and is not fully classifiable, although the maximal (Theorem 22.2.2) and minimal clones are known.

---

# Part VIII — Further Effective Methods

## 23. Congruence Closure and Ground Decision Procedures

### 23.1. The Ground Word Problem

> [!definition] Definition 23.1.1: Ground equational theory and the uniform word problem
> Let $\Sigma$ be a sig. and $C$ a finite set of constants (and other ground subterms). A **ground equation** is a pair $a\approx b$ of ground terms.

> [!theorem] Theorem 23.1.2: Decidability of the ground word problem
> The uniform word problem for ground equations over a finite sig. is **decidable**. Unlike the general word problem (Novikov–Boone, undecidable), the ground case is tractable because no rule may be instantiated: the relevant cong. is generated by finitely many ground pairs closed under reflexivity, symmetry, transitivity, and the **cong. rule restricted to the finitely many subterms that occur**.

### 23.2. The Congruence Closure Algorithm

> [!definition] Definition 23.2.1: Subterm graph and congruence closure
> Let $G$ be the finite set of all subterms occurring in $E\cup\{s,t\}$ (the **term universe**, closed under subterms). The **cong. closure** of $E$ on $G$ is the least equiv. $\sim$ on $G$ containing $E$ and satisfying the **local cong. rule**:
> $$
> f(u_1,\dots,u_n),\ f(v_1,\dots,v_n)\in G\ \wedge\ u_i\sim v_i\ (\forall i)\ \Longrightarrow\ f(u_1,\dots,u_n)\sim f(v_1,\dots,v_n).
> $$

> [!construction] Construction 23.2.2: Union–find with congruence propagation
> Maintain a **union–find** structure over $G$ with classes, plus, for each class, the set of **parent** terms (terms having a member of the class as an immediate argument). Process each input equation $a\approx b$ by $\mathrm{union}(a,b)$; after each merge, **propagate**: ∀ pair of parents that have become congruent (equal head, argument-classes now equal), merge them too, cascading.

> [!theorem] Theorem 23.2.3: Correctness and the e-graph
> The data structure of Construction 23.2.2 computes exactly the cong. closure $\sim$ (Definition 23.2.1), so membership queries $s\sim t$ are answered by comparing class representatives. The maintained structure — a term DAG quotiented by the running cong. — is the **e-graph (equiv. graph)** of modern solvers, supporting incremental assertion of equations, backtracking, and querying, and combining with other decision procedures by **Nelson–Oppen** equality sharing.

### 23.3. Scope, Combination, and Limits

> [!definition] Definition 23.3.1: Theory combination
> The **Nelson–Oppen** method decides the union of two **stably-infinite**, **sig.-disjoint** decidable theories by cong. closure over the shared (equality) sig.: each theory propagates **entailed equalities between shared constants** to the other until closure or contradiction. This lifts ground decidability of the equational fragment to combined theories (uninterpreted functions $+$ linear arithmetic $+$ arrays, etc.), the architecture of $\mathsf{SMT}$.

---

## 24. Anti-Unification

> [!definition] Definition 24.1.1: Generalization and least general generalization
> A term $g$ is a **generalization** of $s$ and $t$ if there are substs. $\sigma,\tau$ with $g\sigma=s$ and $g\tau=t$. A generalization $g$ is a **least general generalization (lgg)** (most specific generalization) if every generalization $g'$ of $s,t$ is more general than $g$ ($g'\lesssim g$): $g$ is $\le$-greatest in the subsumption preorder among common generalizations.

> [!theorem] Theorem 24.1.2: Existence and uniqueness of the lgg
> In the free term algebra over a finitary sig., **every** finite set of terms has a **least general generalization**, **unique up to variable renaming**, and computable in polynomial time. Hence syntactic anti-unification, like syntactic unification, is **unitary** — but with no failure case: the lgg always exists (in the worst case it is a bare variable).

> [!construction] Construction 24.1.3: The anti-unification algorithm
> Compute the lgg of $s,t$ by simultaneous top-down traversal, maintaining a map from already-seen mismatched pairs to variables:
> $$
> \mathrm{lgg}(f(s_1,\dots,s_n),\,f(t_1,\dots,t_n))=f(\mathrm{lgg}(s_1,t_1),\dots,\mathrm{lgg}(s_n,t_n)),
> $$
> $$
> \mathrm{lgg}(s,t)=z_{(s,t)}\ \text{(a fresh variable, reused for repeated pairs)}\quad\text{when heads differ.}
> $$

---

## 25. Higher-Order Unification and Rewriting

### 25.1. The Higher-Order Unification Problem

> [!definition] Definition 25.1.1: Higher-order unification
> Fix a simply-typed $\lambda$-calculus over base types, with terms taken modulo $\alpha\beta\eta$-equiv. (Part II; $\beta\eta$ as the equational theory of §8.3). A **higher-order unification problem** is a finite set of equations $\{s_i\stackrel{?}{=}t_i\}$ between typed $\lambda$-terms; a **solution** is a (capture-avoiding, type-preserving) subst. $\sigma$ of $\lambda$-terms for free variables with $s_i\sigma=_{\beta\eta}t_i\sigma$ for all $i$.

> [!theorem] Theorem 25.1.2: Undecidability and the type hierarchy
> Higher-order unification is **undecidable** (Huet, Goldfarb): already **second-order** unification is undecidable (Goldfarb's reduction from Hilbert's tenth problem), and even with a single second-order variable. The problem is **infinitary** in unification type: solution sets need not have finite complete sets and need not have most general unifiers.

> [!construction] Construction 25.1.3: Huet's preunification procedure
> **Huet's algorithm** searches for unifiers by alternating: **simplification** (decompose **rigid–rigid** equations, whose heads are constants/bound variables, exactly as first-order decomposition) and **projection/imitation** for **flexible–rigid** equations (head a free variable on one side): the flexible variable is guessed to either **imitate** the rigid head or **project** onto one of its arguments. The procedure is **complete** (enumerates a complete set of unifiers in the limit) but may not terminate; it postpones unsolvable **flex–flex** pairs as a **preunifier**, since flex–flex pairs are always solvable.

### 25.2. Patterns: the Decidable Fragment

> [!definition] Definition 25.2.1: Miller patterns
> A **(Miller) pattern** is a $\lambda$-term in which every free (meta)variable is applied only to **distinct bound variables** ($F\,x_1\cdots x_k$ with the $x_i$ distinct and bound). The **higher-order pattern unification** problem restricts all equations to patterns.

> [!theorem] Theorem 25.2.2: Decidability and unitarity of pattern unification
> Higher-order **pattern** unification is **decidable**, and a unifiable pattern problem has a **most general unifier** (it is **unitary**), computable by a Martelli–Montanari-style procedure extended with rules for the flexible cases (where the distinct-bound-variable restriction makes imitation/projection deterministic). Pattern unification recovers, inside the higher-order world, the good first-order behavior of Theorem 12.2.2 and is the fragment used in practice by logical frameworks and dependently-typed languages.

### 25.3. Higher-Order Rewriting

> [!definition] Definition 25.3.1: Higher-order rewrite system
> A **higher-order rewrite system (HRS)** (Nipkow's format / combinatory reduction systems) consists of rules $\ell\to r$ between typed $\lambda$-terms with metavariables, where matching is performed **modulo $\alpha\beta\eta$** (typically restricted so left sides are **patterns**, making matching decidable and unitary by Theorem 25.2.2). Rewriting fires a rule by pattern-matching a subterm and replacing it, with capture handled by the $\lambda$-calculus subst..

> [!theorem] Theorem 25.3.2: Critical pairs and confluence for HRSs
> For pattern HRSs there is a higher-order **Critical Pair Lemma**: critical pairs are computed by higher-order pattern unification of left-hand sides, and a terminating pattern HRS is confluent iff all its critical pairs are joinable (Mayr–Nipkow), generalizing Theorem 13.3.2. Termination is established by higher-order reduction orderings (e.g. the higher-order recursive path ordering, HORPO).

---

# Part IX — Unifying and Advanced Frameworks

## 26. Combinatory Algebra and the Elimination of Binding

### 26.1. Applicative Structures and Combinatory Algebras

> [!definition] Definition 26.1.1: Applicative structure
> An **applicative structure** is a set $A$ with a single binary op. $\cdot:A\times A\to A$ (**application**), written by juxtaposition and associating to the **left**: $xyz:=(xy)z$. It is an $\Omega$-algebra for the sig. with one binary symbol — no binders.

> [!definition] Definition 26.1.2: Combinatory algebra
> A **combinatory algebra** is an applicative structure with two distinguished constants $\mathsf K,\mathsf S$ satisfying the **combinator equations**
> $$
> \mathsf K\,x\,y\approx x,\qquad \mathsf S\,x\,y\,z\approx (x\,z)\,(y\,z).
> $$

> [!theorem] Theorem 26.1.3: Combinatory completeness (bracket abstraction)
> In any combinatory algebra, ∀ term $t$ built from variables and elements there is a term $\lambda^{*}x.\,t$ **not containing $x$** with
> constructed by **bracket abstraction**: $\lambda^{*}x.\,x:=\mathsf I$; $\lambda^{*}x.\,t:=\mathsf K\,t$ if $x\notin\operatorname{var}(t)$; $\lambda^{*}x.\,(t\,u):=\mathsf S\,(\lambda^{*}x.\,t)\,(\lambda^{*}x.\,u)$.
> $$
> (\lambda^{*}x.\,t)\,a\ \approx\ t[x{:=}a]\qquad\text{for all }a,
> $$

### 26.2. The Cost: Weak Equality and Lambda Algebras

> [!definition] Definition 26.2.2: Lambda algebras and lambda models
> A **lambda algebra** is a combinatory algebra additionally satisfying the finitely many **Curry axioms** that force bracket abstraction to model $\lambda\beta$-conversion (the equations making the two translations between combinators and $\lambda$-terms mutually inverse modulo the theory). A **lambda model** further satisfies the **weak extensionality** (Meyer–Scott) axiom internalizing the $\xi$-rule.

> [!theorem] Theorem 26.2.3: Algebraic status of the $\lambda$-calculus
> The $\lambda\beta$-calculus is **algebraizable** as the variety of **lambda algebras** (equivalently, $\lambda\beta$ is the equational theory of lambda algebras), and $\lambda\beta\eta$ as a stronger variety. Hence the untyped $\lambda$-calculus, unlike first-order logic (§10, Part III), **does** admit a binder-free equational presentation — but only via the indirect combinatory encoding, and the naive equational treatment "$\lambda$ as an op. symbol with $\beta$ as an identity" is **unsound** (it lacks the $\xi$/extensionality control).

---

## 27. Rewriting Logic and Membership Equational Logic

### 27.1. Membership Equational Logic

> [!definition] Definition 27.1.1: Membership signature and atomic sentences
> A **membership sig.** has a set $K$ of **kinds**, op. symbols typed by kinds, and a set $S$ of **sorts** each assigned to a kind. The **atomic sentences** are **equations** $t\approx t'$ (between terms of the same kind) and **memberships** $t:s$ ("$t$ has sort $s$").

> [!definition] Definition 27.1.2: Conditional axioms of MEL
> The axioms of MEL are **conditional**:
> $$
> \Big(\bigwedge_i u_i\approx v_i\ \wedge\ \bigwedge_j w_j:s_j\Big)\ \Rightarrow\ t\approx t'\ \ \text{or}\ \ t:s,
> $$

> [!theorem] Theorem 27.1.3: MEL subsumes the Part I frameworks
> Many-sorted, order-sorted, and partial equational specifications all translate **conservatively** into membership equational logic: sorts become membership predicates, subsorts become Horn implications between them, and partial ops. become ops. whose result has a sort only under definedness conditions. MEL has **initial models** (constructed as quotients of a term algebra by the least cong.-plus-membership relation satisfying the axioms) and a **sound and complete** deduction system, so the entire Part I apparatus is a fragment of one logic.

### 27.2. Rewriting Logic

> [!definition] Definition 27.2.1: Rewrite theory
> A **rewrite theory** is $\mathcal R=(\Sigma,E,R)$ where $(\Sigma,E)$ is a (membership) equational theory and $R$ is a set of **rewrite rules** $\ell\to r$ (possibly conditional). Crucially, rules in $R$ are **not** equations: they are read as **one-directional transitions** modulo the equations $E$.

> [!definition] Definition 27.2.2: Deduction and the two layers
> Rewriting-logic deduction derives sequents $t\to t'$ by reflexivity, transitivity, **cong.** (rewrite in context), and **replacement** (apply a rule under a subst.), all **modulo $E$** (rewrite up to equational equality of states). The **equational layer $E$** specifies the **static** data structure (what counts as the same state); the **rule layer $R$** specifies **dynamic** change (which states transition to which).

---

## 28. Coalgebraic Modal Logic and Algebra–Coalgebra Duality

### 28.1. Modal Algebras

> [!definition] Definition 28.1.1: Boolean algebra with operators; modal algebra
> A **modal algebra** is a Boolean algebra $(B,+,\cdot,-,0,1)$ with a unary operator $\Diamond:B\to B$ that is **normal and additive**: $\Diamond 0=0$ and $\Diamond(x+y)=\Diamond x+\Diamond y$ (dually $\Box=-\Diamond-$ preserves $1$ and meets). Modal algebras form a **variety** (equationally axiomatized), and stronger modal logics (T, S4, S5, K4, …) are subvarieties cut out by further equations ($\Diamond$ idempotency, increasingness, etc.).

> [!definition] Definition 28.1.2: Kripke frames as coalgebras
> A **Kripke frame** is a set $W$ of worlds with an accessibility relation $\mathrel{\to}\subseteq W\times W$, i.e. a coalgebra $W\to\mathcal P(W)$ for the **powerset functor** $\mathcal P$. A **model** adds a valuation.

### 28.2. Duality

> [!theorem] Theorem 28.2.1: Jónsson–Tarski duality
> The complex-algebra and ultrafilter-frame constructions form a **duality** between modal algebras and (descriptive general) Kripke frames, extending **Stone duality** between Boolean algebras and Stone spaces:
> with the **algebra** side built from the **coalgebra** (frame) by taking the powerset Boolean algebra with $\Diamond$ the relational image, and the frame recovered from the algebra via its ultrafilters and the canonical relation.
> $$
> \text{modal algebras}\ \xleftrightarrow{\ \text{dual equivalence}\ }\ \text{descriptive general frames},
> $$

> [!theorem] Theorem 28.2.2: Coalgebraic modal logic (general functor)
> For a broad class of $\mathbf{Set}$-endofunctors $H$ (replacing $\mathcal P$), one obtains a **coalgebraic modal logic** whose models are $H$-coalgebras (§17), whose modalities are given by **predicate liftings** for $H$, and which is **sound and complete**, **expressive** (modally distinguishes non-bisimilar states up to behavioral equiv.), and dual to a variety of **$H$-modal algebras**. The base treatise's sig. functor $H_\Omega$, the powerset functor, distribution functors (probabilistic logic), and others all instantiate this scheme.

---

## 29. Institutions and Specification

### 29.1. The Definition of an Institution

> [!definition] Definition 29.1.1: Institution
> An **institution** consists of: a cat. $\mathbf{Sign}$ of **sigs.**; a functor $\mathrm{Sen}:\mathbf{Sign}\to\mathbf{Set}$ giving, for each sig. $\Sigma$, its set of **sentences** and, for each sig. morphism, a **sentence-translation** map; a functor $\mathrm{Mod}:\mathbf{Sign}^{\mathrm{op}}\to\mathbf{Cat}$ giving the **cat. of models** and a **model-reduction** functor for each sig. morphism; and, for each $\Sigma$, a **satisfaction relation** $\models_\Sigma\,\subseteq|\mathrm{Mod}(\Sigma)|\times\mathrm{Sen}(\Sigma)$.

> [!definition] Definition 29.1.2: The satisfaction condition
> The data must obey the **satisfaction condition**: ∀ sig. morphism $\varphi:\Sigma\to\Sigma'$, model $M'$ of $\Sigma'$, and sentence $\psi$ of $\Sigma$,
> $$
> M'\ \models_{\Sigma'}\ \mathrm{Sen}(\varphi)(\psi)\quad\Longleftrightarrow\quad \mathrm{Mod}(\varphi)(M')\ \models_{\Sigma}\ \psi,
> $$

### 29.2. Structured Specification

> [!definition] Definition 29.2.1: Specification-building operations
> Over **any** institution, specifications are built and combined by institution-independent ops.: **union** (combine sentence sets over a pushout of sigs.), **translation/renaming** (along a sig. morphism), **hiding** (reduct along a morphism, exporting a sub-sig.), and **parameterization** (a specification with a formal parameter sig., instantiated by pushout). The semantics of each is defined purely from $\mathrm{Sen}$, $\mathrm{Mod}$, and the satisfaction condition.

> [!theorem] Theorem 29.2.2: Institution-independence of structuring
> The soundness of the structuring ops. — that a structured specification denotes a well-defined model class, that translation preserves consequence, and that parameterized specifications instantiate correctly by **amalgamation** (a pushout of sigs. lifts to a pullback of model cats.) — holds in **any** institution satisfying mild conditions (existence of sig. pushouts, the amalgamation property). Hence the entire machinery of modular specification is developed **once**, abstractly, and applies to every logic of Parts I–III, VII, and §§27–28 simultaneously.

---

# Part X — Data Types, Domains, and Explicit Computation

## 30. W-Types, Containers, and Dependent Polynomial Functors

### 30.1. Containers and Polynomial Functors

> [!definition] Definition 30.1.1: Container
> A **container** (one-variable) is a pair $(\mathsf{Sh},\mathsf{Pos})$ with $\mathsf{Sh}$ a set of **shapes** and $\mathsf{Pos}:\mathsf{Sh}\to\mathbf{Set}$ a family of **position** sets, $\mathsf{Pos}(s)$ being the positions of shape $s$. Its **extension** is the endofunctor
> $$
> \llbracket\mathsf{Sh}\triangleleft\mathsf{Pos}\rrbracket(Y)\ :=\ \coprod_{s\in\mathsf{Sh}}\ Y^{\mathsf{Pos}(s)}.
> $$

> [!definition] Definition 30.1.2: Polynomial functor (general)
> A **polynomial** is a diagram $I\xleftarrow{\,s\,}B\xrightarrow{\,f\,}A\xrightarrow{\,t\,}J$ in $\mathbf{Set}$ (or a locally cartesian closed cat.); its associated **dependent poly. functor** $P:\mathbf{Set}/I\to\mathbf{Set}/J$ is the composite $\Sigma_t\circ\Pi_f\circ\Delta_s$ of reindexing, dependent product, and dependent sum. The one-object case ($I=J=1$) is a container; the case $I=J=S$ with $\Delta,\Sigma$ over $S$ is the **sorted** sig. functor $H_\Sigma$ of §2.

### 30.2. W-Types

> [!definition] Definition 30.2.1: W-type
> Given a container $(\mathsf{Sh},\mathsf{Pos})$, the **W-type** $\mathsf W_{s:\mathsf{Sh}}\,\mathsf{Pos}(s)$ is the **initial algebra** of $\llbracket\mathsf{Sh}\triangleleft\mathsf{Pos}\rrbracket$: the set of **well-founded trees** whose nodes are labeled by shapes $s$ with exactly $\mathsf{Pos}(s)$ children, one per position. Its single constructor is $\mathsf{sup}:\coprod_{s}\big(\mathsf{Pos}(s)\to\mathsf W\big)\to\mathsf W$, "a shape together with a child for each position." $\mathsf W$ is exactly the ground term algebra $\mathbf T_\Omega(\varnothing)$ when the container is a finitary sig..

> [!theorem] Theorem 30.2.2: W-types as initial algebras; induction and recursion
> $\mathsf W$ carries the structure of the **initial** $\llbracket\mathsf{Sh}\triangleleft\mathsf{Pos}\rrbracket$-algebra: ∀ algebra $(C,\theta)$ there is a unique hom. $\mathsf W\to C$ (**recursion**), and the corresponding **induction principle** holds (a predicate closed under $\mathsf{sup}$ holds of all trees). This is the base treatise's struc. recursion/induction (its §6, §13.3) stated for arbitrary (possibly infinitary) containers; in dependent type theory, W-types are the single primitive from which all well-founded inductive types ($\mathbb N$, lists, finite and countably-branching trees, ordinals up to $\varepsilon_0$, syntax of an algebraic theory) are derived.

### 30.3. Indexed and Dependent Inductive Types

> [!definition] Definition 30.3.1: Indexed container / inductive family
> An **indexed container** over an index set $I$ assigns to each $i\in I$ a set of shapes and to each shape a family of positions tagged by indices, yielding a dependent poly. functor on $\mathbf{Set}/I$. Its initial algebra is an **inductive family** $(D_i)_{i\in I}$ — the dependent generalization of the sorted term algebra (§2.3) in which the index/sort of a subterm may **depend on data**, not merely on a fixed sig. profile.

---

## 31. Initial-Algebra Semantics of Abstract Data Types

### 31.1. Specifications and Their Initial Semantics

> [!definition] Definition 31.1.1: Algebraic specification
> An **algebraic specification** is a presentation $\mathrm{Spec}=(\Sigma,E)$: a (many-sorted, §2) sig. $\Sigma$ of **constructors and ops.** together with a set $E$ of equations (or conditional equations / MEL axioms, §27). Its **model class** is $\mathrm{Mod}(\Sigma,E)$, the algebras satisfying $E$; its **initial semantics** is the (up-to-isomorphism unique) **initial** model $\mathbf I_{\mathrm{Spec}}$.

> [!theorem] Theorem 31.1.2: Existence and form of the initial model
> Every algebraic specification $(\Sigma,E)$ has an **initial model**, namely the ground-term quotient
> with $\theta_E$ the cong. generated by $E$ on ground terms.
> $$
> \mathbf I_{\mathrm{Spec}}\ \cong\ \mathbf T_\Sigma(\varnothing)\big/\theta_E,
> $$

### 31.2. No Junk, No Confusion

> [!definition] Definition 31.2.1: No junk; no confusion
> Relative to a chosen set of **constructor** symbols $\mathcal C\subseteq\Sigma$, a model $A$ has:
> $$
> \textbf{no junk}\quad \text{if } A \text{ is generated by the constructors: } A=\langle\varnothing\rangle_A \text{ using } \mathcal C \text{ (every element is a constructor term value);}
> $$
> $$
> \textbf{no confusion}\quad \text{if distinct constructor ground terms denote distinct elements, except as forced by } E.
> $$

> [!theorem] Theorem 31.2.2: Initiality = no junk + no confusion
> A model $A\in\mathrm{Mod}(\Sigma,E)$ is **initial** iff it has **no junk** and **no confusion**:
> Thus the design slogans are precisely the base treatise's **freeness = generatedness + injectivity** specialized to ground terms modulo $E$: initiality is "as free as $E$ allows."
> $$
> \textbf{no junk}\ \equiv\ \text{the unique homomorphism } \mathbf T_\Sigma(\varnothing)\to A \text{ is surjective (generatedness, base treatise §5.3);}
> $$
> $$
> \textbf{no confusion}\ \equiv\ \text{its kernel is exactly } \theta_E \text{ (no identifications beyond } E\text{, base treatise §5.4–5.5).}
> $$

---

## 32. Continuous Algebras, Domains, and Denotational Fixpoints

### 32.1. Complete Partial Orders and Continuity

> [!definition] Definition 32.1.1: CPO and continuous map
> A **(pointed) complete partial order (CPO)** is a poset $(D,\sqsubseteq)$ with a least element $\bot$ in which every **directed** subset (every finite subset has an upper bound in the set) has a supremum $\bigsqcup$. A map $f:D\to E$ is **monotone** if order-preserving and **(Scott-)continuous** if it preserves directed suprema: $f(\bigsqcup S)=\bigsqcup f[S]$ for directed $S$.

> [!theorem] Theorem 32.1.2: Kleene fixed-point theorem
> Every Scott-continuous self-map $f:D\to D$ on a pointed CPO has a **least fixed point**
> the supremum of the ascending chain of finite approximations.
> $$
> \operatorname{lfp}(f)\ =\ \bigsqcup_{n\in\mathbb N} f^n(\bot)\ =\ \bigsqcup\,(\,\bot\sqsubseteq f(\bot)\sqsubseteq f(f(\bot))\sqsubseteq\cdots\,),
> $$

### 32.2. Denotational Semantics of Recursion

> [!construction] Construction 32.2.1: Denotation of a recursive program
> Interpret types as CPOs and a recursive definition $F=\Phi(F)$ (where $\Phi$ is continuous in the function-space CPO, itself a CPO under the pointwise order with continuous functions) by $\llbracket F\rrbracket:=\operatorname{lfp}(\Phi)=\bigsqcup_n\Phi^n(\bot)$ (Theorem 32.1.2). Non-termination on an input $a$ is denoted by $\llbracket F\rrbracket(a)=\bot$; partial and infinite results are directed suprema in the completed term algebra (§16.2).

> [!theorem] Theorem 32.2.2: Adequacy and full abstraction (schematic)
> For a typed functional language with denotational semantics $\llbracket-\rrbracket$ into domains and operational semantics by rewriting (§13), **computational adequacy** holds: a program **terminates operationally** iff its **denotation is $\ne\bot$** (at ground type, equals the computed value). The stronger **full abstraction** property — operational (observational) equiv. coincides with equality of denotations — is delicate and **fails** for the naive domain model of sequential higher-order languages (the **parallel-or** problem), repaired only by refined models (stable/sequential domains, games).

### 32.3. Algebraic and Bifinite Domains

> [!definition] Definition 32.3.1: Compact elements and algebraic domains
> An element $c$ of a CPO is **compact (finite)** if whenever $c\sqsubseteq\bigsqcup S$ for directed $S$, then $c\sqsubseteq s$ for some $s\in S$. A CPO is **algebraic** if every element is the directed supremum of the compact elements below it, and a **Scott domain** if additionally bounded-complete.

---

## 33. Explicit Substitution Calculi

### 33.1. The $\lambda\sigma$-Calculus

> [!definition] Definition 33.1.1: Syntax of explicit substitutions
> The **$\lambda\sigma$-calculus** extends de Bruijn $\lambda$-terms (§6) with two syntactic cats. — **terms** and **substs.** — and constructors making subst. explicit:
> $$
> \textbf{terms}\quad a ::= \underline 1 \mid a\,b \mid \lambda a \mid a[s];\qquad \textbf{substitutions}\quad s ::= \mathrm{id} \mid {\uparrow} \mid a\cdot s \mid s\circ t,
> $$

> [!definition] Definition 33.1.2: The $\sigma$-rules and $\mathrm{Beta}$
> The calculus has a set of **$\sigma$-rules** that **propagate** substs. through term structure and compose them (e.g. $(a\,b)[s]\to a[s]\,b[s]$, $(\lambda a)[s]\to\lambda(a[\underline 1\cdot(s\circ{\uparrow})])$, $\underline 1[a\cdot s]\to a$, associativity/identity laws for $\circ$), together with the rule
> $$
> \mathrm{Beta}:\quad (\lambda a)\,b\ \to\ a[\,b\cdot\mathrm{id}\,]
> $$

### 33.2. Properties

> [!theorem] Theorem 33.2.1: The substitution sub-calculus is convergent
> The $\sigma$-rules **without** $\mathrm{Beta}$ form a **convergent** (terminating and confluent) rewrite system (§13): every term-with-explicit-substs. has a unique $\sigma$-normal form, which is the corresponding pure de Bruijn term with all substs. carried out. Thus the meta-level de Bruijn subst. (§6.2) is exactly **$\sigma$-normalization**, turning the base treatise's subst. op. into a terminating computation.

---

# Part XI — Refinements of the Effective Theory

## 34. Term Graph Rewriting and Sharing

### 34.1. Term Graphs

> [!definition] Definition 34.1.1: Term graph
> A **term graph** over $\Omega$ is a labeled graph: a finite set $N$ of **nodes**, a labeling $\mathrm{lab}:N\to\Omega\cup X$, a **successor** function giving each node labeled $f\in\Omega_n$ an ordered list of $n$ successor nodes, and a distinguished **root**. An **acyclic** term graph denotes a finite term by **unraveling** (the tree of paths from the root); a **cyclic** term graph denotes a **rational infinite term** (§16.2).

> [!definition] Definition 34.1.2: Graph rewrite step
> A **term graph rewrite rule** is a pair of graphs (a redex pattern and a replacement) with an interface of shared nodes. A **rewrite step** matches the left pattern as a subgraph (a graph hom.), **redirects** edges to the replacement, and garbage-collects unreachable nodes.

### 34.2. Soundness and Speedups

> [!theorem] Theorem 34.2.1: Adequacy of acyclic term graph rewriting
> For an ordinary (left-linear) TRS, acyclic term graph rewriting is **sound and complete** w.r.t. term rewriting on the unravelings: a graph rewrite step corresponds to one-or-more parallel term rewrite steps on the denoted term, and every term rewrite sequence is realized by a graph rewrite sequence. Sharing can yield **exponential speedups** (one graph step effects many term steps on shared copies) and is what makes call-by-need evaluation efficient.

---

## 35. Modularity of Termination and Confluence

> [!definition] Definition 35.1.1: Disjoint and constructor-sharing unions
> Two TRSs $R_1$ (over $\Omega_1$) and $R_2$ (over $\Omega_2$) form a **disjoint union** $R_1\uplus R_2$ if $\Omega_1\cap\Omega_2=\varnothing$; they form a **constructor-sharing union** if they share only **constructors** (symbols not occurring at the head of any left side). A property $\mathsf P$ is **modular** for a class of unions if $\mathsf P(R_1)\wedge\mathsf P(R_2)\Rightarrow\mathsf P(R_1\cup R_2)$.

> [!theorem] Theorem 35.1.2: Toyama's theorem (modularity of confluence)
> **Confluence is modular for disjoint unions:** if $R_1$ and $R_2$ are confluent and sig.-disjoint, then $R_1\uplus R_2$ is confluent (Toyama). Confluence is robust under combination.

> [!theorem] Theorem 35.1.4: Conditions restoring modular termination
> Termination **is** modular for disjoint unions under additional hypotheses: if both systems are **non-collapsing** (no rule has a variable right side) **or** both are **non-duplicating** (no rule has more occurrences of a variable on the right than the left), the union terminates; likewise **completeness** (convergence) is modular for disjoint unions (Toyama–Klop–Barendregt), and there are refined results for constructor-sharing and hierarchical unions. The general failure (Warning 35.1.3) is repaired exactly by controlling collapsing and duplicating rules.

---

## 36. Equational Theorem Proving: Paramodulation and Superposition

### 36.1. Paramodulation

> [!definition] Definition 36.1.1: Clauses and the paramodulation rule
> A **clause** is a finite disjunction of literals (atoms or negated atoms), with equality $\approx$ a distinguished predicate. The **paramodulation** inference combines resolution with equational replacement: from clauses $C\vee s\approx t$ and $D[u]$ (with $u$ a subterm), if $\sigma=\mathrm{mgu}(s,u)$, derive
> $$
> \big(C\vee D[t]\big)\sigma,
> $$

### 36.2. Superposition

> [!definition] Definition 36.2.1: Ordered superposition with selection
> **Superposition** is paramodulation **restricted** by a reduction ordering $>$ (§13.2) and a literal selection function: inferences are performed only into **maximal** terms of **maximal** literals and only in the $>$-decreasing direction (rewriting big to small), and rewriting **below variables** is forbidden (as in critical pairs, §13.3). These restrictions drastically prune the search space while preserving refutation completeness.

> [!theorem] Theorem 36.2.2: Completeness of superposition; completion as a special case
> The **superposition calculus** (ordered superposition + ordered resolution + equality factoring + redundancy elimination) is **sound and refutation-complete** for first-order logic with equality, and is **compatible with redundancy**: clauses subsumed or simplified by smaller ones may be deleted, making saturation practical. **Restricted to unit equations** (clauses that are single equations), superposition **coincides with unfailing Knuth–Bendix completion** (§13.4): completion is the equational special case of superposition.

---

# Part XII — Behavioral Specification

## 37. Hidden Algebra and Observational Equivalence

### 37.1. Hidden Signatures and Behavioral Equivalence

> [!definition] Definition 37.1.1: Hidden signature
> A **hidden sig.** partitions sorts into **visible** sorts $V$ (data: Booleans, integers — interpreted by a fixed data algebra) and **hidden** sorts $H$ (states). Operations are classified as **attributes** (hidden input, visible output — observations), **methods** (hidden input and output — state changes), and data ops. on $V$.

> [!definition] Definition 37.1.2: Behavioral (observational) equivalence
> Two states $a,b$ of a hidden algebra are **behaviorally equivalent**, $a\equiv b$, if **every experiment yields the same visible result**: for all visible-result contexts $C[\,]$ (built from the hidden ops.), $C[a]=C[b]$ in the data algebra. $\equiv$ is the largest **hidden cong.** (cong. identical to equality on visible sorts); it is the **final/greatest** such relation, dual to the least cong. $\theta_E$ of initial semantics.

> [!theorem] Theorem 37.1.3: Behavioral satisfaction and final models
> A hidden specification is interpreted by **behavioral satisfaction**: an equation holds **behaviorally** if both sides are behaviorally equivalent (not necessarily equal). The model class admits a **final (terminal)** model in which states are identified exactly when behaviorally equivalent — the minimal-state realization, the coalgebraic dual (final coalgebra, §17.2) of the initial data algebra of §31.

---

# Part XIII — Recursion Schemes and the Effectivity Map

## 38. Recursion Schemes

### 38.1. Catamorphisms and Anamorphisms

> [!definition] Definition 38.1.1: Catamorphism (fold)
> For the sig. functor $H_\Omega$ with initial algebra $(\mu H_\Omega,\mathrm{in})$ and any algebra $(C,\theta:H_\Omega C\to C)$, the **catamorphism** $(\!|\theta|\!):\mu H_\Omega\to C$ is the unique hom. with
> $$
> (\!|\theta|\!)\circ\mathrm{in}\ =\ \theta\circ H_\Omega(\!|\theta|\!).
> $$

> [!definition] Definition 38.1.2: Anamorphism (unfold)
> For the final coalgebra $(\nu H_\Omega,\mathrm{out})$ (§17.2) and any coalgebra $(C,\gamma:C\to H_\Omega C)$, the **anamorphism** $[\!(\gamma)\!]:C\to\nu H_\Omega$ is the unique coalgebra hom. with
> $$
> \mathrm{out}\circ[\!(\gamma)\!]\ =\ H_\Omega[\!(\gamma)\!]\circ\gamma,
> $$

> [!definition] Definition 38.1.3: Hylomorphism
> A **hylomorphism** is the composite of an anamorphism followed by a catamorphism, $(\!|\theta|\!)\circ[\!(\gamma)\!]$, computing through a (virtual) intermediate data structure that is built and consumed without being materialized. It models **divide-and-conquer** recursion (the call tree is the intermediate structure).

### 38.2. Parametrized and Course-of-Value Schemes

> [!definition] Definition 38.2.1: Paramorphism and apomorphism
> A **paramorphism** generalizes the catamorphism by giving each recursive step access to the **original substructure** as well as the recursively computed value (recursion "with the input in hand"), justified by the universal property of $\mu H_\Omega$ applied to the algebra on $C\times\mu H_\Omega$. Its dual, the **apomorphism**, generalizes the anamorphism by allowing each step to either continue corecursively **or** halt by supplying a whole final-coalgebra element (corecursion "with early termination").

> [!definition] Definition 38.2.2: Histomorphism and futumorphism
> A **histomorphism** gives each step access to **all** previously computed values (course-of-value recursion, e.g. Fibonacci), justified via the **cofree comonad** on $H_\Omega$; its dual, the **futumorphism**, allows each corecursive step to produce **several** layers at once, via the **free monad**. These comonad/monad-justified schemes are the most general total recursion/corecursion patterns in common use.

> [!theorem] Theorem 38.2.3: Schemes as instances of (co)initiality with (co)monads
> Each recursion scheme is a uniquely-determined map guaranteed by a universal property: catamorphism/paramorphism/histomorphism by **initiality** of $\mu H_\Omega$ (possibly twisted by a comonad), anamorphism/apomorphism/futumorphism by **finality** of $\nu H_\Omega$ (possibly twisted by a monad). Their existence and uniqueness are corollaries of the base treatise's and §17's universal properties; their value is **guaranteed totality and termination/productivity** by constr., in contrast to general (possibly non-terminating) recursion.

---

## 39. The Decidability and Complexity Map

### 39.1. Core Problems and Their Status

---

# Part XIV — Synthesis

## 40. Synthesis

### 40.1. The Companion's Spine

### 40.2. Comparison Tables

### 40.3. Consolidated Failure-Mode Checklist

### 40.4. Master Index of Parts

### 40.5. Closing Synthesis

---

# Appendices

## Appendix A. Worked Instances

### A.1. Peano Naturals: Initial Algebra, Recursion, Coalgebraic Dual

### A.2. Lists and the Sorted/Parametric Layer

### A.3. Boolean Algebra: Variety, SI, Recognizability

### A.4. The Untyped $\lambda$-Calculus: Binding, Rewriting, Algebra

---

## Appendix B. Gröbner Bases as Knuth–Bendix Completion

> [!definition] Definition B.1: Polynomial reduction
> Fix a field $k$, variables $x_1,\dots,x_n$, and a **monomial order** $>$ (a reduction order on monomials, e.g. lexicographic or degree-reverse-lexicographic — an instance of §13.2). A polynomial $f$ **reduces** modulo a set $G$ of polynomials by repeatedly cancelling the **leading monomial** of $f$ using a $g\in G$ whose leading monomial divides it: $f\to_G f-\tfrac{\mathrm{lt}(f)}{\mathrm{lt}(g)}\,g$.

> [!definition] Definition B.2: S-polynomial (critical pair)
> For $g_1,g_2\in G$ with leading terms $\mathrm{lt}(g_i)$, the **S-polynomial** is
> $$
> S(g_1,g_2)\ =\ \frac{L}{\mathrm{lt}(g_1)}\,g_1\ -\ \frac{L}{\mathrm{lt}(g_2)}\,g_2,\qquad L=\operatorname{lcm}(\mathrm{lt}(g_1),\mathrm{lt}(g_2)),
> $$

> [!theorem] Theorem B.3: Buchberger's criterion = the Critical Pair Lemma
> A finite set $G$ is a **Gröbner basis** of the ideal it generates iff **every S-polynomial reduces to $0$ modulo $G$**. This is the Critical Pair Lemma (Thm 13.3.2) for polynomial reduction: $G$ is **confluent** (every polynomial has a unique normal form) iff all critical pairs (S-polynomials) are joinable; termination is automatic from the monomial order (Dickson's lemma supplies well-foundedness, the polynomial analogue of Kruskal's theorem, Def 13.2.2).

> [!theorem] Theorem B.4: Buchberger's algorithm = Knuth–Bendix completion
> **Buchberger's algorithm** — repeatedly compute S-polynomials, reduce them modulo the current basis, and adjoin any nonzero remainders as new basis elements until all S-polynomials reduce to $0$ — is exactly **Knuth–Bendix completion** (Constr 13.4.1) for the equational theory of the ideal, with S-polynomials as deduced critical pairs and the monomial order as the reduction order. Unlike the general case (Warn 13.4.4), completion here **always terminates** (Dickson's lemma bounds the process), so a finite Gröbner basis always exists and the **ideal membership problem** ($f\in I$?) is decided by reduction to $0$ — the polynomial word problem, always solvable.

---

## Appendix C. Unification at Work: Type Inference and Logic Programming

### C.1. Hindley–Milner Type Inference

> [!definition] Definition C.1.1: Types as a free algebra; type substitution
> Monomorphic types over base types and a binary function-space constructor $\to$ form the free algebra $\mathbf T_{\{\to,\dots\}}(\mathrm{TVar})$ on a set $\mathrm{TVar}$ of **type variables** (base treatise §2). A **type subst.** is a subst. in this algebra (Def 1.4.3); type-variable instantiation is its homomorphic action.

> [!theorem] Theorem C.1.2: Principal types via unification (Hindley–Milner / Algorithm W)
> For the let-polymorphic $\lambda$-calculus, type inference reduces to **first-order unification** in the type algebra: each application node imposes an equation $\tau_{\mathrm{fun}}\stackrel{?}{=}\tau_{\mathrm{arg}}\to\beta$ (with $\beta$ fresh), and the **mgu** of the accumulated constraints (Thm 12.2.2) yields the **principal (most general) type**, of which every valid type of the expression is an instance (the subsumption order, Def 12.1.2). The occurs check (Def 12.2.3) rejects self-referential types such as $\alpha\to\alpha=\alpha$, which is exactly the failure of typing $\lambda x.xx$ without recursive types.

### C.2. SLD-Resolution and Logic Programming

> [!definition] Definition C.2.1: Horn clauses and SLD-resolution
> A **definite (Horn) program** is a set of clauses $A\leftarrow B_1,\dots,B_k$ (atoms over a first-order term algebra). Given a **goal** $\leftarrow G_1,\dots,G_m$, an **SLD-resolution** step selects a goal atom $G_i$, chooses a (renamed) program clause $A\leftarrow \vec B$, computes $\sigma=\mathrm{mgu}(G_i,A)$ (Thm 12.2.2), and replaces the goal by $(\dots,G_{i-1},\vec B,G_{i+1},\dots)\sigma$.

> [!theorem] Theorem C.2.2: Soundness and completeness of SLD-resolution
> For definite programs, SLD-resolution is **sound** (every computed answer is a logical consequence) and **complete** (every correct answer is subsumed by a computed one), with the **least Herbrand model** — the ground atoms derivable, an initial-algebra-style least fixpoint (Thm 32.1.2 / §9) of the program's immediate-consequence operator — as declarative semantics. Unification supplies the single inference engine; the least fixpoint supplies the meaning.

---

## Appendix D. Index of Notation

> [!notation] Notation D.1: Principal symbols of the companion
> The recurring notation, with defining locations.

---

## Appendix E. Further Worked Instances

### E.1. Groups: Decidable Free Case, Undecidable General Case

### E.2. Relation Algebras: A Non-Finitely-Axiomatizable Representable Class

### E.3. A Recognizable Tree Language and Its Minimal Automaton

### E.4. A Quantitative Coalgebra: Streams and Probabilistic Transition Systems

---

## Appendix F. Algebraic Logic: Completeness, Finite Models, and Decidable Fragments

> [!theorem] Theorem F.1: Completeness as representability
> Gödel's completeness theorem for first-order logic is equivalent, under the cylindric algebraization (§10.3), to the statement that the Lindenbaum cylindric algebra $\mathfrak{Lt}(\Theta)$ of every consistent theory is **representable** (embeds into a cylindric set algebra). "Provable $=$ valid" becomes "the syntactic algebra has a set-theoretic model," and the constr. of a model from a consistent theory is the constr. of a representation. Thus the central metatheorem of logic is a **representation theorem** in algebraic logic, parallel to Stone's theorem for Boolean algebras (§28.2).

> [!theorem] Theorem F.2: Finite model property and decidability
> A variety (or quasivariety) of algebras has the **finite model property (FMP)** if every non-identity is refuted in a finite member. FMP plus finite axiomatizability yields **decidability** of the equational theory: enumerate proofs and finite countermodels in parallel.
