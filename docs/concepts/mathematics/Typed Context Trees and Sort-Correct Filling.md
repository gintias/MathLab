---
title: "Typed Context Trees and Sort-Correct Filling"
subtitle: "Many-sorted syntax trees, typed holes, context profiles, filling, extraction, and composition laws"
tags: [trees, typed-syntax, contexts, holes, many-sorted-algebra, sort-correctness, first-order-logic, substitution, syntax-trees, schema-records]
---

# Typed Context Trees and Sort-Correct Filling

## 0. Orientation

### 0.1. Purpose

The previous tree development gave the untyped infrastructure: finite address-tree domains, labelled trees, ranked labels, subtree extraction, grafting, replacement, and one-hole contexts. That is enough for ordinary term trees or propositional formula trees when there is only one syntactic category in view. But first-order logic immediately forces a refinement. A first-order syntax tree is not merely a tree whose nodes have the right number of children. It is a tree whose nodes have children of the right **sort**.

For example, a function symbol consumes terms and produces a term:

$$
f:	ext{Term}^n	o 	ext{Term}.
$$

A predicate symbol consumes terms and produces a formula:

$$
R:	ext{Term}^n	o 	ext{Formula}.
$$

A connective consumes formulas and produces a formula:

$$
\wedge:	ext{Formula},	ext{Formula}	o	ext{Formula}.
$$

So the next layer is not generic graph-theoretic tree theory. The next layer is **typed syntax-tree theory**: trees with labelled constructors whose input and output sorts are prescribed, together with holes that can be filled only by trees of matching sort.

### 0.2. Big Picture

The central object of this note is a typed context profile

$$
(s_0,\dots,s_{n-1})\Rightarrow s.
$$

This means:

> a context of output sort $s$ with $n$ holes, where hole $i$ expects input sort $s_i$.

If

$$
C:(s_0,\dots,s_{n-1})\Rightarrow s
$$

and if

$$
t_i:s_i
\qquad(0\le i<n),
$$

then filling gives a well-sorted tree

$$
C[t_0,\dots,t_{n-1}]:s.
$$

The first main theorem is therefore:

> [!theorem] Sort-correct filling
> Filling a sort-correct typed context with sort-correct inputs of the required sorts produces a sort-correct tree of the context's output sort.

The second main theorem is:

> [!theorem] Context composition laws
> Typed context composition is well-defined, sort-correct, associative, and has identity holes.

These two results are the mathematical backbone of schema instantiation. A schema is a typed context together with side conditions and an interpretation of its holes. Before binding, alpha-equivalence, or FOL substitution can be made rigorous, one needs this typed context calculus.

### 0.3. What this note does and does not do

This note does the following:

1. defines a set of syntactic sorts;
2. defines typed constructor signatures;
3. defines sort-correct typed trees;
4. defines typed holes and context profiles;
5. defines filling as typed substitution of holes by trees;
6. proves filling preserves sort correctness;
7. defines context extraction from a position;
8. defines context composition;
9. proves identity and associativity laws;
10. specializes the framework to first-order syntax.

This note does **not** yet solve binding. It treats quantifier nodes such as

$$
\forall_x:	ext{Formula}\to\text{Formula}
$$

as typed constructors. That is enough for sort correctness. It is not enough for capture-avoiding substitution or alpha-equivalence. Those belong to the next layer.

> [!warning] Boundary of this note
> Sort correctness answers: "Can this kind of object be inserted here?" It does not answer: "Will this insertion capture a free variable?" Binding-aware admissibility is a later side-condition layer.

---

## 1. Address-tree background

### 1.1. Address space

Let

$$
\mathbb A:=\mathbb N_{>0}^{<\omega}
$$

be the set of finite sequences of positive integers. The empty sequence is denoted

$$
\varepsilon.
$$

If $p\in\mathbb A$ and $i\in\mathbb N_{>0}$, write

$$
p\cdot i
$$

for the address obtained by appending $i$ to $p$. More generally, write $p\cdot q$ for concatenation of addresses.

### 1.2. Prefix order

For $p,q\in\mathbb A$, define

$$
p\preceq q
$$

iff there exists $r\in\mathbb A$ such that

$$
q=p\cdot r.
$$

Then $p$ is a prefix of $q$, or equivalently an ancestor address of $q$.

Write

$$
p\prec q
$$

iff $p\preceq q$ and $p\ne q$.

### 1.3. Finite address-tree domains

> [!definition] Finite address-tree domain
> A **finite address-tree domain** is a finite nonempty subset
>
> $$
> D\subseteq\mathbb A
> $$
>
> satisfying:
>
> 1. **prefix closure**: if $q\in D$ and $p\preceq q$, then $p\in D$;
> 2. **left-sibling closure**: if $p\cdot(i+1)\in D$, then $p\cdot i\in D$.

The root is $\varepsilon$. The $i$-th child of $p$ is $p\cdot i$, when that address belongs to $D$.

For $p\in D$, define the child-index set

$$
\operatorname{ch}_D(p):=\{i\in\mathbb N_{>0}:p\cdot i\in D\}.
$$

Because of left-sibling closure, there is a unique $k_p\in\mathbb N$ such that

$$
\operatorname{ch}_D(p)=\{1,\dots,k_p\}.
$$

The integer $k_p$ is the number of children of $p$.

---

## 2. Sorts and typed constructor signatures

### 2.1. Sort sets

> [!definition] Sort set
> A **sort set** is a set $\mathsf S$ whose elements are called **sorts**.

A sort is a syntactic category. For ordinary first-order syntax, a minimal choice is

$$
\mathsf S=\{\mathrm{Term},\mathrm{Formula}\}.
$$

For a proof system, one may enlarge this to

$$
\mathsf S=\{\mathrm{Term},\mathrm{Formula},\mathrm{Sequent},\mathrm{Proof}\}.
$$

For many-sorted first-order logic, where object-language terms themselves have object sorts, one usually refines the syntactic term sort into a family:

$$
\mathsf S=\{\mathrm{Term}_\tau:\tau\in\mathsf{ObjSort}\}\cup\{\mathrm{Formula}\}.
$$

> [!warning] Two meanings of "sort"
> There are two levels of sorting. First, there are **syntactic sorts** such as Term, Formula, Sequent, and Proof. Second, in many-sorted first-order logic, object-language terms may have **object sorts** such as GroupElement, FieldElement, or NaturalNumber. One can combine these by using syntactic sorts $\mathrm{Term}_\tau$ indexed by object sorts $\tau$.

### 2.2. Typed constructor profiles

In a ranked alphabet, a constructor only remembers how many children it has. In a typed signature, a constructor remembers the sorts of its children and the sort of its output.

