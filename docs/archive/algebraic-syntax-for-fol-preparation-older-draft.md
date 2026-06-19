# Algebraic Syntax for First-Order Logic Preparation

## 0. Orientation and Scope

### 0.1. Purpose and Boundary of the Development

> [!definition] Definition 0.1: Algebraic Syntax Spine
> Let $\Omega$ be a one-sorted finitary operation signature and let $X$ be a set. The algebraic syntax spine determined by $(\Omega,X)$ is the connected system consisting of:
> 
> 1. an absolutely free $\Omega$-algebra $\mathbf T_{\Omega}(X)$ on $X$;
> 2. concrete presentations of $\mathbf T_{\Omega}(X)$ by expressions, trees, tagged tuples, strings, or implementation carriers;
> 3. structural operations on syntax, including decomposition, subterm extraction, recursion, substitution, context application, and arity-indexed superposition;
> 4. evaluation homomorphisms from $\mathbf T_{\Omega}(X)$ into target $\Omega$-algebras;
> 5. kernels and quotients recording semantic or imposed syntactic identifications.

This note develops only the universal-algebraic machinery needed to control the term-forming component of first-order logic. It does not develop relation symbols, formula formation, satisfaction, binding, deductive calculi, theories, or model theory except insofar as they motivate the algebraic treatment of terms.

> [!remark] Remark 0.2: Syntax Before Semantics
> Raw terms are constructed before any target algebra, assignment, or interpretation is chosen. A term is not initially a function on a semantic domain. A term becomes a semantic value only after a valuation into a target algebra is extended to an evaluation homomorphism.

> [!warning] Warning 0.3: Presentations Are Not Literally Identical
> A tree, a displayed expression, a tagged tuple, and a well-formed string may present the same abstract term. They are not the same set-theoretic object unless the presentation has been explicitly chosen as the definition of the carrier. The correct invariant relation is canonical isomorphism over the generator set $X$, not literal equality of carriers.

### 0.2. Main Pipeline

The main pipeline is:

$$
(\Omega,X)
\longmapsto
\mathbf T_{\Omega}(X)
\longmapsto
\text{concrete presentations}
\longmapsto
\text{syntax operations}
\longmapsto
\operatorname{ev}_{g}:\mathbf T_{\Omega}(X)\to \mathbf B
\longmapsto
\operatorname{im}(\operatorname{ev}_{g})\cong \mathbf T_{\Omega}(X)/\ker(\operatorname{ev}_{g}).
$$

> [!definition] Definition 0.4: Abstract Syntax Object
> For a finitary signature $\Omega$ and set $X$, an abstract syntax object is a pair $(\mathbf F,\eta)$ where $\mathbf F$ is an $\Omega$-algebra and $\eta:X\to |F|$ is a map satisfying the universal mapping property for free $\Omega$-algebras on $X$.

> [!definition] Definition 0.5: Concrete Syntax Presentation
> A concrete syntax presentation of $(\Omega,X)$ is a triple $(\mathbf P,\eta^{P},\iota^{P})$ where:
> 
> 1. $\mathbf P$ is a concretely specified $\Omega$-algebra;
> 2. $\eta^{P}:X\to |P|$ is a generator insertion map;
> 3. $\iota^{P}:\mathbf T_{\Omega}(X)\to \mathbf P$ is an $\Omega$-isomorphism satisfying $\iota^{P}\circ \eta_X=\eta^{P}$.

### 0.3. Standing Distinctions

> [!definition] Definition 0.6: Syntactic Equality
> Syntactic equality in $\mathbf T_{\Omega}(X)$ is equality of elements of the carrier $T_{\Omega}(X)$. If terms are represented concretely, syntactic equality is transported from the canonical term algebra by the chosen presentation isomorphism.

> [!definition] Definition 0.7: Semantic Equality Under a Valuation
> Let $\mathbf B$ be an $\Omega$-algebra and let $g:X\to |B|$ be a valuation. Terms $s,t\in T_{\Omega}(X)$ are semantically equal under $g$ when
> 
> $$
> \operatorname{ev}_{g}(s)=\operatorname{ev}_{g}(t).
> $$

> [!definition] Definition 0.8: Generatedness Versus Freeness
> Let $\mathbf A$ be an $\Omega$-algebra and $S\subseteq |A|$.
> 
> 1. $S$ generates $\mathbf A$ if $\langle S\rangle_{\mathbf A}=|A|$.
> 2. $S$ freely generates $\mathbf A$ if there exists a map $\eta:S_{0}\to |A|$ with image $S$ such that $(\mathbf A,\eta)$ is free on $S_{0}$.
> 
> Generatedness asserts existence of expressions by constructors. Freeness asserts uniqueness of homomorphic extension from arbitrary assignments.

> [!warning] Warning 0.9: Parser, Substitution, Evaluation, and Quotient Maps
> The following maps have different types and must not be conflated:
> 
> $$
> \operatorname{parse}:\text{strings}\rightharpoonup T_{\Omega}(X),
> $$
> 
> $$
> \widehat{\sigma}:T_{\Omega}(X)\to T_{\Omega}(Y),
> $$
> 
> $$
> \operatorname{ev}_{g}:T_{\Omega}(X)\to |B|,
> $$
> 
> $$
> \pi_{\theta}:T_{\Omega}(X)\to T_{\Omega}(X)/\theta.
> $$
> 
> A parser reads a representation. A substitution is syntax-to-syntax evaluation. An evaluator is syntax-to-semantics evaluation. A quotient projection sends terms to equivalence classes.

---

## 1. Signatures, Algebras, and Homomorphisms

### 1.1. Finitary Signatures

> [!definition] Definition 1.1: One-Sorted Finitary Signature
> A one-sorted finitary signature is a family
> 
> $$
> \Omega=(\Omega_n)_{n\in\mathbb N}
> $$
> 
> of pairwise disjoint sets. An element $f\in \Omega_n$ is called an operation symbol of arity $n$. The set of all symbols is
> 
> $$
> |\Omega|=\bigcup_{n\in\mathbb N}\Omega_n.
> $$
> 
> If $f\in\Omega_n$, write $\operatorname{ar}(f)=n$.

> [!definition] Definition 1.2: Nullary Symbol
> A nullary symbol is an element $c\in\Omega_0$. It is a formal operation symbol of arity $0$, and in every $\Omega$-algebra it is interpreted as a distinguished element of the carrier.

> [!warning] Warning 1.3: Constants Are Not Variables
> A nullary operation symbol $c\in\Omega_0$ belongs to the signature and receives an interpretation in every $\Omega$-algebra. A variable $x\in X$ belongs to an external generator set and receives a value only after a valuation $g:X\to |A|$ is chosen.

### 1.2. $\Omega$-Algebras

> [!definition] Definition 1.4: $\Omega$-Algebra
> Let $\Omega$ be a one-sorted finitary signature. An $\Omega$-algebra is a pair
> 
> $$
> \mathbf A=(A,(f^{\mathbf A})_{f\in|\Omega|})
> $$
> 
> where $A$ is a set, called the carrier, and for each $f\in\Omega_n$ there is a function
> 
> $$
> f^{\mathbf A}:A^n\to A.
> $$
> 
> For $n=0$, identify $A^0$ with the singleton set $\{()\}$, so $f^{\mathbf A}:A^0\to A$ selects one element of $A$.

> [!notation] Notation 1.5: Carrier of an Algebra
> The carrier of an $\Omega$-algebra $\mathbf A$ is denoted by $|A|$ or $A$ when no ambiguity arises. The operation interpreting $f\in\Omega_n$ in $\mathbf A$ is denoted $f^{\mathbf A}$.

> [!definition] Definition 1.6: Syntax Algebra and Target Algebra
> A syntax algebra is an $\Omega$-algebra whose carrier consists of syntactic objects. A target algebra is an $\Omega$-algebra used as the semantic destination of an evaluation homomorphism. The same symbol $f\in\Omega_n$ induces:
> 
> $$
> f^{\mathbf T}:T^n\to T
> $$
> 
> on syntax and
> 
> $$
> f^{\mathbf B}:B^n\to B
> $$
> 
> in a target algebra.

### 1.3. Homomorphisms and Isomorphisms

> [!definition] Definition 1.7: Homomorphism
> Let $\mathbf A$ and $\mathbf B$ be $\Omega$-algebras. A homomorphism $h:\mathbf A\to\mathbf B$ is a function
> 
> $$
> h:|A|\to |B|
> $$
> 
> such that for every $f\in\Omega_n$ and every $(a_1,\ldots,a_n)\in |A|^n$,
> 
> $$
> h(f^{\mathbf A}(a_1,\ldots,a_n))
> =
> f^{\mathbf B}(h(a_1),\ldots,h(a_n)).
> $$
> 
> For $c\in\Omega_0$, this condition is
> 
> $$
> h(c^{\mathbf A})=c^{\mathbf B}.
> $$

> [!definition] Definition 1.8: Isomorphism
> A homomorphism $h:\mathbf A\to\mathbf B$ is an isomorphism if there exists a homomorphism $k:\mathbf B\to\mathbf A$ such that
> 
> $$
> k\circ h=\operatorname{id}_{|A|}
> \qquad\text{and}\qquad
> h\circ k=\operatorname{id}_{|B|}.
> $$
> 
> Equivalently, $h$ is a bijective homomorphism whose inverse function is a homomorphism.

> [!definition] Definition 1.9: Generator-Preserving Homomorphism
> Let $(\mathbf A,\eta_A)$ and $(\mathbf B,\eta_B)$ be $\Omega$-algebras equipped with maps $\eta_A:X\to |A|$ and $\eta_B:X\to |B|$. A homomorphism $h:\mathbf A\to\mathbf B$ is generator-preserving over $X$ if
> 
> $$
> h\circ \eta_A=\eta_B.
> $$

> [!remark] Remark 1.10: Isomorphism Is Not Definitional Identity
> If $h:\mathbf A\to\mathbf B$ is an isomorphism, then $\mathbf A$ and $\mathbf B$ have the same algebraic structure up to transport along $h$. This does not imply $|A|=|B|$ as sets.

---

## 2. Subalgebras, Kernels, Congruences, and Quotients

### 2.1. Subalgebras and Generated Subalgebras

> [!definition] Definition 2.1: Closed Subset
> Let $\mathbf A$ be an $\Omega$-algebra. A subset $S\subseteq |A|$ is closed under the operations of $\mathbf A$ if for every $f\in\Omega_n$ and every $(s_1,\ldots,s_n)\in S^n$,
> 
> $$
> f^{\mathbf A}(s_1,\ldots,s_n)\in S.
> $$
> 
> For $c\in\Omega_0$, this requires $c^{\mathbf A}\in S$.

> [!definition] Definition 2.2: Subalgebra
> Let $\mathbf A$ be an $\Omega$-algebra. A subalgebra of $\mathbf A$ is an $\Omega$-algebra $\mathbf S$ such that:
> 
> 1. $|S|\subseteq |A|$;
> 2. $|S|$ is closed under all operations of $\mathbf A$;
> 3. for each $f\in\Omega_n$, the operation $f^{\mathbf S}$ is the restriction of $f^{\mathbf A}$ to $|S|^n$.

> [!definition] Definition 2.3: Generated Subalgebra
> Let $\mathbf A$ be an $\Omega$-algebra and let $S\subseteq |A|$. The subalgebra generated by $S$, denoted
> 
> $$
> \langle S\rangle_{\mathbf A},
> $$
> 
> is the intersection of all closed subsets of $|A|$ containing $S$.

