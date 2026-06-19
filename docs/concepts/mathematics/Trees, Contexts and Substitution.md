---
title: "Trees, Tree Algebras, Contexts, Substitution, and Rewriting"
subtitle: "A treatise on finite trees as mathematical objects: presentations, anatomy, the address model, ranked and typed trees, tree algebras and freeness, the calculus of subtrees, replacement, contexts, plugging, substitution, matching, rewriting systems, rewriting metatheory, congruences, normal forms, quotient tree algebras, and adjacent theories"
tags: [trees, tree-algebra, free-algebra, contexts, plugging, substitution, matching, rewriting, term-rewriting, confluence, termination, congruence, quotient, normal-forms, tree-automata, tree-transducers, operads, term-graphs, dag, infinite-trees, coalgebra, syntax, universal-algebra]
---

# Trees, Tree Algebras, Contexts, Substitution, and Rewriting

## 0. Orientation

### 0.1. Aim and Standing Object

This treatise develops the theory of finite trees as mathematical objects in their own right and then erects upon them a disciplined **tree calculus**: the family of operations by which trees are taken apart, recombined, focused, instantiated, matched, and rewritten. The conceptual spine — the linear development to which every later section is subordinated — is the chain

$$
\text{trees} \;\to\; \text{positions and subtrees} \;\to\; \text{replacement} \;\to\; \text{contexts} \;\to\; \text{substitution} \;\to\; \text{matching} \;\to\; \text{rewriting} \;\to\; \text{normal forms and quotients}.
$$

Each arrow is a definitional dependency, not an analogy. Positions and subtrees are defined from the structure of a tree; replacement at a position is defined from subtree extraction; a context is exactly the residue of a tree after a subtree is removed; substitution is the homomorphic extension of an assignment of trees to leaf variables; matching is the partial inverse of substitution restricted to a pattern; a one-step rewrite is the replacement at a position of a subtree that matches a rule's left-hand side by the corresponding instance of its right-hand side; normal forms are the rewrite-irreducible trees; and quotient tree algebras are the carriers obtained by collapsing trees along the congruence a rewrite or equation set generates. A reader who has internalized the early definitions of tree domain, position, subtree, replacement, context, and substitution should be able to reconstruct the formal meaning of every rewriting statement in the later sections without appeal to intuition.

The development begins in the **single-sorted, untyped** setting, with no assumed familiarity, and only later admits ranks, sorts, and types. The single-sorted ranked case is developed first and in full; the many-sorted and typed cases are obtained as decorations of it, introduced precisely at the point where a sort discipline changes which operations are defined.

### 0.2. Scope and Allocation of Depth

The treatise is organized so that the **core calculus** — tree domains, positions, subtrees, replacement, contexts (single-sorted, then typed), substitution, patterns and matching, rewriting, rewriting metatheory, equations, congruences, normal forms, and quotient tree algebras — receives the majority of the development and is treated with maximal granularity. Adjacent theories — term graphs and DAGs, tree automata and tree languages, tree transducers, operads, infinite and coinductive trees, algorithms, and proof-theoretic applications — are treated as compact but precise formal surveys, each connected back to the core spine. Compactness here means brevity of treatment, never vagueness: each survey section states explicit definitions, gives representative examples, records the key structural results, and ties the material to subtrees, contexts, substitution, matching, or rewriting.

### 0.3. Standing Distinctions

A number of distinctions are load-bearing throughout and are made at the point where each first becomes mathematically relevant rather than relegated to commentary. They are collected here as an index of the conceptual hazards the formal apparatus is designed to manage.

1. **Nodes versus labels.** A node is a position in a tree (an address); a label is a symbol decorating a node. The same label may decorate many nodes; the same address may carry different labels in different trees.
2. **Positions versus subtrees.** A position is an address in the tree domain; the subtree at a position is the entire substructure hanging below it, readdressed to its own root. A position is finite data (a sequence); a subtree is a tree.
3. **Paths versus branches.** A path is any chain in the ancestor order; a branch is a maximal path, running from the root to a leaf.
4. **Tree domains versus labelled trees.** A tree domain is bare combinatorial shape (a prefix-closed, sibling-closed set of addresses); a labelled tree adds a labelling function. Shape and decoration are separable.
5. **Replacement versus substitution.** Replacement $t[p:=s]$ acts at a single position; substitution $\widehat\sigma(t)$ acts simultaneously at every occurrence of selected variables.
6. **Substitution versus relabelling.** Relabelling changes labels while preserving the address domain; substitution may replace a leaf by an arbitrarily large tree, changing the domain.
7. **Plugging versus substitution.** Plugging $C[s]$ fills a fixed, finite set of holes; substitution replaces generator leaves recursively, at a number of sites determined by the input tree.
8. **Contexts versus trees.** A context is a tree over an extended alphabet containing hole symbols; it is an operation on trees, not a tree of the base alphabet.
9. **One-hole versus multi-hole contexts.** A one-hole context is a unary tree operation; a $k$-hole context is a $k$-ary tree operation.
10. **Object variables versus pattern variables.** Object variables are nullary labels inside the trees being manipulated; pattern variables (metavariables) are placeholders in rules and patterns, instantiated by matching.
11. **Matching versus unification.** Matching solves $\ell\sigma = u$ for $\sigma$ with $u$ a fixed ground (or held-fixed) tree; unification solves $s\sigma = t\sigma$ with variables on both sides.
12. **Equations versus rewrite rules.** An equation $\ell = r$ generates a symmetric identification; a rule $\ell \to r$ generates a directed reduction.
13. **Congruence closure versus rewrite closure.** The congruence generated by a set of equations is symmetric, reflexive, transitive, and closed under contexts and substitution; the rewrite relation generated by a set of rules is closed under contexts and substitution but is directed and need be neither symmetric nor transitive until closures are taken.
14. **Syntactic equality versus quotient equality.** Two trees are syntactically equal when they are the same element of the tree algebra; they are quotient-equal when they fall in the same class of a congruence.
15. **Tree occurrence versus DAG sharing.** A tree records each occurrence of a repeated substructure separately; a directed acyclic graph may identify equal substructures by sharing, which is not syntactic equality unless an abstraction map declares it so.

> [!remark] Remark 0.1: Reading conventions
> Numbered items — Definition, Notation, Construction, Lemma, Proposition, Theorem, Corollary, Proof Sketch, Example, Remark, Warning — form the formal spine and are numbered consecutively within each top-level section, so "Definition 9.4" is the fourth numbered item of Section 9. Running prose between items records structural relationships only and introduces no obligations. Proof sketches accompany the nontrivial results: they identify the governing construction, the decisive verification, and the structural principle (induction on a tree order, a universal property, a well-foundedness argument) at which the conclusion follows; they are not complete proofs and do not expand routine verifications that have already been isolated by name.

### 0.4. Relation to the Companion Notes

This treatise is self-contained relative to its scope. Where it overlaps the companion developments on single-sorted tree calculus and on algebraic syntax for first-order logic, it harmonizes notation with them but develops the outlined material directly and in full rather than deferring to them. The address model of trees, the prefix order, the constructor notation $a(t_1,\dots,t_n)$, the subtree, replacement, context-extraction, and plugging operations, the substitution monad, and the rewriting and quotient apparatus are aligned with the single-sorted companion; the universal-algebraic vocabulary — signatures $\Omega$, $\Omega$-algebras, homomorphisms, generated subalgebras, kernels, congruences, quotients, the universal mapping property, and the term algebra $\mathbf{T}_\Omega(X)$ — is aligned with the algebraic-syntax companion. Both layers are redeveloped here as needed; nothing in the core is left to "see elsewhere."

---

## 1. Ambient Setting and Notation

### 1.1. Foundational Conventions

> [!notation] Notation 1.1: Set-theoretic background
> The ambient foundation is a fixed model of Zermelo–Fraenkel set theory with Choice (ZFC). Write $\mathbb{N} = \{0,1,2,\dots\}$ for the natural numbers and $\mathbb{N}_{>0} = \{1,2,3,\dots\}$ for the positive integers. For a set $A$ and $n \in \mathbb{N}$, $A^n$ is the set of $n$-tuples from $A$, with $A^0 = \{()\}$ a singleton whose unique element is the empty tuple; $A^{<\omega} = \bigcup_{n \in \mathbb{N}} A^n$ is the set of finite sequences over $A$, with empty sequence $\varepsilon$ and concatenation written $u \cdot v$. The length of $u \in A^{<\omega}$ is $|u|$. The power set of $A$ is $\mathcal{P}(A)$, and $f[S] = \{f(a) : a \in S\}$ is the image of $S \subseteq \operatorname{dom}(f)$. Three relations are kept rigorously distinct: set-theoretic equality $=$, structural isomorphism $\cong$, and definitional identity $:=$.

> [!notation] Notation 1.2: Finiteness and size conventions
> Unless an section is explicitly headed otherwise (the development of infinite and coinductive trees), every tree, tree domain, signature instance, and rewrite is **finite**: finitely many nodes, finitely many positions, finite depth. Label sets, signatures, and variable sets may be of arbitrary cardinality, but each individual tree uses only finitely many of their elements. The reliance on finiteness is flagged wherever a result depends on it essentially — chiefly in the stabilization of stage constructions at $\omega$, the well-foundedness of the subtree order, the legitimacy of structural induction and recursion, and the finite branching that makes redex search and matching effective.

The methodological decision governing the entire treatise is that a tree is a combinatorial object that exists **prior to any interpretation**. Its construction — a closure process governed by a shape discipline and a labelling — is kept strictly separate from its evaluation, its denotation, or its meaning in any algebra. This separation is what later licenses the clean distinction between syntactic equality and quotient or semantic equality, and between operations that build and transform trees (extraction, replacement, plugging, substitution, rewriting) and operations that consume trees into values (folds, evaluations).

### 1.2. The Address Monoid

The single most useful concrete model of trees in this treatise is the **address model**, in which nodes are finite sequences of positive integers and the tree is reconstructed from the set of addresses it occupies together with a labelling. The address model is adopted as the primary working representation precisely because it makes positions, subtrees, replacement, contexts, and rewriting completely explicit; the alternative presentations of the next section are shown to be canonically equivalent to it.

> [!definition] Definition 1.3: Address space, addresses, positions
> The **address space** is the set
>
> $$
> \mathbb{A} := \mathbb{N}_{>0}^{<\omega}
> $$
>
> of finite sequences of positive integers. Its elements are called **addresses** or **positions**. The empty sequence $\varepsilon$ is the **root address**. For $p = (i_1,\dots,i_k) \in \mathbb{A}$, the number $|p| = k$ is the **length** or **depth** of $p$. Concatenation of addresses is written $p \cdot q$; for $i \in \mathbb{N}_{>0}$ we abbreviate $p \cdot (i)$ to $p \cdot i$, the address of the prospective $i$-th child of the node at $p$.

> [!notation] Notation 1.4: The monoid structure
> $(\mathbb{A}, \cdot, \varepsilon)$ is the free monoid on $\mathbb{N}_{>0}$: concatenation is associative, $\varepsilon$ is a two-sided unit, and every nonempty address factors uniquely as $i \cdot p'$ (first index then remainder) and as $p'' \cdot i$ (initial segment then last index). Freeness of this monoid is the combinatorial engine behind unique readability of trees: an address records, without ambiguity, a finite sequence of "descend into the $i$-th child" instructions.

> [!definition] Definition 1.5: Prefix order, ancestor relation
> The **prefix order** on $\mathbb{A}$ is
>
> $$
> p \preceq q \quad\Longleftrightarrow\quad \exists\, r \in \mathbb{A}\ \ q = p \cdot r.
> $$
>
> When $p \preceq q$, $p$ is an **ancestor address** of $q$ and $q$ a **descendant address** of $p$; the witnessing $r$ is the **residual** of $q$ below $p$, written $r = p^{-1}q$ when it exists (it is then unique by freeness of $\mathbb{A}$). Write $p \prec q$ for $p \preceq q \wedge p \neq q$ (strict ancestry). Two addresses are **comparable** if one is a prefix of the other and **disjoint** (synonym: **incomparable**, **parallel**), written $p \mathbin{\|} q$, otherwise.

> [!proposition] Proposition 1.6: The prefix order is a well-founded partial order with least element
> The relation $\preceq$ is a partial order on $\mathbb{A}$ with least element $\varepsilon$; restricted to any finite set of addresses it is well-founded, and the strict part $\prec$ has no infinite descending chains.
>
> [!proof-sketch] Proof Sketch 1.6
> Reflexivity, antisymmetry, and transitivity follow from the monoid laws and uniqueness of factorization in the free monoid $\mathbb{A}$: $p \preceq q \preceq p$ forces residuals composing to $\varepsilon$, hence each is $\varepsilon$. Minimality of $\varepsilon$ is $\varepsilon \cdot p = p$. Well-foundedness on a set $D$ follows since $p \prec q$ implies $|p| < |q|$, and lengths are natural numbers, which are well-ordered; an infinite $\prec$-descending chain would yield an infinite strictly decreasing sequence of naturals.

The map $p \mapsto |p|$ is a strictly order-preserving function from $(\mathbb{A}, \prec)$ to $(\mathbb{N}, <)$; it is the source of every induction "on the depth of a node" and, dually, of recursion that descends from a node into its children. Disjointness $p \mathbin{\|} q$ is the geometric condition under which the substructures at $p$ and $q$ do not overlap, and it is exactly the hypothesis under which replacements at $p$ and at $q$ commute (Section 9).

### 1.3. Orientation of Primitive Data

The primitive data of the theory, fixed once and used throughout the core, are: (i) the address space $\mathbb{A}$ with its prefix order, a fixed mathematical object; (ii) a **label set** $L$, an arbitrary set whose elements decorate nodes; and, when a shape discipline is imposed, (iii) a **rank function** $\rho : L \to \mathbb{N}$ assigning to each label the number of children a node carrying it must have. The pair $(L, \rho)$ is a ranked alphabet (Section 4). Variables and constants enter as rank-zero labels; operation symbols of a signature enter as labels ranked by arity. The remainder of this section fixes only $\mathbb{A}$; labels, ranks, and sorts are introduced where the corresponding structural layer is developed, so that the bare shape theory of Sections 2–3 is available before any decoration is imposed.

---

## 2. Presentations of Trees

The word "tree" denotes several related but non-identical mathematical objects. This section assembles the principal presentations, states the conditions defining each, and records the canonical correspondences among them. The purpose is twofold: to fix the address presentation as the primary working model, and to make explicit which extra structure each alternative presentation carries or discards. None of these presentations is "the" definition; each is a realization, and the substantive content is the equivalences and their limits.

### 2.1. Graph-Theoretic Trees

> [!definition] Definition 2.1: Undirected tree
> An **undirected tree** is a graph $G = (V, E)$ — $V$ a finite set of **vertices**, $E$ a set of two-element subsets of $V$ called **edges** — that is connected and acyclic. Equivalently, $G$ is an undirected tree iff any two vertices are joined by a unique simple path; equivalently, $G$ is connected and $|E| = |V| - 1$; equivalently, $G$ is acyclic and $|E| = |V| - 1$.

> [!definition] Definition 2.2: Rooted tree
> A **rooted tree** is a pair $(G, r)$ with $G$ an undirected tree and $r \in V$ a distinguished vertex, the **root**. The root induces an orientation: each non-root vertex $v$ has a unique neighbor on the path from $v$ to $r$, its **parent**; the other neighbors are its **children**. This makes the edge set a function "child $\mapsto$ parent" defined off the root and orients every edge toward the root.

An undirected tree carries no distinguished vertex and no order on the neighbors of a vertex. Rooting selects a vertex and thereby an ancestry; it does not order siblings. The graph presentation is the natural one for questions about connectivity, distance in the edge metric, spanning structures, and enumeration of unordered or unrooted shapes, and it is the presentation least adapted to syntax, precisely because it omits the sibling order that syntax requires.

> [!warning] Warning 2.3: Graph trees underdetermine syntactic trees
> A rooted graph-theoretic tree does not record an order among the children of a vertex, so it cannot distinguish $f(x,y)$ from $f(y,x)$, nor identify "the second argument of a node." Every later operation indexed by child position — subtree at an address, replacement at a position, plugging into the $i$-th hole — is undefined on bare rooted graph trees. The address and ordered presentations supply exactly the missing datum.

### 2.2. Ordered Rooted Trees

> [!definition] Definition 2.4: Ordered rooted tree
> An **ordered rooted tree** is a rooted tree together with, for each vertex $v$, a linear order on the set of children of $v$. Equivalently, the children of each vertex are enumerated $v_1, \dots, v_{k}$ without repetition. Two ordered rooted trees are **equal** when there is a root-preserving, parent-preserving, and child-order-preserving bijection of vertices; they are **isomorphic as ordered rooted trees** under the same condition. The sibling order is the additional datum over Definition 2.2.

Ordered rooted trees are the combinatorial objects underlying syntax: the children of an internal node are its arguments in order, and the leaves read left to right are the frontier. They are in canonical bijection with the address model, the bijection being "name each vertex by the sequence of child indices on the path from the root."

### 2.3. Trees as Partial Orders

> [!definition] Definition 2.5: Tree order
> A **tree order** (or **tree poset**) is a partial order $(V, \le)$ with a least element (the root) such that for every $v \in V$ the set of predecessors ${\downarrow} v := \{u : u \le v\}$ is a finite chain. The elements are the nodes; $u \le v$ reads "$u$ is an ancestor of $v$"; the **parent** of a non-root $v$ is the greatest element of ${\downarrow} v \setminus \{v\}$ (it exists because ${\downarrow}v$ is a finite chain); **leaves** are the maximal elements; the **root** is the least element.

The poset presentation captures ancestry exactly: the cover relation is the parent relation, principal down-sets are the ancestor chains, and principal up-sets ${\uparrow} v := \{w : v \le w\}$ are the descendant sets, which carry the induced order of the subtree at $v$. It does not, by itself, order siblings; an **ordered tree poset** adds for each $v$ a linear order on its children (its covers), recovering the ordered rooted tree. The poset view is the natural home for the induction and recursion principles of Section 5, because well-foundedness of $\le$ on a finite tree is immediate and the recursion theorem is the recursion theorem for the ancestor order.

### 2.4. Trees as Prefix-Closed Address Domains

> [!definition] Definition 2.6: Finite address-tree domain
> A **finite address-tree domain** (briefly, a **tree domain**) is a finite, nonempty subset $D \subseteq \mathbb{A}$ satisfying:
>
> 1. **prefix closure**: if $q \in D$ and $p \preceq q$, then $p \in D$;
> 2. **left-sibling closure** (no sibling gaps): if $p \cdot (i+1) \in D$ for some $i \in \mathbb{N}_{>0}$, then $p \cdot i \in D$.
>
> The root $\varepsilon$ lies in every tree domain (nonemptiness plus prefix closure). For $p \in D$, the **child arity** of $p$ in $D$ is
>
> $$
> k_D(p) := \big|\{\, i \in \mathbb{N}_{>0} : p \cdot i \in D \,\}\big|,
> $$
>
> and by left-sibling closure the children of $p$ are exactly $p \cdot 1, \dots, p \cdot k_D(p)$, contiguously indexed.

Prefix closure is the statement that every node carries its ancestors; left-sibling closure is the statement that children are numbered $1, 2, \dots, k$ with no omissions, so that "the $i$-th child" is unambiguous and total below the arity. A tree domain is precisely the bare combinatorial shape of an ordered rooted tree, encoded so that every node has a canonical name.

> [!proposition] Proposition 2.7: Address domains realize ordered rooted shapes
> The assignment sending an ordered rooted tree to the set of child-index sequences of its vertices is a bijection between (isomorphism classes of) finite ordered rooted trees and finite address-tree domains, under which the root maps to $\varepsilon$, the parent map to "delete last index," and the child order to the natural order of last indices.
>
> [!proof-sketch] Proof Sketch 2.7
> Given an ordered rooted tree, name the root $\varepsilon$ and inductively name the $i$-th child of the node named $p$ by $p \cdot i$. Prefix closure holds because every named node has a named parent; left-sibling closure holds because children are enumerated contiguously. The map is injective on isomorphism classes because the names reconstruct the parent and sibling-order data, and surjective because any tree domain $D$ defines an ordered rooted tree on vertex set $D$ with parent "delete last index" and child order by last index; the two passages are mutually inverse.

> [!notation] Notation 2.8: The address model is primary
> Henceforth "tree" means a labelled finite address-tree domain (Definition 4.4), and tree domains are the bare shapes. The address presentation is adopted because positions, subtrees, replacement, contexts, and rewriting are all defined by elementary operations on the set $D$ and the labelling — restriction, residual, union after re-rooting — with no auxiliary bookkeeping. Statements proved in the address model transfer to the ordered-rooted and poset models along the canonical bijections of Propositions 2.7 and 2.5; statements about internal encoding (specific index sequences) are model-relative and do not transfer.

### 2.5. Recursively Generated Trees

> [!construction] Construction 2.9: Trees as a least fixed point of grafting
> Fix a ranked alphabet $(L,\rho)$ (Section 4). Define the set $T_L$ of **(recursively generated) trees over $L$** as the least set such that whenever $a \in L$ with $\rho(a) = n$ and $t_1, \dots, t_n \in T_L$, the formal expression $a(t_1, \dots, t_n)$ lies in $T_L$. The base case is $n = 0$: each rank-zero label $a$ yields the atomic tree $a()$, written $a$. "Least set closed under the grafting clauses" is made precise as $T_L = \bigcup_{k<\omega} T_L^{(k)}$, where $T_L^{(0)} = \{\, a() : \rho(a) = 0\,\}$ and $T_L^{(k+1)}$ adds all $a(t_1,\dots,t_n)$ with $t_i \in T_L^{(k)}$.

The recursive presentation is the one in which structural induction and recursion are definitionally transparent: a property holds of all trees iff it holds of every $a(t_1,\dots,t_n)$ whenever it holds of $t_1,\dots,t_n$, and a function is defined on all trees by specifying its value on $a(t_1,\dots,t_n)$ from its values on the $t_i$. The least-fixed-point clause guarantees there is nothing in $T_L$ except what the constructors build, which is exactly what licenses these principles. The equivalence of the recursive and address presentations is Proposition 4.7.

### 2.6. Trees as Initial Algebras and Fixed Points of Branching Functors

> [!construction] Construction 2.10: The branching (polynomial) functor
> Fix a ranked alphabet $(L, \rho)$. Define the **branching functor** $F_L$ on the category of sets by
>
> $$
> F_L(Z) := \coprod_{a \in L} Z^{\rho(a)} \;=\; \{\, (a, z_1, \dots, z_{\rho(a)}) : a \in L,\ z_i \in Z \,\},
> $$
>
> a **polynomial functor**: a coproduct, indexed by labels, of finite powers given by the ranks. An **$F_L$-algebra** is a set $Z$ with a structure map $F_L(Z) \to Z$; a homomorphism of $F_L$-algebras is a function commuting with the structure maps.

> [!theorem] Theorem 2.11: Finite trees as the initial $F_L$-algebra
> The set $T_L$ of finite trees over $L$, with structure map sending $(a, t_1, \dots, t_n)$ to $a(t_1, \dots, t_n)$, is the **initial** $F_L$-algebra: for every $F_L$-algebra $(Z, \zeta)$ there is a unique homomorphism $T_L \to Z$. Equivalently $T_L$ is the least fixed point $\mu F_L$ of $F_L$, and the structure map is an isomorphism $F_L(T_L) \xrightarrow{\ \cong\ } T_L$.
>
> [!proof-sketch] Proof Sketch 2.11
> The structure map is a bijection because every tree is uniquely either an atom or $a(t_1,\dots,t_n)$ for a unique label and unique immediate subtrees (unique readability, Proposition 4.8), which is exactly injectivity and surjectivity of $(a, \vec t\,) \mapsto a(\vec t\,)$. Initiality: define the unique homomorphism $h : T_L \to Z$ by recursion, $h(a(t_1,\dots,t_n)) = \zeta(a, h(t_1),\dots,h(t_n))$; the recursion is legitimate by well-foundedness of the immediate-subtree relation (Section 5), it is a homomorphism by construction, and any homomorphism must satisfy the same recursion, hence is equal to $h$. Leastness of the fixed point is the finitary stage construction of Construction 2.9.

The initial-algebra presentation is the most structural: it identifies "the trees over $L$" with a universal solution to the equation $Z \cong F_L(Z)$, makes the recursion principle into the universal property, and is the exact dual of the coalgebraic presentation of infinite trees (Section 22), where the same functor's **final** coalgebra appears. It also exhibits the tree algebra of Section 8 as a special case: when $L = X \sqcup \Omega$ with $X$ rank-zero variables and $\Omega$ a signature, $\mu F_L$ is the absolutely free $\Omega$-algebra on $X$.

> [!remark] Remark 2.12: What each presentation is good for
> The presentations are pairwise canonically equivalent on finite ordered trees, but expose different machinery and should be selected accordingly. Graph trees expose connectivity and the edge metric but suppress sibling order. Ordered rooted trees expose sibling order directly and are the natural objects of combinatorial enumeration. Poset trees expose ancestry, well-foundedness, and the induction/recursion principles. Address domains expose positions, subtrees, replacement, contexts, and rewriting, and are adopted as primary for that reason. The recursive presentation exposes structural induction and constructor recursion. The initial-algebra presentation exposes the universal property and the link to coalgebra, free algebras, and fixed-point semantics. A claim about distances belongs to the graph model; a claim about positions belongs to the address model; a claim about recursion belongs to the recursive or initial-algebra model. Mixing the models is legitimate only along the canonical correspondences, and only for data those correspondences preserve.

---

## 3. Basic Tree Structure

This section develops the internal anatomy of trees in the address model, slowly and exhaustively, so that every later operation — $t|_p$, $t[p:=s]$, context extraction, plugging, matching at a position — rests on unambiguous primitives. The decorations of labels and ranks are deferred to Section 4; here the carrier is a bare tree domain $D$, except where a labelling is needed to define a notion (it is then flagged).

### 3.1. Nodes, Root, Parent, Children

> [!definition] Definition 3.1: Nodes and root
> Let $D$ be a tree domain. The elements of $D$ are the **nodes** (synonym in the address model: **positions**) of $D$. The unique node $\varepsilon \in D$ is the **root**. A node is identified with its address; "the node $p$" and "the position $p$" are the same datum, namely $p \in D$.

