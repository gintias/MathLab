---
title: "Parameterized Propositional Logic Modulo Tautologies"
subtitle: "Raw syntax, contexts, substitutions, quotient Boolean algebras, schema operators, and first-order instantiation"
tags: [logic, propositional-logic, sentential-logic, universal-algebra, free-algebra, boolean-algebra, lindenbaum-tarski-algebra, contexts, substitutions, schemas, formal-logic, first-order-logic]
---

# Parameterized Propositional Logic Modulo Tautologies

## 0. Orientation

### 0.1. Purpose of the treatise

This treatise develops a fully syntactic and algebraic skeleton of propositional logic suitable for later use inside first-order logic. The goal is not merely to define propositional formulas, truth tables, or tautologies in the usual introductory way. The goal is to isolate a reusable **parameterized propositional module** with the following features:

1. raw formulas are built as an absolutely free algebra;
2. contexts are formulas with holes and therefore induce fixed-shape operations;
3. substitutions are homomorphic extensions of assignments of atoms to formulas;
4. tautological equivalence is a congruence on raw formulas;
5. quotienting by tautological equivalence gives the free Boolean algebra on the atom set;
6. quotient contexts form the Boolean clone of polynomial operations;
7. tautological schemas are precisely top-valued quotient contexts;
8. broader schema operators such as CNF, DNF, duality, and variable elimination sit above ordinary contexts;
9. the entire mechanism can be instantiated into first-order logic by filling propositional holes with first-order formulas.

The intended endpoint is a rigorous way to say:

$$
\text{all substitution instances of propositional tautologies are available inside FOL.}
$$

But instead of treating that as informal schema language, we derive it from free syntax, substitution, quotient Boolean algebras, and context operations.

### 0.2. The central architecture

The development has four layers.

**Layer 1: raw propositional syntax.** For each atom set $A$, we construct the formula algebra

$$
\mathbf{Fm}(A),
$$

the absolutely free propositional algebra on $A$.

**Layer 2: tautological quotient.** We quotient raw formulas by tautological equivalence:

$$
LT(A):=Fm(A)/{\equiv_{\mathrm{taut}}}.
$$

This is the Lindenbaum-Tarski algebra of classical propositional logic over $A$, and it is the free Boolean algebra on $A$.

**Layer 3: contexts and quotient contexts.** For a finite hole set

$$
H_n=\{\Box_0,\dots,\Box_{n-1}\},
$$

we define raw contexts and quotient contexts by

$$
Ctx_n(P):=Fm(P\sqcup H_n),
$$

and

$$
QCtx_n(P):=LT(P\sqcup H_n).
$$

Raw contexts are fixed syntactic templates. Quotient contexts are Boolean polynomial operations with parameters.

**Layer 4: schema operators.** Context filling and substitution are not the only useful formula operations. CNF, DNF, duality, resolution, variable elimination, and interpolation are recursive or semantic transformations. These are treated as schema operators, not ordinary contexts.

The slogan is:

$$
\boxed{
\text{contexts} \subsetneq \text{context/substitution operations} \subsetneq \text{recursive schema operators}.
}
$$

### 0.3. Main distinction

A recurring distinction governs the entire theory.

A **context** has fixed finite shape. For example,

$$
C(\Box_0,\Box_1)=\Box_0\vee\Box_1
$$

has one outer disjunction node and two holes. Filling the holes changes the inputs but not the outer template shape.

A **syntax operator** may inspect and transform an arbitrary input formula. For example,

$$
\varphi\mapsto CNF(\varphi),
$$

or

$$
\varphi\mapsto \varphi[A:=\top]\vee\varphi[A:=\bot]
$$

does not have one fixed finite context shape independent of $\varphi$. The output shape depends on the input formula.

Thus:

$$
\boxed{\text{context} = \text{fixed formula with holes};}
$$

$$
\boxed{\text{operator} = \text{possibly recursive transformation on formulas}.}
$$

---

## 1. Raw propositional syntax

### 1.1. Atom sets and connective signatures

> [!definition] Atom set
> An **atom set** is a set $A$ whose elements are treated as propositional atoms, sentence symbols, or propositional variables. Typical elements are denoted
>
> $$
> p,q,r,A_0,A_1,\dots.
> $$
>
> Atoms have no internal syntactic structure at the propositional level.

Fix a classical propositional connective signature. For the Boolean algebraic development, the minimal convenient signature is

$$
\Omega_{BA}=\{\neg,\wedge,\vee,\top,\bot\},
$$

with arities

$$
\operatorname{ar}(\neg)=1,
$$

$$
\operatorname{ar}(\wedge)=\operatorname{ar}(\vee)=2,
$$

and

$$
\operatorname{ar}(\top)=\operatorname{ar}(\bot)=0.
$$

One may also use the expanded propositional signature

$$
\Omega_{PL}=\{\neg,\wedge,\vee,\to,\leftrightarrow,\top,\bot\},
$$

where

$$
\operatorname{ar}(\to)=\operatorname{ar}(\leftrightarrow)=2.
$$

The connectives $\to$ and $\leftrightarrow$ are definitional expansions of the Boolean signature, because classically

$$
\alpha\to\beta\equiv \neg\alpha\vee\beta,
$$

and

$$
\alpha\leftrightarrow\beta\equiv(\alpha\wedge\beta)\vee(\neg\alpha\wedge\neg\beta).
$$

> [!remark] Primitive versus derived connectives
> It is harmless to include $\to$ and $\leftrightarrow$ as primitive raw constructors, provided they are interpreted by their classical truth tables and identified in the quotient with their Boolean definitions. For the strict Boolean-algebra theorem, the reduct to $\{\neg,\wedge,\vee,\top,\bot\}$ is the essential part.

### 1.2. Formula algebra

> [!definition] Raw formula algebra
> For an atom set $A$, the **raw formula algebra** $\mathbf{Fm}(A)$ is the absolutely free $\Omega_{PL}$-algebra on $A$. Its carrier $Fm(A)$ is the set of propositional formulas over $A$.

Equivalently, $Fm(A)$ is generated by the clauses:

1. if $a\in A$, then $a\in Fm(A)$;
2. $\top,\bot\in Fm(A)$;
3. if $\varphi\in Fm(A)$, then $\neg\varphi\in Fm(A)$;
4. if $\varphi,\psi\in Fm(A)$ and $\circ\in\{\wedge,\vee,\to,\leftrightarrow\}$, then $(\varphi\circ\psi)\in Fm(A)$.

The algebra operations are the formal constructors:

$$
\neg^{\mathbf{Fm}}(\varphi)=\neg\varphi,
$$

$$
\wedge^{\mathbf{Fm}}(\varphi,\psi)=(\varphi\wedge\psi),
$$

and similarly for $\vee,\to,\leftrightarrow,\top,\bot$.

Raw formula equality is literal syntactic equality. Therefore

$$
(p\wedge q)\neq(q\wedge p)
$$

inside $Fm(A)$ unless the chosen concrete representation literally makes them the same object, which it should not.

> [!warning] Raw formulas do not yet satisfy Boolean laws
> The raw formula algebra is absolutely free as syntax. It does not satisfy commutativity, associativity, De Morgan laws, excluded middle, absorption, or distributivity as equations. Those laws appear only after quotienting by tautological equivalence.

### 1.3. Universal mapping property

> [!theorem] Freeness of raw formula syntax
> Let $\mathbf B$ be any $\Omega_{PL}$-algebra and let $g:A\to B$ be any function. Then there exists a unique $\Omega_{PL}$-homomorphism
>
> $$
> \widehat g:\mathbf{Fm}(A)\to\mathbf B
> $$
>
> satisfying
>
> $$
> \widehat g(a)=g(a)
> \qquad(a\in A).
> $$

> [!proof-sketch]
> Define $\widehat g$ by structural recursion on formulas. On atoms use $g$. On constants use the corresponding nullary operations of $\mathbf B$. On compound formulas commute with the relevant connective interpretation in $\mathbf B$. Unique readability of raw formulas gives well-definedness; structural induction gives uniqueness.

This theorem is the engine behind both substitution and truth-value evaluation.

---

## 2. Truth assignments and tautological equivalence

### 2.1. The two-element algebra

Let

$$
\mathbf 2=(\{0,1\},\neg,\wedge,\vee,\top,\bot)
$$

be the two-element Boolean algebra. Interpret

$$
\top^{\mathbf 2}=1,
\qquad
\bot^{\mathbf 2}=0,
$$

and use the usual Boolean operations. If $\to$ and $\leftrightarrow$ are primitive, define

$$
a\to b:=\neg a\vee b,
$$

and

$$
a\leftrightarrow b:=(a\wedge b)\vee(\neg a\wedge\neg b).
$$

Thus $\mathbf 2$ is an $\Omega_{PL}$-algebra.

### 2.2. Truth assignments

> [!definition] Truth assignment
> A **truth assignment** on an atom set $A$ is a function
>
> $$
> v:A\to 2.
> $$

By freeness, $v$ extends uniquely to a homomorphism