> [!proposition] Proposition 2.4: Minimality of Generated Subalgebras
> Let $\mathbf A$ be an $\Omega$-algebra and $S\subseteq |A|$. Then $\langle S\rangle_{\mathbf A}$ is the least subalgebra of $\mathbf A$ whose carrier contains $S$. Thus for every subalgebra $\mathbf C\leq \mathbf A$,
> 
> $$
> S\subseteq |C|
> \quad\Longrightarrow\quad
> \langle S\rangle_{\mathbf A}\subseteq |C|.
> $$

> [!proposition] Proposition 2.5: Image of a Homomorphism
> Let $h:\mathbf A\to\mathbf B$ be a homomorphism of $\Omega$-algebras. Then
> 
> $$
> \operatorname{im}(h)=\{h(a):a\in |A|\}
> $$
> 
> is the carrier of a subalgebra of $\mathbf B$.

### 2.2. Kernels and Congruences

> [!definition] Definition 2.6: Kernel of a Homomorphism
> Let $h:\mathbf A\to\mathbf B$ be a homomorphism. The kernel of $h$ is the binary relation
> 
> $$
> \ker h=\{(a,a')\in |A|^2:h(a)=h(a')\}.
> $$

> [!definition] Definition 2.7: Congruence
> Let $\mathbf A$ be an $\Omega$-algebra. A congruence on $\mathbf A$ is an equivalence relation $\theta\subseteq |A|^2$ such that for every $f\in\Omega_n$ and all $a_i,b_i\in |A|$,
> 
> $$
> (a_i,b_i)\in\theta\ \text{for all }1\leq i\leq n
> \quad\Longrightarrow\quad
> (f^{\mathbf A}(a_1,\ldots,a_n),f^{\mathbf A}(b_1,\ldots,b_n))\in\theta.
> $$

> [!proposition] Proposition 2.8: Kernel Congruence
> Let $h:\mathbf A\to\mathbf B$ be a homomorphism of $\Omega$-algebras. Then $\ker h$ is a congruence on $\mathbf A$.

### 2.3. Quotients and the First Isomorphism Theorem

> [!construction] Construction 2.9: Quotient Algebra
> Let $\mathbf A$ be an $\Omega$-algebra and let $\theta$ be a congruence on $\mathbf A$. The quotient algebra $\mathbf A/\theta$ has carrier
> 
> $$
> |A|/\theta=\{[a]_{\theta}:a\in |A|\},
> $$
> 
> and for each $f\in\Omega_n$ operation
> 
> $$
> f^{\mathbf A/\theta}([a_1]_{\theta},\ldots,[a_n]_{\theta})
> =
> [f^{\mathbf A}(a_1,\ldots,a_n)]_{\theta}.
> $$
> 
> Compatibility of $\theta$ with all operations is precisely the condition that these operations are well-defined.

> [!construction] Construction 2.10: Quotient Projection
> Let $\theta$ be a congruence on $\mathbf A$. The quotient projection is the homomorphism
> 
> $$
> \pi_{\theta}:\mathbf A\to \mathbf A/\theta,
> \qquad
> \pi_{\theta}(a)=[a]_{\theta}.
> $$

> [!theorem] Theorem 2.11: First Isomorphism Theorem for $\Omega$-Algebras
> Let $h:\mathbf A\to\mathbf B$ be a homomorphism of $\Omega$-algebras. Then $\ker h$ is a congruence on $\mathbf A$, $\operatorname{im}(h)$ is a subalgebra of $\mathbf B$, and there is a unique isomorphism
> 
> $$
> \overline h:\mathbf A/\ker h\to \operatorname{im}(h)
> $$
> 
> satisfying
> 
> $$
> \overline h([a]_{\ker h})=h(a)
> $$
> 
> for every $a\in |A|$.

> [!warning] Warning 2.12: Arbitrary Equivalence Relations Do Not Define Quotient Algebras
> If an equivalence relation $\theta$ on $|A|$ is not compatible with all operations of $\mathbf A$, then the formula
> 
> $$
> f([a_1]_{\theta},\ldots,[a_n]_{\theta})=[f(a_1,\ldots,a_n)]_{\theta}
> $$
> 
> may depend on the chosen representatives.

---

## 3. Absolutely Free $\Omega$-Algebras

### 3.1. Generator Maps and Assignments

> [!definition] Definition 3.1: Generator Set
> A generator set for syntax is a set $X$ external to the signature $\Omega$. Elements of $X$ are variable atoms. They are not operation symbols of $\Omega$.

> [!definition] Definition 3.2: Algebra with Designated Generators
> Let $\Omega$ be a finitary signature and $X$ a set. An $\Omega$-algebra with designated generators indexed by $X$ is a pair $(\mathbf A,\eta)$ where $\mathbf A$ is an $\Omega$-algebra and
> 
> $$
> \eta:X\to |A|
> $$
> 
> is a function.

> [!definition] Definition 3.3: Assignment into an Algebra
> Let $\mathbf A$ be an $\Omega$-algebra. An assignment of the generator set $X$ into $\mathbf A$ is an arbitrary function
> 
> $$
> g:X\to |A|.
> $$
> 
> No homomorphism condition is imposed because $X$ carries no $\Omega$-algebra structure.

### 3.2. Universal Mapping Property

> [!definition] Definition 3.4: Absolutely Free $\Omega$-Algebra on $X$
> Let $\Omega$ be a finitary signature and $X$ a set. An absolutely free $\Omega$-algebra on $X$ is a pair $(\mathbf F,\eta_X)$ such that $\mathbf F$ is an $\Omega$-algebra, $\eta_X:X\to |F|$ is a function, and for every $\Omega$-algebra $\mathbf A$ and every function $g:X\to |A|$, there exists a unique homomorphism
> 
> $$
> \widehat g:\mathbf F\to \mathbf A
> $$
> 
> satisfying
> 
> $$
> \widehat g\circ \eta_X=g.
> $$

> [!notation] Notation 3.5: Extension Notation
> If $(\mathbf F,\eta_X)$ is free on $X$ and $g:X\to |A|$, the unique homomorphic extension of $g$ is denoted
> 
> $$
> \widehat g:\mathbf F\to\mathbf A.
> $$
> 
> When $\mathbf F=\mathbf T_{\Omega}(X)$ and $\mathbf A=\mathbf B$ is a target algebra, the same homomorphism is often denoted
> 
> $$
> \operatorname{ev}_{g}:\mathbf T_{\Omega}(X)\to \mathbf B.
> $$

> [!theorem] Theorem 3.6: Uniqueness up to Unique Generator-Preserving Isomorphism
> Let $(\mathbf F,\eta_F)$ and $(\mathbf G,\eta_G)$ be absolutely free $\Omega$-algebras on the same set $X$. Then there exists a unique isomorphism
> 
> $$
> \alpha:\mathbf F\to\mathbf G
> $$
> 
> such that
> 
> $$
> \alpha\circ\eta_F=\eta_G.
> $$
> 
> Its inverse is the unique homomorphism $\beta:\mathbf G\to\mathbf F$ satisfying $\beta\circ\eta_G=\eta_F$.

> [!proposition] Proposition 3.7: Freeness Implies Generatedness
> Let $(\mathbf F,\eta_X)$ be absolutely free on $X$. Then the subalgebra of $\mathbf F$ generated by $\eta_X[X]$ is all of $\mathbf F$:
> 
> $$
> \langle \eta_X[X]\rangle_{\mathbf F}=|F|.
> $$

> [!warning] Warning 3.8: Generatedness Does Not Imply Freeness
> A subset $S\subseteq |A|$ may generate an algebra $\mathbf A$ without freely generating it. Generatedness provides terms representing elements. Freeness requires that all assignments of generators into any algebra extend uniquely to homomorphisms.

---

## 4. The Canonical Term Algebra

### 4.1. Formal Term Formation

> [!construction] Construction 4.1: Raw Terms over $(\Omega,X)$
> Let $\Omega$ be a finitary signature and let $X$ be a set. Define $T_{\Omega}(X)$ as the least set satisfying:
> 
> 1. for each $x\in X$, there is a term $\eta_X(x)\in T_{\Omega}(X)$;
> 2. for each $c\in\Omega_0$, there is a term $c()\in T_{\Omega}(X)$;
> 3. for each $f\in\Omega_n$ with $n\geq 1$ and each $(t_1,\ldots,t_n)\in T_{\Omega}(X)^n$, there is a term
> 
> $$
> f(t_1,\ldots,t_n)\in T_{\Omega}(X).
> $$

> [!definition] Definition 4.2: Variable Term
> A variable term is a term of the form $\eta_X(x)$ for some $x\in X$.

> [!definition] Definition 4.3: Nullary Operation Term
> A nullary operation term is a term of the form $c()$ for some $c\in\Omega_0$. It is often displayed as $c$, but its formal origin as an operation-symbol term remains distinct from a variable term.

> [!definition] Definition 4.4: Compound Term
> A compound term is a term of the form
> 
> $$
> f(t_1,\ldots,t_n)
> $$
> 
> where $f\in\Omega_n$, $n\geq 1$, and $t_i\in T_{\Omega}(X)$ for every $1\leq i\leq n$.

### 4.2. Term Algebra Structure

> [!construction] Construction 4.5: Canonical Term Algebra
> The canonical term algebra over $(\Omega,X)$ is the $\Omega$-algebra
> 
> $$
> \mathbf T_{\Omega}(X)=(T_{\Omega}(X),(f^{\mathbf T})_{f\in|\Omega|})
> $$
> 
> where, for $f\in\Omega_n$,
> 
> $$
> f^{\mathbf T}(t_1,\ldots,t_n)=f(t_1,\ldots,t_n).
> $$
> 
> For $c\in\Omega_0$, $c^{\mathbf T}=c()$.

> [!notation] Notation 4.6: Suppressing $\eta_X$
> When no confusion arises, the variable term $\eta_X(x)$ is denoted by $x$. This is an abbreviation, not an identification of $x\in X$ with an element of every target algebra.

> [!theorem] Theorem 4.7: Freeness of the Canonical Term Algebra
> Let $\Omega$ be a finitary signature and $X$ a set. The pair
> 
> $$
> (\mathbf T_{\Omega}(X),\eta_X)
> $$
> 
> is an absolutely free $\Omega$-algebra on $X$.

### 4.3. Unique Readability, Induction, and Recursion

> [!theorem] Theorem 4.8: Unique Readability of Raw Terms
> Every term $t\in T_{\Omega}(X)$ is exactly one of the following:
> 
> 1. $t=\eta_X(x)$ for a unique $x\in X$;
> 2. $t=c()$ for a unique $c\in\Omega_0$;
> 3. $t=f(t_1,\ldots,t_n)$ for a unique $n\geq 1$, unique $f\in\Omega_n$, and unique tuple $(t_1,\ldots,t_n)\in T_{\Omega}(X)^n$.
> 
> In particular, distinct constructor forms have disjoint ranges, and each constructor is injective on its input tuple.

> [!theorem] Theorem 4.9: Structural Induction on Terms
> Let $P\subseteq T_{\Omega}(X)$ be a subset. Suppose:
> 
> 1. $\eta_X(x)\in P$ for every $x\in X$;
> 2. $c()\in P$ for every $c\in\Omega_0$;
> 3. for every $f\in\Omega_n$ with $n\geq 1$, if $t_1,\ldots,t_n\in P$, then $f(t_1,\ldots,t_n)\in P$.
> 
> Then $P=T_{\Omega}(X)$.