> [!definition] Definition 3.2: Parent and child
> Let $D$ be a tree domain and $p \in D$ with $p \neq \varepsilon$. Writing $p = p' \cdot i$ with $i \in \mathbb{N}_{>0}$ (the unique factorization removing the last index), the node $p'$ is the **parent** of $p$, denoted $\operatorname{par}(p)$; correspondingly $p$ is a **child** of $p'$. The set of children of $p \in D$ is
>
> $$
> \operatorname{ch}_D(p) := \{\, p \cdot i : i \in \mathbb{N}_{>0},\ p \cdot i \in D \,\} = \{\, p \cdot 1, \dots, p \cdot k_D(p) \,\}.
> $$
>
> The parent map $\operatorname{par} : D \setminus \{\varepsilon\} \to D$ is total (prefix closure guarantees $p' \in D$) and surjective onto the internal nodes; the root has no parent.

> [!definition] Definition 3.3: Siblings
> Two distinct nodes $p, q \in D$ are **siblings** if they have the same parent, i.e. $\operatorname{par}(p) = \operatorname{par}(q)$, equivalently $p = u \cdot i$ and $q = u \cdot j$ with $i \neq j$ and common $u$. The **$i$-th child** of $p$, when it exists, is $p \cdot i$; left-sibling closure makes $\operatorname{ch}_D(p)$ an initial segment of the children indices, so "the $i$-th child" is defined for $1 \le i \le k_D(p)$ and undefined beyond.

### 3.2. Ancestors, Descendants, Paths, Branches

> [!definition] Definition 3.4: Ancestor and descendant
> For $p, q \in D$, $p$ is an **ancestor** of $q$ (and $q$ a **descendant** of $p$) when $p \preceq q$ in the prefix order; the ancestry is **strict** when $p \prec q$. The ancestors of $q$ form the chain
>
> $$
> {\downarrow}\, q := \{\, p \in D : p \preceq q \,\} = \{\, \text{the prefixes of } q \,\},
> $$
>
> a finite linearly ordered set of size $|q| + 1$ running $\varepsilon \prec \cdots \prec q$. The descendants of $p$ form the up-set ${\uparrow}\, p := \{\, q \in D : p \preceq q \,\}$, which carries the structure of the subtree at $p$ (Section 3.5).

> [!definition] Definition 3.5: Path and branch
> A **path** in $D$ is any nonempty chain in $(D, \preceq)$ — a set of pairwise comparable nodes; concretely a path from $p$ to $q$ with $p \preceq q$ is the chain $\{\, r \in D : p \preceq r \preceq q \,\}$. A **branch** is a maximal path, equivalently a path from the root $\varepsilon$ to a leaf. The **branches** of $D$ are in bijection with its leaves, each leaf $\ell$ determining the branch ${\downarrow}\, \ell$.

> [!warning] Warning 3.6: Paths are not branches; both differ from addresses
> A path is a chain of nodes; a branch is a root-to-leaf path; an address is a single node's name. Conflating them produces category errors: "the path to $p$" is the ancestor chain ${\downarrow}\,p$ (a set of nodes), whereas "the address of $p$" is the sequence $p$ itself (one element of $\mathbb{A}$). The number of branches is the number of leaves; the number of paths is far larger (every comparable pair bounds one).

### 3.3. Leaves, Internal Nodes, Frontier

> [!definition] Definition 3.7: Leaf and internal node
> A node $p \in D$ is a **leaf** if it has no children, $\operatorname{ch}_D(p) = \varnothing$, equivalently $k_D(p) = 0$; otherwise $p$ is **internal**. The **frontier** (synonym: **leaf set**) of $D$ is
>
> $$
> \partial D := \{\, p \in D : k_D(p) = 0 \,\}.
> $$
>
> The internal nodes are $D \setminus \partial D$. In a labelled arity-correct tree (Definition 4.6) a node is a leaf iff its label has rank zero, so the frontier is then determined by the labelling.

The frontier is the active boundary of a tree. In a derivation tree the leaves are open assumptions or terminal symbols; in a syntax tree they are variables and constants; in a parse tree, read left to right, they spell the generated string (the yield, Section 6). Internal nodes carry the constructors that assemble the leaves into a whole.

### 3.4. Levels, Depth, Height

> [!definition] Definition 3.8: Depth of a node, level, width
> The **depth** of a node $p \in D$ is its address length, $\operatorname{depth}_D(p) := |p|$; the root has depth $0$. The **$k$-th level** of $D$ is
>
> $$
> D_k := \{\, p \in D : |p| = k \,\},
> $$
>
> and the **width** of $D$ is $\operatorname{width}(D) := \max_k |D_k|$, the largest level size.

> [!definition] Definition 3.9: Height of a tree
> The **height** of $D$ is
>
> $$
> \operatorname{ht}(D) := \max\{\, |p| : p \in D \,\},
> $$
>
> the depth of its deepest node; a one-node tree has height $0$. The **height of a node** is ambiguous in the literature between the node's depth from the root and the height of the subtree it roots; this treatise resolves the ambiguity by using $\operatorname{depth}_D(p) = |p|$ for the former and $\operatorname{subht}_D(p) := \operatorname{ht}(D|_p)$ (Section 3.5) for the latter, never "height of a node" unqualified.

### 3.5. Subtrees and Immediate Subtrees

The subtree at a node is the single most important derived object: it is the input to extraction, the matched object in rewriting, and the focus of a context decomposition. It is defined here on bare domains and immediately on labelled trees in Section 4.

> [!definition] Definition 3.10: Subdomain at a node
> Let $D$ be a tree domain and $p \in D$. The **subdomain of $D$ at $p$** is
>
> $$
> D|_p := \{\, q \in \mathbb{A} : p \cdot q \in D \,\},
> $$
>
> the set of residuals below $p$. It is itself a tree domain: it contains $\varepsilon$ (since $p \in D$), is prefix-closed (if $p\cdot q \in D$ and $q' \preceq q$ then $p \cdot q' \in D$), and is left-sibling closed (inherited from $D$). The readdressing $q \mapsto p \cdot q$ is a bijection $D|_p \to {\uparrow}\,p$ that carries $\varepsilon$ to $p$ and preserves the prefix order and child indices.

> [!definition] Definition 3.11: Immediate subdomain
> The **immediate subdomains** of $D$ (when $\varepsilon$ is internal, with children $1, \dots, k$) are the subdomains $D|_1, \dots, D|_k$ at the children of the root. Every node $p \neq \varepsilon$ lies in exactly one immediate subdomain, namely $D|_{i}$ for $i$ the first index of $p$, at residual position equal to $p$ with its first index removed.

The distinction between **subtree** and **immediate subtree** is the distinction driving recursion: the immediate subtrees of $a(t_1,\dots,t_n)$ are exactly $t_1,\dots,t_n$, and a structural recursion descends one level to them; the subtree at an arbitrary position $p$ is reached by iterating the immediate-subtree passage $|p|$ times, and a position-indexed operation reaches it directly. The immediate-subtree relation is the cover relation of the strict ancestor order restricted to roots of subtrees, and its well-foundedness (Section 5) is what makes structural recursion legitimate.

### 3.6. Size, Leaf Count, Branching, Arity

> [!definition] Definition 3.12: Size, leaf count, internal count
> For a tree domain $D$:
>
> $$
> |D| := \#D \quad(\text{the \textbf{size}, the number of nodes}), \qquad \operatorname{leaf}(D) := |\partial D|, \qquad \operatorname{int}(D) := |D \setminus \partial D|,
> $$
>
> so that $|D| = \operatorname{leaf}(D) + \operatorname{int}(D)$.

> [!definition] Definition 3.13: Branching number and arity
> The **branching number** (out-degree) of a node $p$ is $k_D(p)$, the number of its children. The **arity** of $p$, when $D$ is the domain of a labelled arity-correct tree $(D,\ell)$, is $\rho(\ell(p))$, and arity-correctness is exactly the identity $k_D(p) = \rho(\ell(p))$ at every node (Definition 4.6). On bare domains only the branching number is defined; arity is a labelled notion.

> [!proposition] Proposition 3.14: Handshake identity for rooted trees
> For every tree domain $D$,
>
> $$
> \sum_{p \in D} k_D(p) \;=\; |D| - 1,
> $$
>
> equivalently $\sum_{k \ge 0} k\, b_k(D) = |D| - 1$, where $b_k(D) := |\{p \in D : k_D(p) = k\}|$ is the **branching profile**.
>
> [!proof-sketch] Proof Sketch 3.14
> Each non-root node is the child of exactly one node (its parent is unique), so the multiset of all children, $\bigsqcup_{p} \operatorname{ch}_D(p)$, is exactly $D \setminus \{\varepsilon\}$, of size $|D| - 1$; the left side counts the same multiset by summing out-degrees. The branching-profile form regroups the sum by out-degree value.

The handshake identity is a structural invariant used as a consistency check on tree encodings and traversals, and it specializes usefully: for a full binary tree (every internal node has out-degree exactly $2$) it gives $\operatorname{leaf}(D) = \operatorname{int}(D) + 1$, and more generally for trees all of whose internal nodes have out-degree $m$ it gives $(m-1)\operatorname{int}(D) = \operatorname{leaf}(D) - 1$.

### 3.7. Tree Equality

> [!definition] Definition 3.15: Equality of tree domains and of labelled trees
> Two tree domains are **equal** when they are equal as subsets of $\mathbb{A}$: $D = D'$ iff they contain exactly the same addresses. Two labelled trees $(D,\ell)$ and $(D',\ell')$ are **equal** when $D = D'$ and $\ell = \ell'$ as functions, i.e. same domain and same label at every node. Equality of trees is thus literal identity of the encoding data, not isomorphism.

> [!warning] Warning 3.16: Tree equality is syntactic, not semantic, not up-to-isomorphism
> In the address model two trees are equal precisely when they occupy the same addresses with the same labels. This is **syntactic equality**: it distinguishes $f(x,y)$ from $f(y,x)$ (different labels at addresses $1$ and $2$) and distinguishes a tree from any non-trivial rearrangement of it. It is strictly finer than (i) isomorphism of ordered rooted trees, which it coincides with only because the address names are canonical; (ii) semantic equality under any evaluation; and (iii) quotient equality modulo a congruence (Section 16). Every identification coarser than Definition 3.15 is an explicitly imposed relation, never the default.

The labelled notion of subtree, the constructor notation, and the formal definitions of replacement and contexts all presuppose this syntactic equality as their base; quotient and semantic identifications are layered on top in Sections 12, 16, and the survey sections, never silently.

---

## 4. Shapes, Labels, Ranked Trees, and Typed Trees

A tree carries several superimposed layers of structure, and confusion between them is the most common source of error in tree manipulation. This section separates them: bare shape, addressed shape, labelled tree, ranked labelled tree, and typed/sorted tree. The single-sorted ranked case is developed fully first; the typed case is introduced only afterward, as a sort-indexed refinement.

### 4.1. Bare Shape and Addressed Shape

> [!definition] Definition 4.1: Bare shape
> The **bare shape** of a tree is its underlying ordered rooted tree up to ordered isomorphism — the branching pattern alone, with no labels and no canonical names. Two trees have the same bare shape iff there is a root-, parent-, and sibling-order-preserving bijection of nodes. The bare shapes are the isomorphism classes of ordered rooted trees.

> [!definition] Definition 4.2: Addressed shape
> The **addressed shape** of a tree is its tree domain $D \subseteq \mathbb{A}$: the bare shape made concrete by canonical addresses. By Proposition 2.7 the addressed shapes (tree domains) are in bijection with the bare shapes (ordered-rooted isomorphism classes), so the addressed shape is a canonical choice of representative. A labelled tree has an addressed shape (its domain) obtained by forgetting the labelling.

The passage from bare to addressed shape replaces "a shape up to isomorphism" by "a specific prefix-closed sibling-closed set," eliminating the ambiguity of unnamed nodes. The passage from addressed shape to labelled tree adds the labelling. These two passages are orthogonal: relabelling changes the labels while fixing the addressed shape (Section 4.4); reshaping changes the domain.

### 4.2. Labelled Trees

> [!definition] Definition 4.3: Label set
> A **label set** (synonym: **alphabet**) is an arbitrary set $L$ whose elements are the **labels** available to decorate nodes. No structure on $L$ is assumed at this layer; ranks and sorts are added below. When $L$ is partitioned as $L = X \sqcup \Omega$ with $X$ a set of rank-zero **variables** and $\Omega$ a ranked set of **operation symbols**, the resulting labelled trees are term trees (Section 8).

> [!definition] Definition 4.4: Labelled address tree
> An **$L$-labelled (finite) tree** is a pair $t = (D, \ell)$ where $D$ is a finite address-tree domain and $\ell : D \to L$ is a function, the **labelling**. The domain is $\operatorname{dom}(t) := D$, also written $D_t$; the label at $p$ is $\ell(p)$, also written $\ell_t(p)$. The set of all $L$-labelled finite trees is written $T_L^{\flat}$ (the superscript $\flat$ marks that no rank discipline is yet imposed); the arity-correct subset (Definition 4.6) is $T_L$ or $\operatorname{Tree}_L$.

> [!warning] Warning 4.5: Labels are not nodes
> A label $\ell(p) \in L$ and a node $p \in D$ are objects of different kinds. A node is a position; a label is a symbol. One label may occur at many nodes — $\#_a(t) := |\{p : \ell(p) = a\}|$ counts the occurrences of label $a$ — and label equality $\ell(p) = \ell(q)$ is far weaker than node equality $p = q$ or subtree equality $t|_p = t|_q$. The distinction is the source of the difference between relabelling (acts on labels, fixes nodes) and substitution (acts on variable-labelled leaves, may change nodes).

### 4.3. Ranked Alphabets and Arity-Correct Trees

> [!definition] Definition 4.6: Ranked alphabet, arity correctness
> A **ranked alphabet** (synonym: **single-sorted signature**) is a pair $(L, \rho)$ with $L$ a label set and $\rho : L \to \mathbb{N}$ a **rank function**; $\rho(a)$ is the **rank** (synonym: **arity**) of $a$, the number of children a node labelled $a$ must carry. Write $L_n := \{a \in L : \rho(a) = n\}$ for the labels of rank $n$. An $L$-labelled tree $(D, \ell)$ is **arity-correct** if for every $p \in D$,
>
> $$
> k_D(p) \;=\; \rho(\ell(p)),
> $$
>
> i.e. each node has exactly as many children as its label's rank prescribes. Unless explicitly stated otherwise, **a tree over $(L,\rho)$** means a finite arity-correct $L$-labelled address tree; the set of these is $\operatorname{Tree}_L$ (or $T_L$).

> [!definition] Definition 4.7: Constructor (grafting) notation
> For $a \in L$ with $\rho(a) = n$ and trees $t_1, \dots, t_n \in \operatorname{Tree}_L$ with $t_i = (D_i, \ell_i)$, the **grafted tree** $a(t_1, \dots, t_n)$ is the tree $(D, \ell)$ with
>
> $$
> D := \{\varepsilon\} \cup \bigcup_{i=1}^{n} \{\, i \cdot p : p \in D_i \,\}, \qquad \ell(\varepsilon) := a, \qquad \ell(i \cdot p) := \ell_i(p).
> $$
>
> When $n = 0$ this is the atomic tree $a$ with domain $\{\varepsilon\}$ and $\ell(\varepsilon) = a$. The grafted tree is arity-correct whenever the $t_i$ are, and $a(t_1,\dots,t_n)$ has root labelled $a$ with $i$-th immediate subtree exactly $t_i$.

> [!proposition] Proposition 4.8: Unique readability
> Every nonempty arity-correct tree $t$ over $(L,\rho)$ is equal to $a(t_1,\dots,t_n)$ for a **unique** label $a = \ell_t(\varepsilon)$ with $n = \rho(a)$ and **unique** immediate subtrees $t_i = t|_i$ ($1 \le i \le n$). Hence the grafting map
>
> $$
> \coprod_{a \in L} \operatorname{Tree}_L^{\,\rho(a)} \;\xrightarrow{\ \cong\ }\; \operatorname{Tree}_L, \qquad (a, t_1, \dots, t_n) \mapsto a(t_1, \dots, t_n),
> $$
>
> is a bijection.
>
> [!proof-sketch] Proof Sketch 4.8
> Surjectivity: given $t = (D,\ell)$ with $a := \ell(\varepsilon)$, arity-correctness gives $k_D(\varepsilon) = \rho(a) = n$, so the children are $1, \dots, n$; setting $t_i := t|_i$ reconstructs $t = a(t_1,\dots,t_n)$ by the domain and label formulas of Definition 4.7. Injectivity: from $a(t_1,\dots,t_n) = (D,\ell)$, the root label recovers $a$ uniquely, and the immediate-subtree formula $t_i = t|_i$ recovers each $t_i$ uniquely. This is the bijectivity of the structure map of the initial algebra (Theorem 2.11).

Unique readability is the structural fact that underwrites everything definitional: because the root label and the immediate subtrees are recovered uniquely, recursion on trees has well-defined clauses, and because the recovery is total on nonempty trees, those clauses are exhaustive. It is the address-model rendering of "no two distinct constructor applications produce the same tree."

> [!warning] Warning 4.9: Malformed and overloaded labels
> A labelled tree that violates arity-correctness — some node with $k_D(p) \neq \rho(\ell(p))$ — is **malformed** and is not a member of $\operatorname{Tree}_L$; constructor notation $a(t_1,\dots,t_n)$ presupposes $n = \rho(a)$ and is otherwise undefined. The rank function must assign each label exactly one rank: a symbol may not be simultaneously binary and ternary. "Overloaded" symbols are modeled by distinct labels of distinct ranks. This single-valuedness is load-bearing — unique readability, prefix-word parsing (Section 6), and the freeness criteria (Section 8) all fail under genuine overloading.

### 4.4. Shape-Preserving Relabelling

> [!definition] Definition 4.10: Rank-preserving alphabet map and relabelling
> Let $(L, \rho_L)$ and $(M, \rho_M)$ be ranked alphabets. A **rank-preserving alphabet map** is a function $\varphi : L \to M$ with $\rho_M(\varphi(a)) = \rho_L(a)$ for all $a$. It induces the **relabelling**
>
> $$
> \operatorname{map}_\varphi : \operatorname{Tree}_L \to \operatorname{Tree}_M, \qquad \operatorname{map}_\varphi(D, \ell) := (D, \varphi \circ \ell),
> $$
>
> which fixes the address domain and rewrites each label by $\varphi$. Because $\varphi$ preserves rank, $\operatorname{map}_\varphi(t)$ is arity-correct whenever $t$ is.

> [!proposition] Proposition 4.11: Relabelling is shape-preserving and functorial
> For every rank-preserving $\varphi$, $\operatorname{map}_\varphi$ satisfies $D_{\operatorname{map}_\varphi(t)} = D_t$ (shape preservation), commutes with grafting, $\operatorname{map}_\varphi(a(t_1,\dots,t_n)) = \varphi(a)(\operatorname{map}_\varphi(t_1),\dots,\operatorname{map}_\varphi(t_n))$, and is functorial, $\operatorname{map}_{\psi \circ \varphi} = \operatorname{map}_\psi \circ \operatorname{map}_\varphi$ and $\operatorname{map}_{\mathrm{id}_L} = \mathrm{id}$.
>
> [!proof-sketch] Proof Sketch 4.11
> Shape preservation is immediate from the definition (only the labelling is altered). Commutation with grafting and functoriality follow by computing both sides on the address domain and labelling and using $\rho_M \circ \varphi = \rho_L$ for arity-correctness; equivalently, $\operatorname{map}_\varphi$ is the unique $F$-homomorphism induced by $\varphi$ between the initial algebras, and functoriality is uniqueness.

> [!warning] Warning 4.12: Relabelling versus substitution
> A relabelling changes a label of rank $n$ to another label of rank $n$ and never alters the address domain. Replacing a variable leaf $x$ (rank $0$) by a larger tree $s$ is **not** a relabelling: it changes the domain (the leaf $p$ becomes the root of a copy of $s$) and is governed by substitution (Section 12). The litmus test is rank: a label-to-label map that preserves rank is a relabelling; a leaf-to-tree assignment is a substitution.

### 4.5. Variables and Constants as Rank-Zero Labels

> [!definition] Definition 4.13: Variables, constants, signatures
> In syntactic applications the ranked alphabet is partitioned as $L = X \sqcup \Omega$ where: $X$ is a set of **variables** (synonym in this role: **generators**), all of rank $0$; and $\Omega = (\Omega, \operatorname{ar})$ is a **signature** of **operation symbols**, with $\Omega_n := \{f \in \Omega : \operatorname{ar}(f) = n\}$ the $n$-ary symbols and the rank of $f$ taken to be $\operatorname{ar}(f)$. The rank-zero operation symbols $\Omega_0$ are the **(formal) constants**. Trees over $X \sqcup \Omega$ are the **term trees** over the signature $\Omega$ with variables $X$; their set is written $\operatorname{Tree}_\Omega(X)$ or, as an algebra, $\mathbf{T}_\Omega(X)$ (Section 8).

> [!warning] Warning 4.14: Constants are forced; variables are free
> Both constants $c \in \Omega_0$ and variables $x \in X$ occur as rank-zero leaves, but they behave oppositely under the operations of the calculus. A constant is part of the signature: it is interpreted in every algebra and preserved by every homomorphism, and substitution does not touch it. A variable is adjoined from outside: it carries no fixed interpretation, receives a value only through a substitution $\sigma : X \to \operatorname{Tree}_\Omega(X)$ or an assignment into an algebra, and is exactly the kind of leaf that substitution replaces. The construction of $\mathbf{T}_\Omega(X)$ requires $X \cap \Omega = \varnothing$; identifying $X$ with $\Omega_0$ destroys both freeness and the substitution calculus.

### 4.6. Typed and Many-Sorted Trees

The single-sorted theory above suffices for untyped syntax: every node accepts a child in any position, subject only to rank. Typed syntax adds a discipline of **sorts** that constrains which trees may occupy which child positions. The typed theory is introduced here only after the ranked theory is in hand, and the central later use — typed contexts and typed rewriting — is built on it in Sections 11 and 14.

> [!definition] Definition 4.15: Many-sorted signature
> A **many-sorted signature** is a triple $(S, \Sigma, \tau)$ where $S$ is a set of **sorts**; $\Sigma$ is a set of **operation symbols**; and $\tau$ assigns to each $f \in \Sigma$ a **type**
>
> $$
> \tau(f) = (s_1, \dots, s_n; s) \in S^{<\omega} \times S,
> $$
>
> written $f : s_1 \times \cdots \times s_n \to s$. Here $n$ is the **arity** of $f$, the sequence $(s_1, \dots, s_n)$ its **input sorts** (the $i$-th argument must have sort $s_i$), and $s$ its **output sort** (synonym: **result sort**). Symbols with $n = 0$ are **constants of sort $s$**, $c : {} \to s$. A set $X = (X_s)_{s \in S}$ of **sorted variables** adjoins, for each sort, rank-zero generators of that sort, with $X_s \cap \Sigma = \varnothing$.

> [!definition] Definition 4.16: Well-sorted (typed) tree
> Fix $(S, \Sigma, \tau)$ and sorted variables $X = (X_s)$. The **well-sorted trees of sort $s$**, forming the set $\operatorname{Tree}_\Sigma(X)_s$, are defined by simultaneous recursion over $S$:
>
> 1. for each variable $x \in X_s$, the atom $x$ is a well-sorted tree of sort $s$;
> 2. for each constant $c : {} \to s$, the atom $c$ is a well-sorted tree of sort $s$;
> 3. for each $f : s_1 \times \cdots \times s_n \to s$ and well-sorted trees $t_i$ of sort $s_i$ ($1 \le i \le n$), the tree $f(t_1, \dots, t_n)$ is a well-sorted tree of sort $s$.
>
> A well-sorted tree has a **unique sort** $\operatorname{sort}(t) \in S$, namely the output sort of its root symbol (or the sort of its root variable); the family $(\operatorname{Tree}_\Sigma(X)_s)_{s \in S}$ is an $S$-sorted set.

> [!proposition] Proposition 4.17: Typed trees are arity-correct trees with a sort constraint
> Every well-sorted tree, with sorts forgotten, is an arity-correct tree over the ranked alphabet $(X \sqcup \Sigma, \rho)$ where $\rho(x) = 0$ for $x \in X$ and $\rho(f) = n$ for $f$ of arity $n$. Conversely an arity-correct tree over this alphabet is well-sorted iff at every internal node $p$ with $\ell(p) = f : s_1 \times \cdots \times s_n \to s$ the $i$-th child's root symbol has output sort $s_i$, and at every variable/constant leaf the declared sort is consistent up the tree. Thus the well-sorted trees are exactly the arity-correct trees satisfying a local sort-matching predicate at every edge.
>
> [!proof-sketch] Proof Sketch 4.17
> Forgetting sorts preserves the child count $= $ arity equation, giving arity-correctness. The converse characterization is the observation that clause (3) of Definition 4.16 constrains each argument's sort to the corresponding input sort, a condition local to each parent–child edge; a global induction on height shows the family of edge-local constraints is equivalent to membership in some $\operatorname{Tree}_\Sigma(X)_s$. Uniqueness of the sort is unique readability (Proposition 4.8) plus determinism of output sorts.

> [!warning] Warning 4.18: Sort-correctness is a genuine restriction
> In the single-sorted setting any arity-correct grafting $a(t_1,\dots,t_n)$ is a legal tree. In the typed setting $f(t_1,\dots,t_n)$ is legal only when each $\operatorname{sort}(t_i)$ equals the declared input sort $s_i$; otherwise the grafting is undefined, even though the child counts match. This sort side-condition propagates into the typed forms of replacement, plugging, substitution, matching, and rewriting (Sections 9, 11, 12, 13, 14): each of those operations acquires a sort-compatibility hypothesis without which its result is not a well-sorted tree. The single-sorted theory is the special case $|S| = 1$, in which the sort constraint is vacuous.

> [!remark] Remark 4.19: One-sorted first, typed as decoration
> The remainder of the core (Sections 5–10, 12–16) is developed in the single-sorted ranked setting, where statements are cleanest and the sort side-conditions are absent. The typed/many-sorted refinements are collected at the points where they alter the mathematics: typed contexts (Section 11), typed substitution and typed matching (Sections 12.6 and 13.6), and typed rewriting (Section 14.7). In each case the refinement is exactly "impose the sort-matching predicate of Proposition 4.17 on every operation," and the single-sorted theorem specializes by taking $|S| = 1$.

---

## 5. Trees and Orders

Trees are order-theoretic objects in two complementary ways: the ancestor relation is a well-founded partial order with least element, and the immediate-subtree relation is the cover relation that drives structural recursion. This section develops exactly the order theory the calculus consumes — enough to legitimize induction and recursion on trees — and no more.

### 5.1. The Ancestor Order and Its Anatomy

> [!definition] Definition 5.1: Ancestor order of a tree
> For a tree $t = (D, \ell)$, the **ancestor order** is the restriction of the prefix order to the domain, $(D, \preceq)$. By Proposition 1.6 it is a partial order with least element $\varepsilon$ (the root) and is well-founded; by Definition 3.4 every principal down-set ${\downarrow}\,q$ is a finite chain (the ancestors of $q$) and every principal up-set ${\uparrow}\,p$ is the node set of the subtree at $p$.

> [!proposition] Proposition 5.2: Order-theoretic characterization of tree domains
> A finite poset $(P, \le)$ is order-isomorphic to the ancestor order of some tree domain iff it has a least element and every principal down-set is a chain. Under such an isomorphism: the root is the least element; the parent of a non-minimal $p$ is the unique cover of $p$ from below; leaves are the maximal elements; and adding a linear order on the covers of each element recovers an ordered rooted tree, hence (Proposition 2.7) a tree domain.
>
> [!proof-sketch] Proof Sketch 5.2
> ($\Rightarrow$) The ancestor order of a tree domain has least element $\varepsilon$ and chain down-sets (Definition 3.4). ($\Leftarrow$) Given $(P,\le)$ with these properties, the down-set ${\downarrow}p$ being a finite chain gives each non-least $p$ a unique lower cover (its parent), making $P$ a rooted tree poset; choosing a sibling order yields an ordered rooted tree, and Proposition 2.7 names its nodes by addresses. The correspondence carries minima to root, covers to parent edges, maxima to leaves.

The poset axioms "least element" and "chain down-sets" are precisely the abstract content of "rooted with unique ancestry": uniqueness of the path to the root is the chain condition on down-sets. This is the order-theoretic definition of a tree promised by the outline, and it is equivalent — modulo a sibling order — to all the presentations of Section 2.

### 5.2. The Immediate-Subtree Order

> [!definition] Definition 5.3: Immediate-subtree relation
> On the set $\operatorname{Tree}_L$ of all trees over $(L,\rho)$, the **immediate-subtree relation** $\vartriangleleft_1$ is defined by $s \vartriangleleft_1 t$ iff $s$ is an immediate subtree of $t$, i.e. $t = a(t_1,\dots,t_n)$ and $s = t_i$ for some $i$. Its transitive closure $\vartriangleleft$ is the **proper-subtree relation**: $s \vartriangleleft t$ iff $s = t|_p$ for some $p \neq \varepsilon$ in $D_t$. The reflexive closure $\trianglelefteq$ is the **subtree relation**: $s \trianglelefteq t$ iff $s = t|_p$ for some $p \in D_t$.

> [!proposition] Proposition 5.4: Well-foundedness of the subtree relation
> On $\operatorname{Tree}_L$ the proper-subtree relation $\vartriangleleft$ is well-founded: there is no infinite sequence $t_0 \vartriangleright t_1 \vartriangleright t_2 \vartriangleright \cdots$. Equivalently, every nonempty set of trees has a $\vartriangleleft$-minimal element, and the size function $t \mapsto |t|$ is a strictly $\vartriangleleft$-decreasing map into $(\mathbb{N}, <)$.
>
> [!proof-sketch] Proof Sketch 5.4
> If $s \vartriangleleft t$ then $s = t|_p$ with $p \neq \varepsilon$, and $|s| = |D_t|_p| < |D_t| = |t|$ because the subdomain $D_t|_p$ is a proper subset of $D_t$ (it omits at least $\varepsilon$'s other descendants and the nodes strictly above $p$). Thus $|{\cdot}|$ strictly decreases along $\vartriangleleft$, and an infinite descending $\vartriangleleft$-chain would force an infinite strictly decreasing chain in $\mathbb{N}$, impossible. Well-foundedness is equivalent to existence of minimal elements (using dependent choice, available in ZFC).

Well-foundedness of $\vartriangleleft$ in the finite setting is the single fact that makes structural induction and recursion legitimate; it is also exactly the statement that the initial-algebra recursion of Theorem 2.11 terminates. The reliance on finiteness is essential here: for infinite trees (Section 22) the subtree relation is not well-founded, and induction/recursion are replaced by coinduction/corecursion.

### 5.3. Structural Induction

> [!theorem] Theorem 5.5: Principle of structural induction on trees
> Let $P$ be a property of trees over $(L,\rho)$. Suppose that for every $a \in L$ of rank $n$ and all trees $t_1, \dots, t_n$,
>
> $$
> \big(P(t_1) \wedge \cdots \wedge P(t_n)\big) \;\Longrightarrow\; P\big(a(t_1,\dots,t_n)\big),
> $$
>
> the case $n = 0$ reading "$P(a)$ holds for every atom $a$." Then $P(t)$ holds for every tree $t \in \operatorname{Tree}_L$.
>
> [!proof-sketch] Proof Sketch 5.5
> Suppose not; let $S = \{t : \neg P(t)\}$ be nonempty. By well-foundedness of $\vartriangleleft$ (Proposition 5.4) pick a $\vartriangleleft$-minimal $t \in S$. Write $t = a(t_1,\dots,t_n)$ (unique readability). Each $t_i \vartriangleleft t$, so by minimality $t_i \notin S$, i.e. $P(t_i)$ holds for all $i$; the induction hypothesis then forces $P(t)$, contradicting $t \in S$. Hence $S = \varnothing$.

> [!remark] Remark 5.6: Two induction schemes
> Two well-founded relations support two superficially different but interderivable inductions. **Structural induction** (Theorem 5.5) descends along $\vartriangleleft_1$ to immediate subtrees and is the form used for definitions and proofs phrased with constructor notation. **Induction on height** (or on size) descends along the natural-number measure $\operatorname{ht}$ (or $|{\cdot}|$) and is the form used when a global numerical bound organizes the argument. Both are instances of well-founded induction on $\operatorname{Tree}_L$; the measure-based form follows from Proposition 5.4 because $\operatorname{ht}$ and $|{\cdot}|$ strictly decrease to immediate subtrees.

### 5.4. Structural Recursion

> [!theorem] Theorem 5.7: Structural recursion theorem (single-sorted)
> Let $A$ be a set and suppose given, for each label $a \in L$ of rank $n$, a function $h_a : A^n \to A$ (a constant $h_a \in A$ when $n = 0$). Then there exists a **unique** function
>
> $$
> H : \operatorname{Tree}_L \to A \qquad\text{with}\qquad H\big(a(t_1,\dots,t_n)\big) = h_a\big(H(t_1), \dots, H(t_n)\big) \quad\text{for all } a, t_1, \dots, t_n.
> $$
>
> $H$ is the **fold** (synonym: **catamorphism**, **structural recursion**) determined by the family $(h_a)_{a \in L}$.
>
> [!proof-sketch] Proof Sketch 5.7
> Existence: define $H$ by well-founded recursion on $\vartriangleleft$ (legitimate by Proposition 5.4), the displayed equation being a valid recursion clause since the arguments $t_i$ are $\vartriangleleft$-below $a(t_1,\dots,t_n)$ and the clause is exhaustive and deterministic by unique readability (Proposition 4.8). Uniqueness: if $H'$ satisfies the same equation, then $H = H'$ by structural induction (Theorem 5.5), the inductive step being immediate from the shared clause. Abstractly, $H$ is the unique $F_L$-algebra homomorphism from the initial algebra $\operatorname{Tree}_L$ to the $F_L$-algebra $A$ with structure map $(a, \vec x) \mapsto h_a(\vec x)$ (Theorem 2.11).

Theorem 5.7 is the engine behind every measure and every shape-preserving transformation in the sequel: size, height, leaf count, support, yield, evaluation, pretty-printing, and the homomorphic extension of a substitution are all folds, each obtained by naming the family $(h_a)$. The uniqueness clause is as important as existence: it guarantees that two recursive specifications agreeing on the constructor clauses define the same function, which is the mechanism behind nearly every later identity proved "by structural induction."

> [!warning] Warning 5.8: Recursion needs well-definedness on the actual carrier
> Theorem 5.7 produces a total function on the absolutely free carrier $\operatorname{Tree}_L$, where the constructor clauses never conflict because unique readability makes the decomposition $t = a(\vec t\,)$ unique. On a **quotient** carrier $\operatorname{Tree}_L/{\equiv}$ the same clauses may conflict — two representatives of a class might recurse to different values — and recursion requires the additional **descent** hypothesis that the family $(h_a)$ respects $\equiv$ (Section 16). The free case is the one where recursion is unconditional; the quotient case is the one where it carries a proof obligation.

### 5.5. Recursion Along Descendants and Height

> [!construction] Construction 5.9: Decorating a tree by a fold
> Given a fold $H : \operatorname{Tree}_L \to A$, the **decoration** of a tree $t$ by $H$ is the function $\alpha_H^t : D_t \to A$, $\alpha_H^t(p) := H(t|_p)$, recording at each node the fold value of the subtree it roots. Decorations are computed bottom-up: $\alpha_H^t(p) = h_{\ell(p)}\big(\alpha_H^t(p\cdot 1), \dots, \alpha_H^t(p \cdot k)\big)$, so a single postorder pass evaluates $\alpha_H^t$ at every node, with the root value $\alpha_H^t(\varepsilon) = H(t)$.

This makes precise the sense in which "recursion along descendants" computes a value at every node simultaneously, and it is the formal basis of synthesized attributes (Section 20.3 below in the survey) and of incremental recomputation (Section 23). The dual, **inherited** decorations, are computed top-down by recursion along the ancestor chain — depth is the prototype, $\operatorname{depth}(\varepsilon) = 0$ and $\operatorname{depth}(p \cdot i) = \operatorname{depth}(p) + 1$ — and rest on the well-foundedness of the ancestor order rather than the subtree order.

---

## 6. Tree Metrics and Measures

Quantitative structure on trees comes in two strictly distinct flavors that the outline insists be separated: **node metrics**, which measure the relation of two nodes inside one fixed tree, and **tree metrics/measures**, which measure one tree or compare two trees. This section develops both, keeping the distinction explicit, and isolates the measures most relevant to syntax: size, height, depth, leaf count, variable-occurrence count, and tree edit distance.

### 6.1. Numerical Measures of a Single Tree

> [!definition] Definition 6.1: Basic fold measures
> For a tree $t = (D, \ell)$ over $(L, \rho)$ define, each as a fold (Theorem 5.7):
>
> $$
> |t| := |D| \ (\text{size}), \qquad \operatorname{ht}(t) := \max_{p \in D}|p| \ (\text{height}), \qquad \operatorname{leaf}(t) := |\partial D| \ (\text{leaf count}),
> $$
>
> with constructor recurrences, for $t = a(t_1, \dots, t_n)$,
>
> $$
> |t| = 1 + \sum_{i=1}^n |t_i|, \qquad \operatorname{ht}(t) = \begin{cases} 0, & n = 0,\\ 1 + \max_i \operatorname{ht}(t_i), & n > 0,\end{cases} \qquad \operatorname{leaf}(t) = \begin{cases} 1, & n = 0,\\ \sum_i \operatorname{leaf}(t_i), & n > 0.\end{cases}
> $$

> [!definition] Definition 6.2: Occurrence counts and support
> For $a \in L$, the **occurrence count** is $\#_a(t) := |\{p \in D : \ell(p) = a\}|$, a fold with $h_b(x_1,\dots,x_n) = [b = a] + \sum_i x_i$. The **label support** is $\operatorname{supp}(t) := \{a \in L : \#_a(t) > 0\}$, a fold with $h_a(S_1,\dots,S_n) = \{a\} \cup \bigcup_i S_i$. When $L = X \sqcup \Omega$, the **variable support** is $\operatorname{Var}(t) := \operatorname{supp}(t) \cap X$ and the **variable-occurrence count** is $\sum_{x \in X} \#_x(t)$; these control the substitution and rewriting calculus (the side-condition $\operatorname{Var}(r) \subseteq \operatorname{Var}(\ell)$ in Section 14 is a support containment).

> [!definition] Definition 6.3: Path-length and balance measures
> The **external path length** $\operatorname{EPL}(t) := \sum_{p \in \partial D} |p|$ sums leaf depths; the **internal path length** $\operatorname{IPL}(t) := \sum_{p \in D \setminus \partial D} |p|$ sums internal-node depths. A local **imbalance** at an internal node $p$ is $\max_i \operatorname{subht}_t(p\cdot i) - \min_i \operatorname{subht}_t(p \cdot i)$, and the **global imbalance** $\operatorname{imb}(t)$ is the maximum of these over internal nodes. These measures govern the cost of search, evaluation, and proof traversal: trees with equal leaf count can have widely different $\operatorname{EPL}$, hence different average access cost.

> [!remark] Remark 6.4: Width versus size versus height as complexity parameters
> The three parameters control different resources. Size $|t|$ is the baseline input size and bounds the work of any single full traversal. Height $\operatorname{ht}(t)$ bounds the recursion depth (stack usage) of a depth-first computation. Width $\operatorname{width}(t) = \max_k |D_k|$ bounds the queue or frontier size of a breadth-first computation. For a fixed size, these can vary independently: a path (each internal node unary) has height $|t|-1$ and width $1$; a shallow bushy tree has height $1$ and width $|t|-1$. Algorithmic claims must name which parameter they bound.

### 6.2. Node Metrics Within a Tree

> [!definition] Definition 6.5: Least common ancestor and node distance
> Fix a tree $t = (D, \ell)$. For $p, q \in D$ the **least common ancestor** $\operatorname{lca}(p,q)$ is the longest common prefix of $p$ and $q$ as sequences; it lies in $D$ by prefix closure and is the $\preceq$-greatest node $\preceq$ both $p$ and $q$. The **node distance** in the underlying (undirected, unit-weight) tree graph is
>
> $$
> d_t(p, q) := \big(|p| - |\operatorname{lca}(p,q)|\big) + \big(|q| - |\operatorname{lca}(p,q)|\big),
> $$
>
> the number of edges on the unique simple path from $p$ to $q$, namely up from $p$ to $\operatorname{lca}(p,q)$ then down to $q$.

> [!proposition] Proposition 6.6: $d_t$ is a metric on the nodes of $t$
> For each fixed tree $t$, $d_t$ is a metric on $D$: $d_t(p,q) \ge 0$ with equality iff $p = q$; $d_t(p,q) = d_t(q,p)$; and $d_t(p, r) \le d_t(p, q) + d_t(q, r)$. It is the graph (shortest-path) metric of the underlying undirected tree, where every two nodes are joined by a unique simple path.
>
> [!proof-sketch] Proof Sketch 6.6
> Nonnegativity and identity-of-indiscernibles follow because $|p|, |q| \ge |\operatorname{lca}(p,q)|$ with simultaneous equality iff $p = q = \operatorname{lca}(p,q)$. Symmetry is manifest. The triangle inequality is the general fact that shortest-path length in a connected graph is a metric; in a tree the unique-path formula via the lca makes it exact, and inserting the intermediate node $q$ can only lengthen the route.

> [!warning] Warning 6.7: Node metric versus tree metric
> $d_t(p,q)$ measures two **nodes inside one tree** $t$; it is undefined for nodes of different trees, since addresses have no cross-tree meaning. A **distance between two trees** $t, t'$ — such as edit distance (Definition 6.8) — is a different object with a different type: $\operatorname{Tree}_L \times \operatorname{Tree}_L \to \mathbb{N}$, not $D \times D \to \mathbb{N}$. Conflating the two ("the distance between these subtrees") is a type error unless one specifies whether the subtrees are compared as positions in a common host tree (node metric) or as standalone trees (tree metric).

### 6.3. Metrics and Distances Between Trees

> [!definition] Definition 6.8: Tree edit distance
> Fix a set of **primitive edits** on labelled trees — typically: relabel a node, delete a node (splicing its children into its parent's child list), and insert a node — each with a nonnegative **cost**. The **tree edit distance** $\delta(t, t')$ is the minimum total cost of a sequence of primitive edits transforming $t$ into $t'$. With unit costs and the standard ordered-tree edit model, $\delta$ is computable in polynomial time by dynamic programming over the postorder structure.

> [!proposition] Proposition 6.9: Edit distance is a (pseudo)metric
> If the primitive edit costs are symmetric (each edit's inverse is available at equal cost) and positive for any edit that changes the tree, then $\delta$ is a metric on $\operatorname{Tree}_L$: $\delta(t,t') \ge 0$ with equality iff $t = t'$, $\delta$ is symmetric, and $\delta$ satisfies the triangle inequality.
>
> [!proof-sketch] Proof Sketch 6.9
> Symmetry: reverse an optimal edit script and use cost symmetry. Triangle inequality: concatenating an optimal $t \to t'$ script with an optimal $t' \to t''$ script is an admissible $t \to t''$ script, so $\delta(t,t'') \le \delta(t,t') + \delta(t',t'')$. Identity of indiscernibles: any nonempty script has positive cost, and $t = t'$ is reached by the empty script of cost $0$.

> [!warning] Warning 6.10: Edit distance is syntactic, not semantic
> Tree edit distance measures syntactic dissimilarity of shape and labels. It is not a logical or semantic invariant: two formulas may be edit-close yet logically unrelated, or edit-far yet equivalent under the congruence of a theory (Section 16). For the same reason $\delta$ does not in general respect the operations — it is not built to satisfy a congruence property — so it should be used as a heuristic similarity measure (clustering proof terms, suggesting repairs, near-match detection) and never as a stand-in for quotient equality. The prefix metric on infinite trees (Section 22) is a genuinely different inter-tree metric, defined by agreement up to depth, and is the one that interacts well with the coalgebraic structure.

---

## 7. Tree Decomposition

The operations of the calculus all rest on ways of breaking a tree into parts and reassembling them. This section catalogues the decompositions and proves the decomposition uniqueness facts on which replacement, contexts, and rewriting depend. The crowning decomposition — tree $=$ context plus focused subtree — is the conceptual bridge to Sections 9–14 and is treated last.

### 7.1. Root and Immediate-Subtree Decomposition

> [!proposition] Proposition 7.1: Root decomposition
> Every nonempty tree $t$ decomposes uniquely as $t = a(t_1, \dots, t_n)$ with $a = \ell_t(\varepsilon)$, $n = \rho(a)$, and $t_i = t|_i$. This is unique readability (Proposition 4.8) restated as a decomposition: the root label and the ordered list of immediate subtrees are a complete, irredundant set of data for $t$.

Root decomposition is the one-step, top-level decomposition; iterating it is structural recursion. It is the decomposition exposed by the initial-algebra structure map (Theorem 2.11) and is the form in which the recursive presentation (Section 2.5) operates.

### 7.2. Decomposition by Position; Subtree Extraction

> [!definition] Definition 7.2: Subtree at a position (labelled)
> Let $t = (D, \ell)$ and $p \in D$. The **subtree of $t$ at $p$** is
>
> $$
> t|_p := (D|_p, \ell_p), \qquad D|_p = \{\, q \in \mathbb{A} : p \cdot q \in D \,\}, \qquad \ell_p(q) := \ell(p \cdot q),
> $$
>
> the substructure rooted at $p$, readdressed so that $p$ becomes the new root. (The companion notes write $t \downarrow p$ for the same object; the two notations are synonymous, and $t|_p$ is used here as primary.) Then $t|_\varepsilon = t$, $(t|_p)|_q = t|_{p \cdot q}$, and $t|_{i} $ is the $i$-th immediate subtree.

> [!proposition] Proposition 7.3: Extraction is a fold-compatible projection
> Subtree extraction satisfies, for $t = a(t_1,\dots,t_n)$: $t|_\varepsilon = t$ and $t|_{i \cdot q} = t_i|_q$. Consequently every fold $H$ commutes with extraction through its decoration, $H(t|_p) = \alpha_H^t(p)$ (Construction 5.9), and label support, size, and height of a subtree are read off the corresponding decoration at $p$.
>
> [!proof-sketch] Proof Sketch 7.3
> The recurrences $t|_\varepsilon = t$ and $t|_{i\cdot q} = t_i|_q$ are immediate from $D|_{i \cdot q} = (D|_i)|_q$ and the corresponding label identity, using the domain formula of Definition 4.7. The fold statement is Construction 5.9 specialized to extraction; it is proved by induction on $|p|$.

### 7.3. Frontier and Path Decompositions

> [!definition] Definition 7.4: Frontier word (yield)
> The **frontier word** or **yield** of $t$, $\operatorname{yield}(t) \in L^{<\omega}$, is the left-to-right sequence of leaf labels, the fold with $h_a() = a$ for $\rho(a) = 0$ and $h_a(w_1, \dots, w_n) = w_1 \cdot {} \cdots {} \cdot w_n$ for $n > 0$. The frontier decomposition expresses the leaf data of $t$ as a single word; it forgets the internal structure and is the datum a parse tree contributes to a grammar derivation.

> [!definition] Definition 7.5: Cut and path decomposition
> A **cut** of $t$ at a node $p$ separates $t$ into the **upper part** — the context $t[p := \Box]$ obtained by deleting the subtree below $p$ and marking $p$ (Section 8.x/Section 10) — and the **lower part** $t|_p$. A **path decomposition** along a branch $\varepsilon \prec p_1 \prec \cdots \prec p_m$ (each $p_{j+1}$ a child of $p_j$) records, at each step, the label and the off-path sibling subtrees; this is exactly the data of a zipper (Section 23) and of a nested one-hole context.

### 7.4. Context–Subtree Decomposition

> [!theorem] Theorem 7.6: Context–subtree decomposition and uniqueness
> Let $t = (D, \ell)$ be a tree and $p \in D$. Write $C := t[p := \Box]$ for the one-hole context obtained by replacing the subtree at $p$ with the hole $\Box$ (Definition 10.4), and $s := t|_p$ for the subtree at $p$. Then
>
> $$
> t \;=\; C[s],
> $$
>
> the plugging of $s$ into the unique hole of $C$. Moreover the pair $(C, s)$ is **uniquely determined by the position $p$**: for each $p \in D$ there is exactly one one-hole context with hole at $p$ and exactly one subtree filling it that reproduce $t$, and conversely each one-hole context $C$ with hole address $h$ and each tree $s$ yield $t = C[s]$ with $p = h$, $C = t[p:=\Box]$, $s = t|_p$.
>
> [!proof-sketch] Proof Sketch 7.6
> Outside the subtree at $p$ — at addresses $q$ with $p \npreceq q$ — the context $C$ keeps the labels and addresses of $t$ unchanged; at $p$ it carries the hole. Plugging $s = t|_p$ into the hole reinserts exactly the addresses $p \cdot q$ for $q \in D|_p$ with labels $\ell(p \cdot q)$, which are precisely the descendants of $p$ in $t$ with their original labels (Definitions 10.4, 10.6). Hence $C[s]$ and $t$ agree on domain and labelling, so $C[s] = t$. Uniqueness: the hole of a one-hole context occupies a single address, which must be $p$ to recover the deleted subtree's location; given $p$, the context's labelled domain off $p$ is forced to equal $t$'s, and the filler is forced to equal $t|_p$.

> [!remark] Remark 7.7: The master decomposition
> Theorem 7.6 is the structural heart of the calculus: it says every tree, at every one of its positions, factors canonically as
>
> $$
> \text{tree} \;=\; \text{context} \;+\; \text{focused subtree},
> $$
>
> with the context recording "everything except the focus" and the subtree recording "the focus." Subtree extraction reads off the second factor; replacement substitutes a new second factor; rewriting replaces the focus by a rule-image; the zipper stores the pair $(C, s)$ for efficient local editing. Every position-indexed operation in Sections 9, 10, 13, and 14 is an operation on this factorization. The decomposition is unique for one-hole contexts; for multi-hole contexts the analogous decomposition records several disjoint foci simultaneously (Section 10.6), with uniqueness relative to the chosen set of pairwise-disjoint positions.

---

## 8. Tree Algebras

Trees over a signature are not merely a set; they carry the operations that build them, and with respect to those operations they form an algebra with a sharp universal property. This section develops the single-sorted tree algebra, identifies it with the absolutely free algebra and with the term algebra, and isolates the two facts — generatedness and unique decomposition — whose conjunction is freeness. The universal-algebraic vocabulary is recalled in the minimal form the development needs.

### 8.1. Signatures, Algebras, Homomorphisms (Recalled)

> [!definition] Definition 8.1: $\Omega$-algebra and homomorphism
> A **signature** $\Omega$ is a set of operation symbols with arity $\operatorname{ar} : \Omega \to \mathbb{N}$; $\Omega_n = \operatorname{ar}^{-1}(n)$. An **$\Omega$-algebra** $\mathbf{A} = (A, (f^{\mathbf{A}})_{f \in \Omega})$ is a carrier set $A$ with, for each $f \in \Omega_n$, an operation $f^{\mathbf{A}} : A^n \to A$ (a distinguished element $c^{\mathbf{A}} \in A$ when $n = 0$). A **homomorphism** $h : \mathbf{A} \to \mathbf{B}$ is a function $h : A \to B$ with $h(f^{\mathbf{A}}(a_1,\dots,a_n)) = f^{\mathbf{B}}(h(a_1),\dots,h(a_n))$ for all $f \in \Omega_n$ and $a_i \in A$; for $n = 0$, $h(c^{\mathbf{A}}) = c^{\mathbf{B}}$. Boldface $\mathbf{A}, \mathbf{B}$ denote algebras, italic $A, B$ their carriers.

> [!definition] Definition 8.2: Generated subalgebra, generatedness
> A subset $C \subseteq A$ is **closed** if $f^{\mathbf{A}}(c_1,\dots,c_n) \in C$ whenever $f \in \Omega_n$ and $c_i \in C$ (including $c^{\mathbf{A}} \in C$ for $c \in \Omega_0$). The **subalgebra generated by** $S \subseteq A$ is $\langle S \rangle_{\mathbf{A}} := \bigcap\{C : S \subseteq C,\ C \text{ closed}\}$, the least closed superset of $S$; $\mathbf{A}$ is **generated by** $S$ when $\langle S \rangle_{\mathbf{A}} = A$. In the finitary setting $\langle S \rangle_{\mathbf{A}} = \bigcup_{k<\omega} S^{(k)}$ with $S^{(0)} = S \cup \{c^{\mathbf{A}} : c \in \Omega_0\}$ and $S^{(k+1)} = S^{(k)} \cup \{f^{\mathbf{A}}(\vec a) : f \in \Omega_{\ge 1}, \vec a \in (S^{(k)})^{\operatorname{ar}(f)}\}$.

### 8.2. The Tree Algebra over a Signature

> [!definition] Definition 8.3: Tree algebra
> Let $\Omega$ be a signature and $X$ a set of variables with $X \cap \Omega = \varnothing$, ranked so that $\rho(x) = 0$ for $x \in X$ and $\rho(f) = \operatorname{ar}(f)$ for $f \in \Omega$. The **tree algebra** $\mathbf{T}_\Omega(X)$ has carrier $T_\Omega(X) := \operatorname{Tree}_{X \sqcup \Omega}$ (the arity-correct term trees, Definition 4.6) and, for each $f \in \Omega_n$, the **constructor operation**
>
> $$
> f^{\mathbf{T}} : T_\Omega(X)^n \to T_\Omega(X), \qquad f^{\mathbf{T}}(t_1, \dots, t_n) := f(t_1, \dots, t_n),
> $$
>
> the grafting of a fresh root labelled $f$ over the $t_i$ (Definition 4.7). The constructor operations are the **basic operations** of $\mathbf{T}_\Omega(X)$; the constants $c \in \Omega_0$ are interpreted as the atomic trees $c$. The **generator insertion** is $\eta : X \to T_\Omega(X)$, $\eta(x) := x$ (the one-node variable tree).

> [!warning] Warning 8.4: Formal constructor versus interpreted operation
> The symbol $f \in \Omega_n$ has two meanings that must never be identified. As a **constructor** $f^{\mathbf{T}}$ it builds a strictly larger tree $f(t_1,\dots,t_n)$ and forgets nothing — its output records its inputs verbatim as immediate subtrees. As an **interpreted operation** $f^{\mathbf{B}}$ in a target algebra $\mathbf{B}$ it computes an element of $B$ and may collapse information. The equation $f^{\mathbf{T}}(t_1,\dots,t_n) = f^{\mathbf{B}}(b_1,\dots,b_n)$ is type-incorrect: the left side is a tree, the right an element of $B$. The two are related only through evaluation homomorphisms (Section 8.6).

### 8.3. Destructors and Unique Decomposition

> [!definition] Definition 8.5: Destructors
> On $\mathbf{T}_\Omega(X)$ define the partial **destructors**: the **root-label** map $\operatorname{rt} : T_\Omega(X) \to X \sqcup \Omega$, $\operatorname{rt}(t) := \ell_t(\varepsilon)$; and, for $1 \le i \le \rho(\operatorname{rt}(t))$, the **$i$-th immediate-subtree** map $t \mapsto t|_i$. These invert the constructors: $\operatorname{rt}(f(t_1,\dots,t_n)) = f$ and $(f(t_1,\dots,t_n))|_i = t_i$.

> [!proposition] Proposition 8.6: Unique decomposition
> The constructor operations and the variable atoms partition $T_\Omega(X)$: every tree $t$ is either a variable atom $x$ ($x \in X$), a constant atom $c$ ($c \in \Omega_0$), or $f(t_1,\dots,t_n)$ for a unique $f \in \Omega_{\ge 1}$ and unique $t_1,\dots,t_n$. Equivalently the map
>
> $$
> X \;\sqcup\; \coprod_{f \in \Omega} T_\Omega(X)^{\operatorname{ar}(f)} \;\xrightarrow{\ \cong\ }\; T_\Omega(X), \qquad x \mapsto x, \ (f, \vec t\,) \mapsto f(\vec t\,),
> $$
>
> is a bijection (the disjoint sum of the generator insertion and the constructor maps).
>
> [!proof-sketch] Proof Sketch 8.6
> This is unique readability (Proposition 4.8) over the alphabet $X \sqcup \Omega$, with the rank-zero labels split into variables ($X$) and constants ($\Omega_0$). The root label classifies $t$ into the variable, constant, or compound case disjointly, and in the compound case the immediate subtrees are recovered by the destructors $t|_i$. Disjointness of the cases uses $X \cap \Omega = \varnothing$.

Unique decomposition is the algebraic content of "syntax is a free construction": the constructors are jointly injective and have disjoint images, and together with the generators they exhaust the carrier. This is exactly the hypothesis that converts generatedness into freeness.

### 8.4. Freeness of the Tree Algebra

> [!definition] Definition 8.7: Absolutely free algebra (universal mapping property)
> A pair $(\mathbf{F}, \eta)$ of an $\Omega$-algebra and an insertion $\eta : X \to F$ is **absolutely free on $X$** if for every $\Omega$-algebra $\mathbf{A}$ and every assignment $g : X \to A$ there is a **unique** homomorphism $\widehat{g} : \mathbf{F} \to \mathbf{A}$ with $\widehat{g} \circ \eta = g$. Equivalently, restriction along $\eta$ is a bijection $\operatorname{Hom}_\Omega(\mathbf{F}, \mathbf{A}) \to A^X$ for every $\mathbf{A}$.

> [!theorem] Theorem 8.8: The tree algebra is absolutely free
> For every signature $\Omega$ and variable set $X$ with $X \cap \Omega = \varnothing$, the pair $(\mathbf{T}_\Omega(X), \eta)$ is absolutely free on $X$. Explicitly, for each assignment $g : X \to A$ into an $\Omega$-algebra $\mathbf{A}$, the homomorphic extension $\widehat g$ is the unique fold (Theorem 5.7) determined by the family $h_x := g(x)$ (for $x \in X$) and $h_f := f^{\mathbf{A}}$ (for $f \in \Omega$):
>
> $$
> \widehat g(x) = g(x), \qquad \widehat g\big(f(t_1,\dots,t_n)\big) = f^{\mathbf{A}}\big(\widehat g(t_1), \dots, \widehat g(t_n)\big).
> $$
>
> [!proof-sketch] Proof Sketch 8.8
> Existence: the displayed clauses are exactly the constructor clauses of a fold into $A$, with the variable atoms sent by $g$ and each operation symbol interpreted by $f^{\mathbf{A}}$; Theorem 5.7 produces a unique function $\widehat g$ satisfying them, and the second clause is the homomorphism condition, so $\widehat g$ is a homomorphism extending $g$. Uniqueness: any homomorphism $k$ with $k \circ \eta = g$ satisfies the same two clauses (the first because $k\circ\eta = g$, the second because $k$ is a homomorphism), hence equals $\widehat g$ by the uniqueness clause of Theorem 5.7. Thus restriction along $\eta$ is bijective.

> [!theorem] Theorem 8.9: Freeness = generatedness + unique decomposition
> Let $\mathbf{A}$ be an $\Omega$-algebra with insertion $\eta : X \to A$. Then $(\mathbf{A}, \eta)$ is absolutely free on $X$ iff (i) $\mathbf{A}$ is generated by $\eta[X]$ (**generatedness**) and (ii) the combined map $X \sqcup \coprod_f A^{\operatorname{ar}(f)} \to A$, $x \mapsto \eta(x)$, $(f,\vec a) \mapsto f^{\mathbf{A}}(\vec a)$, is injective (**unique decomposition**: distinct generators are distinct, generators are not values of operations, and operations are jointly injective with disjoint images).
>
> [!proof-sketch] Proof Sketch 8.9
> ($\Rightarrow$) Freeness implies generatedness (the subalgebra $\langle \eta[X]\rangle$ admits a retraction by the UMP applied to the corestricted insertion, forcing it to be all of $A$) and implies unique decomposition (the unique comparison homomorphism from $\mathbf{T}_\Omega(X)$ is an isomorphism, transporting Proposition 8.6). ($\Leftarrow$) Generatedness makes the canonical comparison homomorphism $\Phi : \mathbf{T}_\Omega(X) \to \mathbf{A}$ (the extension of $\eta$) surjective; unique decomposition makes $\Phi$ injective by structural induction comparing decompositions; an isomorphism transports freeness from $\mathbf{T}_\Omega(X)$ (Theorem 8.8) to $\mathbf{A}$.

> [!corollary] Corollary 8.10: Uniqueness of free algebras up to unique isomorphism over $X$
> Any two absolutely free $\Omega$-algebras on the same $X$ are isomorphic by a **unique** isomorphism commuting with the insertions. In particular every concrete presentation of syntax that is generated by its variable atoms and satisfies unique decomposition — recursive term expressions, address trees, tagged tuples, well-formed strings — is canonically isomorphic to $\mathbf{T}_\Omega(X)$, and the isomorphism is the unique generator-preserving one.
>
> [!proof-sketch] Proof Sketch 8.10
> Apply the UMP of each free algebra to the other's insertion to obtain mutually inverse generator-preserving homomorphisms; their composites are endomorphisms fixing the generators, hence identities by the uniqueness clause of the UMP. Uniqueness of the isomorphism is the same rigidity. For a concrete presentation, Theorem 8.9 certifies freeness, and Corollary 8.10 supplies the canonical comparison with $\mathbf{T}_\Omega(X)$.

### 8.5. Term Algebras and Tree Algebras

> [!remark] Remark 8.11: Terms and trees are canonically isomorphic, not identical
> The **term algebra** is the absolutely free algebra realized by recursively built formal expressions — strings of symbols, parentheses, and commas, or nested tuples $(f, t_1, \dots, t_n)$ — whereas the **tree algebra** $\mathbf{T}_\Omega(X)$ is realized by labelled address trees. Both are absolutely free on $X$ (each is generated by its variable atoms and satisfies unique decomposition), so by Corollary 8.10 there is a unique generator-preserving isomorphism between them. They are not the *same set* — a string is not a tree and a nested tuple is not an address map — and quantities tied to a presentation's internal encoding (string length, tuple nesting, address index sequences) do not transfer across the isomorphism, only the algebraic and operational structure does. The tree presentation is preferred in this treatise because it makes positions, subtrees, replacement, contexts, and rewriting elementary; the term presentation is preferred where linear input/output and parsing dominate.

### 8.6. Evaluation, Image, and Kernel

> [!definition] Definition 8.12: Evaluation homomorphism
> For an $\Omega$-algebra $\mathbf{B}$ and an assignment $g : X \to B$, the **evaluation** of syntax in $\mathbf{B}$ under $g$ is the homomorphic extension $\operatorname{ev}_g := \widehat g : \mathbf{T}_\Omega(X) \to \mathbf{B}$ of Theorem 8.8. It computes the value $\operatorname{ev}_g(t) \in B$ of a tree $t$ by interpreting each operation symbol as its operation in $\mathbf{B}$ and each variable by its $g$-value.

> [!theorem] Theorem 8.13: Image is the generated subalgebra; kernel is a congruence
> For every evaluation $\operatorname{ev}_g : \mathbf{T}_\Omega(X) \to \mathbf{B}$: the image $\operatorname{im}(\operatorname{ev}_g)$ is the subalgebra $\langle g[X] \rangle_{\mathbf{B}}$ generated by the values of the variables; and the kernel $\ker(\operatorname{ev}_g) = \{(t, t') : \operatorname{ev}_g(t) = \operatorname{ev}_g(t')\}$ is a congruence on $\mathbf{T}_\Omega(X)$. Consequently $\mathbf{T}_\Omega(X)/\ker(\operatorname{ev}_g) \cong \langle g[X]\rangle_{\mathbf{B}}$, and every generated $\Omega$-algebra is a quotient of free syntax by an evaluation kernel.
>
> [!proof-sketch] Proof Sketch 8.13
> The image of a homomorphism is a subalgebra, and the image of the generated subalgebra $\langle X \rangle_{\mathbf{T}} = T_\Omega(X)$ is $\langle g[X] \rangle_{\mathbf{B}}$ (homomorphisms carry generators to generators of the image). The kernel of any homomorphism is a congruence: it is an equivalence relation, and compatibility with each $f$ follows from preservation, $\operatorname{ev}_g(f(\vec t\,)) = f^{\mathbf{B}}(\operatorname{ev}_g \vec t\,)$. The isomorphism is the first isomorphism theorem for $\Omega$-algebras.

> [!remark] Remark 8.14: Why trees, specifically
> The free object is unique up to canonical isomorphism, so as an *abstract* algebra the choice of presentation is immaterial. Trees are singled out for the operational layer because the tree presentation makes available, as elementary set-theoretic operations on $(D, \ell)$, the entire calculus that the abstract UMP only implies: positions index the nodes, subtrees are restrictions and readdressings, replacement and contexts are deletions and re-graftings, substitution is the fold of an assignment, matching is shape comparison with binding, and a rewrite is a replacement at a matched position. The next sections develop this calculus, and every operation in it is presentation-specific machinery realizing structure that lives, abstractly, on the free algebra.

---

## 9. Tree Operations and the Calculus of Subtrees

This section develops the elementary operations of the tree calculus as a coherent system, with explicit domains of definition. The two operations that generate the rest are **subtree extraction** $t|_p$ and **subtree replacement** $t[p:=s]$; from them follow grafting, pruning, simultaneous replacement, and the composition laws that govern how replacements at different positions interact. Throughout, the setting is single-sorted ranked trees over $(L, \rho)$ (with $L = X \sqcup \Omega$ in syntactic applications); the typed refinements are noted in Section 9.7 and developed in Section 11.

### 9.1. Extraction

> [!definition] Definition 9.1: Subtree extraction
> For a tree $t = (D,\ell)$ and a position $p \in D$, the **extraction** of $t$ at $p$ is the subtree $t|_p = (D|_p, \ell_p)$ of Definition 7.2. Extraction is a **partial** operation: $t|_p$ is defined exactly when $p \in D_t$, i.e. $p$ is a valid position of $t$. Its **input data** are a tree and a position of that tree; its **output** is a tree.

> [!proposition] Proposition 9.2: Laws of extraction
> Extraction satisfies, whenever the relevant positions are valid:
>
> $$
> t|_\varepsilon = t, \qquad (t|_p)|_q = t|_{p \cdot q}, \qquad \big(a(t_1,\dots,t_n)\big)|_{i \cdot q} = t_i|_q.
> $$
>
> In particular the positions of $t|_p$ are exactly the residuals $\{q : p \cdot q \in D_t\} = D_t|_p$, and $(t|_p)|_q$ is defined iff $p \cdot q \in D_t$.
>
> [!proof-sketch] Proof Sketch 9.2
> Each identity is read off the domain and label formulas of Definition 7.2 together with $D|_{p \cdot q} = (D|_p)|_q$, which holds because $r \in (D|_p)|_q \Leftrightarrow p \cdot q \cdot r \in D \Leftrightarrow r \in D|_{p\cdot q}$; the label identity is the analogous computation $\ell(p\cdot q\cdot r)$.

### 9.2. Replacement

> [!definition] Definition 9.3: Subtree replacement
> For a tree $t = (D, \ell)$, a position $p \in D$, and a tree $s = (E, m)$, the **replacement** of the subtree at $p$ by $s$ is the tree $t[p := s] = (D', \ell')$ with
>
> $$
> D' := \{\, q \in D : p \npreceq q \,\} \;\cup\; \{\, p \cdot r : r \in E \,\}, \qquad \ell'(q) := \begin{cases} \ell(q), & p \npreceq q,\\ m(r), & q = p \cdot r,\ r \in E. \end{cases}
> $$
>
> Replacement is **partial**: $t[p:=s]$ is defined exactly when $p \in D_t$. Its **input data** are a host tree, a position of the host, and a replacement tree; its **output** is a tree. (In the typed setting it is defined only when additionally $\operatorname{sort}(s)$ matches the sort required at $p$; Section 9.7.)

> [!proposition] Proposition 9.4: Replacement is well-defined and arity-correct
> For $p \in D_t$ and any tree $s$, $t[p:=s]$ is a tree (a finite arity-correct labelled address domain), and
>
> $$
> (t[p:=s])|_p = s, \qquad (t[p:=s])|_q = t|_q \ \text{ for } q \mathbin{\|} p \text{ or } q \prec p \text{ with the focus spliced in}.
> $$
>
> More precisely $(t[p:=s])|_q = t|_q$ for every $q$ with $q \mathbin{\|} p$ (disjoint from the replacement site), and the new subtree at $p$ is exactly $s$.
>
> [!proof-sketch] Proof Sketch 9.4
> $D'$ is prefix-closed: a prefix of $p \cdot r$ is either a prefix of $p$ (in $D$, retained since $p \npreceq$ a strict prefix of $p$) or $p \cdot r'$ with $r' \preceq r$ (in $E$ by prefix-closure of $E$). Left-sibling closure and arity-correctness hold because off the site the labels and child sets are those of $t$, and at and below $p$ they are those of $s$ re-rooted at $p$, both arity-correct. The subtree identities follow by computing $D'|_p = E$ (the addresses $p\cdot r$, $r \in E$, readdressed) with labels $m$, giving $(t[p:=s])|_p = s$, and $D'|_q = D|_q$ with original labels for $q \mathbin\| p$.

> [!proposition] Proposition 9.5: Replacement factors through context extraction
> For every $t$, $p \in D_t$, and $s$,
>
> $$
> t[p := s] \;=\; \big(t[p := \Box]\big)[s] \;=\; C[s] \quad\text{where } C = t[p:=\Box],
> $$
>
> and in particular $t[p := t|_p] = t$. Thus replacement is exactly "extract the one-hole context at $p$, then plug $s$ into its hole," linking replacement (Section 9) to contexts (Section 10).
>
> [!proof-sketch] Proof Sketch 9.5
> Context extraction $t[p:=\Box]$ deletes the subtree below $p$ and marks $p$ with the hole; plugging $s$ reinserts $s$ at $p$. Comparing domain and label formulas with Definition 9.3 shows the two constructions coincide. The identity $t[p:=t|_p] = t$ is Theorem 7.6 ($t = C[t|_p]$) rewritten via this factorization.

### 9.3. Grafting, Pruning, and Restriction

> [!definition] Definition 9.6: Root grafting
> For $a \in L$ of rank $n$ and trees $t_1, \dots, t_n$, the **root grafting** is the constructor $a(t_1, \dots, t_n)$ of Definition 4.7: a fresh root labelled $a$ over the given children. Grafting is total on arity-matched inputs; it is the basic operation of the tree algebra (Section 8) and the synthesis side of root decomposition (Proposition 7.1).

> [!definition] Definition 9.7: Pruning and leaf grafting
> **Pruning** at a position $p$ replaces the subtree at $p$ by a designated atomic tree: given a rank-zero label $\bullet$ (a "stub"), $\operatorname{prune}_p(t) := t[p := \bullet]$. **Leaf grafting** is the special case of replacement in which the site $p$ is a leaf of $t$: when $\ell_t(p)$ has rank $0$, $t[p:=s]$ attaches $s$ at the former leaf $p$. Substitution (Section 12) is exactly simultaneous leaf grafting at every occurrence of selected variable leaves.

> [!definition] Definition 9.8: Restriction to a subtree
> The **restriction** of $t$ to the subtree at $p$ is the operation $t \mapsto t|_p$ regarded as forgetting everything outside ${\uparrow}\,p$; it is extraction (Definition 9.1). Restriction and grafting are inverse in the local sense $a(t|_1, \dots, t|_n) = t$ for an internal root (root decomposition) and $\big(a(t_1,\dots,t_n)\big)|_i = t_i$ (Proposition 9.2).

### 9.4. Simultaneous and Composed Replacement

> [!definition] Definition 9.9: Simultaneous replacement at disjoint positions
> Let $p_1, \dots, p_k \in D_t$ be **pairwise disjoint** ($p_i \mathbin\| p_j$ for $i \neq j$) and let $s_1, \dots, s_k$ be trees. The **simultaneous replacement** $t[p_1 := s_1, \dots, p_k := s_k]$ is the tree obtained by replacing, at each $p_i$, the subtree by $s_i$, all at once:
>
> $$
> D' := \{\, q \in D : p_i \npreceq q \ \forall i \,\} \;\cup\; \bigcup_{i=1}^k \{\, p_i \cdot r : r \in E_i \,\},
> $$
>
> with labels from $\ell$ off all sites and from $m_i$ inside site $i$. Pairwise disjointness guarantees the sites do not overlap, so the union is a well-defined tree.

> [!proposition] Proposition 9.10: Disjoint replacements commute; nested ones do not
> If $p \mathbin\| q$ then for all $s, r$,
>
> $$
> t[p := s][q := r] \;=\; t[q := r][p := s] \;=\; t[p := s,\ q := r].
> $$
>
> If instead $p \prec q$ (so $q$ lies inside the subtree at $p$), then $t[p:=s][q:=r]$ generally differs from $t[q:=r][p:=s]$: the outer replacement at $p$ deletes the site $q$, so the order is not interchangeable.
>
> [!proof-sketch] Proof Sketch 9.10
> For $p \mathbin\| q$, the two single replacements touch disjoint sets of addresses (the descendants of $p$ and of $q$ respectively, which are disjoint because neither prefixes the other), so they commute and their combined effect is the simultaneous replacement. For $p \prec q$: after $t[p:=s]$ the address $q = p \cdot r$ no longer indexes the original subtree (it now indexes a position of $s$, if present at all), so the second replacement acts on a different object; concretely take $s$ an atom, which removes $q$ entirely, making $t[p:=s][q:=r] = t[p:=s]$ while $t[q:=r][p:=s] = t[p:=s]$ only by accident — the general inequality is exhibited by any $s$ retaining position $r$ with a different subtree there.

> [!proposition] Proposition 9.11: Nesting law for comparable replacements
> If $p \preceq q$, write $q = p \cdot r$. Then replacement composes through the subtree:
>
> $$
> t[q := s] \;=\; t\big[\, p := (t|_p)[r := s] \,\big],
> $$
>
> i.e. replacing deep at $q$ equals replacing at the ancestor $p$ by the locally modified subtree. In particular every replacement reduces to a root-level replacement of an immediate subtree by recursion on $|p|$.
>
> [!proof-sketch] Proof Sketch 9.11
> Both sides agree off ${\uparrow}\,p$ (they equal $t$ there) and inside ${\uparrow}\,p$ both install $(t|_p)[r:=s]$ as the subtree at $p$: the left side because $q = p\cdot r$ and replacement at $q$ only alters ${\uparrow}\,q \subseteq {\uparrow}\,p$ within the subtree at $p$, the right side by definition. Compare domains and labels via Definition 9.3.

### 9.5. Relabelling, Map, Fold, Unfold

> [!definition] Definition 9.12: Map (relabelling) and fold (recall)
> For a rank-preserving $\varphi : L \to M$, the **map** $\operatorname{map}_\varphi$ relabels while fixing the domain (Definition 4.10). For a family $(h_a)$, the **fold** $H$ consumes a tree into a value (Theorem 5.7). These are the two shape-respecting transformations: map outputs a tree of the same shape; fold outputs an element of an arbitrary carrier. Both are total.

> [!definition] Definition 9.13: Unfold (anamorphism), finite case
> Given a set $A$, a "seed" $a_0 \in A$, and a **coalgebra** structure $\kappa : A \to \coprod_{a \in L} A^{\rho(a)}$ that is **well-founded** (no infinite $\kappa$-descent), the **unfold** generates the finite tree $\operatorname{unfold}_\kappa(a_0)$ by $\operatorname{unfold}_\kappa(x) = b(\operatorname{unfold}_\kappa(y_1), \dots, \operatorname{unfold}_\kappa(y_m))$ where $\kappa(x) = (b, y_1, \dots, y_m)$. Without the well-foundedness hypothesis $\kappa$ generates an infinite tree (Section 22), a final-coalgebra element rather than an initial-algebra one.

> [!warning] Warning 9.14: Map versus substitution versus fold versus rewrite
> Four operations with overlapping informal descriptions must be kept apart by their type and effect on shape. **Map** changes labels of equal rank and preserves the domain. **Fold** consumes a tree into a value in an arbitrary set. **Substitution** replaces variable leaves by trees and generally enlarges the domain. **Rewrite** replaces a matched subtree by a rule-image and generally changes both shape and size locally. Replacing every variable $x$ by $f(x)$ is not a map (it changes a rank-$0$ leaf into a rank-$1$ subtree); changing every label $a$ to $\varphi(a)$ of equal rank is a map; computing $|t|$ is a fold; simplifying $x + 0$ to $x$ is a rewrite.

### 9.6. Transport of Operations Between Presentations

> [!proposition] Proposition 9.15: Operations transport along the canonical isomorphism
> Let $\mathbf{P}$ be any concrete presentation of free syntax — recursive expressions, address trees, tagged tuples, well-formed strings — certified free on $X$ (Theorem 8.9), and let $\Phi : \mathbf{T}_\Omega(X) \xrightarrow{\cong} \mathbf{P}$ be the unique generator-preserving isomorphism (Corollary 8.10). Then every operation of the tree calculus defined on $\mathbf{T}_\Omega(X)$ — extraction, replacement, grafting, context plugging, substitution, matching, the one-step rewrite — transports to $\mathbf{P}$ by conjugation with $\Phi$, and the transported operation satisfies the same laws. Quantities that are not invariant under $\Phi$ (string length, address index sequences) do not transport.
>
> [!proof-sketch] Proof Sketch 9.15
> $\Phi$ is a homomorphism preserving constructors and generators, hence preserves the destructors and the recursive structure used to define each operation; conjugating an operation $O$ on $\mathbf{T}$ by $\Phi$ yields $\Phi \circ O \circ \Phi^{-1}$ on $\mathbf{P}$, and the defining recursion of $O$ transports because $\Phi$ commutes with the constructors. Laws stated as equations between such operations transport because $\Phi$ is a bijection. Presentation-specific data are by definition not in the image of any operation expressible from constructors and destructors, so they need not transport.

> [!remark] Remark 9.16: The two generators of the calculus
> The entire single-sorted calculus is generated by extraction and replacement, in the precise sense that grafting is replacement at the root of a stub (or the inverse of immediate extraction), pruning and leaf grafting are special replacements, context plugging is replacement at the hole, substitution is the fold whose leaf clauses are leaf replacements, and the one-step rewrite is replacement at a matched position. The structural laws — the extraction recurrence (Proposition 9.2), the factorization through contexts (Proposition 9.5), the commutation of disjoint replacements and the nesting law (Propositions 9.10–9.11) — are the equations of this calculus and are invoked repeatedly in the rewriting development.

### 9.7. Typed Refinement of the Operations

> [!warning] Warning 9.17: Sort side-conditions on the operations
> In the typed setting (Definitions 4.15–4.16) each operation acquires a sort hypothesis. Extraction $t|_p$ is unconditional but its output has sort $\operatorname{sort}(t|_p)$, the sort of the symbol at $p$. Replacement $t[p:=s]$ is defined only when $\operatorname{sort}(s)$ equals the sort required at $p$ — the input sort of $p$'s parent symbol for the relevant child position, or $\operatorname{sort}(t)$ if $p = \varepsilon$ — for otherwise the result is not well-sorted. Grafting $f(t_1,\dots,t_n)$ requires $\operatorname{sort}(t_i) = s_i$ for the declared type $f : s_1 \times \cdots \times s_n \to s$. Simultaneous replacement requires each $s_i$ to match the sort at $p_i$. These are exactly the conditions of Proposition 4.17 imposed pointwise; the single-sorted laws of this section are their $|S| = 1$ specializations, where every sort condition holds vacuously.

---

## 10. Contexts: The Single-Sorted Case

A context is a tree with holes. Plugging trees into the holes produces a tree. This makes a context an operation on trees — unary if it has one hole, $k$-ary if it has $k$ — and the operation it induces is a **polynomial operation** of the tree algebra. This section develops contexts from the ground up in the single-sorted setting, with no prior familiarity assumed, before the typed complications of Section 11. The governing slogans, made precise below, are: a context is a tree with holes; plugging is substitution into holes; contexts are polynomial operations on trees.

### 10.1. Hole Symbols and One-Hole Contexts

> [!definition] Definition 10.1: Hole symbol
> Fix a **hole symbol** $\Box \notin L$, adjoined to the alphabet with rank $\rho(\Box) := 0$, so that holes are leaves. Work over the extended ranked alphabet $L_\Box := L \sqcup \{\Box\}$. A tree over $L_\Box$ may carry occurrences of $\Box$ at some of its leaves.

> [!definition] Definition 10.2: One-hole context
> A **one-hole context over $L$** is a tree $C = (D_C, \ell_C)$ over $L_\Box$ in which the hole symbol $\Box$ occurs **exactly once**, necessarily at a leaf (since $\rho(\Box) = 0$). The unique address $h \in D_C$ with $\ell_C(h) = \Box$ is the **hole address** of $C$. The set of one-hole contexts over $L$ is written $\operatorname{Ctx}_L^{1}$.

> [!example] Example 10.3: A one-hole context and its hole
> Over $L = \{f^{(2)}, g^{(2)}, x^{(0)}, y^{(0)}, z^{(0)}\}$ (superscripts are ranks), the tree $C = f(x, \Box)$ has domain $\{\varepsilon, 1, 2\}$ with $\ell_C(\varepsilon) = f$, $\ell_C(1) = x$, $\ell_C(2) = \Box$, so its hole address is $h = 2$. Plugging $g(y,z)$ into the hole yields $f(x, g(y,z))$. The context records "an $f$ with first argument $x$ and a vacant second argument."

### 10.2. Context Extraction and Plugging

> [!definition] Definition 10.4: Context extraction at a position
> For a tree $t = (D, \ell)$ and $p \in D$, the **context extracted at $p$** is the one-hole context $t[p := \Box] = (D_C, \ell_C)$ with
>
> $$
> D_C := \{\, q \in D : p \npreceq q \,\} \cup \{p\}, \qquad \ell_C(q) := \begin{cases} \ell(q), & q \in D_C,\ q \neq p,\\ \Box, & q = p, \end{cases}
> $$
>
> obtained by discarding the strict descendants of $p$ and relabelling $p$ itself by $\Box$. Its hole address is $p$. (This is the partial-domain version of replacement by an atom; cf. Proposition 9.5.)

> [!definition] Definition 10.5: Plugging into a one-hole context
> Let $C = (D_C, \ell_C)$ be a one-hole context with hole address $h$, and let $s = (E, m)$ be a tree over $L$. The **plugging** $C[s]$ is the tree $(D, \ell)$ over $L$ with
>
> $$
> D := (D_C \setminus \{h\}) \cup \{\, h \cdot r : r \in E \,\}, \qquad \ell(q) := \begin{cases} \ell_C(q), & q \in D_C \setminus \{h\},\\ m(r), & q = h \cdot r,\ r \in E, \end{cases}
> $$
>
> obtained by replacing the hole leaf $h$ with the tree $s$. Plugging is **total**: any $L$-tree may be plugged into any one-hole context, and the result is a genuine $L$-tree (the hole symbol is consumed). In the typed setting plugging carries a sort condition (Section 11).

> [!proposition] Proposition 10.6: Extraction and plugging are mutually inverse at a position
> For every tree $t$ and $p \in D_t$,
>
> $$
> \big(t[p := \Box]\big)\big[\,t|_p\,\big] = t,
> $$
>
> and conversely for every one-hole context $C$ with hole $h$ and every tree $s$,
>
> $$
> (C[s])\big|_h = s, \qquad (C[s])[h := \Box] = C.
> $$
>
> Thus, fixing the hole position, plugging and "extract-the-subtree-and-the-context" are inverse bijections between trees $t$ with $p \in D_t$ and pairs $(C, s)$ with $C$ a one-hole context of hole $h = p$ and $s$ an $L$-tree.
>
> [!proof-sketch] Proof Sketch 10.6
> The first identity is Theorem 7.6 in the present notation: off ${\uparrow}\,p$ the context retains $t$, and plugging $t|_p$ reinstalls the discarded descendants with their labels. The converse identities follow by computing $(C[s])|_h = (E, m) = s$ from the plugging formula and observing that extracting the context back at $h$ deletes exactly the freshly inserted $s$ and restores the hole. Bijectivity is the conjunction of the two directions.

### 10.3. Composition, Identity, and the Context Monoid

> [!definition] Definition 10.7: Context composition
> For one-hole contexts $C_1, C_2$ with hole addresses $h_1, h_2$, the **composite** $C_1 \circ C_2$ is the one-hole context obtained by plugging $C_2$ (a tree over $L_\Box$ with its single hole) into the hole of $C_1$; formally it is computed by the plugging formula of Definition 10.5 with $s = C_2$, the resulting tree over $L_\Box$ retaining exactly the one hole of $C_2$ at address $h_1 \cdot h_2$. It is characterized by its action:
>
> $$
> (C_1 \circ C_2)[s] = C_1\big[C_2[s]\big] \quad\text{for every } L\text{-tree } s.
> $$

> [!definition] Definition 10.8: Identity context
> The **identity context** is the single-hole tree $I := \Box$, with domain $\{\varepsilon\}$ and hole address $\varepsilon$. It satisfies $I[s] = s$ for every $s$.

> [!proposition] Proposition 10.9: One-hole contexts form a monoid
> Under composition $\circ$, with identity $I$, the one-hole contexts over $L$ form a monoid:
>
> $$
> I \circ C = C = C \circ I, \qquad (C_1 \circ C_2) \circ C_3 = C_1 \circ (C_2 \circ C_3).
> $$
>
> The map $C \mapsto C[-]$ to unary operations on $\operatorname{Tree}_L$ under function composition is a monoid homomorphism, and it is injective, so one-hole contexts are faithfully represented by the unary operations they induce.
>
> [!proof-sketch] Proof Sketch 10.9
> Unit and associativity are proved either extensionally — both sides act on every $s$ as $s \mapsto C_1[C_2[C_3[s]]]$, and a context is determined by its plugging action (injectivity below) — or directly, by comparing the address $h_1 \cdot h_2 \cdot h_3$ of the composite hole and the labellings, which are unambiguous by associativity of address concatenation. Injectivity of $C \mapsto C[-]$: distinct contexts differ at some non-hole address or in hole position, and plugging a fixed atom exposes the difference, since $C[s]$ off the hole equals $C$ off the hole and $C[s]|_h = s$ pins the hole position.

### 10.4. The Path Picture and Nested Contexts

> [!remark] Remark 10.10: A one-hole context is a decorated root-to-hole path
> A one-hole context with hole $h = (i_1, \dots, i_m)$ is determined by the data along the path from the root to the hole: at each step $j$ the label of the node $(i_1,\dots,i_{j-1})$, the index $i_j$ of the child continuing toward the hole, and the off-path sibling subtrees at that node. Composition concatenates such paths. This path representation is the structural content of the **zipper** (Section 23): a zipper at position $p$ is precisely the pair $(t[p:=\Box], t|_p)$ stored as a stack of path frames, and moving the focus pushes or pops a frame, rebuilding one parent node per pop.

### 10.5. Multi-Hole Contexts

> [!definition] Definition 10.11: Indexed holes and $k$-hole contexts
> Fix hole symbols $H_k := \{\Box_0, \dots, \Box_{k-1}\}$, each of rank $0$ and disjoint from $L$, over the extended alphabet $L_{H_k} := L \sqcup H_k$. A **$k$-hole context over $L$** (with **ordered, named** holes, each occurring **exactly once**) is a tree $C$ over $L_{H_k}$ in which each $\Box_i$ ($0 \le i < k$) occurs exactly once, at a leaf. Its **hole addresses** $h_0, \dots, h_{k-1}$ are the addresses of $\Box_0, \dots, \Box_{k-1}$; they are pairwise distinct, and (since each is a leaf) pairwise disjoint. The set is $\operatorname{Ctx}_L^{k}$.

> [!definition] Definition 10.12: Linear and nonlinear, ordered and named holes
> A multi-hole context in which each hole symbol occurs **exactly once** is **linear**. Permitting a hole symbol to occur **more than once** yields a **nonlinear** context, whose plugging substitutes the *same* tree at all occurrences of a given $\Box_i$ — the source of diagonal operations such as $C[\Box_0, \Box_0]$. Holes may be **ordered** (indexed $0, \dots, k-1$, plugged positionally) or **named** (drawn from a set of distinct names, plugged by name); ordered holes are the special case of names $0, 1, \dots, k-1$ with the numeric order. Unless stated otherwise, contexts here are linear with ordered holes.

> [!definition] Definition 10.13: Plugging into a $k$-hole context
> For a linear $k$-hole context $C$ with hole addresses $h_0, \dots, h_{k-1}$ and trees $s_0, \dots, s_{k-1}$ over $L$, the **simultaneous plugging** $C[s_0, \dots, s_{k-1}]$ replaces each hole leaf $\Box_i$ (at $h_i$) by $s_i$:
>
> $$
> D := \big(D_C \setminus \{h_0,\dots,h_{k-1}\}\big) \cup \bigcup_{i=0}^{k-1} \{\, h_i \cdot r : r \in E_i \,\},
> $$
>
> with labels from $\ell_C$ off the holes and from $m_i$ inside $s_i$. Because the hole addresses are pairwise disjoint, this is well-defined and equals the simultaneous replacement $C[h_0 := s_0, \dots, h_{k-1} := s_{k-1}]$ of the holes (Definition 9.9, reading the holes as marked leaves). It induces the $k$-ary operation $C[-,\dots,-] : \operatorname{Tree}_L^k \to \operatorname{Tree}_L$.

> [!warning] Warning 10.14: Linear versus nonlinear plugging
> For a linear context, plugging is a $k$-ary operation with independent inputs at disjoint sites. For a nonlinear context, where $\Box_i$ occurs at several addresses, plugging installs the *same* $s_i$ at every such address, so the result depends on $s_i$ through multiple copies; this is the tree-level diagonal. Nonlinear contexts therefore do not correspond to honest projections-plus-grafting but to operations that duplicate an argument, and they are exactly the contexts whose induced operations are not multilinear. Nonlinear **patterns** (Section 13) impose the dual constraint on matching: the same metavariable at several positions forces equality of the matched subtrees.

### 10.6. Context Composition for Multi-Hole Contexts

> [!definition] Definition 10.15: Composition of multi-hole contexts
> Let $C$ be a $k$-hole context and, for each $i < k$, let $D_i$ be an $m_i$-hole context. The **composite** $C[D_0, \dots, D_{k-1}]$ is obtained by plugging each $D_i$ into the $i$-th hole of $C$; the resulting context has $m_0 + \cdots + m_{k-1}$ holes, reindexed contiguously — the holes of $D_0$ become $\Box_0, \dots, \Box_{m_0 - 1}$, those of $D_1$ become $\Box_{m_0}, \dots, \Box_{m_0 + m_1 - 1}$, and so on — to avoid collisions. Its induced operation is the corresponding composite of the induced operations.

> [!proposition] Proposition 10.16: Multi-hole decomposition at a disjoint position-set
> Let $t$ be a tree and $P = \{p_0, \dots, p_{k-1}\} \subseteq D_t$ a set of pairwise-disjoint positions. There is a unique $k$-hole context $C$ with hole addresses $p_0, \dots, p_{k-1}$ and unique subtrees $s_i = t|_{p_i}$ with
>
> $$
> t = C[s_0, \dots, s_{k-1}],
> $$
>
> namely $C = t[p_0 := \Box_0, \dots, p_{k-1} := \Box_{k-1}]$. The decomposition is unique relative to the chosen disjoint set $P$; different choices of $P$ give different multi-hole decompositions of the same $t$.
>
> [!proof-sketch] Proof Sketch 10.16
> Pairwise disjointness makes the simultaneous marking $t[p_i := \Box_i]$ well-defined (Proposition 9.10), and plugging back $s_i = t|_{p_i}$ reinstalls each subtree by the one-hole identity (Proposition 10.6) applied at each disjoint site independently. Uniqueness given $P$: the holes must sit at the addresses $p_i$, the off-hole labelled domain is forced to equal $t$'s, and the fillers are forced to be $t|_{p_i}$.

### 10.7. Contexts as Polynomial Operations

> [!definition] Definition 10.17: Polynomial operations of the tree algebra
> A **$k$-ary polynomial operation** of the tree algebra $\mathbf{T}_\Omega(X)$ is a function $\operatorname{Tree}_\Omega(X)^k \to \operatorname{Tree}_\Omega(X)$ built from the projections $(s_0,\dots,s_{k-1}) \mapsto s_i$ and the constructors $f^{\mathbf{T}}$ by composition, allowing also the insertion of fixed parameter trees. Equivalently, it is a term operation of $\mathbf{T}_\Omega(X)$ with $k$ formal argument places, possibly using elements of $T_\Omega(X)$ as constants.

> [!theorem] Theorem 10.18: Contexts are exactly the polynomial operations
> The induced-operation map sends each linear $k$-hole context to a $k$-ary polynomial operation of $\mathbf{T}_\Omega(X)$, and this map is a bijection between linear $k$-hole contexts (up to the naming of holes) and $k$-ary **multilinear** polynomial operations using each argument exactly once. Allowing nonlinear contexts (repeated holes) and missing holes recovers all polynomial operations: a polynomial operation that uses argument $i$ several times corresponds to a context repeating $\Box_i$, and one that omits an argument corresponds to a context lacking that hole.
>
> [!proof-sketch] Proof Sketch 10.18
> A $k$-hole context, read by structural recursion on its tree over $L_{H_k}$, is built from holes (the projections) and constructors $f$ (the basic operations) and fixed $L$-labelled leaves (parameter constants), so its induced operation is polynomial; linearity (each hole once) corresponds to using each projection once, i.e. multilinearity. Conversely a polynomial operation's formation tree, with the argument places marked by holes, is a context inducing it. The correspondence is bijective up to hole naming because the formation tree of a polynomial operation is unique (unique readability), and repeated/omitted arguments correspond exactly to repeated/absent holes.

> [!remark] Remark 10.19: The three slogans, made precise
> The informal slogans now have exact referents. "A context is a tree with holes" is Definition 10.2/10.11: a tree over $L_\Box$ (or $L_{H_k}$) with the prescribed hole occurrences. "Plugging is substitution into holes" is Definition 10.5/10.13: plugging is the simultaneous replacement of the hole leaves, which is the special case of substitution (Section 12) in which the replaced leaves are the holes rather than object variables. "Contexts are polynomial operations on trees" is Theorem 10.18: the induced-operation map identifies linear $k$-hole contexts with multilinear $k$-ary polynomial operations of $\mathbf{T}_\Omega(X)$. The first slogan is the object view, the second the operational view, the third the algebraic view, and they are three readings of one structure. Contexts are also a **clone**: holes are projections, composition is operation composition, and every context induces a tree operation (Definition 10.15, Theorem 10.18); this is the context clone that recurs in the typed and quotient settings.

---

## 11. Typed and Many-Sorted Contexts

In the single-sorted setting a context is "a tree with a hole," and any tree may be plugged into any hole. In the typed setting this is false: a hole has an **input sort** (the sort of tree it accepts) and the whole context has an **output sort** (the sort of tree it produces), and plugging is defined only when the filler's sort matches the hole's input sort. This section refines Section 10 by the sort discipline of Definitions 4.15–4.16. The base theory is unchanged in form; every operation acquires a sort-matching hypothesis.

### 11.1. Typed Holes and Typed Contexts

> [!definition] Definition 11.1: Sorted hole
> Fix a many-sorted signature $(S, \Sigma, \tau)$ with sorted variables $X = (X_s)$. For each sort $s \in S$ adjoin a **hole symbol of input sort $s$**, written $\Box^{s}$, a fresh constant of sort $s$ (so a tree may use $\Box^s$ where a tree of sort $s$ is required). A hole of input sort $s$ may be filled only by a well-sorted tree of sort $s$.

> [!definition] Definition 11.2: Typed one-hole context and its profile
> A **typed one-hole context of profile $s \Rightarrow t$** is a well-sorted tree $C$ of sort $t$ over the signature extended by a single hole symbol $\Box^{s}$, in which $\Box^{s}$ occurs exactly once (at a leaf). The sort $s$ is the **input sort** (the hole's sort), and $t$ is the **output sort** (the sort of $C$ as a whole). We write
>
> $$
> C : s \Rightarrow t
> $$
>
> to record that $C$ accepts a tree of sort $s$ at its hole and returns a tree of sort $t$. The single-sorted one-hole context (Definition 10.2) is the case $|S| = 1$, where every profile is the unique $\ast \Rightarrow \ast$.

> [!definition] Definition 11.3: Typed plugging
> For $C : s \Rightarrow t$ with hole at $h$ and a well-sorted tree $u$ of sort $s$, the **typed plugging** $C[u]$ replaces the hole leaf by $u$ exactly as in Definition 10.5; the result is a well-sorted tree of sort $t$. Typed plugging is **partial**: $C[u]$ is defined only when $\operatorname{sort}(u) = s$ matches the hole's input sort; plugging a tree of any other sort is undefined, the result failing to be well-sorted at the hole's parent edge.

> [!proposition] Proposition 11.4: Typed plugging preserves well-sortedness; profile is forced
> If $C : s \Rightarrow t$ and $\operatorname{sort}(u) = s$, then $C[u]$ is well-sorted of sort $t$. Conversely, given a well-sorted tree $w$ of sort $t$ and a position $p \in D_w$ with $\operatorname{sort}(w|_p) = s$, the context $C := w[p := \Box^{s}]$ has profile $s \Rightarrow t$ and $w = C[w|_p]$. Thus the input sort of the extracted context is forced to be the sort of the extracted subtree, and the output sort is the sort of the host.
>
> [!proof-sketch] Proof Sketch 11.4
> Well-sortedness of $C[u]$: off the hole $C$ is well-sorted of sort $t$ with a hole demanding sort $s$ at the hole's parent edge; substituting $u$ of sort $s$ satisfies that edge constraint, and all other edges are unaffected, so the result is well-sorted of sort $t$ (Proposition 4.17). The converse is the typed reading of context extraction (Theorem 7.6): marking $w$ at $p$ leaves a hole whose required sort is exactly $\operatorname{sort}(w|_p)$, since that subtree fed the parent edge at $p$.

### 11.2. Typed Composition

> [!definition] Definition 11.5: Composition of typed contexts
> For typed one-hole contexts $C : s \Rightarrow t$ and $C' : r \Rightarrow s$ (note the matching middle sort), the composite $C \circ C' : r \Rightarrow t$ is obtained by plugging $C'$ into the hole of $C$; it is defined only because the output sort of $C'$ equals the input sort of $C$, so that $C'$ may legally fill $C$'s hole. It satisfies $(C \circ C')[u] = C[C'[u]]$ for every $u$ of sort $r$.

> [!proposition] Proposition 11.6: Typed contexts form a category
> The typed one-hole contexts over $(S, \Sigma, \tau)$ form a category $\mathbf{Ctx}$ whose objects are the sorts $S$, whose morphisms $s \to t$ are the typed one-hole contexts $C : s \Rightarrow t$, whose composition is context composition (Definition 11.5, defined exactly when the middle sorts match), and whose identity at $s$ is the typed identity context $I^{s} := \Box^{s} : s \Rightarrow s$. The single-sorted context monoid (Proposition 10.9) is the one-object case $|S| = 1$.
>
> [!proof-sketch] Proof Sketch 11.6
> Identity and associativity laws hold as in Proposition 10.9, now indexed by sorts: $I^t \circ C = C = C \circ I^s$ for $C : s \Rightarrow t$, and associativity of plugging along matching sorts. Composition is defined precisely when the codomain sort of one morphism equals the domain sort of the next, which is the categorical composability condition; hence a category rather than a monoid, the monoid being recovered when there is a single sort (a single object).

### 11.3. Typed Multi-Hole Contexts

> [!definition] Definition 11.7: Typed multi-hole context and its profile
> A **typed $k$-hole context** carries holes $\Box^{s_0}_0, \dots, \Box^{s_{k-1}}_{k-1}$ of input sorts $s_0, \dots, s_{k-1}$, each occurring once at a leaf, in a well-sorted tree of some output sort $s$. Its **profile** is
>
> $$
> C : (s_0, \dots, s_{k-1}) \Rightarrow s,
> $$
>
> meaning $C$ accepts trees of sorts $s_0, \dots, s_{k-1}$ at its respective holes and returns a tree of sort $s$. Typed plugging $C[u_0, \dots, u_{k-1}]$ is defined exactly when $\operatorname{sort}(u_i) = s_i$ for all $i$, and then is well-sorted of sort $s$.

> [!warning] Warning 11.8: Sort mismatch is the typed failure mode of plugging
> The single-sorted theory never fails to plug. The typed theory fails precisely when sorts misalign: $C[u]$ is undefined when $\operatorname{sort}(u)$ differs from the hole's input sort, and $C \circ C'$ is undefined when $C'$'s output sort differs from $C$'s input sort. These are not errors to be repaired but the correct domain restrictions: plugging is a sort-indexed partial operation, total only within each profile. A typed rewrite rule (Section 14.7) must therefore have matching left/right output sorts and matching pattern-variable sorts, so that contracting a redex inside a typed context yields a well-sorted tree.

> [!remark] Remark 11.9: Typed contexts as a coloured operad / clone
> The typed multi-hole contexts form a **coloured (typed) clone**, equivalently a coloured operad (Section 21): the colours are the sorts $S$, the operations of profile $(s_0,\dots,s_{k-1}) \Rightarrow s$ are the typed $k$-hole contexts, holes are the typed projections, and composition is typed context composition with sort-matching. This is the typed refinement of the context clone of Remark 10.19, and it is the structure into which typed substitution and typed matching (Sections 12.6, 13.6) and typed rewriting (Section 14.7) fit: each is required to respect the colouring.

---

## 12. Substitution on Trees

Substitution is the systematic replacement of variable leaves by trees, performed simultaneously at every occurrence and propagated recursively through the whole tree. It is the homomorphic extension of an assignment of trees to variables, and as such it is the universal mapping property of the free tree algebra instantiated with a syntax target. This section develops substitution as an operation with laws — a monad — and rigorously separates it from replacement, relabelling, plugging, and evaluation.

### 12.1. Substitutions and Their Extensions

> [!definition] Definition 12.1: Substitution assignment
> Fix $L = X \sqcup \Omega$. A **substitution** is a function
>
> $$
> \sigma : X \to \operatorname{Tree}_\Omega(Y)
> $$
>
> assigning to each variable $x \in X$ a tree $\sigma(x)$ over the (possibly different) variable set $Y$. When $Y = X$ the substitution is an endo-substitution. The **support** of $\sigma$ is $\{x : \sigma(x) \neq x\}$; $\sigma$ is **finite** when its support is finite, the case relevant to rules.

> [!definition] Definition 12.2: Homomorphic extension
> The **homomorphic extension** of $\sigma : X \to \operatorname{Tree}_\Omega(Y)$ is the unique fold
>
> $$
> \widehat{\sigma} : \operatorname{Tree}_\Omega(X) \to \operatorname{Tree}_\Omega(Y), \qquad \widehat\sigma(x) := \sigma(x), \qquad \widehat\sigma\big(f(t_1, \dots, t_n)\big) := f\big(\widehat\sigma(t_1), \dots, \widehat\sigma(t_n)\big),
> $$
>
> existing and unique by the structural recursion theorem (Theorem 5.7) with leaf clauses $h_x = \sigma(x)$ and operation clauses $h_f = f^{\mathbf{T}}$. Equivalently $\widehat\sigma = \operatorname{ev}_\sigma$, the evaluation homomorphism (Definition 8.12) into the *syntax* algebra $\mathbf{T}_\Omega(Y)$ — substitution is evaluation into trees. We abbreviate $\widehat\sigma(t)$ to $t\sigma$ when convenient.

> [!proposition] Proposition 12.3: $\widehat\sigma$ is the unique constructor-preserving extension
> $\widehat\sigma$ is the unique function $\operatorname{Tree}_\Omega(X) \to \operatorname{Tree}_\Omega(Y)$ that restricts to $\sigma$ on variable atoms and commutes with every constructor $f$. It is a homomorphism of $\Omega$-algebras and the only one extending $\sigma$ along the generator insertion.
>
> [!proof-sketch] Proof Sketch 12.3
> Existence and the two clauses are Definition 12.2. Uniqueness is the uniqueness clause of Theorem 5.7 (equivalently the UMP of $\mathbf{T}_\Omega(X)$, Theorem 8.8): any constructor-preserving extension satisfies the same recursion, hence equals $\widehat\sigma$.

### 12.2. The Substitution Monad

> [!definition] Definition 12.4: Identity substitution and composition
> The **identity substitution** $\iota_X : X \to \operatorname{Tree}_\Omega(X)$ is $\iota_X(x) = x$ (the variable atom). For $\sigma : X \to \operatorname{Tree}_\Omega(Y)$ and $\tau : Y \to \operatorname{Tree}_\Omega(Z)$, the **composite** $\tau \star \sigma : X \to \operatorname{Tree}_\Omega(Z)$ is $(\tau \star \sigma)(x) := \widehat\tau(\sigma(x))$, "apply $\sigma$, then $\tau$."

> [!theorem] Theorem 12.5: Substitution laws (Kleisli triple)
> The assignment $X \mapsto \operatorname{Tree}_\Omega(X)$ with unit $\iota$ and extension $(-)\widehat{\ }$ is a monad: for all composable $\sigma, \tau$,
>
> $$
> \widehat{\iota_X} = \mathrm{id}_{\operatorname{Tree}_\Omega(X)}, \qquad \widehat\sigma \circ \iota_X = \sigma, \qquad \widehat\tau \circ \widehat\sigma = \widehat{\,\tau \star \sigma\,} = \widehat{\,\widehat\tau \circ \sigma\,}.
> $$
>
> Equivalently $\star$ is associative with two-sided unit $\iota$, so substitutions form a category (the Kleisli category) with objects variable sets and morphisms substitutions.
>
> [!proof-sketch] Proof Sketch 12.5
> The first two laws are immediate: $\widehat{\iota_X}$ satisfies the identity's recursion and so is the identity by uniqueness, and $\widehat\sigma(\iota_X(x)) = \widehat\sigma(x) = \sigma(x)$. The third law: both $\widehat\tau \circ \widehat\sigma$ and $\widehat{\widehat\tau \circ \sigma}$ are homomorphisms $\operatorname{Tree}_\Omega(X) \to \operatorname{Tree}_\Omega(Z)$ agreeing on variable atoms ($x \mapsto \widehat\tau(\sigma(x))$), hence equal by the uniqueness clause (Proposition 12.3). Associativity and unit laws of $\star$ follow by evaluating both sides on a variable and applying the third law.

> [!remark] Remark 12.6: Substitution composition is application order
> The law $\widehat\tau \circ \widehat\sigma = \widehat{\tau \star \sigma}$ is the precise statement that substituting by $\sigma$ and then by $\tau$ equals substituting by the single composite $\tau \star \sigma$. It is the workhorse identity of the rewriting metatheory: it is what makes the rewrite relation stable under substitution (Section 14.4) and what underlies the substitution clause in the generation of congruences (Section 16) and in the critical-pair lemma (Section 15).

### 12.3. Simultaneous Substitution and Single-Variable Notation

> [!definition] Definition 12.7: Single-variable substitution
> When $\sigma$ has support $\{x\}$ with $\sigma(x) = s$ and $\sigma(y) = y$ for $y \neq x$, the extension is written $t[x := s] := \widehat\sigma(t)$. This replaces **every** occurrence of the leaf $x$ in $t$ by $s$. More generally $t[x_1 := s_1, \dots, x_k := s_k]$ denotes the extension of the substitution with $\sigma(x_i) = s_i$ (distinct $x_i$) and $\sigma(y) = y$ otherwise — simultaneous, not sequential.

> [!warning] Warning 12.8: Single-variable substitution is not single-position replacement
> The notations collide deliberately and must be disambiguated by their bracket contents. $t[p := s]$ with a **position** $p$ is replacement at one site (Section 9). $t[x := s]$ with a **variable** $x$ is substitution at every occurrence of $x$ (Definition 12.7). They agree only in the degenerate case that $x$ occurs at exactly one leaf, which is the position of that leaf. In general $t[x := s]$ touches as many sites as $x$ has occurrences — zero, one, or many — while $t[p := s]$ touches exactly one. Simultaneity also matters: $t[x := s]$ replaces all $x$'s with the *original* $s$, not iteratively, so an $x$ inside $s$ is not itself replaced.

> [!warning] Warning 12.9: Substitution versus relabelling versus plugging
> Three superficially similar operations differ in type and effect. **Relabelling** $\operatorname{map}_\varphi$ sends a rank-$n$ label to a rank-$n$ label and fixes the domain (Section 4.4). **Substitution** $\widehat\sigma$ sends rank-$0$ variable leaves to arbitrary trees and generally enlarges the domain. **Plugging** $C[s]$ fills the fixed holes of a context, a number of sites fixed by $C$, not by occurrences of a variable. Plugging is the special case of substitution in which the "variables" are the hole symbols and each occurs once (linear context) — indeed $C[s] = \widehat{\sigma}(C)$ for $\sigma(\Box) = s$ reading $C$ as a tree over $L_\Box$ — but plugging holds the context fixed and varies the filler, whereas substitution holds the assignment fixed and varies the input tree.

### 12.4. Substitution into Subtrees and Contexts

> [!proposition] Proposition 12.10: Substitution commutes with extraction
> For every substitution $\sigma$, tree $t$, and position $p \in D_t$,
>
> $$
> \widehat\sigma(t)\big|_{p'} = \widehat\sigma\big(t|_p\big) \quad\text{for the image position } p' \text{ of } p,
> $$
>
> where, because substitution may enlarge the tree only below variable leaves, the positions of $t$ above and beside variable occurrences are preserved and $p' = p$ for every $p$ not lying strictly below a substituted variable. In particular for $p$ an internal (non-variable) position, $\widehat\sigma(t)|_p = \widehat\sigma(t|_p)$.
>
> [!proof-sketch] Proof Sketch 12.10
> By structural induction on $t$. For $t = f(t_1, \dots, t_n)$ and $p = i \cdot q$, $\widehat\sigma(t)|_{i \cdot q} = \widehat\sigma(t_i)|_q = \widehat\sigma(t_i|_q)$ by the constructor clause and the induction hypothesis. For $p = \varepsilon$ it is trivial. The position $p$ shifts only when it lies below a variable leaf $x$, where the single-node leaf is replaced by $\sigma(x)$, enlarging the addresses below $x$; positions not below any substituted variable keep their addresses.

> [!proposition] Proposition 12.11: Substitution acts on contexts and commutes with plugging up to the substituted filler
> Reading a one-hole context $C$ as a tree over $L_\Box$ with $\Box$ held fixed by $\sigma$ (i.e. $\sigma(\Box) = \Box$), $\widehat\sigma(C)$ is again a one-hole context, and for every tree $s$,
>
> $$
> \widehat\sigma\big(C[s]\big) = \widehat\sigma(C)\big[\,\widehat\sigma(s)\,\big].
> $$
>
> Thus substitution distributes over plugging, applying to the context and the filler separately.
>
> [!proof-sketch] Proof Sketch 12.11
> $\widehat\sigma(C)$ keeps the single hole because $\sigma$ fixes $\Box$, and the distribution law is proved by structural induction on $C$: at the hole both sides equal $\widehat\sigma(s)$, and at a constructor node both sides push $\widehat\sigma$ inside by the constructor clause, matching by the induction hypothesis. Equivalently it is the homomorphism property of $\widehat\sigma$ applied to the polynomial operation induced by $C$ (Theorem 10.18).

### 12.5. Substitution versus Evaluation

> [!warning] Warning 12.12: Substitution stays in syntax; evaluation leaves it
> Substitution $\widehat\sigma : \operatorname{Tree}_\Omega(X) \to \operatorname{Tree}_\Omega(Y)$ and evaluation $\operatorname{ev}_g : \mathbf{T}_\Omega(X) \to \mathbf{B}$ are both homomorphic extensions of generator data by the same universal mechanism, and both are written by the same recursion. They differ in **codomain**: substitution's target is a *syntax* algebra (its outputs are trees, which can be further substituted, matched, rewritten), whereas evaluation's target is an arbitrary *semantic* algebra (its outputs are values, opaque to the tree calculus). Substitution is the case of evaluation with target $\mathbf{T}_\Omega(Y)$ and $g = \sigma$; conversely evaluation is "substitution into a semantic algebra." Confusing them collapses the syntax/semantics distinction and is the source of the error in Warning 8.4.

### 12.6. Typed Substitution

> [!definition] Definition 12.13: Sorted substitution
> In the typed setting a **sorted substitution** is a family $\sigma = (\sigma_s)_{s \in S}$ of functions $\sigma_s : X_s \to \operatorname{Tree}_\Sigma(Y)_s$ assigning to each variable of sort $s$ a tree of the *same* sort $s$. Its homomorphic extension $\widehat\sigma$ is the unique sort-preserving constructor-preserving extension; sort-preservation, $\operatorname{sort}(\widehat\sigma(t)) = \operatorname{sort}(t)$, holds because $\sigma$ respects sorts and the constructors have fixed output sorts.

> [!warning] Warning 12.14: Sorted substitution must respect sorts
> A substitution that sent a variable $x \in X_s$ to a tree of sort $s' \neq s$ would produce ill-sorted results: the parent edge that demanded sort $s$ at $x$ would receive sort $s'$. Hence in the typed theory the assignment is required to be sort-respecting variable-by-variable. The single-sorted theory is the case $|S| = 1$, where the sort constraint is vacuous and any assignment is admissible. Typed substitution composition and the monad laws (Theorem 12.5) hold sortwise, making typed substitutions a category over $S$-sorted variable sets.

---

## 13. Patterns and Matching

Matching is the operation that decides whether, and how, a pattern fits a tree, and it is the operation most often left vague. This section defines it precisely. A pattern is a tree containing **pattern variables** (metavariables); a match of a pattern $\ell$ against a tree $u$ is a substitution $\sigma$ with $\ell\sigma = u$. Matching is the partial inverse of substitution restricted to the pattern, it is the engine of rule application in Section 14, and it must be distinguished sharply from unification. The development gives the recursive matching algorithm, the uniqueness theorem for linear patterns, the failure conditions, and worked examples and non-examples.

### 13.1. Object Variables versus Pattern Variables

> [!definition] Definition 13.1: Pattern variables and patterns
> Fix the syntactic alphabet $L = X \sqcup \Omega$ (object variables $X$, operation symbols $\Omega$). Adjoin a disjoint set $M$ of **pattern variables** (synonyms: **metavariables**, **schema variables**), each of rank $0$ and with $M \cap (X \sqcup \Omega) = \varnothing$. A **pattern** over $\Omega$ (with object variables $X$ and pattern variables $M$) is a tree over the ranked alphabet $M \sqcup X \sqcup \Omega$, i.e. a member of $\operatorname{Tree}_\Omega(X \sqcup M)$ in which elements of $M$ may occur at leaves. A **ground tree** (synonym: **object tree**, **subject**) is a tree over $X \sqcup \Omega$ containing no pattern variables.

> [!warning] Warning 13.2: The two kinds of variable have different roles
> Object variables $x \in X$ are leaves of the trees being manipulated and are themselves subject to substitution and rewriting. Pattern variables $U, V, W \in M$ are placeholders in rules and patterns, instantiated by matching, and never appear in the objects being rewritten. Writing a rule as $(x + y) + z \to x + (y + z)$ with $x, y, z$ "ranging over arbitrary trees" silently uses the object variables as pattern variables; the disciplined form is
>
> $$
> +(+(U, V), W) \;\to\; +(U, +(V, W))
> $$
>
> over distinct metavariables $U, V, W \in M$. Keeping $X$ and $M$ disjoint prevents the conflation and is presupposed throughout the rewriting development. When no confusion arises the object-variable notation is used informally, but the metavariable reading is the formal one.

### 13.2. Matching Substitutions and the Matching Relation

> [!definition] Definition 13.3: Pattern substitution
> A **pattern substitution** is a function $\sigma : M \to \operatorname{Tree}_\Omega(X)$ assigning a ground tree to each metavariable, with homomorphic extension $\widehat\sigma : \operatorname{Tree}_\Omega(X \sqcup M) \to \operatorname{Tree}_\Omega(X)$ fixing object variables and constants and sending each metavariable $U$ to $\sigma(U)$. We write $\ell\sigma := \widehat\sigma(\ell)$ for the **instance** of pattern $\ell$ under $\sigma$.

> [!definition] Definition 13.4: Match of a pattern against a tree
> Let $\ell$ be a pattern and $u$ a ground tree. A **match** of $\ell$ against $u$ is a pattern substitution $\sigma$ with
>
> $$
> \ell\sigma = u.
> $$
>
> When such a $\sigma$ exists, $\ell$ **matches** $u$. The **domain of the match** is the set of metavariables actually bound, $\operatorname{dom}(\sigma) := \operatorname{Var}_M(\ell) = \operatorname{supp}(\ell) \cap M$, the metavariables occurring in $\ell$; the values of $\sigma$ outside $\operatorname{Var}_M(\ell)$ are irrelevant to $\ell\sigma$ and may be taken arbitrary (conventionally $\sigma(U) = U$, but $U \in M$ then survives — for a *ground* match one restricts attention to $\sigma$ defined on $\operatorname{Var}_M(\ell)$).

> [!definition] Definition 13.5: Matching at a position
> For a host tree $t$, a position $p \in D_t$, and a pattern $\ell$, a **match at $p$** is a pattern substitution $\sigma$ with
>
> $$
> \ell\sigma = t|_p,
> $$
>
> i.e. a match of $\ell$ against the subtree at $p$. The pair $(p, \sigma)$ records *where* the pattern fits ($p$) and *how* ($\sigma$); it is the redex datum of Section 14. Matching at a position is matching against a subtree, so the whole theory of Definition 13.4 applies with $u = t|_p$.

### 13.3. The Matching Algorithm and Its Determinism

> [!construction] Construction 13.6: First-order tree matching
> Given a pattern $\ell$ and a ground tree $u$, compute a candidate match $\sigma$ (a partial function $M \rightharpoonup \operatorname{Tree}_\Omega(X)$) by recursion on $\ell$, maintaining a binding store, processing corresponding positions of $\ell$ and $u$:
>
> 1. **metavariable**: if $\ell = U \in M$, then if $U$ is unbound set $\sigma(U) := u$; if $U$ is already bound to $u'$, succeed iff $u' = u$ (the equality check), else fail.
> 2. **object leaf**: if $\ell = x \in X$ or $\ell = c \in \Omega_0$, succeed iff $u = x$ (resp. $u = c$), else fail.
> 3. **compound**: if $\ell = f(\ell_1, \dots, \ell_n)$, succeed iff $u = f(u_1, \dots, u_m)$ with the same root symbol $f$ and $m = n$, and recursively match each $\ell_i$ against $u_i$ (sharing the binding store, left to right); else fail (root-symbol or arity mismatch).
>
> The algorithm **succeeds** iff $\ell$ matches $u$, and on success returns the unique $\sigma$ restricted to $\operatorname{Var}_M(\ell)$ with $\ell\sigma = u$.

> [!proposition] Proposition 13.7: Soundness, completeness, and uniqueness of the matching algorithm
> Construction 13.6 succeeds iff a match exists, and on success its output $\sigma$ is the **unique** pattern substitution on $\operatorname{Var}_M(\ell)$ with $\ell\sigma = u$. Hence matching, as a function $(\ell, u) \mapsto \sigma$, is a **partial function**: at most one match exists for any pattern–tree pair.
>
> [!proof-sketch] Proof Sketch 13.7
> By structural induction on $\ell$. Soundness: each clause maintains the invariant $\ell'\sigma = u'$ for the corresponding sub-pattern and subtree, so on overall success $\ell\sigma = u$. Completeness: if some $\tau$ has $\ell\tau = u$, then at each metavariable leaf $U$ the equation forces $\tau(U) = u|_{(\text{position of } U)} = $ the value the algorithm assigns, and at compound nodes $\ell\tau = u$ forces the matching root symbol and arity, so the algorithm does not fail. Uniqueness: a metavariable's value is forced by the subtree of $u$ at the (any) position where it occurs in $\ell$, and the equality check in clause 1 guarantees consistency across multiple occurrences; thus $\sigma$ is determined on $\operatorname{Var}_M(\ell)$.

The uniqueness of the match — at most one $\sigma$ for each $(\ell, u)$ — is the structural reason matching is computationally cheap and deterministic, in contrast to unification (Section 13.5), where most general solutions form a nontrivial set and require occurs-checks and variable elimination.

### 13.4. Linear and Nonlinear Patterns

> [!definition] Definition 13.8: Linearity of a pattern
> A pattern $\ell$ is **linear** if each metavariable in $M$ occurs **at most once** in $\ell$; otherwise it is **nonlinear**. The associativity pattern $+(+(U,V),W)$ is linear; the pattern $f(U, U)$ is nonlinear (the metavariable $U$ occurs twice).

> [!proposition] Proposition 13.9: Linear patterns match freely; nonlinear patterns impose equality constraints
> If $\ell$ is linear, then $\ell$ matches a ground tree $u$ iff $u$ has the same "rigid skeleton" as $\ell$ — agreeing at every object-leaf and every internal node, with arbitrary subtrees at the metavariable positions — and the match, when it exists, binds each metavariable to the subtree of $u$ at its unique occurrence, with no consistency check needed. If $\ell$ is nonlinear, a match additionally requires that the subtrees of $u$ at the several occurrences of each repeated metavariable be **equal**; e.g. $f(U,U)$ matches $u$ iff $u = f(s, s)$ with $u|_1 = u|_2$.
>
> [!proof-sketch] Proof Sketch 13.9
> For linear $\ell$, clause 1 of Construction 13.6 never encounters an already-bound metavariable, so no equality check fires and the binding at each metavariable's unique position is unconstrained; the match exists iff the object-leaf and compound clauses all succeed, which is the rigid-skeleton condition. For nonlinear $\ell$, a repeated metavariable triggers the equality check in clause 1, succeeding iff the subtrees at its occurrences coincide.

> [!example] Example 13.10: A worked linear match
> Pattern $\ell = +(U, +(V, W))$ (linear) against $u = +(a, +(b, c))$ with $a, b, c$ ground trees. Construction 13.6: root symbols agree ($+$), arities agree ($2$); match $U$ against $a$ (bind $U \mapsto a$); match $+(V, W)$ against $+(b, c)$, root symbols agree, then $V \mapsto b$, $W \mapsto c$. Result:
>
> $$
> \sigma : U \mapsto a, \quad V \mapsto b, \quad W \mapsto c, \qquad \ell\sigma = +(a, +(b,c)) = u. \checkmark
> $$
>
> The same $\ell$ does **not** match $u' = +(+(a,b), c)$: matching $\ell = +(U, +(V,W))$ against $u'$ binds $U \mapsto +(a,b)$ and then requires $+(V,W)$ to match $c$, but $c$'s root is not $+$ (or $c$ is a leaf), so the compound clause fails. Hence $\ell$ matches $u$ but not $u'$ — exactly the distinction associativity-as-rewriting must bridge, and matching alone does not.

> [!example] Example 13.11: A worked nonlinear match and a non-example
> Pattern $\ell = f(U, U)$ (nonlinear) against $u = f(g(a), g(a))$: match first $U$ against $g(a)$ (bind $U \mapsto g(a)$), then match second $U$ against $g(a)$; the equality check $g(a) = g(a)$ succeeds, giving $\sigma : U \mapsto g(a)$ with $\ell\sigma = f(g(a), g(a)) = u$. The same $\ell$ does **not** match $u' = f(g(a), g(b))$: the second occurrence triggers the equality check $g(a) = g(b)$, which fails. Thus $f(U,U)$ recognizes exactly trees with equal children; the rewrite rule $f(U,U) \to U$ collapses such duplicates (Section 14).

### 13.5. Matching versus Unification

> [!definition] Definition 13.12: Unification
> Given two patterns $s, t$ (both possibly containing metavariables), a **unifier** is a pattern substitution $\sigma$ with $s\sigma = t\sigma$; a **most general unifier** (mgu) is a unifier $\sigma$ such that every unifier factors as $\rho \star \sigma$ for some $\rho$. Unification asks for substitutions making two patterns *equal*, with metavariables on **both** sides.

> [!warning] Warning 13.13: Matching is one-sided; unification is two-sided
> The distinction is structural, not merely a matter of degree:
>
> $$
> \text{matching:}\quad \ell\sigma = u \ \ (\ell \text{ a pattern}, \ u \text{ fixed/ground}); \qquad \text{unification:}\quad s\sigma = t\sigma \ \ (s, t \text{ both patterns}).
> $$
>
> In matching the right side is held fixed (only the pattern is instantiated), so a match — if it exists — is unique (Proposition 13.7). In unification both sides are instantiated, so solutions form a set ordered by generality with a most general representative computed by the unification algorithm (decompose, eliminate, occurs-check). Matching is the special case of unification in which one side is ground, but the algorithms and complexity differ: matching needs no occurs-check and yields a unique result; unification needs the occurs-check and yields an mgu up to renaming. Rewriting uses **matching** to locate redexes (the subject tree is fixed); completion and critical-pair computation (Section 15) use **unification** to overlap two left-hand sides.

### 13.6. Matching Modulo Equations and Typed Matching

> [!definition] Definition 13.14: Matching modulo a congruence
> Given a congruence $\equiv$ on trees (Section 16), a **match modulo $\equiv$** of pattern $\ell$ against $u$ is a substitution $\sigma$ with $\ell\sigma \equiv u$ (rather than $\ell\sigma = u$). Equational matching — most importantly matching modulo associativity (A), commutativity (C), or both (AC) — is strictly harder: matches need not be unique, may be exponentially many, and require specialized algorithms; e.g. modulo C the pattern $+(U, V)$ matches $a + b$ by both $(U \mapsto a, V \mapsto b)$ and $(U \mapsto b, V \mapsto a)$.

> [!warning] Warning 13.15: Syntactic matching is unique; equational matching is not
> The clean uniqueness of Proposition 13.7 is a property of **syntactic** matching ($\ell\sigma = u$). It fails for matching modulo nontrivial equations: $\ell\sigma \equiv u$ may have several or no solutions even when $\ell\sigma = u$ has one or none. Equational matching is the advanced extension required when rewriting is performed modulo a background theory (AC-rewriting); it is flagged here as a genuine increase in difficulty and is not assumed in the basic rewriting development of Section 14, which uses syntactic matching exclusively.

> [!definition] Definition 13.16: Typed matching
> In the typed setting each metavariable $U \in M$ carries a sort $\operatorname{sort}(U) \in S$, and a **typed match** of a well-sorted pattern $\ell$ against a well-sorted tree $u$ is a sort-respecting pattern substitution $\sigma$ (with $\operatorname{sort}(\sigma(U)) = \operatorname{sort}(U)$) such that $\ell\sigma = u$. The matching algorithm of Construction 13.6 is refined by checking, when binding $U \mapsto u'$, that $\operatorname{sort}(u') = \operatorname{sort}(U)$; a sort mismatch is an additional failure mode. The single-sorted theory is the case $|S| = 1$, where sort checks are vacuous and Proposition 13.7 holds verbatim.

> [!remark] Remark 13.17: Matching as the partial inverse of substitution
> Matching and substitution are dual operations. Substitution takes a pattern $\ell$ and a substitution $\sigma$ and *produces* the instance $\ell\sigma$. Matching takes a pattern $\ell$ and a target $u$ and *recovers* the unique $\sigma$ (if any) with $\ell\sigma = u$ — it inverts substitution along the pattern. This is why matching is a partial function: substitution-by-$\ell$ is injective on the metavariables of $\ell$ (each metavariable's value is read off a fixed position of the output), so its inverse is single-valued where defined. The redex-location step of rewriting (Section 14) is exactly "find a position $p$ and the unique $\sigma$ inverting the left-hand-side substitution at $t|_p$."

---

## 14. Tree Rewriting Systems

Rewriting is the directed transformation of trees by rules, applied at any position inside any context, with the matched instance of a left-hand side replaced by the corresponding instance of a right-hand side. This section assembles the one-step rewrite relation from the previously developed pieces — patterns, matching, substitution, contexts, replacement — so that it is fully explicit. Every clause names its data; nothing is left to "a rule applies when the left side matches a subtree." The construction proceeds: rules, variable condition, redex, contractum, context-at-position, one-step relation, closures, strategies, typed refinement.

### 14.1. Rewrite Rules and the Variable Condition

> [!definition] Definition 14.1: Rewrite rule
> Fix the syntactic alphabet $\Omega$ (operation symbols), object variables $X$, and metavariables $M$. A **rewrite rule** is an ordered pair of patterns
>
> $$
> \ell \to r, \qquad \ell, r \in \operatorname{Tree}_\Omega(X \sqcup M),
> $$
>
> with $\ell$ the **left-hand side** (lhs) and $r$ the **right-hand side** (rhs), subject to the two standing conditions:
>
> 1. **non-variable lhs**: $\ell$ is not a single metavariable (so $\ell \notin M$); otherwise the rule would match every tree at its root and rewriting could never terminate or be local.
> 2. **variable condition**: $\operatorname{Var}_M(r) \subseteq \operatorname{Var}_M(\ell)$, every metavariable of the rhs occurs in the lhs.
>
> The **metavariables of the rule** are $\operatorname{Var}_M(\ell)$. A **term rewriting system (TRS)** over $\Omega$ is a set $R$ of rewrite rules.

> [!warning] Warning 14.2: Why the variable condition is mandatory
> If a metavariable $U$ occurred in $r$ but not in $\ell$, then a match $\sigma$ of $\ell$ against a subtree would leave $\sigma(U)$ unconstrained, so $r\sigma$ would be ill-defined (or require an arbitrary choice) — the rule would not determine its result. The condition $\operatorname{Var}_M(r) \subseteq \operatorname{Var}_M(\ell)$ guarantees that the matching substitution computed from $\ell$ binds every metavariable needed to build $r\sigma$. The non-variable-lhs condition rules out the degenerate rule $U \to r$, which matches everything and trivializes the relation. Both conditions are presupposed by every result below; rules violating them are excluded from the definition of a TRS.

> [!example] Example 14.3: Standard rules and the conditions
> Over $\Omega = \{+^{(2)}, \neg^{(1)}, \dots\}$: associativity $+(+(U,V),W) \to +(U,+(V,W))$ (linear lhs, $\operatorname{Var}_M(r) = \{U,V,W\} = \operatorname{Var}_M(\ell)$, valid); commutativity $+(U,V) \to +(V,U)$ (valid but non-terminating, Section 15); double negation $\neg(\neg(U)) \to U$ (valid, $\operatorname{Var}_M(r) = \{U\} \subseteq \{U\}$, size-decreasing); idempotent collapse $f(U,U) \to U$ (nonlinear lhs, valid). The illegal "rule" $U \to f(U, V)$ fails both conditions (lhs a metavariable; $V \in \operatorname{Var}_M(r) \setminus \operatorname{Var}_M(\ell)$) and is not a rewrite rule.

### 14.2. Redexes and Contracta

> [!definition] Definition 14.4: Redex
> Let $R$ be a TRS and $t$ a ground tree. A **redex** of $t$ (with respect to $R$) is a triple $(p, \ell \to r, \sigma)$ consisting of a position $p \in D_t$, a rule $\ell \to r \in R$, and a pattern substitution $\sigma$ such that
>
> $$
> t|_p = \ell\sigma,
> $$
>
> i.e. $\sigma$ is the (unique, by Proposition 13.7) match of the lhs $\ell$ against the subtree $t|_p$. The subtree $t|_p = \ell\sigma$ is the **redex subtree** (an instance of the lhs); the position $p$ is the **redex position**; the rule is the **rule of the redex**. A tree is a **redex** simpliciter when it is $\ell\sigma$ for some rule and substitution (a redex at its root).

> [!definition] Definition 14.5: Contractum
> Given a redex $(p, \ell \to r, \sigma)$ of $t$, its **contractum** is the tree
>
> $$
> r\sigma = \widehat\sigma(r),
> $$
>
> the instance of the rhs under the same matching substitution. The variable condition (Definition 14.1) ensures $\sigma$ is defined on every metavariable of $r$, so $r\sigma$ is a well-defined ground tree. **Contracting** the redex replaces the redex subtree $\ell\sigma$ by the contractum $r\sigma$ at position $p$.

### 14.3. The Context at a Position and the One-Step Relation

> [!definition] Definition 14.6: Context associated to a redex position
> For a redex at position $p$ of $t$, the **associated context** is the one-hole context extracted at $p$,
>
> $$
> C := t[p := \Box], \qquad\text{so that}\qquad t = C[\,t|_p\,] = C[\ell\sigma]
> $$
>
> by the context–subtree decomposition (Theorem 7.6, Proposition 10.6). The context records "all of $t$ except the redex subtree," with the hole marking where the redex sits.

> [!definition] Definition 14.7: One-step rewrite relation
> Let $R$ be a TRS. The **one-step rewrite relation** $\to_R$ on ground trees is defined by: $t \to_R t'$ iff there exist a rule $\ell \to r \in R$, a position $p \in D_t$, a pattern substitution $\sigma$, and the associated context $C = t[p := \Box]$ such that
>
> $$
> t = C[\ell\sigma] \qquad\text{and}\qquad t' = C[r\sigma].
> $$
>
> Equivalently, in replacement form,
>
> $$
> t' = t[p := r\sigma] \qquad\text{where}\qquad t|_p = \ell\sigma.
> $$
>
> The pair $(t, t')$ is a **rewrite step**; the redex is contracted at $p$ by $\ell \to r$ via $\sigma$, inside the context $C$. The two formulations agree by Proposition 9.5 ($C[s] = t[p := s]$ for $C = t[p:=\Box]$).

> [!proposition] Proposition 14.8: The one-step relation is well-defined and effective
> For a finite TRS $R$ over a finite signature and a ground tree $t$, the set of redexes of $t$ is finite and computable: it is $\{(p, \ell\to r, \sigma) : p \in D_t,\ \ell\to r \in R,\ \sigma = \operatorname{match}(\ell, t|_p) \text{ exists}\}$, with at most $|D_t| \cdot |R|$ elements (one match per position–rule pair, by uniqueness of matches). For each redex the contractum $r\sigma$ and the result $t' = t[p := r\sigma]$ are computable. Hence $\to_R$ is a decidable, finitely-branching relation on the (infinite) set of ground trees.
>
> [!proof-sketch] Proof Sketch 14.8
> Each position $p$ and rule $\ell \to r$ admit at most one match of $\ell$ against $t|_p$ (Proposition 13.7), found by Construction 13.6; enumerating positions ($|D_t|$ of them) and rules ($|R|$ of them) enumerates all redexes. For each, $r\sigma$ is computed by substitution and $t[p := r\sigma]$ by replacement (Definition 9.3). Finiteness of the redex set bounds the out-degree of $t$ under $\to_R$, giving finite branching.

> [!example] Example 14.9: A one-step rewrite, fully instantiated
> Let $R = \{\neg(\neg(U)) \to U\}$ and $t = \wedge(p, \neg(\neg(q)))$ over $\Omega = \{\wedge^{(2)}, \neg^{(1)}\}$, $p, q \in \Omega_0$. The subtree at position $2$ is $t|_2 = \neg(\neg(q))$, which matches the lhs $\neg(\neg(U))$ with $\sigma : U \mapsto q$, so $(2, \neg(\neg(U)) \to U, \sigma)$ is a redex. The associated context is $C = t[2 := \Box] = \wedge(p, \Box)$. The contractum is $r\sigma = U\sigma = q$. The step is
>
> $$
> t = \wedge(p, \neg(\neg(q))) = C[\neg(\neg(q))] \ \to_R\ C[q] = \wedge(p, q) = t[2 := q] = t'.
> $$
>
> Every datum — rule, position $p=2$, substitution $\sigma$, context $C$, redex subtree $\ell\sigma = \neg(\neg(q))$, contractum $r\sigma = q$ — is explicit, and $t'$ is recovered both as $C[r\sigma]$ and as $t[2 := r\sigma]$.

### 14.4. Closure Properties of the One-Step Relation

> [!proposition] Proposition 14.10: Stability under contexts and substitutions
> The one-step relation $\to_R$ is closed under contexts and under substitution:
>
> 1. **context closure**: if $t \to_R t'$ then $C[t] \to_R C[t']$ for every one-hole context $C$;
> 2. **substitution closure**: if $t \to_R t'$ then $\widehat\tau(t) \to_R \widehat\tau(t')$ for every substitution $\tau$.
>
> [!proof-sketch] Proof Sketch 14.10
> (1) If $t \to_R t'$ via redex at $p$ with context $C_0 = t[p:=\Box]$, then $C[t]$ has the same redex at the shifted position $h \cdot p$ (where $h$ is the hole of $C$), with associated context $C \circ C_0$, and contracting it yields $C[t']$. Concretely $C[t] = (C \circ C_0)[\ell\sigma] \to_R (C \circ C_0)[r\sigma] = C[t']$. (2) If $t = C_0[\ell\sigma]$ then $\widehat\tau(t) = \widehat\tau(C_0)[\ell(\tau \star \sigma)]$ by the distribution law (Proposition 12.11) and the substitution composition law (Theorem 12.5), so the redex persists under $\tau$ with substitution $\tau \star \sigma$, and contracting yields $\widehat\tau(C_0)[r(\tau \star\sigma)] = \widehat\tau(t')$, using the variable condition so that $\tau \star \sigma$ is defined on $\operatorname{Var}_M(r)$.

Closure under contexts is the formal content of "rules apply inside arbitrary trees"; closure under substitution is what makes a rule with metavariables stand for all its instances. Together they say $\to_R$ is the least relation containing the **rule instances** $\ell\sigma \to r\sigma$ and closed under contexts — the inductive characterization recorded next.

> [!proposition] Proposition 14.11: Inductive characterization of $\to_R$
> $\to_R$ is the least binary relation on ground trees such that (i) $\ell\sigma \to_R r\sigma$ for every rule $\ell \to r \in R$ and substitution $\sigma$ (the **root steps**), and (ii) if $t_i \to_R t_i'$ then $f(t_1, \dots, t_i, \dots, t_n) \to_R f(t_1, \dots, t_i', \dots, t_n)$ for every $f \in \Omega_n$ (closure under immediate contexts).
>
> [!proof-sketch] Proof Sketch 14.11
> Any one-step rewrite $C[\ell\sigma] \to C[r\sigma]$ is generated from a root step (i) by iterating the immediate-context closure (ii) along the path from the root to the hole of $C$ (induction on $|h|$, $h$ the hole address). Conversely both (i) and (ii) are instances of Definition 14.7 (root steps take $p = \varepsilon$; immediate-context closure takes $C = f(t_1, \dots, \Box, \dots, t_n)$), so the relation of Definition 14.7 satisfies the closure clauses, and minimality identifies the two.

### 14.5. Rewrite Sequences and Closures

> [!definition] Definition 14.12: Rewrite sequences and derived relations
> From $\to_R$ form:
>
> $$
> \to_R^{0} := \{(t,t)\} \ (\text{identity}), \qquad \to_R^{k+1} := \to_R^{k} \circ \to_R, \qquad \to_R^{*} := \bigcup_{k \ge 0} \to_R^{k} \ (\text{reflexive-transitive closure}),
> $$
>
> also written $\twoheadrightarrow_R$; the **symmetric closure** $\leftrightarrow_R := \to_R \cup \to_R^{-1}$; and the **conversion relation** $\leftrightarrow_R^{*}$, the reflexive-transitive-symmetric closure (an equivalence relation). A **rewrite sequence** (synonym: **reduction sequence**, **derivation**) from $t$ is a (finite or infinite) sequence $t = t_0 \to_R t_1 \to_R t_2 \to_R \cdots$; its length is the number of steps. $t \twoheadrightarrow_R t'$ reads "$t$ reduces to $t'$."

> [!remark] Remark 14.13: Reduction, conversion, and the equational theory
> The directed relations $\to_R, \twoheadrightarrow_R$ model **computation** (one-way reduction), while $\leftrightarrow_R^{*}$ models **provable equality** in the equational theory obtained by reading each rule as a two-way equation. Section 15 studies when the directed relation computes the equivalence — when $t \leftrightarrow_R^* t'$ can be decided by reducing both to normal form — and Section 16 identifies $\leftrightarrow_R^{*}$ with the congruence generated by the rules read as equations. The conversion relation is the bridge from rewriting to quotients.

### 14.6. Strategies

> [!definition] Definition 14.14: Redex selection and strategies
> When $t$ has several redexes, a **rewrite strategy** is a rule for choosing which to contract (or which set to contract in parallel). Standard strategies, defined by the position and rule chosen:
>
> 1. **leftmost-innermost**: contract a redex none of whose proper subtrees is a redex, leftmost among these (call-by-value flavor);
> 2. **leftmost-outermost**: contract a redex no proper ancestor of which is a redex, leftmost among these (call-by-name flavor);
> 3. **parallel-innermost / parallel-outermost**: contract all such redexes simultaneously where they are pairwise disjoint;
> 4. **full parallel** (at a set of pairwise-disjoint redexes): contract all of them at once, using simultaneous replacement (Definition 9.9), legitimate because disjoint contractions commute (Proposition 9.10).
>
> A strategy is a **function** (or relation) selecting steps; it does not change $\to_R$ but restricts which sequences are followed.

> [!warning] Warning 14.15: Strategy matters only when the system is not confluent-terminating
> If $R$ is terminating and confluent (Section 15), every strategy reaches the same unique normal form, so strategy is a matter of efficiency, not result. When $R$ is non-terminating (e.g. commutativity) or non-confluent, the strategy can determine whether a normal form is reached at all and which one: an outermost strategy may terminate where an innermost one diverges, and vice versa. Parallel contraction at disjoint redexes is always safe (commuting replacements); contraction at *overlapping* redexes is the subject of critical-pair analysis (Section 15) and is not, in general, order-independent.

### 14.7. Typed Rewriting

> [!definition] Definition 14.16: Typed rewrite rule and typed one-step relation
> In the typed setting a **typed rewrite rule** $\ell \to r$ consists of well-sorted patterns with sorted metavariables satisfying:
>
> 1. **sort agreement**: $\operatorname{sort}(\ell) = \operatorname{sort}(r)$ (same output sort), so that contracting preserves the sort of the redex;
> 2. **variable condition with sorts**: $\operatorname{Var}_M(r) \subseteq \operatorname{Var}_M(\ell)$ and each shared metavariable has the same sort on both sides.
>
> The **typed one-step relation** is Definition 14.7 with typed matching (Definition 13.16) and the requirement that $\sigma$ be sort-respecting; the associated typed context $C : \operatorname{sort}(\ell) \Rightarrow \operatorname{sort}(t)$ then accepts both $\ell\sigma$ and $r\sigma$ (same sort), so $C[r\sigma]$ is well-sorted of sort $\operatorname{sort}(t)$.

> [!proposition] Proposition 14.17: Typed rewriting preserves sorts
> If $\ell \to r$ is a typed rule and $t \to_R t'$ by it, then $\operatorname{sort}(t') = \operatorname{sort}(t)$ and $t'$ is well-sorted. Hence the typed one-step relation restricts to each sort: $\to_R$ relates only trees of equal sort.
>
> [!proof-sketch] Proof Sketch 14.17
> Sort agreement gives $\operatorname{sort}(\ell\sigma) = \operatorname{sort}(\ell) = \operatorname{sort}(r) = \operatorname{sort}(r\sigma)$ (substitution preserves sort, Definition 12.13), so the redex subtree and contractum have equal sort. The associated typed context $C$ has input sort equal to that common sort and output sort $\operatorname{sort}(t)$; plugging either keeps the output sort (Proposition 11.4), so $\operatorname{sort}(C[r\sigma]) = \operatorname{sort}(t)$ and the result is well-sorted. The single-sorted relation is the case $|S| = 1$.