$$
\operatorname{val}_v:\mathbf{Fm}(A)\to\mathbf 2.
$$

This is ordinary truth-table evaluation.

Explicitly:

$$
\operatorname{val}_v(a)=v(a),
$$

$$
\operatorname{val}_v(\neg\varphi)=\neg\operatorname{val}_v(\varphi),
$$

$$
\operatorname{val}_v(\varphi\wedge\psi)=
\operatorname{val}_v(\varphi)\wedge\operatorname{val}_v(\psi),
$$

and similarly for the other connectives.

### 2.3. Finite support

> [!definition] Support
> The **support** of a formula $\varphi\in Fm(A)$ is the finite set
>
> $$
> \operatorname{supp}(\varphi)\subseteq A
> $$
>
> of atoms occurring in $\varphi$.

> [!lemma] Finite support
> Every formula has finite support.

> [!proof-sketch]
> Induct on formula formation. Atomic formulas have singleton support, constants have empty support, unary connectives preserve support, and binary connectives take finite unions of supports.

> [!proposition] Evaluation depends only on support
> If $v,w:A\to2$ agree on $\operatorname{supp}(\varphi)$, then
>
> $$
> \operatorname{val}_v(\varphi)=\operatorname{val}_w(\varphi).
> $$

> [!proof-sketch]
> Induct on $\varphi$. Every recursive evaluation clause only uses the values of immediate subformulas, whose supports are contained in the support of the whole formula.

### 2.4. Tautologies

> [!definition] Tautology
> A formula $\varphi\in Fm(A)$ is a **tautology** if
>
> $$
> \operatorname{val}_v(\varphi)=1
> $$
>
> for every truth assignment $v:A\to2$.

> [!definition] Tautological equivalence
> For $\varphi,\psi\in Fm(A)$, define
>
> $$
> \varphi\equiv_{\mathrm{taut}}\psi
> $$
>
> iff for every $v:A\to2$,
>
> $$
> \operatorname{val}_v(\varphi)=\operatorname{val}_v(\psi).
> $$

Equivalently, if $\leftrightarrow$ is available,

$$
\varphi\equiv_{\mathrm{taut}}\psi
\quad\Longleftrightarrow\quad
\varphi\leftrightarrow\psi\text{ is a tautology}.
$$

### 2.5. Kernel description

For each truth assignment $v:A\to2$, the evaluation map has kernel

$$
\ker(\operatorname{val}_v)
=
\{(\varphi,\psi):\operatorname{val}_v(\varphi)=\operatorname{val}_v(\psi)\}.
$$

Then

$$
\equiv_{\mathrm{taut}}
=
\bigcap_{v:A\to2}\ker(\operatorname{val}_v).
$$

> [!proposition] Tautological equivalence is a congruence
> The relation $\equiv_{\mathrm{taut}}$ is a congruence on $\mathbf{Fm}(A)$.

> [!proof-sketch]
> Each $\ker(\operatorname{val}_v)$ is a congruence because $\operatorname{val}_v$ is a homomorphism. Intersections of congruences are congruences. Hence $\equiv_{\mathrm{taut}}$ is a congruence.

This congruence is the algebraic form of classical truth-functional equality.

---

## 3. The Lindenbaum-Tarski algebra

### 3.1. Quotient by tautological equivalence

> [!definition] Lindenbaum-Tarski algebra of propositional logic
> For an atom set $A$, define
>
> $$
> LT(A):=Fm(A)/{\equiv_{\mathrm{taut}}}.
> $$
>
> The equivalence class of $\varphi$ is denoted
>
> $$
> [\varphi].
> $$

Because $\equiv_{\mathrm{taut}}$ is a congruence, all connectives descend to operations on equivalence classes:

$$
\neg[\varphi]=[\neg\varphi],
$$

$$
[\varphi]\wedge[\psi]=[\varphi\wedge\psi],
$$

$$
[\varphi]\vee[\psi]=[\varphi\vee\psi],
$$

and similarly for any primitive expanded connectives.

The quotient projection is

$$
\pi_A:Fm(A)\to LT(A),
\qquad
\pi_A(\varphi)=[\varphi].
$$

It is a surjective homomorphism and

$$
\ker(\pi_A)=\equiv_{\mathrm{taut}}.
$$

### 3.2. Boolean algebra structure

> [!theorem] $LT(A)$ is a Boolean algebra
> The reduct
>
> $$
> (LT(A),\wedge,\vee,\neg,\top,\bot)
> $$
>
> is a Boolean algebra.

> [!proof-sketch]
> Each Boolean algebra identity is valid under every truth assignment. For example, commutativity of meet follows because
>
> $$
> \varphi\wedge\psi\equiv_{\mathrm{taut}}\psi\wedge\varphi.
> $$
>
> Similarly excluded middle, contradiction, associativity, absorption, distributivity, and De Morgan laws are tautological equivalences. Since equality in the quotient is tautological equivalence, the identities hold in $LT(A)$.

### 3.3. The free Boolean algebra theorem

> [!theorem] Free Boolean algebra theorem
> The pair
>
> $$
> (LT(A),\iota_A)
> $$
>
> where
>
> $$
> \iota_A:A\to LT(A),
> \qquad
> \iota_A(a)=[a],
> $$
>
> is the free Boolean algebra on $A$. That is, for every Boolean algebra $\mathbf B$ and every function $g:A\to B$, there exists a unique Boolean homomorphism
>
> $$
> \overline g:LT(A)\to B
> $$
>
> such that
>
> $$
> \overline g([a])=g(a)
> \qquad(a\in A).
> $$

> [!proof-sketch]
> First extend $g:A\to B$ to a raw formula homomorphism
>
> $$
> \widehat g:Fm(A)\to B
> $$
>
> by structural recursion. If $\varphi\equiv_{\mathrm{taut}}\psi$, then $\widehat g(\varphi)=\widehat g(\psi)$ in every Boolean algebra. This follows by disjunctive normal form: tautologically equivalent formulas have the same truth table over their finite support, hence the same Boolean term function. Therefore $\equiv_{\mathrm{taut}}\subseteq\ker(\widehat g)$, so $\widehat g$ descends uniquely through the quotient. Define
>
> $$
> \overline g([\varphi])=\widehat g(\varphi).
> $$
>
> This is a Boolean homomorphism extending $g$. Uniqueness follows because any Boolean homomorphism $h:LT(A)\to B$ extending $g$ gives $h\circ\pi_A:Fm(A)\to B$, a raw homomorphism extending $g$, hence equal to $\widehat g$ by freeness of raw formulas. Since $\pi_A$ is surjective, $h=\overline g$.

Thus:

$$
\boxed{
LT(A)=Fm(A)/{\equiv_{\mathrm{taut}}}
\text{ is the free Boolean algebra on }A.
}
$$

### 3.4. Order as entailment

Every Boolean algebra has a natural order:

$$
x\le y
\quad\Longleftrightarrow\quad
x\wedge y=x.
$$

In $LT(A)$ this order is semantic entailment.

> [!proposition] Boolean order equals propositional entailment
> For formulas $\varphi,\psi\in Fm(A)$,
>
> $$
> [\varphi]\le[\psi]
> $$
>
> iff every truth assignment that makes $\varphi$ true also makes $\psi$ true.

> [!proof-sketch]
> $[\varphi]\le[\psi]$ iff $[\varphi]\wedge[\psi]=[\varphi]$, iff $\varphi\wedge\psi\equiv_{\mathrm{taut}}\varphi$. This says exactly that, under every truth assignment, whenever $\varphi$ has value $1$, so does $\psi$.

Equivalently,

$$
[\varphi]\le[\psi]
\quad\Longleftrightarrow\quad
[\varphi\to\psi]=\top.
$$

---

## 4. Substitutions

### 4.1. Raw substitutions

> [!definition] Formula substitution
> Let $A,B$ be atom sets. A **formula substitution** from $A$ to $B$ is a function
>
> $$
> \sigma:A\to Fm(B).
> $$

By freeness, $\sigma$ extends uniquely to a homomorphism

$$
\widehat\sigma:Fm(A)\to Fm(B).
$$

It satisfies

$$
\widehat\sigma(a)=\sigma(a),
$$

$$
\widehat\sigma(\neg\varphi)=\neg\widehat\sigma(\varphi),
$$

$$
\widehat\sigma(\varphi\wedge\psi)=
\widehat\sigma(\varphi)\wedge\widehat\sigma(\psi),
$$

and similarly for all connectives.

This is ordinary simultaneous substitution.

### 4.2. Substitution-evaluation lemma

Let

$$
\sigma:A\to Fm(B)
$$

be a substitution and let

$$
v:B\to2
$$

be a truth assignment. Define

$$
v_\sigma:A\to2
$$

by

$$
v_\sigma(a):=\operatorname{val}_v(\sigma(a)).
$$

> [!theorem] Substitution-evaluation lemma
> For every $\varphi\in Fm(A)$,
>
> $$
> \operatorname{val}_v(\widehat\sigma(\varphi))
> =
> \operatorname{val}_{v_\sigma}(\varphi).
> $$