> [!definition] Constructor profile
> Given a sort set $\mathsf S$, a **constructor profile** is an expression
>
> $$
> c:s_0,\dots,s_{n-1}\to s,
> $$
>
> where $n\in\mathbb N$, $s_0,\dots,s_{n-1},s\in\mathsf S$, and $c$ is a constructor symbol.

The finite list

$$
(s_0,\dots,s_{n-1})
$$

is the input profile of $c$, and $s$ is the output sort.

If $n=0$, then $c$ is a nullary constructor of sort $s$:

$$
c:()	o s.
$$

### 2.3. Typed signatures

> [!definition] Typed constructor signature
> A **typed constructor signature** over $\mathsf S$ is a set $\mathcal C$ of constructor symbols together with functions assigning to each $c\in\mathcal C$:
>
> 1. a natural number $\operatorname{ar}(c)$;
> 2. an input sort list
>    $$
>    \operatorname{in}(c)=(s_0,\dots,s_{n-1})\in\mathsf S^n;
>    $$
> 3. an output sort
>    $$
>    \operatorname{out}(c)\in\mathsf S.
>    $$

We write

$$
c:s_0,\dots,s_{n-1}\to s
$$

when

$$
\operatorname{in}(c)=(s_0,\dots,s_{n-1})
$$

and

$$
\operatorname{out}(c)=s.
$$

### 2.4. Relation with ranked alphabets

Every typed constructor signature has an underlying ranked alphabet by forgetting the sorts and remembering only arity:

$$
\rho(c)=\operatorname{ar}(c).
$$

But this forgetful move loses important information. For example, both symbols

$$
f:\mathrm{Term},\mathrm{Term}\to\mathrm{Term}
$$

and

$$
\wedge:\mathrm{Formula},\mathrm{Formula}\to\mathrm{Formula}
$$

have arity $2$, but they are not interchangeable. A term cannot be placed where a formula is expected.

> [!core] Arity correctness versus sort correctness
> Arity correctness says the node has the right number of children. Sort correctness says each child has the right kind, and the whole node has the declared output kind. Sort correctness strictly refines arity correctness.

---

## 3. Typed labelled trees

### 3.1. Labelled address trees

A labelled tree consists of a finite address-tree domain and a labelling function.

> [!definition] Labelled address tree
> Let $\mathcal C$ be a set of constructor symbols. A **$\mathcal C$-labelled address tree** is a pair
>
> $$
> \mathsf t=(D,\ell)
> $$
>
> where $D$ is a finite address-tree domain and
>
> $$
> \ell:D\to\mathcal C
> $$
>
> is a labelling function.

This is still not typed. It says which symbol labels each node, but it does not yet require children to have the sorts expected by the node label.

### 3.2. Sort assignment to nodes

Given a typed constructor signature, every label has an output sort. Therefore every labelled node has a candidate sort.

For a labelled tree $\mathsf t=(D,\ell)$, define

$$
\operatorname{sort}_{\mathsf t}(p):=\operatorname{out}(\ell(p)).
$$

This is the output sort of the subtree rooted at $p$, provided the tree is well-sorted.

### 3.3. Sort-correctness

> [!definition] Sort-correct typed tree
> Let $(\mathsf S,\mathcal C)$ be a typed constructor signature. A $\mathcal C$-labelled address tree
>
> $$
> \mathsf t=(D,\ell)
> $$
>
> is **sort-correct** if for every node $p\in D$, whenever
>
> $$
> \ell(p):s_0,\dots,s_{n-1}\to s,
> $$
>
> the following hold:
>
> 1. $p$ has exactly $n$ children:
>    $$
>    \operatorname{ch}_D(p)=\{1,\dots,n\};
>    $$
> 2. for each $0\le i<n$, the child $p\cdot(i+1)$ has output sort $s_i$:
>    $$
>    \operatorname{out}(\ell(p\cdot(i+1)))=s_i.
>    $$
>
> The output sort of the whole tree is
>
> $$
> \operatorname{out}(\mathsf t):=\operatorname{out}(\ell(\varepsilon)).
> $$

The child index is written $i+1$ because addresses use positive indices $1,2,\dots$, while sort lists are usually indexed from $0$.

### 3.4. Trees of a fixed sort

> [!definition] Carrier of trees of sort $s$
> For $s\in\mathsf S$, define
>
> $$
> \operatorname{Tree}_s(\mathcal C)
> $$
>
> to be the set of all finite sort-correct $\mathcal C$-labelled address trees of output sort $s$.

The total sorted family of trees is

$$
\operatorname{Tree}_{\mathsf S}(\mathcal C):=(\operatorname{Tree}_s(\mathcal C))_{s\in\mathsf S}.
$$

This is not one carrier but an $\mathsf S$-sorted family of carriers.

---

## 4. Typed tree constructors

### 4.1. Root grafting with sorts

Let

$$
c:s_0,\dots,s_{n-1}\to s
$$

be a typed constructor. Given sort-correct trees

$$
\mathsf t_i\in\operatorname{Tree}_{s_i}(\mathcal C)
\qquad(0\le i<n),
$$

define

$$
G_c(\mathsf t_0,\dots,\mathsf t_{n-1})
$$

by creating a fresh root labelled $c$ and attaching $\mathsf t_i$ as the $(i+1)$-st child.

If

$$
\mathsf t_i=(D_i,\ell_i),
$$

then the new domain is

$$
D=\{\varepsilon\}\cup\bigcup_{i=0}^{n-1}\{(i+1)\cdot p:p\in D_i\},
$$

and the new labelling is

$$
\ell(\varepsilon)=c,
$$

$$
\ell((i+1)\cdot p)=\ell_i(p).
$$

> [!proposition] Typed root grafting preserves sort correctness
> If $c:s_0,\dots,s_{n-1}\to s$ and $\mathsf t_i\in\operatorname{Tree}_{s_i}(\mathcal C)$ for each $i<n$, then
>
> $$
> G_c(\mathsf t_0,\dots,\mathsf t_{n-1})\in\operatorname{Tree}_s(\mathcal C).
> $$

> [!proof]
> The underlying domain is a finite address-tree domain by the ordinary grafting lemma. The root has exactly $n$ children, indexed $1,\dots,n$. For each $i<n$, the subtree attached at child $i+1$ has output sort $s_i$ by assumption. All non-root nodes lie inside one of the attached trees, and their local sort-correctness is inherited from the corresponding $\mathsf t_i$. Therefore the whole grafted tree is sort-correct, and its root output sort is $s$.

### 4.2. The many-sorted tree algebra

The constructors define operations between the sorted carriers:

$$
G_c:
\operatorname{Tree}_{s_0}(\mathcal C)\times\cdots\times
\operatorname{Tree}_{s_{n-1}}(\mathcal C)
\to
\operatorname{Tree}_s(\mathcal C).
$$

Thus the family

