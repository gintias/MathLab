---
title: "Many-Sorted First-Order Logic — Formal Theory Reference"
subtitle: "Primitive data, sorted syntax, semantics, deduction, models, metatheory, and integration with algebraic syntax"
tags: [logic, first-order-logic, many-sorted, universal-algebra, syntax, semantics, models, deduction, completeness, compactness, lowenheim-skolem, schemas, contexts]
---

# Many-Sorted First-Order Logic — Formal Theory Reference

## 0. Orientation

This note fixes a presentation-neutral development of many-sorted first-order logic. The primitive logical data are deliberately minimal: a set of sorts, sort-indexed variables, sort-profiled function symbols, and sort-profiled relation symbols. Constants are nullary function symbols. Formulas are not primitive sorts. Equality is a logical symbol at each sort unless explicitly removed.

The formal pipeline is

$$
\text{sorts and profiles}
\to
\text{many-sorted signature}
\to
\text{term algebra}
\to
\text{raw formulas}
\to
\text{binding and substitution}
\to
\text{structures and assignments}
\to
\text{satisfaction}
\to
\text{semantic consequence}
\to
\text{deductive consequence}
\to
\text{metatheory}.
$$

The core theory does not choose strings, trees, tuples, de Bruijn codes, address trees, or any other concrete presentation. Such objects enter only as representations after an explicit isomorphism with the invariant syntax object has been supplied.

> [!warning] Warning 0.1: Core object versus representation
> A term, formula, context, derivation, or schema is not identified with a string or parse tree in the core theory. A concrete carrier $P$ becomes a presentation of syntax only after a structure-preserving map
>
> $$
> r:P\cong \operatorname{Syn}
> $$
>
> has been specified. Any operation defined by inspecting a representation must be transported through such an isomorphism before it is a syntax-level operation.

---

## 1. Ambient Set-Theoretic and Sorted Notation

### 1.1. Sets, words, and profiles

> [!notation] Notation 1.1: Ambient universe
> Work in a fixed set-theoretic universe containing all sets, families, products, quotient sets, syntax sets, structures, assignments, theories, derivation objects, and model classes used below. Unless explicitly stated otherwise, every language, signature, carrier, and variable supply is a set.

> [!notation] Notation 1.2: Finite ordinals and tuples
> For $n\in\mathbb N$, identify
>
> $$
> n=\{0,1,\dots,n-1\}.
> $$
>
> For a set $A$ define
>
> $$
> A^n=\{a:n\to A\}.
> $$
>
> If $a\in A^n$, write $a=(a_0,\dots,a_{n-1})$ with $a_i=a(i)$.

> [!notation] Notation 1.3: Words
> For a set $A$ define
>
> $$
> A^{<\omega}:=\coprod_{n\in\mathbb N}A^n.
> $$
>
> An element $w\in A^{<\omega}$ is a finite word. If $w\in A^n$, write
>
> $$
> |w|=n.
> $$
>
> The unique element of $A^0$ is denoted $()$.

> [!definition] Definition 1.4: Sort set
> A **sort set** is a set
>
> $$
> S.
> $$
>
> Its elements are called **sorts**. The one-sorted case is the special case $S=\{*\}$.

> [!definition] Definition 1.5: Input profile and operation profile
> Let $S$ be a sort set.
>
> An **input profile** is a word
>
> $$
> w=(s_0,\dots,s_{n-1})\in S^n
> $$
>
> for some $n\in\mathbb N$.
>
> An **operation profile** is a pair
>
> $$
> (w,s)\in S^{<\omega}\times S,
> $$
>
> written
>
> $$
> w\to s
> $$
>
> or
>
> $$
> (s_0,\dots,s_{n-1})\to s.
> $$
>
> Its arity is $|w|=n$.

> [!notation] Notation 1.6: Sorted products along a profile
> Let $A=(A_s)_{s\in S}$ be an $S$-indexed family of sets and let $w=(s_0,\dots,s_{n-1})\in S^n$. Define
>
> $$
> A_w:=\prod_{i<n}A_{s_i}.
> $$
>
> If $w=()$, then
>
> $$
> A_{()}=1
> $$
>
> is a fixed singleton.

### 1.2. Sorted families and sorted maps

> [!definition] Definition 1.7: $S$-sorted family
> Let $S$ be a set. An **$S$-sorted family of sets** is a function
>
> $$
> A:S\to\mathbf{Set},
> $$
>
> written
>
> $$
> A=(A_s)_{s\in S}.
> $$

> [!definition] Definition 1.8: $S$-sorted map
> Let $A=(A_s)_{s\in S}$ and $B=(B_s)_{s\in S}$ be $S$-sorted families. An **$S$-sorted map**
>
> $$
> h:A\to B
> $$
>
> is a family of functions
>
> $$
> h=(h_s:A_s\to B_s)_{s\in S}.
> $$
>
> Composition and identities are componentwise:
>
> $$
> (k\circ h)_s=k_s\circ h_s,
> \qquad
> (\operatorname{id}_A)_s=\operatorname{id}_{A_s}.
> $$

> [!notation] Notation 1.9: Componentwise inclusion and power family
> For $S$-sorted families $A$ and $B$, write
>
> $$
> A\subseteq B
> $$
>
> iff $A_s\subseteq B_s$ for every $s\in S$. Define
>
> $$
> \mathcal P_S(A):=\prod_{s\in S}\mathcal P(A_s)
> $$
>
> ordered componentwise by inclusion. If $h:A\to B$ is a sorted map, define
>
> $$
> h[A]=(h_s[A_s])_{s\in S}.
> $$

> [!definition] Definition 1.10: Tagged total carrier
> If a one-sorted ambient carrier is needed for an $S$-sorted family $A$, use the tagged coproduct
>
> $$
> \coprod_{s\in S}A_s=\{(s,a):s\in S,\ a\in A_s\}.
> $$
>
> The untagged union $\bigcup_{s\in S}A_s$ is not used unless the components are already disjoint and this has been stated.

> [!warning] Warning 1.11: Sort-indexed equality
> Equality of elements is typed by ambient membership. If $a\in A_s$ and $b\in A_t$ with $s\neq t$, the expression $a=b$ is metatheoretically meaningful only if $A_s$ and $A_t$ are parts of a common ambient set; it is not an object-language equality formula. Object-language equality compares terms of the same sort.

---

## 2. Primitive Data of a Many-Sorted First-Order Language

### 2.1. Nonlogical symbols

> [!definition] Definition 2.1: Many-sorted first-order signature
> A **many-sorted first-order signature** is a tuple
>
> $$
> \mathcal L=(S,\operatorname{Func}_{\mathcal L},\operatorname{Rel}_{\mathcal L})
> $$
>
> consisting of the following data:
>
> 1. a sort set $S$;
> 2. a family of pairwise disjoint sets of function symbols
>    $$
>    \operatorname{Func}_{\mathcal L}=(\operatorname{Func}_{\mathcal L,w,s})_{(w,s)\in S^{<\omega}\times S};
>    $$
> 3. a family of pairwise disjoint sets of relation symbols
>    $$
>    \operatorname{Rel}_{\mathcal L}=(\operatorname{Rel}_{\mathcal L,w})_{w\in S^{<\omega}}.
>    $$
>
> If $f\in\operatorname{Func}_{\mathcal L,w,s}$, write
>
> $$
> f:w\to s.
> $$
>
> If $R\in\operatorname{Rel}_{\mathcal L,w}$, write
>
> $$
> R:w.
> $$

> [!definition] Definition 2.2: Constants
> For $s\in S$, a **constant symbol of sort $s$** is an element
>
> $$
> c\in\operatorname{Func}_{\mathcal L,(),s}.
> $$
>
> Constants are nullary function symbols. There is no separate primitive set of constants.

> [!notation] Notation 2.3: Underlying symbol sets
> Define
>
> $$
> |\operatorname{Func}_{\mathcal L}|:=\coprod_{(w,s)\in S^{<\omega}\times S}\operatorname{Func}_{\mathcal L,w,s}
> $$
>
> and
>
> $$
> |\operatorname{Rel}_{\mathcal L}|:=\coprod_{w\in S^{<\omega}}\operatorname{Rel}_{\mathcal L,w}.
> $$
>
> For $f\in|\operatorname{Func}_{\mathcal L}|$, define $\operatorname{in}(f)=w$ and $\operatorname{out}(f)=s$ iff $f\in\operatorname{Func}_{\mathcal L,w,s}$. For $R\in|\operatorname{Rel}_{\mathcal L}|$, define $\operatorname{prof}(R)=w$ iff $R\in\operatorname{Rel}_{\mathcal L,w}$.

> [!definition] Definition 2.4: Variable supply for $\mathcal L$
> A **variable supply over $S$** is an $S$-sorted family
>
> $$
> \operatorname{Var}=(\operatorname{Var}_s)_{s\in S}
> $$
>
> such that:
>
> 1. each $\operatorname{Var}_s$ is infinite;
> 2. the sets $\operatorname{Var}_s$ are pairwise disjoint.
>
> Elements of $\operatorname{Var}_s$ are variables of sort $s$.

> [!definition] Definition 2.5: Formal language datum
> A **many-sorted first-order language datum** is a pair
>
> $$
> (\mathcal L,\operatorname{Var})
> $$
>
> where $\mathcal L$ is a many-sorted first-order signature with sort set $S$ and $\operatorname{Var}$ is a variable supply over $S$.
>
> When $\operatorname{Var}$ is fixed, the language datum is denoted simply by $\mathcal L$.

> [!remark] Remark 2.6: Logical symbols
> The logical apparatus consists of $\neg$, $\to$, $\forall$, parentheses or formation markers, and equality symbols $=_s$ for $s\in S$. The connectives $\wedge$, $\vee$, $\leftrightarrow$, and $\exists$ are definitional abbreviations unless explicitly added as primitive logical constructors. Logical symbols are not elements of $|\operatorname{Func}_{\mathcal L}|$ or $|\operatorname{Rel}_{\mathcal L}|$.

> [!warning] Warning 2.7: No formula sort in the primitive language
> The sort set $S$ classifies variables, terms, function inputs and outputs, and structure carriers. The set of formulas is a separate recursively generated set. Adding a formula sort is an algebraic encoding, not part of the basic many-sorted first-order language datum.

### 2.2. Functional reduct of a language

> [!definition] Definition 2.8: Functional signature of $\mathcal L$
> The **functional reduct** or **term signature** of $\mathcal L$ is the many-sorted algebraic signature
>
> $$
> \Sigma_{\mathcal L}:=(S,(\operatorname{Func}_{\mathcal L,w,s})_{(w,s)\in S^{<\omega}\times S}).
> $$
>
> Its operation symbols are exactly the function symbols of $\mathcal L$, including constants.

> [!definition] Definition 2.9: Relational profile family
> The **relational part** of $\mathcal L$ is the profile-indexed family
>
> $$
> \operatorname{Rel}_{\mathcal L}=(\operatorname{Rel}_{\mathcal L,w})_{w\in S^{<\omega}}.
> $$
>
> Relation symbols do not produce terms. They are used only in atomic formulas.

> [!proposition] Proposition 2.10: Language decomposition
> A many-sorted first-order signature $\mathcal L$ is equivalently the data
>
> $$
> \mathcal L=(\Sigma_{\mathcal L},\operatorname{Rel}_{\mathcal L}),
> $$
>
> where $\Sigma_{\mathcal L}$ is a many-sorted functional signature over $S$ and $\operatorname{Rel}_{\mathcal L}$ is a family of relation-symbol sets indexed by $S^{<\omega}$.

> [!proof-sketch] Proof Sketch 2.10
> The original tuple determines $\Sigma_{\mathcal L}$ by forgetting relation symbols and determines $\operatorname{Rel}_{\mathcal L}$ by forgetting function symbols. Conversely, $\Sigma_{\mathcal L}$ supplies $S$ and all function-profile classes, while $\operatorname{Rel}_{\mathcal L}$ supplies all relation-profile classes. No additional primitive data are required.

---

## 3. Terms as the Free Algebra of the Functional Reduct

### 3.1. Term algebra

> [!definition] Definition 3.1: $\Sigma_{\mathcal L}$-algebra
> A **$\Sigma_{\mathcal L}$-algebra** is a tuple
>
> $$
> \mathbf A=(A,(f^{\mathbf A})_{f\in|\operatorname{Func}_{\mathcal L}|})
> $$
>
> where $A=(A_s)_{s\in S}$ is an $S$-sorted family and, for each $f\in\operatorname{Func}_{\mathcal L,w,s}$,
>
> $$
> f^{\mathbf A}:A_w\to A_s
> $$
>
> is a function.

> [!definition] Definition 3.2: Homomorphism of functional reducts
> If $\mathbf A$ and $\mathbf B$ are $\Sigma_{\mathcal L}$-algebras, a homomorphism
>
> $$
> h:\mathbf A\to\mathbf B
> $$
>
> is an $S$-sorted map $h=(h_s:A_s\to B_s)_{s\in S}$ such that, for every $f\in\operatorname{Func}_{\mathcal L,w,s}$ with $w=(s_0,\dots,s_{n-1})$ and every $a\in A_w$,
>
> $$
> h_s(f^{\mathbf A}(a_0,\dots,a_{n-1}))
> =
> f^{\mathbf B}(h_{s_0}(a_0),\dots,h_{s_{n-1}}(a_{n-1})).
> $$

> [!definition] Definition 3.3: Term algebra as a free algebra
> The **$\mathcal L$-term algebra on $\operatorname{Var}$** is a free $\Sigma_{\mathcal L}$-algebra
>
> $$
> (\mathbf{Term}_{\mathcal L},\eta)
> $$
>
> on the $S$-sorted generator family $\operatorname{Var}$.
>
> Thus $\mathbf{Term}_{\mathcal L}$ is a $\Sigma_{\mathcal L}$-algebra with carrier
>
> $$
> \operatorname{Term}_{\mathcal L}=(\operatorname{Term}_{\mathcal L,s})_{s\in S}
> $$
>
> and generator insertion
>
> $$
> \eta_s:\operatorname{Var}_s\to\operatorname{Term}_{\mathcal L,s}
> $$
>
> such that for every $\Sigma_{\mathcal L}$-algebra $\mathbf A$ and every sorted map $g:\operatorname{Var}\to A$, there exists a unique homomorphism
>
> $$
> \widehat g:\mathbf{Term}_{\mathcal L}\to\mathbf A
> $$
>
> satisfying
>
> $$
> \widehat g\circ\eta=g.
> $$

> [!notation] Notation 3.4: Terms of a sort
> An element
>
> $$
> t\in\operatorname{Term}_{\mathcal L,s}
> $$
>
> is an **$\mathcal L$-term of sort $s$**. If $w=(s_0,\dots,s_{n-1})$, write
>
> $$
> \operatorname{Term}_{\mathcal L,w}:=\prod_{i<n}\operatorname{Term}_{\mathcal L,s_i}.
> $$

> [!theorem] Theorem 3.5: Existence and uniqueness of term algebras
> For every many-sorted first-order language datum $(\mathcal L,\operatorname{Var})$, the term algebra $\mathbf{Term}_{\mathcal L}$ exists. If $(\mathbf F,\iota)$ and $(\mathbf G,\kappa)$ are two free $\Sigma_{\mathcal L}$-algebras on $\operatorname{Var}$, then there is a unique $\Sigma_{\mathcal L}$-isomorphism
>
> $$
> \nu:\mathbf F\cong\mathbf G
> $$
>
> such that
>
> $$
> \nu\circ\iota=\kappa.
> $$

> [!proof-sketch] Proof Sketch 3.5
> Existence follows from the usual construction of the free algebra for a finitary many-sorted signature, obtained as the least sorted family closed under the formal operations and containing the variables. The universal property is verified by structural recursion on generated terms. Uniqueness follows by applying the universal property in both directions and using uniqueness of homomorphic extensions to show the two composites are identities.

### 3.2. Formation and structural principles

> [!construction] Construction 3.6: Formal function application
> If $f\in\operatorname{Func}_{\mathcal L,w,s}$ and $w=(s_0,\dots,s_{n-1})$, the interpretation of $f$ in the free algebra is a function
>
> $$
> f^{\mathbf{Term}}:\operatorname{Term}_{\mathcal L,w}\to\operatorname{Term}_{\mathcal L,s}.
> $$
>
> For $t_i\in\operatorname{Term}_{\mathcal L,s_i}$, the term
>
> $$
> f^{\mathbf{Term}}(t_0,\dots,t_{n-1})\in\operatorname{Term}_{\mathcal L,s}
> $$
>
> is the formal application of $f$ to the tuple $(t_0,\dots,t_{n-1})$.

> [!proposition] Proposition 3.7: Sort-correct term formation
> Let $f\in\operatorname{Func}_{\mathcal L,w,s}$ with $w=(s_0,\dots,s_{n-1})$. The expression $f(t_0,\dots,t_{n-1})$ is a term of sort $s$ exactly when
>
> $$
> t_i\in\operatorname{Term}_{\mathcal L,s_i}
> $$
>
> for all $i<n$. There is no term $f(t_0,\dots,t_{n-1})$ in the language if any $t_i$ fails to have sort $s_i$.

> [!proof-sketch] Proof Sketch 3.7
> The formal operation $f^{\mathbf{Term}}$ has domain $\operatorname{Term}_{\mathcal L,w}$ and codomain $\operatorname{Term}_{\mathcal L,s}$. The domain condition is precisely the componentwise sort condition on the input tuple.

> [!theorem] Theorem 3.8: Structural induction for terms
> Let $P=(P_s)_{s\in S}$ be an $S$-sorted family with
>
> $$
> P_s\subseteq\operatorname{Term}_{\mathcal L,s}.
> $$
>
> Assume:
>
> 1. for every $s\in S$ and $x\in\operatorname{Var}_s$,
>    $$
>    \eta_s(x)\in P_s;
>    $$
> 2. for every $f\in\operatorname{Func}_{\mathcal L,w,s}$, if $w=(s_0,\dots,s_{n-1})$ and $t_i\in P_{s_i}$ for all $i<n$, then
>    $$
>    f^{\mathbf{Term}}(t_0,\dots,t_{n-1})\in P_s.
>    $$
>
> Then
>
> $$
> P_s=\operatorname{Term}_{\mathcal L,s}
> $$
>
> for every $s\in S$.

> [!proof-sketch] Proof Sketch 3.8
> The family $P$ is the carrier of a subalgebra of $\mathbf{Term}_{\mathcal L}$ containing the image of $\eta$. Since $\mathbf{Term}_{\mathcal L}$ is generated by $\eta[\operatorname{Var}]$, the least such subalgebra is all of $\mathbf{Term}_{\mathcal L}$.

> [!theorem] Theorem 3.9: Structural recursion for terms
> Let $B=(B_s)_{s\in S}$ be an $S$-sorted family. Suppose given:
>
> 1. functions
>    $$
>    b_s:\operatorname{Var}_s\to B_s
>    $$
>    for all $s\in S$;
> 2. for every $f\in\operatorname{Func}_{\mathcal L,w,s}$ with $w=(s_0,\dots,s_{n-1})$, a function
>    $$
>    F_f:B_w\to B_s.
>    $$
>
> Then there is a unique sorted map
>
> $$
> R:\operatorname{Term}_{\mathcal L}\to B
> $$
>
> satisfying
>
> $$
> R_s(\eta_s(x))=b_s(x)
> $$
>
> for $x\in\operatorname{Var}_s$, and
>
> $$
> R_s(f^{\mathbf{Term}}(t_0,\dots,t_{n-1}))
> =
> F_f(R_{s_0}(t_0),\dots,R_{s_{n-1}}(t_{n-1})).
> $$

> [!proof-sketch] Proof Sketch 3.9
> The data $(B,(F_f))$ make $B$ a $\Sigma_{\mathcal L}$-algebra. The sorted map $b:\operatorname{Var}\to B$ extends uniquely to a homomorphism $\widehat b:\mathbf{Term}_{\mathcal L}\to B$, and its homomorphism equations are exactly the displayed recursion clauses.

> [!definition] Definition 3.10: Variables occurring in a term
> For $t\in\operatorname{Term}_{\mathcal L,s}$ and $r\in S$, define
>
> $$
> \operatorname{Var}_r(t)\subseteq\operatorname{Var}_r
> $$
>
> by structural recursion:
>
> $$
> \operatorname{Var}_r(\eta_s(x))=
> \begin{cases}
> \{x\},&r=s,\\
> \varnothing,&r\neq s,
> \end{cases}
> $$
>
> and, for $f\in\operatorname{Func}_{\mathcal L,w,s}$ with $w=(s_0,\dots,s_{n-1})$,
>
> $$
> \operatorname{Var}_r(f(t_0,\dots,t_{n-1}))=
> \bigcup_{i<n}\operatorname{Var}_r(t_i).
> $$
>
> The sorted support of $t$ is
>
> $$
> \operatorname{Var}(t)=(\operatorname{Var}_r(t))_{r\in S}.
> $$

> [!proposition] Proposition 3.11: Finite support of terms
> For every $t\in\operatorname{Term}_{\mathcal L,s}$, the set
>
> $$
> \{(r,x):r\in S,
> \ x\in\operatorname{Var}_r(t)\}
> $$
>
> is finite.

> [!proof-sketch] Proof Sketch 3.11
> Apply structural induction. A variable term has one occurrence. A formal application has support equal to the finite union of the supports of its finitely many immediate subterms.