---

## 15. Rewriting Metatheory

Once the one-step relation is defined, the central questions are whether reduction halts, whether divergent reductions reconverge, and whether normal forms are unique. This section develops the standard metatheory — normalization and termination, confluence and its local form, the diamond and Church–Rosser properties, joinability, critical pairs and overlap, orthogonality, Newman's lemma, and completion — keeping the four implications among termination, confluence, and uniqueness of normal forms explicit and correctly directed. The setting is an abstract TRS $R$ over $\Omega$ with the one-step relation $\to_R$ of Section 14.

### 15.1. Normal Forms and Normalization

> [!definition] Definition 15.1: Irreducible tree, normal form
> A ground tree $t$ is **irreducible** (synonym: **a normal form**, **in $R$-normal form**) if there is no $t'$ with $t \to_R t'$ — equivalently, $t$ contains no redex (no position $p$ and rule whose lhs matches $t|_p$). Write $\operatorname{NF}(R)$ for the set of $R$-normal forms. A tree $t'$ is **a normal form of $t$** if $t \twoheadrightarrow_R t'$ and $t' \in \operatorname{NF}(R)$.

> [!definition] Definition 15.2: Weak and strong normalization
> $R$ is **weakly normalizing** (WN) if every tree has at least one normal form — for each $t$ there exists $t' \in \operatorname{NF}(R)$ with $t \twoheadrightarrow_R t'$. $R$ is **strongly normalizing** (SN, synonym: **terminating**, **noetherian**) if there is no infinite reduction sequence $t_0 \to_R t_1 \to_R t_2 \to_R \cdots$. SN implies WN (any maximal reduction ends at a normal form), but not conversely (a tree may have a terminating reduction to a normal form and also an infinite one).