$$
(\operatorname{Tree}_s(\mathcal C))_{s\in\mathsf S}
$$

is a many-sorted algebra.

### 4.3. Unique decomposition

> [!proposition] Unique typed decomposition
> Suppose
>
> $$
> G_c(\mathsf t_0,\dots,\mathsf t_{n-1})
> =
> G_d(\mathsf u_0,\dots,\mathsf u_{m-1}).
> $$
>
> Then
>
> $$
> c=d,
> \qquad
> n=m,
> \qquad
> \mathsf t_i=\mathsf u_i\text{ for each }i<n.
> $$

> [!proof]
> Equality of labelled address trees gives equality of root labels, so $c=d$. Hence their arities agree, so $n=m$. The $i$-th input tree is recovered as the subtree at address $(i+1)$ of the grafted tree. Therefore $\mathsf t_i=\mathsf u_i$ for each $i<n$.

Unique decomposition is the no-confusion property that makes structural recursion and context operations well-defined.

---

## 5. Stage construction of typed trees

### 5.1. Nullary constructors

For each sort $s\in\mathsf S$, define

$$
T^s_0:=\{G_c(): c:()\to s\}.
$$

These are the one-node sort-correct trees of sort $s$.

### 5.2. Successor stages

Given sorted families

$$
(T^s_m)_{s\in\mathsf S},
$$

define

$$
T^s_{m+1}
:=
T^s_m
\cup
\{G_c(\mathsf t_0,\dots,\mathsf t_{n-1}):
 c:s_0,\dots,s_{n-1}\to s,
 \mathsf t_i\in T^{s_i}_m\}.
$$

Then set

$$
T^s_\omega:=\bigcup_{m<\omega}T^s_m.
$$

### 5.3. Generatedness theorem

> [!theorem] Stage construction yields all finite sort-correct trees
> For every sort $s\in\mathsf S$,
>
> $$
> T^s_\omega=\operatorname{Tree}_s(\mathcal C).
> $$

> [!proof]
> First, by induction on $m$, every element of $T^s_m$ is a finite sort-correct tree of sort $s$. The base stage contains only nullary one-node trees of sort $s$. The successor step follows from typed root grafting.
>
> Conversely, let $\mathsf t\in\operatorname{Tree}_s(\mathcal C)$. We prove $\mathsf t\in T^s_\omega$ by induction on height. If $\mathsf t$ has height $0$, then its root label is some nullary constructor $c:()\to s$, so $\mathsf t=G_c()\in T^s_0$. If $\mathsf t$ has positive height, write its root label as $c:s_0,\dots,s_{n-1}\to s$, and let $\mathsf t_i$ be the immediate subtree at child $i+1$. Each $\mathsf t_i$ has sort $s_i$ and smaller height. By the induction hypothesis, $\mathsf t_i\in T^{s_i}_\omega$. Since there are finitely many inputs, choose $m$ such that all $\mathsf t_i\in T^{s_i}_m$. Then $G_c(\mathsf t_0,\dots,\mathsf t_{n-1})\in T^s_{m+1}$. This tree is $\mathsf t$ by unique decomposition. Hence $\mathsf t\in T^s_\omega$.

### 5.4. Structural induction

> [!theorem] Structural induction for typed trees
> For each sort $s\in\mathsf S$, let $\mathcal P_s$ be a property of trees in $\operatorname{Tree}_s(\mathcal C)$. Suppose that for every constructor
>
> $$
> c:s_0,\dots,s_{n-1}\to s,
> $$
>
> whenever $\mathsf t_i\in\operatorname{Tree}_{s_i}(\mathcal C)$ and $\mathcal P_{s_i}(\mathsf t_i)$ holds for all $i<n$, then
>
> $$
> \mathcal P_s(G_c(\mathsf t_0,\dots,\mathsf t_{n-1}))
> $$
>
> holds. Then $\mathcal P_s(\mathsf t)$ holds for every $s$ and every $\mathsf t\in\operatorname{Tree}_s(\mathcal C)$.

This is simultaneous induction over all sorts.

### 5.5. Structural recursion

> [!theorem] Structural recursion for typed trees
> Let $(A_s)_{s\in\mathsf S}$ be an $\mathsf S$-sorted family of sets. For every constructor
>
> $$
> c:s_0,\dots,s_{n-1}\to s,
> $$
>
> suppose given a function
>
> $$
> h_c:A_{s_0}\times\cdots\times A_{s_{n-1}}\to A_s.
> $$
>
> Then there exists a unique sorted family of functions
>
> $$
> H_s:\operatorname{Tree}_s(\mathcal C)\to A_s
> $$
>
> such that
>
> $$
> H_s(G_c(\mathsf t_0,\dots,\mathsf t_{n-1}))
> =
> h_c(H_{s_0}(\mathsf t_0),\dots,H_{s_{n-1}}(\mathsf t_{n-1})).
> $$

This is the typed version of tree folds.

---

## 6. Typed holes

### 6.1. Hole declarations

A context is a tree with holes. In a typed setting, every hole must declare the sort of object it accepts.

> [!definition] Typed hole profile
> A **typed hole profile** is a finite list of sorts
>
> $$
> \Gamma=(s_0,\dots,s_{n-1}).
> $$
>
> Associated to $\Gamma$ is a set of hole symbols
>
> $$
> H_\Gamma:=\{\Box_0^{s_0},\dots,\Box_{n-1}^{s_{n-1}}\}.
> $$

The superscript indicates the required sort of the hole.

### 6.2. Holes as nullary constructors

To build contexts using the same tree machinery, treat each hole as a nullary constructor of its declared sort:

$$
\Box_i^{s_i}:()\to s_i.
$$

Given a base typed constructor signature $(\mathsf S,\mathcal C)$, define the extended signature

$$
\mathcal C[\Gamma]:=\mathcal C\sqcup H_\Gamma,
$$

where each hole is added as a fresh nullary constructor.

> [!warning] Holes must be fresh
> Hole symbols are not object-language variables unless explicitly identified with them. They are meta-syntactic placeholders. They should be taken disjoint from the ordinary constructor symbols.

### 6.3. Contexts with hole variables versus occurrence holes

There are two different notions that are often both called "holes."

**Hole variables** may occur many times. For example, in the propositional schema

$$
\Box_0\to(\Box_1\to\Box_0),
$$

the hole variable $\Box_0$ appears twice. Filling $\Box_0$ inserts the same formula in both places.

**Occurrence holes** are individual holes that occur exactly once. For example, a one-hole tree context extracted from a position has one distinguished hole occurrence.

Both notions are useful.

> [!convention] Contexts in this note
> Unless explicitly stated otherwise, $\Box_i^{s_i}$ is a **hole variable**, so it may occur zero, one, or many times inside a context. When a hole is required to occur exactly once, we call the context **linear** or **one-occurrence** in that hole.