> [!definition] Definition 3.12: Closed terms
> A term $t\in\operatorname{Term}_{\mathcal L,s}$ is **closed** if
>
> $$
> \operatorname{Var}_r(t)=\varnothing
> $$
>
> for every $r\in S$. The family of closed terms is denoted
>
> $$
> \operatorname{CTerm}_{\mathcal L,s}:=\operatorname{Term}_{\mathcal L,s}\cap\operatorname{Term}_{\mathcal L,s}(\varnothing).
> $$

---

## 4. Atomic Formulas, Raw Formulas, and Binding

### 4.1. Atomic formulas

> [!definition] Definition 4.1: Equality atoms
> For $s\in S$, the set of **equality atoms of sort $s$** is
>
> $$
> \operatorname{EqAtom}_{\mathcal L,s}:=
> \operatorname{Term}_{\mathcal L,s}\times\operatorname{Term}_{\mathcal L,s}.
> $$
>
> The pair $(t,u)\in\operatorname{EqAtom}_{\mathcal L,s}$ is displayed as
>
> $$
> t=_s u.
> $$
>
> There is no equality atom $t=_{}u$ when $t$ and $u$ have different sorts.

> [!definition] Definition 4.2: Relation atoms
> If $R\in\operatorname{Rel}_{\mathcal L,w}$ and $w=(s_0,\dots,s_{n-1})$, the set of **$R$-atoms** is
>
> $$
> \{R\}\times\operatorname{Term}_{\mathcal L,w}.
> $$
>
> The element $(R,t_0,\dots,t_{n-1})$ is displayed as
>
> $$
> R(t_0,\dots,t_{n-1}).
> $$

> [!definition] Definition 4.3: Atomic formula set
> The set of **atomic $\mathcal L$-formulas** is
>
> $$
> \operatorname{Atom}_{\mathcal L}:=
> \left(\coprod_{s\in S}\operatorname{EqAtom}_{\mathcal L,s}\right)
> \coprod
> \left(\coprod_{w\in S^{<\omega}}\coprod_{R\in\operatorname{Rel}_{\mathcal L,w}}
> \{R\}\times\operatorname{Term}_{\mathcal L,w}\right).
> $$

> [!proposition] Proposition 4.4: Sort correctness of atoms
> Let $R\in\operatorname{Rel}_{\mathcal L,w}$ with $w=(s_0,\dots,s_{n-1})$. The expression $R(t_0,\dots,t_{n-1})$ is an atomic formula iff
>
> $$
> t_i\in\operatorname{Term}_{\mathcal L,s_i}
> $$
>
> for all $i<n$. The expression $t=_s u$ is an atomic formula iff
>
> $$
> t,u\in\operatorname{Term}_{\mathcal L,s}.
> $$

> [!proof-sketch] Proof Sketch 4.4
> Both assertions restate membership in the corresponding tagged coproduct defining $\operatorname{Atom}_{\mathcal L}$.

### 4.2. Raw formulas

> [!definition] Definition 4.5: Formula constructor signature
> Define the raw formula constructor signature over the set $\operatorname{Atom}_{\mathcal L}$ by the following operations on a single formula carrier:
>
> 1. every $\alpha\in\operatorname{Atom}_{\mathcal L}$ is a nullary generator;
> 2. one unary connective constructor
>    $$
>    \neg;
>    $$
> 3. one binary connective constructor
>    $$
>    \to;
>    $$
> 4. for every $s\in S$ and every $x\in\operatorname{Var}_s$, one unary binder constructor
>    $$
>    \forall_x.
>    $$

> [!definition] Definition 4.6: Raw formula set
> The set of **raw $\mathcal L$-formulas** is the least set
>
> $$
> \operatorname{Form}^{\mathrm{raw}}_{\mathcal L}
> $$
>
> satisfying:
>
> 1. $\operatorname{Atom}_{\mathcal L}\subseteq\operatorname{Form}^{\mathrm{raw}}_{\mathcal L}$;
> 2. if $\varphi\in\operatorname{Form}^{\mathrm{raw}}_{\mathcal L}$, then
>    $$
>    \neg\varphi\in\operatorname{Form}^{\mathrm{raw}}_{\mathcal L};
>    $$
> 3. if $\varphi,\psi\in\operatorname{Form}^{\mathrm{raw}}_{\mathcal L}$, then
>    $$
>    (\varphi\to\psi)\in\operatorname{Form}^{\mathrm{raw}}_{\mathcal L};
>    $$
> 4. if $x\in\operatorname{Var}_s$ and $\varphi\in\operatorname{Form}^{\mathrm{raw}}_{\mathcal L}$, then
>    $$
>    \forall x\,\varphi\in\operatorname{Form}^{\mathrm{raw}}_{\mathcal L};
>    $$
> 5. no object is in $\operatorname{Form}^{\mathrm{raw}}_{\mathcal L}$ except by finitely many applications of clauses 1--4.

> [!notation] Notation 4.7: Defined connectives
> Define abbreviations by
>
> $$
> \varphi\vee\psi:=((\neg\varphi)\to\psi),
> $$
>
> $$
> \varphi\wedge\psi:=\neg(\varphi\to\neg\psi),
> $$
>
> $$
> \varphi\leftrightarrow\psi:=(\varphi\to\psi)\wedge(\psi\to\varphi),
> $$
>
> and, for $x\in\operatorname{Var}_s$,
>
> $$
> \exists x\,\varphi:=\neg\forall x\,\neg\varphi.
> $$
>
> If these symbols are taken as primitive instead, the same semantic clauses below are imposed directly.

> [!theorem] Theorem 4.8: Formula induction
> Let $P\subseteq\operatorname{Form}^{\mathrm{raw}}_{\mathcal L}$. Assume:
>
> 1. $\operatorname{Atom}_{\mathcal L}\subseteq P$;
> 2. $\varphi\in P$ implies $\neg\varphi\in P$;
> 3. $\varphi,\psi\in P$ implies $(\varphi\to\psi)\in P$;
> 4. $x\in\operatorname{Var}_s$ and $\varphi\in P$ imply $\forall x\,\varphi\in P$.
>
> Then
>
> $$
> P=\operatorname{Form}^{\mathrm{raw}}_{\mathcal L}.
> $$

> [!proof-sketch] Proof Sketch 4.8
> By definition, $\operatorname{Form}^{\mathrm{raw}}_{\mathcal L}$ is the least subset of the ambient universe containing all atoms and closed under the displayed operations. The assumptions say exactly that $P$ is another such closed set.

> [!theorem] Theorem 4.9: Formula recursion
> Let $B$ be a set. Suppose given:
>
> 1. a function
>    $$
>    A:\operatorname{Atom}_{\mathcal L}\to B;
>    $$
> 2. a function
>    $$
>    N:B\to B;
>    $$
> 3. a function
>    $$
>    I:B\times B\to B;
>    $$
> 4. for every $s\in S$ and $x\in\operatorname{Var}_s$, a function
>    $$
>    Q_x:B\to B.
>    $$
>
> Then there exists a unique function
>
> $$
> F:\operatorname{Form}^{\mathrm{raw}}_{\mathcal L}\to B
> $$
>
> such that
>
> $$
> F(\alpha)=A(\alpha),
> $$
>
> $$
> F(\neg\varphi)=N(F(\varphi)),
> $$
>
> $$
> F(\varphi\to\psi)=I(F(\varphi),F(\psi)),
> $$
>
> and
>
> $$
> F(\forall x\,\varphi)=Q_x(F(\varphi)).
> $$

> [!proof-sketch] Proof Sketch 4.9
> Regard formulas as the free algebra generated by atoms under the displayed connectives and binder constructors. The stated data are exactly an algebra structure on $B$ together with an interpretation of the atomic generators.

### 4.3. Free variables and sentences

> [!definition] Definition 4.10: Free variables of an atom
> For an atom $\alpha$ and $r\in S$, define $\operatorname{FV}_r(\alpha)\subseteq\operatorname{Var}_r$ as follows:
>
> 1. if $\alpha$ is $t=_s u$, then
>    $$
>    \operatorname{FV}_r(\alpha)=\operatorname{Var}_r(t)\cup\operatorname{Var}_r(u);
>    $$
> 2. if $\alpha$ is $R(t_0,\dots,t_{n-1})$, then
>    $$
>    \operatorname{FV}_r(\alpha)=\bigcup_{i<n}\operatorname{Var}_r(t_i).
>    $$

> [!definition] Definition 4.11: Free variables of a formula
> For $\varphi\in\operatorname{Form}^{\mathrm{raw}}_{\mathcal L}$ and $r\in S$, define
>
> $$
> \operatorname{FV}_r(\varphi)\subseteq\operatorname{Var}_r
> $$
>
> by recursion:
>
> $$
> \operatorname{FV}_r(\neg\varphi)=\operatorname{FV}_r(\varphi),
> $$
>
> $$
> \operatorname{FV}_r(\varphi\to\psi)=\operatorname{FV}_r(\varphi)\cup\operatorname{FV}_r(\psi),
> $$
>
> and, if $x\in\operatorname{Var}_s$,
>
> $$
> \operatorname{FV}_r(\forall x\,\varphi)=
> \begin{cases}
> \operatorname{FV}_s(\varphi)\setminus\{x\},&r=s,\\
> \operatorname{FV}_r(\varphi),&r\neq s.
> \end{cases}
> $$
>
> The sorted family of free variables is
>
> $$
> \operatorname{FV}(\varphi)=(\operatorname{FV}_r(\varphi))_{r\in S}.
> $$

> [!proposition] Proposition 4.12: Finite support of formulas
> For every $\varphi\in\operatorname{Form}^{\mathrm{raw}}_{\mathcal L}$, the set
>
> $$
> \{(r,x):r\in S,
> \ x\in\operatorname{FV}_r(\varphi)\}
> $$
>
> is finite.

> [!proof-sketch] Proof Sketch 4.12
> Atomic formulas have finite support because they contain finitely many terms and each term has finite support. The Boolean clauses preserve finite unions. The quantifier clause removes one variable from one component and leaves all other components unchanged.

> [!definition] Definition 4.13: Sentence
> A raw formula $\sigma\in\operatorname{Form}^{\mathrm{raw}}_{\mathcal L}$ is a **sentence** if
>
> $$
> \operatorname{FV}_s(\sigma)=\varnothing
> $$
>
> for every $s\in S$. The set of $\mathcal L$-sentences is
>
> $$
> \operatorname{Sent}_{\mathcal L}:=
> \{\sigma\in\operatorname{Form}^{\mathrm{raw}}_{\mathcal L}:\forall s\in S,
> \ \operatorname{FV}_s(\sigma)=\varnothing\}.
> $$

---

## 5. Substitution, Alpha-Equivalence, and Hygiene

### 5.1. Term substitutions

> [!definition] Definition 5.1: Sorted term substitution
> A **term substitution** is an $S$-sorted map
>
> $$
> \sigma:\operatorname{Var}\to\operatorname{Term}_{\mathcal L},
> $$
>
> i.e. a family
>
> $$
> \sigma_s:\operatorname{Var}_s\to\operatorname{Term}_{\mathcal L,s}.
> $$
>
> Thus a variable of sort $s$ is replaced only by a term of sort $s$.

> [!construction] Construction 5.2: Extension of a term substitution
> For a substitution $\sigma:\operatorname{Var}\to\operatorname{Term}_{\mathcal L}$, define
>
> $$
> \widehat\sigma:\mathbf{Term}_{\mathcal L}\to\mathbf{Term}_{\mathcal L}
> $$
>
> as the unique $\Sigma_{\mathcal L}$-homomorphism satisfying
>
> $$
> \widehat\sigma\circ\eta=\sigma.
> $$
>
> Componentwise,
>
> $$
> \widehat\sigma_s(\eta_s(x))=\sigma_s(x),
> $$
>
> and
>
> $$
> \widehat\sigma_s(f(t_0,\dots,t_{n-1}))=
> f(\widehat\sigma_{s_0}(t_0),\dots,\widehat\sigma_{s_{n-1}}(t_{n-1})).
> $$

> [!definition] Definition 5.3: Identity and composition of substitutions
> The identity substitution is
>
> $$
> \operatorname{id}^{\sharp}:\operatorname{Var}\to\operatorname{Term}_{\mathcal L},
> \qquad
> \operatorname{id}^{\sharp}_s(x)=\eta_s(x).
> $$
>
> If $\sigma:\operatorname{Var}\to\operatorname{Term}_{\mathcal L}$ and $\tau:\operatorname{Var}\to\operatorname{Term}_{\mathcal L}$ are substitutions, define the Kleisli composite
>
> $$
> \tau\star\sigma:=\widehat\tau\circ\sigma.
> $$

> [!proposition] Proposition 5.4: Substitution monoid laws
> For substitutions $\rho,\tau,\sigma$, the following equations hold:
>
> $$
> \operatorname{id}^{\sharp}\star\sigma=\sigma,
> $$
>
> $$
> \sigma\star\operatorname{id}^{\sharp}=\sigma,
> $$
>
> $$
> \rho\star(\tau\star\sigma)=(\rho\star\tau)\star\sigma,
> $$
>
> and
>
> $$
> \widehat{\tau\star\sigma}=\widehat\tau\circ\widehat\sigma.
> $$

> [!proof-sketch] Proof Sketch 5.4
> Each equation follows from uniqueness of homomorphic extensions out of the free term algebra. The final identity implies associativity by evaluating both sides on variables and extending uniquely.

### 5.2. Formula substitution as a partial raw operation

> [!definition] Definition 5.5: Binder-erased substitution at a variable
> Let $x\in\operatorname{Var}_s$ and let $\sigma$ be a term substitution. Define
>
> $$
> \sigma^{\setminus x}:\operatorname{Var}\to\operatorname{Term}_{\mathcal L}
> $$
>
> by
>
> $$
> (\sigma^{\setminus x})_s(x)=\eta_s(x),
> $$
>
> $$
> (\sigma^{\setminus x})_r(y)=\sigma_r(y)
> $$
>
> for every $(r,y)\neq(s,x)$.

> [!definition] Definition 5.6: Capture obstruction for a binder
> Let $x\in\operatorname{Var}_s$, let $\psi\in\operatorname{Form}^{\mathrm{raw}}_{\mathcal L}$, and let $\sigma$ be a term substitution. Define the binder-capture obstruction
>
> $$
> \operatorname{Cap}_{x,\sigma}(\psi)
> $$
>
> by
>
> $$
> \operatorname{Cap}_{x,\sigma}(\psi)
> \Longleftrightarrow
> \exists r\in S\,\exists y\in\operatorname{FV}_r(\psi)\,
> \big(y\neq x\ \wedge\ x\in\operatorname{Var}_s(\sigma_r(y))\big).
> $$
>
> The negation
>
> $$
> \neg\operatorname{Cap}_{x,\sigma}(\psi)
> $$
>
> says that substituting below the binder $\forall x$ does not introduce a free occurrence of $x$ into the scope of that binder.

> [!definition] Definition 5.7: Admissibility of a substitution for a formula
> Define the predicate
>
> $$
> \operatorname{SubstOK}_{\sigma}(\varphi)
> $$
>
> by recursion on $\varphi$:
>
> 1. if $\varphi$ is atomic, then $\operatorname{SubstOK}_{\sigma}(\varphi)$ holds;
> 2. $\operatorname{SubstOK}_{\sigma}(\neg\varphi)$ iff $\operatorname{SubstOK}_{\sigma}(\varphi)$;
> 3. $\operatorname{SubstOK}_{\sigma}(\varphi\to\psi)$ iff $\operatorname{SubstOK}_{\sigma}(\varphi)$ and $\operatorname{SubstOK}_{\sigma}(\psi)$;
> 4. if $x\in\operatorname{Var}_s$, then
>    $$
>    \operatorname{SubstOK}_{\sigma}(\forall x\,\varphi)
>    $$
>    iff
>    $$
>    \operatorname{SubstOK}_{\sigma^{\setminus x}}(\varphi)
>    \quad\text{and}\quad
>    \neg\operatorname{Cap}_{x,\sigma}(\varphi).
>    $$

> [!construction] Construction 5.8: Guarded raw substitution in formulas
> If $\operatorname{SubstOK}_{\sigma}(\varphi)$ holds, define
>
> $$
> \varphi[\sigma]\in\operatorname{Form}^{\mathrm{raw}}_{\mathcal L}
> $$
>
> by recursion:
>
> $$
> (t=_s u)[\sigma]:=\widehat\sigma_s(t)=_s\widehat\sigma_s(u),
> $$
>
> $$
> R(t_0,\dots,t_{n-1})[\sigma]
> :=
> R(\widehat\sigma_{s_0}(t_0),\dots,\widehat\sigma_{s_{n-1}}(t_{n-1})),
> $$
>
> $$
> (\neg\varphi)[\sigma]:=\neg(\varphi[\sigma]),
> $$
>
> $$
> (\varphi\to\psi)[\sigma]:=\varphi[\sigma]\to\psi[\sigma],
> $$
>
> and
>
> $$
> (\forall x\,\varphi)[\sigma]:=\forall x\,(\varphi[\sigma^{\setminus x}]).
> $$

> [!warning] Warning 5.9: Substitution is not merely replacement
> The operation $\varphi[\sigma]$ is partial on raw formulas because binders can capture variables introduced by substituted terms. A total operation on raw formulas requires an explicit alpha-renaming convention. A total operation on alpha-equivalence classes requires proving independence of representatives.

### 5.3. Single-variable substitution and alpha-equivalence

> [!definition] Definition 5.10: Single-variable term substitution
> Let $x\in\operatorname{Var}_s$ and $t\in\operatorname{Term}_{\mathcal L,s}$. Define
>
> $$
> [t/x]:\operatorname{Var}\to\operatorname{Term}_{\mathcal L}
> $$
>
> by
>
> $$
> [t/x]_s(x)=t
> $$
>
> and
>
> $$
> [t/x]_r(y)=\eta_r(y)
> $$
>
> for every $(r,y)\neq(s,x)$.
>
> If $\operatorname{SubstOK}_{[t/x]}(\varphi)$ holds, write
>
> $$
> \varphi[t/x]:=\varphi[[t/x]].
> $$

> [!definition] Definition 5.11: Freshness for a formula
> A variable $y\in\operatorname{Var}_s$ is **fresh for** $\varphi$ if
>
> $$
> y\notin\operatorname{FV}_s(\varphi)
> $$
>
> and $y$ has no bound occurrence in $\varphi$ under the chosen raw presentation. Equivalently, $y$ does not occur in the finite variable-occurrence set of $\varphi$.

> [!definition] Definition 5.12: Alpha-renaming step
> Let $x,y\in\operatorname{Var}_s$ and let $\varphi\in\operatorname{Form}^{\mathrm{raw}}_{\mathcal L}$. If $y$ is fresh for $\varphi$, define one alpha-renaming step by
>
> $$
> \forall x\,\varphi
> \sim_1
> \forall y\,(\varphi[y/x]),
> $$
>
> where $\varphi[y/x]$ is the guarded substitution instance from Definition 5.10. The freshness assumption guarantees the guard.

> [!definition] Definition 5.13: Alpha-equivalence
> The **alpha-equivalence relation**
>
> $$
> \equiv_{\alpha}\ \subseteq\
> \operatorname{Form}^{\mathrm{raw}}_{\mathcal L}\times\operatorname{Form}^{\mathrm{raw}}_{\mathcal L}
> $$
>
> is the least equivalence relation satisfying:
>
> 1. if $\varphi\sim_1\psi$, then $\varphi\equiv_{\alpha}\psi$;
> 2. $\varphi\equiv_{\alpha}\psi$ implies $\neg\varphi\equiv_{\alpha}\neg\psi$;
> 3. $\varphi_0\equiv_{\alpha}\psi_0$ and $\varphi_1\equiv_{\alpha}\psi_1$ imply
>    $$
>    (\varphi_0\to\varphi_1)\equiv_{\alpha}(\psi_0\to\psi_1);
>    $$
> 4. if $z\in\operatorname{Var}_r$ and $\varphi\equiv_{\alpha}\psi$, then
>    $$
>    \forall z\,\varphi\equiv_{\alpha}\forall z\,\psi.
>    $$

> [!definition] Definition 5.14: Binding-aware formula set
> The **alpha-quotient formula set** is
>
> $$
> \operatorname{Form}_{\mathcal L}:=
> \operatorname{Form}^{\mathrm{raw}}_{\mathcal L}/\equiv_{\alpha}.
> $$
>
> The quotient map is
>
> $$
> q_{\alpha}:\operatorname{Form}^{\mathrm{raw}}_{\mathcal L}\to\operatorname{Form}_{\mathcal L}.
> $$
>
> A raw formula may be used as notation for its alpha-class when no ambiguity is possible.

> [!proposition] Proposition 5.15: Alpha-invariance of free variables
> If $\varphi\equiv_{\alpha}\psi$, then for every $s\in S$,
>
> $$
> \operatorname{FV}_s(\varphi)=\operatorname{FV}_s(\psi).
> $$

> [!proof-sketch] Proof Sketch 5.15
> It suffices to check one alpha-renaming step and closure under constructors. A fresh renaming changes only the name of bound occurrences introduced by the displayed binder and leaves free occurrences unchanged. The constructor clauses preserve equality of free-variable families.

> [!theorem] Theorem 5.16: Capture-avoiding substitution on alpha-classes
> Let $\sigma:\operatorname{Var}\to\operatorname{Term}_{\mathcal L}$ be a term substitution. There is a well-defined operation
>
> $$
> [-][\sigma]:\operatorname{Form}_{\mathcal L}\to\operatorname{Form}_{\mathcal L}
> $$
>
> obtained by choosing raw representatives, alpha-renaming bound variables to satisfy the guards in Definition 5.7, performing guarded raw substitution, and passing to alpha-classes.