> [!warning] Warning 15.3: Weak normalization does not give unique normal forms
> Weak normalization only asserts that *some* reduction reaches *some* normal form. Without confluence (Section 15.3) different reductions of the same tree may reach different normal forms, so "the normal form" is not well-defined under WN alone. Uniqueness of normal forms is a consequence of confluence, not of normalization; the function $\operatorname{nf}_R$ exists only when both hold.

### 15.2. Termination via Reduction Orders

> [!definition] Definition 15.4: Reduction order
> A strict partial order $\succ$ on ground trees is a **reduction order** if it is (i) **well-founded** (no infinite descending chain), (ii) **stable under contexts** ($t \succ t' \Rightarrow C[t] \succ C[t']$), and (iii) **stable under substitutions** ($t \succ t' \Rightarrow \widehat\sigma(t) \succ \widehat\sigma(t')$). A TRS $R$ is **compatible** with $\succ$ if $\ell\sigma \succ r\sigma$ for every rule $\ell \to r \in R$ and substitution $\sigma$; it suffices (using the variable condition) that $\ell \succ r$ as patterns for an order extended to metavariables.

> [!theorem] Theorem 15.5: Termination by a compatible reduction order
> If there exists a reduction order $\succ$ compatible with $R$ (i.e. $\ell\sigma \succ r\sigma$ for all rules and substitutions), then $R$ is terminating.
>
> [!proof-sketch] Proof Sketch 15.5
> Each one-step rewrite strictly decreases $\succ$: from $t = C[\ell\sigma] \to_R C[r\sigma] = t'$, compatibility gives $\ell\sigma \succ r\sigma$, and context stability lifts this to $C[\ell\sigma] \succ C[r\sigma]$, i.e. $t \succ t'$. An infinite reduction would yield an infinite $\succ$-descending chain, contradicting well-foundedness. Hence no infinite reduction exists.