> [!theorem] Theorem 4.10: Structural Recursion on Terms
> Let $C$ be a set. Suppose data are given as follows:
> 
> 1. for each $x\in X$, an element $a_x\in C$;
> 2. for each $c\in\Omega_0$, an element $a_c\in C$;
> 3. for each $f\in\Omega_n$ with $n\geq 1$, a function
> 
> $$
> R_f:C^n\to C.
> $$
> 
> Then there exists a unique function $\rho:T_{\Omega}(X)\to C$ satisfying
> 
> $$
> \rho(\eta_X(x))=a_x,
> $$
> 
> $$
> \rho(c())=a_c,
> $$
> 
> and
> 
> $$
> \rho(f(t_1,\ldots,t_n))
> =
> R_f(\rho(t_1),\ldots,\rho(t_n)).
> $$

---

## 5. Set-Theoretic Construction Engine for Freeness

### 5.1. Constructor Systems

> [!definition] Definition 5.1: Constructor System over $(\Omega,X)$
> A constructor system over $(\Omega,X)$ consists of:
> 
> 1. a set $C$;
> 2. an insertion map $\eta^C:X\to C$;
> 3. for each $f\in\Omega_n$, a function
> 
> $$
> N_f^C:C^n\to C.
> $$
> 
> The associated candidate $\Omega$-algebra is
> 
> $$
> \mathbf C=(C,(N_f^C)_{f\in|\Omega|}).
> $$

> [!definition] Definition 5.2: Concrete Syntax Candidate
> A concrete syntax candidate for $(\Omega,X)$ is a constructor system whose intended elements are concrete codes, trees, expressions, strings, or data structures representing formal terms.

> [!warning] Warning 5.3: A Data Structure Is Not Automatically Free Syntax
> Specifying constructors on a carrier does not prove that the carrier is a free syntax algebra. One must verify generatedness and absence of unwanted identifications.

### 5.2. Generated Closure and Construction Rank

> [!construction] Construction 5.4: Stage Construction
> Let $(C,\eta^C,(N_f^C))$ be a constructor system. Define subsets $C_k\subseteq C$ by:
> 
> $$
> C_0=\eta^C[X]\cup\{N_c^C():c\in\Omega_0\},
> $$
> 
> and
> 
> $$
> C_{k+1}
> =
> C_k\cup
> \{N_f^C(a_1,\ldots,a_n):f\in\Omega_n,\ n\geq 1,\ a_i\in C_k\}.
> $$
> 
> The finite-stage generated carrier is
> 
> $$
> C_{\omega}=\bigcup_{k\in\mathbb N}C_k.
> $$

> [!definition] Definition 5.5: Construction Rank
> If $a\in C_{\omega}$, the construction rank of $a$ is
> 
> $$
> \operatorname{rk}(a)=\min\{k\in\mathbb N:a\in C_k\}.
> $$

> [!proposition] Proposition 5.6: Generatedness by Finite Stages
> If $C=C_{\omega}$, then the candidate algebra $\mathbf C$ is generated by
> 
> $$
> \eta^C[X]\cup\{N_c^C():c\in\Omega_0\}.
> $$
> 
> If nullary symbols are already included as operations of the algebra, then $\mathbf C$ is generated as an $\Omega$-algebra by $\eta^C[X]$.

### 5.3. Free-Generation Criteria

> [!definition] Definition 5.7: Constructor Disjointness
> A constructor system $(C,\eta^C,(N_f^C))$ has disjoint constructors if:
> 
> 1. $\eta^C[X]$ is disjoint from every operation-constructor range;
> 2. for distinct $c,d\in\Omega_0$, $N_c^C()\neq N_d^C()$;
> 3. for $c\in\Omega_0$ and $f\in\Omega_n$ with $n\geq 1$, $N_c^C()$ is not in the range of $N_f^C$;
> 4. if $f\in\Omega_m$, $g\in\Omega_n$, and $f\neq g$, then the ranges of $N_f^C$ and $N_g^C$ are disjoint.

> [!definition] Definition 5.8: Constructor Injectivity
> A constructor $N_f^C:C^n\to C$ is injective if
> 
> $$
> N_f^C(a_1,\ldots,a_n)=N_f^C(b_1,\ldots,b_n)
> \quad\Longrightarrow\quad
> a_i=b_i\ \text{for all }1\leq i\leq n.
> $$

> [!definition] Definition 5.9: Unique Decomposition for a Constructor System
> A constructor system has unique decomposition if every element $a\in C$ is exactly one of:
> 
> 1. $\eta^C(x)$ for a unique $x\in X$;
> 2. $N_c^C()$ for a unique $c\in\Omega_0$;
> 3. $N_f^C(a_1,\ldots,a_n)$ for a unique $n\geq 1$, unique $f\in\Omega_n$, and unique tuple $(a_1,\ldots,a_n)\in C^n$.

> [!theorem] Theorem 5.10: Concrete Freeness Criterion
> Let $(C,\eta^C,(N_f^C))$ be a constructor system over $(\Omega,X)$ and let $\mathbf C$ be the associated $\Omega$-algebra. Suppose:
> 
> 1. $C=C_{\omega}$, where $C_{\omega}$ is the finite-stage closure generated by the constructors;
> 2. the constructor system has unique decomposition.
> 
> Then $(\mathbf C,\eta^C)$ is an absolutely free $\Omega$-algebra on $X$.

### 5.4. Comparison Map Method

> [!construction] Construction 5.11: Canonical Comparison Map
> Let $(\mathbf C,\eta^C)$ be a concrete syntax candidate over $(\Omega,X)$. Since $\mathbf T_{\Omega}(X)$ is free, the generator map $\eta^C:X\to C$ extends uniquely to a homomorphism
> 
> $$
> \chi_C:\mathbf T_{\Omega}(X)\to \mathbf C
> $$
> 
> satisfying
> 
> $$
> \chi_C(\eta_X(x))=\eta^C(x).
> $$

> [!proposition] Proposition 5.12: Surjectivity by Generatedness
> If $\mathbf C$ is generated by $\eta^C[X]$, then the canonical comparison map
> 
> $$
> \chi_C:\mathbf T_{\Omega}(X)\to\mathbf C
> $$
> 
> is surjective.

> [!proposition] Proposition 5.13: Injectivity by Unique Decomposition
> If $\mathbf C$ has unique decomposition and is generated by $\eta^C[X]$ together with nullary operation values, then the canonical comparison map $\chi_C$ is injective.

> [!corollary] Corollary 5.14: Concrete Presentation Theorem
> Under the hypotheses of Theorem 5.10, the canonical comparison map
> 
> $$
> \chi_C:\mathbf T_{\Omega}(X)\to\mathbf C
> $$
> 
> is the unique generator-preserving isomorphism from the canonical term algebra to the concrete syntax algebra.

---

## 6. Recursive Term-Expression Presentation

### 6.1. Expression Formation

> [!definition] Definition 6.1: Expression Alphabet
> Fix a finitary signature $\Omega$ and a set $X$. An expression alphabet for $(\Omega,X)$ consists of pairwise disjoint token classes for:
> 
> 1. variables $\operatorname{VarTok}(x)$ indexed by $x\in X$;
> 2. operation symbols $\operatorname{OpTok}(f)$ indexed by $f\in|\Omega|$;
> 3. delimiter tokens such as left parenthesis, right parenthesis, and comma.

> [!construction] Construction 6.2: Recursive Expressions
> The expression carrier $E_{\Omega}(X)$ is the least set of finite token strings satisfying:
> 
> 1. $\operatorname{VarTok}(x)\in E_{\Omega}(X)$ for each $x\in X$;
> 2. $\operatorname{OpTok}(c)\operatorname{LP}\operatorname{RP}\in E_{\Omega}(X)$ for each $c\in\Omega_0$;
> 3. if $f\in\Omega_n$ with $n\geq 1$ and $e_1,\ldots,e_n\in E_{\Omega}(X)$, then
> 
> $$
> \operatorname{OpTok}(f)\operatorname{LP}e_1\operatorname{COM}\cdots\operatorname{COM}e_n\operatorname{RP}
> \in E_{\Omega}(X).
> $$

> [!remark] Remark 6.3: Typography Is Presentation Data
> The printed expression $f(t_1,\ldots,t_n)$ is not the abstract constructor itself. It is a representational convention that must be controlled by disjoint lexical classes and parse rules.

### 6.2. Expression Algebra

> [!construction] Construction 6.4: Expression Algebra
> Define the $\Omega$-algebra
> 
> $$
> \mathbf E_{\Omega}(X)=(E_{\Omega}(X),(N_f^E)_{f\in|\Omega|})
> $$
> 
> by:
> 
> $$
> N_f^E(e_1,\ldots,e_n)
> =
> \operatorname{OpTok}(f)\operatorname{LP}e_1\operatorname{COM}\cdots\operatorname{COM}e_n\operatorname{RP}
> $$
> 
> for $f\in\Omega_n$, with the analogous empty-parenthesis expression for $n=0$. The generator map is
> 
> $$
> \eta^E(x)=\operatorname{VarTok}(x).
> $$

> [!theorem] Theorem 6.5: Freeness of Recursive Expression Syntax
> If the expression alphabet has disjoint lexical classes and the grammar in Construction 6.2 is used without ambiguous abbreviations, then
> 
> $$
> (\mathbf E_{\Omega}(X),\eta^E)
> $$
> 
> is an absolutely free $\Omega$-algebra on $X$.

> [!warning] Warning 6.6: Ambiguous Display Destroys Presentation Faithfulness
> If expression formation permits two different parse trees for the same displayed token string, then the displayed strings do not form a faithful presentation of the term algebra unless an additional parse-disambiguation convention is included as part of the data.

---

## 7. Tree Syntax Algebra

### 7.1. Addressed Tree Domains

> [!definition] Definition 7.1: Address Set
> Let $\mathbb N^{<\omega}$ be the set of all finite sequences of natural numbers. Its elements are called addresses. The empty sequence is denoted by $\epsilon$. If $p,q\in\mathbb N^{<\omega}$, their concatenation is denoted $p^\frown q$.

> [!definition] Definition 7.2: Prefix Order
> For $p,q\in\mathbb N^{<\omega}$, write $p\preceq q$ if there exists $r\in\mathbb N^{<\omega}$ such that
> 
> $$
> q=p^\frown r.
> $$
> 
> Then $p$ is a prefix of $q$.

> [!definition] Definition 7.3: Finite Tree Domain
> A finite tree domain is a finite subset $D\subseteq\mathbb N^{<\omega}$ such that:
> 
> 1. $\epsilon\in D$;
> 2. if $q\in D$ and $p\preceq q$, then $p\in D$;
> 3. for each $p\in D$, there exists $k_p\in\mathbb N$ such that
> 
> $$
> \{i\in\mathbb N:p^\frown(i)\in D\}=\{0,\ldots,k_p-1\}.
> $$

### 7.2. Labelled Ranked Trees

> [!definition] Definition 7.4: Label Set for Term Trees
> For a finitary signature $\Omega$ and generator set $X$, define the label set
> 
> $$
> L_{\Omega,X}=X\sqcup|\Omega|.
> $$
> 
> The coproduct notation indicates that variable labels and operation-symbol labels are kept disjoint.