This convention is important for schemas. Formula metavariables are hole variables, not necessarily unique hole occurrences.

---

## 7. Typed context profiles

### 7.1. Contexts as trees over an extended signature

> [!definition] Typed context
> Let $\Gamma=(s_0,\dots,s_{n-1})$ be a typed hole profile and let $s\in\mathsf S$. A **typed context of profile $\Gamma\Rightarrow s$** is a sort-correct tree
>
> $$
> C\in\operatorname{Tree}_s(\mathcal C[\Gamma]).
> $$
>
> We write
>
> $$
> C:(s_0,\dots,s_{n-1})\Rightarrow s.
> $$

Thus a context is just a well-sorted tree whose leaves may include typed holes.

### 7.2. Pure versus parameterized contexts

A context may be **pure**, meaning its only nullary symbols are holes, or **parameterized**, meaning it may also contain ordinary object-language symbols.

For example, in first-order syntax, the term context

$$
f(\Box^{\mathrm{Term}},a)
$$

has parameter $a$ and hole $\Box^{\mathrm{Term}}$.

The formula context

$$
\forall x\,(\Box^{\mathrm{Formula}}\to P(x))
$$

has parameters $x$ and $P$ and one formula hole.

> [!remark] Parameters are ordinary constructors
> In the tree representation, parameters are just ordinary constructor labels from the fixed signature. Holes are the special added nullary constructors waiting to be filled.

### 7.3. The identity context

For each sort $s\in\mathsf S$, define the one-hole identity context

$$
\mathbf 1_s:(s)\Rightarrow s
$$

as the one-node tree labelled by $\Box_0^s$.

Filling it with a tree $t:s$ returns $t$.

### 7.4. Projection contexts

More generally, for a profile

$$
\Gamma=(s_0,\dots,s_{n-1}),
$$

and an index $i<n$, the $i$-th projection context is the one-node tree

$$
\pi_i^\Gamma:(s_0,\dots,s_{n-1})\Rightarrow s_i
$$

labelled by $\Box_i^{s_i}$.

It returns the $i$-th input.

---

## 8. Filling typed contexts

### 8.1. Filling data

Let

$$
C:(s_0,\dots,s_{n-1})\Rightarrow s.
$$

A filling for $C$ consists of trees

$$
\mathsf t_i\in\operatorname{Tree}_{s_i}(\mathcal C)
\qquad(0\le i<n).
$$

The result should be a tree

$$
C[\mathsf t_0,\dots,\mathsf t_{n-1}]\in\operatorname{Tree}_s(\mathcal C).
$$

### 8.2. Recursive definition of filling

Filling is defined by structural recursion on the context tree.

If the context is a hole leaf $\Box_i^{s_i}$, define

$$
\Box_i^{s_i}[\mathsf t_0,\dots,\mathsf t_{n-1}]
:=
\mathsf t_i.
$$

If the context has root constructor

$$
c:r_0,\dots,r_{m-1}\to r
$$

from the original signature $\mathcal C$, with immediate subcontexts

$$
C_j:(s_0,\dots,s_{n-1})\Rightarrow r_j,
$$

then define

$$
G_c(C_0,\dots,C_{m-1})[\mathsf t_0,\dots,\mathsf t_{n-1}]
:=
G_c(C_0[\vec{\mathsf t}],\dots,C_{m-1}[\vec{\mathsf t}]).
$$

Here

$$
\vec{\mathsf t}=(\mathsf t_0,\dots,\mathsf t_{n-1}).
$$

This definition simply says: recursively fill the holes in the subcontexts, then rebuild the root.

### 8.3. Filling as homomorphic extension

Equivalently, filling is a homomorphic extension. The hole assignment

$$
\theta:H_\Gamma\to\bigcup_{s\in\mathsf S}\operatorname{Tree}_s(\mathcal C)
$$

is defined by

$$
\theta(\Box_i^{s_i})=\mathsf t_i.
$$

It is sort-respecting because $\mathsf t_i$ has sort $s_i$. The unique many-sorted homomorphic extension sends the context tree $C$ to its filled tree.

Thus:

$$
C[\vec{\mathsf t}]=\widehat\theta(C).
$$

> [!core] Filling is substitution
> Typed context filling is exactly many-sorted substitution of typed holes by typed trees.

### 8.4. Main theorem: filling preserves sort correctness

> [!theorem] Sort-correct filling
> Let
>
> $$
> C:(s_0,\dots,s_{n-1})\Rightarrow s
> $$
>
> be a typed context. If
>
> $$
> \mathsf t_i\in\operatorname{Tree}_{s_i}(\mathcal C)
> \qquad(0\le i<n),
> $$
>
> then
>
> $$
> C[\mathsf t_0,\dots,\mathsf t_{n-1}]
> \in
> \operatorname{Tree}_s(\mathcal C).
> $$

> [!proof]
> We prove the claim by structural induction on $C$.
>
> If $C$ is the hole leaf $\Box_i^{s_i}$, then
>
> $$
> C[\mathsf t_0,\dots,\mathsf t_{n-1}]=\mathsf t_i,
> $$
>
> which belongs to $\operatorname{Tree}_{s_i}(\mathcal C)$. Since the output sort of this context is $s_i$, the result has the required sort.
>
> Otherwise, $C$ has the form
>
> $$
> C=G_c(C_0,\dots,C_{m-1}),
> $$
>
> where
>
> $$
> c:r_0,\dots,r_{m-1}\to s,
> $$
>
> and each
>
> $$
> C_j:(s_0,\dots,s_{n-1})\Rightarrow r_j.
> $$
>
> By the induction hypothesis,
>
> $$
> C_j[\mathsf t_0,\dots,\mathsf t_{n-1}]
> \in
> \operatorname{Tree}_{r_j}(\mathcal C)
> $$
>
> for each $j<m$. Typed root grafting then gives
>
> $$
> G_c(C_0[\vec{\mathsf t}],\dots,C_{m-1}[\vec{\mathsf t}])
> \in
> \operatorname{Tree}_s(\mathcal C).
> $$
>
> By the recursive definition of filling, this is exactly $C[\vec{\mathsf t}]$. Hence filling preserves sort correctness.

### 8.5. Multiple occurrences of a hole

If a hole variable occurs more than once, filling duplicates the same input tree at every occurrence.

For example, if

$$
C(\Box_0,\Box_1)=\Box_0\to(\Box_1\to\Box_0),
$$

then

$$
C[\alpha,\beta]=\alpha\to(\beta\to\alpha).
$$

The two occurrences of $\Box_0$ receive the same filled formula $\alpha$.

This is why contexts over hole variables naturally represent schematic formula patterns.

---

## 9. Replacement and extracted one-hole contexts