> [!proof-sketch]
> Induct on $\varphi$. The atomic case is exactly the definition of $v_\sigma$. The connective cases follow because both sides evaluate connectives homomorphically in $\mathbf 2$.

Diagrammatically:

$$
\begin{array}{ccc}
Fm(A) & \xrightarrow{\widehat\sigma} & Fm(B) \\
\operatorname{val}_{v_\sigma}\downarrow & & \downarrow\operatorname{val}_v \\
2 & = & 2
\end{array}
$$

The slogan is:

$$
\boxed{
\text{substitution before evaluation equals evaluation under the pulled-back truth assignment.}
}
$$

### 4.3. Tautologies are closed under substitution

> [!theorem] Substitution preserves tautologies
> If $\varphi\in Fm(A)$ is a tautology and $\sigma:A\to Fm(B)$ is any substitution, then $\widehat\sigma(\varphi)$ is a tautology in $Fm(B)$.

> [!proof-sketch]
> Let $v:B\to2$ be arbitrary. By the substitution-evaluation lemma,
>
> $$
> \operatorname{val}_v(\widehat\sigma(\varphi))
> =
> \operatorname{val}_{v_\sigma}(\varphi).
> $$
>
> Since $\varphi$ is tautological, the right side is $1$. Hence the substituted formula evaluates to $1$ under every $v$.

### 4.4. Substitutions descend to quotient homomorphisms

> [!theorem] Substitution respects tautological equivalence
> If
>
> $$
> \varphi\equiv_{\mathrm{taut}}\psi,
> $$
>
> then
>
> $$
> \widehat\sigma(\varphi)\equiv_{\mathrm{taut}}\widehat\sigma(\psi).
> $$

> [!proof-sketch]
> For any $v:B\to2$, use the substitution-evaluation lemma:
>
> $$
> \operatorname{val}_v(\widehat\sigma(\varphi))
> =\operatorname{val}_{v_\sigma}(\varphi)
> =\operatorname{val}_{v_\sigma}(\psi)
> =\operatorname{val}_v(\widehat\sigma(\psi)).
> $$

Therefore $\widehat\sigma$ descends to a Boolean homomorphism

$$
\overline\sigma:LT(A)\to LT(B)
$$

given by

$$
\overline\sigma([\varphi])=[\widehat\sigma(\varphi)].
$$

Thus substitutions are not merely syntactic conveniences; they are Boolean homomorphisms between free Boolean algebras after quotienting.

---

## 5. Contexts

### 5.1. Hole sets

For each $n<\omega$, fix a finite set of hole symbols

$$
H_n=\{\Box_0,\dots,\Box_{n-1}\}.
$$

The holes are treated exactly like propositional atoms at the raw syntax level. Their special role is not in formula formation, but in how we later fill them.

### 5.2. Pure contexts

> [!definition] Pure context
> A **pure $n$-hole propositional context** is a formula
>
> $$
> C\in Fm(H_n).
> $$

Example:

$$
C(\Box_0,\Box_1)
=
(\Box_0\wedge\Box_1)\leftrightarrow(\Box_1\wedge\Box_0).
$$

Given formulas $\alpha_0,\dots,\alpha_{n-1}\in Fm(P)$, define the filling substitution

$$
\sigma_C:H_n\to Fm(P)
$$

by

$$
\sigma_C(\Box_i)=\alpha_i.
$$

Then the filled context is

$$
C[\alpha_0,
\dots,
\alpha_{n-1}]
:=
\widehat{\sigma_C}(C).
$$

Thus:

$$
\boxed{
\text{filling a context is substitution by homomorphic extension.}
}
$$

### 5.3. Parameterized contexts

Pure contexts have only holes. But it is often useful to allow background parameters.

> [!definition] Parameterized context
> For an atom set $P$, define
>
> $$
> Ctx_n(P):=Fm(P\sqcup H_n).
> $$
>
> An element $C\in Ctx_n(P)$ is an **$n$-hole context over parameters $P$**.

The atoms in $P$ are treated as fixed parameters; the atoms in $H_n$ are treated as holes.

Given

$$
C\in Fm(P\sqcup H_n)
$$

and

$$
\alpha_0,
\dots,
\alpha_{n-1}\in Fm(P),
$$

define the filling substitution

$$
\sigma:P\sqcup H_n\to Fm(P)
$$

by

$$
\sigma(p)=p
\qquad(p\in P),
$$

and

$$
\sigma(\Box_i)=\alpha_i.
$$

Then

$$
C[\alpha_0,
\dots,
\alpha_{n-1}]
:=
\widehat\sigma(C).
$$

Pure contexts are the special case $P=\varnothing$.

### 5.4. Contexts as operations

Every context induces an operation.

If

$$
C\in Ctx_n(P),
$$

then

$$
C[-]:Fm(P)^n\to Fm(P)
$$

is defined by

$$
(\alpha_0,
\dots,
\alpha_{n-1})
\mapsto
C[\alpha_0,
\dots,
\alpha_{n-1}].
$$

For example,

$$
C(\Box_0,
\Box_1)=\Box_0\wedge\Box_1
$$

induces

$$
(\alpha,
\beta)
\mapsto
\alpha\wedge\beta.
$$

A more complicated context induces a more complicated fixed-shape operation.

> [!remark] Contexts are polynomial operations
> In universal-algebra language, contexts are syntax polynomial operations: terms or formulas over ordinary parameters and distinguished hole variables. Filling the holes is the corresponding polynomial operation on the formula algebra.

---

## 6. Quotient contexts and Boolean polynomial operations

### 6.1. Quotient context algebra

Since contexts are formulas over $P\sqcup H_n$, their quotient classes live in

$$
LT(P\sqcup H_n).
$$

> [!definition] Quotient contexts
> Define
>
> $$
> QCtx_n(P):=LT(P\sqcup H_n).
> $$
>
> An element of $QCtx_n(P)$ is a context modulo tautological equivalence.

Raw contexts are syntactic templates. Quotient contexts are Boolean polynomial operations with parameters.

### 6.2. Action on quotient formulas

Given

$$
[C]\in QCtx_n(P)
$$

and

$$
[\alpha_0],
\dots,
[\alpha_{n-1}]\in LT(P),
$$

define

$$
[C]([\alpha_0],
\dots,
[\alpha_{n-1}])
:=
[C[\alpha_0,
\dots,
\alpha_{n-1}]].
$$

> [!proposition] Well-definedness of quotient context action
> The displayed operation is independent of all representatives.

> [!proof-sketch]
> If $C\equiv_{\mathrm{taut}}C'$ and $\alpha_i\equiv_{\mathrm{taut}}\alpha_i'$ for each $i$, substitution-stability of tautological equivalence gives
>
> $$
> C[\alpha_0,
> \dots,
> \alpha_{n-1}]
> \equiv_{\mathrm{taut}}
> C'[\alpha_0',
> \dots,
> \alpha_{n-1}'].
> $$

Thus every quotient context induces a genuine operation

$$
LT(P)^n\to LT(P).
$$

### 6.3. Tautological contexts

> [!definition] Tautological context
> A pure context $C\in Fm(H_n)$ is **tautological** if
>
> $$
> [C]=\top
> $$
>
> in $LT(H_n)$.

Equivalently, $C$ evaluates to $1$ under every truth assignment $H_n\to2$.

> [!theorem] Tautological contexts produce tautological instances
> If $C\in Fm(H_n)$ satisfies $[C]=\top$ in $LT(H_n)$, then for every atom set $P$ and every tuple $\alpha_0,
> \dots,
> \alpha_{n-1}\in Fm(P)$,
>
> $$
> C[\alpha_0,
> \dots,
> \alpha_{n-1}]
> $$
>
> is a tautology.

> [!proof-sketch]
> Filling induces a Boolean homomorphism
>
> $$
> LT(H_n)\to LT(P).
> $$
>
> Boolean homomorphisms preserve $\top$. Hence $[C]=\top$ maps to
>
> $$
> [C[\alpha_0,
> \dots,
> \alpha_{n-1}]]=\top.
> $$

Therefore:

$$
\boxed{
\text{tautological schemas are precisely top-valued pure quotient contexts.}
}
$$

### 6.4. Examples

**Commutativity of conjunction:**

$$
C(\Box_0,
\Box_1)
=
(\Box_0\wedge\Box_1)\leftrightarrow(\Box_1\wedge\Box_0).
$$

Then

$$
[C]=\top\in LT(H_2),
$$

so every instance

$$
(\alpha\wedge\beta)\leftrightarrow(\beta\wedge\alpha)
$$

is tautological.

**Exportation:**

$$
C(\Box_0,
\Box_1,
\Box_2)
=
((\Box_0\wedge\Box_1)\to\Box_2)
\leftrightarrow
(\Box_0\to(\Box_1\to\Box_2)).
$$

Again $[C]=\top$, so all formula fillings are tautologies.

**Contraposition:**

$$
C(\Box_0,
\Box_1)
=
(\Box_0\to\Box_1)
\leftrightarrow
(\neg\Box_1\to\neg\Box_0).
$$