> [!example] Example 15.6: A terminating and a non-terminating rule
> The double-negation rule $\neg(\neg(U)) \to U$ is compatible with the size order ($t \succ t'$ iff $|t| > |t'|$, which is well-founded and context/substitution stable): contracting strictly decreases size, so $R$ terminates (Theorem 15.5). The commutativity rule $+(U,V) \to +(V,U)$ is **not** terminating: $+(a,b) \to +(b,a) \to +(a,b) \to \cdots$ loops forever, and no reduction order can be compatible with it because $\ell\sigma$ and $r\sigma$ have equal size and the rule can be applied back and forth. Recursive path orders and polynomial interpretations are the standard tools for constructing reduction orders for less trivial systems.

### 15.3. Confluence and the Church–Rosser Property

> [!definition] Definition 15.7: Joinability, confluence, local confluence
> Two trees $u, v$ are **joinable**, written $u \downarrow_R v$, if there is $w$ with $u \twoheadrightarrow_R w$ and $v \twoheadrightarrow_R w$. The system $R$ is:
>
> 1. **confluent** if for all $t, u, v$ with $t \twoheadrightarrow_R u$ and $t \twoheadrightarrow_R v$, $u$ and $v$ are joinable;
> 2. **locally (weakly) confluent** if for all $t, u, v$ with $t \to_R u$ and $t \to_R v$ (single steps), $u$ and $v$ are joinable;
> 3. **Church–Rosser** if for all $u, v$ with $u \leftrightarrow_R^* v$ (convertible), $u$ and $v$ are joinable.

> [!theorem] Theorem 15.8: Confluence equals the Church–Rosser property
> $R$ is confluent iff $R$ is Church–Rosser.
>
> [!proof-sketch] Proof Sketch 15.8
> ($\Leftarrow$) Church–Rosser applied to $u \leftarrow\!\!\twoheadleftarrow t \twoheadrightarrow\!\!\rightarrow v$ (a special conversion) gives joinability, which is confluence. ($\Rightarrow$) By induction on the length of a conversion $u \leftrightarrow_R^* v$: each elementary $\leftrightarrow_R$ step, peak, or valley is absorbed using confluence to merge the two reduction fronts; the inductive step pastes a confluence diamond onto the running common reduct, yielding a single $w$ reachable from both ends.

> [!corollary] Corollary 15.9: Confluence gives unique normal forms
> If $R$ is confluent, then every tree has **at most one** normal form: if $t \twoheadrightarrow_R u$ and $t \twoheadrightarrow_R v$ with $u, v \in \operatorname{NF}(R)$, then $u = v$. If moreover $R$ is weakly normalizing, every tree has a **unique** normal form $\operatorname{nf}_R(t)$, and $u \leftrightarrow_R^* v \iff \operatorname{nf}_R(u) = \operatorname{nf}_R(v)$.
>
> [!proof-sketch] Proof Sketch 15.9
> Confluence makes $u, v$ joinable to some $w$; but $u, v$ are normal forms, so the reductions $u \twoheadrightarrow_R w$ and $v \twoheadrightarrow_R w$ have length $0$, forcing $u = w = v$. With WN a normal form exists; uniqueness makes $\operatorname{nf}_R$ a total function. The convertibility criterion is Church–Rosser (Theorem 15.8): $u \leftrightarrow_R^* v$ iff $u, v$ join, iff they have the same normal form.

### 15.4. The Four Implications