### 9.1. Subtrees in typed trees

Let

$$
\mathsf t=(D,\ell)\in\operatorname{Tree}_s(\mathcal C)
$$

and let $p\in D$. The subtree at $p$ is

$$
\mathsf t\downarrow p=(D_p,\ell_p),
$$

where

$$
D_p=\{q\in\mathbb A:p\cdot q\in D\},
$$

and

$$
\ell_p(q)=\ell(p\cdot q).
$$

Its output sort is

$$
\operatorname{out}(\mathsf t\downarrow p)=\operatorname{out}(\ell(p)).
$$

> [!proposition] Subtrees preserve sort correctness
> If $\mathsf t\in\operatorname{Tree}_s(\mathcal C)$ and $p\in D_{\mathsf t}$, then
>
> $$
> \mathsf t\downarrow p\in\operatorname{Tree}_{\operatorname{out}(\ell(p))}(\mathcal C).
> $$

The proof is inherited local sort-correctness below $p$.

### 9.2. Extracted one-hole context

Given a tree $\mathsf t:s$ and a position $p$ whose subtree has sort $r$, one can replace that subtree by a fresh hole $\Box^r$.

> [!definition] Extracted one-hole context
> Let $\mathsf t\in\operatorname{Tree}_s(\mathcal C)$ and $p\in D_{\mathsf t}$. Let
>
> $$
> r:=\operatorname{out}(\ell(p)).
> $$
>
> The **context extracted from $\mathsf t$ at $p$** is the one-hole context
>
> $$
> C_{\mathsf t,p}:(r)\Rightarrow s
> $$
>
> obtained by replacing the entire subtree rooted at $p$ by a hole $\Box^r$.

Formally, the extracted context has domain

$$
D_C=\{q\in D_{\mathsf t}:p\npreceq q\}\cup\{p\},
$$

with label

$$
\ell_C(p)=\Box^r,
$$

and

$$
\ell_C(q)=\ell(q)
$$

for $q\in D_C\setminus\{p\}$.

### 9.3. Reconstruction theorem

> [!theorem] Context-subtree reconstruction
> Let $\mathsf t:s$ be a sort-correct tree and $p\in D_{\mathsf t}$. If $r$ is the sort of the subtree $\mathsf t\downarrow p$, then
>
> $$
> C_{\mathsf t,p}[\mathsf t\downarrow p]=\mathsf t.
> $$

> [!proof-sketch]
> Outside the replaced subtree, the extracted context agrees with $\mathsf t$. At the hole address $p$, filling inserts exactly the removed subtree. Therefore the resulting domain and labelling agree with $\mathsf t$ at every address.

### 9.4. Sort-correct replacement at a position

If $\mathsf u:r$ is any tree of the same sort as $\mathsf t\downarrow p$, define

$$
\mathsf t[p:=\mathsf u]:=C_{\mathsf t,p}[\mathsf u].
$$

> [!corollary] Sort-correct replacement
> If $\mathsf t:s$, $p\in D_{\mathsf t}$, and $\mathsf u$ has the same sort as $\mathsf t\downarrow p$, then
>
> $$
> \mathsf t[p:=\mathsf u]:s.
> $$

This is the typed version of raw replacement.

> [!warning] Replacement is not capture avoidance
> In FOL, replacing a formula subtree inside the scope of a quantifier may bind variables that were free in the inserted formula. Sort-correct replacement only guarantees that formulas go in formula positions and terms go in term positions. Binding safety requires additional side conditions.

---

## 10. Context composition

### 10.1. Why composition is needed

Contexts are operations on syntax. Therefore they should compose.

If

$$
C:(s_0,\dots,s_{n-1})\Rightarrow s
$$

and each hole $i$ is filled not by an ordinary tree but by another context

$$
D_i:\Delta_i\Rightarrow s_i,
$$

then the result is a new context of output sort $s$ whose holes are the holes of all the $D_i$.

This is context composition.

### 10.2. Profiles and concatenation

Let

$$
\Gamma=(s_0,\dots,s_{n-1})
$$

be the input profile of $C$.

For each $i<n$, let

$$
\Delta_i=(r_{i,0},\dots,r_{i,k_i-1})
$$

be the input profile of $D_i$.

The composite profile is the concatenation

$$
\Delta_0\oplus\cdots\oplus\Delta_{n-1}.
$$

Explicitly,

$$
\Delta_0\oplus\cdots\oplus\Delta_{n-1}
=
(r_{0,0},\dots,r_{0,k_0-1},r_{1,0},\dots,r_{n-1,k_{n-1}-1}).
$$

### 10.3. Renaming holes before composition

To avoid collisions, contexts being composed should have disjoint hole symbols. The cleanest convention is to reindex all holes of $D_i$ into the appropriate block of the concatenated profile.

Let

$$
K_i:=k_0+\cdots+k_{i-1}.
$$

Then the $j$-th hole of $D_i$ becomes the $(K_i+j)$-th hole of the composite profile.

This is only bookkeeping, but it is important for formal equality.

### 10.4. Simultaneous composition

> [!definition] Simultaneous context composition
> Let
>
> $$
> C:(s_0,\dots,s_{n-1})\Rightarrow s
> $$
>
> and
>
> $$
> D_i:\Delta_i\Rightarrow s_i
> \qquad(0\le i<n).
> $$
>
> The **simultaneous composite**
>
> $$
> C[D_0,\dots,D_{n-1}]
> $$
>
> is the context
>
> $$
> C[D_0,\dots,D_{n-1}]:
> \Delta_0\oplus\cdots\oplus\Delta_{n-1}\Rightarrow s
> $$
>
> obtained by filling the $i$-th hole of $C$ with the context $D_i$, after block-renaming the holes of each $D_i$.

This is the same operation as filling, but the fillers are themselves contexts rather than closed trees.

### 10.5. Sort correctness of composition

> [!theorem] Context composition preserves sort correctness
> If
>
> $$
> C:(s_0,\dots,s_{n-1})\Rightarrow s
> $$
>
> and
>
> $$
> D_i:\Delta_i\Rightarrow s_i
> $$
>
> for each $i<n$, then
>
> $$
> C[D_0,\dots,D_{n-1}]:
> \Delta_0\oplus\cdots\oplus\Delta_{n-1}\Rightarrow s.
> $$

> [!proof-sketch]
> Treat each $D_i$ as a sort-correct tree of output sort $s_i$ in the extended signature whose holes are the composite-profile holes. Since $D_i$ has exactly the output sort expected by hole $i$ of $C$, the sort-correct filling theorem applies. The result has output sort $s$ and holes exactly those in the concatenated profile.

### 10.6. Partial composition

Sometimes one plugs a context into a single hole and leaves the other holes alone.

Suppose