> [!proof-sketch] Proof Sketch 5.16
> Each raw formula has finitely many variable occurrences and each substituted term used by the formula has finite support; each variable supply $\operatorname{Var}_s$ is infinite. Hence bound variables can be renamed to variables fresh for the finite obstruction set. Independence of the choices follows from the definition of $\equiv_{\alpha}$ and induction on formula structure.

---

## 6. Structures, Assignments, and Term Evaluation

### 6.1. Structures

> [!definition] Definition 6.1: Many-sorted $\mathcal L$-structure
> A **many-sorted $\mathcal L$-structure** is a tuple
>
> $$
> \mathcal M=(M,(f^{\mathcal M})_{f\in|\operatorname{Func}_{\mathcal L}|},(R^{\mathcal M})_{R\in|\operatorname{Rel}_{\mathcal L}|})
> $$
>
> where:
>
> 1. $M=(M_s)_{s\in S}$ is an $S$-sorted family of nonempty sets;
> 2. for every $f\in\operatorname{Func}_{\mathcal L,w,s}$,
>    $$
>    f^{\mathcal M}:M_w\to M_s
>    $$
>    is a function;
> 3. for every $R\in\operatorname{Rel}_{\mathcal L,w}$,
>    $$
>    R^{\mathcal M}\subseteq M_w
>    $$
>    is a relation on the corresponding sorted product.

> [!definition] Definition 6.2: Functional reduct of a structure
> The **functional reduct** of $\mathcal M$ is the $\Sigma_{\mathcal L}$-algebra
>
> $$
> \mathcal M_{\mathrm{alg}}:=(M,(f^{\mathcal M})_{f\in|\operatorname{Func}_{\mathcal L}|}).
> $$
>
> Relation interpretations are not part of $\mathcal M_{\mathrm{alg}}$.

> [!warning] Warning 6.3: Nonempty sort convention
> This note assumes
>
> $$
> M_s\neq\varnothing
> $$
>
> for every $s\in S$. Allowing empty sorts changes the validity of quantifier principles and requires restating Henkin constructions, completeness, and Löwenheim-Skolem bounds.

> [!definition] Definition 6.4: Assignment
> An **assignment in $\mathcal M$** is an $S$-sorted map
>
> $$
> a:\operatorname{Var}\to M,
> $$
>
> i.e.
>
> $$
> a_s:\operatorname{Var}_s\to M_s
> $$
>
> for every $s\in S$.

> [!definition] Definition 6.5: Assignment update
> Let $a:\operatorname{Var}\to M$, let $x\in\operatorname{Var}_s$, and let $m\in M_s$. Define
>
> $$
> a[x\mapsto m]:\operatorname{Var}\to M
> $$
>
> by
>
> $$
> a[x\mapsto m]_s(x)=m
> $$
>
> and
>
> $$
> a[x\mapsto m]_r(y)=a_r(y)
> $$
>
> for every $(r,y)\neq(s,x)$.

> [!notation] Notation 6.6: Agreement on a sorted variable family
> If $A=(A_s)_{s\in S}$ with $A_s\subseteq\operatorname{Var}_s$, write
>
> $$
> a\equiv_A b
> $$
>
> iff
>
> $$
> a_s(x)=b_s(x)
> $$
>
> for every $s\in S$ and every $x\in A_s$.

### 6.2. Term evaluation

> [!construction] Construction 6.7: Term evaluation
> Let $\mathcal M$ be an $\mathcal L$-structure and let $a:\operatorname{Var}\to M$ be an assignment. The **term evaluation homomorphism** is
>
> $$
> \operatorname{ev}^{\mathcal M}_a:\mathbf{Term}_{\mathcal L}\to\mathcal M_{\mathrm{alg}}
> $$
>
> defined as the unique $\Sigma_{\mathcal L}$-homomorphism satisfying
>
> $$
> \operatorname{ev}^{\mathcal M}_a\circ\eta=a.
> $$
>
> For $t\in\operatorname{Term}_{\mathcal L,s}$, write
>
> $$
> t^{\mathcal M}[a]:=\operatorname{ev}^{\mathcal M}_{a,s}(t)\in M_s.
> $$

> [!proposition] Proposition 6.8: Recursive clauses for term evaluation
> For $x\in\operatorname{Var}_s$,
>
> $$
> x^{\mathcal M}[a]=a_s(x).
> $$
>
> If $f\in\operatorname{Func}_{\mathcal L,w,s}$ with $w=(s_0,\dots,s_{n-1})$ and $t_i\in\operatorname{Term}_{\mathcal L,s_i}$, then
>
> $$
> f(t_0,\dots,t_{n-1})^{\mathcal M}[a]
> =
> f^{\mathcal M}(t_0^{\mathcal M}[a],\dots,t_{n-1}^{\mathcal M}[a]).
> $$

> [!proof-sketch] Proof Sketch 6.8
> These equations are the generator and homomorphism clauses for the unique extension $\operatorname{ev}^{\mathcal M}_a$.

> [!proposition] Proposition 6.9: Term dependence on occurring variables
> If $t\in\operatorname{Term}_{\mathcal L,s}$ and assignments $a,b:\operatorname{Var}\to M$ satisfy
>
> $$
> a\equiv_{\operatorname{Var}(t)}b,
> $$
>
> then
>
> $$
> t^{\mathcal M}[a]=t^{\mathcal M}[b].
> $$

> [!proof-sketch] Proof Sketch 6.9
> Use structural induction on $t$. The variable case is the agreement hypothesis. The function-symbol case follows by applying the induction hypothesis to each immediate subterm and then applying the same interpreted function.

> [!definition] Definition 6.10: Valuation pulled back by a substitution
> Let $\sigma$ be a term substitution and let $a$ be an assignment in $\mathcal M$. Define
>
> $$
> a_{\sigma}:\operatorname{Var}\to M
> $$
>
> by
>
> $$
> (a_{\sigma})_s(x)=\sigma_s(x)^{\mathcal M}[a].
> $$

> [!theorem] Theorem 6.11: Term substitution evaluation lemma
> For every term substitution $\sigma$, assignment $a$ in $\mathcal M$, sort $s\in S$, and term $t\in\operatorname{Term}_{\mathcal L,s}$,
>
> $$
> (\widehat\sigma_s(t))^{\mathcal M}[a]
> =
> t^{\mathcal M}[a_{\sigma}].
> $$

> [!proof-sketch] Proof Sketch 6.11
> Both sides define homomorphisms $\mathbf{Term}_{\mathcal L}\to\mathcal M_{\mathrm{alg}}$. On a variable $x$, the left side gives $\sigma(x)^{\mathcal M}[a]$, which is the value of $a_{\sigma}(x)$; the right side is the evaluation extension of $a_{\sigma}$. Uniqueness of homomorphic extension gives equality.

---

## 7. Satisfaction, Validity, and Semantic Consequence

### 7.1. Satisfaction relation

> [!definition] Definition 7.1: Satisfaction for atomic formulas
> Let $\mathcal M$ be an $\mathcal L$-structure and $a:\operatorname{Var}\to M$ an assignment.
>
> If $t,u\in\operatorname{Term}_{\mathcal L,s}$, define
>
> $$
> \mathcal M\models(t=_s u)[a]
> $$
>
> iff
>
> $$
> t^{\mathcal M}[a]=u^{\mathcal M}[a]
> $$
>
> in $M_s$.
>
> If $R\in\operatorname{Rel}_{\mathcal L,w}$ with $w=(s_0,\dots,s_{n-1})$, define
>
> $$
> \mathcal M\models R(t_0,\dots,t_{n-1})[a]
> $$
>
> iff
>
> $$
> (t_0^{\mathcal M}[a],\dots,t_{n-1}^{\mathcal M}[a])\in R^{\mathcal M}\subseteq M_w.
> $$

> [!definition] Definition 7.2: Satisfaction for connectives and quantifiers
> The satisfaction relation is extended to raw formulas by recursion:
>
> $$
> \mathcal M\models(\neg\varphi)[a]
> \Longleftrightarrow
> \mathcal M\not\models\varphi[a],
> $$
>
> $$
> \mathcal M\models(\varphi\to\psi)[a]
> \Longleftrightarrow
> (\mathcal M\not\models\varphi[a])\text{ or }(\mathcal M\models\psi[a]),
> $$
>
> and, for $x\in\operatorname{Var}_s$,
>
> $$
> \mathcal M\models(\forall x\,\varphi)[a]
> \Longleftrightarrow
> \forall m\in M_s,
> \ \mathcal M\models\varphi[a[x\mapsto m]].
> $$

> [!proposition] Proposition 7.3: Satisfaction is alpha-invariant
> If $\varphi\equiv_{\alpha}\psi$, then for every $\mathcal M$ and every assignment $a$,
>
> $$
> \mathcal M\models\varphi[a]
> \Longleftrightarrow
> \mathcal M\models\psi[a].
> $$
>
> Hence satisfaction descends to a relation on $\operatorname{Form}_{\mathcal L}$.

> [!proof-sketch] Proof Sketch 7.3
> It is enough to verify one fresh alpha-renaming step. If $y$ is fresh for $\varphi$, then varying $x$ in $\forall x\,\varphi$ and varying $y$ in $\forall y\,\varphi[y/x]$ range over the same carrier $M_s$, and the substitution clause for variables gives matching assignments. Closure under connectives and additional binders follows by induction.

> [!proposition] Proposition 7.4: Dependence on free variables
> Let $\varphi\in\operatorname{Form}_{\mathcal L}$ and let $a,b:\operatorname{Var}\to M$. If
>
> $$
> a\equiv_{\operatorname{FV}(\varphi)} b,
> $$
>
> then
>
> $$
> \mathcal M\models\varphi[a]
> \Longleftrightarrow
> \mathcal M\models\varphi[b].
> $$

> [!proof-sketch] Proof Sketch 7.4
> Use induction on a raw representative. Atomic cases use term dependence. Boolean cases are immediate. For $\forall x\,\psi$, update both assignments at $x$ by the same arbitrary $m\in M_s$ and apply the induction hypothesis to $\psi$.

> [!notation] Notation 7.5: Truth of a sentence
> If $\sigma\in\operatorname{Sent}_{\mathcal L}$, write
>
> $$
> \mathcal M\models\sigma
> $$
>
> iff
>
> $$
> \mathcal M\models\sigma[a]
> $$
>
> for some, equivalently every, assignment $a:\operatorname{Var}\to M$.

> [!theorem] Theorem 7.6: Formula substitution lemma
> Let $\sigma$ be a term substitution and let $\varphi\in\operatorname{Form}_{\mathcal L}$. For every $\mathcal L$-structure $\mathcal M$ and assignment $a$, if substitution is interpreted capture-avoidantly on alpha-classes, then
>
> $$
> \mathcal M\models \varphi[\sigma][a]
> \Longleftrightarrow
> \mathcal M\models \varphi[a_{\sigma}].
> $$
>
> In the raw guarded presentation, the same equivalence holds whenever $\operatorname{SubstOK}_{\sigma}(\varphi)$ holds.

> [!proof-sketch] Proof Sketch 7.6
> Atomic cases reduce to Theorem 6.11. Boolean cases follow from the recursive truth clauses. In the quantifier case, the substitution guard is exactly the condition ensuring that assignment update at the bound variable commutes with evaluating the substituted terms for all free variables not bound by that quantifier. The alpha-class version first chooses a representative for which the raw guard holds.

### 7.2. Semantic notions

> [!definition] Definition 7.7: Validity
> A formula $\varphi\in\operatorname{Form}_{\mathcal L}$ is **valid**, written
>
> $$
> \models_{\mathcal L}\varphi,
> $$
>
> iff for every $\mathcal L$-structure $\mathcal M$ and every assignment $a$ in $\mathcal M$,
>
> $$
> \mathcal M\models\varphi[a].
> $$

> [!definition] Definition 7.8: Satisfiability
> A set $\Gamma\subseteq\operatorname{Form}_{\mathcal L}$ is **satisfiable** iff there exist an $\mathcal L$-structure $\mathcal M$ and an assignment $a$ such that
>
> $$
> \forall\gamma\in\Gamma,
> \ \mathcal M\models\gamma[a].
> $$
>
> If $\Gamma\subseteq\operatorname{Sent}_{\mathcal L}$, this is equivalent to existence of $\mathcal M$ with
>
> $$
> \forall\gamma\in\Gamma,
> \ \mathcal M\models\gamma.
> $$

> [!definition] Definition 7.9: Semantic consequence for formulas
> For $\Gamma\subseteq\operatorname{Form}_{\mathcal L}$ and $\varphi\in\operatorname{Form}_{\mathcal L}$, define
>
> $$
> \Gamma\models_{\mathcal L}\varphi
> $$
>
> iff for every $\mathcal L$-structure $\mathcal M$ and every assignment $a$,
>
> $$
> \big(\forall\gamma\in\Gamma,
> \ \mathcal M\models\gamma[a]\big)
> \Longrightarrow
> \mathcal M\models\varphi[a].
> $$

> [!definition] Definition 7.10: Semantic consequence for theories
> If $T\subseteq\operatorname{Sent}_{\mathcal L}$ and $\sigma\in\operatorname{Sent}_{\mathcal L}$, write
>
> $$
> T\models_{\mathcal L}\sigma
> $$
>
> iff every $\mathcal L$-structure satisfying every sentence in $T$ satisfies $\sigma$.

> [!proposition] Proposition 7.11: Consequence and unsatisfiability
> If $T\subseteq\operatorname{Sent}_{\mathcal L}$ and $\sigma\in\operatorname{Sent}_{\mathcal L}$, then
>
> $$
> T\models_{\mathcal L}\sigma
> $$
>
> iff
>
> $$
> T\cup\{\neg\sigma\}
> $$
>
> is unsatisfiable.

> [!proof-sketch] Proof Sketch 7.11
> A model of $T\cup\{\neg\sigma\}$ is exactly a model of $T$ in which $\sigma$ is false. This is the negation of preservation of $\sigma$ across all models of $T$.

> [!definition] Definition 7.12: Theory, model class, and semantic closure
> An **$\mathcal L$-theory** is a set
>
> $$
> T\subseteq\operatorname{Sent}_{\mathcal L}.
> $$
>
> Its model class is
>
> $$
> \operatorname{Mod}_{\mathcal L}(T):=
> \{\mathcal M:\mathcal M\text{ is an }\mathcal L\text{-structure and }\forall\sigma\in T,
> \ \mathcal M\models\sigma\}.
> $$
>
> Its semantic closure is
>
> $$
> \operatorname{Cn}_{\models}(T):=
> \{\sigma\in\operatorname{Sent}_{\mathcal L}:T\models_{\mathcal L}\sigma\}.
> $$

> [!definition] Definition 7.13: Complete theory
> A satisfiable theory $T\subseteq\operatorname{Sent}_{\mathcal L}$ is **complete** iff for every sentence $\sigma\in\operatorname{Sent}_{\mathcal L}$,
>
> $$
> T\models\sigma
> \quad\text{or}\quad
> T\models\neg\sigma.
> $$

---

## 8. Substructures, Homomorphisms, Embeddings, and Generated Parts

### 8.1. Substructures

> [!definition] Definition 8.1: Substructure
> Let $\mathcal M$ and $\mathcal N$ be $\mathcal L$-structures. A **substructure relation**
>
> $$
> \mathcal M\subseteq\mathcal N
> $$
>
> means:
>
> 1. for every $s\in S$,
>    $$
>    M_s\subseteq N_s;
>    $$
> 2. for every $f\in\operatorname{Func}_{\mathcal L,w,s}$,
>    $$
>    f^{\mathcal M}=f^{\mathcal N}\restriction M_w;
>    $$
> 3. for every $R\in\operatorname{Rel}_{\mathcal L,w}$,
>    $$
>    R^{\mathcal M}=R^{\mathcal N}\cap M_w.
>    $$
>
> Clause 2 includes closure:
>
> $$
> f^{\mathcal N}[M_w]\subseteq M_s.
> $$

> [!construction] Construction 8.2: Substructure generated by a sorted set
> Let $\mathcal N$ be an $\mathcal L$-structure and let $A=(A_s)_{s\in S}$ with $A_s\subseteq N_s$. Define $B=(B_s)_{s\in S}$ to be the least sorted family such that:
>
> 1. $A_s\subseteq B_s\subseteq N_s$ for all $s$;
> 2. for every constant $c\in\operatorname{Func}_{\mathcal L,(),s}$,
>    $$
>    c^{\mathcal N}\in B_s;
>    $$
> 3. for every $f\in\operatorname{Func}_{\mathcal L,w,s}$,
>    $$
>    f^{\mathcal N}[B_w]\subseteq B_s.
>    $$
>
> The induced structure on $B$ with relations restricted from $\mathcal N$ is the **substructure generated by $A$**, denoted
>
> $$
> \langle A\rangle_{\mathcal N}.
> $$

> [!proposition] Proposition 8.3: Minimality of generated substructures
> If $\mathcal M\subseteq\mathcal N$ and $A_s\subseteq M_s$ for every $s\in S$, then
>
> $$
> \langle A\rangle_{\mathcal N}\subseteq\mathcal M.
> $$
>
> Hence $\langle A\rangle_{\mathcal N}$ is the least substructure of $\mathcal N$ containing $A$ sortwise.

> [!proof-sketch] Proof Sketch 8.3
> The carrier of any substructure containing $A$ contains all constants and is closed under all function interpretations. Therefore it contains the intersection of all such closed sorted families. Relations are restricted only after the carrier has been generated.

> [!theorem] Theorem 8.4: Term description of generated substructures
> Let $\mathcal N$ be an $\mathcal L$-structure and $A\subseteq N$ a sorted family. For each $s\in S$,
>
> $$
> |\langle A\rangle_{\mathcal N}|_s
> =
> \{t^{\mathcal N}[a]:t\in\operatorname{Term}_{\mathcal L,s},
> \ a:\operatorname{Var}\to N,
> \ \operatorname{Var}_r(t)\subseteq a_r^{-1}[A_r]\text{ for every }r\in S\}.
> $$
>
> Equivalently, $|\langle A\rangle_{\mathcal N}|_s$ consists of values of terms of sort $s$ under assignments sending all variables occurring in the term to elements of the corresponding component of $A$.

> [!proof-sketch] Proof Sketch 8.4
> The right-hand side contains $A$ by using variable terms, contains constants by using nullary symbols, and is closed under functions by the evaluation recursion. Conversely, every closed-under-functions family containing $A$ contains the value of every such term by induction on terms.

> [!warning] Warning 8.5: Relations do not generate elements
> Relation symbols constrain tuples by truth conditions. They do not add elements to generated substructures. The carrier of $\langle A\rangle_{\mathcal N}$ is generated only by $A$, constants, and function symbols.

### 8.2. Homomorphisms and embeddings

> [!definition] Definition 8.6: Homomorphism of $\mathcal L$-structures
> Let $\mathcal M$ and $\mathcal N$ be $\mathcal L$-structures. A **homomorphism**
>
> $$
> h:\mathcal M\to\mathcal N
> $$
>
> is a sorted map $h=(h_s:M_s\to N_s)_{s\in S}$ satisfying:
>
> 1. for every $f\in\operatorname{Func}_{\mathcal L,w,s}$ and $m\in M_w$,
>    $$
>    h_s(f^{\mathcal M}(m))=f^{\mathcal N}(h_w(m));
>    $$
> 2. for every $R\in\operatorname{Rel}_{\mathcal L,w}$ and $m\in M_w$,
>    $$
>    m\in R^{\mathcal M}\Longrightarrow h_w(m)\in R^{\mathcal N},
>    $$
>    where
>    $$
>    h_w(m_0,\dots,m_{n-1})=(h_{s_0}(m_0),\dots,h_{s_{n-1}}(m_{n-1})).
>    $$

> [!definition] Definition 8.7: Strong homomorphism, embedding, and isomorphism
> A homomorphism $h:\mathcal M\to\mathcal N$ is **strong** iff for every $R\in\operatorname{Rel}_{\mathcal L,w}$ and $m\in M_w$,
>
> $$
> m\in R^{\mathcal M}
> \Longleftrightarrow
> h_w(m)\in R^{\mathcal N}.
> $$
>
> It is an **embedding** iff it is strong and each component
>
> $$
> h_s:M_s\to N_s
> $$
>
> is injective. It is an **isomorphism** iff it is an embedding and each $h_s$ is bijective.

> [!proposition] Proposition 8.8: Term preservation by homomorphisms
> If $h:\mathcal M\to\mathcal N$ is a homomorphism, $a:\operatorname{Var}\to M$ is an assignment, and $t\in\operatorname{Term}_{\mathcal L,s}$, then
>
> $$
> h_s(t^{\mathcal M}[a])=t^{\mathcal N}[h\circ a].
> $$

> [!proof-sketch] Proof Sketch 8.8
> The two sides are homomorphic evaluations of the same term into $\mathcal N_{\mathrm{alg}}$ and agree on variables. Equivalently, prove the statement by structural induction on $t$.

> [!proposition] Proposition 8.9: Quantifier-free preservation
> If $h:\mathcal M\to\mathcal N$ is a homomorphism, then every positive atomic relation formula is preserved from $\mathcal M$ to $\mathcal N$. If $h$ is an embedding, then every quantifier-free formula is preserved and reflected:
>
> $$
> \mathcal M\models\varphi[a]
> \Longleftrightarrow
> \mathcal N\models\varphi[h\circ a]
> $$
>
> for every quantifier-free $\varphi$.

> [!proof-sketch] Proof Sketch 8.9
> Atomic equality follows from injectivity when reflection is required. Relation atoms use the strong preservation-reflection clause. Boolean connectives preserve equivalences by their truth clauses.