This context is top-valued in $LT(H_2)$.

---

## 7. The Boolean clone of quotient contexts

### 7.1. Pure quotient contexts by arity

Define

$$
\mathsf{BoolCtx}(n):=LT(H_n).
$$

Elements of $\mathsf{BoolCtx}(n)$ are $n$-ary Boolean term operations, represented syntactically by formulas in $n$ holes modulo tautological equivalence.

There are projection contexts

$$
\pi_i^{(n)}:=[\Box_i]\in LT(H_n).
$$

### 7.2. Composition of contexts

Let

$$
[C]\in LT(H_n)
$$

and

$$
[D_0],
\dots,
[D_{n-1}]\in LT(H_m).
$$

Define the composite

$$
[C]\circ([D_0],
\dots,
[D_{n-1}])
\in LT(H_m)
$$

by

$$
[C]\circ([D_0],
\dots,
[D_{n-1}])
:=
[C[D_0,
\dots,
D_{n-1}]].
$$

This is well-defined because substitution descends to the quotient.

> [!theorem] Boolean context clone
> The family
>
> $$
> (\mathsf{BoolCtx}(n))_{n<\omega}
> $$
>
> with projections and the above composition is a clone. It is the clone of Boolean term operations.

> [!proof-sketch]
> Projection laws follow from filling a hole by the corresponding input context. Associativity follows from associativity of substitution: filling $C$ by the $D_i$ and then filling each $D_i$ by $E_j$ gives the same result as first filling each $D_i$ by the $E_j$ and then filling $C$. All equalities are taken in the quotient, where substitution is well-defined.

This is the most compact algebraic object encoding propositional logic modulo tautologies:

$$
\boxed{
\text{propositional logic modulo tautologies}=	ext{the Boolean clone of quotient contexts}.
}
$$

### 7.3. Tautological schemas as top elements in the clone

A tautological $n$-schema is an element

$$
[C]\in\mathsf{BoolCtx}(n)
$$

such that

$$
[C]=\top.
$$

Its induced operation on any $LT(P)$ is the constant-top operation:

$$
([\alpha_0],
\dots,
[\alpha_{n-1}])
\mapsto
\top.
$$

Thus complicated tautologies are not separate mechanisms. They are simply more complicated elements of the Boolean context clone that happen to equal $\top$.

---

## 8. Schema operators beyond contexts

### 8.1. Why contexts are not enough

Contexts have fixed shape. Many useful formula transformations do not.

Examples:

$$
\varphi\mapsto CNF(\varphi),
$$

$$
\varphi\mapsto DNF(\varphi),
$$

$$
\varphi\mapsto \varphi^*,
$$

$$
\varphi\mapsto \varphi[A:=\top]\vee\varphi[A:=\bot].
$$

These inspect the input formula and recursively or semantically determine a new formula.

So we introduce a broader notion.

> [!definition] Schema operator
> A **schema operator** is a partial or total function
>
> $$
> S:D\to Fm(P)
> $$
>
> whose domain $D$ is a syntactically specified class of data, and whose values are formulas, built from allowed operations such as context filling, substitutions, recursive transforms, quotient-level operations, and side conditions.

Contexts are a source of schema operators, but not all schema operators are contexts.

### 8.2. Context schema operators

Every context

$$
C\in Fm(H_n)
$$

induces

$$
S_C:Fm(P)^n\to Fm(P)
$$

by

$$
S_C(\alpha_0,
\dots,
\alpha_{n-1})=C[\alpha_0,
\dots,
\alpha_{n-1}].
$$

If $C$ is tautological, the image of $S_C$ consists entirely of tautologies.

### 8.3. Substitution schema operators

A substitution

$$
\sigma:P\to Fm(Q)
$$

induces

$$
S_\sigma:Fm(P)\to Fm(Q)
$$

by

$$
S_\sigma(\varphi)=\widehat\sigma(\varphi).
$$

This is not an ordinary one-hole context in general. It recursively acts on every atom occurrence in $\varphi$.

### 8.4. Recursive syntax transforms

A recursive syntax transform is defined by clauses on formula constructors. For example, duality may be given by

$$
p^*=\neg p,
$$

$$
(\neg\alpha)^*=\neg(\alpha^*),
$$

$$
(\alpha\wedge\beta)^*=\alpha^*\vee\beta^*,
$$

$$
(\alpha\vee\beta)^*=\alpha^*\wedge\beta^*.
$$

This is a formula operator. It is not a fixed context.

### 8.5. Normal-form operators

A normal-form operator is a representative-selection function

$$
N:Fm(P)\to Fm(P)
$$

such that

$$
N(\varphi)\equiv_{\mathrm{taut}}\varphi.
$$

At the quotient level,

$$
[N(\varphi)]=[\varphi].
$$

Normal forms choose syntactic representatives of quotient classes. They are not context operations because their output shape depends on the truth table or recursive structure of the input formula.

---

## 9. Normal forms as quotient representatives

### 9.1. Minterms and DNF

Let $S=\{p_1,
\dots,
p_n\}\subseteq P$ be finite. For a truth assignment

$$
\epsilon:S\to2,
$$

define the minterm

$$
m_\epsilon
=
\bigwedge_{i=1}^n \ell_i,
$$

where

$$
\ell_i=
\begin{cases}
p_i,&\epsilon(p_i)=1,\\
\neg p_i,&\epsilon(p_i)=0.
\end{cases}
$$

Then $m_\epsilon$ is true exactly on the truth-table row $\epsilon$.

> [!theorem] Disjunctive normal form
> Every formula $\varphi$ with support contained in finite $S$ is tautologically equivalent to
>
> $$
> \bigvee_{\epsilon:S\to2,\ \operatorname{val}_\epsilon(\varphi)=1}m_\epsilon.
> $$
>
> If no row satisfies $\varphi$, the empty disjunction is $\bot$.

> [!proof-sketch]
> Under any row $\delta:S\to2$, exactly one minterm $m_\delta$ is true. Therefore the displayed disjunction is true exactly on the rows where $\varphi$ is true.

Thus $DNF(\varphi)$ is a representative of $[\varphi]$.

### 9.2. Maxterms and CNF

For a row $\epsilon:S\to2$, define the maxterm $M_\epsilon$ that is false exactly on $\epsilon$. Let

$$
M_\epsilon
=
\bigvee_{i=1}^n k_i,
$$

where

$$
k_i=
\begin{cases}
\neg p_i,&\epsilon(p_i)=1,\\
p_i,&\epsilon(p_i)=0.
\end{cases}
$$

Then $M_\epsilon$ is false exactly when the assignment is $\epsilon$.

> [!theorem] Conjunctive normal form
> Every formula $\varphi$ with support contained in finite $S$ is tautologically equivalent to
>
> $$
> \bigwedge_{\epsilon:S\to2,\ \operatorname{val}_\epsilon(\varphi)=0}M_\epsilon.
> $$
>
> If no row falsifies $\varphi$, the empty conjunction is $\top$.

> [!proof-sketch]
> A conjunction of maxterms is true exactly on the rows excluded by none of the maxterms. Since each falsifying row of $\varphi$ contributes its own maxterm, the conjunction is true exactly where $\varphi$ is true.

### 9.3. Normal forms are not contexts

There is no fixed one-hole context $C(\Box)$ such that

$$
C[\varphi]=DNF(\varphi)
$$

for every formula $\varphi$. The size and shape of $DNF(\varphi)$ depend on the finite support and truth table of $\varphi$.

Therefore:

$$
\boxed{
\text{normal forms are quotient representative choices, not contexts.}
}
$$

---

## 10. Duality

### 10.1. Recursive definition

For formulas using $\neg,\wedge,\vee$, define the dual transform recursively by

$$
p^*=\neg p,
$$

$$
\top^*=\bot,
\qquad
\bot^*=\top,
$$

$$
(\neg\alpha)^*=\neg(\alpha^*),
$$

$$
(\alpha\wedge\beta)^*=\alpha^*\vee\beta^*,
$$

$$
(\alpha\vee\beta)^*=\alpha^*\wedge\beta^*.
$$

This is a recursive syntax transformation.

### 10.2. Quotient meaning

> [!theorem] Duality realizes complementation
> For every formula $\alpha$,
>
> $$
> [\alpha^*]=\neg[\alpha]
> $$
>
> in $LT(P)$.

> [!proof-sketch]
> Induct on $\alpha$. The atomic case gives $[p^*]=[\neg p]=\neg[p]$. The Boolean constants are immediate. The negation step uses double negation in the quotient. The binary steps use De Morgan laws:
>
> $$
> \neg(a\wedge b)=\neg a\vee\neg b,
> $$
>
> and
>
> $$
> \neg(a\vee b)=\neg a\wedge\neg b.
> $$

Duality is not a Boolean homomorphism. Complementation reverses meet and join. It is a De Morgan anti-automorphism at the quotient level.

Thus:

$$
\boxed{
\text{duality is a recursive syntax transform whose quotient effect is Boolean complement.}
}
$$

---