$$
C:(s_0,\dots,s_{n-1})\Rightarrow s
$$

and

$$
D:(r_0,\dots,r_{m-1})\Rightarrow s_i.
$$

Then the partial composite

$$
C\circ_i D
$$

has profile

$$
(s_0,\dots,s_{i-1},r_0,\dots,r_{m-1},s_{i+1},\dots,s_{n-1})\Rightarrow s.
$$

It is obtained by replacing the $i$-th hole of $C$ by $D$.

### 10.7. Identity laws

> [!theorem] Identity laws
> Let
>
> $$
> C:(s_0,\dots,s_{n-1})\Rightarrow s.
> $$
>
> For each $i<n$, let $\pi_i^\Gamma$ be the $i$-th projection context. Then
>
> $$
> C[\pi_0^\Gamma,\dots,\pi_{n-1}^\Gamma]=C.
> $$
>
> Also, if $D:(\Delta)\Rightarrow s_i$, then
>
> $$
> \mathbf 1_{s_i}[D]=D.
> $$

> [!proof-sketch]
> Filling each hole of $C$ by the corresponding projection hole changes nothing. Filling the identity context by $D$ returns $D$ because the identity context is just a single hole.

### 10.8. Associativity law

> [!theorem] Associativity of context composition
> Let
>
> $$
> C:(s_0,\dots,s_{n-1})\Rightarrow s,
> $$
>
> let
>
> $$
> D_i:\Delta_i\Rightarrow s_i,
> $$
>
> and for every hole of every $D_i$, let $E_{i,j}$ be a context of the appropriate sort. Then, after the canonical reindexing of holes,
>
> $$
> (C[D_0,\dots,D_{n-1}])[E_{0,0},\dots,E_{n-1,k_{n-1}-1}]
> =
> C[D_0[E_{0,0},\dots],\dots,D_{n-1}[E_{n-1,0},\dots]].
> $$

> [!proof-sketch]
> Both sides are obtained by replacing each hole occurrence of $C$ with the corresponding $D_i$, and then replacing each hole occurrence of each $D_i$ with the corresponding $E_{i,j}$. The order of carrying out these replacements does not affect the final labelled address tree, provided hole reindexing is performed consistently. A formal proof is by structural induction on $C$.

### 10.9. Clone and multicategory intuition

The family of all typed contexts with profiles

$$
(s_0,\dots,s_{n-1})\Rightarrow s
$$

forms a typed clone-like or multicategory-like structure:

- sorts are objects;
- contexts are multi-input operations;
- identity holes are identity operations;
- context composition is multi-operation composition.

One does not need this vocabulary immediately, but the structure is already present.

---

## 11. First-order syntax as typed trees

### 11.1. One-sorted first-order language

Fix a one-sorted first-order language $\mathcal L$ with:

- variables $x,y,z,\dots$;
- constant symbols $c,d,\dots$;
- function symbols $f\in\operatorname{Func}_n(\mathcal L)$;
- relation symbols $R\in\operatorname{Rel}_n(\mathcal L)$;
- equality, optionally;
- logical connectives;
- quantifiers.

For the syntactic sort set, take

$$
\mathsf S_{\mathrm{FOL}}=\{\mathrm{Term},\mathrm{Formula}\}.
$$

### 11.2. Term constructors

Each variable $x$ is a nullary term constructor:

$$
x:()\to\mathrm{Term}.
$$

Each constant $c$ is a nullary term constructor:

$$
c:()\to\mathrm{Term}.
$$

Each $n$-ary function symbol $f$ gives a constructor

$$
f:\underbrace{\mathrm{Term},\dots,\mathrm{Term}}_{n}\to\mathrm{Term}.
$$

### 11.3. Atomic formula constructors

Each $n$-ary relation symbol $R$ gives

$$
R:\underbrace{\mathrm{Term},\dots,\mathrm{Term}}_{n}\to\mathrm{Formula}.
$$

Equality gives

$$
=:\mathrm{Term},\mathrm{Term}\to\mathrm{Formula}.
$$

### 11.4. Logical constructors

For connectives:

$$
\neg:\mathrm{Formula}\to\mathrm{Formula},
$$

$$
\wedge,\vee,\to,\leftrightarrow:
\mathrm{Formula},\mathrm{Formula}\to\mathrm{Formula}.
$$

For each variable $x$, treat quantifiers as constructors

$$
\forall_x:\mathrm{Formula}\to\mathrm{Formula},
$$

$$
\exists_x:\mathrm{Formula}\to\mathrm{Formula}.
$$

This gives the correct sort profile. Binding behavior will be added later.

### 11.5. Examples of sort-correct and malformed trees

The term

$$
f(g(x),c)
$$

is a sort-correct Term tree if

$$
g:\mathrm{Term}\to\mathrm{Term},
\qquad
f:\mathrm{Term},\mathrm{Term}\to\mathrm{Term}.
$$

The formula

$$
R(f(x),c)\to\forall y\,S(y)
$$

is a sort-correct Formula tree.

But the expression

$$
f(R(x),c)
$$

is malformed because $f$ expects a term as first input, while $R(x)$ is a formula.

Likewise,

$$
R(x\wedge y)
$$

is malformed because $\wedge$ expects formulas, while $x$ and $y$ are terms.

### 11.6. FOL contexts

A term context:

$$
D(\Box^{\mathrm{Term}})=f(g(\Box),a)
$$

has profile

$$
(\mathrm{Term})\Rightarrow\mathrm{Term}.
$$

A formula context:

$$
C(\Box^{\mathrm{Formula}})=\forall x\,(\Box\to P(x))
$$

has profile

$$
(\mathrm{Formula})\Rightarrow\mathrm{Formula}.
$$

A mixed formula context:

$$
E(\Box_0^{\mathrm{Term}},\Box_1^{\mathrm{Formula}})
=
R(\Box_0)\to\Box_1
$$

has profile

$$
(\mathrm{Term},\mathrm{Formula})\Rightarrow\mathrm{Formula}.
$$

Filling with

$$
t:\mathrm{Term},
\qquad
\varphi:\mathrm{Formula}
$$

gives

$$
E[t,\varphi]=R(t)\to\varphi,
$$

which is sort-correct.

---

## 12. Many-sorted object-language terms

### 12.1. Object sorts

If the object language itself is many-sorted, let $\mathsf O$ be the set of object sorts. For each object sort $\tau\in\mathsf O$, introduce a syntactic sort

$$
\mathrm{Term}_\tau.
$$

Then set

$$
\mathsf S=\{\mathrm{Term}_\tau:\tau\in\mathsf O\}\cup\{\mathrm{Formula}\}.
$$

### 12.2. Many-sorted function symbols

A function symbol has profile

$$
f:\tau_0,\dots,	au_{n-1}\to\tau
$$