> [!definition] Definition 8.10: Elementary embedding
> An embedding $h:\mathcal M\to\mathcal N$ is **elementary**, written
>
> $$
> h:\mathcal M\preccurlyeq\mathcal N,
> $$
>
> iff for every formula $\varphi\in\operatorname{Form}_{\mathcal L}$ and assignment $a:\operatorname{Var}\to M$,
>
> $$
> \mathcal M\models\varphi[a]
> \Longleftrightarrow
> \mathcal N\models\varphi[h\circ a].
> $$
>
> If $\mathcal M\subseteq\mathcal N$ and the inclusion is elementary, write
>
> $$
> \mathcal M\preccurlyeq\mathcal N.
> $$

> [!theorem] Theorem 8.11: Many-sorted Tarski-Vaught test
> Let $\mathcal M\subseteq\mathcal N$. Then $\mathcal M\preccurlyeq\mathcal N$ iff for every $s\in S$, every formula $\varphi$ with $x\in\operatorname{Var}_s$ among its free variables, and every assignment $a:\operatorname{Var}\to M$,
>
> $$
> \mathcal N\models\exists x\,\varphi[a]
> $$
>
> implies that there exists $m\in M_s$ such that
>
> $$
> \mathcal N\models\varphi[a[x\mapsto m]].
> $$

> [!proof-sketch] Proof Sketch 8.11
> The forward direction follows from elementarity and the satisfaction clause for $\exists$. Conversely, prove preservation and reflection by induction on formulas. Boolean cases are immediate, and the displayed witness property supplies the existential step; universal formulas reduce to existential formulas by negation.

> [!warning] Warning 8.12: Substructure is not elementarity
> A substructure preserves the interpretation of function symbols and restricts relations. It need not contain witnesses for existential formulas true in a larger structure. The obstruction is sort-specific: a missing witness in one carrier $M_s$ can destroy elementarity even if all other sorts are unchanged.

---

## 9. Reducts, Expansions, Definitional Extensions, and Encodings

### 9.1. Language reducts and structure reducts