> [!definition] Definition 7.5: Ranked Term Tree
> A ranked term tree over $(\Omega,X)$ is a pair $\tau=(D,\ell)$ where:
> 
> 1. $D\subseteq\mathbb N^{<\omega}$ is a finite tree domain;
> 2. $\ell:D\to L_{\Omega,X}$ is a labeling function;
> 3. if $\ell(p)=x\in X$, then $p$ has no children in $D$;
> 4. if $\ell(p)=f\in\Omega_n$, then $p$ has exactly $n$ children:
> 
> $$
> p^\frown(0),\ldots,p^\frown(n-1).
> $$

> [!definition] Definition 7.6: Tree Equality
> Two ranked term trees $(D,\ell)$ and $(D',\ell')$ are equal if
> 
> $$
> D=D'
> \qquad\text{and}\qquad
> \ell=\ell'.
> $$

### 7.3. Tree Algebra

> [!construction] Construction 7.7: Variable Leaf Tree
> For $x\in X$, define $\eta^{\operatorname{Tr}}(x)$ as the tree with domain $\{\epsilon\}$ and label $\ell(\epsilon)=x$.

> [!construction] Construction 7.8: Root Constructor for Trees
> Let $f\in\Omega_n$ and let $\tau_i=(D_i,\ell_i)$ be ranked term trees for $0\leq i<n$. Define
> 
> $$
> N_f^{\operatorname{Tr}}(\tau_0,\ldots,\tau_{n-1})=(D,\ell)
> $$
> 
> where
> 
> $$
> D=\{\epsilon\}\cup\{(i)^\frown p:0\leq i<n,\ p\in D_i\},
> $$
> 
> $\ell(\epsilon)=f$, and
> 
> $$
> \ell((i)^\frown p)=\ell_i(p).
> $$

> [!definition] Definition 7.9: Tree Syntax Algebra
> The tree syntax algebra is
> 
> $$
> \mathbf{Tr}_{\Omega}(X)
> =
> (\operatorname{Tr}_{\Omega}(X),(N_f^{\operatorname{Tr}})_{f\in|\Omega|}),
> $$
> 
> where $\operatorname{Tr}_{\Omega}(X)$ is the set of all ranked term trees over $(\Omega,X)$.

> [!theorem] Theorem 7.10: Freeness of Tree Syntax
> The pair
> 
> $$
> (\mathbf{Tr}_{\Omega}(X),\eta^{\operatorname{Tr}})
> $$
> 
> is an absolutely free $\Omega$-algebra on $X$. The unique generator-preserving isomorphism
> 
> $$
> \tau_{\Omega,X}:\mathbf T_{\Omega}(X)\to \mathbf{Tr}_{\Omega}(X)
> $$
> 
> sends each raw term to its ranked tree.

### 7.4. Local Tree Operations

> [!definition] Definition 7.11: Subtree at an Address
> Let $\tau=(D,\ell)$ be a ranked term tree and let $p\in D$. The subtree of $\tau$ at $p$ is the tree
> 
> $$
> \tau|_p=(D_p,\ell_p)
> $$
> 
> where
> 
> $$
> D_p=\{q\in\mathbb N^{<\omega}:p^\frown q\in D\}
> $$
> 
> and
> 
> $$
> \ell_p(q)=\ell(p^\frown q).
> $$

> [!definition] Definition 7.12: Height of a Tree
> The height of a ranked term tree $\tau=(D,\ell)$ is
> 
> $$
> \operatorname{ht}(\tau)=\max\{|p|:p\in D\},
> $$
> 
> where $|p|$ is the length of the address $p$.

> [!definition] Definition 7.13: Immediate Components of a Nonleaf Tree
> If $\tau=N_f^{\operatorname{Tr}}(\tau_0,\ldots,\tau_{n-1})$, then the immediate components of $\tau$ are the ordered tuple
> 
> $$
> (\tau_0,\ldots,\tau_{n-1}).
> $$

---

## 8. Tagged Tuple Syntax Algebra

### 8.1. Tuple Codes

> [!definition] Definition 8.1: Tuple Tag Set
> Let
> 
> $$
> \operatorname{Tag}=\{\operatorname{var},\operatorname{op}\}
> $$
> 
> with $\operatorname{var}\neq\operatorname{op}$. Tuple syntax uses these tags to prevent collisions between variables and operation-code expressions.

> [!construction] Construction 8.2: Tagged Tuple Carrier
> Define $U_{\Omega}(X)$ as the least set satisfying:
> 
> 1. for each $x\in X$,
> 
> $$
> (\operatorname{var},x)\in U_{\Omega}(X);
> $$
> 
> 2. for each $f\in\Omega_n$ and each $(u_1,\ldots,u_n)\in U_{\Omega}(X)^n$,
> 
> $$
> (\operatorname{op},f,(u_1,\ldots,u_n))\in U_{\Omega}(X).
> $$

> [!definition] Definition 8.3: Variable Code, Operation Code, and Nullary Code
> A variable code is a tuple $(\operatorname{var},x)$. An operation code is a tuple $(\operatorname{op},f,(u_1,\ldots,u_n))$ with $f\in\Omega_n$. A nullary code is an operation code $(\operatorname{op},c,())$ with $c\in\Omega_0$.

### 8.2. Tuple Algebra

> [!construction] Construction 8.4: Tagged Tuple Algebra
> The tagged tuple syntax algebra is
> 
> $$
> \mathbf U_{\Omega}(X)=(U_{\Omega}(X),(N_f^U)_{f\in|\Omega|}),
> $$
> 
> where
> 
> $$
> N_f^U(u_1,\ldots,u_n)=(\operatorname{op},f,(u_1,\ldots,u_n)).
> $$
> 
> The generator insertion is
> 
> $$
> \eta^U(x)=(\operatorname{var},x).
> $$

> [!theorem] Theorem 8.5: Freeness of Tagged Tuple Syntax
> The pair
> 
> $$
> (\mathbf U_{\Omega}(X),\eta^U)
> $$
> 
> is an absolutely free $\Omega$-algebra on $X$. Its comparison map from $\mathbf T_{\Omega}(X)$ is the unique generator-preserving isomorphism.

> [!remark] Remark 8.6: Tuple Codes as Formal Set-Theoretic Syntax
> Tagged tuple syntax is well-suited for set-theoretic construction because the tags encode the constructor class, the operation symbol, and the ordered list of immediate subterms without relying on typography or visual tree shape.

---

## 9. String Syntax Algebra

### 9.1. Strings, Grammars, and Well-Formedness

> [!definition] Definition 9.1: String Alphabet for a Signature
> A string alphabet for $(\Omega,X)$ is a set $\Sigma_{\Omega,X}$ containing pairwise disjoint lexical classes for variables, operation symbols, separators, parentheses, and any additional delimiters used by the grammar.

> [!definition] Definition 9.2: Finite String
> A finite string over $\Sigma_{\Omega,X}$ is a function
> 
> $$
> s:\{0,\ldots,n-1\}\to \Sigma_{\Omega,X}
> $$
> 
> for some $n\in\mathbb N$. The set of all finite strings over $\Sigma_{\Omega,X}$ is denoted $\Sigma_{\Omega,X}^{<\omega}$.

> [!definition] Definition 9.3: Well-Formed Term String
> A well-formed term string is a finite string produced by a specified grammar whose formation clauses correspond exactly to:
> 
> 1. variable atoms;
> 2. nullary operation symbols;
> 3. arity-correct operation application with delimiters sufficient for unique parsing.

> [!warning] Warning 9.4: Not Every String Is Syntax
> The carrier of string syntax is not $\Sigma_{\Omega,X}^{<\omega}$ but the subset of well-formed strings. Malformed strings belong to the ambient representation space but not to the syntax algebra.

### 9.2. Flattening and Parsing

> [!definition] Definition 9.5: Flattening Map
> A flattening map is a function
> 
> $$
> \operatorname{flat}:T_{\Omega}(X)\to \Sigma_{\Omega,X}^{<\omega}
> $$
> 
> assigning to each term a displayed string according to a chosen grammar.

> [!definition] Definition 9.6: Parser
> A parser for a string presentation is a partial function
> 
> $$
> \operatorname{parse}:\Sigma_{\Omega,X}^{<\omega}\rightharpoonup T_{\Omega}(X)
> $$
> 
> whose domain is the set of well-formed strings.

> [!definition] Definition 9.7: Unique Readability for Strings
> A string presentation has unique readability if
> 
> $$
> \operatorname{parse}(\operatorname{flat}(t))=t
> $$
> 
> for every $t\in T_{\Omega}(X)$, and
> 
> $$
> \operatorname{flat}(\operatorname{parse}(s))=s
> $$
> 
> for every well-formed string $s$.

> [!theorem] Theorem 9.8: Freeness of Hygienic String Syntax
> If a grammar for $\Sigma_{\Omega,X}^{<\omega}$ has unique readability and its well-formed strings are closed under arity-correct constructor formation, then the well-formed strings form an absolutely free $\Omega$-algebra on $X$.

### 9.3. Parser Versus Evaluator

> [!definition] Definition 9.9: Interpreter from Strings
> Let $\mathbf B$ be an $\Omega$-algebra and $g:X\to |B|$ a valuation. The string interpreter induced by $g$ is the partial map
> 
> $$
> \operatorname{interp}_g
> =
> \operatorname{ev}_{g}\circ\operatorname{parse}.
> $$
> 
> It is defined exactly on well-formed strings in the domain of $\operatorname{parse}$.

> [!warning] Warning 9.10: Parsing Is Not Evaluation
> A parser returns syntax. An evaluator returns semantic values in a target algebra. A string interpreter is a composite of parsing and evaluation, and its partiality comes from parsing, not from the algebraic evaluation homomorphism on raw syntax.

---

## 10. Additional and Implementation-Oriented Presentations

### 10.1. Prefix, Infix, and Notational Systems

> [!definition] Definition 10.1: Prefix Presentation
> A prefix presentation displays an operation application by placing the operation symbol before its arguments. Under fixed arities, prefix notation can be uniquely readable without parentheses if the lexical stream and arity function are part of the presentation data.

> [!definition] Definition 10.2: Fully Parenthesized Infix Presentation
> A fully parenthesized infix presentation for a binary operation symbol $*$ displays a compound term as
> 
> $$
> (s*t).
> $$
> 
> Parentheses are part of the representation and encode the binary tree shape.

> [!warning] Warning 10.3: Bare Infix Is Not Raw Syntax Without Grammar Data
> The expression $x*y*z$ is not a raw term until precedence, associativity, or explicit bracketing conventions determine whether it represents
> 
> $$
> (x*y)*z
> $$
> 
> or
> 
> $$
> x*(y*z).
> $$
> 
> Associativity of notation is not the same as an algebraic law in a target algebra.

### 10.2. DAGs, Sharing, and Cycles

> [!definition] Definition 10.4: Term DAG Representation
> A term DAG representation is a finite directed acyclic graph with labelled nodes whose unfolding at the root is a ranked term tree. It represents a term by sharing repeated subtrees.

> [!definition] Definition 10.5: Unfolding Map
> The unfolding map sends a rooted labelled term DAG to the ranked term tree obtained by duplicating shared nodes along distinct root-to-node paths.

> [!warning] Warning 10.6: Sharing Is Not Occurrence Identity
> Two occurrences of the same subterm in a tree may be represented by one shared node in a DAG. Sharing is a representation-level compression and must not be confused with equality of syntactic occurrences.