at the object-language level. It becomes a syntax constructor

$$
f:
\mathrm{Term}_{\tau_0},\dots,\mathrm{Term}_{\tau_{n-1}}
\to
\mathrm{Term}_{\tau}.
$$

### 12.3. Many-sorted relation symbols

A relation symbol with argument sorts

$$
R:\tau_0,\dots,	au_{n-1}
$$

becomes

$$
R:
\mathrm{Term}_{\tau_0},\dots,\mathrm{Term}_{\tau_{n-1}}
\to
\mathrm{Formula}.
$$

Equality is usually sorted:

$$
=_{\tau}:\mathrm{Term}_{\tau},\mathrm{Term}_{\tau}\to\mathrm{Formula}.
$$

### 12.4. Many-sorted typed holes

A term hole must specify the object sort:

$$
\Box^{\mathrm{Term}_\tau}.
$$

A formula hole remains

$$
\Box^{\mathrm{Formula}}.
$$

Thus the context

$$
f(\Box^{\mathrm{Term}_\tau})
$$

is only well-sorted if $f$ expects an argument of object sort $\tau$.

---

## 13. Sequent and proof contexts

### 13.1. Adding sequents as a sort

For proof theory, one often adds a syntactic sort

$$
\mathrm{Sequent}.
$$

A sequent constructor may take finite lists of formulas. One possible representation is to treat contexts $\Gamma,\Delta$ as finite sequences or finite multisets of formulas and define a constructor

$$
\Rightarrow:
\mathrm{FormList},\mathrm{FormList}\to\mathrm{Sequent}.
$$

If one wants to keep the sort set smaller, one may encode sequents as separate record objects rather than syntax trees. But if proof trees are being treated uniformly, a sequent sort is useful.

### 13.2. Proof trees as typed trees

A proof rule with premise sequents

$$
J_0,\dots,J_{n-1}
$$

and conclusion sequent $J$ gives a proof constructor

$$
\mathsf R:\mathrm{Proof}_{J_0},\dots,\mathrm{Proof}_{J_{n-1}}\to\mathrm{Proof}_J
$$

if using dependent proof sorts, or more simply

$$
\mathsf R:\mathrm{Proof},\dots,\mathrm{Proof}\to\mathrm{Proof}
$$

with decorations recording premise and conclusion sequents.

The dependent version is more precise; the decorated version is simpler.

### 13.3. Proof contexts

A proof context is a proof tree with proof holes. It has a profile such as

$$
(\mathrm{Proof},\mathrm{Proof})\Rightarrow\mathrm{Proof}.
$$

In a fully typed proof calculus, holes may carry expected judgments:

$$
\Box^{\mathrm{Proof}(\Gamma\Rightarrow\Delta)}.
$$

That belongs to the later proof-record layer, but the same typed-context idea is already visible.

---

## 14. Schema records and typed contexts

### 14.1. Why typed contexts are needed for schemas

A schema is not just a string with blanks. It must know what sort of object each blank accepts.

For example, universal instantiation has informal shape

$$
\forall x\,\varphi\to \varphi[x:=t].
$$

Here:

- $x$ ranges over variables;
- $t$ ranges over terms;
- $\varphi$ ranges over formulas;
- the output is a formula;
- there is a side condition: $t$ must be free for $x$ in $\varphi$.

Typed contexts handle the term/formula distinction. Binding-aware substitution and side conditions handle the rest.

### 14.2. Propositional tautology schema as typed context

In propositional logic, there is only one main sort:

$$
\mathrm{Formula}.
$$

A tautological schema context

$$
C:(\mathrm{Formula},\dots,\mathrm{Formula})\Rightarrow\mathrm{Formula}
$$

can be filled by arbitrary formulas. Sort correctness is automatic because all holes and all fillers have sort Formula.

The proposition that every filling of a tautological context is valid belongs to the quotient Boolean algebra layer. But the fact that every filling is a formula belongs to the typed context layer.

### 14.3. FOL axiom schemas

For FOL, a schema record should include:

1. a metavariable profile;
2. typed hole declarations;
3. a typed template/context;
4. an admissible filling class;
5. side conditions;
6. an instance map;
7. a soundness theorem.

Typed context trees supply items 2, 3, and the sort-correctness part of item 6.

The next binding-aware layer supplies the side-condition machinery.

---

## 15. Matching typed contexts

### 15.1. Matching problem

Given a context

$$
C:(s_0,\dots,s_{n-1})\Rightarrow s
$$

and a tree

$$
\mathsf u:s,
$$

a matching problem asks whether there exist trees

$$
\mathsf t_i:s_i
$$

such that

$$
C[\mathsf t_0,\dots,\mathsf t_{n-1}]=\mathsf u.
$$

If so, the tuple $(\mathsf t_0,\dots,\mathsf t_{n-1})$ is a filling that realizes $\mathsf u$ as an instance of $C$.

### 15.2. Typed matching is sort-filtered

A formula hole cannot match a term subtree. A term hole cannot match a formula subtree.

Thus sort profiles drastically reduce ambiguity and rule out malformed matches before deeper syntactic comparison begins.

### 15.3. Repeated holes impose equality constraints

If the same hole variable occurs twice, matching requires the same subtree at both occurrences.

For example, the schema

$$
\Box_0\to(\Box_1\to\Box_0)
$$

matches

$$
P(a)\to((Q(b)\wedge R(c))\to P(a))
$$

with

$$
\Box_0\mapsto P(a),
\qquad
\Box_1\mapsto Q(b)\wedge R(c).
$$

It does not match

$$
P(a)\to((Q(b)\wedge R(c))\to S(a))
$$

unless $P(a)=S(a)$ in the equality relation being used.

This is where later quotient layers may matter: matching raw syntax, matching modulo alpha-equivalence, and matching modulo definitional equality are different problems.

---

## 16. Rewriting under typed contexts

### 16.1. Typed rewrite rules

A typed rewrite rule has the form

$$
L\to R
$$

where $L$ and $R$ have the same sort:

$$
L,R:s.
$$

The same-sort condition is required so that replacing $L$ by $R$ preserves sort correctness.

### 16.2. Contextual closure

A rewrite rule can be applied inside any context expecting sort $s$:

$$
C:(s)\Rightarrow r.
$$

Then

$$
C[L]\to C[R].
$$

More generally, with substitutions or schema matching,

$$
C[L\sigma]\to C[R\sigma].
$$

### 16.3. Sort preservation of rewriting

> [!proposition] Typed rewriting preserves sorts
> If $L,R:s$ and $C:(s)\Rightarrow r$, then both $C[L]$ and $C[R]$ have sort $r$.

> [!proof]
> Apply sort-correct filling to $C$ with filler $L:s$, and again with filler $R:s$.