> [!definition] Definition 9.1: Same-sort language inclusion
> Let $\mathcal L\subseteq\mathcal L'$ be many-sorted signatures with the same sort set $S$. This means
>
> $$
> \operatorname{Func}_{\mathcal L,w,s}\subseteq\operatorname{Func}_{\mathcal L',w,s}
> $$
>
> for every $(w,s)$ and
>
> $$
> \operatorname{Rel}_{\mathcal L,w}\subseteq\operatorname{Rel}_{\mathcal L',w}
> $$
>
> for every $w$.
>
> Then $\mathcal L'$ is an **expansion** of $\mathcal L$, and $\mathcal L$ is a **same-sort reduct** of $\mathcal L'$.

> [!construction] Construction 9.2: Structure reduct
> If $\mathcal L\subseteq\mathcal L'$ and $\mathcal M'$ is an $\mathcal L'$-structure, the **$\mathcal L$-reduct**
>
> $$
> \mathcal M'\restriction\mathcal L
> $$
>
> has the same sorted carrier as $\mathcal M'$ and interprets only symbols belonging to $\mathcal L$.

> [!definition] Definition 9.3: Structure expansion
> Let $\mathcal L\subseteq\mathcal L'$ and let $\mathcal M$ be an $\mathcal L$-structure. An **$\mathcal L'$-expansion** of $\mathcal M$ is an $\mathcal L'$-structure $\mathcal M'$ such that
>
> $$
> \mathcal M'\restriction\mathcal L=\mathcal M.
> $$

> [!proposition] Proposition 9.4: Satisfaction is invariant under reduct for old formulas
> If $\mathcal L\subseteq\mathcal L'$, $\mathcal M'$ is an $\mathcal L'$-structure, $\varphi\in\operatorname{Form}_{\mathcal L}$, and $a$ is an assignment into the common carrier, then
>
> $$
> \mathcal M'\models\varphi[a]
> \Longleftrightarrow
> (\mathcal M'\restriction\mathcal L)\models\varphi[a].
> $$

> [!proof-sketch] Proof Sketch 9.4
> Induct on $\varphi$. Term evaluation for old terms uses only old function symbols. Atomic relation clauses use only old relation symbols. Boolean and quantifier clauses are unchanged.

### 9.2. Algebraic reducts of first-order structures

> [!definition] Definition 9.5: Algebraic reduct of a language
> The **algebraic reduct** of $\mathcal L$ is the functional many-sorted signature
>
> $$
> \Sigma_{\mathcal L}.
> $$
>
> The relation symbols and equality symbols are omitted.

> [!definition] Definition 9.6: Algebraic reduct of a structure
> For an $\mathcal L$-structure $\mathcal M$, the **algebraic reduct** is
>
> $$
> \mathcal M_{\mathrm{alg}}
> $$
>
> from Definition 6.2. It is a $\Sigma_{\mathcal L}$-algebra, not an $\mathcal L$-structure.

> [!proposition] Proposition 9.7: Exact term-layer integration
> For every assignment $a:\operatorname{Var}\to M$, term evaluation in $\mathcal M$ is exactly the homomorphic evaluation map
>
> $$
> \operatorname{ev}^{\mathcal M}_a:\mathbf{Term}_{\mathcal L}\to\mathcal M_{\mathrm{alg}}
> $$
>
> into the algebraic reduct. Relation symbols play no role in the definition of term evaluation.

> [!proof-sketch] Proof Sketch 9.7
> The recursive clauses for evaluating terms mention only variables and function symbols. The universal mapping property of the free algebra over $\Sigma_{\mathcal L}$ gives the evaluation map uniquely.

> [!warning] Warning 9.8: Algebraic reduct does not determine truth
> The algebraic reduct $\mathcal M_{\mathrm{alg}}$ determines values of terms but not truth of relation atoms. Two $\mathcal L$-structures can have the same algebraic reduct and different interpretations of a relation symbol $R$, hence different satisfaction relations.

### 9.3. Definitional expansions

> [!definition] Definition 9.9: Defining formula for a new relation symbol
> Let $\mathcal L\subseteq\mathcal L'$ and let $R\in\operatorname{Rel}_{\mathcal L',w}\setminus\operatorname{Rel}_{\mathcal L,w}$ with $w=(s_0,\dots,s_{n-1})$. A **definition of $R$ over a theory $T\subseteq\operatorname{Sent}_{\mathcal L}$** is an $\mathcal L$-formula
>
> $$
> \rho_R(x_0,\dots,x_{n-1})
> $$
>
> with $x_i\in\operatorname{Var}_{s_i}$ and
>
> $$
> \operatorname{FV}(\rho_R)\subseteq\{x_0,\dots,x_{n-1}\}.
> $$

> [!definition] Definition 9.10: Defining formula for a new function symbol
> Let $f\in\operatorname{Func}_{\mathcal L',w,s}\setminus\operatorname{Func}_{\mathcal L,w,s}$ with $w=(s_0,\dots,s_{n-1})$. A **definition of $f$ over $T$** is an $\mathcal L$-formula
>
> $$
> \rho_f(x_0,\dots,x_{n-1},y)
> $$
>
> where $x_i\in\operatorname{Var}_{s_i}$ and $y\in\operatorname{Var}_s$, such that
>
> $$
> T\models\forall x_0\cdots\forall x_{n-1}\exists! y\,\rho_f(x_0,\dots,x_{n-1},y).
> $$

> [!definition] Definition 9.11: Definitional expansion of a theory
> Let $\mathcal L\subseteq\mathcal L'$ have the same sort set. An $\mathcal L'$-theory $T'$ is a **definitional expansion** of an $\mathcal L$-theory $T$ if:
>
> 1. $T\subseteq T'$;
> 2. each new relation symbol $R$ has a defining formula $\rho_R$ and $T'$ contains
>    $$
>    \forall\bar x\,(R(\bar x)\leftrightarrow\rho_R(\bar x));
>    $$
> 3. each new function symbol $f$ has a defining formula $\rho_f$ and $T'$ contains
>    $$
>    \forall\bar x\,\rho_f(\bar x,f(\bar x));
>    $$
> 4. for every model $\mathcal M\models T$, there is a unique $\mathcal L'$-expansion $\mathcal M'\models T'$.

> [!theorem] Theorem 9.12: Conservativity of definitional expansion
> If $T'$ is a definitional expansion of $T$, then for every $\mathcal L$-sentence $\sigma$,
>
> $$
> T'\models\sigma
> \Longleftrightarrow
> T\models\sigma.
> $$

> [!proof-sketch] Proof Sketch 9.12
> Every model of $T$ has a unique expansion to a model of $T'$, and the reduct of every model of $T'$ is a model of $T$. Satisfaction of old-language sentences is invariant under reduct by Proposition 9.4.

### 9.4. One-sorted encodings

> [!construction] Construction 9.13: Guarded one-sorted encoding
> Given a many-sorted language $\mathcal L$ with sort set $S$, a guarded one-sorted encoding supplies a one-sorted language $\mathcal L^{\flat}$ containing:
>
> 1. unary predicates $P_s$ for $s\in S$;
> 2. one function symbol $f^{\flat}$ for each $f\in\operatorname{Func}_{\mathcal L,w,s}$;
> 3. one relation symbol $R^{\flat}$ for each $R\in\operatorname{Rel}_{\mathcal L,w}$;
> 4. axioms asserting that the predicates $P_s$ are inhabited and disjoint when disjointness is intended;
> 5. guard axioms forcing $f^{\flat}$ to send $P_{s_0}\times\cdots\times P_{s_{n-1}}$ into $P_s$;
> 6. translation clauses relativizing $\forall x\in\operatorname{Var}_s$ to $P_s$.

> [!warning] Warning 9.14: One-sorted encoding is not definitional identity
> The guarded encoding changes the syntax of terms and formulas. Quantifiers become relativized, sort admissibility becomes expressed by predicates, and totality of one-sorted functions outside the intended sort products requires dummy behavior or additional axioms. Therefore many-sorted logic and its one-sorted encoding are compared by an explicit translation, not by equality of languages.

---

## 10. Deductive Calculi and Schema Objects

### 10.1. Abstract formula calculus

> [!definition] Definition 10.1: Finitary rule over formulas
> A **finitary inference rule** over $\mathcal L$ is a set
>
> $$
> \rho\subseteq\coprod_{n\in\mathbb N}\operatorname{Form}_{\mathcal L}^n\times\operatorname{Form}_{\mathcal L}.
> $$
>
> An element
>
> $$
> ((\varphi_0,\dots,\varphi_{n-1}),\psi)\in\rho
> $$
>
> is displayed as
>
> $$
> \frac{\varphi_0\quad\cdots\quad\varphi_{n-1}}{\psi}.
> $$

> [!definition] Definition 10.2: Hilbert-style calculus datum
> A **Hilbert-style calculus datum** for $\mathcal L$ is a pair
>
> $$
> \mathsf C=(\operatorname{Ax}_{\mathsf C},\operatorname{Rule}_{\mathsf C})
> $$
>
> where
>
> $$
> \operatorname{Ax}_{\mathsf C}\subseteq\operatorname{Form}_{\mathcal L}
> $$
>
> and
>
> $$
> \operatorname{Rule}_{\mathsf C}
> $$
>
> is a set of finitary inference rules over $\mathcal L$.

> [!definition] Definition 10.3: Derivation from assumptions
> Let $\mathsf C$ be a calculus datum and $\Gamma\subseteq\operatorname{Form}_{\mathcal L}$. A **$\mathsf C$-derivation of $\varphi$ from $\Gamma$** is a finite sequence
>
> $$
> (\delta_0,\dots,\delta_{m-1})\in\operatorname{Form}_{\mathcal L}^m
> $$
>
> such that $\delta_{m-1}=\varphi$ and for every $i<m$, at least one of the following holds:
>
> 1. $\delta_i\in\Gamma$;
> 2. $\delta_i\in\operatorname{Ax}_{\mathsf C}$;
> 3. there exist $\rho\in\operatorname{Rule}_{\mathsf C}$, indices $j_0,\dots,j_{n-1}<i$, and
>    $$
>    ((\delta_{j_0},\dots,\delta_{j_{n-1}}),\delta_i)\in\rho.
>    $$
>
> Write
>
> $$
> \Gamma\vdash_{\mathsf C}\varphi
> $$
>
> iff such a derivation exists.

> [!proposition] Proposition 10.4: Structural properties of derivability
> For any calculus datum $\mathsf C$, the relation $\vdash_{\mathsf C}$ satisfies:
>
> 1. reflexivity:
>    $$
>    \varphi\in\Gamma\Longrightarrow\Gamma\vdash_{\mathsf C}\varphi;
>    $$
> 2. weakening:
>    $$
>    \Gamma\subseteq\Delta\text{ and }\Gamma\vdash_{\mathsf C}\varphi
>    \Longrightarrow
>    \Delta\vdash_{\mathsf C}\varphi;
>    $$
> 3. finitarity:
>    $$
>    \Gamma\vdash_{\mathsf C}\varphi
>    \Longrightarrow
>    \exists\Gamma_0\subseteq\Gamma\text{ finite with }\Gamma_0\vdash_{\mathsf C}\varphi.
>    $$

> [!proof-sketch] Proof Sketch 10.4
> Reflexivity is witnessed by the one-term derivation. Weakening preserves every derivation line. Finitarity uses only the finitely many assumption lines appearing in the finite derivation sequence.

### 10.2. Schema records

> [!definition] Definition 10.5: Formula schema record
> A **formula schema record** over $\mathcal L$ is a tuple
>
> $$
> \mathfrak S=(P,D,I)
> $$
>
> where:
>
> 1. $P$ is a parameter set;
> 2. $D\subseteq P$ is the side-condition domain;
> 3. $I:D\to\operatorname{Form}_{\mathcal L}$ is an instance map.
>
> Its set of instances is
>
> $$
> \operatorname{Inst}(\mathfrak S):=I[D]
> \subseteq\operatorname{Form}_{\mathcal L}.
> $$

> [!definition] Definition 10.6: Sound schema record
> A schema record $\mathfrak S=(P,D,I)$ is **semantically sound** iff
>
> $$
> \forall d\in D,
> \ \models_{\mathcal L} I(d).
> $$
>
> It is **theory-sound over $T$** iff
>
> $$
> \forall d\in D,
> \ T\models_{\mathcal L} I(d).
> $$

> [!example] Example 10.7: Universal instantiation schema
> Let $P$ be the set of triples
>
> $$
> (s,x,t,\varphi)
> $$
>
> with $s\in S$, $x\in\operatorname{Var}_s$, $t\in\operatorname{Term}_{\mathcal L,s}$, and $\varphi\in\operatorname{Form}_{\mathcal L}$. Let $D\subseteq P$ consist of triples for which $t$ is free for $x$ in $\varphi$, equivalently the substitution $[t/x]$ is admissible after alpha-renaming. Define
>
> $$
> I(s,x,t,\varphi):=(\forall x\,\varphi)\to\varphi[t/x].
> $$
>
> Then $\mathfrak S_{\forall\operatorname{E}}=(P,D,I)$ is semantically sound.

> [!proof-sketch] Proof Sketch 10.7
> If $\mathcal M\models\forall x\,\varphi[a]$, then $\mathcal M\models\varphi[a[x\mapsto t^{\mathcal M}[a]]]$. The substitution lemma identifies this with satisfaction of $\varphi[t/x]$ under $a$.

> [!example] Example 10.8: Propositional tautology schema
> Let $H_n=\{0,\dots,n-1\}$ be a finite set of propositional holes and let $\mathbf{Fm}(H_n)$ be the free propositional formula algebra on $H_n$. Let $D_n\subseteq\mathbf{Fm}(H_n)$ be the set of tautologies. For each $C\in D_n$ and tuple $(\varphi_0,\dots,\varphi_{n-1})\in\operatorname{Form}_{\mathcal L}^n$, define
>
> $$
> I(C,\varphi_0,\dots,\varphi_{n-1})=C[\varphi_0,
> \dots,\varphi_{n-1}].
> $$
>
> The resulting schema record is semantically sound.

> [!proof-sketch] Proof Sketch 10.8
> For each structure and assignment, the truth values of $\varphi_i$ determine a truth assignment on $H_n$. Since $C$ is tautological, its Boolean evaluation is true for that assignment.

### 10.3. Soundness and completeness as properties of a calculus

> [!definition] Definition 10.9: Sound calculus
> A calculus datum $\mathsf C$ is **sound for many-sorted first-order semantics** iff for every $\Gamma\subseteq\operatorname{Form}_{\mathcal L}$ and $\varphi\in\operatorname{Form}_{\mathcal L}$,
>
> $$
> \Gamma\vdash_{\mathsf C}\varphi
> \Longrightarrow
> \Gamma\models_{\mathcal L}\varphi.
> $$

> [!definition] Definition 10.10: Complete calculus
> A calculus datum $\mathsf C$ is **complete for many-sorted first-order semantics** iff for every $\Gamma\subseteq\operatorname{Form}_{\mathcal L}$ and $\varphi\in\operatorname{Form}_{\mathcal L}$,
>
> $$
> \Gamma\models_{\mathcal L}\varphi
> \Longrightarrow
> \Gamma\vdash_{\mathsf C}\varphi.
> $$

> [!theorem] Theorem 10.11: Rule-by-rule soundness criterion
> Let $\mathsf C=(\operatorname{Ax}_{\mathsf C},\operatorname{Rule}_{\mathsf C})$. Assume:
>
> 1. every axiom is valid:
>    $$
>    \operatorname{Ax}_{\mathsf C}\subseteq\{\varphi:\models\varphi\};
>    $$
> 2. every rule $\rho\in\operatorname{Rule}_{\mathsf C}$ is truth-preserving: whenever
>    $$
>    ((\varphi_0,\dots,\varphi_{n-1}),\psi)\in\rho,
>    $$
>    then
>    $$
>    \{\varphi_0,\dots,\varphi_{n-1}\}\models\psi.
>    $$
>
> Then $\mathsf C$ is sound.

> [!proof-sketch] Proof Sketch 10.11
> Induct on derivation length. Assumption lines are true under any assignment satisfying $\Gamma$; axiom lines are valid; rule lines are true because their earlier premise lines are true and the rule is truth-preserving.

> [!warning] Warning 10.12: Eigenvariable conditions are rule data
> A quantifier rule containing a freshness or eigenvariable condition is a different mathematical rule from the same displayed fraction without that condition. Omitting the side condition changes the relation $\rho\subseteq\coprod_n\operatorname{Form}^n\times\operatorname{Form}$ and can destroy soundness.

---

## 11. Henkin Construction and Completeness

### 11.1. Consistency and Henkin data

> [!definition] Definition 11.1: Syntactic consistency
> Let $\mathsf C$ be a calculus for $\mathcal L$. A theory $T\subseteq\operatorname{Sent}_{\mathcal L}$ is **$\mathsf C$-consistent** iff there is no sentence $\sigma\in\operatorname{Sent}_{\mathcal L}$ such that
>
> $$
> T\vdash_{\mathsf C}\sigma
> \quad\text{and}\quad
> T\vdash_{\mathsf C}\neg\sigma.
> $$
>
> For explosive classical calculi this is equivalent to absence of a derivation of every sentence.

> [!definition] Definition 11.2: Maximal consistent theory
> A $\mathsf C$-consistent theory $T$ is **maximal consistent** iff for every sentence $\sigma\in\operatorname{Sent}_{\mathcal L}$,
>
> $$
> \sigma\in T
> \quad\text{or}\quad
> \neg\sigma\in T,
> $$
>
> and no proper extension of $T$ in $\operatorname{Sent}_{\mathcal L}$ is $\mathsf C$-consistent.

> [!definition] Definition 11.3: Henkin witness property
> A theory $T\subseteq\operatorname{Sent}_{\mathcal L}$ has the **many-sorted Henkin witness property** iff for every sort $s\in S$ and every formula $\varphi$ with
>
> $$
> \operatorname{FV}(\exists x\,\varphi)=\varnothing
> $$
>
> for $x\in\operatorname{Var}_s$, there exists a closed term
>
> $$
> c_{\varphi,x}\in\operatorname{CTerm}_{\mathcal L,s}
> $$
>
> such that
>
> $$
> T\vdash_{\mathsf C}(\exists x\,\varphi)\to\varphi[c_{\varphi,x}/x].
> $$

> [!construction] Construction 11.4: Henkin expansion
> Given $\mathcal L$ and $T\subseteq\operatorname{Sent}_{\mathcal L}$, form an expansion $\mathcal L^H$ by adding:
>
> 1. for every $s\in S$, at least one new constant
>    $$
>    d_s:()\to s;
>    $$
> 2. for every formula $\varphi$ and variable $x\in\operatorname{Var}_s$ for which $\exists x\,\varphi$ is a sentence after parameters are fixed, a new constant
>    $$
>    c_{\varphi,x}:()\to s.
>    $$
>
> Add the Henkin sentence
>
> $$
> (\exists x\,\varphi)\to\varphi[c_{\varphi,x}/x]
> $$
>
> for each such pair $(\varphi,x)$.

> [!warning] Warning 11.5: Witness constants are symbols
> A Henkin constant $c_{\varphi,x}$ is an added nullary function symbol of sort $s$. It is not an element of any structure until a structure interpreting the expanded language is constructed.

### 11.2. Term model construction

> [!definition] Definition 11.6: Equality congruence induced by a theory
> Let $T$ be a theory in a language with equality and let $\mathsf C$ include equality rules. For closed terms $t,u\in\operatorname{CTerm}_{\mathcal L,s}$ define
>
> $$
> t\equiv_{T,s}u
> \Longleftrightarrow
> T\vdash_{\mathsf C} t=_s u.
> $$
>
> The sorted family
>
> $$
> \equiv_T=(\equiv_{T,s})_{s\in S}
> $$
>
> is an equivalence relation on the sorted closed-term family when $T$ is maximal consistent and the equality rules include reflexivity, symmetry, transitivity, and substitution of identicals.

> [!proposition] Proposition 11.7: Congruence and relation compatibility of $\equiv_T$
> Under the equality rules, $\equiv_T$ satisfies:
>
> 1. if $f\in\operatorname{Func}_{\mathcal L,w,s}$, $t_i,u_i\in\operatorname{CTerm}_{\mathcal L,s_i}$, and $t_i\equiv_{T,s_i}u_i$ for all $i<n$, then
>    $$
>    f(t_0,\dots,t_{n-1})\equiv_{T,s}f(u_0,\dots,u_{n-1});
>    $$
> 2. if $R\in\operatorname{Rel}_{\mathcal L,w}$ and $t_i\equiv_{T,s_i}u_i$ for all $i<n$, then
>    $$
>    R(t_0,\dots,t_{n-1})\in T
>    \Longleftrightarrow
>    R(u_0,\dots,u_{n-1})\in T.
>    $$

> [!proof-sketch] Proof Sketch 11.7
> Function compatibility follows by repeated application of substitution of identicals to the equality formula comparing the two function terms. Relation compatibility follows by substituting equals into atomic relation formulas and using maximal consistency to convert provable equivalence into membership agreement.

> [!construction] Construction 11.8: Many-sorted Henkin term model
> Let $T$ be a maximal consistent Henkin theory in $\mathcal L$. Define an $\mathcal L$-structure
>
> $$
> \mathcal H_T
> $$
>
> as follows.
>
> For each $s\in S$, set
>
> $$
> H_{T,s}:=\operatorname{CTerm}_{\mathcal L,s}/\equiv_{T,s}.
> $$
>
> For $f\in\operatorname{Func}_{\mathcal L,w,s}$, define
>
> $$
> f^{\mathcal H_T}([t_0],\dots,[t_{n-1}])
> :=
> [f(t_0,\dots,t_{n-1})].
> $$
>
> For $R\in\operatorname{Rel}_{\mathcal L,w}$, define
>
> $$
> ([t_0],\dots,[t_{n-1}])\in R^{\mathcal H_T}
> \Longleftrightarrow
> R(t_0,\dots,t_{n-1})\in T.
> $$

> [!proposition] Proposition 11.9: Well-definedness of the term model
> The structure $\mathcal H_T$ is well-defined. Each carrier $H_{T,s}$ is nonempty, every function interpretation is independent of representatives, and every relation interpretation is independent of representatives.

> [!proof-sketch] Proof Sketch 11.9
> Nonemptiness follows from the added constants $d_s$. Function and relation well-definedness are exactly the compatibility clauses of Proposition 11.7.

> [!definition] Definition 11.10: Canonical assignment in a term model
> If the language contains constants naming representatives of variables, or if one works with formulas whose free variables are assigned closed terms, a canonical assignment sends each variable $x\in\operatorname{Var}_s$ to a class
>
> $$
> [t_x]\in H_{T,s}.
> $$
>
> For the truth lemma for sentences, no assignment choice is needed.

> [!theorem] Theorem 11.11: Truth lemma for Henkin term models
> Let $T$ be a maximal consistent Henkin theory and let $\mathcal H_T$ be its term model. For every sentence $\sigma\in\operatorname{Sent}_{\mathcal L}$,
>
> $$
> \mathcal H_T\models\sigma
> \Longleftrightarrow
> \sigma\in T.
> $$

> [!proof-sketch] Proof Sketch 11.11
> Prove the stronger assignment form for formulas with parameters represented by closed terms. Atomic equality is the definition of $\equiv_T$; atomic relations are interpreted by membership in $T$. Boolean cases use maximal consistency. The existential case uses the Henkin witness axiom to pass from $\exists x\,\varphi\in T$ to a witnessing closed term and conversely uses existential introduction.

### 11.3. Completeness

> [!theorem] Theorem 11.12: Model existence theorem
> Let $\mathsf C$ be a sound classical many-sorted first-order calculus with equality and Henkin-complete axiom/rule treatment. If
>
> $$
> T\subseteq\operatorname{Sent}_{\mathcal L}
> $$
>
> is $\mathsf C$-consistent, then $T$ has an $\mathcal L$-model.

> [!proof-sketch] Proof Sketch 11.12
> Extend $\mathcal L$ to a Henkin language, add Henkin axioms while preserving consistency, and extend the resulting theory to a maximal consistent Henkin theory $T^*$. Build $\mathcal H_{T^*}$. By the truth lemma, $\mathcal H_{T^*}\models T^*$. The reduct $\mathcal H_{T^*}\restriction\mathcal L$ models $T$.

> [!theorem] Theorem 11.13: Gödel completeness for many-sorted first-order logic
> For a sound and complete classical many-sorted first-order calculus $\mathsf C$, for every $T\subseteq\operatorname{Sent}_{\mathcal L}$ and $\sigma\in\operatorname{Sent}_{\mathcal L}$,
>
> $$
> T\models_{\mathcal L}\sigma
> \Longleftrightarrow
> T\vdash_{\mathsf C}\sigma.
> $$

> [!proof-sketch] Proof Sketch 11.13
> Soundness gives the forward preservation from derivability to semantic consequence. For the converse, if $T\nvdash\sigma$, then $T\cup\{\neg\sigma\}$ is consistent. By model existence it has a model, which is a model of $T$ falsifying $\sigma$.

> [!corollary] Corollary 11.14: Satisfiability equals consistency
> Under the hypotheses of Theorem 11.13, a theory $T\subseteq\operatorname{Sent}_{\mathcal L}$ is satisfiable iff it is $\mathsf C$-consistent.

> [!proof-sketch] Proof Sketch 11.14
> If $T$ has a model, soundness excludes derivations of contradiction. If $T$ is consistent, the model existence theorem supplies a model.

> [!warning] Warning 11.15: Completeness depends on nonempty sorts and equality rules
> The term-model proof above uses nonempty carriers for every sort, equality congruence rules, and Henkin constants of the correct sorts. Removing or changing any of these data changes the theorem statement.

---

## 12. Compactness, Löwenheim-Skolem, and Diagrams

### 12.1. Compactness

> [!definition] Definition 12.1: Finite satisfiability
> A theory $T\subseteq\operatorname{Sent}_{\mathcal L}$ is **finitely satisfiable** iff for every finite subset
>
> $$
> T_0\subseteq T,
> $$
>
> there exists an $\mathcal L$-structure $\mathcal M$ such that
>
> $$
> \mathcal M\models T_0.
> $$

> [!theorem] Theorem 12.2: Compactness theorem
> A theory $T\subseteq\operatorname{Sent}_{\mathcal L}$ is satisfiable iff it is finitely satisfiable.

> [!proof-sketch] Proof Sketch 12.2
> The forward direction is immediate. For the reverse direction, finite satisfiability implies syntactic consistency by soundness and finitarity of derivations. Completeness then gives a model.

> [!corollary] Corollary 12.3: Compactness for semantic consequence
> For $T\subseteq\operatorname{Sent}_{\mathcal L}$ and $\sigma\in\operatorname{Sent}_{\mathcal L}$,
>
> $$
> T\models\sigma
> $$
>
> iff there exists a finite $T_0\subseteq T$ such that
>
> $$
> T_0\models\sigma.
> $$

> [!proof-sketch] Proof Sketch 12.3
> Apply compactness to $T\cup\{\neg\sigma\}$ and use Proposition 7.11.

> [!warning] Warning 12.4: Compactness is many-sorted without finiteness of $S$
> Compactness does not require the sort set $S$ to be finite. Cardinal estimates and effective enumerability statements do depend on the size and coding of $S$ and of the symbol families.

### 12.2. Löwenheim-Skolem

> [!definition] Definition 12.5: Cardinality of a many-sorted language
> Define
>
> $$
> |\mathcal L|:=
> \max\left(\aleph_0,
> |S|,
> \left|\coprod_{(w,s)}\operatorname{Func}_{\mathcal L,w,s}\right|,
> \left|\coprod_w\operatorname{Rel}_{\mathcal L,w}\right|
> \right).
> $$

> [!definition] Definition 12.6: Cardinality of a sorted subset
> If $A=(A_s)_{s\in S}$ with $A_s\subseteq M_s$, define
>
> $$
> |A|:=\left|\coprod_{s\in S}A_s\right|.
> $$
>
> For a structure $\mathcal M$, define
>
> $$
> |M|:=\left|\coprod_{s\in S}M_s\right|.
> $$

> [!theorem] Theorem 12.7: Downward Löwenheim-Skolem theorem
> Let $\mathcal N$ be an infinite $\mathcal L$-structure and let $A=(A_s)_{s\in S}$ with $A_s\subseteq N_s$. There exists an elementary substructure
>
> $$
> \mathcal M\preccurlyeq\mathcal N
> $$
>
> such that $A_s\subseteq M_s$ for all $s\in S$ and
>
> $$
> |M|\leq\max(|A|,|\mathcal L|).
> $$

> [!proof-sketch] Proof Sketch 12.7
> Add one chosen element of each sort to $A$ to preserve nonempty carriers. Close under function symbols and under Skolem choices for existential formulas with parameters from the current set. Iterate for $\omega$ stages. The cardinal bound is preserved because at each stage only at most $|\mathcal L|$ many definable witnesses over the current set are added. The Tarski-Vaught test gives elementarity.

> [!theorem] Theorem 12.8: Upward Löwenheim-Skolem theorem
> Let $\mathcal M$ be an infinite $\mathcal L$-structure and let $\kappa$ be a cardinal with
>
> $$
> \kappa\geq\max(|M|,|\mathcal L|).
> $$
>
> Then there exists an elementary extension
>
> $$
> \mathcal N\succcurlyeq\mathcal M
> $$
>
> such that
>
> $$
> |N|=\kappa.
> $$

> [!proof-sketch] Proof Sketch 12.8
> Add new constants of specified sorts in total cardinality $\kappa$, add sentences requiring many of them to be distinct within selected nonempty sorts or across tagged carrier components as appropriate, and apply compactness to obtain an elementary extension. Use downward Löwenheim-Skolem to reduce to size exactly $\kappa$.

### 12.3. Diagrams

> [!construction] Construction 12.9: Constant expansion by elements
> For an $\mathcal L$-structure $\mathcal M$, define $\mathcal L(M)$ by adding for each $s\in S$ and each $m\in M_s$ a new constant symbol
>
> $$
> \bar m:()\to s.
> $$
>
> The canonical expansion of $\mathcal M$ to $\mathcal L(M)$ interprets $\bar m$ as $m$.

> [!definition] Definition 12.10: Atomic diagram
> The **atomic diagram** of $\mathcal M$ is the set of all atomic and negated atomic $\mathcal L(M)$-sentences true in the canonical expansion of $\mathcal M$.

> [!definition] Definition 12.11: Elementary diagram
> The **elementary diagram** of $\mathcal M$ is
>
> $$
> \operatorname{Diag}_{\mathrm{el}}(\mathcal M):=
> \{\sigma\in\operatorname{Sent}_{\mathcal L(M)}:\mathcal M\models\sigma\}
> $$
>
> in the canonical expansion.

> [!proposition] Proposition 12.12: Diagram tests
> Let $\mathcal M$ and $\mathcal N$ be $\mathcal L$-structures. An expansion of $\mathcal N$ to $\mathcal L(M)$ satisfying the atomic diagram of $\mathcal M$ induces an embedding
>
> $$
> \mathcal M\hookrightarrow\mathcal N.
> $$
>
> An expansion satisfying the elementary diagram induces an elementary embedding
>
> $$
> \mathcal M\preccurlyeq\mathcal N.
> $$

> [!proof-sketch] Proof Sketch 12.12
> Interpret the map by $m\mapsto\bar m^{\mathcal N}$. Atomic diagram sentences ensure preservation and reflection of functions, equality, and relations. Elementary diagram sentences ensure preservation of all formulas with parameters.

---

## 13. Quotients, Congruences, and Equality-Compatible Collapse

### 13.1. Congruences on structures

> [!definition] Definition 13.1: Sorted equivalence relation
> Let $M=(M_s)_{s\in S}$ be an $S$-sorted family. A **sorted equivalence relation** on $M$ is a family
>
> $$
> \theta=(\theta_s)_{s\in S}
> $$
>
> where each
>
> $$
> \theta_s\subseteq M_s\times M_s
> $$
>
> is an equivalence relation.

> [!definition] Definition 13.2: Function congruence
> Let $\mathcal M$ be an $\mathcal L$-structure. A sorted equivalence relation $\theta$ on $M$ is a **function congruence** iff for every $f\in\operatorname{Func}_{\mathcal L,w,s}$ with $w=(s_0,\dots,s_{n-1})$,
>
> $$
> a_i\ \theta_{s_i}\ b_i\text{ for all }i<n
> $$
>
> implies
>
> $$
> f^{\mathcal M}(a_0,\dots,a_{n-1})\ \theta_s\ f^{\mathcal M}(b_0,\dots,b_{n-1}).
> $$

> [!definition] Definition 13.3: Relation-compatible congruence
> A function congruence $\theta$ on $\mathcal M$ is **relation-compatible** iff for every $R\in\operatorname{Rel}_{\mathcal L,w}$ with $w=(s_0,\dots,s_{n-1})$,
>
> $$
> a_i\ \theta_{s_i}\ b_i\text{ for all }i<n
> $$
>
> implies
>
> $$
> (a_0,\dots,a_{n-1})\in R^{\mathcal M}
> \Longleftrightarrow
> (b_0,\dots,b_{n-1})\in R^{\mathcal M}.
> $$

> [!construction] Construction 13.4: Quotient structure
> If $\theta$ is relation-compatible on $\mathcal M$, define the quotient $\mathcal L$-structure
>
> $$
> \mathcal M/\theta
> $$
>
> by carriers
>
> $$
> (M/\theta)_s:=M_s/\theta_s,
> $$
>
> functions
>
> $$
> f^{\mathcal M/\theta}([a_0],\dots,[a_{n-1}])
> :=
> [f^{\mathcal M}(a_0,\dots,a_{n-1})],
> $$
>
> and relations
>
> $$
> ([a_0],\dots,[a_{n-1}])\in R^{\mathcal M/\theta}
> \Longleftrightarrow
> (a_0,\dots,a_{n-1})\in R^{\mathcal M}.
> $$

> [!proposition] Proposition 13.5: Well-definedness criterion for quotients
> Construction 13.4 is well-defined iff $\theta$ is both a function congruence and relation-compatible.

> [!proof-sketch] Proof Sketch 13.5
> Function well-definedness is exactly compatibility with function symbols. Relation well-definedness is exactly invariance of relation truth under replacement of entries by equivalent entries. These conditions are also necessary by considering representatives of quotient classes.

> [!warning] Warning 13.6: Algebraic congruence is insufficient for relational quotients
> A congruence on $\mathcal M_{\mathrm{alg}}$ need not respect relation symbols. Quotienting an $\mathcal L$-structure requires relation compatibility in addition to function compatibility.

### 13.2. Kernels

> [!definition] Definition 13.7: Kernel of a homomorphism
> Let $h:\mathcal M\to\mathcal N$ be a homomorphism whose relation preservation is forward. Define the sorted kernel
>
> $$
> \ker(h)_s:=\{(a,b)\in M_s^2:h_s(a)=h_s(b)\}.
> $$
>
> Then $\ker(h)$ is a function congruence on $\mathcal M$.

> [!proposition] Proposition 13.8: Kernel relation compatibility for strong homomorphisms
> If $h:\mathcal M\to\mathcal N$ is a strong homomorphism, then $\ker(h)$ is relation-compatible.

> [!proof-sketch] Proof Sketch 13.8
> If $a_i$ and $b_i$ have equal $h$-images, then $h_w(a)=h_w(b)$. Strong preservation-reflection gives $a\in R^{\mathcal M}$ iff $h_w(a)\in R^{\mathcal N}$ iff $h_w(b)\in R^{\mathcal N}$ iff $b\in R^{\mathcal M}$.

> [!theorem] Theorem 13.9: First isomorphism theorem for strong homomorphisms
> Let $h:\mathcal M\to\mathcal N$ be a strong homomorphism. Let $\operatorname{im}(h)$ be the sorted image equipped with induced functions and relations from $\mathcal N$. Then there is a unique isomorphism
>
> $$
> \mathcal M/\ker(h)\cong\operatorname{im}(h)
> $$
>
> sending
>
> $$
> [a]_{\ker(h)_s}\mapsto h_s(a)
> $$
>
> for every $s\in S$.

> [!proof-sketch] Proof Sketch 13.9
> The displayed map is well-defined exactly by definition of the kernel, bijective onto the image, and preserves functions by homomorphicity. Relation reflection on the image uses strongness.

---

## 14. Presentation-Neutral Syntax Transfer

### 14.1. Presentations of terms and formulas

> [!definition] Definition 14.1: Presentation of the term algebra
> A **presentation of $\mathcal L$-terms** is a $\Sigma_{\mathcal L}$-algebra $\mathbf P$ together with an isomorphism
>
> $$
> r:\mathbf P\cong\mathbf{Term}_{\mathcal L}.
> $$
>
> The carrier $P_s$ may consist of strings, trees, tuples, codes, or another concrete object, but none of those choices is part of the abstract term theory.

> [!definition] Definition 14.2: Presentation of raw formulas
> A **presentation of raw formulas** is an algebra $\mathbf Q$ for the raw formula constructor signature together with an isomorphism
>
> $$
> q:\mathbf Q\cong\operatorname{Form}^{\mathrm{raw}}_{\mathcal L}
> $$
>
> respecting atoms, Boolean constructors, and binder constructors.

> [!theorem] Theorem 14.3: Transfer across presentations
> Let $r:\mathbf P\cong\mathbf{Term}_{\mathcal L}$ be a term presentation. Every operation, relation, predicate, or construction $F$ on $\mathbf{Term}_{\mathcal L}$ transports to $\mathbf P$ by conjugation through $r$ whenever its domain and codomain are functorially built from the term carriers.
>
> For example, an operation
>
> $$
> F:\operatorname{Term}_{\mathcal L,w}\to\operatorname{Term}_{\mathcal L,s}
> $$
>
> transports to
>
> $$
> F^P:=r_s^{-1}\circ F\circ r_w:P_w\to P_s.
> $$

> [!proof-sketch] Proof Sketch 14.3
> Since $r$ is a componentwise bijective homomorphism with inverse homomorphism, conjugation preserves equations, domains, codomains, compatibility, and universal properties. All transported operations are uniquely determined by commutation with $r$.

> [!warning] Warning 14.4: Representation-dependent algorithms are extra structure
> A parser, printer, address system, or tree traversal is an operation on a chosen presentation. It becomes an operation on abstract syntax only after a transfer map is specified and the result is shown independent of representational choices relevant to the construction.

### 14.2. Contexts and term operations

> [!definition] Definition 14.5: Term context profile
> Let $w=(s_0,\dots,s_{n-1})\in S^n$ and $s\in S$. A **term context of profile $w\Rightarrow s$** is an element
>
> $$
> C\in\operatorname{Term}_{\mathcal L(X)}{}_s
> $$
>
> where $X$ is an auxiliary sorted hole family with distinguished variables
>
> $$
> \Box_i\in X_{s_i}
> $$
>
> for $i<n$, and all non-hole variables are parameters explicitly listed as part of the context datum.

> [!construction] Construction 14.6: Filling a term context
> If $C$ has hole profile $w=(s_0,\dots,s_{n-1})$ and $t_i\in\operatorname{Term}_{\mathcal L,s_i}$, define
>
> $$
> C[t_0,\dots,t_{n-1}]
> $$
>
> as the value of the unique substitution sending
>
> $$
> \Box_i\mapsto t_i
> $$
>
> and fixing all parameter variables.

> [!proposition] Proposition 14.7: Sort-correct filling
> If $C$ has profile $w\Rightarrow s$ and $t_i\in\operatorname{Term}_{\mathcal L,s_i}$ for all $i<n$, then
>
> $$
> C[t_0,\dots,t_{n-1}]\in\operatorname{Term}_{\mathcal L,s}.
> $$

> [!proof-sketch] Proof Sketch 14.7
> Filling is a sorted term substitution. The substitution extension is a homomorphism of the free sorted term algebra, hence its $s$-component lands in terms of sort $s$.

> [!definition] Definition 14.8: Term operation induced by a context
> A context $C:w\Rightarrow s$ induces a function
>
> $$
> C^{\sharp}:\operatorname{Term}_{\mathcal L,w}\to\operatorname{Term}_{\mathcal L,s}
> $$
>
> by
>
> $$
> C^{\sharp}(t_0,\dots,t_{n-1})=C[t_0,\dots,t_{n-1}].
> $$
>
> Such operations are the syntactic polynomial operations of the term algebra.

> [!remark] Remark 14.9: Contexts are fixed-shape operations
> A context operation is determined by one fixed term or formula with holes. A recursive transformation such as normalization, prenexing, or substitution over arbitrary input syntax is not a context unless it is represented by one fixed finite expression with holes.

### 14.3. Propositional skeleton inside first-order logic

> [!definition] Definition 14.10: Propositional skeleton instantiation
> Let $P$ be a set of propositional parameters and let
>
> $$
> \nu:P\to\operatorname{Form}_{\mathcal L}
> $$
>
> be a map. The induced homomorphism
>
> $$
> \widehat\nu:\mathbf{Fm}(P)\to\operatorname{Form}_{\mathcal L}
> $$
>
> sends propositional formulas to $\mathcal L$-formulas by replacing each parameter $p$ with $\nu(p)$ and interpreting propositional connectives by the corresponding logical connectives.

> [!theorem] Theorem 14.11: Tautological instances are valid
> If $C\in\mathbf{Fm}(P)$ is a propositional tautology, then for every $\nu:P\to\operatorname{Form}_{\mathcal L}$,
>
> $$
> \models_{\mathcal L}\widehat\nu(C).
> $$

> [!proof-sketch] Proof Sketch 14.11
> Fix $\mathcal M$ and $a$. The map $p\mapsto 1$ iff $\mathcal M\models\nu(p)[a]$ is a truth assignment on $P$. Since $C$ is tautological, its Boolean value is true. The recursive satisfaction clauses match the Boolean evaluation of the propositional skeleton.

---


## 15. Logical Axioms as Mathematical Schema Records

### 15.1. Generalization wrapper

> [!definition] Definition 15.1: Universal closure of a formula
> Let
>
> $$
> \vec x=(x_0,\dots,x_{n-1})
> $$
>
> be a finite sequence with $x_i\in\operatorname{Var}_{s_i}$ for some $s_i\in S$. Define
>
> $$
> \operatorname{Gen}_{\vec x}(\varphi)
> $$
>
> by recursion on $n$:
>
> $$
> \operatorname{Gen}_{()}(\varphi):=\varphi,
> $$
>
> $$
> \operatorname{Gen}_{(x_0,\dots,x_{n-1})}(\varphi):=
> \forall x_0\,\operatorname{Gen}_{(x_1,\dots,x_{n-1})}(\varphi).
> $$
>
> Repetitions in $\vec x$ are permitted. The result is a formula in $\operatorname{Form}_{\mathcal L}$.

> [!lemma] Lemma 15.2: Validity is closed under universal closure
> If
>
> $$
> \models_{\mathcal L}\varphi,
> $$
>
> then for every finite variable sequence $\vec x$,
>
> $$
> \models_{\mathcal L}\operatorname{Gen}_{\vec x}(\varphi).
> $$

> [!proof-sketch] Proof Sketch 15.2
> Induct on the length of $\vec x$. For one step, if $\varphi$ is true under every assignment, then for any assignment $a$ and every $m\in M_s$, $\varphi$ is true under $a[x\mapsto m]$, so $\forall x\,\varphi$ is true under $a$.

> [!definition] Definition 15.3: Generalized schema record
> A **generalized schema record** is a tuple
>
> $$
> \mathfrak S=(P,D,B)
> $$
>
> where $P$ is a parameter set, $D\subseteq P$, and
>
> $$
> B:D\to\operatorname{Form}_{\mathcal L}
> $$
>
> is a base-instance map. Its generalized instance set is
>
> $$
> \operatorname{GInst}(\mathfrak S):=
> \{\operatorname{Gen}_{\vec x}(B(d)):
> d\in D,
> \ \vec x\in(\coprod_{s\in S}\operatorname{Var}_s)^{<\omega}\}.
> $$
>
> It is sound iff
>
> $$
> \forall d\in D,
> \ \models B(d).
> $$

> [!proposition] Proposition 15.4: Soundness of generalized schema records
> If $\mathfrak S=(P,D,B)$ is sound, then
>
> $$
> \operatorname{GInst}(\mathfrak S)\subseteq
> \{\varphi\in\operatorname{Form}_{\mathcal L}:\models\varphi\}.
> $$

> [!proof-sketch] Proof Sketch 15.4
> Apply Lemma 15.2 to each valid base instance $B(d)$.

### 15.2. Quantifier axiom schemas

> [!definition] Definition 15.5: Quantifier distribution schema
> Define a schema record $\mathfrak S_{\forall\to}$ as follows. Let $P$ be the set of triples
>
> $$
> (s,x,\varphi,\psi)
> $$
>
> with $s\in S$, $x\in\operatorname{Var}_s$, and $\varphi,\psi\in\operatorname{Form}_{\mathcal L}$. Let $D=P$. Define
>
> $$
> B(s,x,\varphi,\psi):=
> \forall x(\varphi\to\psi)\to(\forall x\,\varphi\to\forall x\,\psi).
> $$

> [!proposition] Proposition 15.6: Soundness of quantifier distribution
> For every $(s,x,\varphi,\psi)\in D$,
>
> $$
> \models B(s,x,\varphi,\psi).
> $$

> [!proof-sketch] Proof Sketch 15.6
> Fix $\mathcal M$ and assignment $a$. If $\forall x(\varphi\to\psi)$ and $\forall x\varphi$ hold at $a$, then for every $m\in M_s$, both $\varphi\to\psi$ and $\varphi$ hold at $a[x\mapsto m]$, hence $\psi$ holds there. Therefore $\forall x\psi$ holds at $a$.

> [!definition] Definition 15.7: Vacuous generalization schema
> Let $P$ be the set of triples
>
> $$
> (s,x,\varphi)
> $$
>
> with $s\in S$, $x\in\operatorname{Var}_s$, and $\varphi\in\operatorname{Form}_{\mathcal L}$. Let
>
> $$
> D:=\{(s,x,\varphi)\in P:x\notin\operatorname{FV}_s(\varphi)\}.
> $$
>
> Define
>
> $$
> B(s,x,\varphi):=\varphi\to\forall x\,\varphi.
> $$

> [!proposition] Proposition 15.8: Soundness of vacuous generalization
> For every $(s,x,\varphi)\in D$,
>
> $$
> \models B(s,x,\varphi).
> $$

> [!proof-sketch] Proof Sketch 15.8
> If $x\notin\operatorname{FV}_s(\varphi)$ and $\mathcal M\models\varphi[a]$, then by dependence on free variables, $\mathcal M\models\varphi[a[x\mapsto m]]$ for every $m\in M_s$. Hence $\mathcal M\models\forall x\varphi[a]$.

> [!definition] Definition 15.9: Universal instantiation schema
> Let $P$ be the set of quadruples
>
> $$
> (s,x,t,\varphi)
> $$
>
> where $s\in S$, $x\in\operatorname{Var}_s$, $t\in\operatorname{Term}_{\mathcal L,s}$, and $\varphi\in\operatorname{Form}_{\mathcal L}$. Let
>
> $$
> D:=\{(s,x,t,\varphi)\in P:\varphi[t/x]\text{ is defined capture-avoidantly}\}.
> $$
>
> Define
>
> $$
> B(s,x,t,\varphi):=\forall x\,\varphi\to\varphi[t/x].
> $$

> [!proposition] Proposition 15.10: Soundness of universal instantiation
> For every $(s,x,t,\varphi)\in D$,
>
> $$
> \models B(s,x,t,\varphi).
> $$

> [!proof-sketch] Proof Sketch 15.10
> If $\forall x\varphi$ holds at $a$, then $\varphi$ holds at $a[x\mapsto t^{\mathcal M}[a]]$. The formula substitution lemma identifies this with satisfaction of $\varphi[t/x]$ at $a$.

### 15.3. Equality axiom schemas

> [!definition] Definition 15.11: Equality reflexivity schema
> Let
>
> $$
> P:=\coprod_{s\in S}\operatorname{Term}_{\mathcal L,s}.
> $$
>
> For $(s,t)\in P$, define
>
> $$
> B(s,t):=t=_s t.
> $$
>
> The equality reflexivity schema is $\mathfrak S_{=\mathrm{refl}}=(P,P,B)$.

> [!proposition] Proposition 15.12: Soundness of equality reflexivity
> For every $s\in S$ and $t\in\operatorname{Term}_{\mathcal L,s}$,
>
> $$
> \models t=_s t.
> $$

> [!proof-sketch] Proof Sketch 15.12
> For every structure and assignment, $t^{\mathcal M}[a]$ is an element of $M_s$, and equality in $M_s$ is reflexive.

> [!definition] Definition 15.13: Equality substitutivity for relation symbols
> Let $P_R$ be the set of tuples
>
> $$
> (R,(t_i)_{i<n},(u_i)_{i<n})
> $$
>
> where $R\in\operatorname{Rel}_{\mathcal L,w}$, $w=(s_0,\dots,s_{n-1})$, and $t_i,u_i\in\operatorname{Term}_{\mathcal L,s_i}$. Define
>
> $$
> B_R:=
> \left(\bigwedge_{i<n} t_i=_{s_i}u_i\right)
> \to
> \left(R(t_0,\dots,t_{n-1})\to R(u_0,\dots,u_{n-1})\right),
> $$
>
> where the finite conjunction is interpreted by the chosen Boolean abbreviations and is $\top$ when $n=0$.

> [!proposition] Proposition 15.14: Soundness of relation substitutivity
> Every instance $B_R$ from Definition 15.13 is valid.

> [!proof-sketch] Proof Sketch 15.14
> Under any assignment, the antecedent asserts equality of corresponding term values in the appropriate carriers. Therefore the two interpreted tuples in $M_w$ are equal, so membership in $R^{\mathcal M}\subseteq M_w$ is the same for both.

> [!definition] Definition 15.15: Equality substitutivity for function symbols
> Let $P_F$ be the set of tuples
>
> $$
> (f,(t_i)_{i<n},(u_i)_{i<n})
> $$
>
> where $f\in\operatorname{Func}_{\mathcal L,w,s}$, $w=(s_0,\dots,s_{n-1})$, and $t_i,u_i\in\operatorname{Term}_{\mathcal L,s_i}$. Define
>
> $$
> B_F:=
> \left(\bigwedge_{i<n} t_i=_{s_i}u_i\right)
> \to
> \left(f(t_0,\dots,t_{n-1})=_s f(u_0,\dots,u_{n-1})\right).
> $$

> [!proposition] Proposition 15.16: Soundness of function substitutivity
> Every instance $B_F$ from Definition 15.15 is valid.

> [!proof-sketch] Proof Sketch 15.16
> Equal input tuples in $M_w$ have the same image under the function $f^{\mathcal M}:M_w\to M_s$.

> [!remark] Remark 15.17: Equality schemas are sorted
> Equality axioms are families indexed by sorts and profiles. A single untyped equality substitutivity schema is not well-formed unless it is read as shorthand for the sorted family above.

---

## 16. Natural Deduction and Sequent Calculus as Formal Data

### 16.1. Natural deduction records

> [!definition] Definition 16.1: Natural deduction judgment object
> A **natural deduction judgment** is a pair
>
> $$
> (\Gamma,\varphi)
> $$
>
> where $\Gamma\in\mathcal P_{\mathrm{fin}}(\operatorname{Form}_{\mathcal L})$ is a finite set of open assumptions and $\varphi\in\operatorname{Form}_{\mathcal L}$. It is displayed as
>
> $$
> \Gamma\vdash\varphi.
> $$

> [!definition] Definition 16.2: Natural deduction rule
> A **natural deduction rule** is a set
>
> $$
> \rho\subseteq
> \coprod_{n\in\mathbb N}
> (\mathcal P_{\mathrm{fin}}(\operatorname{Form}_{\mathcal L})\times\operatorname{Form}_{\mathcal L})^n
> \times
> (\mathcal P_{\mathrm{fin}}(\operatorname{Form}_{\mathcal L})\times\operatorname{Form}_{\mathcal L}).
> $$
>
> An element of $\rho$ consists of finitely many premise judgments and one conclusion judgment.

> [!definition] Definition 16.3: Universal introduction rule with side condition
> The universal-introduction rule is the set of pairs
>
> $$
> \frac{\Gamma\vdash\varphi}{\Gamma\vdash\forall x\,\varphi}
> $$
>
> where $x\in\operatorname{Var}_s$ and
>
> $$
> x\notin\bigcup_{\gamma\in\Gamma}\operatorname{FV}_s(\gamma).
> $$

> [!proposition] Proposition 16.4: Soundness of universal introduction
> If the premise judgment $\Gamma\vdash\varphi$ is semantically valid and the side condition of Definition 16.3 holds, then the conclusion judgment $\Gamma\vdash\forall x\varphi$ is semantically valid.

> [!proof-sketch] Proof Sketch 16.4
> Let $a$ satisfy every formula in $\Gamma$. For any $m\in M_s$, the updated assignment $a[x\mapsto m]$ still satisfies every $\gamma\in\Gamma$ because $x$ is not free in any open assumption. Hence $\varphi$ holds at every such update, so $\forall x\varphi$ holds at $a$.

> [!definition] Definition 16.5: Existential elimination rule with eigenvariable
> The existential-elimination rule consists of inferences
>
> $$
> \frac{\Gamma\vdash\exists x\,\varphi\qquad \Delta\cup\{\varphi[y/x]\}\vdash\psi}
> {\Gamma\cup\Delta\vdash\psi}
> $$
>
> where $x,y\in\operatorname{Var}_s$, $\varphi[y/x]$ is capture-avoiding, and
>
> $$
> y\notin
> \operatorname{FV}_s(\psi)
> \cup
> \bigcup_{\gamma\in\Gamma\cup\Delta}\operatorname{FV}_s(\gamma)
> \cup
> (\operatorname{FV}_s(\varphi)\setminus\{x\}).
> $$

> [!proposition] Proposition 16.6: Soundness of existential elimination
> The rule in Definition 16.5 is semantically valid.

> [!proof-sketch] Proof Sketch 16.6
> If $\exists x\varphi$ holds under an assignment satisfying $\Gamma\cup\Delta$, choose $m\in M_s$ witnessing $\varphi$. Modify the assignment by sending $y$ to $m$. Freshness ensures all open assumptions and $\psi$ have unchanged truth values except for the intended witness formula. The second premise yields $\psi$.

> [!warning] Warning 16.7: The eigenvariable is a side-condition object
> The freshness condition in Definition 16.5 is part of the rule as a set of admissible inferences. It is not an informal comment. Removing it produces a different rule relation and can make invalid conclusions derivable.

### 16.2. Sequents

> [!definition] Definition 16.8: Sequent
> A **multiple-conclusion sequent** is a pair
>
> $$
> (\Gamma,\Delta)
> $$
>
> with
>
> $$
> \Gamma,\Delta\in\mathcal P_{\mathrm{fin}}(\operatorname{Form}_{\mathcal L}).
> $$
>
> It is displayed as
>
> $$
> \Gamma\Rightarrow\Delta.
> $$

> [!definition] Definition 16.9: Semantic validity of a sequent
> A sequent $\Gamma\Rightarrow\Delta$ is **valid in $\mathcal M$** iff for every assignment $a$,
>
> $$
> \left(\forall\gamma\in\Gamma,
> \ \mathcal M\models\gamma[a]\right)
> \Longrightarrow
> \left(\exists\delta\in\Delta,
> \ \mathcal M\models\delta[a]\right).
> $$
>
> It is **valid** iff it is valid in every $\mathcal L$-structure.

> [!definition] Definition 16.10: Structural sequent rules
> The weakening, contraction, and cut relations are the sets of inferences satisfying the following schemes:
>
> $$
> \frac{\Gamma\Rightarrow\Delta}{\Gamma\cup\{\varphi\}\Rightarrow\Delta},
> \qquad
> \frac{\Gamma\Rightarrow\Delta}{\Gamma\Rightarrow\Delta\cup\{\varphi\}},
> $$
>
> and
>
> $$
> \frac{\Gamma\Rightarrow\Delta\cup\{\varphi\}\qquad \Gamma\cup\{\varphi\}\Rightarrow\Delta}
> {\Gamma\Rightarrow\Delta}.
> $$

> [!definition] Definition 16.11: Right universal sequent rule
> The right universal rule consists of inferences
>
> $$
> \frac{\Gamma\Rightarrow\Delta\cup\{\varphi[y/x]\}}
> {\Gamma\Rightarrow\Delta\cup\{\forall x\,\varphi\}}
> $$
>
> where $x,y\in\operatorname{Var}_s$, $\varphi[y/x]$ is capture-avoiding, and
>
> $$
> y\notin
> \bigcup_{\gamma\in\Gamma}\operatorname{FV}_s(\gamma)
> \cup
> \bigcup_{\delta\in\Delta}\operatorname{FV}_s(\delta)
> \cup
> (\operatorname{FV}_s(\varphi)\setminus\{x\}).
> $$

> [!proposition] Proposition 16.12: Soundness of the right universal rule
> The rule in Definition 16.11 preserves validity of sequents.

> [!proof-sketch] Proof Sketch 16.12
> Suppose the conclusion is falsified by $\mathcal M,a$: all formulas in $\Gamma$ hold, all formulas in $\Delta$ fail, and $\forall x\varphi$ fails. Then some $m\in M_s$ makes $\varphi$ fail under $a[x\mapsto m]$. Assign $y$ to $m$. Freshness preserves the truth of $\Gamma$ and falsity of $\Delta$, and the substitution lemma gives falsity of $\varphi[y/x]$, contradicting validity of the premise.

> [!theorem] Theorem 16.13: Cut elimination statement
> For standard classical or intuitionistic many-sorted sequent calculi whose logical and equality rules are formulated with the sorted side conditions above, every derivable sequent has a cut-free derivation. The exact induction measure depends on the chosen primitive connectives and on whether sequents are sets, multisets, or lists.

> [!proof-sketch] Proof Sketch 16.13
> The proof is the usual double induction on cut formula complexity and derivation height. Many-sortedness changes only the admissible substitution and eigenvariable clauses; each reduction step preserves profiles because every term substituted for a variable has the same sort as that variable.

> [!corollary] Corollary 16.14: Subformula property for cut-free derivations
> In a cut-free many-sorted sequent calculus, every formula occurring in a derivation is a subformula or a permitted sorted substitution instance of a subformula of an end-sequent formula, with equality rules contributing only their specified atomic instances.

> [!proof-sketch] Proof Sketch 16.14
> Inspect the cut-free rules. Each logical rule decomposes a principal formula already present in the conclusion or introduces a formula whose immediate components occur in premises. Quantifier rules introduce only sort-correct term or eigenvariable instances.

---

## 17. Definability, Types, Automorphisms, and Elementary Equivalence

### 17.1. Definable sets and functions

> [!definition] Definition 17.1: Parameter expansion by a sorted subset
> Let $\mathcal M$ be an $\mathcal L$-structure and let $A=(A_s)_{s\in S}$ with $A_s\subseteq M_s$. Define $\mathcal L(A)$ by adding, for each $a\in A_s$, a constant symbol
>
> $$
> \bar a:()\to s.
> $$
>
> The canonical expansion interprets $\bar a$ by $a$.

> [!definition] Definition 17.2: Definable relation with parameters
> Let $\mathcal M$ be an $\mathcal L$-structure, let $A\subseteq M$ be a sorted parameter family, and let $w=(s_0,\dots,s_{n-1})$. A subset
>
> $$
> D\subseteq M_w
> $$
>
> is **definable in $\mathcal M$ with parameters from $A$** iff there exist variables $x_i\in\operatorname{Var}_{s_i}$ and an $\mathcal L(A)$-formula $\varphi(x_0,\dots,x_{n-1})$ such that
>
> $$
> D=\{m\in M_w:\mathcal M_A\models\varphi[m_0/x_0,\dots,m_{n-1}/x_{n-1}]\}.
> $$
>
> Here $\mathcal M_A$ is the canonical $\mathcal L(A)$-expansion.

> [!definition] Definition 17.3: Parameter-free definability
> A subset $D\subseteq M_w$ is **parameter-free definable** iff it is definable with parameters from the empty sorted family
>
> $$
> A_s=\varnothing
> $$
>
> for all $s\in S$.

> [!definition] Definition 17.4: Definable function
> Let $w=(s_0,\dots,s_{n-1})$. A function
>
> $$
> F:M_w\to M_s
> $$
>
> is **definable in $\mathcal M$ with parameters from $A$** iff its graph
>
> $$
> \Gamma_F:=\{(m_0,\dots,m_{n-1},m)\in M_w\times M_s:F(m_0,
> \dots,m_{n-1})=m\}
> $$
>
> is definable with parameters from $A$.

> [!proposition] Proposition 17.5: Automorphism invariance of parameter-free definability
> If $D\subseteq M_w$ is parameter-free definable and $h:\mathcal M\cong\mathcal M$ is an automorphism, then
>
> $$
> h_w[D]=D.
> $$

> [!proof-sketch] Proof Sketch 17.5
> If $D$ is defined by $\varphi(\bar x)$, isomorphism invariance of satisfaction gives $\mathcal M\models\varphi[\bar m]$ iff $\mathcal M\models\varphi[h_w(\bar m)]$.

> [!warning] Warning 17.6: Definability is not set existence
> A subset $D\subseteq M_w$ can exist set-theoretically without being definable in $\mathcal M$. Definability is relative to the language, structure, variable profile, and allowed parameter family.

### 17.2. Types

> [!definition] Definition 17.7: Formula variables of a profile
> For $w=(s_0,\dots,s_{n-1})$, fix a tuple of distinct variables
>
> $$
> \bar x=(x_0,
> \dots,x_{n-1})
> $$
>
> with $x_i\in\operatorname{Var}_{s_i}$. Define
>
> $$
> \operatorname{Form}_{\mathcal L}(\bar x):=
> \{\varphi\in\operatorname{Form}_{\mathcal L}:
> \operatorname{FV}(\varphi)\subseteq\{x_0,
> \dots,x_{n-1}\}\}.
> $$

> [!definition] Definition 17.8: Complete type realized by a tuple
> Let $\mathcal M$ be an $\mathcal L$-structure, let $A\subseteq M$ be a sorted parameter family, let $w=(s_0,\dots,s_{n-1})$, and let $m\in M_w$. The **complete type of $m$ over $A$** is
>
> $$
> \operatorname{tp}^{\mathcal M}(m/A):=
> \{\varphi(\bar x)\in\operatorname{Form}_{\mathcal L(A)}(\bar x):
> \mathcal M_A\models\varphi[m]\}.
> $$

> [!definition] Definition 17.9: Realization of a partial type
> Let $p(\bar x)\subseteq\operatorname{Form}_{\mathcal L(A)}(\bar x)$. An element $m\in M_w$ **realizes** $p$ in $\mathcal M$ iff
>
> $$
> \forall\varphi\in p,
> \ \mathcal M_A\models\varphi[m].
> $$

> [!definition] Definition 17.10: Consistency of a type with a theory
> Let $T\subseteq\operatorname{Sent}_{\mathcal L(A)}$. A set $p(\bar x)$ is **consistent with $T$** iff every finite subset
>
> $$
> p_0\subseteq p
> $$
>
> satisfies
>
> $$
> T\cup\{\exists\bar x\bigwedge p_0\}
> $$
>
> is satisfiable, where $\exists\bar x$ abbreviates the sorted existential block
>
> $$
> \exists x_0\cdots\exists x_{n-1}.
> $$

> [!proposition] Proposition 17.11: Realization in an elementary extension
> If $p(\bar x)$ is consistent with $\operatorname{Th}(\mathcal M_A)$, then there exists an elementary extension
>
> $$
> \mathcal N_A\succcurlyeq\mathcal M_A
> $$
>
> and $n\in N_w$ realizing $p$.

> [!proof-sketch] Proof Sketch 17.11
> Add new constants $c_i:()\to s_i$ and add sentences $\varphi(c_0,\dots,c_{n-1})$ for all $\varphi\in p$. Finite satisfiability follows from consistency. Compactness gives a model of the expanded theory; the elementary diagram of $\mathcal M_A$ embeds $\mathcal M_A$ elementarily into its reduct.

### 17.3. Elementary equivalence and chains

> [!definition] Definition 17.12: Complete theory of a structure
> The **complete theory** of an $\mathcal L$-structure $\mathcal M$ is
>
> $$
> \operatorname{Th}(\mathcal M):=
> \{\sigma\in\operatorname{Sent}_{\mathcal L}:\mathcal M\models\sigma\}.
> $$

> [!definition] Definition 17.13: Elementary equivalence
> Two $\mathcal L$-structures $\mathcal M$ and $\mathcal N$ are **elementarily equivalent**, written
>
> $$
> \mathcal M\equiv\mathcal N,
> $$
>
> iff
>
> $$
> \operatorname{Th}(\mathcal M)=\operatorname{Th}(\mathcal N).
> $$

> [!proposition] Proposition 17.14: Isomorphism invariance of satisfaction
> If $h:\mathcal M\cong\mathcal N$, $a:\operatorname{Var}\to M$, and $\varphi\in\operatorname{Form}_{\mathcal L}$, then
>
> $$
> \mathcal M\models\varphi[a]
> \Longleftrightarrow
> \mathcal N\models\varphi[h\circ a].
> $$
>
> Hence $\mathcal M\cong\mathcal N$ implies $\mathcal M\equiv\mathcal N$.

> [!proof-sketch] Proof Sketch 17.14
> Terms are preserved by homomorphism and reflected by the inverse isomorphism. Atomic relation truth is preserved and reflected by the isomorphism definition. Boolean and quantifier clauses follow by induction, using that each $h_s:M_s\to N_s$ is bijective for the quantifier step.

> [!definition] Definition 17.15: Elementary chain
> Let $(I,\leq)$ be a linearly ordered set. An **elementary chain** is a family
>
> $$
> (\mathcal M_i)_{i\in I}
> $$
>
> such that
>
> $$
> i\leq j\Longrightarrow\mathcal M_i\preccurlyeq\mathcal M_j.
> $$

> [!theorem] Theorem 17.16: Elementary chain theorem
> Let $(\mathcal M_i)_{i\in I}$ be an elementary chain. Define
>
> $$
> M_s:=\bigcup_{i\in I}M_{i,s}
> $$
>
> for every $s\in S$, with function and relation interpretations given by the union of the compatible interpretations. Then the resulting $\mathcal L$-structure $\mathcal M$ satisfies
>
> $$
> \mathcal M_i\preccurlyeq\mathcal M
> $$
>
> for every $i\in I$.

> [!proof-sketch] Proof Sketch 17.16
> Compatibility of operations and relations follows from the chain condition. For elementarity, use the Tarski-Vaught test: any existential witness for parameters from $M_i$ lies in some $M_j$ with $j\geq i$ and then is reflected back as needed by $\mathcal M_i\preccurlyeq\mathcal M_j$.

---

## 18. Algebraic Integration, Term Operations, and Theory Morphisms

### 18.1. Free-forgetful adjunction and term monad

> [!definition] Definition 18.1: Forgetful functor for the functional reduct
> Let
>
> $$
> U:\mathbf{Alg}(\Sigma_{\mathcal L})\to\mathbf{Set}^S
> $$
>
> be the functor sending a $\Sigma_{\mathcal L}$-algebra to its sorted carrier and a homomorphism to its underlying sorted map.

> [!theorem] Theorem 18.2: Free-forgetful adjunction
> The assignment
>
> $$
> X\mapsto\mathbf T_{\Sigma_{\mathcal L}}(X)
> $$
>
> extends to a functor
>
> $$
> F:\mathbf{Set}^S\to\mathbf{Alg}(\Sigma_{\mathcal L})
> $$
>
> left adjoint to $U$:
>
> $$
> F\dashv U.
> $$
>
> For every $X\in\mathbf{Set}^S$ and every $\Sigma_{\mathcal L}$-algebra $\mathbf A$ there is a natural bijection
>
> $$
> \mathbf{Alg}(\Sigma_{\mathcal L})(F(X),\mathbf A)
> \cong
> \mathbf{Set}^S(X,U\mathbf A).
> $$

> [!proof-sketch] Proof Sketch 18.2
> The bijection sends a homomorphism to its restriction along the generator insertion $X\to UF(X)$. Its inverse sends a sorted generator assignment to the unique homomorphic extension. Naturality follows from uniqueness of extension.

> [!corollary] Corollary 18.3: Term monad
> The composite
>
> $$
> T:=U\circ F:\mathbf{Set}^S\to\mathbf{Set}^S
> $$
>
> is a monad. Its unit is the generator insertion
>
> $$
> \eta_X:X\to T(X),
> $$
>
> and its multiplication
>
> $$
> \mu_X:T(T(X))\to T(X)
> $$
>
> is the homomorphic extension of
>
> $$
> \operatorname{id}_{T(X)}:T(X)\to T(X).
> $$

> [!proof-sketch] Proof Sketch 18.3
> This is the monad induced by any adjunction. Explicitly, $\mu_X$ is simultaneous substitution of terms for term-valued variables. The monad laws are the substitution identity and associativity laws.

### 18.2. Sorted term operations and clones

> [!definition] Definition 18.4: Formal operation of profile $w\Rightarrow s$
> Let $w=(s_0,\dots,s_{n-1})$. A **formal $\mathcal L$-term operation of profile $w\Rightarrow s$** is an element
>
> $$
> t\in T_{\Sigma_{\mathcal L}}(X)_s
> $$
>
> where $X$ is the sorted family with distinguished variables
>
> $$
> x_i\in X_{s_i}
> $$
>
> for $i<n$ and no other variables, up to the evident renaming of the distinguished variables.

> [!construction] Construction 18.5: Interpretation of a formal operation in a structure
> Let $t$ be a formal operation of profile $w\Rightarrow s$ and let $\mathcal M$ be an $\mathcal L$-structure. Define
>
> $$
> t^{\mathcal M}:M_w\to M_s
> $$
>
> by
>
> $$
> t^{\mathcal M}(m_0,\dots,m_{n-1})=t^{\mathcal M}[a],
> $$
>
> where $a(x_i)=m_i$ and $a$ is arbitrary on variables not occurring in $t$.

> [!proposition] Proposition 18.6: Well-definedness of term-operation interpretation
> The value $t^{\mathcal M}(m_0,\dots,m_{n-1})$ in Construction 18.5 is independent of the assignment values on variables not occurring in $t$.

> [!proof-sketch] Proof Sketch 18.6
> Apply Proposition 6.9 to the term $t$.

> [!definition] Definition 18.7: Many-sorted clone of term operations
> The **term clone** of $\mathcal M_{\mathrm{alg}}$ is the profile-indexed family
>
> $$
> \operatorname{Clo}(\mathcal M)_{w,s}
> $$
>
> where $\operatorname{Clo}(\mathcal M)_{w,s}$ is the set of all functions
>
> $$
> M_w\to M_s
> $$
>
> induced by $\mathcal L$-terms of profile $w\Rightarrow s$.

> [!proposition] Proposition 18.8: Closure of term operations under sorted superposition
> If
>
> $$
> F\in\operatorname{Clo}(\mathcal M)_{w,s}
> $$
>
> and
>
> $$
> G_i\in\operatorname{Clo}(\mathcal M)_{v,s_i}
> $$
>
> for $w=(s_0,\dots,s_{n-1})$, then
>
> $$
> H(m):=F(G_0(m),\dots,G_{n-1}(m))
> $$
>
> belongs to
>
> $$
> \operatorname{Clo}(\mathcal M)_{v,s}.
> $$

> [!proof-sketch] Proof Sketch 18.8
> Choose terms representing $F$ and the $G_i$. Substitute the representing terms for the variables of the term representing $F$. The substitution result has the required output sort and interprets as $H$ by the substitution evaluation lemma.

### 18.3. Theory morphisms and translations

> [!definition] Definition 18.9: Same-sort signature morphism
> Let $\mathcal L$ and $\mathcal K$ have the same sort set $S$. A **same-sort signature morphism**
>
> $$
> \tau:\mathcal L\to\mathcal K
> $$
>
> consists of functions
>
> $$
> \tau^F_{w,s}:\operatorname{Func}_{\mathcal L,w,s}\to\operatorname{Func}_{\mathcal K,w,s}
> $$
>
> and
>
> $$
> \tau^R_w:\operatorname{Rel}_{\mathcal L,w}\to\operatorname{Rel}_{\mathcal K,w}
> $$
>
> for every profile.

> [!construction] Construction 18.10: Translation of terms and formulas along a signature morphism
> A same-sort signature morphism $\tau:\mathcal L\to\mathcal K$ induces:
>
> 1. a homomorphism of term algebras
>    $$
>    \tau_T:\mathbf{Term}_{\mathcal L}\to\mathbf{Term}_{\mathcal K}
>    $$
>    fixing variables and sending each $f$ to $\tau^F(f)$;
> 2. a formula translation
>    $$
>    \tau_F:\operatorname{Form}_{\mathcal L}\to\operatorname{Form}_{\mathcal K}
>    $$
>    commuting with logical constructors, sending equality to equality, and sending
>    $$
>    R(t_0,\dots,t_{n-1})
>    $$
>    to
>    $$
>    \tau^R(R)(\tau_T(t_0),\dots,\tau_T(t_{n-1})).
>    $$

> [!definition] Definition 18.11: Reduct along a signature morphism
> If $\tau:\mathcal L\to\mathcal K$ and $\mathcal N$ is a $\mathcal K$-structure, define the **$\tau$-reduct** $\tau^*(\mathcal N)$ by:
>
> 1. the same sorted carriers as $\mathcal N$;
> 2. for $f\in\operatorname{Func}_{\mathcal L,w,s}$,
>    $$
>    f^{\tau^*(\mathcal N)}:=\tau^F(f)^{\mathcal N};
>    $$
> 3. for $R\in\operatorname{Rel}_{\mathcal L,w}$,
>    $$
>    R^{\tau^*(\mathcal N)}:=\tau^R(R)^{\mathcal N}.
>    $$

> [!theorem] Theorem 18.12: Satisfaction under signature translation
> Let $\tau:\mathcal L\to\mathcal K$, let $\mathcal N$ be a $\mathcal K$-structure, let $a$ be an assignment into its carriers, and let $\varphi\in\operatorname{Form}_{\mathcal L}$. Then
>
> $$
> \tau^*(\mathcal N)\models\varphi[a]
> \Longleftrightarrow
> \mathcal N\models\tau_F(\varphi)[a].
> $$

> [!proof-sketch] Proof Sketch 18.12
> First prove the corresponding term-evaluation identity by induction on terms. Then prove the formula statement by induction on formulas. Equality and relation atoms use the definitions of $\tau_T$, $\tau_F$, and $\tau^*(\mathcal N)$; logical constructors commute by construction.

> [!remark] Remark 18.13: Integration boundary
> Signature translations compare languages. Definitional expansions compare theories with unique model expansions. Concrete presentations compare syntax carriers by isomorphism. These are distinct comparison mechanisms and should not be conflated.

---


## 19. Elementary Classes, Equational Theories, and Algebraic Theories

### 19.1. Elementary classes

> [!definition] Definition 19.1: Elementary class
> Let $\mathcal K$ be a class of $\mathcal L$-structures. The class $\mathcal K$ is **elementary** iff there exists a theory
>
> $$
> T\subseteq\operatorname{Sent}_{\mathcal L}
> $$
>
> such that
>
> $$
> \mathcal K=\operatorname{Mod}_{\mathcal L}(T).
> $$
>
> It is **finitely axiomatizable** iff such a $T$ can be chosen finite. It is **singly axiomatizable** iff such a $T$ can be chosen of the form $T=\{\sigma\}$.

> [!proposition] Proposition 19.2: Elementary classes are isomorphism closed
> If $\mathcal K=\operatorname{Mod}_{\mathcal L}(T)$ and $\mathcal M\in\mathcal K$ with
>
> $$
> \mathcal M\cong\mathcal N,
> $$
>
> then
>
> $$
> \mathcal N\in\mathcal K.
> $$

> [!proof-sketch] Proof Sketch 19.2
> Isomorphism invariance of satisfaction gives $\mathcal M\models\sigma$ iff $\mathcal N\models\sigma$ for every sentence $\sigma\in T$.

> [!definition] Definition 19.3: Universal and existential sentences
> A sentence $\sigma$ is **universal** iff it is logically equivalent to a sentence of the form
>
> $$
> \forall x_0\cdots\forall x_{n-1}\,\theta
> $$
>
> where $x_i\in\operatorname{Var}_{s_i}$ and $\theta$ is quantifier-free.
>
> A sentence $\sigma$ is **existential** iff it is logically equivalent to a sentence of the form
>
> $$
> \exists x_0\cdots\exists x_{n-1}\,\theta
> $$
>
> with $\theta$ quantifier-free.
>
> A theory is universal or existential iff all of its axioms have the corresponding form.

> [!definition] Definition 19.4: Universal Horn sentence
> A **universal Horn sentence** is a universal closure of a formula
>
> $$
> (\alpha_0\wedge\cdots\wedge\alpha_{k-1})\to\beta
> $$
>
> where each $\alpha_i$ is atomic and $\beta$ is atomic or $\bot$. The variables occurring in the displayed quantifier-free formula are sorted variables, and each atom must be sort-correct.

> [!remark] Remark 19.5: Sorts in preservation theorems
> Preservation statements for universal, existential, or Horn theories use the same syntactic forms as in the one-sorted case, but substructures, products, and homomorphisms are sorted objects. Every quantified variable ranges over its own carrier $M_s$.

### 19.2. Equations as many-sorted first-order sentences

> [!definition] Definition 19.6: Many-sorted equation
> Let $X=(X_s)_{s\in S}$ be a sorted variable family. A **many-sorted equation over $X$ of sort $s$** is a pair
>
> $$
> (t,u)\in T_{\Sigma_{\mathcal L}}(X)_s\times T_{\Sigma_{\mathcal L}}(X)_s.
> $$
>
> It is displayed as
>
> $$
> t\approx_s u.
> $$
>
> There is no equation between terms of different sorts.

> [!definition] Definition 19.7: First-order sentence associated to an equation
> Let $e$ be the equation $t\approx_s u$. Let
>
> $$
> \operatorname{Var}(e):=\operatorname{Var}(t)\cup\operatorname{Var}(u)
> $$
>
> as a finite sorted family. Choose a finite sequence $\vec x$ listing all variables in $\operatorname{Var}(e)$, each with its assigned sort. The **universal closure** of $e$ is the sentence
>
> $$
> \forall\vec x\,(t=_s u).
> $$
>
> Different listings of $\operatorname{Var}(e)$ yield logically equivalent sentences.

> [!definition] Definition 19.8: Satisfaction of an equation in an algebra
> Let $\mathbf A$ be a $\Sigma_{\mathcal L}$-algebra. The algebra $\mathbf A$ satisfies the equation
>
> $$
> t\approx_s u
> $$
>
> iff for every sorted valuation
>
> $$
> g:X\to A,
> $$
>
> the two evaluations agree:
>
> $$
> \operatorname{ev}_{g,s}(t)=\operatorname{ev}_{g,s}(u).
> $$
>
> Write
>
> $$
> \mathbf A\models t\approx_s u.
> $$

> [!proposition] Proposition 19.9: Equational satisfaction equals first-order satisfaction
> Let $\mathcal M$ be an $\mathcal L$-structure and let $e$ be $t\approx_s u$. Then
>
> $$
> \mathcal M_{\mathrm{alg}}\models e
> $$
>
> iff
>
> $$
> \mathcal M\models\forall\vec x\,(t=_s u),
> $$
>
> where $\vec x$ lists the variables occurring in $e$.

> [!proof-sketch] Proof Sketch 19.9
> A sorted valuation $g:X\to M$ is the same data as an assignment of the variables occurring in $e$ to the corresponding carriers. Term evaluation in $\mathcal M$ is evaluation in the algebraic reduct. The equality atom is true exactly when the two evaluated elements of $M_s$ are equal.

> [!definition] Definition 19.10: Many-sorted equational theory
> A **many-sorted equational theory** over $\Sigma_{\mathcal L}$ is a set
>
> $$
> E
> $$
>
> of many-sorted equations. Its algebraic model class is
>
> $$
> \operatorname{Mod}_{\mathrm{alg}}(E):=
> \{\mathbf A\in\mathbf{Alg}(\Sigma_{\mathcal L}):\forall e\in E,
> \ \mathbf A\models e\}.
> $$
>
> Its associated first-order theory is
>
> $$
> T_E:=\{\forall\vec x\,(t=_s u): (t\approx_s u)\in E\}.
> $$

> [!corollary] Corollary 19.11: Equational classes are elementary
> If $E$ is a many-sorted equational theory and $\mathcal L$ has no relation symbols beyond equality, then
>
> $$
> \operatorname{Mod}_{\mathrm{alg}}(E)
> $$
>
> is the same class as
>
> $$
> \operatorname{Mod}_{\mathcal L}(T_E)
> $$
>
> after identifying $\mathcal L$-structures with their algebraic reducts.

> [!proof-sketch] Proof Sketch 19.11
> Apply Proposition 19.9 to every equation in $E$.

> [!example] Example 19.12: Many-sorted algebraic theory of directed graphs with source and target
> Let
>
> $$
> S=\{V,E\}
> $$
>
> and let the functional signature contain
>
> $$
> s:E\to V,
> \qquad
> t:E\to V.
> $$
>
> With no equations, a model is a directed multigraph object with vertex carrier $A_V$, edge carrier $A_E$, and source and target maps. Adding relation symbols, such as incidence predicates, moves beyond the purely equational class and requires the relational satisfaction clauses of first-order logic.

> [!example] Example 19.13: Typed algebraic theory with operations
> Let $S=\{A,B\}$ and let the functional signature contain
>
> $$
> m:(A,A)\to A,
> \qquad
> e:()\to A,
> \qquad
> p:A\to B.
> $$
>
> The equation
>
> $$
> m(x,e)\approx_A x
> $$
>
> is well-formed for $x\in X_A$. The expression
>
> $$
> m(x,p(x))\approx_A x
> $$
>
> is not an equation because $p(x)$ has sort $B$, not sort $A$.

### 19.3. Presentations by generators and equations

> [!definition] Definition 19.14: Congruence generated by equations on a free algebra
> Let $X\in\mathbf{Set}^S$ and let $E$ be a set of equations
>
> $$
> t\approx_s u
> $$
>
> with $t,u\in T_{\Sigma_{\mathcal L}}(X)_s$. Define
>
> $$
> \theta_E
> $$
>
> to be the least sorted congruence on $\mathbf T_{\Sigma_{\mathcal L}}(X)$ such that
>
> $$
> t\ \theta_{E,s}\ u
> $$
>
> for every equation $t\approx_s u$ in $E$.

> [!construction] Construction 19.15: Algebra presented by generators and equations
> The **many-sorted algebra presented by $X$ and $E$** is
>
> $$
> \langle X\mid E\rangle:=
> \mathbf T_{\Sigma_{\mathcal L}}(X)/\theta_E.
> $$
>
> The generator map is the composite
>
> $$
> X\xrightarrow{\eta_X}T_{\Sigma_{\mathcal L}}(X)
> \xrightarrow{q_E}T_{\Sigma_{\mathcal L}}(X)/\theta_E.
> $$

> [!theorem] Theorem 19.16: Universal property of presentations
> Let $\mathbf A$ be a $\Sigma_{\mathcal L}$-algebra and let
>
> $$
> g:X\to A
> $$
>
> be a sorted map. There exists a unique homomorphism
>
> $$
> \bar g:\langle X\mid E\rangle\to\mathbf A
> $$
>
> satisfying
>
> $$
> \bar g\circ q_E\circ\eta_X=g
> $$
>
> iff, for every equation $t\approx_s u$ in $E$,
>
> $$
> \operatorname{ev}_{g,s}(t)=\operatorname{ev}_{g,s}(u).
> $$

> [!proof-sketch] Proof Sketch 19.16
> The map $g$ extends uniquely to $\widehat g:\mathbf T(X)\to\mathbf A$. It factors through the quotient by $\theta_E$ iff $\theta_E\subseteq\ker(\widehat g)$. Since $\theta_E$ is the least congruence containing the listed equations, this is equivalent to the displayed equality condition.

> [!warning] Warning 19.17: First-order theories are not usually algebra presentations
> A general first-order theory may contain relation symbols, quantifiers alternating in arbitrary patterns, and non-equational axioms. Only the purely functional equational fragment presents algebras by generators and equations. Relational first-order theories require satisfaction in structures, not merely quotienting a term algebra.

### 19.4. Elementary classes versus algebraic varieties

> [!definition] Definition 19.18: Many-sorted variety
> A class $\mathcal V\subseteq\mathbf{Alg}(\Sigma_{\mathcal L})$ is a **many-sorted variety** iff there exists a set $E$ of many-sorted equations such that
>
> $$
> \mathcal V=\operatorname{Mod}_{\mathrm{alg}}(E).
> $$

> [!proposition] Proposition 19.19: Varieties are elementary classes in the equality language
> If $\mathcal V$ is a many-sorted variety, then under the identification of $\Sigma_{\mathcal L}$-algebras with equality-only $\mathcal L$-structures,
>
> $$
> \mathcal V
> $$
>
> is elementary.

> [!proof-sketch] Proof Sketch 19.19
> If $\mathcal V=\operatorname{Mod}_{\mathrm{alg}}(E)$, use the associated first-order theory $T_E$ from Definition 19.10.

> [!warning] Warning 19.20: Elementary does not imply equational
> An elementary class need not be a variety. Axioms using relation symbols, existential quantifiers, negations of equations, or implications not equivalent to equations generally cannot be represented as a class of algebras satisfying only equations.

---


## 20. Boundary Variants and Hypothesis Changes

This section records variants only to isolate which statements depend on which hypotheses. The core theory above remains the nonempty-carrier, equality-included, total-function, many-sorted first-order system.

### 20.1. Equality-free languages

> [!definition] Definition 20.1: Equality-free variant
> The **equality-free variant** of $\mathcal L$ is obtained by replacing the atomic formula set $\operatorname{Atom}_{\mathcal L}$ with
>
> $$
> \operatorname{Atom}^{-}_{\mathcal L}:=
> \coprod_{w\in S^{<\omega}}
> \coprod_{R\in\operatorname{Rel}_{\mathcal L,w}}
> \{R\}\times\operatorname{Term}_{\mathcal L,w}.
> $$
>
> No formulas of the form $t=_s u$ are available unless equality is added as an ordinary relation symbol.

> [!proposition] Proposition 20.2: Equality-free semantics
> In the equality-free variant, the satisfaction relation is Definition 7.2 together with the relation-atom part of Definition 7.1. The equality-atom clause is omitted. Term evaluation is unchanged.

> [!proof-sketch] Proof Sketch 20.2
> Equality symbols affect only atomic formula formation and atomic satisfaction. The term algebra and the interpretation of function symbols are independent of equality.

> [!warning] Warning 20.3: Ordinary equality as a relation symbol is not logical equality
> If a binary relation symbol $E_s\in\operatorname{Rel}_{\mathcal L,(s,s)}$ is used in an equality-free language, its interpretation is an arbitrary subset
>
> $$
> E_s^{\mathcal M}\subseteq M_s\times M_s.
> $$
>
> It is not forced to be the diagonal unless axioms impose reflexivity, substitutivity, and extensional behavior. Logical equality $=_s$ is interpreted as the diagonal by definition.

### 20.2. Empty sort carriers

> [!definition] Definition 20.4: Empty-sort semantics
> An **empty-sort semantics** for $\mathcal L$ permits structures $\mathcal M$ with
>
> $$
> M_s=\varnothing
> $$
>
> for some $s\in S$.
> Function interpretations must still be functions
>
> $$
> f^{\mathcal M}:M_w\to M_s.
> $$
>
> If $w=()$, this requires an element of $M_s$; hence a constant of sort $s$ forces $M_s\neq\varnothing$.

> [!warning] Warning 20.5: Empty sorts require changing assignments
> In the main theory, an assignment is a total sorted map
>
> $$
> a_s:\operatorname{Var}_s\to M_s.
> $$
>
> Since each $\operatorname{Var}_s$ is nonempty, no such assignment exists if $M_s=\varnothing$. Therefore empty-sort semantics is not obtained merely by allowing some carriers to be empty; one must also replace total assignments by local assignments on finite supports, restrict attention to sentences with a separate truth definition, or otherwise modify the semantic apparatus.

> [!proposition] Proposition 20.6: Quantifier clauses under local empty-sort semantics
> Suppose a modified semantics uses assignments only on the finite free-variable support of the formula being evaluated. If $M_s=\varnothing$ and $x\in\operatorname{Var}_s$, then, for any local assignment on the free variables of $\forall x\,\varphi$,
>
> $$
> \mathcal M\models\forall x\,\varphi
> $$
>
> holds vacuously, while
>
> $$
> \mathcal M\models\exists x\,\varphi
> $$
>
> fails.

> [!proof-sketch] Proof Sketch 20.6
> The universal clause quantifies over all $m\in M_s$ and the existential clause requires at least one $m\in M_s$. If $M_s=\varnothing$, the former condition is empty and the latter condition is impossible.

> [!warning] Warning 20.7: Completeness statements change with empty sorts
> The Henkin term model construction in Section 11 forces nonempty carriers by adding constants $d_s:()\to s$. That construction is complete for nonempty-sort semantics. A completeness theorem for empty-sort semantics must omit this requirement and adjust assignments, quantifier axioms, and Henkin witnesses accordingly.

### 20.3. Partial functions and relation-valued syntax

> [!definition] Definition 20.8: Partial-function variant
> A **partial-function variant** replaces a function-symbol interpretation
>
> $$
> f^{\mathcal M}:M_w\to M_s
> $$
>
> by a partial function
>
> $$
> f^{\mathcal M}:D_f\rightharpoonup M_s
> $$
>
> with domain
>
> $$
> D_f\subseteq M_w.
> $$
>
> Term evaluation becomes partial unless the syntax or semantics supplies definedness predicates and definedness side conditions.

> [!warning] Warning 20.9: Partial functions are not a harmless notation change
> The free term algebra is built for total operations. If function symbols are partial, then evaluation of a well-formed term can be undefined under an assignment. Substitution lemmas, satisfaction clauses for atoms, and homomorphic evaluation must be replaced by a partial-algebra or definedness-sensitive theory.

> [!definition] Definition 20.10: Relational coding of partial functions
> A partial function symbol of profile $w\to s$ may be represented in ordinary first-order logic by a relation symbol
>
> $$
> F:w\mathbin{\smallfrown}(s)
> $$
>
> together with axioms
>
> $$
> \forall\bar x\forall y\forall z((F(\bar x,y)\wedge F(\bar x,z))\to y=_s z)
> $$
>
> and optional existence axioms specifying the domain of definition.

> [!remark] Remark 20.11: Why total functions remain primitive here
> Standard many-sorted first-order logic treats function symbols as total sort-respecting operations. This keeps the term algebra free and term evaluation total. Partiality can be represented, but it is additional theory, not part of the primitive language datum used above.

### 20.4. Subsorts and order-sorted refinements

> [!definition] Definition 20.12: Subsort expansion datum
> A **subsort expansion datum** over a sort set $S$ consists of a preorder
>
> $$
> \leq\ \subseteq S\times S
> $$
>
> together with intended inclusions
>
> $$
> M_s\subseteq M_t
> $$
>
> whenever $s\leq t$.

> [!warning] Warning 20.13: Subsorts are not part of bare many-sorted logic
> In the core theory, different sorts have unrelated carriers. If $s\neq t$, there is no inclusion $M_s\subseteq M_t$, no coercion $M_s\to M_t$, and no cross-sort equality unless additional symbols or translations are supplied. Order-sorted logic adds new primitive data and new admissibility rules.

> [!definition] Definition 20.14: Coercion-symbol representation
> A subsort relation $s\leq t$ can be represented inside the bare many-sorted framework by adding a function symbol
>
> $$
> \iota_{s,t}:s\to t
> $$
>
> and axioms expressing injectivity or compatibility as needed. The resulting language is an ordinary many-sorted language with extra function symbols; it is not definitionally the same as an order-sorted language unless the translation is specified.

### 20.5. Infinitary syntax

> [!definition] Definition 20.15: Infinitary-profile variant
> An **infinitary-profile variant** replaces $S^{<\omega}$ by a specified class of arity-indexed profiles
>
> $$
> (s_i)_{i\in I}\to s
> $$
>
> where $I$ may be infinite. Function interpretations have domains
>
> $$
> \prod_{i\in I}M_{s_i}.
> $$
>
> Formula formation may also admit infinitary conjunctions, disjunctions, or quantifier blocks.

> [!warning] Warning 20.16: Infinitary logic changes compactness and proof theory
> The compactness theorem, finitary derivation systems, finite support of formulas, and the ordinary Henkin construction are tied to finitary syntax. Infinitary logics require separate hypotheses on arities, cardinal bounds, and proof rules.

> [!remark] Remark 20.17: Scope of the present note
> The present note is finitary. Every function symbol and relation symbol has a finite input profile, every term and formula is finite, and every derivation is finite unless a later section explicitly replaces those hypotheses.

---

## 21. Synthesis and Audit Checklist

### 21.1. Core object inventory

> [!remark] Remark 21.1: Primitive data
> The primitive data for the main theory are exactly
>
> $$
> S,
> \qquad
> (\operatorname{Var}_s)_{s\in S},
> \qquad
> (\operatorname{Func}_{\mathcal L,w,s})_{(w,s)},
> \qquad
> (\operatorname{Rel}_{\mathcal L,w})_{w}.
> $$
>
> Constants are the elements of $\operatorname{Func}_{\mathcal L,(),s}$. Equality is logical and sort-indexed. Formulas are not sorts. Structures interpret precisely the nonlogical symbols.

> [!remark] Remark 21.2: Main constructed objects
> From the primitive data one constructs:
>
> $$
> \Sigma_{\mathcal L},
> \quad
> \mathbf{Term}_{\mathcal L},
> \quad
> \operatorname{Atom}_{\mathcal L},
> \quad
> \operatorname{Form}^{\mathrm{raw}}_{\mathcal L},
> \quad
> \operatorname{Form}_{\mathcal L},
> \quad
> \operatorname{Sent}_{\mathcal L}.
> $$
>
> From a structure and assignment one constructs:
>
> $$
> \mathcal M_{\mathrm{alg}},
> \quad
> \operatorname{ev}^{\mathcal M}_a,
> \quad
> \models_{\mathcal L}.
> $$

> [!remark] Remark 21.3: Main equivalences and universal properties
> The term algebra satisfies
>
> $$
> \mathbf{Alg}(\Sigma_{\mathcal L})(\mathbf{Term}_{\mathcal L},\mathbf A)
> \cong
> \mathbf{Set}^S(\operatorname{Var},A).
> $$
>
> Term evaluation is the instance
>
> $$
> \operatorname{ev}^{\mathcal M}_a=\widehat a.
> $$
>
> Formula satisfaction is invariant under alpha-equivalence:
>
> $$
> \varphi\equiv_{\alpha}\psi
> \Longrightarrow
> (\mathcal M\models\varphi[a]\Longleftrightarrow\mathcal M\models\psi[a]).
> $$
>
> Definitional expansion is conservative on old sentences:
>
> $$
> T'\models\sigma
> \Longleftrightarrow
> T\models\sigma.
> $$

> [!warning] Warning 21.4: Principal failure modes
> The common failures are:
>
> 1. applying a function symbol to terms outside its input profile;
> 2. forming equality between terms of different sorts;
> 3. treating relation symbols as term constructors;
> 4. replacing variables under binders without capture checks or alpha-renaming;
> 5. using a quotient of the algebraic reduct without relation compatibility;
> 6. assuming a one-sorted encoding is definitionally identical to the many-sorted language;
> 7. treating a concrete presentation as the syntax object without specifying the isomorphism.

> [!theorem] Theorem 21.5: Consolidated soundness of the architecture
> Under the standing hypotheses of this note, the following data are mutually compatible:
>
> 1. the free many-sorted term algebra $\mathbf{Term}_{\mathcal L}$;
> 2. raw formula formation and alpha-quotienting;
> 3. capture-avoiding substitution;
> 4. term evaluation into the algebraic reduct of a structure;
> 5. satisfaction for formulas under sorted assignments;
> 6. semantic consequence over all nonempty many-sorted structures;
> 7. sound and complete classical deductive calculi with equality and sorted quantifier rules;
> 8. quotient and term-model constructions subject to congruence and relation-compatibility conditions;
> 9. presentation transfer through explicit isomorphisms.

> [!proof-sketch] Proof Sketch 21.5
> Items 1 and 4 are linked by the universal property of the free algebra. Items 2 and 3 are linked by alpha-equivalence and freshness for infinite variable supplies. Items 4 and 5 are linked by the recursive satisfaction clauses and the substitution lemma. Items 6 and 7 are linked by soundness and Henkin completeness. Item 8 is governed by the quotient well-definedness criterion. Item 9 follows by conjugating all constructions through specified isomorphisms.

### 21.2. Compact comparison table

| Object | Primitive input | Output | Governing condition |
|---|---:|---:|---|
| Term algebra | $S$, $\operatorname{Var}$, $\operatorname{Func}_{\mathcal L}$ | $\mathbf{Term}_{\mathcal L}$ | Free $\Sigma_{\mathcal L}$-algebra |
| Atomic formulas | terms, equality, relations | $\operatorname{Atom}_{\mathcal L}$ | Sort-matching profiles |
| Raw formulas | atoms, $\neg$, $\to$, $\forall_x$ | $\operatorname{Form}^{\mathrm{raw}}_{\mathcal L}$ | Least closed set |
| Binding-aware formulas | raw formulas | $\operatorname{Form}_{\mathcal L}$ | Quotient by $\equiv_{\alpha}$ |
| Structure | $\mathcal L$ | $\mathcal M$ | Nonempty sorted carriers and interpretations |
| Assignment | $\operatorname{Var}$, $M$ | $a$ | Sorted map $\operatorname{Var}\to M$ |
| Term evaluation | $\mathcal M$, $a$ | $t^{\mathcal M}[a]$ | Homomorphic extension |
| Satisfaction | $\mathcal M$, $a$, formula | truth value | Recursive clauses |
| Substructure | $\mathcal M\subseteq\mathcal N$ | inclusion | Function closure and relation restriction |
| Quotient | $\mathcal M$, $\theta$ | $\mathcal M/\theta$ | Function and relation compatibility |
| Calculus | axiom set, rules | $\vdash_{\mathsf C}$ | Finite derivations |
| Completeness | consistent theory | model | Henkin term model |



### 21.3. Formal dependency checklist

> [!remark] Remark 21.7: Dependency order of definitions
> The definitions in the core development have the following dependency order:
>
> $$
> S
> \prec
> S^{<\omega}
> \prec
> \mathcal L
> \prec
> \Sigma_{\mathcal L}
> \prec
> \mathbf{Term}_{\mathcal L}
> \prec
> \operatorname{Atom}_{\mathcal L}
> \prec
> \operatorname{Form}^{\mathrm{raw}}_{\mathcal L}
> \prec
> \equiv_{\alpha}
> \prec
> \operatorname{Form}_{\mathcal L}.
> $$
>
> Semantics has the separate dependency order
>
> $$
> \mathcal L
> \prec
> \mathcal M
> \prec
> a:\operatorname{Var}\to M
> \prec
> \operatorname{ev}^{\mathcal M}_a
> \prec
> \models_{\mathcal L}.
> $$
>
> No semantic object is used in the construction of terms or formulas.

> [!warning] Warning 21.8: Hypotheses not to suppress
> The following hypotheses are load-bearing and must be carried in later uses:
>
> 1. if $f\in\operatorname{Func}_{\mathcal L,w,s}$, then $f$ has exactly the input profile $w$ and output sort $s$;
> 2. if $R\in\operatorname{Rel}_{\mathcal L,w}$, then $R$ accepts exactly tuples from the product associated to $w$;
> 3. if $x\in\operatorname{Var}_s$, then $\forall x$ quantifies over $M_s$ and substitution for $x$ uses terms of sort $s$;
> 4. every structure in the main semantics has $M_s\neq\varnothing$ for every $s\in S$;
> 5. equality $=_s$ is the diagonal on $M_s$ and has no cross-sort instances;
> 6. quotient structures require both function congruence and relation compatibility;
> 7. completeness and compactness are stated for finitary syntax and finite derivations.

> [!remark] Remark 21.9: Minimal primitive-data principle
> The language datum does not include a truth-value object, proof system, class of structures, concrete syntax carrier, parser, set of contexts, set of schemas, definitional expansion, or one-sorted translation. Each of those is constructed later from, or imposed on, the primitive language datum. Adding any of them to the primitive data changes the object being defined.

> [!proposition] Proposition 21.10: Separation of functional and relational information
> Let $\mathcal M$ and $\mathcal N$ be $\mathcal L$-structures with the same sorted carriers and the same interpretations of every function symbol. Then for every assignment $a$ and every term $t$,
>
> $$
> t^{\mathcal M}[a]=t^{\mathcal N}[a].
> $$
>
> If there is a relation symbol $R$ such that
>
> $$
> R^{\mathcal M}\neq R^{\mathcal N},
> $$
>
> then there may exist an atomic formula $\alpha$ and assignment $a$ such that
>
> $$
> \mathcal M\models\alpha[a]
> \quad\text{and}\quad
> \mathcal N\not\models\alpha[a].
> $$

> [!proof-sketch] Proof Sketch 21.10
> The term claim is structural induction, since terms use only function symbols. If relation interpretations differ, choose a tuple in their symmetric difference and assign variables of the corresponding sorts to its coordinates; the associated relation atom separates satisfaction.

> [!proposition] Proposition 21.11: Formula-sort nonexistence in the core
> In the core language datum, there is no sort $\mathsf{Formula}\in S$ and no carrier $M_{\mathsf{Formula}}$ in an $\mathcal L$-structure. The expression
>
> $$
> \varphi\in\operatorname{Form}_{\mathcal L}
> $$
>
> is a metatheoretic assertion about syntax, whereas
>
> $$
> t\in\operatorname{Term}_{\mathcal L,s}
> $$
>
> identifies a term whose semantic value lies in $M_s$ under an assignment.

> [!proof-sketch] Proof Sketch 21.11
> This is an immediate consequence of the primitive data: $S$ indexes variables, terms, function profiles, and structure carriers. Formula formation is a separate inductive construction over atoms and logical constructors.

> [!warning] Warning 21.12: Schema variables are metalinguistic unless encoded
> A symbol such as $\Phi$ standing for an arbitrary formula in an axiom schema is not an object-language variable. It belongs to the parameter set $P$ of a schema record. To make formula variables object-level, one must add a separate higher-order or algebraic encoding, which is outside bare many-sorted first-order logic.



> [!proposition] Proposition 21.13: Later modules attach by explicit interfaces
> Each later module attaches to the core theory through one of the following mathematical interfaces:
>
> 1. a **presentation interface**, consisting of an isomorphism
>    $$
>    r:P\cong\operatorname{Syn}_{\mathcal L};
>    $$
> 2. a **semantic interface**, consisting of an $\mathcal L$-structure $\mathcal M$ and assignment $a:\operatorname{Var}\to M$;
> 3. a **proof interface**, consisting of a calculus datum $\mathsf C=(\operatorname{Ax}_{\mathsf C},\operatorname{Rule}_{\mathsf C})$;
> 4. a **schema interface**, consisting of a schema record
>    $$
>    \mathfrak S=(P,D,I);
>    $$
> 5. a **quotient interface**, consisting of a relation-compatible congruence $\theta$.
>
> Any construction not supplied through one of these interfaces is additional structure, not part of the bare many-sorted first-order language.

> [!proof-sketch] Proof Sketch 21.13
> Presentations act by transport along isomorphisms. Semantics acts by interpreting symbols in carriers and extending assignments. Proof theory acts by closure under finite rule applications. Schemas act by instance maps from side-condition domains. Quotients act only when the congruence makes functions and relations well-defined on classes. These interfaces exhaust the later constructions used above.

> [!warning] Warning 21.14: Do not move derived interfaces into primitive data
> Adding a parser, proof checker, schema registry, quotient relation, definitional extension, or intended model class to the language datum obscures the mathematical dependency order. Such data may be fixed for a project, but they are project-level enrichments of the language, not constituents of the many-sorted first-order signature itself.



> [!remark] Remark 21.15: Reading convention for later reuse
> When this note is used as a dependency, imported objects should be referenced by their defining data. For example, an assignment is not merely a function symbolically named $a$; it is a sorted map
>
> $$
> a_s:\operatorname{Var}_s\to M_s
> $$
>
> for every $s\in S$. A theorem that uses assignments, substitutions, reducts, or quotients should restate the corresponding domain, codomain, and compatibility hypotheses before invoking the result.

> [!remark] Remark 21.6: Final separation of roles
> The algebraic layer constructs and evaluates terms. The logical layer constructs formulas, manages binding, and defines truth. The model-theoretic layer studies classes of structures under satisfaction. The proof-theoretic layer studies derivations relative to specified axiom and rule data. These layers interact by explicit maps and theorems; none is identified with another.