> [!warning] Warning 10.7: Cycles Leave Finitary Term Syntax
> A cyclic graph does not unfold to a finite term tree. Treating cyclic graphs as syntax requires a separate theory of infinite or regular terms, which is not part of this finitary development.

### 10.3. Implementation Fidelity

> [!definition] Definition 10.8: Faithful Implementation Representation
> An implementation carrier $D$ faithfully represents $T_{\Omega}(X)$ if there exists a bijection
> 
> $$
> r:D\to T_{\Omega}(X)
> $$
> 
> such that constructor operations, equality, and distinguished variables are transported along $r$.

> [!remark] Remark 10.9: Canonicalization Is Extra Structure
> Hash-consing, interning, normalization, pointer identity, serialization, and memoization are implementation choices. They may improve computation but do not alter raw syntactic equality unless a quotient or canonical representative convention is explicitly imposed.

---

## 11. Transfer of Structure Across Presentations

### 11.1. Presentation Data and Transfer Maps

> [!definition] Definition 11.1: Syntax Presentation over $X$
> A syntax presentation over $X$ is a triple
> 
> $$
> \mathcal P=(\mathbf P,\eta^P,\iota^P)
> $$
> 
> where $\mathbf P$ is an $\Omega$-algebra, $\eta^P:X\to |P|$, and
> 
> $$
> \iota^P:\mathbf T_{\Omega}(X)\to\mathbf P
> $$
> 
> is a generator-preserving isomorphism.

> [!construction] Construction 11.2: Transfer Between Presentations
> Let
> 
> $$
> \mathcal P=(\mathbf P,\eta^P,\iota^P)
> \qquad\text{and}\qquad
> \mathcal Q=(\mathbf Q,\eta^Q,\iota^Q)
> $$
> 
> be syntax presentations over $X$. The canonical transfer map from $\mathcal P$ to $\mathcal Q$ is
> 
> $$
> \operatorname{tr}_{P,Q}
> =
> \iota^Q\circ(\iota^P)^{-1}:\mathbf P\to\mathbf Q.
> $$

> [!proposition] Proposition 11.3: Transfer Is Generator-Preserving
> For every $x\in X$,
> 
> $$
> \operatorname{tr}_{P,Q}(\eta^P(x))=\eta^Q(x).
> $$

> [!proposition] Proposition 11.4: Transfer Commutes with Constructors
> Let $f\in\Omega_n$ and $p_1,\ldots,p_n\in |P|$. Then
> 
> $$
> \operatorname{tr}_{P,Q}(f^{\mathbf P}(p_1,\ldots,p_n))
> =
> f^{\mathbf Q}(\operatorname{tr}_{P,Q}(p_1),\ldots,\operatorname{tr}_{P,Q}(p_n)).
> $$

### 11.2. Transfer of Equality, Operations, and Evaluation