> [!warning] Warning 15.10: Termination and confluence are independent
> The two properties neither implies the other, and the implications among them and uniqueness of normal forms must be kept correctly directed:
>
> 1. **terminating $\not\Rightarrow$ confluent**: $\{a \to b,\ a \to c\}$ with $b, c$ distinct normal forms terminates but is not confluent ($a$ has two normal forms).
> 2. **confluent $\not\Rightarrow$ terminating**: $\{a \to a\}$ (or commutativity) is trivially confluent (the only reducts of $a$ are $a$, joinable) but does not terminate.
> 3. **terminating $+$ locally confluent $\Rightarrow$ confluent** (Newman's lemma, Theorem 15.11).
> 4. **terminating $+$ confluent $\Rightarrow$ unique normal forms** (Corollary 15.9 with SN giving existence): the pair is **convergent** (synonym: **complete**), and $\operatorname{nf}_R$ is a total computable function deciding $\leftrightarrow_R^*$.
>
> The decisive subtlety is that *local* confluence (single-step peaks) does **not** imply confluence in general; it does so only under termination.

> [!theorem] Theorem 15.11: Newman's lemma
> A terminating TRS is confluent iff it is locally confluent.
>
> [!proof-sketch] Proof Sketch 15.11
> ($\Rightarrow$) trivial (confluence implies its single-step special case). ($\Leftarrow$) by well-founded (noetherian) induction on $\to_R$, available because $R$ terminates. For a tree $t$ with $t \twoheadrightarrow_R u$ and $t \twoheadrightarrow_R v$: if either reduction is empty, joinability is trivial; otherwise factor $t \to_R t_1 \twoheadrightarrow_R u$ and $t \to_R t_2 \twoheadrightarrow_R v$. Local confluence joins $t_1, t_2$ at some $s$; the induction hypothesis (applied to the $\to_R$-smaller $t_1$, then $t_2$) joins $u$ with $s$ and $s$ with $v$, and transitivity assembles a common reduct of $u$ and $v$. Termination is exactly what licenses the noetherian induction and fails for the non-terminating counterexamples.

### 15.5. Critical Pairs and Overlaps

Local confluence is decidable for finite systems via **critical pairs**: the finitely many essential ways two rules' left-hand sides can overlap. This reduces confluence (for terminating systems) to a finite check.

> [!definition] Definition 15.12: Overlap and critical pair
> Let $\ell_1 \to r_1$ and $\ell_2 \to r_2$ be rules (renamed to share no metavariables). An **overlap** occurs at a non-variable position $p$ of $\ell_1$ if the subpattern $\ell_1|_p$ and $\ell_2$ are **unifiable** with most general unifier $\mu$ (Definition 13.12). The resulting **critical pair** is
>
> $$
> \big(\, r_1\mu,\ (\ell_1\mu)[p := r_2\mu] \,\big),
> $$
>
> the two trees obtained from the overlapped instance $\ell_1\mu$ by contracting, respectively, the outer redex (by rule $1$ at the root) and the inner redex (by rule $2$ at $p$). Overlaps at $p = \varepsilon$ of two distinct rules, and self-overlaps of a rule with itself at non-root positions, are included; the trivial root self-overlap of a rule with its renamed copy is excluded.

> [!theorem] Theorem 15.13: Critical pair lemma
> A TRS is locally confluent iff every critical pair $(s_1, s_2)$ is joinable ($s_1 \downarrow_R s_2$). For a finite system over a finite signature there are finitely many critical pairs, computed by unifying left-hand sides at non-variable positions, so local confluence is decidable.
>
> [!proof-sketch] Proof Sketch 15.13
> A single-step peak $u \leftarrow_R t \to_R v$ contracts two redexes of $t$ at positions $p_1, p_2$. If the redexes are at disjoint positions, they commute (Proposition 9.10) and join in one step each (a "disjoint peak"). If one is below the other but inside a *variable* part of the other's lhs, the substitution absorbs it (a "variable overlap") and they join using substitution closure. The remaining case — the redexes overlap at a non-variable position — is, up to context and substitution, exactly an instance of a critical pair; joinability of all critical pairs therefore yields joinability of every peak, and conversely each critical pair is a peak. Finiteness follows from finiteness of rules and non-variable positions.

> [!corollary] Corollary 15.14: Convergence criterion
> A terminating TRS is convergent (terminating and confluent, hence with unique normal forms) iff all its critical pairs are joinable. This is decidable: check termination by a reduction order, then check joinability of the finitely many critical pairs by reducing each component to normal form and comparing.
>
> [!proof-sketch] Proof Sketch 15.14
> Combine Newman's lemma (Theorem 15.11: termination reduces confluence to local confluence) with the critical pair lemma (Theorem 15.13: local confluence reduces to critical-pair joinability). Under termination, joinability of each critical pair is decided by normalizing both components (unique normal forms exist once confluence is being established, but joinability itself only needs a common reduct, found by reducing both sides).

### 15.6. Orthogonality

> [!definition] Definition 15.15: Left-linear, non-overlapping, orthogonal
> A TRS is **left-linear** if every rule's lhs is a linear pattern (no repeated metavariable). It is **non-overlapping** if it has no critical pairs (no two rules, and no rule with itself at a non-root position, overlap at a non-variable position). It is **orthogonal** if it is left-linear and non-overlapping.

> [!theorem] Theorem 15.16: Orthogonal systems are confluent
> Every orthogonal TRS is confluent, even without termination.
>
> [!proof-sketch] Proof Sketch 15.16
> Left-linearity makes redexes contract independently when disjoint or nested-in-variable-position; non-overlapping removes all critical-pair peaks. The standard proof introduces parallel (or complete-development) reduction $\Rrightarrow_R$, shows it satisfies the **diamond property** (if $t \Rrightarrow u$ and $t \Rrightarrow v$ then $u \Rrightarrow w \Lleftarrow v$ for some $w$) using left-linearity and absence of overlaps to develop all residual redexes, and concludes confluence of $\to_R$ since $\twoheadrightarrow_R$ and $\Rrightarrow_R^*$ coincide. Termination is not needed because the diamond property is a one-step (parallel) confluence that is preserved under iteration.

> [!remark] Remark 15.17: Confluence with and without termination
> Two distinct routes to confluence are now available. For **terminating** systems, confluence reduces to local confluence (Newman) and thence to a finite critical-pair check (Corollary 15.14) — the route used to certify convergent rewrite presentations. For possibly **non-terminating** systems, **orthogonality** (left-linear, non-overlapping) yields confluence directly via the diamond property (Theorem 15.16) — the route used for the lambda calculus and other systems where reduction need not halt. The two routes handle the two counterexamples of Warning 15.10: the first needs termination to rule out $\{a\to b, a\to c\}$ (which is non-overlapping at the root but has a root critical pair $b \neq c$), the second tolerates non-termination but forbids overlaps.

### 15.7. Completion and Rewriting as Oriented Equations

> [!remark] Remark 15.18: Knuth–Bendix completion, conceptually
> A set of equations $E$ may fail to be convergent when oriented naively into rules. **Knuth–Bendix completion** attempts to transform $(E, \succ)$ — equations together with a reduction order — into a convergent TRS $R$ presenting the same equational theory ($\leftrightarrow_R^* = {=_E}$, Section 16) by repeatedly: orienting each equation $\ell = r$ into $\ell \to r$ or $r \to \ell$ according to $\succ$; computing critical pairs; and adjoining the normal forms of any non-joinable critical pair as new rules, until no non-joinable critical pairs remain. The procedure may succeed (yielding a decision procedure for $=_E$ by normal-form comparison), fail (when an equation cannot be oriented, e.g. commutativity), or run forever. It is the algorithmic bridge from an equational specification to a convergent rewrite implementation, and its termination/orientation obstructions are exactly the AC-type equations that motivate rewriting *modulo* a congruence (Sections 13.6, 16.6).

> [!remark] Remark 15.19: Rules as oriented equations — the metatheoretic summary
> A rewrite system is an **orientation** of an equational theory: each rule $\ell \to r$ is the equation $\ell = r$ given a direction. The directed relation $\twoheadrightarrow_R$ computes, and the symmetric relation $\leftrightarrow_R^*$ is provable equality. Termination guarantees computation halts; confluence guarantees the answer is independent of choices; together (convergence) they make $\operatorname{nf}_R$ a decision procedure for the equational theory, computing the canonical representative of each equivalence class. The metatheory of this section is precisely the analysis of when an oriented equational theory yields such a decision procedure — when rewriting *computes* the quotient of the next section.

---

## 16. Equations, Congruences, Normal Forms, and Quotient Tree Algebras

Directed rewriting computes; symmetric equations identify. This section develops the undirected side: equations between trees, the congruence they generate, the quotient tree algebra that collapses trees along a congruence, and the precise relationship between rewriting and quotient equality. The central object is the quotient $\operatorname{Tree}_\Omega(X)/{\equiv}$, an $\Omega$-algebra whose elements are equivalence classes of trees, and the central theorem is that a convergent rewrite system gives a system of canonical representatives — normal forms — for the classes of the congruence it generates.

### 16.1. Congruences on Trees

> [!definition] Definition 16.1: Congruence
> An equivalence relation $\equiv$ on $\operatorname{Tree}_\Omega(X)$ is a **congruence** if it is **compatible** with every constructor: for each $f \in \Omega_n$ and all trees $t_i, s_i$,
>
> $$
> t_1 \equiv s_1, \ \dots, \ t_n \equiv s_n \;\Longrightarrow\; f(t_1, \dots, t_n) \equiv f(s_1, \dots, s_n).
> $$
>
> Equivalently (Proposition 16.3) $\equiv$ is closed under contexts: $t \equiv s \Rightarrow C[t] \equiv C[s]$ for every one-hole context $C$. The set of congruences is closed under arbitrary intersection and contains the diagonal $\Delta$ (syntactic equality) and the total relation $\nabla$.

> [!definition] Definition 16.2: Congruence generated by a relation
> For a binary relation $B \subseteq \operatorname{Tree}_\Omega(X)^2$, the **congruence generated by $B$**, written $\operatorname{Cg}(B)$, is the least congruence containing $B$:
>
> $$
> \operatorname{Cg}(B) := \bigcap \{\, \equiv\ :\ B \subseteq{} \equiv,\ \equiv \text{ a congruence} \,\},
> $$
>
> well-defined because congruences are closed under intersection. It is constructed from below by closing $B$ under reflexivity, symmetry, transitivity, and the constructor-compatibility clause (equivalently context closure).

> [!proposition] Proposition 16.3: Constructor compatibility equals context closure
> An equivalence relation $\equiv$ is compatible with all constructors iff it is closed under all one-hole contexts: $t \equiv s \Rightarrow C[t] \equiv C[s]$ for every $C \in \operatorname{Ctx}^1_L$.
>
> [!proof-sketch] Proof Sketch 16.3
> ($\Rightarrow$) By structural induction on $C$: the hole case is $t \equiv s$ itself; the constructor case $C = f(\dots, C', \dots)$ uses compatibility of $f$ with the induction hypothesis $C'[t] \equiv C'[s]$, the other arguments related to themselves by reflexivity. ($\Leftarrow$) Constructor compatibility is the special case of context closure for the immediate contexts $C = f(s_1, \dots, \Box, \dots, s_n)$, combined componentwise via transitivity to vary all arguments at once.

### 16.2. Equational Theories

> [!definition] Definition 16.4: Equation, axiom set, equational consequence
> An **equation** over $\Omega$ (with metavariables $M$) is a pair of patterns written $\ell = r$. A set $E$ of equations is an **equational theory** (or **axiom set**). The **congruence generated by $E$** on ground trees is
>
> $$
> {=_E} := \operatorname{Cg}\big(\{\, (\ell\sigma, r\sigma) : (\ell = r) \in E,\ \sigma \text{ a substitution} \,\}\big),
> $$
>
> the least congruence containing every substitution instance of every axiom. Two trees with $t =_E s$ are **provably equal** (in $E$); $=_E$ is the **equational theory generated by $E$**.

> [!theorem] Theorem 16.5: Derivational (Birkhoff) characterization of $=_E$
> $t =_E s$ holds iff $t$ and $s$ are connected by a finite chain of **equational rewrites**: there is a sequence $t = u_0, u_1, \dots, u_m = s$ where each adjacent pair $u_j, u_{j+1}$ has the form $C[\ell\sigma], C[r\sigma]$ (or $C[r\sigma], C[\ell\sigma]$) for some axiom $\ell = r \in E$, context $C$, and substitution $\sigma$. Equivalently $=_E$ is generated from the axiom instances by the rules reflexivity, symmetry, transitivity, congruence (constructor compatibility), and substitution.
>
> [!proof-sketch] Proof Sketch 16.5
> The relation defined by such chains is reflexive (empty chain), symmetric (reverse the chain), transitive (concatenate chains), context-closed (apply a context to every link), and contains the axiom instances; hence it is a congruence containing $B$, so it contains $\operatorname{Cg}(B) = {=_E}$. Conversely every link is in any congruence containing $B$ (axiom instance under a context), so the chain relation is contained in every such congruence, hence in $=_E$. The two inclusions give equality; the inference-rule formulation is the same closure described proof-theoretically.

> [!remark] Remark 16.6: Equational logic is rewriting without orientation
> Theorem 16.5 exhibits $=_E$ as exactly the conversion relation $\leftrightarrow_R^*$ (Definition 14.12) of the TRS $R$ obtained by orienting each axiom *both* ways: a provable equality is a finite undirected rewrite chain. This is the precise sense in which an equation $\ell = r$ "is" a two-way rule. The asymmetry of $\to_R$ versus $=_E$ is solely orientation; the symmetric closure of any orientation recovers $=_E$.

### 16.3. Quotient Tree Algebras

> [!definition] Definition 16.7: Quotient tree algebra
> Let $\equiv$ be a congruence on $\operatorname{Tree}_\Omega(X)$. The **quotient tree algebra** $\operatorname{Tree}_\Omega(X)/{\equiv}$ has carrier the set of equivalence classes $\{[t]_\equiv : t \in \operatorname{Tree}_\Omega(X)\}$ and constructor operations defined on representatives:
>
> $$
> f^{/\equiv}\big([t_1]_\equiv, \dots, [t_n]_\equiv\big) := \big[\, f(t_1, \dots, t_n) \,\big]_\equiv \qquad (f \in \Omega_n).
> $$
>
> The **quotient map** $\operatorname{nat}_\equiv : \operatorname{Tree}_\Omega(X) \to \operatorname{Tree}_\Omega(X)/{\equiv}$, $t \mapsto [t]_\equiv$, is a surjective homomorphism with kernel $\equiv$.

> [!proposition] Proposition 16.8: Well-definedness requires exactly a congruence
> The operations $f^{/\equiv}$ of Definition 16.7 are well-defined (independent of the chosen representatives) iff $\equiv$ is a congruence. Conversely, if every $f^{/\equiv}$ is well-defined, $\equiv$ is a congruence.
>
> [!proof-sketch] Proof Sketch 16.8
> Well-definedness of $f^{/\equiv}$ at all arguments is precisely the implication "$t_i \equiv s_i \ \forall i \Rightarrow f(\vec t\,) \equiv f(\vec s\,)$," which is constructor compatibility (Definition 16.1). Thus compatibility is necessary and sufficient. An arbitrary equivalence relation that is not a congruence yields representative-dependent, hence undefined, operations.

> [!warning] Warning 16.9: A mere equivalence relation does not yield a quotient algebra
> If $\equiv$ is an equivalence relation but not a congruence, the formula $f^{/\equiv}([t_1],\dots,[t_n]) = [f(\vec t\,)]$ assigns different classes to different representatives of the same inputs, and no algebra structure on the class set makes $\operatorname{nat}_\equiv$ a homomorphism. Compatibility with the constructors is the exact well-definedness condition. This is the prototype of every "descent" obligation: a fold, evaluation, or substitution descends to the quotient only when it respects $\equiv$ (Warning 5.8, Section 16.5).

> [!theorem] Theorem 16.10: Universal property of the quotient tree algebra
> Let $\equiv$ be a congruence on $\operatorname{Tree}_\Omega(X)$ and $h : \operatorname{Tree}_\Omega(X) \to \mathbf{B}$ a homomorphism with $\equiv\ \subseteq \ker h$. Then there is a **unique** homomorphism $\bar h : \operatorname{Tree}_\Omega(X)/{\equiv} \to \mathbf{B}$ with $\bar h \circ \operatorname{nat}_\equiv = h$, namely $\bar h([t]_\equiv) = h(t)$. In particular $\operatorname{Tree}_\Omega(X)/{=_E}$ is the **free algebra in the variety defined by $E$** on the generators $X$: it satisfies every equation of $E$ and maps uniquely to any $E$-algebra extending an assignment of $X$.
>
> [!proof-sketch] Proof Sketch 16.10
> $\bar h$ is well-defined because $[t] = [t'] \Rightarrow (t,t') \in {\equiv} \subseteq \ker h \Rightarrow h(t) = h(t')$; it is a homomorphism because $h$ and $\operatorname{nat}_\equiv$ are and $\operatorname{nat}_\equiv$ is surjective; uniqueness because the value on each class is forced by surjectivity of $\operatorname{nat}_\equiv$. For the relative-freeness statement, take $\equiv\ = {=_E}$: the quotient satisfies $E$ (axiom instances are collapsed) and the UMP transports through $\operatorname{nat}_{=_E}$ to give the free $E$-algebra.

### 16.4. Raw Syntax versus Quotient Syntax

> [!warning] Warning 16.11: Syntactic equality versus quotient equality
> In raw syntax all distinct trees are distinct: $f(x,y) \neq f(y,x)$, $+(+(a,b),c) \neq +(a,+(b,c))$. Imposing equations collapses some of these: under commutativity $f(x,y) =_E f(y,x)$, under associativity $+(+(a,b),c) =_E +(a,+(b,c))$. The quotient $\operatorname{Tree}_\Omega(X)/{=_E}$ remembers only the **class**, discarding the exact tree shape that the theory declares irrelevant. The two equalities must never be conflated: a property defined on raw trees (size, a specific position's label, the precise frontier) is generally **not** invariant under $=_E$ and so does not descend to the quotient; only $=_E$-invariant data live on classes.

> [!example] Example 16.12: Standard quotients
> The quotient construction subsumes the passage from raw syntax to familiar algebraic objects: raw group words modulo the group axioms (associativity, inverse, unit) give the free group; raw Boolean expressions modulo the Boolean identities give the free Boolean algebra; raw arithmetic expressions modulo the ring axioms give the free commutative ring; raw formulas modulo tautological equivalence give the Lindenbaum algebra; raw lambda terms modulo $\alpha\beta\eta$ give the term model. In each case $\operatorname{Tree}_\Omega(X)/{=_E}$ is the syntactic free object of the corresponding variety (Theorem 16.10), and the equations are the variety's axioms.

### 16.5. When Rewriting Computes Quotient Equality

> [!theorem] Theorem 16.13: Convergent rewriting decides the generated congruence
> Let $E$ be an equation set and $R$ an orientation of $E$ (each rule $\ell \to r$ obtained from an axiom $\ell = r$) such that $R$ is **convergent** (terminating and confluent). Then:
>
> 1. the conversion relation of $R$ equals the congruence of $E$: $\leftrightarrow_R^* \,=\, {=_E}$;
> 2. every tree $t$ has a unique normal form $\operatorname{nf}_R(t)$, and the normal forms are a **system of canonical representatives** for the classes of $=_E$: $[t]_{=_E} \mapsto \operatorname{nf}_R(t)$ is a well-defined bijection from $\operatorname{Tree}_\Omega(X)/{=_E}$ onto $\operatorname{NF}(R)$;
> 3. quotient equality is decidable by normalization: $t =_E s \iff \operatorname{nf}_R(t) = \operatorname{nf}_R(s)$.
>
> [!proof-sketch] Proof Sketch 16.13
> (1) Orienting $E$ both ways recovers $=_E$ as $\leftrightarrow_R^*$ (Remark 16.6), and orienting one way gives a relation whose symmetric-transitive closure is still $=_E$ because each reversed rule instance is an axiom instance. (2) Convergence gives existence (termination) and uniqueness (confluence, Corollary 15.9) of normal forms, so $\operatorname{nf}_R$ is total; it is constant on $=_E$-classes because $t =_E s \Rightarrow t \leftrightarrow_R^* s \Rightarrow \operatorname{nf}_R(t) = \operatorname{nf}_R(s)$ (Church–Rosser), and injective on classes because equal normal forms force convertibility; surjectivity onto $\operatorname{NF}(R)$ is clear. (3) is the decision procedure: normalize both and compare.

> [!warning] Warning 16.14: Not every quotient is presented by a convergent system
> Theorem 16.13 requires a convergent orientation, which need not exist. Commutativity $+(U,V) = +(V,U)$ cannot be oriented into a terminating rule, and associativity–commutativity together (AC) generically resist finite convergent orientation. The standard remedies — rewriting **modulo** AC (computing in $\operatorname{NF}$ up to AC-equivalence using AC-matching, Section 13.6) and Knuth–Bendix completion (Remark 15.18) — extend the reach of the method but do not make every congruence rewrite-decidable. Some equational theories are undecidable, so no decision procedure (convergent system or otherwise) exists. The slogan "rewriting computes the quotient" holds exactly when a convergent (possibly modulo-AC) presentation is available.

### 16.6. Quotients Up to Structural Equivalences

> [!remark] Remark 16.15: AC, identity, and the canonical-representative program
> The most frequent quotients in practice are by **associativity, commutativity, and unit** equations. Associativity is handled by **flattening** variadic operators (replacing nested binary nodes by a single variadic node, Section 17 of the companion calculus), commutativity by **sorting** the children of commutative nodes into a canonical order, and units by **eliminating** identity arguments. The composite "flatten, sort, simplify units" computes a canonical representative of each AC-with-unit class, realizing the quotient by a normalization function even where a finite convergent term-rewriting orientation is unavailable. This is the constructive face of the quotient: a chosen normal form per class, computed by structural recursion.

> [!remark] Remark 16.16: Binding quotients are different in kind
> Quotients by $\alpha$-equivalence (renaming of bound variables), $\beta$-reduction, and definitional equality arise in binding syntax (lambda calculus, first-order logic with quantifiers) and are flagged here as **outside** the untyped non-binding setting of this treatise. They differ structurally: $\alpha$-equivalence is a congruence on a syntax with binders, where naive replacement is unsound (capture, Warning 16.17), and $\beta$/definitional equality combine a rewrite relation with the binding discipline. Their treatment requires the capture-avoiding refinement of substitution and is the subject of the typed, binding-aware sequel; in the present non-binding calculus, raw replacement, context filling, and substitution are all capture-free and the quotient theory above applies without qualification.

> [!warning] Warning 16.17: Why binding breaks naive substitution (boundary note)
> In a syntax with binders, the context $\forall x.\,\Box$ filled with $P(x)$ yields $\forall x.\,P(x)$, **capturing** the free $x$ — legitimate as schema/context filling but not as object-level substitution. Object-level capture-avoiding substitution $\varphi[x := t]$ must rename bound variables to avoid capturing the free variables of $t$. This divergence between context filling (capture-permitting) and capture-avoiding substitution (capture-forbidding) does not arise in the present non-binding trees, where every leaf is either a constructor-free object variable subject to uniform substitution or a constant; it is recorded here only to mark the boundary at which the untyped tree calculus must be upgraded, and the distinction between the three operations — raw replacement, context filling, capture-avoiding substitution — becomes load-bearing.

---

## 17. Term Graphs, DAGs, Sharing, and Compression

A tree records every occurrence of a repeated substructure separately. Many applications instead **share** equal substructures, representing them once and pointing to them several times; the resulting object is a directed acyclic graph (DAG), or more generally a term graph, and is no longer a tree. This section develops the tree/DAG distinction precisely, the unfolding that recovers a tree from a DAG, the sharing that compresses a tree into a DAG, and the resulting shift of category from trees to term graphs. The treatment is compact but exact, and is tied back to subtree equality, congruence closure, and rewriting.

### 17.1. Expression DAGs and Sharing

> [!definition] Definition 17.1: Term DAG over a signature
> A **term DAG** over $(L, \rho)$ is a finite directed acyclic graph with a distinguished **root** node, in which each node carries a label $a \in L$ and has an **ordered** list of exactly $\rho(a)$ out-edges to child nodes, and every node is reachable from the root. Unlike a tree domain, a node may have **in-degree greater than one** (several parents pointing to it), which is **sharing**. The acyclicity forbids a node from being its own descendant.

> [!definition] Definition 17.2: Unfolding a DAG to a tree
> The **unfolding** $\operatorname{unf}(G)$ of a term DAG $G$ is the tree obtained by traversing $G$ from the root and duplicating every shared node once per access path: recursively, $\operatorname{unf}$ of a node labelled $a$ with children $c_1, \dots, c_n$ is $a(\operatorname{unf}(c_1), \dots, \operatorname{unf}(c_n))$. Acyclicity guarantees the recursion terminates, so $\operatorname{unf}(G)$ is a finite tree. Two DAGs are **tree-equivalent** if they unfold to the same tree.

> [!proposition] Proposition 17.3: Unfolding is a well-defined fold; sharing is invisible to it
> Unfolding is the structural recursion (Theorem 5.7) computing, at each node, the constructor $a$ applied to the unfoldings of its children; it is well-defined on acyclic graphs by induction on the longest path to a sink. Distinct DAGs that share differently but unfold equally — e.g. a fully unshared tree and its maximally shared DAG — have the same unfolding, so the tree records no sharing information.
>
> [!proof-sketch] Proof Sketch 17.3
> Acyclicity gives a well-founded "reachable-from" order on nodes (longest-path-to-sink strictly decreases along edges), licensing the recursion. The unfolding clause is exactly the constructor clause of a fold into $\operatorname{Tree}_L$, so by uniqueness any two computations agree. Sharing affects only how many times a subtree's unfolding is recomputed, not the result, whence tree-equivalent DAGs unfold identically.

> [!definition] Definition 17.4: DAGification (maximal sharing) and hash-consing
> **DAGification** of a tree $t$ is the construction of a term DAG $\operatorname{dag}(t)$ with $\operatorname{unf}(\operatorname{dag}(t)) = t$ that shares **all equal subtrees**: distinct positions $p, q$ of $t$ with $t|_p = t|_q$ map to the **same** DAG node. It is computed by **hash-consing**: process nodes bottom-up, maintaining a table keyed by (label, child-node-identities); before creating a node, look it up and reuse the existing one if present. The result is the minimal-size DAG unfolding to $t$, with one node per distinct subtree of $t$.

### 17.2. Trees, DAGs, and the Category Shift

> [!warning] Warning 17.5: Sharing is not syntactic equality
> A DAG node shared between two positions asserts that the two subtrees are **equal as trees** (Definition 3.15), which is *syntactic* equality, the one DAGification is built to detect. Sharing is therefore sound for syntactic equality and only for it: a DAG must not share two subtrees that are merely congruent or semantically equal unless an explicit abstraction map (an e-graph's equivalence, a congruence-closure structure) declares the identification. Conversely, a tree never shares, so it distinguishes a repeated subtree's occurrences as distinct **positions** even though they carry equal subtrees. The tree records occurrences; the DAG records distinct subtrees.

> [!warning] Warning 17.6: Many tree recursions assume unique parenthood
> Structural recursion and context extraction rest on each non-root node having a **unique** parent (Definition 3.2), which holds in trees and fails in DAGs (a shared node has several parents). Consequently: a bottom-up fold still works on a DAG (compute once per node, memoized by node identity — indeed this is the efficiency gain), but **context extraction** becomes ambiguous, since a shared node sits in several surrounding contexts, one per parent. DAGification is therefore not a transparent optimization at the level of the calculus: it changes the ambient category from trees (initial $F_L$-algebra) to acyclic term graphs, on which "the context of a subterm" is no longer single-valued. Operations defined by position must be re-examined: replacement at a shared node affects all its occurrences at once, which is sometimes the intended sharing semantics and sometimes a bug.

> [!definition] Definition 17.7: Cyclic term graphs and regular infinite trees
> Allowing **cycles** in a term graph (dropping acyclicity) yields a finite presentation of an **infinite** tree: unfolding a cyclic graph never terminates and produces an infinite tree (Section 22), which is **regular** — it has only finitely many distinct subtrees, namely the unfoldings of the graph's nodes. Cyclic term graphs are the finite data structures behind regular infinite trees, recursive type definitions, and streams, and graph rewriting on them models computation that a tree rewriting cannot finitely present.

### 17.3. Uses and Graph Rewriting

> [!remark] Remark 17.8: Where sharing pays
> Maximal sharing compresses a tree of size $|t|$ to a DAG of size equal to the number of *distinct* subtrees of $t$, which can be exponentially smaller (e.g. a balanced tree of repeated halves). The applications are: **common subexpression elimination** in compilers; **memoized evaluation** and **memoized folds**, where a fold value is computed once per distinct subtree (Section 23); **proof compression**, sharing repeated lemmas; **efficient congruence closure** and **e-graphs / equality saturation**, where the graph stores an entire congruence class compactly; and **term graph rewriting**, which rewrites the shared representation directly. Each trades the tree's positional transparency for compactness and shared recomputation, exactly along the tree/DAG distinction of Warning 17.6.

> [!remark] Remark 17.9: Graph rewriting versus tree rewriting
> Tree rewriting (Section 14) contracts a redex at one position, affecting one occurrence. **Graph rewriting** contracts a redex on the shared graph, automatically affecting **all** occurrences of the shared redex node at once — a single graph step can realize many tree steps. This makes graph rewriting more efficient but semantically distinct: it implements rewriting *modulo sharing*, sound for the tree semantics only when the sharing reflects genuine syntactic equality and the rule does not need to distinguish occurrences. The correspondence "graph step ↔ parallel tree steps at all unfolded copies" is the precise bridge, and it is exact for left-linear rules where copies do not interfere.

---

## 18. Tree Automata and Tree Languages

A tree automaton is a finite-state recognizer for a set of trees, the tree analogue of a finite word automaton. Tree automata formalize decidable syntactic predicates over trees — well-formedness, sort-correctness, membership in a grammar-defined class, presence of a pattern — and connect the tree calculus to formal language theory and to syntax/proof checking. This section gives the definitions, the determinization and closure results, the recognizable = regular characterization, and the link to folds and to the rewriting spine. The treatment is compact and precise.

### 18.1. Tree Languages and Bottom-Up Automata

> [!definition] Definition 18.1: Tree language
> A **tree language** over $(L, \rho)$ is a subset $\mathcal{L} \subseteq \operatorname{Tree}_L$. Examples: all well-formed trees over a sub-alphabet; all trees containing a given label; all trees in a given sort (typed setting); all normal forms of a TRS; all instances of a fixed linear pattern.

> [!definition] Definition 18.2: Bottom-up finite tree automaton
> A **(nondeterministic) bottom-up finite tree automaton** (NFTA) over $(L, \rho)$ is a tuple $\mathcal{A} = (Q, L, Q_f, \Delta)$ where $Q$ is a finite set of **states**, $Q_f \subseteq Q$ the **accepting (final) states**, and $\Delta$ a set of **transitions** of the form
>
> $$
> a(q_1, \dots, q_n) \to q \qquad (a \in L_n,\ q_1, \dots, q_n, q \in Q),
> $$
>
> reading "a node labelled $a$ whose children are in states $q_1, \dots, q_n$ may take state $q$." A **run** of $\mathcal{A}$ on a tree $t$ assigns states to nodes bottom-up consistently with $\Delta$; the run **accepts** if the root state is in $Q_f$. The **language recognized** is $\mathcal{L}(\mathcal{A}) := \{ t : \text{some run of } \mathcal{A} \text{ on } t \text{ accepts}\}$.

> [!definition] Definition 18.3: Determinism, top-down automata
> $\mathcal{A}$ is **deterministic** (a DFTA) if for each $a$ and $(q_1,\dots,q_n)$ there is at most one transition $a(q_1,\dots,q_n) \to q$; then each tree has at most one run, and the run is the fold (Theorem 5.7) into $Q$ with $h_a = $ the transition function. A **top-down** tree automaton instead assigns the root an initial state and propagates states to children by transitions $q \to a(q_1, \dots, q_n)$; top-down nondeterministic automata recognize the same languages as bottom-up ones, but deterministic top-down automata are strictly weaker.

> [!example] Example 18.4: Recognizing "contains label $b$" as a finite-state fold
> Over $L$ with a distinguished $b \in L$, take $Q = \{0, 1\}$ (0 = "subtree contains no $b$", 1 = "contains $b$"), $Q_f = \{1\}$, and transitions $a(q_1, \dots, q_n) \to 1$ if $a = b$ or some $q_i = 1$, else $\to 0$. This DFTA accepts exactly the trees containing $b$; its run is the fold with $h_a(\vec q) = [a = b] \vee \bigvee_i q_i$, exhibiting the recognizer as a Boolean-valued structural recursion (Definition 6.2 analogue).

### 18.2. Determinization, Closure, and Recognizability

> [!theorem] Theorem 18.5: Determinization
> For every NFTA there is a DFTA recognizing the same language, obtained by the **subset construction**: states are sets of NFTA-states, the transition on $a$ with child subsets $S_1, \dots, S_n$ is $\{ q : a(q_1,\dots,q_n) \to q \in \Delta,\ q_i \in S_i\}$, and accepting subsets are those meeting $Q_f$. Hence nondeterministic and deterministic bottom-up automata recognize the same class of languages.
>
> [!proof-sketch] Proof Sketch 18.5
> The subset construction's run on $t$ computes, at each node, the *set* of all states the NFTA could assign there; this is again a fold (into $\mathcal{P}(Q)$). Acceptance of the determinized run (root subset meets $Q_f$) holds iff some NFTA run reaches a final root state, i.e. iff $t \in \mathcal{L}(\mathcal{A})$. Finiteness of $\mathcal{P}(Q)$ keeps the DFTA finite.

> [!definition] Definition 18.6: Regular (recognizable) tree language; regular tree grammar
> A tree language is **recognizable** (synonym: **regular**) if it is $\mathcal{L}(\mathcal{A})$ for some finite tree automaton. Equivalently it is generated by a **regular tree grammar** — a finite set of nonterminals with productions $A \to a(B_1, \dots, B_n)$ — the nonterminals playing the role of states. Regular tree languages are exactly the recognizable ones.

> [!theorem] Theorem 18.7: Closure properties and decidability
> The class of regular tree languages is effectively closed under union, intersection, and complement, and the emptiness, membership, finiteness, and equivalence problems are decidable.
>
> [!proof-sketch] Proof Sketch 18.7
> Union and intersection: product automaton with appropriately combined accepting sets. Complement: determinize, complete, and complement the accepting set (correct only after determinization). Membership: run the (determinized) automaton, a fold, in linear time. Emptiness: mark the set of reachable states bottom-up (least fixed point); the language is empty iff no final state is reachable. Equivalence: reduce to emptiness of the symmetric difference via the closure operations. All constructions are effective on finite automata.

### 18.3. Connections to the Spine

> [!remark] Remark 18.8: Automata recognize; folds compute; the connection
> A deterministic bottom-up tree automaton **is** a finite-state fold (Definition 18.3): the carrier is the finite state set, and recognition is the fold value at the root tested for acceptance. This places tree automata inside the structural-recursion framework of Section 5 with a *finite* carrier, which is exactly what makes their decision problems decidable. The recognizable predicates are therefore the syntactic properties computable by a height-uniform bottom-up pass: well-formedness over a sub-signature, sort-correctness (Proposition 4.17 is a local edge condition, hence regular), being in normal form for a left-linear TRS (the redex patterns form a regular set, and its complement is recognizable), and membership in a pattern's match set (for linear patterns).

> [!remark] Remark 18.9: Applications to syntax and proof checking
> Tree automata supply decidable membership tests for grammar-defined syntactic classes: whether a parse tree conforms to a grammar, whether a formula is in negation normal form, whether a proof tree obeys the local side-conditions of its inference rules (each rule is a local constraint on a node and its children, hence a transition), and whether a term is a normal form. Because the regular languages are closed under Boolean operations and have decidable emptiness, conjunctions of such syntactic disciplines remain decidable, and counterexamples are extractable. Tree automata are thus the recognizer layer sitting atop the tree calculus, complementary to the transducer layer (Section 19) that transforms rather than recognizes.

---

## 19. Tree Transducers and Tree Transformations

A tree transducer is a finite device that transforms input trees into output trees, the operational model of structured recursive syntax transformations. Where a tree automaton recognizes a language, a transducer computes a tree-to-tree (or tree-to-forest) function. This section gives the bottom-up and top-down models, identifies structural recursion as the prototypical transformation, and connects transducers to the rewriting and normalization spine through concrete syntactic passes. The treatment is compact and precise.

### 19.1. Structural Recursion as Transformation

> [!definition] Definition 19.1: Tree homomorphism (relabelling transducer)
> A **tree homomorphism** from $(L, \rho_L)$ to $(M, \rho_M)$ is given by, for each $a \in L_n$, an output **context** $C_a$ with $n$ ordered holes over $M$; it induces the transformation
>
> $$
> \mathcal{H}\big(a(t_1, \dots, t_n)\big) := C_a\big[\mathcal{H}(t_1), \dots, \mathcal{H}(t_n)\big],
> $$
>
> a fold (Theorem 5.7) into $\operatorname{Tree}_M$ whose constructor clauses are context pluggings. Rank-preserving relabelling (Definition 4.10) is the special case $C_a = \varphi(a)(\Box_0, \dots, \Box_{n-1})$; more general $C_a$ may delete, duplicate, or restructure children, realizing nontrivial syntax-directed translation.

> [!remark] Remark 19.2: Folds are the semantic kernel of transduction
> Every deterministic tree transformation defined by a single bottom-up pass with finite control is a fold whose carrier is (finite control state $\times$ output tree); the relabelling/tree-homomorphism case is the stateless fold into $\operatorname{Tree}_M$. The transducer formalism adds **finite state** to the fold, exactly as the automaton (Section 18) added finite state to the Boolean fold, allowing the output at a node to depend on a bounded summary of its subtree in addition to the children's outputs.

### 19.2. Bottom-Up and Top-Down Transducers

> [!definition] Definition 19.3: Bottom-up tree transducer
> A **bottom-up tree transducer** is a tuple $(Q, L, M, Q_f, \Delta)$ with finite states $Q$, accepting states $Q_f$, and transition rules
>
> $$
> a(q_1(x_1), \dots, q_n(x_n)) \to q\big(\,u[x_1, \dots, x_n]\,\big),
> $$
>
> where $u$ is an output tree over $M$ with the variables $x_i$ marking where the (already transduced) children are inserted; the device processes the input bottom-up, carrying a state and a partial output at each node, and accepts/outputs at the root when the state is final. It computes a (partial, possibly nondeterministic) relation $\operatorname{Tree}_L \rightharpoonup \operatorname{Tree}_M$.

> [!definition] Definition 19.4: Top-down tree transducer
> A **top-down tree transducer** processes the input from the root, with rules
>
> $$
> q\big(a(x_1, \dots, x_n)\big) \to u\big[\, q_{i,j}(x_{i}) \,\big],
> $$
>
> sending state $q$ at an $a$-node to an output tree $u$ over $M$ whose leaves are recursive calls $q'(x_i)$ on children in new states. Top-down transducers can **copy** subtrees (calling several states on the same child) and so realize transformations bottom-up transducers cannot, and vice versa; the two classes are incomparable in general, and their composition closures define richer hierarchies.

> [!warning] Warning 19.5: Bottom-up and top-down are incomparable
> Bottom-up transducers can **delete** a subtree only after inspecting it (state computed first), enabling test-then-delete; top-down transducers can **copy** a subtree before inspecting it, enabling copy-then-process-differently. Neither inclusion holds: the class of bottom-up tree transformations and the class of top-down tree transformations are incomparable. This contrasts with automata (Section 18), where nondeterministic top-down and bottom-up recognize the *same* languages; for transducers the direction of processing changes the computed function class, because copying and deletion interact with the order of state computation.

### 19.3. Syntactic Passes as Transductions

> [!example] Example 19.6: Standard transformations
> The following syntax transformations are tree transductions, each a fold or finite-state transducer:
>
> 1. **double-negation elimination**: the relabelling-with-restructuring sending $\neg(\neg(t)) \mapsto t'$ (where $t'$ is the transduced $t$), a bottom-up transducer with a state recording "top is a negation";
> 2. **negation normal form**: pushing negations to the leaves via De Morgan laws, a top-down transducer with states "positive/negative polarity" that flips at each negation;
> 3. **parse tree → abstract syntax tree (AST)**: a tree homomorphism deleting punctuation nonterminals and collapsing chain productions, with $C_a$ chosen to drop or restructure;
> 4. **desugaring**: expanding derived constructs into core ones, a tree homomorphism with $C_a$ the core encoding of $a$;
> 5. **erasing annotations**: a relabelling forgetting decoration, shape-preserving (Definition 4.10).

> [!remark] Remark 19.7: Transducers versus rewriting versus attribute grammars
> A transducer computes a transformation in one (or boundedly many) structured passes with finite control; **rewriting** (Section 14) computes by iterating local steps to a normal form, possibly unboundedly many. The two coincide when a normalization is achievable in a single syntax-directed pass (e.g. NNF, double-negation elimination on a linear system), and diverge when normalization requires fixpoint iteration (e.g. full simplification under interacting rules). **Attribute grammars** generalize folds by combining **synthesized** attributes (bottom-up, Section 5.5, Construction 5.9) and **inherited** attributes (top-down, depth-like), computing decorations whose dependencies flow both ways; a transducer's output is a synthesized attribute valued in trees, and an attribute grammar's well-defined evaluation is the simultaneous solution of its bottom-up and top-down decorations. All three are realizations of structural recursion with varying control, and all rest on the well-foundedness of the subtree (and ancestor) orders of Section 5.

---

## 20. Operads and Trees as Composition Patterns

Trees are the free composition patterns for operations with many inputs and one output. The theory that makes this precise is the theory of **operads**, in which an operation is something with $n$ inputs and one output, composition is grafting at inputs, and the free operad on a set of generating operations is built from trees. This section gives the operadic view as a conceptual unifier of grafting, contexts, and substitution, in compact but precise form; it is an adjacent theory, not the primary framework. The governing slogan is: a tree is a recipe for composing operations.

### 20.1. Operations, Grafting, and Operads

> [!definition] Definition 20.1: (Non-symmetric) operad
> A **non-symmetric operad** $\mathcal{O}$ consists of sets $\mathcal{O}(n)$ for $n \in \mathbb{N}$ (the **operations of arity $n$**, with $n$ inputs and one output), an **identity** $\mathrm{id} \in \mathcal{O}(1)$, and **composition** maps
>
> $$
> \gamma : \mathcal{O}(n) \times \mathcal{O}(k_1) \times \cdots \times \mathcal{O}(k_n) \to \mathcal{O}(k_1 + \cdots + k_n),
> $$
>
> $(f; g_1, \dots, g_n) \mapsto f(g_1, \dots, g_n)$, "plug $g_i$ into the $i$-th input of $f$," subject to **associativity** (nested grafting is order-independent) and **unitality** ($\mathrm{id}$ is a two-sided unit). A **symmetric operad** adds an action of the symmetric groups $S_n$ on $\mathcal{O}(n)$ permuting inputs, compatibly with $\gamma$.

> [!definition] Definition 20.2: Partial composition
> Operadic composition is generated by **partial composition** maps
>
> $$
> \circ_i : \mathcal{O}(n) \times \mathcal{O}(m) \to \mathcal{O}(n + m - 1), \qquad f \circ_i g := f(\mathrm{id}, \dots, \mathrm{id}, g, \mathrm{id}, \dots, \mathrm{id}),
> $$
>
> grafting $g$ into the $i$-th input of $f$ and leaving the others as inputs. Partial composition satisfies associativity and commutativity relations ($f \circ_i (g \circ_j h)$ and the interchange of $\circ_i, \circ_j$ at distinct inputs), and the full $\gamma$ is recovered by iterating $\circ_i$.

### 20.2. The Free Operad on Trees

> [!theorem] Theorem 20.3: Trees form the free operad on a signature
> Let $\Omega$ be a signature regarded as a graded set of generating operations ($f \in \Omega_n$ an arity-$n$ generator). The **free non-symmetric operad** on $\Omega$ has $\mathcal{O}(n) = $ the set of trees over $\Omega$ with exactly $n$ ordered **input leaves** (holes), composition $\gamma$ given by **grafting** input leaves to roots, and identity the single input leaf $\Box \in \mathcal{O}(1)$. Symmetrizing (allowing input permutations) gives the free symmetric operad.
>
> [!proof-sketch] Proof Sketch 20.3
> A tree with $n$ ordered input leaves is exactly an $n$-hole **linear context** over $\Omega$ (Section 10.5) with no object variables, i.e. a multilinear $n$-ary polynomial operation (Theorem 10.18). Grafting the root of the $i$-th such tree onto the $i$-th input leaf is operadic composition; associativity and unitality are the context-composition laws (Proposition 10.16, Definition 10.15). Freeness: any map of $\Omega$ into an operad's generators extends uniquely along grafting to a map of operads, by structural recursion on the tree, since grafting is the only composition and the input leaf is the identity — the universal property of the initial-algebra/free construction transported to the operadic grading.

> [!remark] Remark 20.4: Contexts, operads, and substitution unified
> The operadic picture identifies the three calculus notions as one structure graded by input count. **Internal nodes are operations** (the generators $f \in \Omega$), **leaves are input slots** (the holes), and **grafting is composition** ($\circ_i$, partial composition $=$ plugging into one hole). A linear multi-hole context (Section 10) *is* an operadic operation; context composition (Definition 10.15) *is* operadic composition; and substitution (Section 12) is the operad-algebra action — an $\mathcal{O}$-algebra is a set with an action of each operation, and evaluating a tree of operations against argument values is exactly the fold of Section 5. Thus operads are the common abstraction of grafting, contexts, plugging, and substitution; the **colored** (typed) operad of Remark 11.9 is the many-sorted refinement, with colors the sorts and operations the typed contexts.

> [!warning] Warning 20.5: Operads are a unifier, not the primary framework here
> The operadic formulation is included as a conceptual organizer: it explains why grafting, contexts, and substitution obey the same associativity and unit laws (they are one operad's composition) and connects the tree calculus to homotopy theory, universal algebra, and rewriting on operadic terms. It is deliberately **not** taken as the foundational framework of this treatise, which is the address model and its elementary operations, because the operadic abstraction suppresses positions and subtrees — precisely the data the calculus of Sections 9–16 exploits. The slogan "a tree is a recipe for composing operations" is the operadic reading of unique readability (Proposition 4.8): a tree is its own formation history under grafting.

---

## 21. Trees, Logic, and Proof Theory

Trees are the carriers of formal syntax and formal proof. This section surveys the principal logical species of tree — term trees, formula trees, abstract syntax trees, parse trees, proof and derivation trees — distinguishing them by their labels, arities, and correctness conditions, and connecting substitution, contexts, and rewriting to logical operations. The treatment is compact and precise, and respects the boundary (Warning 16.17) at which binding requires capture-aware refinements.

### 21.1. Term Trees, Formula Trees, and ASTs

> [!definition] Definition 21.1: Term tree and formula tree
> A **term tree** over a first-order signature is a tree over $X \sqcup \Omega$ (variables and function symbols), an element of $\operatorname{Tree}_\Omega(X)$ (Definition 8.3); its leaves are variables and constants, its internal nodes function symbols. A **formula tree** adds a layer: a tree whose root region is built from logical connectives and quantifiers (a separate sort of label) over **atomic formula** nodes (relation symbols applied to term trees). Formula trees are **many-sorted** (Definition 4.15) — at least a sort *term* and a sort *formula* — with relation symbols typed $R : \mathit{term} \times \cdots \times \mathit{term} \to \mathit{formula}$ and connectives typed over *formula*.

> [!warning] Warning 21.2: Formula trees carry a sort discipline and binders
> A formula tree is not a single-sorted term tree: it distinguishes the sort *term* (arguments of relations and functions) from the sort *formula* (arguments of connectives), and ill-sorted combinations — a connective applied to a term, a function applied to a formula — are excluded by Proposition 4.17. Quantifiers $\forall x, \exists x$ introduce **binders**, placing formula syntax outside the non-binding calculus: object-level substitution into a formula must be capture-avoiding (Warning 16.17), whereas schema/context filling may legitimately capture. The single-sorted, non-binding theory of Sections 1–16 is the substrate; the formula layer is the typed, binding-aware upgrade.

> [!definition] Definition 21.3: Parse tree versus abstract syntax tree
> A **parse tree** (concrete syntax tree) records a full grammar derivation: its internal nodes are grammar nonterminals, its leaves terminals, and its yield (Definition 7.4) is the parsed string; it retains punctuation, grouping, and chain productions. An **abstract syntax tree** (AST) records only the essential operator/operand structure: internal nodes are operations, leaves are atoms, and inessential concrete-syntax artifacts are discarded. The AST is obtained from the parse tree by a tree transduction (Example 19.6(3)); they are different trees with different labels and correctness conditions, related by a syntax-directed transformation.

### 21.2. Proof Trees and Derivation Trees

> [!definition] Definition 21.4: Derivation/proof tree
> A **proof tree** (synonym in many calculi: **derivation tree**) records how a judgment is derived: each node is an instance of an **inference rule**, its children the derivations of the rule's premises, and its label/conclusion the derived judgment; leaves are axiom instances or open assumptions. Correctness is a **local** condition at every node — the node's conclusion and its children's conclusions must instantiate a rule of the calculus, with the rule's side-conditions satisfied — and the global object is well-formed iff every node is locally correct.

> [!warning] Warning 21.5: Formula trees and proof trees are different trees
> A formula tree records **how a formula is built** from connectives and atoms; its labels are logical and term symbols, its arities the connectives' arities, its correctness the sort discipline. A proof tree records **how a judgment is derived**; its labels are inference rules, its arities the rules' premise counts, its correctness the local rule-instance condition (including substitution and freshness side-conditions). They are distinct species: a proof tree's nodes are *labelled by* (or *carry*) formulas/judgments, but the tree structure is the proof's, not the formula's. Conflating them — treating a proof as if it were a big formula — loses the inference-rule labelling and the local correctness conditions that make it a proof.

> [!remark] Remark 21.6: Substitution, contexts, and rewriting in proof theory
> The tree calculus instruments proof theory directly. **Substitution** realizes the term-instantiation in $\forall$-elimination and rule instances (capture-avoiding in the binding layer). **Contexts** isolate a subderivation or a subformula for local manipulation: a derivation context is a proof tree with a hole admitting a subderivation of a fixed judgment, and plugging composes proofs. **Rewriting** models proof transformation: **normalization** in natural deduction (eliminating detours, i.e. introduction immediately followed by elimination) and **cut elimination** in the sequent calculus are rewrite systems on proof trees, whose termination (strong normalization) and confluence are the proof-theoretic analogues of Section 15, and whose normal forms are the cut-free/normal proofs. $\beta$-reduction on lambda terms is the Curry–Howard image of natural-deduction normalization, a rewriting process (Section 14) on the term trees corresponding to proofs. Thus the spine trees → contexts → substitution → matching → rewriting → normal forms reappears, at the level of proofs, as derivations → derivation contexts → instantiation → rule matching → proof transformation → normal proofs.

---

## 22. Infinite and Coinductive Trees

The finite trees of the core are the **initial algebra** of the branching functor $F_L$ (Theorem 2.11), built bottom-up and supporting induction and recursion. Dropping finiteness yields **infinite trees**, the **final coalgebra** of the same functor, observed top-down and supporting coinduction and corecursion. This section gives the coinductive picture compactly and precisely, marks where the finite-case machinery (well-founded induction, structural recursion, well-foundedness of $\vartriangleleft$) fails, and connects infinite trees to streams, regular trees, cyclic term graphs, and the prefix metric. It is an optional adjacent development, deliberately not central.

### 22.1. Infinite Trees as a Final Coalgebra

> [!definition] Definition 22.1: Infinite labelled tree
> An **infinite (finitely branching) tree** over $(L, \rho)$ is a function $t : D \to L$ on a possibly **infinite** tree domain $D \subseteq \mathbb{A}$ (prefix-closed, left-sibling-closed, arity-correct: $k_D(p) = \rho(\ell(p))$ at every node), with no finiteness requirement on $D$. The set of all such (finite and infinite) trees is $T_L^\infty$. Arity-correctness with finite ranks forces finite branching, but branches may be infinite.

> [!theorem] Theorem 22.2: Infinite trees as the final $F_L$-coalgebra
> An **$F_L$-coalgebra** is a set $Z$ with a map $\zeta : Z \to F_L(Z)$ ("observe the root label and the children-seeds"). The set $T_L^\infty$, with the observation map $t \mapsto (\ell(\varepsilon), t|_1, \dots, t|_{\rho(\ell(\varepsilon))})$, is the **final** $F_L$-coalgebra: for every coalgebra $(Z, \zeta)$ there is a **unique** coalgebra homomorphism $\operatorname{unfold}_\zeta : Z \to T_L^\infty$. Equivalently $T_L^\infty$ is the greatest fixed point $\nu F_L$, with the observation map an isomorphism $T_L^\infty \xrightarrow{\cong} F_L(T_L^\infty)$.
>
> [!proof-sketch] Proof Sketch 22.2
> The observation map is a bijection because every (finite or infinite) tree is uniquely its root label together with its immediate subtrees, and conversely any such data assemble a tree (no well-foundedness needed). Finality: $\operatorname{unfold}_\zeta(z)$ is defined **corecursively** — its root label and children-seeds are read from $\zeta(z)$, and the children are $\operatorname{unfold}_\zeta$ of those seeds — producing a possibly infinite tree; it is the unique coalgebra map because any such map must commute with observation, which determines it level by level (uniqueness by coinduction, the dual of the initial-algebra uniqueness).

### 22.2. Corecursion, Coinduction, and the Failure of the Finite Machinery

> [!warning] Warning 22.3: Induction and structural recursion fail for infinite trees
> The finite-case engine breaks down: the proper-subtree relation $\vartriangleleft$ is **not well-founded** on $T_L^\infty$ (an infinite branch descends forever), so structural induction (Theorem 5.5) and structural recursion (Theorem 5.7) are unavailable, and the size measure $|t|$ is infinite. The replacements are **dual**: properties are proved by **coinduction** (a property holds of all infinite trees if it is closed under observation — a bisimulation argument), and functions *into* infinite trees are defined by **corecursion** (specify the root and the seeds of the children, guarded so each step makes progress). Folds *out of* infinite trees exist only when the target carries enough structure to take limits (e.g. a complete metric or a cpo); arbitrary folds do not.

> [!definition] Definition 22.4: Bisimulation and coinductive equality
> A **bisimulation** on $T_L^\infty$ is a relation $\mathrel{R}$ such that $t \mathrel{R} t'$ implies $\ell_t(\varepsilon) = \ell_{t'}(\varepsilon)$ and $t|_i \mathrel{R} t'|_i$ for all $i$. Two infinite trees are **bisimilar** iff related by some bisimulation; bisimilarity is the largest bisimulation. **Coinductive equality** of infinite trees is bisimilarity, and by finality it coincides with literal equality $t = t'$ (same domain, same labels): for the final coalgebra, bisimilar elements are equal.
>
> [!proof-sketch] Proof Sketch 22.4
> A bisimulation relating $t, t'$ forces, by induction on depth $|p|$, that $\ell_t(p) = \ell_{t'}(p)$ and that the domains agree to depth $|p|$ (the root condition gives depth $0$, the children condition advances the depth); hence $D_t = D_{t'}$ and $\ell_t = \ell_{t'}$, i.e. $t = t'$. This is the coinduction proof principle: to prove two infinite trees equal, exhibit a bisimulation relating them.

### 22.3. Regular Trees, Streams, and Finite Presentations

> [!definition] Definition 22.5: Regular infinite tree
> An infinite tree is **regular** if it has only **finitely many distinct subtrees** $\{t|_p : p \in D\}$. Regular trees are exactly the trees **unfolded from finite cyclic term graphs** (Definition 17.7): the graph's nodes are the distinct subtrees, and a back-edge realizes a subtree equal to an ancestor's subtree. Equivalently, regular trees are the corecursive solutions of finite guarded systems of equations $Z_i = a_i(Z_{i_1}, \dots, Z_{i_{n_i}})$.

> [!example] Example 22.6: Streams as unary infinite trees
> Over a ranked alphabet whose labels all have rank $1$ except a final coalgebraic structure, an infinite **stream** $(a_0, a_1, a_2, \dots)$ is a unary infinite tree: a single infinite branch with the $k$-th node labelled $a_k$. Streams are the final coalgebra of $Z \mapsto A \times Z$ (head and tail), the unary instance of $F_L$. A stream is **regular** iff it is eventually periodic, presented by a finite cyclic graph (a lasso). Corecursion defines streams (e.g. the stream of natural numbers by $\mathit{nats} = 0 : \operatorname{map}(+1)\, \mathit{nats}$), and bisimulation proves stream equalities.

> [!definition] Definition 22.7: Prefix metric on infinite trees
> The **prefix metric** on $T_L^\infty$ is $d(t, t') := 2^{-k}$ where $k$ is the least depth at which $t$ and $t'$ disagree (in domain or label), and $d(t,t) = 0$. It is an ultrametric, $T_L^\infty$ is complete under it, and the finite trees (or finite-depth truncations) are dense. Corecursive definitions are **contractive** maps and have unique fixed points by Banach's theorem, giving an alternative, metric account of corecursion: an infinite tree is the limit of its finite truncations, and a guarded corecursive specification is a contraction whose fixed point is the defined tree.

> [!remark] Remark 22.8: Why infinite trees are kept peripheral
> Infinite and coinductive trees are a genuine and useful theory — modeling streams, recursive types, non-terminating computations, behaviors of reactive systems, and the semantics of cyclic term graphs — but they invert the core methodology: top-down observation and coinduction replace bottom-up construction and induction, well-foundedness is lost, and the central calculus operations (position-indexed replacement, context extraction at arbitrary positions, finite matching) require care or finiteness assumptions to remain effective. The finite trees of Sections 1–16 remain the primary object precisely because they are the initial algebra on which the full calculus is unconditional; infinite trees are the dual final-coalgebra companion, included to complete the structural picture (initial/final, induction/coinduction, recursion/corecursion) without displacing the finite core.

---

## 23. Algorithms and Computation on Trees

The tree calculus is implementable, and its operations have characteristic costs and data-structure tradeoffs. This section records, compactly and with mathematical precision, the principal algorithms — traversals, measure computation, position finding, matching, substitution, redex search, normalization — together with the representations that support them and the complexity parameters that govern them. It is implementation-aware mathematics, not programming exposition, and every algorithm is tied to a construction of the core.

### 23.1. Representations

> [!definition] Definition 23.1: Concrete representations of trees
> A finite tree admits several encodings, each exposing different operations:
>
> 1. **nested tuples** $(a, t_1, \dots, t_n)$ — direct image of the recursive presentation (Section 2.5), good for pattern matching and recursion;
> 2. **address maps** $\ell : D \to L$ — the model of this treatise, good for positions, subtrees, replacement, contexts;
> 3. **node records with child pointers** — good for traversal and in-place mutation;
> 4. **parent-pointer trees** — good for upward navigation and path-to-root updates;
> 5. **zippers** (Definition 23.6) — good for focused local editing;
> 6. **hash-consed DAGs** (Section 17) — good for sharing, memoization, and structural equality in $O(1)$ per node.
>
> The representations are inter-convertible in linear time and realize the same abstract tree (Proposition 9.15); choice is governed by which operations dominate.

### 23.2. Traversals and Basic Measures

> [!definition] Definition 23.2: Traversal orders
> A **traversal** is an order of visiting nodes. **Preorder** visits a node before its children ($\operatorname{pre}(a(t_1,\dots,t_n)) = a \cdot \operatorname{pre}(t_1) \cdots \operatorname{pre}(t_n)$), the basis of prefix notation, parseable without parentheses by slot-counting on ranks. **Postorder** visits children before the node, the basis of postfix/stack evaluation. **Inorder** (binary trees) visits left child, node, right child, the basis of infix notation (needing parentheses or precedence to disambiguate). **Breadth-first** (level order) visits by increasing depth, using a queue. Depth-first traversals use stack depth $O(\operatorname{ht}(t))$; breadth-first uses queue size $O(\operatorname{width}(t))$.

> [!proposition] Proposition 23.3: Linear-time measures and the slot-counting parser
> Size, height, leaf count, label-occurrence counts, support, and any fold (Theorem 5.7) with $O(1)$ per-node combine cost are computable in $O(|t|)$ time and $O(\operatorname{ht}(t))$ auxiliary stack space by a single postorder pass (Construction 5.9). A prefix word $s = (a_0, \dots, a_{m-1})$ of ranked labels decodes to a unique tree iff the **slot count** $q_s(j) = 1 + \sum_{i < j}(\rho(a_i) - 1)$ stays positive for $j < m$ and reaches $0$ at $j = m$; the parse is computable in $O(m)$.
>
> [!proof-sketch] Proof Sketch 23.3
> Each measure is a fold; a postorder pass computes the decoration $\alpha_H^t$ bottom-up (Construction 5.9), one $O(1)$ combine per node, total $O(|t|)$, with recursion/stack depth $O(\operatorname{ht}(t))$. The slot-count criterion holds because reading a rank-$n$ label consumes one open slot and opens $n$, net $n - 1$; a complete tree consumes the initial single slot exactly at the end, and positivity throughout forbids premature completion — this is the unique-readability condition (Proposition 4.8) for the prefix encoding.

### 23.3. Matching, Substitution, Redex Search, Normalization

> [!proposition] Proposition 23.4: Costs of the calculus operations
> For finite trees and a finite TRS over a finite signature:
>
> 1. **subtree extraction** $t|_p$ and **replacement** $t[p:=s]$ touch only the path to $p$ and the inserted subtree, $O(|p| + |s|)$ with structural sharing of the untouched parts (persistent update);
> 2. **syntactic matching** of pattern $\ell$ against $u$ (Construction 13.6) runs in $O(\min(|\ell|, |u|))$ for linear $\ell$, with an added equality-check cost for nonlinear $\ell$ (amortized $O(1)$ per repeated-variable check using hash-consing);
> 3. **substitution** $\widehat\sigma(t)$ runs in $O(|t| + \sum_x \#_x(t)\cdot|\sigma(x)|)$, the output size, and shares unsubstituted parts;
> 4. **redex search** enumerates the $\le |D_t|\cdot|R|$ position–rule pairs (Proposition 14.8), each tested by matching; root-label and arity **indexing** (discrimination trees) prunes most pairs in practice;
> 5. **normalization** iterates rewrite steps under a strategy until a normal form is reached; for a convergent system the number of steps is bounded by the reduction order's descent (Theorem 15.5) and the result is the unique $\operatorname{nf}_R(t)$ (Theorem 16.13).
>
> [!proof-sketch] Proof Sketch 23.4
> (1) Replacement rebuilds only the ancestors of $p$ (path-copying), reusing the disjoint subtrees by Proposition 9.10; persistent data structures realize this in $O(|p|+|s|)$. (2) Matching descends $\ell$ and $u$ in lockstep, halting at the first mismatch; uniqueness (Proposition 13.7) means no backtracking for syntactic matching. (3) Substitution is a fold producing the output, whose size bounds the cost. (4) Each position–rule pair admits one match attempt; indexing skips pairs whose root labels cannot match. (5) Termination bounds step count; confluence makes the result strategy-independent.

> [!warning] Warning 23.5: Complexity warnings
> Several operations hide costs. Naive **redex search** is $O(|t|\cdot|R|\cdot \text{pattern size})$ without indexing; large rule sets demand discrimination trees or substitution tries. **Substitution** can blow up output size when a variable with many occurrences is mapped to a large tree (size $\sum_x \#_x(t)\cdot|\sigma(x)|$), and repeated substitution can cause exponential growth without sharing — the standard motivation for DAG representation (Section 17). **Nonlinear matching** and **equational (AC) matching** are more expensive (the latter NP-hard in general, Section 13.6). **Normalization** may take a number of steps not polynomially bounded in $|t|$ even for terminating systems (the reduction order may descend through long chains). These are the points at which sharing, indexing, and memoization (Section 23.5) become necessary rather than optional.

### 23.4. Zippers and Focused Editing

> [!definition] Definition 23.6: Zipper
> A **zipper** on a tree $t$ at a focus position $p$ is the pair $(C, s)$ with $C = t[p := \Box]$ (the context) and $s = t|_p$ (the focused subtree), stored as a focused subtree together with a stack of **frames**, each frame recording a parent label, the focused child index, and the left and right sibling subtrees. Navigation is local: **down** pushes a frame (focus a child), **up** pops a frame and rebuilds one parent node, **left/right** shift the focus among siblings, and **replace** swaps $s$ for a new subtree, all in $O(1)$ or $O(\text{out-degree})$ per move, with whole-tree reconstruction $t = C[s]$ available on demand (Theorem 7.6).

> [!remark] Remark 23.7: Zippers realize context–subtree decomposition operationally
> A zipper is the data-structure incarnation of the master decomposition $t = C[\,t|_p\,]$ (Theorem 7.6, Remark 7.7): it stores exactly the context and focused subtree, so local edits at the focus rebuild only the path to the root (the frame stack), and the position need not be re-searched. This makes zippers the natural substrate for interactive proof editing, AST transformation, incremental parsing, and redex-by-redex rewriting, where the same locus is edited repeatedly. Parent pointers and zippers both expose the root-path along which incremental updates (Section 23.5) propagate.

### 23.5. Sharing, Hashing, and Incremental Computation

> [!definition] Definition 23.8: Structural hashing and Merkle decoration
> A **structural hash** is the fold $\operatorname{hash}(a(t_1,\dots,t_n)) = H(a, \operatorname{hash}(t_1), \dots, \operatorname{hash}(t_n))$ into a hash domain, with $H$ collision-resistant. Decorating every node with the hash of its subtree (Construction 5.9) yields a **Merkle tree**: a leaf change alters exactly the hashes on the path to the root, and equal subtrees have equal hashes, enabling $O(1)$ structural-equality tests and hash-consing (Definition 17.4).

> [!remark] Remark 23.9: Memoization, incrementality, and worklists
> Structural hashing supports three efficiency techniques tied to the calculus. **Memoized folds**: compute a fold once per distinct subtree (keyed by hash/DAG node), turning $O(|t|)$ into $O(\text{distinct subtrees})$ when sharing is high (Remark 17.8). **Incremental annotation**: after a replacement at $p$, recompute decorations only along the root-path from $p$ (Construction 5.9 is local in the ancestors), the path exposed by a zipper or parent pointers. **Worklist/frontier algorithms**: BFS uses a queue (width-bounded), bottom-up annotation propagates from leaves, redex saturation queues newly created redexes, and proof search expands open leaves — all instances of frontier-sensitive recursion where the active set is a frontier rather than the whole tree. These connect the static structure theory (folds, decorations, the subtree order) to the dynamics of efficient computation, closing the loop from definitions to implementation.

---

## 24. Further Laws of Contexts and Substitution

The rewriting development of Sections 14–16 invoked several interaction laws between substitution, contexts, and positions. This section collects and proves them as a self-contained body of structural results, deepening the calculus core. These are the lemmas that make the closure properties of $\to_R$, the substitution clause of congruence generation, and the critical-pair analysis go through; they are stated here once and for all, with explicit hypotheses.

### 24.1. The Substitution Lemma

> [!lemma] Lemma 24.1: Substitution lemma
> Let $x, y$ be distinct object variables, $s$ a tree not containing $y$ free as a substitutable variable in the relevant clause, and $u, v$ trees. Then for the single-variable substitutions of Definition 12.7,
>
> $$
> t[x := u][y := v] \;=\; t[y := v]\big[x := u[y := v]\big] \qquad\text{whenever } y \notin \operatorname{Var}(u) \text{ or the orders are reconciled,}
> $$
>
> and in the fully simultaneous form, with $x \neq y$ and $x \notin \operatorname{Var}(v)$,
>
> $$
> t[x := u][y := v] = t[\,x := u[y:=v],\ y := v\,].
> $$
>
> In the non-binding tree setting all variables are free and uniformly substitutable, so no capture side-condition beyond $x \neq y$ is needed; the only subtlety is whether $v$ is substituted into the copies of $u$ introduced by $x$.
>
> [!proof-sketch] Proof Sketch 24.1
> By structural induction on $t$, using the monad composition law (Theorem 12.5). At a variable leaf: if the leaf is $x$, the left side gives $u[y:=v]$ and the right side gives $u[y:=v]$ directly; if the leaf is $y$, both sides give $v$; otherwise both give the leaf. At a constructor node both sides push the substitutions inside by the constructor clauses and match by the induction hypothesis. The composition law $\widehat{\tau}\circ\widehat{\sigma} = \widehat{\tau\star\sigma}$ is the abstract statement of which this is the explicit two-variable instance.

> [!warning] Warning 24.2: The substitution lemma is delicate under binding
> In the non-binding calculus Lemma 24.1 holds with only $x \neq y$ and the placement of $v$ into $u$'s copies as its content. Under binders the lemma acquires the genuine freshness side-condition $x \notin \operatorname{FV}(v)$ **and** capture-avoidance, and is one of the standard sources of error in formalized binding syntax. It is recorded here in its clean non-binding form to mark exactly what the binding upgrade must repair (Warning 16.17).

### 24.2. Contexts, Positions, and Substitution

> [!lemma] Lemma 24.3: Position translation under plugging
> Let $C$ be a one-hole context with hole address $h$ and $s$ a tree. The positions of $C[s]$ are
>
> $$
> D_{C[s]} = (D_C \setminus \{h\}) \cup \{\, h \cdot r : r \in D_s \,\},
> $$
>
> and subtree extraction translates as: for $q \in D_C$ with $q \neq h$ and $h \npreceq q$, $(C[s])|_q = C|_q$ with the hole (if below $q$) still present; for $q = h \cdot r$ with $r \in D_s$, $(C[s])|_{h\cdot r} = s|_r$; and $(C[s])|_h = s$.
>
> [!proof-sketch] Proof Sketch 24.3
> Direct from the plugging formula (Definition 10.5): off the hole the addresses and labels are those of $C$, and at and below $h$ they are those of $s$ readdressed by $h\cdot(-)$. Extraction reads the subtree at each address from this description, splitting on whether the address lies above, at, or below the hole.

> [!lemma] Lemma 24.4: Substitution–plugging distribution (general form)
> For a substitution $\sigma$ fixing the hole symbols, a one-hole context $C$, and a tree $s$,
>
> $$
> \widehat\sigma(C[s]) = \widehat\sigma(C)[\widehat\sigma(s)],
> $$
>
> and for a $k$-hole context $C$ with fillers $s_0, \dots, s_{k-1}$,
>
> $$
> \widehat\sigma\big(C[s_0, \dots, s_{k-1}]\big) = \widehat\sigma(C)\big[\widehat\sigma(s_0), \dots, \widehat\sigma(s_{k-1})\big].
> $$
>
> [!proof-sketch] Proof Sketch 24.4
> The one-hole case is Proposition 12.11. The multi-hole case is the same structural induction on $C$, with each hole $\Box_i$ contributing $\widehat\sigma(s_i)$ at the base and constructor nodes pushing $\widehat\sigma$ inside; equivalently it is the homomorphism property of $\widehat\sigma$ applied to the polynomial operation induced by $C$ (Theorem 10.18), since $\widehat\sigma$ is an $\Omega$-algebra homomorphism and commutes with polynomial operations.

> [!lemma] Lemma 24.5: Parallel moves at disjoint positions
> Let $p \mathbin\| q$ be disjoint positions of $t$, and suppose $t|_p \to_R u$ and $t|_q \to_R v$ are single rewrite steps. Then the contractions commute and may be done in parallel:
>
> $$
> t[p := u][q := v] = t[q := v][p := u] = t[p := u,\ q := v],
> $$
>
> and both equal the result of one parallel-rewrite step contracting the two disjoint redexes simultaneously.
>
> [!proof-sketch] Proof Sketch 24.5
> Disjointness gives commutation of the underlying replacements (Proposition 9.10); since rewriting is replacement at a matched position (Definition 14.7) and the matches at $p$ and $q$ are unaffected by a change at the other disjoint site (extraction is local, Proposition 9.4), the two steps commute and combine into the simultaneous replacement, which is the parallel step. This is the "disjoint peak" case of the critical-pair analysis (Proof Sketch 15.13) and the soundness of parallel-innermost/outermost strategies (Definition 14.14).

### 24.3. The Context Clone in Detail

> [!definition] Definition 24.6: The clone of context operations
> The family $\operatorname{Clone}_L := (\operatorname{Ctx}^k_L)_{k \ge 0}$ of multi-hole contexts over $L$, with the **projections** $\pi^k_i := \Box_i \in \operatorname{Ctx}^k_L$ (the $k$-hole context that is just the $i$-th hole) and **superposition** given by context composition (Definition 10.15), is a **clone**: it contains all projections and is closed under superposition, with the clone identities
>
> $$
> C[\pi^k_0, \dots, \pi^k_{k-1}] = C, \qquad \pi^k_i[D_0, \dots, D_{k-1}] = D_i, \qquad (\text{associativity of nested superposition}).
> $$

> [!proposition] Proposition 24.7: The context clone is the clone of polynomial operations of $\mathbf{T}_\Omega(X)$
> The induced-operation map (Theorem 10.18) is a clone isomorphism from $\operatorname{Clone}_L$ (linear contexts, with repeated/omitted holes allowing the non-multilinear and degenerate operations) onto the clone of polynomial operations of the tree algebra $\mathbf{T}_\Omega(X)$. Under it, projections correspond to argument projections, superposition to operation composition, and the basic contexts $f(\Box_0, \dots, \Box_{n-1})$ to the constructors $f^{\mathbf{T}}$.
>
> [!proof-sketch] Proof Sketch 24.7
> Theorem 10.18 establishes the bijection on operations of each arity; the clone identities of Definition 24.6 transport to the clone identities of polynomial operations because context composition transports to operation composition (Proposition 10.16, Definition 10.15) and the projections transport to argument projections. The basic contexts generate the clone (every context is built from holes and constructors), matching the generation of the polynomial clone by the basic operations.

> [!remark] Remark 24.8: Why the clone view matters for congruences
> The reformulation "a congruence is an equivalence closed under all one-hole contexts" (Proposition 16.3) is exactly "closed under all unary polynomial operations," and the closure of $\to_R$ under contexts (Proposition 14.10) is closure under the action of the context clone. The clone is therefore the algebraic object that organizes both the congruence closure of Section 16 and the contextual closure of Section 14: stability under the context clone is the common condition, symmetric for congruences and directed for rewriting. The typed/colored clone (Remark 11.9) plays the same role in the typed theory.

---

## 25. Abstract Reduction Systems and Modularity

The metatheory of Section 15 — normalization, confluence, Newman's lemma — is, at its core, about a binary relation, not specifically about trees. This section isolates the **abstract** layer: an abstract reduction system is a set with a binary relation, and the termination/confluence theory is developed there in full generality, then specialized back to tree rewriting. This both clarifies which results are structural and which are tree-specific, and supplies the commutation and modularity tools the tree theory uses.

### 25.1. Abstract Reduction Systems

> [!definition] Definition 25.1: Abstract reduction system
> An **abstract reduction system** (ARS) is a pair $(A, \to)$ with $A$ a set and $\to\, \subseteq A \times A$ a binary relation. The derived relations are: $\to^*$ (reflexive-transitive closure), $\to^=$ (reflexive closure), $\to^+$ (transitive closure), $\leftrightarrow$ (symmetric closure $\to \cup \to^{-1}$), and $\leftrightarrow^*$ (conversion, an equivalence). An element $a$ is a **normal form** if it has no $\to$-successor; $a$ **has** normal form $b$ if $a \to^* b$ and $b$ is a normal form. The tree case is $(A, \to) = (\operatorname{Tree}_\Omega(X), \to_R)$.

> [!definition] Definition 25.2: Termination and confluence properties (abstract)
> An ARS is **terminating** (SN) if $\to$ has no infinite chain; **normalizing** (WN) if every element has a normal form; **confluent** (CR) if $b \,{}^*\!\!\leftarrow a \to^* c$ implies $b \downarrow c$ (a common reduct exists); **locally confluent** (WCR) if $b \leftarrow a \to c$ implies $b \downarrow c$; and has **unique normal forms** (UN) if no element has two distinct normal forms. The diamond property holds if $b \leftarrow a \to c$ implies $b \to d \leftarrow c$ for some $d$ (one-step reconvergence).

> [!theorem] Theorem 25.3: Newman's lemma (abstract)
> A terminating ARS is confluent iff it is locally confluent.
>
> [!proof-sketch] Proof Sketch 25.3
> Noetherian induction on $\to$ (available by termination): for $a$ with $a \to^* b$, $a \to^* c$, reduce trivial cases, then factor through first steps $a \to b_1 \to^* b$, $a \to c_1 \to^* c$; local confluence joins $b_1, c_1$ at $d$; the induction hypothesis at the smaller $b_1$ joins $b$ and $d$, at $c_1$ joins $d$ and $c$, and transitivity assembles a common reduct of $b$ and $c$. This is the relation-only content of Theorem 15.11; nothing tree-specific is used.

> [!proposition] Proposition 25.4: Diamond implies confluence; SN + WCR implies UN
> If $\to$ has the diamond property then $\to$ is confluent (the diamond tiles to fill any $b\,{}^*\!\!\leftarrow a \to^* c$). If an ARS is terminating and locally confluent, it is confluent (Newman) and hence has unique normal forms; the pair "terminating + confluent" is **convergent** and yields a total normal-form function $\operatorname{nf}$ deciding $\leftrightarrow^*$.
>
> [!proof-sketch] Proof Sketch 25.4
> Diamond $\Rightarrow$ CR: induct on the lengths of the two reductions, tiling one diamond per pair of opposing steps; the one-step reconvergence keeps the fronts a constant distance apart and they meet. SN + WCR $\Rightarrow$ CR is Newman; CR $\Rightarrow$ UN is Corollary 15.9 abstractly; SN supplies existence of normal forms, so $\operatorname{nf}$ is total and $a \leftrightarrow^* b \iff \operatorname{nf}(a) = \operatorname{nf}(b)$.

### 25.2. Commutation and Modularity

> [!definition] Definition 25.5: Commutation of two relations
> Two relations $\to_1, \to_2$ on $A$ **commute** if $b \,{}^*_1\!\!\leftarrow a \to_2^* c$ implies there is $d$ with $b \to_2^* d \,{}^*_1\!\!\leftarrow c$. A relation is confluent iff it commutes with itself.

> [!theorem] Theorem 25.6: Hindley–Rosen lemma
> If $\to_1$ and $\to_2$ are each confluent and they commute, then their union $\to_1 \cup \to_2$ is confluent.
>
> [!proof-sketch] Proof Sketch 25.6
> A reduction in the union is a sequence of $\to_1$- and $\to_2$-segments. Use confluence of each relation to merge same-colored segments and commutation to swap adjacent opposite-colored fronts past each other; a tiling argument by induction on the number of segments assembles a common reduct. The lemma is the modular tool for proving confluence of a combined system from confluence of its parts plus commutation.

> [!remark] Remark 25.7: Modularity of termination and confluence for tree rewriting
> Combining tree rewriting systems raises **modularity** questions: if $R_1$ and $R_2$ are each terminating (or confluent), is $R_1 \cup R_2$? The answers are subtle and partly negative — termination is **not** modular in general for the disjoint union of TRSs (Toyama's counterexample), while **confluence is modular** for disjoint unions (a consequence of the Hindley–Rosen lemma together with absence of cross-overlaps, since disjoint signatures share no critical pairs). Confluence is also modular under suitable layering and orthogonality. The Hindley–Rosen lemma (Theorem 25.6) is the abstract engine of the positive results: when two rule sets commute and are individually confluent, their combination is confluent, even when termination is lost. These results are why the abstract layer is worth isolating: they are statements about relations and their commutation, instantiated at $\to_{R_1}, \to_{R_2}$.

> [!warning] Warning 25.8: Local confluence is not modular and not sufficient alone
> Two cautions transfer from the abstract layer. First, local confluence alone never implies confluence without termination (Warning 15.10); the abstract counterexample is a relation with $a \to b$, $a \to c$, $b \to a$, $c \to a$ but $b, c$ leading to distinct normal forms via non-terminating detours. Second, termination is not preserved by union even when each part terminates, so a convergent combination requires re-verifying termination of the union (e.g. by a single reduction order compatible with all rules) — confluence modularity does not rescue termination. The safe recipe for a convergent union is: find one reduction order compatible with $R_1 \cup R_2$ (Theorem 15.5), then check all critical pairs, including the **cross** critical pairs between $R_1$ and $R_2$ (Corollary 15.14).

---

## 26. Trees across Mathematics: A Synthesis of Presentations

The same tree object appears, with different emphases and different extra structure, in graph theory, order theory, universal algebra, automata theory, operad theory, and coalgebra. This section consolidates the correspondences developed throughout, stating for each viewpoint what is primitive, what the morphisms are, and which calculus operations it exposes or suppresses. It is the conceptual map of the treatise.

### 26.1. The Six Viewpoints

> [!remark] Remark 26.1: One object, six structures
> The finite ordered labelled tree is realized as:
>
> 1. **graph-theoretic** (Section 2.1): a connected acyclic graph with a root; primitive data are vertices and edges; morphisms are root/parent-preserving graph maps; exposes connectivity and the edge metric $d_t$ (Definition 6.5); **suppresses** sibling order.
> 2. **order-theoretic** (Sections 2.3, 5): a poset with least element and chain down-sets; primitive data are the ancestor order; morphisms are order maps preserving root and covers; exposes ancestry, well-foundedness, and the induction/recursion principles (Theorems 5.5, 5.7); needs an added sibling order for positions.
> 3. **address-theoretic** (Sections 2.4, 4): a prefix-closed sibling-closed set of addresses with a labelling; primitive data are positions and labels; morphisms are shape/label-respecting maps; exposes positions, subtrees, replacement, contexts, plugging, matching, rewriting — the full calculus — and is adopted as primary for that reason.
> 4. **algebraic** (Sections 2.6, 8): the initial $F_L$-algebra / absolutely free $\Omega$-algebra; primitive data are constructors and generators; morphisms are $\Omega$-homomorphisms; exposes the universal property, structural recursion as the unique homomorphism, freeness, substitution as homomorphic extension, and quotients (Section 16).
> 5. **automata/language-theoretic** (Section 18): an element recognized by a finite tree automaton; primitive data are states and transitions; morphisms are simulations; exposes regular tree languages, decidable syntactic predicates, and folds with finite carrier.
> 6. **operadic/coalgebraic** (Sections 20, 22): a free-operad composite (finite) or a final-coalgebra observation (infinite); primitive data are operations and grafting, or observations; exposes composition patterns and, dually, infinite trees, corecursion, and coinduction.

> [!proposition] Proposition 26.2: The correspondences are canonical on finite ordered trees
> On finite ordered labelled trees the six presentations are connected by canonical, structure-preserving bijections: the graph–order correspondence (rooting induces ancestry, Proposition 5.2), the order–address correspondence (Proposition 2.7), the address–algebra correspondence (Theorem 2.11, Proposition 4.8), the algebra–operad correspondence (Theorem 20.3), and the finite-case identification of recognizable predicates with finite-carrier folds (Remark 18.8). Data invariant under these bijections (shape, labels, subtrees, the calculus operations) transfer; presentation-specific data (specific addresses, string lengths, state names) do not.
>
> [!proof-sketch] Proof Sketch 26.2
> Each pairwise correspondence is one of the cited results; composing them gives a coherent system of canonical isomorphisms because each is generator/constructor-preserving and the free object's rigidity (Corollary 8.10) forces all routes between two presentations to agree. Non-transfer of presentation-specific data is the content of Warnings 2.3, 1.15, and 17.5.

### 26.2. What Each Viewpoint Is For

> [!remark] Remark 26.3: Choosing a viewpoint
> The viewpoints are tools, selected by the question. A question about **distance or connectivity** belongs to the graph view; about **induction, recursion, or well-foundedness** to the order view; about **positions, subtrees, replacement, contexts, or rewriting** to the address view; about **universal properties, freeness, evaluation, or quotients** to the algebraic view; about **decidable syntactic classes or recognition** to the automata view; about **composition of operations or infinite/recursive structure** to the operadic/coalgebraic view. The treatise's core calculus lives in the address and algebraic views simultaneously — the address model supplies the operations, the algebraic model supplies the universal property that makes the operations canonical — and the surveys map the calculus into the remaining views. The unity is that all six describe one object, and the calculus is the same calculus however it is presented (Proposition 9.15).

---

## 27. A Fully Worked Development

To consolidate the spine, this section runs a single ranked alphabet through the entire calculus — addresses, subtree, replacement, context extraction, plugging, composition, substitution, matching, a rewrite step, a critical pair, a normal form, and a quotient class — with every datum explicit. The example is small enough to compute by hand and rich enough to exhibit each operation and each distinction.

### 27.1. The Running Signature

> [!example] Example 27.1: The signature and a sample tree
> Fix the ranked alphabet $L = \{ \wedge^{(2)}, \vee^{(2)}, \neg^{(1)}, \top^{(0)}, \bot^{(0)} \} \sqcup X$ with object variables $X = \{x, y, z\}$ of rank $0$ (so $L = X \sqcup \Omega$ with $\Omega$ the Boolean signature). Consider the tree
>
> $$
> t \;=\; \wedge\big(\, \neg(\neg(x)),\ \vee(y, \bot) \,\big),
> $$
>
> with domain and labels
>
> $$
> D_t = \{\varepsilon,\ 1,\ 11,\ 111,\ 2,\ 21,\ 22\}, \quad \ell_t : \varepsilon \mapsto \wedge,\ 1 \mapsto \neg,\ 11 \mapsto \neg,\ 111 \mapsto x,\ 2 \mapsto \vee,\ 21 \mapsto y,\ 22 \mapsto \bot.
> $$
>
> Measures: $|t| = 7$, $\operatorname{ht}(t) = 3$ (deepest node $111$), $\operatorname{leaf}(t) = 3$ (frontier $\{111, 21, 22\}$), $\operatorname{Var}(t) = \{x, y\}$, $\operatorname{supp}(t) = \{\wedge, \neg, \vee, x, y, \bot\}$. The handshake identity (Proposition 3.14) checks: $\sum_p k_{D_t}(p) = 2 + 1 + 1 + 0 + 2 + 0 + 0 = 6 = |t| - 1$. ✓

### 27.2. Extraction, Replacement, Context

> [!example] Example 27.2: Subtree, replacement, and context at position $1$
> Extraction at $p = 1$: $t|_1 = \neg(\neg(x))$, with $D_{t|_1} = \{\varepsilon, 1, 11\}$ readdressed (the old $1, 11, 111$ become $\varepsilon, 1, 11$). Replacement at $1$ by $s = \top$: $t[1 := \top] = \wedge(\top, \vee(y, \bot))$, domain $\{\varepsilon, 1, 2, 21, 22\}$, size $5$. Context extraction at $1$: $C := t[1 := \Box] = \wedge(\Box, \vee(y, \bot))$, hole address $h = 1$. The master decomposition (Theorem 7.6) holds:
>
> $$
> C[t|_1] = \wedge(\Box, \vee(y,\bot))\big[\neg(\neg(x))\big] = \wedge(\neg(\neg(x)), \vee(y,\bot)) = t. \checkmark
> $$
>
> And replacement factors through the context (Proposition 9.5): $t[1 := \top] = C[\top]$.

> [!example] Example 27.3: Composition and disjointness
> Let $C_1 = \wedge(\Box, \vee(y,\bot))$ (hole $1$) and $C_2 = \neg(\Box)$ (hole $1$). The composite $C_1 \circ C_2 = \wedge(\neg(\Box), \vee(y,\bot))$ has hole address $1\cdot 1 = 11$, and $(C_1 \circ C_2)[x] = \wedge(\neg(x), \vee(y,\bot)) = C_1[C_2[x]]$ (Definition 10.7). The positions $1$ and $2$ of $t$ are disjoint ($1 \mathbin\| 2$), so replacements there commute (Proposition 9.10): $t[1 := \top][2 := \bot] = t[2 := \bot][1 := \top] = \wedge(\top, \bot) = t[1 := \top,\ 2 := \bot]$. By contrast $1 \prec 11$, so $t[1 := \top][11 := \top]$ is undefined-or-different: after $t[1 := \top]$ the address $11$ is gone, illustrating Proposition 9.10's failure for comparable positions.

### 27.3. Substitution and Matching

> [!example] Example 27.4: Substitution versus replacement
> Let $\sigma$ substitute $x := \vee(x, y)$, leaving $y, z$ fixed. Then
>
> $$
> \widehat\sigma(t) = \wedge\big(\neg(\neg(\vee(x,y))),\ \vee(y,\bot)\big),
> $$
>
> replacing the single occurrence of $x$ at $111$ by $\vee(x,y)$ and propagating. Here $x$ occurs once, so $\widehat\sigma(t)$ coincides with the replacement $t[111 := \vee(x,y)]$ — but only because $\#_x(t) = 1$. For $t' = \vee(x, \neg(x))$ with $\#_x(t') = 2$, $\widehat\sigma(t') = \vee(\vee(x,y), \neg(\vee(x,y)))$ touches **both** occurrences simultaneously, while a single replacement $t'[1 := \vee(x,y)]$ touches only one — the distinction of Warning 12.8.

> [!example] Example 27.5: A match and a non-match
> Pattern $\ell = \neg(\neg(U))$ (linear, $U \in M$) against $t|_1 = \neg(\neg(x))$: Construction 13.6 gives root $\neg$ = root $\neg$, descend; $\neg$ = $\neg$, descend; bind $U \mapsto x$. So $\sigma : U \mapsto x$ with $\ell\sigma = \neg(\neg(x)) = t|_1$. ✓ The same $\ell$ does **not** match $t|_2 = \vee(y, \bot)$: root $\neg \neq \vee$, immediate failure (Proposition 13.7). The nonlinear pattern $\wedge(U, U)$ does not match $t = \wedge(\neg(\neg(x)), \vee(y,\bot))$: it would bind $U \mapsto \neg(\neg(x))$ then require the second child $\vee(y,\bot)$ to equal $\neg(\neg(x))$, and the equality check fails.

### 27.4. A Rewrite Step, a Critical Pair, and a Normal Form

> [!example] Example 27.6: One rewrite step, fully instantiated
> Take $R = \{ (\mathrm{dn})\ \neg(\neg(U)) \to U,\ (\mathrm{or}\bot)\ \vee(V, \bot) \to V \}$. The tree $t$ has two redexes: $(1, \mathrm{dn}, U\mapsto x)$ since $t|_1 = \neg(\neg(x)) = \ell_{\mathrm{dn}}\sigma$, and $(2, \mathrm{or}\bot, V \mapsto y)$ since $t|_2 = \vee(y,\bot) = \ell_{\mathrm{or}\bot}\tau$. Contracting the first: context $C = t[1:=\Box] = \wedge(\Box, \vee(y,\bot))$, contractum $U\sigma = x$, result
>
> $$
> t \to_R C[x] = \wedge(x, \vee(y,\bot)) = t[1 := x].
> $$
>
> The two redexes are at disjoint positions $1 \mathbin\| 2$, so they may be contracted in parallel (Lemma 24.5): $t \Rrightarrow_R \wedge(x, y)$, the simultaneous result. A full reduction $t \to_R^* \wedge(x, y)$ reaches a normal form.

> [!example] Example 27.7: Convergence and the normal form function
> The system $R$ of Example 27.6 is **terminating** (each rule strictly decreases size, the size order is a reduction order, Theorem 15.5) and has **no critical pairs** (the left-hand sides $\neg(\neg(U))$ and $\vee(V,\bot)$ share no root symbol and cannot overlap at a non-variable position, so no unification of a subpattern occurs — it is non-overlapping; both lhs are linear, so the system is **orthogonal**, Definition 15.15). By orthogonality (Theorem 15.16) or by Newman + empty critical pairs (Corollary 15.14) it is **confluent**, hence **convergent**. Therefore every tree has a unique normal form, and $\operatorname{nf}_R(t) = \wedge(x, y)$. Two trees are $=_E$-equal (for $E$ the equational reading of $R$) iff they have the same normal form (Theorem 16.13): e.g. $\neg(\neg(\vee(z,\bot))) =_E z$ because both normalize to $z$.

> [!example] Example 27.8: A non-confluent and a non-terminating variant
> Adding the rule $(\mathrm{comm})\ \vee(U, V) \to \vee(V, U)$ breaks termination ($\vee(y, z) \to \vee(z, y) \to \vee(y, z) \to \cdots$, Example 15.6), so $\operatorname{nf}_R$ is no longer total; the quotient by commutativity is instead presented by **sorting** children into a canonical order (Remark 16.15). Adding instead $(\mathrm{absurd})\ \wedge(U, \bot) \to \bot$ and $(\mathrm{taut})\ \wedge(U, \top) \to U$ keeps termination; one then checks the critical pairs (e.g. the overlap of $\mathrm{absurd}$ with itself, and with the other rules at the root) are joinable to confirm convergence (Corollary 15.14). The worked system thus exhibits the convergent case, the non-terminating case, and the critical-pair check, exactly the trichotomy of Section 15.

### 27.5. The Quotient Class

> [!example] Example 27.9: A quotient tree algebra
> Let $E$ be the Boolean idempotence-and-units theory generated by $\{\vee(U, \bot) = U,\ \wedge(U, \top) = U,\ \neg(\neg(U)) = U,\ \vee(U,U) = U,\ \wedge(U,U) = U\}$ (a fragment). The quotient $\operatorname{Tree}_\Omega(X)/{=_E}$ has as elements the $=_E$-classes; the class of $t = \wedge(\neg(\neg(x)), \vee(y,\bot))$ contains $\wedge(x, y)$ (via the $\mathrm{dn}$ and $\mathrm{or}\bot$ identities) and is the element $[\wedge(x,y)]$. The constructor operations act on classes by $\wedge^{/\equiv}([a],[b]) = [\wedge(a,b)]$ (Definition 16.7), well-defined because $=_E$ is a congruence (Proposition 16.8). The map $[t]_{=_E} \mapsto \operatorname{nf}_R(t)$ (for a convergent orientation $R$ of the orientable fragment) picks canonical representatives (Theorem 16.13); the non-orientable identities (idempotence, here orientable; commutativity, not present) would otherwise require normalization-modulo. This realizes the passage raw syntax $\to$ quotient syntax of Section 16 on concrete data.

---

## 28. Unification, Anti-Unification, and the Order on Patterns

Matching (Section 13) is one of three closely related operations on patterns, distinguished by which sides carry variables and by the direction of the comparison. This section completes the trio: **matching** ($\ell\sigma = u$, instantiate one side to reach a fixed target), **unification** ($s\sigma = t\sigma$, instantiate both to make them equal), and **anti-unification** (find the least instantiated pattern of which two trees are instances). All three are organized by a single partial order on patterns — the **instantiation order** — under which matching, unification, and anti-unification compute, respectively, downward reachability, greatest lower bounds of the instance sets, and least upper bounds. The development is precise and tied to the rewriting spine (unification computes critical pairs; anti-unification discovers schemas).

### 28.1. The Instantiation Order

> [!definition] Definition 28.1: Instantiation (subsumption) order on patterns
> For patterns $s, t \in \operatorname{Tree}_\Omega(X \sqcup M)$, say $s$ is **more general than** $t$ (or $t$ is an **instance** of $s$), written $s \preceq_{\mathrm{inst}} t$, if there is a pattern substitution $\sigma$ with $s\sigma = t$. The relation $\preceq_{\mathrm{inst}}$ is a preorder; its induced equivalence — $s$ and $t$ are inter-instances — is **renaming equivalence** ($s\sigma = t$ and $t\tau = s$ force $\sigma, \tau$ to be mutually inverse renamings of metavariables). Modulo renaming, $\preceq_{\mathrm{inst}}$ is a partial order. A single metavariable $U \in M$ is the **top** (most general) pattern; ground trees are **minimal** (only instances of themselves up to renaming).

> [!proposition] Proposition 28.2: Matching is downward search in the instantiation order
> A pattern $\ell$ matches a ground tree $u$ iff $\ell \preceq_{\mathrm{inst}} u$, and the matching substitution (Construction 13.6) is the witness $\sigma$ with $\ell\sigma = u$, unique on $\operatorname{Var}_M(\ell)$ (Proposition 13.7). Thus matching decides a single instance-order comparison against a fixed ground target and returns the witnessing substitution.
>
> [!proof-sketch] Proof Sketch 28.2
> By definition $\ell \preceq_{\mathrm{inst}} u$ means $\exists\sigma\ \ell\sigma = u$, which is exactly the existence of a match; uniqueness of $\sigma$ on the metavariables of $\ell$ is Proposition 13.7, since $u$ being ground pins each metavariable's image at its occurrence position.

### 28.2. Unification

> [!definition] Definition 28.3: Unifier and most general unifier
> A **unifier** of patterns $s, t$ is a substitution $\sigma$ with $s\sigma = t\sigma$. A unifier $\mu$ is a **most general unifier (mgu)** if every unifier $\sigma$ factors as $\sigma = \rho \star \mu$ for some $\rho$ (Definition 12.4); equivalently $\mu$ is a $\preceq_{\mathrm{inst}}$-greatest element among the substitutions making $s, t$ equal, so that $s\mu = t\mu$ is the **most general common instance** of $s$ and $t$.

> [!theorem] Theorem 28.4: Unification theorem (existence and computation of mgu)
> Two patterns $s, t$ are unifiable iff the unification algorithm — decompose matching subterms, bind a metavariable to a tree (with an **occurs-check** rejecting $U \mapsto$ a proper superterm of $U$), and fail on root-symbol clash — succeeds; on success it returns an mgu, unique up to renaming. Hence the set of unifiers, when nonempty, has a greatest element in $\preceq_{\mathrm{inst}}$, the most general common instance $s\mu = t\mu$ is the **least upper bound** of $\{s, t\}$ in the instantiation order, and unifiability is decidable in (near-)linear time.
>
> [!proof-sketch] Proof Sketch 28.4
> The algorithm maintains a set of equations and a partial substitution, preserving the invariant "same unifiers." Decomposition $f(\vec s) \doteq f(\vec t) \leadsto s_i \doteq t_i$ is sound (a unifier of the parent unifies the children); clash $f(\dots) \doteq g(\dots)$ with $f \neq g$ has no unifier; variable elimination $U \doteq r$ (with $U \notin \operatorname{Var}_M(r)$, the occurs-check) binds $U \mapsto r$ and substitutes, strictly reducing the number of unsolved metavariables. Termination follows from a well-founded measure (unsolved variables, then total size); on success the accumulated substitution is a unifier and is most general because every binding made was forced. Uniqueness up to renaming is the antisymmetry of $\preceq_{\mathrm{inst}}$ modulo renaming.

> [!warning] Warning 28.5: The occurs-check and the difference from matching
> Unification differs from matching in two structural respects (Warning 13.13): both sides carry metavariables, and the **occurs-check** is required — without it, $U \doteq f(U)$ would falsely "unify," producing the infinite rational tree $f(f(f(\cdots)))$ rather than failing. Matching never needs the occurs-check (its target is fixed/ground, so a metavariable is bound to a subtree of the target, never to a superterm of itself). Unification yields a *set* of unifiers with an mgu; matching yields *at most one* substitution. Unification is the operation used to compute **critical pairs** (Definition 15.12): overlapping two left-hand sides is unifying a subpattern of one with the other, and the mgu produces the overlapped instance from which the critical pair is read.

### 28.3. Anti-Unification

> [!definition] Definition 28.6: Generalization and least general generalization
> A **generalization** (anti-unifier) of trees $t_1, t_2$ is a pattern $g$ such that both $t_1$ and $t_2$ are instances of $g$: $g \preceq_{\mathrm{inst}} t_1$ and $g \preceq_{\mathrm{inst}} t_2$. A **least general generalization (lgg)** (synonym: **most specific generalization**) is a generalization $g$ that is $\preceq_{\mathrm{inst}}$-greatest among generalizations — every generalization is more general than $g$ — so $g$ is the **greatest lower bound** of $\{t_1, t_2\}$ in the instantiation order.

> [!theorem] Theorem 28.7: Existence and computation of the lgg
> Every pair of trees has a least general generalization, unique up to renaming, computed by the anti-unification algorithm: recurse on corresponding positions; where the two trees agree on root symbol and arity, keep that symbol and recurse on children; where they differ, introduce a fresh metavariable, reusing the **same** metavariable for repeated occurrences of the same disagreeing pair (so equal disagreements are generalized consistently). Hence $(\operatorname{Tree}_\Omega(X \sqcup M)/{\sim_{\mathrm{ren}}}, \preceq_{\mathrm{inst}})$ has binary meets given by lgg and binary joins (where defined) given by mgu.
>
> [!proof-sketch] Proof Sketch 28.7
> The algorithm produces a pattern $g$ with substitutions $\sigma_1, \sigma_2$ (recording, per fresh metavariable, the two disagreeing subtrees) such that $g\sigma_i = t_i$, so $g$ is a generalization. It is least general because any generalization $g'$ must place a metavariable wherever $t_1, t_2$ disagree (a constructor symbol there would clash with one of them), so $g' \preceq_{\mathrm{inst}} g$ by mapping $g'$'s metavariables onto $g$'s structure. Consistency of repeated disagreements (same metavariable) is what makes $g$ least rather than merely a generalization. Uniqueness up to renaming is antisymmetry of the order.

> [!example] Example 28.8: A worked anti-unification
> Anti-unify $t_1 = f(a, g(b))$ and $t_2 = f(a, g(c))$ (with $a, b, c$ distinct constants): roots agree ($f$, arity $2$); first children agree ($a$); second children $g(b), g(c)$ agree on root $g$, recurse; $b \neq c$, introduce fresh $U$. Result $g = f(a, g(U))$, with $\sigma_1 : U \mapsto b$, $\sigma_2 : U \mapsto c$. This $f(a, g(U))$ is the lgg — the most specific pattern of which both trees are instances — capturing their shared structure and abstracting only the point of disagreement.

> [!remark] Remark 28.9: The trio and their uses
> Matching, unification, and anti-unification are the three instantiation-order operations, each with a characteristic use in the tree calculus:
>
> 1. **matching** ($\ell \preceq_{\mathrm{inst}} u$, target fixed): locating redexes in rewriting (Section 14), instantiating schemas;
> 2. **unification** (join, lub, mgu): computing critical pairs and overlaps (Section 15), solving equation systems, logic-programming resolution;
> 3. **anti-unification** (meet, glb, lgg): **discovering** schemas and common patterns from examples — given several formulas sharing structure, the lgg infers the common context, the inverse problem to matching.
>
> Together they organize the pattern layer as a lattice-ordered structure on the metavariable-carrying trees, with matching the membership test, unification the join, and anti-unification the meet. The same instantiation order governs subsumption in theorem proving and generalization in inductive inference.

---

## 29. Equational Logic: Soundness, Completeness, and Term Models

Section 16 constructed the congruence $=_E$ generated by an equation set $E$ and the quotient tree algebra $\operatorname{Tree}_\Omega(X)/{=_E}$. This section connects that syntactic construction to semantics: an equation holds in a class of algebras exactly when it is derivable, and the quotient is the generic model. This is the bridge from the tree calculus to model theory and universal algebra, developed compactly. It explains in what sense rewriting and quotienting are *sound* and *complete* for equational reasoning.

### 29.1. Satisfaction and Equational Validity

> [!definition] Definition 29.1: Satisfaction of an equation
> An $\Omega$-algebra $\mathbf{A}$ **satisfies** an equation $\ell = r$ (over metavariables $M$ read as variables), written $\mathbf{A} \models \ell = r$, if for every assignment $g : M \to A$ the evaluations agree: $\operatorname{ev}_g(\ell) = \operatorname{ev}_g(r)$. For a set $E$ of equations, $\mathbf{A} \models E$ if $\mathbf{A}$ satisfies every equation of $E$; the class $\operatorname{Mod}(E) := \{\mathbf{A} : \mathbf{A} \models E\}$ is the **variety** defined by $E$. An equation $\ell = r$ is a **semantic consequence** of $E$, written $E \models \ell = r$, if every algebra in $\operatorname{Mod}(E)$ satisfies it.

> [!theorem] Theorem 29.2: Soundness of equational derivation
> If $\ell = r$ is derivable from $E$ — i.e. $\ell =_E r$ in the congruence of Section 16 (equivalently provable by reflexivity, symmetry, transitivity, congruence, and substitution from $E$, Theorem 16.5) — then $E \models \ell = r$.
>
> [!proof-sketch] Proof Sketch 29.2
> The relation $\{(\ell, r) : E \models \ell = r\}$ is a congruence (each closure rule preserves semantic validity: evaluation respects reflexivity/symmetry/transitivity of equality, commutes with constructors giving congruence, and is stable under substitution since $\operatorname{ev}_g(\ell\sigma) = \operatorname{ev}_{g'}(\ell)$ for the composed assignment $g'$) and it contains $E$. Hence it contains the least such congruence $=_E$, i.e. $\ell =_E r \Rightarrow E \models \ell = r$.

### 29.2. The Term Model and Completeness

> [!construction] Construction 29.3: The free $E$-algebra (term model)
> The quotient $\mathbf{F}_E := \operatorname{Tree}_\Omega(M)/{=_E}$ (taking the variable set to be $M$ itself) is the **term model** of $E$: it satisfies $E$ (Theorem 16.10), is generated by the classes $[U]$ of the metavariables, and is the **free algebra in $\operatorname{Mod}(E)$ on $M$** — every assignment of $M$ into an $E$-algebra extends uniquely to a homomorphism out of $\mathbf{F}_E$.

> [!theorem] Theorem 29.4: Birkhoff completeness
> Equational derivation is complete for equational consequence: for all patterns $\ell, r$,
>
> $$
> E \models \ell = r \quad\Longleftrightarrow\quad \ell =_E r.
> $$
>
> Hence $\operatorname{Mod}(E) = \operatorname{Mod}(E')$ iff $E$ and $E'$ generate the same congruence, and the equational theory $=_E$ is exactly the set of equations valid in the variety $\operatorname{Mod}(E)$.
>
> [!proof-sketch] Proof Sketch 29.4
> ($\Leftarrow$) is soundness (Theorem 29.2). ($\Rightarrow$): the term model $\mathbf{F}_E$ lies in $\operatorname{Mod}(E)$, so if $E \models \ell = r$ then $\mathbf{F}_E \models \ell = r$; evaluating under the generator assignment $U \mapsto [U]$, the identity homomorphism's action gives $\operatorname{ev}(\ell) = [\ell]_{=_E}$ and $\operatorname{ev}(r) = [r]_{=_E}$, so validity in $\mathbf{F}_E$ forces $[\ell]_{=_E} = [r]_{=_E}$, i.e. $\ell =_E r$. The term model is the single algebra witnessing completeness: an equation valid everywhere in the variety is already valid in the generic quotient.

> [!corollary] Corollary 29.5: Convergent rewriting decides equational validity
> If $E$ admits a convergent orientation $R$ (Theorem 16.13), then $E \models \ell = r$ is decidable: it holds iff $\operatorname{nf}_R(\ell) = \operatorname{nf}_R(r)$. Thus a convergent term rewriting system is a decision procedure for the equational theory of its variety, computing in each $=_E$-class the canonical normal-form representative that the term model's elements abstractly are.
>
> [!proof-sketch] Proof Sketch 29.5
> Birkhoff completeness reduces $E \models \ell = r$ to $\ell =_E r$; Theorem 16.13 reduces the latter to equality of normal forms under a convergent $R$. Normalization is effective (terminating, with unique results by confluence), so the composite is a decision procedure.

> [!remark] Remark 29.6: The semantic closure of the spine
> Birkhoff's theorem closes the loop opened in Section 16: the syntactic congruence $=_E$ (built by reflexivity/symmetry/transitivity/congruence/substitution), the quotient tree algebra (its algebra of classes), the variety $\operatorname{Mod}(E)$ (its models), and — when available — the normal-form function $\operatorname{nf}_R$ (its decision procedure) are four faces of one object. Soundness says rewriting/quotienting never proves a false equation; completeness says it proves every valid one; convergence says it decides validity. This is the precise sense in which the directed computation of Section 14 and the symmetric identification of Section 16 *are* equational reasoning, with the tree calculus supplying both the syntax (free term algebra) and the proof theory (congruence closure), and model theory supplying the semantics (varieties) that the term model mediates.

---

## 30. Reduction Orders and Termination Techniques

Theorem 15.5 reduces termination of a tree rewriting system to the existence of a compatible reduction order, but constructing such orders is itself a subject. This section develops the principal techniques — simplification orders, the recursive path order, polynomial and monotone-algebra interpretations, and the multiset and lexicographic order constructions — in compact but precise form, completing the termination half of the metatheory and explaining why termination is generally hard (indeed undecidable).

### 30.1. Simplification Orders

> [!definition] Definition 30.1: Monotone and simplification orders
> A strict order $\succ$ on $\operatorname{Tree}_L$ is **monotone** (has the **replacement property**) if $s \succ s'$ implies $C[s] \succ C[s']$ for every one-hole context $C$ — i.e. it is stable under contexts (Definition 15.4(ii)). It has the **subterm property** if $C[s] \succ s$ for every non-trivial context $C$ (a proper superterm exceeds its subterms). A **simplification order** is a monotone, stable-under-substitution strict order with the subterm property.

> [!theorem] Theorem 30.2: Simplification orders are well-founded
> Over a finite signature, every simplification order is well-founded, hence a reduction order. Consequently a TRS compatible with a simplification order ($\ell \succ r$ for every rule, the **lhs strictly exceeds the rhs**) is terminating.
>
> [!proof-sketch] Proof Sketch 30.2
> Well-foundedness follows from **Kruskal's tree theorem**: the finite trees over a finite signature are **well-quasi-ordered** by the homeomorphic embedding (a tree embeds in any tree containing it as a "subtree with extra material"). An infinite $\succ$-descending chain $t_0 \succ t_1 \succ \cdots$ would, by the wqo, contain indices $i < j$ with $t_i$ embeddable in $t_j$; the subterm and monotonicity properties give $t_j \succeq t_i$, contradicting $t_i \succ t_j$. Hence no infinite descending chain, i.e. well-foundedness; compatibility then gives termination by Theorem 15.5.

### 30.2. The Recursive Path Order

> [!definition] Definition 30.3: Precedence and the recursive path order (RPO)
> Fix a **precedence** $\succ_\Omega$, a strict order on the operation symbols. The **recursive path order** $\succ_{\mathrm{rpo}}$ on ground trees is defined recursively: $s = f(s_1,\dots,s_m) \succ_{\mathrm{rpo}} t$ iff one of
>
> 1. some $s_i \succeq_{\mathrm{rpo}} t$ (subterm dominates), or
> 2. $t = g(t_1,\dots,t_n)$ with $f \succ_\Omega g$ and $s \succ_{\mathrm{rpo}} t_j$ for all $j$ (bigger head, dominates all rhs subterms), or
> 3. $t = f(t_1,\dots,t_n)$ (same head) and $(s_1,\dots,s_m) \succ_{\mathrm{rpo}}^{\mathrm{ext}} (t_1,\dots,t_n)$ in the chosen multiset or lexicographic extension, with $s \succ_{\mathrm{rpo}} t_j$ for all $j$ in the lexicographic case.
>
> The variant using the **multiset** extension at clause 3 is the **multiset path order (MPO)**; using the **lexicographic** extension is the **lexicographic path order (LPO)**.

> [!theorem] Theorem 30.4: RPO is a simplification order
> For any precedence $\succ_\Omega$ (well-founded if $\Omega$ is infinite), $\succ_{\mathrm{rpo}}$ is a simplification order: it is a monotone, substitution-stable strict order with the subterm property, hence well-founded (Theorem 30.2). Therefore a TRS with $\ell \succ_{\mathrm{rpo}} r$ for every rule is terminating, and this is checkable by the recursive definition.
>
> [!proof-sketch] Proof Sketch 30.4
> Irreflexivity and transitivity are proved by simultaneous induction on term sizes from the three clauses. The subterm property is clause 1; monotonicity (context stability) follows because clause 3 with equal heads propagates a child decrease upward; substitution stability holds because the precedence and the recursive structure are unaffected by instantiating variables (a variable is treated as a minimal constant). Well-foundedness is Theorem 30.2. Compatibility $\ell \succ_{\mathrm{rpo}} r$ is decidable by unfolding the definition.

> [!example] Example 30.5: Termination of a system by LPO
> Consider Ackermann-like rules $A(0, y) \to s(y)$, $A(s(x), 0) \to A(x, s(0))$, $A(s(x), s(y)) \to A(x, A(s(x), y))$. With precedence $A \succ_\Omega s$ and the lexicographic extension on $A$'s arguments (first argument dominant), each rule's lhs exceeds its rhs in $\succ_{\mathrm{lpo}}$: the first argument strictly decreases ($s(x) \to x$) in rules 2 and 3, dominating the nested calls, and rule 1 decreases by the subterm/precedence clauses. Hence the system terminates although it computes a non-primitive-recursive function — illustrating that LPO certifies termination of deeply nested recursions where a naive size order fails.

### 30.3. Interpretation Methods

> [!definition] Definition 30.6: Monotone algebra / polynomial interpretation
> A **monotone $\Omega$-algebra** is an $\Omega$-algebra $\mathbf{A}$ on a carrier $A$ equipped with a well-founded order $>_A$ such that every operation $f^{\mathbf{A}}$ is **strictly monotone** in each argument. A **polynomial interpretation** is the case $A = \mathbb{N}$ (or $\{n \in \mathbb{N} : n \ge n_0\}$) with $>_A$ the usual order and each $f^{\mathbf{A}}$ a polynomial strictly monotone in each variable; the induced order on trees is $s \succ t$ iff $\operatorname{ev}_{\mathbf{A}}(s) > \operatorname{ev}_{\mathbf{A}}(t)$ under every assignment of variables to $A$ (uniformly).

> [!theorem] Theorem 30.7: Termination by monotone interpretation
> If $\mathbf{A}$ is a monotone $\Omega$-algebra and a TRS $R$ satisfies $\operatorname{ev}_{g}(\ell) >_A \operatorname{ev}_{g}(r)$ for every rule and every assignment $g$, then $R$ is terminating. For polynomial interpretations this reduces to a finite set of polynomial inequalities (the rules), checkable by comparing coefficients.
>
> [!proof-sketch] Proof Sketch 30.7
> The order $s \succ t :\Leftrightarrow \forall g.\ \operatorname{ev}_g(s) >_A \operatorname{ev}_g(t)$ is a reduction order: well-founded because $>_A$ is and evaluations are natural numbers (or carrier elements) with no infinite descent; context-stable because each $f^{\mathbf{A}}$ is strictly monotone, so a strict decrease in one argument's value strictly decreases the whole; substitution-stable because instantiating a variable amounts to evaluating under a derived assignment. Compatibility is the rule inequality; Theorem 15.5 concludes termination. The reduction to coefficient comparison uses that a polynomial inequality holding for all large naturals is decided by leading terms.

> [!example] Example 30.8: A polynomial interpretation
> For $R = \{ \neg(\neg(U)) \to U,\ \vee(U, \bot) \to U \}$ (Example 27.6), interpret over $\mathbb{N}$ with $\neg^{\mathbf{A}}(n) = n + 1$, $\vee^{\mathbf{A}}(m, n) = m + n + 1$, $\bot^{\mathbf{A}} = 0$, variables $\ge 0$. Then $\operatorname{ev}(\neg(\neg(U))) = U + 2 > U = \operatorname{ev}(U)$ and $\operatorname{ev}(\vee(U,\bot)) = U + 0 + 1 = U + 1 > U$, so both rules strictly decrease the interpretation and $R$ terminates (Theorem 30.7) — a second proof of the termination established by size in Example 27.7, now robust to rules that do not decrease node count.

### 30.4. Limits of Termination Analysis

> [!warning] Warning 30.9: Termination is undecidable
> No algorithm decides, for an arbitrary finite TRS, whether it terminates: termination of term rewriting is undecidable (it encodes the halting problem, since Turing machines are simulable by rewrite systems). The methods of this section are therefore **sufficient conditions**, not decision procedures: RPO/LPO and polynomial interpretations certify termination when they apply but may fail on terminating systems they cannot orient. Modern tools combine them with the **dependency pair** method — which analyzes only the "recursive calls" (the dependency pairs) rather than whole rules and seeks orders making the dependency chains decrease — vastly extending reach, but the undecidability barrier remains: some terminating systems elude all current methods.

> [!remark] Remark 30.10: The shape of the termination toolbox
> The termination techniques form a layered toolbox over the reduction-order criterion (Theorem 15.5): **syntactic orders** (RPO/LPO via a precedence, Theorem 30.4) handle structural recursions cheaply; **semantic orders** (polynomial and matrix interpretations, Theorem 30.7) handle systems where a numerical potential decreases; **transformational methods** (dependency pairs, semantic labelling) reduce a hard termination problem to easier ones. All ultimately exhibit a well-founded, context- and substitution-stable order in which every rule decreases, because that — by Theorem 15.5 — is exactly what termination of a closed-under-contexts-and-substitutions relation requires. The undecidability of Warning 30.9 is why the toolbox is open-ended rather than a single algorithm, and why termination, unlike local confluence (decidable via critical pairs, Theorem 15.13), has no finite complete criterion.

---

## 31. Synthesis: The Tree Calculus

This final section collects the central definitions, constructions, equivalences, theorems, proof mechanisms, and failure modes of the treatise into a single coordinated picture, organized around the operational spine. It is intended as a reference index to the development, not a re-derivation.

### 31.1. The Spine

The conceptual and definitional development is the chain

$$
\text{trees} \;\to\; \text{positions and subtrees} \;\to\; \text{replacement} \;\to\; \text{contexts} \;\to\; \text{substitution} \;\to\; \text{matching} \;\to\; \text{rewriting} \;\to\; \text{normal forms and quotients},
$$

with each stage defined from its predecessors: subtrees from the address structure of trees (Definition 7.2); replacement from subtree extraction (Definition 9.3); contexts as the residue of extraction (Definitions 10.4, 7.6); plugging as replacement at the hole (Proposition 9.5); substitution as the homomorphic extension of a leaf assignment (Definition 12.2); matching as the partial inverse of substitution along a pattern (Definitions 13.4, 13.17); the one-step rewrite as replacement at a matched position by the contracted rhs instance (Definition 14.7); normal forms as rewrite-irreducible trees (Definition 15.1); and the quotient tree algebra as the carrier of congruence classes (Definition 16.7), decided by normalization when a convergent system is available (Theorem 16.13).

### 31.2. The Operations Table

| Notation | Name | Input data | Output | Defining reference | Key law |
|---|---|---|---|---|---|
| $t\lvert_p$ | subtree extraction | tree $t$, position $p \in D_t$ | tree | Def. 7.2 / 9.1 | $(t\lvert_p)\lvert_q = t\lvert_{p\cdot q}$ (Prop. 9.2) |
| $t[p := s]$ | replacement | tree, position, tree | tree | Def. 9.3 | $= C[s]$ for $C = t[p:=\Box]$ (Prop. 9.5) |
| $a(t_1,\dots,t_n)$ | grafting | label, arity-many trees | tree | Def. 4.7 | unique readability (Prop. 4.8) |
| $t[p := \Box]$ | context extraction | tree, position | one-hole context | Def. 10.4 | $C[t\lvert_p] = t$ (Thm. 7.6) |
| $C[s]$ | plugging | context, tree | tree | Def. 10.5 | $(C[s])\lvert_h = s$ (Prop. 10.6) |
| $C_1 \circ C_2$ | context composition | two contexts | context | Def. 10.7 | monoid / category (Props. 10.9, 11.6) |
| $\sigma : X \to T$ | substitution assignment | variable-to-tree map | — | Def. 12.1 | — |
| $\widehat\sigma(t) = t\sigma$ | substitution | assignment, tree | tree | Def. 12.2 | monad laws (Thm. 12.5) |
| $\ell\sigma = u$ | matching | pattern, tree | substitution (partial) | Def. 13.4 | unique match (Prop. 13.7) |
| $(p, \ell\to r, \sigma)$ | redex | position, rule, match | — | Def. 14.4 | $t\lvert_p = \ell\sigma$ |
| $t = C[\ell\sigma]$ | redex in context | tree, context, rule, match | — | Def. 14.6 | located at $p$ |
| $t' = C[r\sigma]$ | rewrite step | redex | tree | Def. 14.7 | $t' = t[p := r\sigma]$ |
| $\twoheadrightarrow_R$ | reduction | TRS, tree | reachable trees | Def. 14.12 | reflexive-transitive closure |
| $\operatorname{nf}_R(t)$ | normal form | convergent TRS, tree | irreducible tree | Def. 15.1, Thm. 16.13 | unique under convergence |
| $T/{=_E}$ | quotient tree algebra | congruence | $\Omega$-algebra of classes | Def. 16.7 | UMP (Thm. 16.10) |

### 31.3. The Central Equivalences and Theorems

> [!remark] Remark 31.1: Load-bearing results
> The development rests on a small number of structural theorems, each invoked repeatedly:
>
> 1. **Unique readability** (Prop. 4.8): the grafting map is a bijection; every nonempty tree decomposes uniquely. Underwrites recursion, the destructors, and matching's determinism.
> 2. **Well-foundedness of the subtree order** (Prop. 5.4): legitimizes structural induction (Thm. 5.5) and structural recursion (Thm. 5.7) in the finite setting; fails for infinite trees (Warning 22.3).
> 3. **Freeness of the tree algebra** (Thm. 8.8) and **freeness = generatedness + unique decomposition** (Thm. 8.9): identify the tree algebra with the absolutely free / initial algebra and make every presentation canonically comparable (Cor. 8.10).
> 4. **Context–subtree decomposition** (Thm. 7.6): $t = C[t\lvert_p]$, the master factorization; the basis of contexts, replacement, zippers, and rewriting.
> 5. **Substitution monad laws** (Thm. 12.5): $\widehat\tau \circ \widehat\sigma = \widehat{\tau \star \sigma}$; the engine of substitution stability of $\to_R$ and of congruence generation.
> 6. **Uniqueness of matches** (Prop. 13.7): syntactic matching is a partial function; distinguishes matching from unification.
> 7. **Newman's lemma** (Thm. 15.11) and the **critical pair lemma** (Thm. 15.13): termination reduces confluence to local confluence, and local confluence to a finite critical-pair check.
> 8. **Convergence decides the congruence** (Thm. 16.13) and **Birkhoff completeness** (Thm. 29.4): rewriting computes quotient and equational equality when convergent, and equational derivation is sound and complete for variety validity.

### 31.4. The Standing Distinctions, Resolved

> [!remark] Remark 31.2: Where each distinction lives
> The hazards of §0.3 are resolved at precise loci: **node vs. label** (Warning 4.5); **position vs. subtree** (Defs. 3.1, 7.2); **path vs. branch** (Warning 3.6); **tree domain vs. labelled tree** (Defs. 4.2, 4.4); **replacement vs. substitution** (Warning 12.8); **substitution vs. relabelling vs. plugging** (Warning 12.9); **one-hole vs. multi-hole context** (Defs. 10.2, 10.11); **object vs. pattern variable** (Warning 13.2); **matching vs. unification** (Warning 13.13, 28.5); **equation vs. rewrite rule** (Remarks 14.13, 16.6); **congruence closure vs. rewrite closure** (Prop. 16.3, Prop. 14.10); **syntactic vs. quotient equality** (Warning 16.11); **tree occurrence vs. DAG sharing** (Warning 17.5). Each is a type or scope distinction enforced by the formal apparatus, not a matter of emphasis.

### 31.5. Failure Modes

> [!warning] Warning 31.3: The catalogue of failure modes
> The treatise's warnings identify the precise conditions under which constructions break:
>
> 1. **Malformed/overloaded trees**: arity-correctness or single-valued rank violated (Warning 4.9) — destroys unique readability.
> 2. **Recursion on quotients without descent**: a fold's clauses must respect $\equiv$ (Warning 5.8, 16.9) — else ill-defined on classes.
> 3. **Sort mismatch in typed plugging/rewriting** (Warnings 11.8, 9.17) — the typed partiality, not an error to repair.
> 4. **Variable condition violated in a rule** ($\operatorname{Var}_M(r) \not\subseteq \operatorname{Var}_M(\ell)$, or lhs a metavariable) (Warning 14.2) — rhs instance undefined or relation trivialized.
> 5. **Termination/confluence confusions**: local confluence without termination does not give confluence; termination and confluence are independent (Warning 15.10) — only convergence gives unique normal forms.
> 6. **Non-orientable equations** (commutativity, AC): no terminating orientation (Warnings 14.15, 16.14) — require rewriting modulo or canonical-representative normalization.
> 7. **Equational vs. syntactic matching**: matching modulo equations loses uniqueness (Warning 13.15).
> 8. **DAG sharing vs. occurrence**: sharing is sound only for syntactic equality; context extraction is multivalued on DAGs (Warnings 17.5, 17.6).
> 9. **Binding/capture**: in syntax with binders, context filling captures while object substitution must avoid capture (Warnings 16.17, 24.2) — the boundary the non-binding calculus does not cross.
> 10. **Undecidability of termination** (Warning 30.9) — termination methods are sufficient, never complete.

### 31.6. Closing Statement

> [!remark] Remark 31.4: What the calculus achieves
> The treatise has developed finite trees from six equivalent presentations (graph, order, address, algebraic, automata-theoretic, operadic/coalgebraic), fixed the address model as primary, and built upon it a calculus whose generators are subtree extraction and replacement. From these, contexts arise as the residue of extraction, plugging as replacement at a hole, substitution as the free algebra's universal extension, matching as substitution's partial inverse along a pattern, rewriting as replacement at a matched position, and normal forms and quotient tree algebras as the static residue of rewriting and equational identification. The metatheory — termination via reduction orders, confluence via critical pairs and orthogonality, convergence as the conjunction deciding the generated congruence, and Birkhoff completeness identifying that congruence with equational validity — shows that the directed calculus of computation and the symmetric calculus of identity are two orientations of one structure. The adjacent theories (DAGs, automata, transducers, operads, proof theory, infinite trees, algorithms) each map the calculus into a neighboring mathematical domain, recognizing the same spine — trees, subtrees, contexts, substitution, matching, rewriting, normal forms, quotients — under a different aspect. The result is the intended object: trees not as pictures or encodings, but as a mathematically controlled environment for syntax, transformation, and computation.