## 11. Variable elimination and propositional projection

### 11.1. Substituting truth constants

Fix $A\in P$. Define substitutions

$$
\sigma_A^\top:P\to Fm(P)
$$

by

$$
\sigma_A^\top(A)=\top,
\qquad
\sigma_A^\top(p)=p\quad(p\neq A),
$$

and

$$
\sigma_A^\bot:P\to Fm(P)
$$

by

$$
\sigma_A^\bot(A)=\bot,
\qquad
\sigma_A^\bot(p)=p\quad(p\neq A).
$$

Let

$$
\varphi[A:=\top]:=\widehat{\sigma_A^\top}(\varphi),
$$

and

$$
\varphi[A:=\bot]:=\widehat{\sigma_A^\bot}(\varphi).
$$

### 11.2. Existential projection

Define

$$
\exists_A\varphi
:=
\varphi[A:=\top]\vee\varphi[A:=\bot].
$$

At the quotient level,

$$
\exists_A[\varphi]
:=
[\varphi[A:=\top]]\vee[\varphi[A:=\bot]].
$$

This is well-defined because substitutions descend to the quotient.

The construction decomposes as:

1. substitute $A:=\top$;
2. substitute $A:=\bot$;
3. combine by the binary disjunction context.

Thus variable elimination is built from substitutions plus a fixed context, but it is not itself a single ordinary context in $\varphi$.

### 11.3. Strongest variable-free consequence

Let $LT(P\setminus\{A\})$ be identified with the subalgebra of $LT(P)$ represented by formulas not involving $A$.

> [!theorem] Existential projection is strongest $A$-free consequence
> For $a\in LT(P)$ and $b\in LT(P\setminus\{A\})$,
>
> $$
> \exists_A(a)\le b
> \quad\Longleftrightarrow\quad
> a\le b.
> $$

> [!proof-sketch]
> Work by truth sets. The element $a$ defines a subset of $2^P$. The element $\exists_A(a)$ defines the projection of that subset along the $A$-coordinate, pulled back to $2^P$. If $b$ does not depend on $A$, then containing $a$ is equivalent to containing its projection. Translating containment of truth sets into Boolean order gives the equivalence.

Therefore $\exists_A(a)$ is the least $A$-free element above $a$, i.e. the strongest $A$-free consequence of $a$ in the entailment order.

> [!warning] $\exists_A$ is not a Boolean homomorphism
> The operation $\exists_A$ preserves joins and $\bot$, but it does not generally preserve meets or complements. It is a projection/quantifier-like operator, not a Boolean-algebra homomorphism.

### 11.4. Universal projection

Define the dual operation

$$
\forall_A[\varphi]
:=
[\varphi[A:=\top]]\wedge[\varphi[A:=\bot]].
$$

This gives the greatest $A$-free element below $[\varphi]$.

Equivalently, $\forall_A$ is right adjoint to the inclusion of the $A$-free subalgebra.

---

## 12. Interpolation through variable elimination

### 12.1. Entailment form

Suppose

$$
\alpha\models\beta.
$$

Equivalently,

$$
[\alpha]\le[\beta]
$$

in $LT(P)$.

Craig interpolation for propositional logic says that there exists a formula $\gamma$ using only the atoms common to $\alpha$ and $\beta$ such that

$$
\alpha\models\gamma
$$

and

$$
\gamma\models\beta.
$$

Equivalently,

$$
[\alpha]\le[\gamma]\le[\beta].
$$

### 12.2. Eliminating variables not in the conclusion

If $A$ occurs in $\alpha$ but not in $\beta$, replace $[\alpha]$ by

$$
\exists_A[\alpha].
$$

Because $[\alpha]\le\exists_A[\alpha]$, we have

$$
\alpha\models\exists_A\alpha.
$$

Because $[\beta]$ is $A$-free and $[\alpha]\le[\beta]$, the adjunction gives

$$
\exists_A[\alpha]\le[\beta].
$$

Therefore

$$
\exists_A\alpha\models\beta.
$$

Repeating this for all atoms occurring in $\alpha$ but not in $\beta$ produces an interpolant whose support is contained in

$$
\operatorname{supp}(\alpha)\cap\operatorname{supp}(\beta).
$$

> [!theorem] Propositional interpolation by elimination
> If $\alpha\models\beta$, then there exists $\gamma$ with
>
> $$
> \operatorname{supp}(\gamma)\subseteq
> \operatorname{supp}(\alpha)\cap\operatorname{supp}(\beta)
> $$
>
> such that
>
> $$
> \alpha\models\gamma\models\beta.
> $$

> [!proof-sketch]
> Starting from $[\alpha]$, repeatedly apply $\exists_A$ to variables $A$ appearing in $\alpha$ but not in $\beta$. Each step moves upward from $[\alpha]$ while remaining below $[\beta]$ because $[\beta]$ is free of the eliminated variable. The resulting class has support only among variables common to $\alpha$ and $\beta$. Choose any formula representative $\gamma$.

This shows that variable elimination is not an isolated trick; it is an algebraic projection mechanism powering interpolation.

---

## 13. Deductive closure and filters

### 13.1. Deductions from tautologies and modus ponens

A Hilbert-style propositional deduction from assumptions $\Sigma\subseteq Fm(P)$ is usually a finite sequence

$$
\langle\alpha_0,
\dots,
\alpha_n\rangle
$$

where each line is either:

1. a member of $\Sigma$;
2. a tautology or axiom-schema instance;
3. obtained from earlier lines by modus ponens.

This is a generated-closure construction:

$$
\operatorname{Ded}(\Sigma)
=
\operatorname{Cl}_{MP}(\Sigma\cup\operatorname{Taut}).
$$

Unlike formula syntax, proofs are not freely generated. A formula may have many proofs.

### 13.2. Algebraic filter semantics

In a Boolean algebra, a filter is an upward-closed meet-closed subset.

> [!definition] Filter generated by assumptions
> For $\Sigma\subseteq Fm(P)$, define the filter generated by $[\Sigma]$ in $LT(P)$ as
>
> $$
> \operatorname{Filt}([\Sigma])
> =
> \{b\in LT(P):[\sigma_1]\wedge\cdots\wedge[\sigma_n]\le b
> \text{ for some }\sigma_1,
> \dots,
> \sigma_n\in\Sigma\}.
> $$

Then

$$
[\varphi]\in\operatorname{Filt}([\Sigma])
$$

means that finitely many assumptions from $\Sigma$ entail $\varphi$ propositionally.

Thus the algebraic form of finite-premise consequence is:

$$
\Sigma\models\varphi
\quad\Longleftrightarrow\quad
[\varphi]\in\operatorname{Filt}([\Sigma]).
$$

This is the quotient-algebraic version of propositional deductive closure.

---

## 14. Instantiating the propositional skeleton in first-order logic

### 14.1. First-order formulas as target fillers

Let $\mathcal L$ be a first-order language and let

$$
Form_{\mathcal L}
$$

be the set of first-order formulas.

The propositional connectives $\neg,\wedge,\vee,\to,\leftrightarrow$ operate on first-order formulas. Therefore $Form_{\mathcal L}$ carries at least the structure needed to interpret propositional contexts.

A pure propositional context

$$
C\in Fm(H_n)
$$

can be filled by first-order formulas

$$
\varphi_0,
\dots,
\varphi_{n-1}\in Form_{\mathcal L}.
$$

The result is the first-order formula

$$
C[\varphi_0,
\dots,
\varphi_{n-1}].
$$

### 14.2. Propositional tautology schema inside FOL

> [!definition] FOL instances of propositional tautologies
> Define
>
> $$
> \operatorname{PropTaut}_{\mathcal L}
> :=
> \{C[\varphi_0,
> \dots,
> \varphi_{n-1}]
> :
> n<\omega,
> C\in Fm(H_n),
> [C]=\top\in LT(H_n),
> \varphi_i\in Form_{\mathcal L}
> \}.
> $$

This is the exact formal version of:

> all substitution instances of propositional tautologies are first-order logical axioms.

No informal schema notation is needed. The schema is a top-valued quotient context, and an instance is context filling by first-order formulas.

### 14.3. Validity of FOL propositional instances

> [!theorem] Propositional tautology instances are FOL-valid
> If
>
> $$
> \theta\in \operatorname{PropTaut}_{\mathcal L},
> $$
>
> then
>
> $$
> \models_{FOL}\theta.
> $$

> [!proof-sketch]
> Write
>
> $$
> \theta=C[\varphi_0,
> \dots,
> \varphi_{n-1}]
> $$
>
> where $[C]=\top$ in $LT(H_n)$. Let $\mathcal M$ be any $\mathcal L$-structure and $s$ any variable assignment. Each formula $\varphi_i$ has a truth value
>
> $$
> \llbracket\varphi_i\rrbracket_{\mathcal M,s}\in2.
> $$
>
> This gives a truth assignment $v:H_n\to2$ by
>
> $$
> v(\Box_i)=\llbracket\varphi_i\rrbracket_{\mathcal M,s}.
> $$
>
> Since $C$ is tautological,
>
> $$
> \operatorname{val}_v(C)=1.
> $$
>
> But $\operatorname{val}_v(C)$ is exactly the truth value of $C[\varphi_0,
> \dots,
> \varphi_{n-1}]$ in $\mathcal M$ under $s$. Hence $\theta$ is true in every structure under every assignment.