This is a small theorem, but it is the formal reason that typed rewrite systems do not produce malformed syntax.

---

## 17. Quotient contexts preview

### 17.1. Congruences on typed syntax

A sorted equivalence relation $\equiv$ consists of an equivalence relation $\equiv_s$ on each carrier $\operatorname{Tree}_s(\mathcal C)$.

It is a congruence if, whenever

$$
\mathsf t_i\equiv_{s_i}\mathsf u_i
$$

for all $i<n$, and

$$
c:s_0,\dots,s_{n-1}\to s,
$$

then

$$
G_c(\mathsf t_0,\dots,\mathsf t_{n-1})
\equiv_s
G_c(\mathsf u_0,\dots,\mathsf u_{n-1}).
$$

### 17.2. Contexts preserve congruence

> [!proposition] Contexts preserve congruent fillings
> Let $\equiv$ be a congruence on typed syntax. If
>
> $$
> C:(s_0,\dots,s_{n-1})\Rightarrow s
> $$
>
> and
>
> $$
> \mathsf t_i\equiv_{s_i}\mathsf u_i
> $$
>
> for all $i<n$, then
>
> $$
> C[\mathsf t_0,\dots,\mathsf t_{n-1}]
> \equiv_s
> C[\mathsf u_0,\dots,\mathsf u_{n-1}].
> $$

> [!proof-sketch]
> Induct on the context $C$. If $C$ is a hole, the claim is one of the assumptions. If $C$ is built by a constructor, apply the induction hypothesis to the immediate subcontexts and then use congruence compatibility of the constructor.

This is the typed version of the fact that contexts are polynomial operations and congruences are stable under polynomial operations.

### 17.3. Quotient contexts

Once a congruence is fixed, context operations descend to quotient syntax:

$$
[C]([\mathsf t_0],\dots,[\mathsf t_{n-1}])
:=
[C[\mathsf t_0,\dots,\mathsf t_{n-1}]].
$$

This is well-defined by the previous proposition.

For propositional logic modulo tautological equivalence, this is exactly the quotient-context calculus in which tautological contexts become top-valued Boolean polynomial operations.

For FOL, likely quotient relations include alpha-equivalence, definitional equality, and logical equivalence modulo a theory.

---

## 18. Pitfalls and boundary cases

### 18.1. Arities are not enough

A binary connective and a binary function symbol both have arity $2$, but their input and output sorts differ. A ranked tree can be arity-correct while still being sort-wrong.

### 18.2. Holes are not variables by default

A hole $\Box^{\mathrm{Formula}}$ is a meta-syntactic placeholder for formulas. It is not an object-language variable. A term hole $\Box^{\mathrm{Term}}$ is not necessarily a variable term either; it can be filled by any term.

### 18.3. Repeated holes are not repeated occurrences unless specified

If a hole variable appears twice, both occurrences receive the same filler. If one wants two independently fillable sites, use two hole variables. If one wants exactly one occurrence, impose linearity.

### 18.4. Sort-correct filling can still capture variables

The formula context

$$
C(\Box)=\forall x\,\Box
$$

is sort-correct. Filling it with $P(x)$ gives

$$
\forall x\,P(x),
$$

which is also sort-correct. But a free occurrence of $x$ in $P(x)$ has become bound. This is not a sort error. It is a binding issue.

### 18.5. Context equality depends on the chosen level

Raw contexts may differ syntactically but induce the same quotient operation. For example, in propositional logic,

$$
\Box_0\wedge\Box_1
$$

and

$$
\Box_1\wedge\Box_0
$$

are different raw contexts but equivalent modulo tautological equivalence.

### 18.6. Matching depends on equality convention

Matching raw syntax, matching modulo alpha-equivalence, and matching modulo logical equivalence are different tasks. A kernel must state which equality relation it uses.

---

## 19. Checklist

- A **sort set** $\mathsf S$ lists syntactic categories such as Term, Formula, Sequent, and Proof.
- A typed constructor has profile
  $$
  c:s_0,\dots,s_{n-1}\to s.
  $$
- A typed tree is **sort-correct** when each node has children whose output sorts match the input profile of the node label.
- $\operatorname{Tree}_s(\mathcal C)$ is the carrier of sort-correct trees of output sort $s$.
- Typed root grafting defines operations
  $$
  G_c:\operatorname{Tree}_{s_0}\times\cdots\times\operatorname{Tree}_{s_{n-1}}\to\operatorname{Tree}_s.
  $$
- A typed hole profile
  $$
  \Gamma=(s_0,\dots,s_{n-1})
  $$
  gives holes $\Box_i^{s_i}$.
- A typed context of profile $\Gamma\Rightarrow s$ is a sort-correct tree over the extended signature $\mathcal C[\Gamma]$ of output sort $s$.
- Filling a context is many-sorted substitution of holes by trees.
- Filling preserves sort correctness:
  $$
  C:(s_0,\dots,s_{n-1})\Rightarrow s,
  \quad
  t_i:s_i
  \implies
  C[t_0,\dots,t_{n-1}]:s.
  $$
- Context extraction at a position gives a one-hole context, and plugging the removed subtree reconstructs the original tree.
- Context composition is typed filling by contexts and satisfies identity and associativity laws.
- Typed rewriting preserves sorts when both sides of a rewrite rule have the same sort.
- Congruences compatible with constructors are automatically compatible with contexts.

---

## 20. Final synthesis

Typed context trees are the disciplined version of "syntax with holes." The untyped tree theory says that a tree has a shape, labels, subtrees, and grafting operations. The typed theory adds one decisive piece of data:

$$
\text{every constructor has an input-output sort profile.}
$$

That one addition turns informal template filling into a theorem. If

$$
C:(s_0,\dots,s_{n-1})\Rightarrow s
$$

and

$$
t_i:s_i,
$$

then

$$
C[t_0,\dots,t_{n-1}]:s.
$$

This is the sort-correctness backbone behind formula contexts, term contexts, sequent contexts, proof contexts, schema instances, and typed rewriting. It does not yet handle binding, capture avoidance, or alpha-equivalence. But it gives the exact structural interface those later layers need.

The conceptual dependency is:

$$
\boxed{
\text{typed constructors}
\to
\text{typed trees}
\to
\text{typed holes}
\to
\text{typed contexts}
\to
\text{sort-correct filling}
\to
\text{context composition}.
}
$$

Once this layer is in place, the FOL-specific layers can be added cleanly:

$$
\boxed{
\text{binding}
\to
\alpha\text{-equivalence}
\to
\text{capture-avoiding substitution}
\to
\text{schema records}
\to
\text{matching and rewriting}
\to
\text{quotients}.
}
$$

The guiding slogan is:

$$
\boxed{
\text{typed contexts are syntax-tree operations with checked input and output sorts.}
}
$$