> [!proposition] Proposition 11.5: Equality Transfer
> Let $p,p'\in |P|$. Then
> 
> $$
> p=p'
> \quad\Longleftrightarrow\quad
> \operatorname{tr}_{P,Q}(p)=\operatorname{tr}_{P,Q}(p').
> $$

> [!construction] Construction 11.6: Transferring a Syntax Operation
> Let $F:T_{\Omega}(X)^m\to T_{\Omega}(X)$ be an $m$-ary operation on canonical syntax. Its transfer to presentation $\mathcal P$ is
> 
> $$
> F^{P}(p_1,\ldots,p_m)
> =
> \iota^P(F((\iota^P)^{-1}(p_1),\ldots,(\iota^P)^{-1}(p_m))).
> $$

> [!construction] Construction 11.7: Evaluation from a Presentation
> Let $\mathcal P=(\mathbf P,\eta^P,\iota^P)$ be a syntax presentation, let $\mathbf B$ be an $\Omega$-algebra, and let $g:X\to |B|$. The evaluation map from $\mathcal P$ is
> 
> $$
> \operatorname{ev}_{g}^{P}
> =
> \operatorname{ev}_{g}\circ(\iota^P)^{-1}:|P|\to |B|.
> $$

> [!theorem] Theorem 11.8: Master Transfer Theorem
> Let $\mathcal P$ and $\mathcal Q$ be syntax presentations over $X$. Then:
> 
> 1. $\operatorname{tr}_{P,Q}$ is the unique generator-preserving isomorphism $\mathbf P\to\mathbf Q$;
> 2. every algebraic operation on syntax definable from the free $\Omega$-algebra structure transfers by conjugation;
> 3. structural induction and structural recursion transfer along $\operatorname{tr}_{P,Q}$;
> 4. evaluation maps from $\mathcal P$ and $\mathcal Q$ agree after transfer:
> 
> $$
> \operatorname{ev}_{g}^{Q}\circ \operatorname{tr}_{P,Q}
> =
> \operatorname{ev}_{g}^{P}.
> $$

> [!warning] Warning 11.9: Transfer Requires Faithfulness
> The master transfer theorem applies to carriers equipped with a specified generator-preserving isomorphism from $\mathbf T_{\Omega}(X)$. It does not apply to malformed strings, ambiguous displays, noninjective encodings, or data structures whose equality relation collapses distinct raw terms.

---

## 12. Structural Operations on Syntax

### 12.1. Decomposition Operations

> [!definition] Definition 12.1: Outer Form
> Let $t\in T_{\Omega}(X)$. The outer form of $t$ is:
> 
> 1. $\operatorname{var}(x)$ if $t=\eta_X(x)$;
> 2. $\operatorname{null}(c)$ if $t=c()$ for $c\in\Omega_0$;
> 3. $\operatorname{node}(f,n)$ if $t=f(t_1,\ldots,t_n)$ for $f\in\Omega_n$ and $n\geq 1$.

> [!definition] Definition 12.2: Immediate Subterms
> If
> 
> $$
> t=f(t_1,\ldots,t_n)
> $$
> 
> with $n\geq 1$, the immediate subterm tuple of $t$ is
> 
> $$
> \operatorname{ch}(t)=(t_1,\ldots,t_n).
> $$
> 
> Variable terms and nullary operation terms have empty immediate subterm tuple.

> [!proposition] Proposition 12.3: Decomposition Is Presentation-Independent
> Any decomposition operation defined on $\mathbf T_{\Omega}(X)$ transfers to every syntax presentation. If the presentation is faithful, the transferred operation returns the corresponding concrete decomposition.

### 12.2. Subterms and Positions

> [!definition] Definition 12.4: Immediate Subterm Relation
> For $s,t\in T_{\Omega}(X)$, write $s\prec_1 t$ if $t=f(t_1,\ldots,t_n)$ for some $f\in\Omega_n$ and $s=t_i$ for some $i$.

> [!definition] Definition 12.5: Subterm Relation
> The subterm relation $\preceq_{\operatorname{sub}}$ is the reflexive transitive closure of $\prec_1$. A proper subterm is a subterm $s\preceq_{\operatorname{sub}}t$ with $s\neq t$.

> [!definition] Definition 12.6: Occurrence Position
> In the tree presentation of a term $t$, an occurrence position is an address $p$ in the domain of the corresponding ranked tree. The subterm at $p$ is the term represented by the subtree at $p$.

> [!warning] Warning 12.7: Subterm Equality Is Not Occurrence Equality
> If the same term occurs twice inside a larger term, then there are two occurrence positions but one subterm value. Occurrence-sensitive operations must use positions or contexts, not merely the set of subterm values.

### 12.3. Complexity Measures

> [!definition] Definition 12.8: Term Height
> The height of $t\in T_{\Omega}(X)$ is the function $\operatorname{ht}:T_{\Omega}(X)\to\mathbb N$ defined by:
> 
> $$
> \operatorname{ht}(\eta_X(x))=0,
> $$
> 
> $$
> \operatorname{ht}(c())=0,
> $$
> 
> and
> 
> $$
> \operatorname{ht}(f(t_1,\ldots,t_n))
> =
> 1+\max_{1\leq i\leq n}\operatorname{ht}(t_i)
> $$
> 
> for $n\geq 1$.

> [!definition] Definition 12.9: Term Size
> The size of $t\in T_{\Omega}(X)$ is the function $\operatorname{size}:T_{\Omega}(X)\to\mathbb N_{>0}$ defined by:
> 
> $$
> \operatorname{size}(\eta_X(x))=1,
> $$
> 
> $$
> \operatorname{size}(c())=1,
> $$
> 
> and
> 
> $$
> \operatorname{size}(f(t_1,\ldots,t_n))
> =
> 1+\sum_{i=1}^{n}\operatorname{size}(t_i).
> $$

> [!definition] Definition 12.10: Variable Set of a Term
> The variable set of $t\in T_{\Omega}(X)$ is the subset $\operatorname{Var}(t)\subseteq X$ defined recursively by:
> 
> $$
> \operatorname{Var}(\eta_X(x))=\{x\},
> $$
> 
> $$
> \operatorname{Var}(c())=\varnothing,
> $$
> 
> and
> 
> $$
> \operatorname{Var}(f(t_1,\ldots,t_n))
> =
> \bigcup_{i=1}^{n}\operatorname{Var}(t_i).
> $$

---

## 13. Structural Induction and Structural Recursion

### 13.1. Structural Induction Principles

> [!theorem] Theorem 13.1: Basic Structural Induction
> Let $P(t)$ be a predicate on $T_{\Omega}(X)$. If:
> 
> 1. $P(\eta_X(x))$ holds for every $x\in X$;
> 2. $P(c())$ holds for every $c\in\Omega_0$;
> 3. for every $f\in\Omega_n$ with $n\geq 1$, $P(t_1),\ldots,P(t_n)$ imply $P(f(t_1,\ldots,t_n))$;
> 
> then $P(t)$ holds for every $t\in T_{\Omega}(X)$.

> [!theorem] Theorem 13.2: Strong Structural Induction
> Let $P(t)$ be a predicate on $T_{\Omega}(X)$. Suppose that for every $t\in T_{\Omega}(X)$, if $P(s)$ holds for every proper subterm $s$ of $t$, then $P(t)$ holds. Then $P(t)$ holds for every $t\in T_{\Omega}(X)$.

> [!proposition] Proposition 13.3: Induction Transfer
> Let $\mathcal P=(\mathbf P,\eta^P,\iota^P)$ be a syntax presentation. A predicate $Q$ on $|P|$ satisfies structural induction on $\mathcal P$ iff the predicate
> 
> $$
> P(t)\Longleftrightarrow Q(\iota^P(t))
> $$
> 
> satisfies structural induction on $T_{\Omega}(X)$.

### 13.2. Structural Recursion and Folds

> [!definition] Definition 13.4: Recursion Algebra
> A recursion algebra for terms over $(\Omega,X)$ consists of a set $C$, elements $a_x\in C$ for $x\in X$, elements $a_c\in C$ for $c\in\Omega_0$, and functions
> 
> $$
> R_f:C^n\to C
> $$
> 
> for each $f\in\Omega_n$ with $n\geq 1$.

> [!construction] Construction 13.5: Fold Induced by Recursion Data
> Given a recursion algebra $C$ as in Definition 13.4, the induced fold is the unique function
> 
> $$
> \operatorname{fold}_{C}:T_{\Omega}(X)\to C
> $$
> 
> satisfying the recursive clauses determined by the data.

> [!remark] Remark 13.6: Algebra-Valued Recursion
> If $C$ is the carrier of an $\Omega$-algebra $\mathbf A$ and the recursive operations $R_f$ are the algebra operations $f^{\mathbf A}$, then the fold is a homomorphism $\mathbf T_{\Omega}(X)\to\mathbf A$.

> [!warning] Warning 13.7: Recursion on Quotients Requires Descent
> A recursively defined map on raw terms need not be well-defined on equivalence classes in a quotient $T_{\Omega}(X)/\theta$. It descends only if it is constant on $\theta$-classes.

---

## 14. Substitution as Syntax-to-Syntax Evaluation

### 14.1. Substitution Assignments

> [!definition] Definition 14.1: Substitution Assignment
> Let $X$ and $Y$ be sets. A substitution assignment from $X$ to $Y$ over $\Omega$ is a function
> 
> $$
> \sigma:X\to T_{\Omega}(Y).
> $$

> [!definition] Definition 14.2: Endosubstitution
> An endosubstitution on $X$ is a substitution assignment
> 
> $$
> \sigma:X\to T_{\Omega}(X).
> $$

> [!warning] Warning 14.3: Simultaneous Substitution Is Primitive
> Substitution is treated as simultaneous by default. A one-variable replacement operation is a special case obtained by choosing a substitution assignment that fixes all other generators.

### 14.2. Substitution Homomorphism

> [!construction] Construction 14.4: Substitution Extension
> Given $\sigma:X\to T_{\Omega}(Y)$, the substitution homomorphism induced by $\sigma$ is the unique homomorphism
> 
> $$
> \widehat{\sigma}:\mathbf T_{\Omega}(X)\to\mathbf T_{\Omega}(Y)
> $$
> 
> satisfying
> 
> $$
> \widehat{\sigma}(\eta_X(x))=\sigma(x)
> $$
> 
> for every $x\in X$.

> [!proposition] Proposition 14.5: Recursive Clauses for Substitution
> Let $\sigma:X\to T_{\Omega}(Y)$. Then:
> 
> $$
> \widehat{\sigma}(\eta_X(x))=\sigma(x),
> $$
> 
> $$
> \widehat{\sigma}(c())=c(),
> $$
> 
> and
> 
> $$
> \widehat{\sigma}(f(t_1,\ldots,t_n))
> =
> f(\widehat{\sigma}(t_1),\ldots,\widehat{\sigma}(t_n)).
> $$

### 14.3. Laws of Substitution

> [!definition] Definition 14.6: Identity Substitution
> The identity substitution on $X$ is
> 
> $$
> \eta_X:X\to T_{\Omega}(X).
> $$

> [!proposition] Proposition 14.7: Identity Law
> The homomorphic extension of $\eta_X:X\to T_{\Omega}(X)$ is the identity homomorphism:
> 
> $$
> \widehat{\eta_X}=\operatorname{id}_{T_{\Omega}(X)}.
> $$

> [!construction] Construction 14.8: Composite Substitution
> Let
> 
> $$
> \sigma:X\to T_{\Omega}(Y)
> \qquad\text{and}\qquad
> \tau:Y\to T_{\Omega}(Z).
> $$
> 
> Their composite substitution is
> 
> $$
> \tau\star\sigma:X\to T_{\Omega}(Z)
> $$
> 
> defined by
> 
> $$
> (\tau\star\sigma)(x)=\widehat{\tau}(\sigma(x)).
> $$

> [!theorem] Theorem 14.9: Associativity of Substitution
> If
> 
> $$
> \sigma:X\to T_{\Omega}(Y),\quad
> \tau:Y\to T_{\Omega}(Z),\quad
> \rho:Z\to T_{\Omega}(W),
> $$
> 
> then
> 
> $$
> \rho\star(\tau\star\sigma)=(\rho\star\tau)\star\sigma.
> $$

> [!theorem] Theorem 14.10: Evaluation-Substitution Compatibility
> Let $\sigma:X\to T_{\Omega}(Y)$ be a substitution assignment, let $\mathbf B$ be an $\Omega$-algebra, and let $g:Y\to |B|$ be a valuation. Define
> 
> $$
> g_{\sigma}:X\to |B|,
> \qquad
> g_{\sigma}(x)=\operatorname{ev}_{g}(\sigma(x)).
> $$
> 
> Then
> 
> $$
> \operatorname{ev}_{g}\circ\widehat{\sigma}
> =
> \operatorname{ev}_{g_{\sigma}}.
> $$

---

## 15. Contexts as Derived Syntax Operations

### 15.1. Hole-Extended Syntax

> [!definition] Definition 15.1: Hole Set
> For $n\in\mathbb N$, let
> 
> $$
> H_n=\{\Box_0,\ldots,\Box_{n-1}\}
> $$
> 
> be a set disjoint from $X$. Elements of $H_n$ are hole symbols.

> [!definition] Definition 15.2: $n$-Hole Raw Context
> An $n$-hole raw context over $X$ is a term
> 
> $$
> C\in T_{\Omega}(X\sqcup H_n).
> $$

> [!definition] Definition 15.3: Exact One-Hole Context
> A one-hole context is a term
> 
> $$
> C\in T_{\Omega}(X\sqcup\{\Box\})
> $$
> 
> in which $\Box$ occurs exactly once.

> [!remark] Remark 15.4: Context Object Versus Context Operation
> A context is a syntactic object in an enlarged term algebra. Its plugging action is the operation induced by substituting terms for holes.

### 15.2. Plugging and Replacement

> [!construction] Construction 15.5: Multi-Hole Plugging
> Let $C\in T_{\Omega}(X\sqcup H_n)$ and let $t_0,\ldots,t_{n-1}\in T_{\Omega}(X)$. Define the plugging result
> 
> $$
> C[t_0,\ldots,t_{n-1}]
> $$
> 
> as $\widehat{\sigma}(C)$, where
> 
> $$
> \sigma:X\sqcup H_n\to T_{\Omega}(X)
> $$
> 
> is given by
> 
> $$
> \sigma(x)=\eta_X(x)
> $$
> 
> for $x\in X$, and
> 
> $$
> \sigma(\Box_i)=t_i.
> $$

> [!definition] Definition 15.6: Context Operation
> Each $n$-hole context $C$ induces an $n$-ary operation
> 
> $$
> C[-,\ldots,-]:T_{\Omega}(X)^n\to T_{\Omega}(X)
> $$
> 
> by plugging.

> [!construction] Construction 15.7: Replacement at a Tree Position
> Let $t\in T_{\Omega}(X)$, let $p$ be an occurrence position of $t$ in the tree presentation, and let $u\in T_{\Omega}(X)$. The replacement $t[p:=u]$ is obtained by decomposing $t$ as
> 
> $$
> t=C[s]
> $$
> 
> for a one-hole context $C$ whose hole occurs at position $p$, and then setting
> 
> $$
> t[p:=u]=C[u].
> $$

### 15.3. Context Closure

> [!proposition] Proposition 15.8: Congruences Are Closed Under Contexts
> Let $\theta$ be a congruence on $\mathbf T_{\Omega}(X)$. If $(s_i,t_i)\in\theta$ for every $0\leq i<n$, then for every $n$-hole context $C$,
> 
> $$
> (C[s_0,\ldots,s_{n-1}],C[t_0,\ldots,t_{n-1}])\in\theta.
> $$

> [!corollary] Corollary 15.9: One-Hole Context Compatibility
> If $\theta$ is a congruence on $\mathbf T_{\Omega}(X)$ and $(s,t)\in\theta$, then for every one-hole context $C$,
> 
> $$
> (C[s],C[t])\in\theta.
> $$

> [!remark] Remark 15.10: Contexts as Polynomial Syntax Operations
> Context operations are syntax-built operations. They are the raw syntactic analogue of polynomial operations in concrete algebras, except that the parameters are syntactic terms rather than elements of a semantic carrier.

---

## 16. Syntactic Clones and Derived Term Operations

### 16.1. Arity-Indexed Terms

> [!notation] Notation 16.1: Finite Variable Context
> For $n\in\mathbb N$, write
> 
> $$
> \underline n=\{0,\ldots,n-1\}
> $$
> 
> and choose variables
> 
> $$
> x_0,\ldots,x_{n-1}.
> $$
> 
> The term set $T_{\Omega}(\underline n)$ is read as the set of formal $n$-ary terms.

> [!definition] Definition 16.2: Projection Term
> For $0\leq i<n$, the $i$-th projection term is
> 
> $$
> x_i\in T_{\Omega}(\underline n).
> $$

> [!remark] Remark 16.3: Terms as Delayed Operations
> A term $t\in T_{\Omega}(\underline n)$ is a formal operation waiting for a target algebra. Before a target algebra is chosen, it is syntax, not a function $A^n\to A$.

### 16.2. Formal Superposition

> [!construction] Construction 16.4: Formal Superposition
> Let $m,n\in\mathbb N$, let
> 
> $$
> t\in T_{\Omega}(\underline m),
> $$
> 
> and let
> 
> $$
> s_0,\ldots,s_{m-1}\in T_{\Omega}(\underline n).
> $$
> 
> Define the superposition
> 
> $$
> t[s_0,\ldots,s_{m-1}]
> \in T_{\Omega}(\underline n)
> $$
> 
> as the result of the substitution $\sigma:\underline m\to T_{\Omega}(\underline n)$ with $\sigma(i)=s_i$.

> [!theorem] Theorem 16.5: Associativity of Formal Superposition
> For arity-compatible terms, formal superposition satisfies:
> 
> $$
> t[s_0,\ldots,s_{m-1}][r_0,\ldots,r_{n-1}]
> =
> t[s_0[r_0,\ldots,r_{n-1}],\ldots,s_{m-1}[r_0,\ldots,r_{n-1}]].
> $$

> [!theorem] Theorem 16.6: Projection Identities
> For $t\in T_{\Omega}(\underline n)$,
> 
> $$
> t[x_0,\ldots,x_{n-1}]=t.
> $$
> 
> If $s_0,\ldots,s_{n-1}\in T_{\Omega}(\underline m)$, then
> 
> $$
> x_i[s_0,\ldots,s_{n-1}]=s_i.
> $$

### 16.3. Syntactic Clone

> [!definition] Definition 16.7: Syntactic Clone
> The syntactic clone of $\Omega$ is the arity-indexed family
> 
> $$
> \operatorname{Syn}_{\Omega}=(T_{\Omega}(\underline n))_{n\in\mathbb N}
> $$
> 
> equipped with projection terms and formal superposition.

> [!remark] Remark 16.8: Relation to the Term Algebra
> The term algebra $\mathbf T_{\Omega}(X)$ treats terms as elements generated from a variable set $X$. The syntactic clone treats terms in finite variable contexts as formal operations and organizes their substitution laws.

### 16.4. Interpretation in Concrete Algebras

> [!construction] Construction 16.9: Term Operation Induced by a Term
> Let $\mathbf A$ be an $\Omega$-algebra and let $t\in T_{\Omega}(\underline n)$. The term operation induced by $t$ on $\mathbf A$ is the function
> 
> $$
> t^{\mathbf A}:|A|^n\to |A|
> $$
> 
> defined by
> 
> $$
> t^{\mathbf A}(a_0,\ldots,a_{n-1})
> =
> \operatorname{ev}_{g_{\vec a}}(t),
> $$
> 
> where $g_{\vec a}:\underline n\to |A|$ is given by $g_{\vec a}(i)=a_i$.

> [!theorem] Theorem 16.10: Interpretation Commutes with Superposition
> Let $\mathbf A$ be an $\Omega$-algebra, let $t\in T_{\Omega}(\underline m)$, and let $s_0,\ldots,s_{m-1}\in T_{\Omega}(\underline n)$. Then
> 
> $$
> (t[s_0,\ldots,s_{m-1}])^{\mathbf A}
> =
> t^{\mathbf A}\circ (s_0^{\mathbf A},\ldots,s_{m-1}^{\mathbf A}),
> $$
> 
> where the right-hand side is the function $A^n\to A$ sending $\vec a$ to
> 
> $$
> t^{\mathbf A}(s_0^{\mathbf A}(\vec a),\ldots,s_{m-1}^{\mathbf A}(\vec a)).
> $$

> [!definition] Definition 16.11: Term Clone of an Algebra
> The term clone of an $\Omega$-algebra $\mathbf A$ is the arity-indexed family
> 
> $$
> \operatorname{Clo}(\mathbf A)_n=\{t^{\mathbf A}:t\in T_{\Omega}(\underline n)\}
> $$
> 
> equipped with ordinary composition of operations and projections.

### 16.5. Kernels and Parameters

> [!definition] Definition 16.12: Clone Kernel of an Algebra
> Let $\mathbf A$ be an $\Omega$-algebra. For each $n$, define an equivalence relation on $T_{\Omega}(\underline n)$ by:
> 
> $$
> s\equiv_{\mathbf A,n} t
> \quad\Longleftrightarrow\quad
> s^{\mathbf A}=t^{\mathbf A}
> $$
> 
> as functions $A^n\to A$. This is the $n$-ary clone kernel of $\mathbf A$.

> [!definition] Definition 16.13: Valuation Kernel
> Let $\mathbf A$ be an $\Omega$-algebra and $g:X\to |A|$. The valuation kernel is
> 
> $$
> \ker(\operatorname{ev}_g)
> =
> \{(s,t):\operatorname{ev}_g(s)=\operatorname{ev}_g(t)\}.
> $$

> [!warning] Warning 16.14: Clone Kernel Is Global, Valuation Kernel Is Local
> The clone kernel identifies terms that induce the same operation under all input assignments. A valuation kernel identifies terms that agree at one fixed assignment. The latter may be strictly larger.

> [!definition] Definition 16.15: Polynomial Operation with Parameters
> Let $\mathbf A$ be an $\Omega$-algebra. An $n$-ary polynomial operation with parameters from $A$ is obtained by evaluating a term in variables $x_0,\ldots,x_{n-1}$ together with additional parameter variables assigned fixed elements of $A$.

---

## 17. Evaluation into Target Algebras

### 17.1. Valuations and Evaluation

> [!definition] Definition 17.1: Target Algebra
> A target algebra for syntax over $\Omega$ is an $\Omega$-algebra $\mathbf B$ used as the codomain of an evaluation homomorphism.

> [!definition] Definition 17.2: Valuation
> Let $\mathbf B$ be an $\Omega$-algebra. A valuation of $X$ in $\mathbf B$ is a function
> 
> $$
> g:X\to |B|.
> $$

> [!construction] Construction 17.3: Evaluation Homomorphism
> Given a valuation $g:X\to |B|$, the evaluation homomorphism is the unique homomorphism
> 
> $$
> \operatorname{ev}_g:\mathbf T_{\Omega}(X)\to \mathbf B
> $$
> 
> satisfying
> 
> $$
> \operatorname{ev}_g(\eta_X(x))=g(x).
> $$

> [!proposition] Proposition 17.4: Recursive Clauses for Evaluation
> For every valuation $g:X\to |B|$:
> 
> $$
> \operatorname{ev}_g(\eta_X(x))=g(x),
> $$
> 
> $$
> \operatorname{ev}_g(c())=c^{\mathbf B},
> $$
> 
> and
> 
> $$
> \operatorname{ev}_g(f(t_1,\ldots,t_n))
> =
> f^{\mathbf B}(\operatorname{ev}_g(t_1),\ldots,\operatorname{ev}_g(t_n)).
> $$

### 17.2. Evaluation Image

> [!definition] Definition 17.5: Evaluation Image
> The evaluation image of $g:X\to |B|$ is
> 
> $$
> \operatorname{im}(\operatorname{ev}_g)
> =
> \{\operatorname{ev}_g(t):t\in T_{\Omega}(X)\}.
> $$

> [!theorem] Theorem 17.6: Generated Subalgebra Theorem for Evaluation
> Let $\mathbf B$ be an $\Omega$-algebra and $g:X\to |B|$ a valuation. Then
> 
> $$
> \operatorname{im}(\operatorname{ev}_g)=\langle g[X]\rangle_{\mathbf B}.
> $$
> 
> More precisely, the image of $\operatorname{ev}_g$ is the subalgebra of $\mathbf B$ generated by the assigned values of the variables, with nullary operation values included by closure under the $\Omega$-operations.

> [!corollary] Corollary 17.7: Evaluation Is Surjective onto the Generated Subalgebra
> With $\mathbf B$ and $g$ as above,
> 
> $$
> \operatorname{ev}_g:\mathbf T_{\Omega}(X)\to \langle g[X]\rangle_{\mathbf B}
> $$
> 
> is a surjective homomorphism.

### 17.3. Evaluation Kernels and Quotients

> [!definition] Definition 17.8: Semantic Collapse Under a Valuation
> A pair $(s,t)\in T_{\Omega}(X)^2$ collapses under $g:X\to |B|$ when
> 
> $$
> \operatorname{ev}_g(s)=\operatorname{ev}_g(t).
> $$
> 
> The set of all such pairs is $\ker(\operatorname{ev}_g)$.

> [!theorem] Theorem 17.9: Evaluation Quotient Theorem
> Let $\mathbf B$ be an $\Omega$-algebra and $g:X\to |B|$ a valuation. Then
> 
> $$
> \mathbf T_{\Omega}(X)/\ker(\operatorname{ev}_g)
> \cong
> \langle g[X]\rangle_{\mathbf B}.
> $$
> 
> The isomorphism sends
> 
> $$
> [t]_{\ker(\operatorname{ev}_g)}
> \longmapsto
> \operatorname{ev}_g(t).
> $$

> [!corollary] Corollary 17.10: No-Collapse Criterion
> The evaluation homomorphism
> 
> $$
> \operatorname{ev}_g:\mathbf T_{\Omega}(X)\to \langle g[X]\rangle_{\mathbf B}
> $$
> 
> is an isomorphism iff
> 
> $$
> \ker(\operatorname{ev}_g)=\Delta_{T_{\Omega}(X)}.
> $$
> 
> Equivalently, the assigned values $g[X]$ freely generate the subalgebra $\langle g[X]\rangle_{\mathbf B}$.

---

## 18. Quotient Syntax and Descent

### 18.1. Quotient Syntax

> [!definition] Definition 18.1: Syntax Congruence
> A syntax congruence is a congruence $\theta$ on $\mathbf T_{\Omega}(X)$. Its elements identify raw terms in a way compatible with all operation-symbol constructors.

> [!construction] Construction 18.2: Quotient Syntax Algebra
> Given a syntax congruence $\theta$ on $\mathbf T_{\Omega}(X)$, the quotient syntax algebra is
> 
> $$
> \mathbf T_{\Omega}(X)/\theta.
> $$

> [!remark] Remark 18.3: Syntax Modulo Equations
> If $E\subseteq T_{\Omega}(X)^2$, then the smallest congruence containing $E$ identifies terms forced equal by the equations in $E$. The resulting quotient is raw syntax modulo the imposed equations.

> [!warning] Warning 18.4: Quotients Lose Raw Unique Decomposition
> In $\mathbf T_{\Omega}(X)/\theta$, a class $[t]_{\theta}$ may contain terms with different outer constructors. Thus raw structural decomposition does not automatically descend to quotient syntax.

### 18.2. Descent

> [!definition] Definition 18.5: Descent Through a Quotient
> Let $\theta$ be an equivalence relation on a set $A$, and let $F:A\to C$ be a function. The function $F$ descends through the quotient map $\pi_{\theta}:A\to A/\theta$ if there exists a function $\overline F:A/\theta\to C$ such that
> 
> $$
> F=\overline F\circ \pi_{\theta}.
> $$

> [!proposition] Proposition 18.6: Descent Criterion
> Let $\theta$ be an equivalence relation on $A$ and $F:A\to C$ a function. Then $F$ descends through $A/\theta$ iff
> 
> $$
> \theta\subseteq \ker F.
> $$

> [!theorem] Theorem 18.7: Evaluation Through Quotient Syntax
> Let $\theta$ be a congruence on $\mathbf T_{\Omega}(X)$, let $\mathbf B$ be an $\Omega$-algebra, and let $g:X\to |B|$. The evaluation homomorphism
> 
> $$
> \operatorname{ev}_g:\mathbf T_{\Omega}(X)\to\mathbf B
> $$
> 
> factors through $\mathbf T_{\Omega}(X)/\theta$ iff
> 
> $$
> \theta\subseteq \ker(\operatorname{ev}_g).
> $$

> [!warning] Warning 18.8: Recursion Modulo Equations Requires Compatibility
> A recursive definition on raw representatives determines a function on quotient classes only if equivalent representatives receive equal recursive values. Freeness of raw syntax does not supply this compatibility automatically.

### 18.3. Substitution on Quotients

> [!definition] Definition 18.9: Substitution Compatibility with Congruences
> Let $\theta$ be a congruence on $\mathbf T_{\Omega}(X)$ and $\psi$ a congruence on $\mathbf T_{\Omega}(Y)$. A substitution assignment $\sigma:X\to T_{\Omega}(Y)$ is compatible with $(\theta,\psi)$ if
> 
> $$
> (s,t)\in\theta
> \quad\Longrightarrow\quad
> (\widehat{\sigma}(s),\widehat{\sigma}(t))\in\psi.
> $$

> [!proposition] Proposition 18.10: Induced Substitution on Quotients
> If $\sigma:X\to T_{\Omega}(Y)$ is compatible with $(\theta,\psi)$, then there is a unique homomorphism
> 
> $$
> \overline{\sigma}:\mathbf T_{\Omega}(X)/\theta\to \mathbf T_{\Omega}(Y)/\psi
> $$
> 
> satisfying
> 
> $$
> \overline{\sigma}([t]_{\theta})=[\widehat{\sigma}(t)]_{\psi}.
> $$

> [!definition] Definition 18.11: Fully Invariant Congruence
> A congruence $\theta$ on $\mathbf T_{\Omega}(X)$ is fully invariant if every endosubstitution $\sigma:X\to T_{\Omega}(X)$ satisfies
> 
> $$
> (s,t)\in\theta
> \quad\Longrightarrow\quad
> (\widehat{\sigma}(s),\widehat{\sigma}(t))\in\theta.
> $$

> [!remark] Remark 18.12: Equational Theories Versus Valuation Kernels
> A valuation kernel is local to one valuation into one target algebra. An equational theory is global over a class of algebras or over all assignments in a given algebra, and is stable under substitution when it determines a fully invariant congruence.

---

## 19. Synthesis: Algebraic Syntax Schemes

### 19.1. Three-Level Architecture

> [!definition] Definition 19.1: Abstract Level
> The abstract level consists of the free algebra
> 
> $$
> \mathbf T_{\Omega}(X)
> $$
> 
> and its universal mapping property. It supplies canonical syntax, homomorphic extension, induction, recursion, substitution, and quotient formation.

> [!definition] Definition 19.2: Presentation Level
> The presentation level consists of concrete syntax algebras such as:
> 
> $$
> \mathbf E_{\Omega}(X),\quad
> \mathbf{Tr}_{\Omega}(X),\quad
> \mathbf U_{\Omega}(X),\quad
> \mathbf S_{\Omega}(X),
> $$
> 
> each equipped with a generator-preserving isomorphism from $\mathbf T_{\Omega}(X)$.

> [!definition] Definition 19.3: Semantic Level
> The semantic level consists of target $\Omega$-algebras $\mathbf B$, valuations $g:X\to |B|$, evaluation homomorphisms $\operatorname{ev}_g$, images, kernels, and quotients.

### 19.2. Fundamental Maps

> [!notation] Notation 19.4: Representation Maps
> Presentation maps and transfer maps have the forms:
> 
> $$
> \iota^P:\mathbf T_{\Omega}(X)\to \mathbf P,
> $$
> 
> $$
> \operatorname{tr}_{P,Q}=\iota^Q\circ(\iota^P)^{-1}.
> $$

> [!notation] Notation 19.5: Syntax-Level Maps
> Substitution and context maps have the forms:
> 
> $$
> \widehat{\sigma}:\mathbf T_{\Omega}(X)\to \mathbf T_{\Omega}(Y),
> $$
> 
> $$
> C[-,\ldots,-]:T_{\Omega}(X)^n\to T_{\Omega}(X).
> $$

> [!notation] Notation 19.6: Semantic and Quotient Maps
> Evaluation and quotient maps have the forms:
> 
> $$
> \operatorname{ev}_g:\mathbf T_{\Omega}(X)\to \mathbf B,
> $$
> 
> $$
> \pi_{\theta}:\mathbf T_{\Omega}(X)\to \mathbf T_{\Omega}(X)/\theta.
> $$

### 19.3. Master Diagrams

> [!remark] Remark 19.7: Presentation Transfer Diagram
> The canonical presentation diagram has center $\mathbf T_{\Omega}(X)$ and spokes
> 
> $$
> \mathbf T_{\Omega}(X)
> \xrightarrow{\iota^P}
> \mathbf P,
> \qquad
> \mathbf T_{\Omega}(X)
> \xrightarrow{\iota^Q}
> \mathbf Q.
> $$
> 
> Transfer between concrete presentations is the composite
> 
> $$
> \mathbf P
> \xrightarrow{(\iota^P)^{-1}}
> \mathbf T_{\Omega}(X)
> \xrightarrow{\iota^Q}
> \mathbf Q.
> $$

> [!remark] Remark 19.8: Substitution and Evaluation Diagram
> For $\sigma:X\to T_{\Omega}(Y)$ and $g:Y\to |B|$, the compatibility condition is:
> 
> $$
> \operatorname{ev}_{g}\circ\widehat{\sigma}
> =
> \operatorname{ev}_{g_{\sigma}},
> $$
> 
> where
> 
> $$
> g_{\sigma}(x)=\operatorname{ev}_{g}(\sigma(x)).
> $$

> [!remark] Remark 19.9: Quotient Descent Diagram
> A map $F:T_{\Omega}(X)\to C$ factors through quotient syntax precisely when:
> 
> $$
> \theta\subseteq \ker F.
> $$
> 
> The descended map $\overline F$ satisfies:
> 
> $$
> F=\overline F\circ\pi_{\theta}.
> $$

### 19.4. Master Table of Schemes

| Scheme | Input | Output | Governing condition |
|---|---:|---:|---|
| Free syntax | $(\Omega,X)$ | $\mathbf T_{\Omega}(X)$ | Universal mapping property |
| Concrete presentation | constructor carrier | presentation $\mathbf P$ | generatedness and unique decomposition |
| Transfer | presentations $\mathbf P,\mathbf Q$ | $\operatorname{tr}_{P,Q}$ | unique isomorphism over $X$ |
| Structural recursion | recursion data | fold $T_{\Omega}(X)\to C$ | unique readability |
| Substitution | $\sigma:X\to T_{\Omega}(Y)$ | $\widehat{\sigma}$ | homomorphic extension |
| Context operation | $C\in T_{\Omega}(X\sqcup H_n)$ | $T_{\Omega}(X)^n\to T_{\Omega}(X)$ | hole substitution |
| Syntactic clone | finite variable terms | formal operations | superposition laws |
| Evaluation | $g:X\to |B|$ | $\operatorname{ev}_g$ | homomorphic extension |
| Generated image | $g:X\to |B|$ | $\langle g[X]\rangle_{\mathbf B}$ | image theorem |
| Kernel quotient | $\operatorname{ev}_g$ | $T_{\Omega}(X)/\ker(\operatorname{ev}_g)$ | first isomorphism |
| Descent | $\theta,F$ | $\overline F$ | $\theta\subseteq\ker F$ |

### 19.5. Final Compression

> [!theorem] Theorem 19.10: Single-Sentence Syntax Presentation Theorem
> Every faithful concrete syntax presentation for $(\Omega,X)$ is an absolutely free $\Omega$-algebra on $X$, hence is canonically isomorphic over $X$ to $\mathbf T_{\Omega}(X)$, and every invariant syntax operation transfers uniquely across such presentations.

> [!corollary] Corollary 19.11: Evaluation as Quotient of Syntax
> For every target $\Omega$-algebra $\mathbf B$ and valuation $g:X\to |B|$,
> 
> $$
> \langle g[X]\rangle_{\mathbf B}
> \cong
> \mathbf T_{\Omega}(X)/\ker(\operatorname{ev}_g).
> $$
> 
> Thus every generated concrete algebra obtained from a valuation is a homomorphic image of raw syntax.

> [!remark] Remark 19.12: Bridge to First-Order Logic
> In first-order logic, the function-symbol fragment of a language determines a finitary signature $\Omega$. The terms of the language form $\mathbf T_{\Omega}(X)$ for the chosen variable reservoir $X$. Relation symbols, equality atoms, connectives, quantifiers, binding, satisfaction, deductive calculi, theories, and models are then added on top of this algebraic term backbone.

> [!warning] Warning 19.13: What This Development Does Not Yet Include
> This development does not yet treat variable binding, free and bound variables in formulas, capture-avoiding substitution, atomic formulas, relation-symbol interpretation, satisfaction, semantic consequence, proof systems, or theories. Those require additional syntax layers beyond the one-sorted algebraic term machinery developed here.

## Appendix A. Compact Reference of Main Objects

### A.1. Carriers

| Object | Carrier | Role |
|---|---:|---|
| $\mathbf T_{\Omega}(X)$ | raw terms | invariant syntax |
| $\mathbf E_{\Omega}(X)$ | recursive expressions | displayed expression presentation |
| $\mathbf{Tr}_{\Omega}(X)$ | ranked addressed trees | structural and occurrence presentation |
| $\mathbf U_{\Omega}(X)$ | tagged tuples | set-theoretic code presentation |
| $\mathbf S_{\Omega}(X)$ | well-formed strings | textual presentation |
| $\mathbf B$ | semantic carrier | target algebra |
| $\mathbf T_{\Omega}(X)/\theta$ | equivalence classes | quotient syntax |

### A.2. Maps

| Map | Type | Meaning |
|---|---:|---|
| $\eta_X$ | $X\to T_{\Omega}(X)$ | variable insertion |
| $\widehat g$ | $\mathbf T_{\Omega}(X)\to\mathbf A$ | homomorphic extension |
| $\operatorname{ev}_g$ | $\mathbf T_{\Omega}(X)\to\mathbf B$ | evaluation |
| $\widehat{\sigma}$ | $\mathbf T_{\Omega}(X)\to\mathbf T_{\Omega}(Y)$ | substitution |
| $\iota^P$ | $\mathbf T_{\Omega}(X)\to\mathbf P$ | presentation isomorphism |
| $\operatorname{tr}_{P,Q}$ | $\mathbf P\to\mathbf Q$ | transfer |
| $\pi_{\theta}$ | $\mathbf T_{\Omega}(X)\to\mathbf T_{\Omega}(X)/\theta$ | quotient projection |
| $\operatorname{parse}$ | $\Sigma^{<\omega}\rightharpoonup T_{\Omega}(X)$ | syntactic parsing |
| $\operatorname{flat}$ | $T_{\Omega}(X)\to\Sigma^{<\omega}$ | string rendering |

### A.3. Failure Modes

> [!warning] Warning A.1: Main Failure Modes
> The principal failure modes in algebraic syntax are:
> 
> 1. identifying variables with constants;
> 2. treating concrete presentations as literally equal;
> 3. using ambiguous string notation without grammar data;
> 4. confusing parsing with evaluation;
> 5. assuming generatedness implies freeness;
> 6. quotienting by an arbitrary equivalence relation rather than a congruence;
> 7. defining functions on quotient syntax without checking descent;
> 8. confusing a valuation kernel with a clone kernel or equational theory;
> 9. treating implementation sharing as syntactic occurrence identity;
> 10. using semantic algebraic laws as if they were raw syntactic equalities.

## Appendix B. Minimal FOL Interface

### B.1. Function-Symbol Fragment

> [!definition] Definition B.1: Function-Symbol Signature of a First-Order Language
> Given a first-order language $L$, its function-symbol signature is the finitary signature $\Omega_L$ whose $n$-ary operation symbols are exactly the $n$-ary function symbols of $L$, including constant symbols as nullary function symbols.

> [!definition] Definition B.2: Term Algebra of a First-Order Language
> Let $L$ be a first-order language and $X$ a variable set. The term algebra of $L$ over $X$ is
> 
> $$
> \mathbf T_{\Omega_L}(X).
> $$

> [!remark] Remark B.3: Relation Symbols Are Not Operations on Terms
> An $n$-ary relation symbol $R$ of a first-order language does not define an operation
> 
> $$
> T_{\Omega_L}(X)^n\to T_{\Omega_L}(X).
> $$
> 
> Instead it contributes to atomic formula formation:
> 
> $$
> R(t_1,\ldots,t_n).
> $$

> [!warning] Warning B.4: Binding Is Not Present in Raw Term Algebra
> Quantifiers bind variables in formulas, not in ordinary first-order terms. Capture-avoiding substitution belongs to the formula layer and requires additional structure beyond the algebraic term syntax developed here.

### B.2. Semantic Interface

> [!definition] Definition B.5: Algebraic Reduct of an $L$-Structure
> Let $L$ be a first-order language and $\mathcal M$ an $L$-structure. The algebraic reduct of $\mathcal M$ is the $\Omega_L$-algebra $\mathbf M_{\operatorname{alg}}$ with carrier $|\mathcal M|$ and operations interpreting the function symbols of $L$.

> [!construction] Construction B.6: Term Evaluation in an $L$-Structure
> Let $\mathcal M$ be an $L$-structure, $X$ a set of variables, and $g:X\to |\mathcal M|$ an assignment. Term evaluation is the homomorphism
> 
> $$
> \operatorname{ev}_g:\mathbf T_{\Omega_L}(X)\to \mathbf M_{\operatorname{alg}}.
> $$

> [!remark] Remark B.7: Transition to Formula Semantics
> The value of a term under an assignment is an element of the structure. The truth value of a formula under an assignment requires relation-symbol interpretation, equality interpretation, Boolean connectives, quantifier clauses, and control of variable binding.