This theorem is the formal bridge from propositional quotient contexts to first-order axiom schemas.

### 14.4. Why this matters

In first-order deductive calculi, the propositional axiom group is often written informally as:

> every tautological instance is an axiom.

The present framework replaces that with:

1. choose a finite hole set $H_n$;
2. choose a pure context $C\in Fm(H_n)$;
3. check $[C]=\top$ in $LT(H_n)$;
4. fill holes by arbitrary first-order formulas.

Thus the propositional layer is a parameterized algebraic module inserted into FOL.

---

## 15. Formal taxonomy

### 15.1. Raw objects

| Object | Meaning |
|---|---|
| $A$ | atom set |
| $Fm(A)$ | raw formula algebra over $A$ |
| $\operatorname{val}_v$ | truth evaluation induced by $v:A\to2$ |
| $\equiv_{\mathrm{taut}}$ | same truth value under every truth assignment |
| $LT(A)$ | quotient $Fm(A)/{\equiv_{\mathrm{taut}}}$ |
| $\pi_A$ | quotient projection $Fm(A)\to LT(A)$ |

### 15.2. Context objects

| Object | Meaning |
|---|---|
| $H_n$ | finite hole set $\{\Box_0,
\dots,
\Box_{n-1}\}$ |
| $Fm(H_n)$ | pure $n$-hole contexts |
| $Ctx_n(P)=Fm(P\sqcup H_n)$ | parameterized raw contexts |
| $LT(H_n)$ | pure quotient contexts / $n$-ary Boolean operations |
| $QCtx_n(P)=LT(P\sqcup H_n)$ | parameterized quotient contexts |
| $[C]=\top$ | $C$ is a tautological schema context |

### 15.3. Operators

| Operator type | Form | Meaning |
|---|---|---|
| context filling | $C[-]:Fm(P)^n\to Fm(P)$ | fixed-shape template operation |
| substitution | $\widehat\sigma:Fm(A)\to Fm(B)$ | homomorphic formula replacement |
| quotient substitution | $\overline\sigma:LT(A)\to LT(B)$ | Boolean homomorphism induced by substitution |
| normal form | $N:Fm(P)\to Fm(P)$ | representative choice with $[N\varphi]=[\varphi]$ |
| duality | $\varphi\mapsto\varphi^*$ | recursive transform realizing complement modulo tautology |
| variable elimination | $\exists_A$ | projection/strongest $A$-free consequence |
| proof closure | $\operatorname{Cl}_{MP}$ | generated closure under modus ponens |

### 15.4. Inclusion hierarchy

The hierarchy is:

$$
\boxed{
\text{fixed contexts}
\subsetneq
\text{substitution/context composites}
\subsetneq
\text{recursive schema operators}.
}
$$

Raw contexts are finite templates. Substitutions are homomorphic formula transformations. Recursive schema operators may inspect arbitrary formula structure or truth-table behavior.

---

## 16. Recommended formal definitions for a reusable module

### 16.1. Module data

A reusable propositional module should specify:

1. a connective signature $\Omega_{PL}$;
2. the free formula algebra functor $Fm(-)$;
3. truth evaluation maps $\operatorname{val}_v$;
4. tautological equivalence $\equiv_{\mathrm{taut}}$;
5. quotient Boolean algebras $LT(-)$;
6. substitution extension $\sigma\mapsto\widehat\sigma$;
7. quotient substitution $\sigma\mapsto\overline\sigma$;
8. context families $Ctx_n(P)$;
9. quotient context families $QCtx_n(P)$;
10. the Boolean context clone $\mathsf{BoolCtx}(n)=LT(H_n)$;
11. top-valued contexts as tautological schemas;
12. enriched schema operators for normal forms, duality, and variable elimination.

### 16.2. Core axioms/results of the module

The module should expose the following formal results:

1. $Fm(A)$ is absolutely free on $A$.
2. Every substitution $A\to Fm(B)$ extends uniquely to a homomorphism $Fm(A)\to Fm(B)$.
3. Truth assignments are homomorphisms $Fm(A)\to2$.
4. The substitution-evaluation square commutes.
5. Tautologies are closed under substitution.
6. Tautological equivalence is a congruence.
7. $LT(A)$ is a Boolean algebra.
8. $LT(A)$ is the free Boolean algebra on $A$.
9. Context filling is substitution on hole variables.
10. Quotient contexts act well-definedly on $LT(P)$.
11. $LT(H_n)$ forms the Boolean clone under context composition.
12. Tautological schema contexts are exactly top elements of $LT(H_n)$.
13. Every top-valued context yields valid FOL instances when holes are filled by FOL formulas.
14. Variable elimination is a quotient-level projection, not a Boolean homomorphism.
15. Normal forms are quotient representatives, not contexts.
16. Duality is a recursive transform realizing Boolean complement modulo tautology.

### 16.3. Minimal FOL interface

To instantiate this module in first-order logic, one only needs:

1. a set $Form_{\mathcal L}$ of first-order formulas;
2. propositional connective operations on $Form_{\mathcal L}$;
3. a semantics assigning each formula a truth value in each structure under each assignment.

Then every tautological context $C\in Fm(H_n)$ gives an FOL-valid schema:

$$
C[\varphi_0,
\dots,
\varphi_{n-1}].
$$

This is the clean abstract replacement for informal propositional axiom schemas.

---

## 17. Final synthesis

The system can now be summarized in one diagrammatic chain:

$$
\text{atoms }A
\longmapsto
Fm(A)
\longrightarrow
LT(A)=Fm(A)/{\equiv_{\mathrm{taut}}}
\longrightarrow
\text{Boolean polynomial operations}.
$$

Substitution is the functorial/homomorphic mechanism:

$$
\sigma:A\to Fm(B)
\quad\leadsto\quad
\widehat\sigma:Fm(A)\to Fm(B)
\quad\leadsto\quad
\overline\sigma:LT(A)\to LT(B).
$$

Contexts are formulas over holes:

$$
Ctx_n(P)=Fm(P\sqcup H_n).
$$

Quotient contexts are Boolean polynomial operations:

$$
QCtx_n(P)=LT(P\sqcup H_n).
$$

Pure quotient contexts form the Boolean clone:

$$
\mathsf{BoolCtx}(n)=LT(H_n).
$$

Tautological schemas are exactly top-valued pure contexts:

$$
[C]=\top\in LT(H_n).
$$

FOL propositional axiom instances are obtained by filling such contexts with first-order formulas:

$$
\operatorname{PropTaut}_{\mathcal L}
=
\{C[\varphi_0,
\dots,
\varphi_{n-1}]:[C]=\top\in LT(H_n)\}.
$$

The refined classification is:

$$
\boxed{
\text{ordinary context} = \text{fixed-shape formula with holes};
}
$$

$$
\boxed{
\text{substitution} = \text{homomorphic extension of generator assignment};
}
$$

$$
\boxed{
\text{schema operator} = \text{possibly recursive formula transformation};
}
$$

$$
\boxed{
\text{tautological schema} = \text{top-valued quotient context}.
}
$$

This is the fully syntactic, parameterized skeleton of classical propositional logic modulo tautological equivalence. It is independent of first-order logic, but it is designed to plug into first-order logic by treating first-order formulas as admissible fillings for propositional holes.

---

## 18. Concrete schema records

### 18.1. Why a schema record is useful

The preceding sections identify tautological schemas with top-valued quotient contexts. That is mathematically clean, but if one wants to build a formal note system, proof checker, parser, or elaborator, it is useful to package a schema as a structured record.

A schema record should separate the following components:

1. the number of holes;
2. the raw context expression;
3. the quotient assertion that the context is tautological;
4. the admissible filling class;
5. the instance map;
6. the soundness theorem for instances.

This prevents the common ambiguity between a schema, an instance of a schema, and a proof that the schema is valid.

### 18.2. Pure tautological schema record

> [!definition] Pure tautological schema record
> A **pure tautological schema record** is a tuple
>
> $$
> \mathfrak S=(n,C,\tau_C)
> $$
>
> where:
>
> 1. $n<\omega$;
> 2. $C\in Fm(H_n)$;
> 3. $\tau_C$ is evidence that
>    $$
>    [C]=\top
>    $$
>    in $LT(H_n)$.

The evidence $\tau_C$ may be a truth-table proof, a derivation in a propositional calculus, a normal-form computation, or any certified proof of tautologicity.

Given an atom set $P$, the schema record determines an instance map

$$
\operatorname{Inst}_{\mathfrak S,P}:Fm(P)^n\to Fm(P)
$$

by

$$
\operatorname{Inst}_{\mathfrak S,P}(\alpha_0,
\dots,
\alpha_{n-1})
=
C[\alpha_0,
\dots,
\alpha_{n-1}].
$$

The soundness theorem says

$$
[\operatorname{Inst}_{\mathfrak S,P}(\alpha_0,
\dots,
\alpha_{n-1})]=\top
$$

in $LT(P)$.

### 18.3. Parameterized schema record

Sometimes one wants parameters as well as holes. For example, a context might contain a fixed distinguished formula variable $p$ and one hole:

$$
C(p;
\Box)=p\to(\Box\vee p).
$$

This is not a pure schema over holes only; it is a parameterized context.

> [!definition] Parameterized schema record
> A **parameterized schema record over $P$** is a tuple
>
> $$
> \mathfrak S=(n,C,\Theta)
> $$
>
> where:
>
> 1. $C\in Fm(P\sqcup H_n)$;
> 2. $\Theta$ is a specified property of the quotient class $[C]\in LT(P\sqcup H_n)$.

Typical choices of $\Theta$ include:

$$
[C]=\top,
$$

or

$$
[C]\le[D],
$$

or membership of $[C]$ in some filter or theory.

The pure tautological case is recovered by setting $P=\varnothing$ and $\Theta$ equal to $[C]=\top$.

### 18.4. Schema instance versus schema operator

A schema record produces an instance map. But the instance map is not itself the schema record. The schema record stores the abstract pattern and its proof/evidence; the instance map acts on input formulas.

Thus one should distinguish:

$$
\mathfrak S=(n,C,\tau_C)
\quad\text{the schema record},
$$

$$
\operatorname{Inst}_{\mathfrak S,P}
\quad\text{the induced operation on formulas over }P,
$$

and

$$
C[\alpha_0,
\dots,
\alpha_{n-1}]
\quad\text{one concrete instance}.
$$

This distinction becomes important in first-order logic, where $C$ is propositional but the fillings $\alpha_i$ may be first-order formulas.

---

## 19. More detailed FOL elaboration

### 19.1. Two syntactic levels

In first-order logic, there are at least two syntax layers:

1. term syntax;
2. formula syntax.

The propositional skeleton acts only on the formula layer. That is, propositional contexts do not inspect term structure, quantifier binding, free variables, or atomic predicate structure. They treat whole first-order formulas as truth-valued atoms for the purpose of Boolean combination.

For a first-order language $\mathcal L$, let

$$
Form_{\mathcal L}
$$

be the raw formula set. It has operations

$$
\neg:Form_{\mathcal L}\to Form_{\mathcal L},
$$

$$
\wedge,
\vee,
\to,
\leftrightarrow:Form_{\mathcal L}^2\to Form_{\mathcal L}.
$$

The quantifiers

$$
\forall x,
\qquad
\exists x
$$

are additional formula constructors, but the propositional skeleton does not need them. It only needs the Boolean connective reduct of the formula algebra.

### 19.2. FOL formula algebra as a target for propositional contexts

For each $n$, a propositional context

$$
C\in Fm(H_n)
$$

induces an $n$-ary operation on $Form_{\mathcal L}$:

$$
C[-]:Form_{\mathcal L}^n\to Form_{\mathcal L}.
$$

This is defined recursively by interpreting propositional connectives as first-order formula connectives and holes as input positions.

Examples:

$$
C(\Box_0,
\Box_1)=\Box_0\to\Box_1
$$

gives

$$
C[\varphi,
\psi]=\varphi\to\psi.
$$

The commutativity tautology context

$$
C(\Box_0,
\Box_1)=(\Box_0\wedge\Box_1)\leftrightarrow(\Box_1\wedge\Box_0)
$$

gives the first-order formula instance

$$
(\varphi\wedge\psi)\leftrightarrow(\psi\wedge\varphi).
$$

### 19.3. FOL validity proof by local Boolean valuation

The soundness argument for propositional instances in FOL is extremely simple but conceptually important.

Fix:

1. an $\mathcal L$-structure $\mathcal M$;
2. a variable assignment $s$;
3. first-order formulas $\varphi_0,
\dots,
\varphi_{n-1}$;
4. a tautological context $C\in Fm(H_n)$.

Each first-order formula has a truth value under $(\mathcal M,s)$:

$$
\llbracket\varphi_i\rrbracket_{\mathcal M,s}\in2.
$$

Define a propositional truth assignment

$$
v_{\mathcal M,s}:H_n\to2
$$

by

$$
v_{\mathcal M,s}(\Box_i)=\llbracket\varphi_i\rrbracket_{\mathcal M,s}.
$$

Then by induction on the propositional context $C$,

$$
\llbracket C[\varphi_0,
\dots,
\varphi_{n-1}]\rrbracket_{\mathcal M,s}
=
\operatorname{val}_{v_{\mathcal M,s}}(C).
$$

If $C$ is tautological, the right side is $1$. Since $\mathcal M$ and $s$ were arbitrary, the instance is FOL-valid.

This is the precise formal reason why the first axiom group in many Hilbert systems can be stated as:

> every substitution instance of a propositional tautology is an axiom.

### 19.4. No capture issues for pure propositional contexts

When filling propositional holes by first-order formulas, no variable capture occurs, because propositional contexts contain no binders. For example,

$$
C(\Box)=\neg\Box
$$

and filling $\Box$ by $\forall x\,R(x)$ simply gives

$$
\neg\forall x\,R(x).
$$

There is no operation in $C$ that binds variables inside the inserted formula.

Capture issues arise only when the context language itself contains binders, as in first-order formula contexts with holes occurring under quantifiers. The propositional skeleton is deliberately binder-free.

This is one reason it is useful to isolate the propositional module before developing the full first-order substitution theory.

### 19.5. Propositional skeleton as a submodule of FOL syntax

The FOL formula algebra has more structure than propositional logic: quantifiers, atomic formulas, terms, relation symbols, equality, and free-variable behavior. But its Boolean connective reduct supports an action of the Boolean context clone.

For every $n$,

$$
\mathsf{BoolCtx}(n)=LT(H_n)
$$

acts on the semantic quotient of FOL formulas modulo logical equivalence, and raw contexts act directly on raw FOL formulas.

Thus the propositional skeleton appears inside FOL in two forms:

1. **raw syntactic action** on formulas by context filling;
2. **semantic quotient action** on logical equivalence classes by Boolean operations.

The first is used to generate axiom instances. The second explains why those instances are valid.

---

## 20. Worked schema examples

### 20.1. Modus ponens compatibility

The tautological context

$$
C(\Box_0,
\Box_1)=
\Box_0\to((\Box_0\to\Box_1)\to\Box_1)
$$

satisfies

$$
[C]=\top\in LT(H_2).
$$

Every instance

$$
\alpha\to((\alpha\to\beta)\to\beta)
$$

is tautological. This is not itself modus ponens; rather, it is a tautological formula that expresses the soundness pattern of modus ponens internally.

Actual modus ponens is a rule:

$$
\frac{\alpha\qquad \alpha\to\beta}{\beta}.
$$

At the quotient level, if $[\alpha]=\top$ and $[\alpha\to\beta]=\top$, then $[\beta]=\top$.

### 20.2. Hypothetical syllogism

Let

$$
C(\Box_0,
\Box_1,
\Box_2)=
((\Box_0\to\Box_1)\wedge(\Box_1\to\Box_2))\to(\Box_0\to\Box_2).
$$

Then

$$
[C]=\top.
$$

Therefore for arbitrary formulas $\alpha,
\beta,
\gamma$,

$$
((\alpha\to\beta)\wedge(\beta\to\gamma))\to(\alpha\to\gamma)
$$

is tautological.

### 20.3. De Morgan laws

The contexts

$$
C_1(\Box_0,
\Box_1)=
\neg(\Box_0\wedge\Box_1)\leftrightarrow(\neg\Box_0\vee\neg\Box_1),
$$

and

$$
C_2(\Box_0,
\Box_1)=
\neg(\Box_0\vee\Box_1)\leftrightarrow(\neg\Box_0\wedge\neg\Box_1)
$$

are top-valued in $LT(H_2)$.

Their instances are tautological in propositional logic and valid in FOL.

### 20.4. Distribution

The context

$$
C(\Box_0,
\Box_1,
\Box_2)=
\Box_0\wedge(\Box_1\vee\Box_2)
\leftrightarrow
((\Box_0\wedge\Box_1)\vee(\Box_0\wedge\Box_2))
$$

is tautological.

At the quotient level this says that meet distributes over join in $LT(P)$.

### 20.5. Absorption

The context

$$
C(\Box_0,
\Box_1)=
\Box_0\wedge(\Box_0\vee\Box_1)\leftrightarrow\Box_0
$$

is tautological. This gives absorption in the Boolean algebra quotient.

These examples illustrate the core principle:

$$
\boxed{
\text{Boolean identities are tautological quotient-context equations.}
}
$$

---

## 21. Implementation-oriented blueprint

### 21.1. Data types

A rigorous implementation can represent the propositional module using the following abstract data types.

**AtomSet.** A set or type of atom names.

**Formula[A].** The inductive type generated by:

1. `atom(a)` for $a\in A$;
2. `top`;
3. `bot`;
4. `neg(phi)`;
5. `and(phi,psi)`;
6. `or(phi,psi)`;
7. optionally `imp(phi,psi)`;
8. optionally `iff(phi,psi)`.

**HoleSet[n].** A finite distinguished atom set $H_n$.

**Context[P,n].** A formula over $P\sqcup H_n$.

**Substitution[A,B].** A map $A\to Formula[B]$.

**TruthAssignment[A].** A map $A\to\{0,1\}$.

**LTClass[A].** An equivalence class of formulas modulo tautological equivalence. In computation, this may be represented by a normalized truth table, BDD, canonical DNF, canonical CNF, or other canonical form.

### 21.2. Core operations

The implementation should expose:

**support:**

$$
\operatorname{supp}:Fm(A)\to\mathcal P_{fin}(A).
$$

**evaluation:**

$$
\operatorname{val}:TruthAssignment(A)\times Fm(A)\to2.
$$

**substitution extension:**

$$
\operatorname{subst}(\sigma,
\varphi)=\widehat\sigma(\varphi).
$$

**context filling:**

$$
\operatorname{fill}(C;
\alpha_0,
\dots,
\alpha_{n-1}).
$$

**tautology check:** finite truth-table check over support.

**equivalence check:** compare truth tables over the union of supports.

**quotient operation:** map formulas to canonical representatives of truth tables.

**schema instantiation:** given a tautological context record and fillers, produce an instance formula plus a proof certificate that it is tautological.

### 21.3. Proof objects

A proof-aware implementation should not merely output formulas; it should track why formulas are valid. For example, a tautological schema instance can carry a certificate:

$$
\operatorname{TautCtx}(C):[C]=\top
$$

and a filling tuple

$$
(\alpha_0,
\dots,
\alpha_{n-1}).
$$

The generated proof object may state:

$$
[C[\alpha_0,
\dots,
\alpha_{n-1}]]=\top
$$

by functoriality/substitution of quotient contexts.

For FOL, the proof object may state:

$$
\models C[\varphi_0,
\dots,
\varphi_{n-1}]
$$

by propositional tautology instantiation.

### 21.4. Avoiding conflations in implementation

The implementation should keep separate:

1. raw formula identity;
2. tautological equivalence;
3. chosen normal representative;
4. proof certificate of equivalence;
5. schema object;
6. schema instance;
7. substitution map;
8. context filling operation.

A common bad design is to identify formulas by their truth tables too early. That loses raw syntax, which is necessary for parsing, proof display, substitution, and FOL embedding.

The correct design is staged:

$$
\text{raw formula}
\xrightarrow{\pi}
\text{quotient class}
\xrightarrow{\text{optional normal form}}
\text{chosen representative}.
$$

---

## 22. Common pitfalls and corrections

### 22.1. Pitfall: every schema is a context

False. Every ordinary context gives a schema operator, but not every schema operator is an ordinary context.

Correction:

$$
\text{contexts are fixed-shape templates; schema operators may be recursive.}
$$

### 22.2. Pitfall: normal forms are quotient operations

A normal-form map is not an operation on quotient classes unless a canonical representative convention is fixed. At the quotient level, normal forms are invisible because

$$
[N(\varphi)]=[\varphi].
$$

Correction: normal forms are representative-selection functions.

### 22.3. Pitfall: variable elimination is a Boolean homomorphism

False. The operation

$$
\exists_A(a)=a[A:=\top]\vee a[A:=\bot]
$$

is not a Boolean homomorphism. It is a join-preserving projection/left adjoint.

Correction: treat $\exists_A$ as a quantifier-like operator, not a homomorphism.

### 22.4. Pitfall: duality is substitution

Duality can be decomposed into recursive clauses, but it is not ordinary substitution because it swaps connectives as well as acting on atoms.

Correction: duality is a recursive syntax translation whose quotient action is complementation.

### 22.5. Pitfall: FOL propositional instances require FOL-specific proof

The validity of propositional tautology instances in FOL requires only the fact that FOL formulas have truth values under structures and assignments and that Boolean connectives are interpreted truth-functionally.

Correction: prove FOL validity by pulling back to a finite propositional truth assignment on holes.

### 22.6. Pitfall: tautological equivalence equals proof equivalence

Tautological equivalence is semantic truth-table equality. Proof equivalence depends on a deductive calculus. Soundness and completeness may identify the two at the theorem level, but they are conceptually different.

Correction: keep semantic quotient $LT(P)$ separate from proof objects and derivations.

---

## 23. Final blueprint for the full propositional module

The complete module can be specified as follows.

### 23.1. Syntax layer

For every atom set $A$:

$$
Fm(A)=\mu X\big(A+1+1+X+X^2+X^2+X^2+X^2\big),
$$

where the summands correspond to atoms, $\top$, $\bot$, negation, conjunction, disjunction, implication, and biconditional.

The precise polynomial depends on which connectives are primitive.

### 23.2. Substitution layer

For every substitution

$$
\sigma:A\to Fm(B),
$$

there is a unique homomorphism

$$
\widehat\sigma:Fm(A)\to Fm(B).
$$

Composition of substitutions is Kleisli composition:

$$
(\tau\star\sigma)(a)=\widehat\tau(\sigma(a)).
$$

The identity substitution is

$$
\eta_A(a)=a.
$$

Thus $Fm(-)$ is a syntax monad.

### 23.3. Semantics layer

Truth assignments are maps

$$
v:A\to2,
$$

and evaluations are homomorphisms

$$
\operatorname{val}_v:Fm(A)\to2.
$$

Substitution and evaluation commute via

$$
\operatorname{val}_v(\widehat\sigma(\varphi))
=
\operatorname{val}_{v_\sigma}(\varphi).
$$

### 23.4. Quotient layer

Tautological equivalence is

$$
\equiv_{\mathrm{taut}}
=
\bigcap_{v:A\to2}\ker(\operatorname{val}_v).
$$

The quotient is

$$
LT(A)=Fm(A)/{\equiv_{\mathrm{taut}}}.
$$

It is the free Boolean algebra on $A$.

### 23.5. Context layer

For holes $H_n$:

$$
Ctx_n(P)=Fm(P\sqcup H_n),
$$

and

$$
QCtx_n(P)=LT(P\sqcup H_n).
$$

Pure quotient contexts

$$
\mathsf{BoolCtx}(n)=LT(H_n)
$$

form the Boolean clone under substitution into holes.

### 23.6. Schema layer

A tautological schema is

$$
C\in Fm(H_n)
\quad\text{with}\quad
[C]=\top.
$$

Its instances over formulas $Fm(P)$ are

$$
C[\alpha_0,
\dots,
\alpha_{n-1}].
$$

All such instances are tautologies.

### 23.7. FOL interface

For a first-order language $\mathcal L$, define

$$
\operatorname{PropTaut}_{\mathcal L}
=
\{C[\varphi_0,
\dots,
\varphi_{n-1}]:[C]=\top\in LT(H_n),\ \varphi_i\in Form_{\mathcal L}\}.
$$

Every element of $\operatorname{PropTaut}_{\mathcal L}$ is first-order valid.

This set is the rigorously parameterized version of the propositional axiom schema group.

---

## 24. Closing summary

The construction begins with raw syntax:

$$
Fm(A),
$$

the absolutely free formula algebra on atoms $A$.

Truth assignments are homomorphisms to $2$, and tautological equivalence is the intersection of all their kernels:

$$
\equiv_{\mathrm{taut}}=igcap_{v:A\to2}\ker(\operatorname{val}_v).
$$

Quotienting gives the free Boolean algebra:

$$
LT(A)=Fm(A)/{\equiv_{\mathrm{taut}}}.
$$

Contexts are formulas over holes:

$$
Ctx_n(P)=Fm(P\sqcup H_n).
$$

Quotient contexts are Boolean polynomial operations:

$$
QCtx_n(P)=LT(P\sqcup H_n).
$$

Pure quotient contexts form the Boolean clone:

$$
\mathsf{BoolCtx}(n)=LT(H_n).
$$

Tautological schemas are exactly those contexts whose quotient class is top:

$$
[C]=\top.
$$

Filling a tautological context by arbitrary formulas preserves tautologicity because filling is substitution, substitution descends to Boolean homomorphisms, and Boolean homomorphisms preserve $\top$.

General schema operators include contexts but go beyond them. CNF and DNF are normal representatives. Duality is a recursive transform realizing Boolean complementation. Variable elimination is an existential projection built from substitutions and disjunction. Deductive closure is a generated closure under tautologies and modus ponens, algebraically reflected by filters.

The final reusable FOL axiom-schema skeleton is:

$$
\boxed{
\operatorname{PropTaut}_{\mathcal L}
=
\{C[\varphi_0,
\dots,
\varphi_{n-1}]:[C]=\top\in LT(H_n),\ \varphi_i\in Form_{\mathcal L}\}.
}
$$

This is the clean formal object: a parameterized, syntactically rigorous propositional-logic module modulo tautologies, ready to be instantiated inside first-order logic.
