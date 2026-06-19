---
title: "Theory Atlas — Algebraic Syntax into First-Order Logic"
subtitle: "A dense, object-level atlas. Universal algebra and algebraic syntax on the left; first-order logic developed as logic on the right; an exact transfer ledger between them."
tags: [theory-atlas, universal-algebra, algebraic-syntax, free-algebra, first-order-logic, binding, semantics, deduction, model-theory, obsidian]
obsidian-compatible-latex: true
---

# Theory Atlas — Algebraic Syntax into First-Order Logic

This atlas moves in three movements. **Part I** develops universal algebra and algebraic syntax as a self-contained engine room: signatures, algebras, free objects, presentations, substitution, contexts, evaluation, kernels, quotients, descent. **Part II** develops first-order logic faithfully *as logic* — language, terms, atoms, formulas, binding, semantics, deduction, theories, models — calling on the Part I machinery only at the exact points where logic genuinely runs on an algebraic engine. **Part III** is a synthesis layer: a ledger of engines, of map types, of equality notions, of the precise universal-algebra transfer points, and a final dependency map.

The atlas is read as a sequence of **rooms**. Each room names the objects now in play, places the engine exactly where it begins to do work, draws one compact hands-up graph, and hands forward what the next room consumes. Object entries display the object as a datum; the datum and the surrounding prose carry the species (set, family, algebra, map, relation, quotient, closure operator, semantic structure). There is no global type tag.

One slogan governs the whole stack:

$$
\boxed{\text{free algebra builds }\textbf{terms}\;;\quad\text{inductive closure builds }\textbf{formulas}\;;\quad\text{the term UMP interprets terms, structural recursion interprets formulas}\;;\quad\text{kernels measure collapse}\;;\quad\text{descent licenses quotients.}}
$$

And one standing correction, load-bearing throughout: **formulas are not a sort of `Σ_L`.** The functional signature carries only function symbols; relations, equality, connectives, and quantifiers do not contribute sorts or operations to `Σ_L`. Raw formulas form a *separate* inductive closure over the term algebra — and, if one wishes, the free algebra for their own formula-constructor signature. They are emphatically not elements of `T_{Σ_L}(\operatorname{Var})`. Consequently, terms are interpreted by the UMP of `T_{Σ_L}(\operatorname{Var})`; formula satisfaction is defined by structural recursion on the formula-constructor algebra. The Lindenbaum–Tarski quotient `LT(T)` is an algebra of formulas modulo provable equivalence — typically a Boolean (or cylindric/polyadic) algebra, but in general *not* a free one.

---

## Master development map

Universal algebra sits at the origin on the left; development flows rightward. UA is not *above* the logic — it is the source the logic half is drawn out of. Labelled edges are engine-driven moves.

```mermaid
flowchart LR
    subgraph UA["PART I · Universal algebra + algebraic syntax (the source)"]
        direction TB
        SIG["Σ"] -->|"⚙ construct"| FREE["T_Σ(X)"]
        FREE -->|"⚙ UMP / interpret"| CAP["recursion · substitution · evaluation"]
        FREE -->|"⚙ transfer"| PRES["presentations"]
        SIG --> CONG["θ, A/θ"]
        FREE -->|"⚙ collapse"| GEN["⟨X⟩ ≅ T_Σ(X)/ker"]
        CONG -->|"⚙ descend"| GEN
    end

    UA -->|"Σ ↦ Σ_L"| TERM["Term_L<br/>(instance of T_Σ(X))"]
    TERM -->|"layer change<br/>(closure, not algebra)"| FORM["Atom_L, Form_L^raw"]
    FORM -->|"⚙ alpha quotient"| BIND["Form_L, capture-avoiding subst"]

    TERM -->|"⚙ evaluate (target = structure)"| SEM["structures, ⊨"]
    BIND --> SEM
    UA -->|"⚙ descend"| QD["congruence / quotient /<br/>Lindenbaum–Tarski"]
    FORM --> QD

    SEM --> DED["⊢, soundness,<br/>Henkin completeness"]
    QD --> DED
    DED --> MT["theories,<br/>compactness, LS, types"]
    SEM --> MT
```

Three edges carry the integration. **`Σ ↦ Σ_L`**: the term layer *is* universal algebra by instantiation, no adaptation. **`Term_L → Atom_L`**: a layer change from a free algebra to an inductive closure, not another algebra. **`interpret`**: one engine reused with three targets — another free algebra (substitution), a structure (evaluation), another presentation (transfer).

---

# PART I · Universal Algebra and Algebraic Syntax

*The self-contained algebra of signatures, algebras, and free objects, then its syntax-theoretic life: presentations, substitution, contexts, evaluation, kernels, descent. No logic, no relation symbols as primitives, no formulas. This movement exports two things that never stop being used — the free algebra and the universal mapping property — plus the collapse-and-descent machinery the logic half quotients with.*

---

## I.0 · Sorting convention

*A standing convention, not a construction. Everything below is sorted; the one-sorted case is recovered by collapsing the sort set to a point. Single-sorted display is used when it is clearer, with the profiled wrapper given immediately wherever profile discipline matters.*

**`S`** · Sort set — the index of typed universes.

$$
S,\qquad\text{one-sorted}\iff S=\{*\}.
$$

**needs** nothing primitive · **yields** the index of every sorted family below · **links** base of `w`, `Σ`, `X`, and all carriers.

**`(X_s)`** · Sort-indexed family — a set assigned to each sort.

$$
X=(X_s)_{s\in S}.
$$

**needs** `S` · **yields** carriers, generator families, variable supplies · **links** maps between families act sortwise.

**`w`** · Profile / arity word — the finite input list of sorts an operation consumes.

$$
w=(s_1,\ldots,s_n)\in S^{<\omega},\qquad A_w:=A_{s_1}\times\cdots\times A_{s_n},\qquad A_{()}=1.
$$

**needs** `S` · **yields** the arity discipline; the domain of every operation · **links** input side of every operation symbol; relations later consume a profile but output no sort.

**`h:(A_s)\to(B_s)`** · Profile-correct map — a sortwise family of functions.

$$
h=(h_s:A_s\to B_s)_{s\in S}.
$$

**needs** two sorted families · **yields** the only shape a homomorphism, assignment, or substitution can take · **links** sort-correctness is the single discipline carried through the entire atlas.

> [!note] Translation rule
> Each later construction has a one-sorted display and a sortwise wrapper obtained by the same substitution everywhere: set $X\rightsquigarrow(X_s)$, carrier $A\rightsquigarrow(A_s)$, operation $A^n\to A\rightsquigarrow A_w\to A_s$, map $A\to B\rightsquigarrow(A_s\to B_s)$. Typed syntax is then nothing but sort-correct free syntax.

**Hands up.** `S`, sorted families, profiles, and profile-correct maps. Every signature, algebra, and term family in the rest of Part I is built over these.

---

## I.1 · Signatures and operation data

*The primitive datum of universal algebra: typed operation symbols. The room fixes what a signature is, where constants live, and how reducts and expansions move between signatures.*

**`Σ`** · Profiled signature — typed operation symbols sorted by input profile and output sort.

$$
\Sigma=\big(S,(\operatorname{Op}_{w,s})_{(w,s)\in S^{<\omega}\times S}\big),\qquad |\Sigma|:=\coprod_{(w,s)}\operatorname{Op}_{w,s}.
$$

For $f\in\operatorname{Op}_{w,s}$ write $f:w\to s$, with $\operatorname{in}(f)=w$, $\operatorname{out}(f)=s$.

**needs** `S`, pairwise-disjoint symbol sets · **yields** the notion of `Σ`-algebra and of free algebra · **links** instantiated as `Σ_L`, the functional reduct of a first-order language.

**`\operatorname{ar}(f)`** · Arity — the length of a symbol's input profile.

$$
\operatorname{ar}(f)=|w|\quad\text{for }f:w\to s.
$$

**needs** `Σ` · **yields** the closure-stage and unique-readability bookkeeping · **links** in the one-sorted case the profile collapses to a single natural number.

**`\operatorname{Op}_{(),s}`** · Nullary symbols / constants — operation symbols of empty profile.

$$
c\in\operatorname{Op}_{(),s}\ \Longleftrightarrow\ c:()\to s.
$$

**needs** `Σ` · **yields** atomic non-variable terms; named constants in algebras · **links** **constants are not a separate primitive** — they are exactly the empty-profile symbols.

**`X` vs `\operatorname{Op}_{(),s}`** · Generators versus constants — two ways an atomic element can enter syntax.

$$
\text{generator }x\in X_s\ \text{(free, replaceable)};\qquad \text{constant }c\in\operatorname{Op}_{(),s}\ \text{(fixed by the signature)}.
$$

**needs** `Σ`, a generator family `X` · **yields** the variable/constant distinction that powers substitution · **links** evaluation may move generators freely but must fix constants.

**`\Sigma\!\restriction` / `\Sigma\sqcup\Sigma'`** · Reduct / expansion — forgetting or adjoining symbols.

$$
\Sigma'\subseteq\Sigma\ \Rightarrow\ \text{every }\Sigma\text{-algebra has a }\Sigma'\text{-reduct};\qquad \Sigma\subseteq\Sigma''\ \Rightarrow\ \text{an expansion adds interpretations.}
$$

**needs** an inclusion of signatures · **yields** the reduct functor on algebras · **links** the functional reduct `Σ_L ⊆ L` is the key instance in the logic half.

> [!warning] Constants and variables
> $c\in\operatorname{Op}_{(),s}$ (a constant, fixed) and $x\in X_s$ (a generator, free) are different objects even when both are atomic terms. Confusing them breaks substitution and evaluation.

**Hands up.** `Σ` with its constants-as-nullary discipline, and the reduct relation. The next room interprets `Σ` in carriers.

---

## I.2 · Algebras and homomorphisms

*A signature acquires meaning in a carrier. This room introduces the objects interpretation maps into and the structure-preserving maps between them.*

**`\mathbf A`** · `Σ`-algebra — a sorted carrier interpreting every operation symbol.

$$
\mathbf A=\big(A,(f^{\mathbf A})_{f\in|\Sigma|}\big),\qquad A=(A_s)_{s\in S},\qquad f^{\mathbf A}:A_w\to A_s.
$$

**needs** `Σ` · **yields** the targets of homomorphisms, evaluation, and quotienting · **links** a first-order structure's algebraic reduct is one of these.

**`h:\mathbf A\to\mathbf B`** · Homomorphism — a profile-correct map commuting with every operation.

$$
h_s\big(f^{\mathbf A}(a_1,\ldots,a_n)\big)=f^{\mathbf B}\big(h_{s_1}(a_1),\ldots,h_{s_n}(a_n)\big)\quad(\forall f:w\to s).
$$

**needs** two `Σ`-algebras · **yields** isomorphisms, embeddings, kernels, images, composition · **links** out of a free algebra a homomorphism is determined by its generator values.

**`\cong`** · Isomorphism — a sortwise-bijective homomorphism.

$$
h:\mathbf A\xrightarrow{\cong}\mathbf B\iff\text{each }h_s\text{ bijective and }h\text{ a hom.}
$$

**needs** a `hom` · **yields** identification of algebras up to relabelling · **links** generator-preserving isomorphisms are the rigidity used in transfer.

**`\theta_X`-preserving `\cong`** · Generator-preserving isomorphism — an iso fixing a chosen generating set.

$$
h\circ\iota_X=\iota'_X.
$$

**needs** two algebras with marked generators · **yields** the uniqueness that makes free objects canonical · **links** any two faithful presentations of syntax meet via exactly one of these.

> [!result] Core homomorphism facts
> - Composition of homomorphisms is a homomorphism; identities are homomorphisms.
> - The image of a homomorphism is a subalgebra of the codomain.
> - A homomorphism out of a generated algebra is determined by its values on the generators.

**Hands up.** `Σ-Alg`, `hom`, and generator-preserving `≅`. The next room asks which subcarriers are closed, and what a generating set generates.

---

## I.3 · Subalgebras and generated structure

*Closure under operations is the first least-fixed-point construction in the atlas. It produces generated subalgebras, supplies structural induction, and separates two notions that are often conflated — generatedness and freeness.*

**`B\leq\mathbf A`** · Subuniverse / subalgebra — a sorted subset closed under all operations.

$$
B=(B_s)_{s\in S},\qquad f^{\mathbf A}(B_w)\subseteq B_s\ (\forall f:w\to s).
$$

**needs** `\mathbf A` · **yields** the lattice of subalgebras; the codomain of generation · **links** images of homomorphisms are subalgebras.

**`\langle X\rangle_{\mathbf A}`** · Generated subalgebra — the least subuniverse containing `X`.

$$
\langle X\rangle_{\mathbf A}=\bigcap\{B\leq\mathbf A:X\subseteq B\}=\bigcup_{n<\omega}X^{(n)},
$$

$$
X^{(0)}=X,\qquad X^{(n+1)}_s=X^{(n)}_s\cup\{f^{\mathbf A}(\vec a):f:w\to s,\ \vec a\in (X^{(n)})_w\}.
$$

**needs** `\mathbf A`, a sorted subset `X` · **yields** finite generation; induction over generated objects · **links** = the image of evaluation $\widehat g$ on the values of the variables.

**`X^{(n)}`** · Finitary stage closure — the stratified construction of `⟨X⟩`.

$$
\langle X\rangle_{\mathbf A}=\bigcup_{n<\omega}X^{(n)}.
$$

**needs** the one-step operation closure · **yields** an induction principle: prove a property on `X` and through each operation · **links** the same stratification generates congruences and (formally) term carriers.

**`\operatorname{im}(h)`** · Homomorphic image — the subalgebra reached by a homomorphism.

$$
\operatorname{im}(h)=\langle h[X]\rangle_{\mathbf B}\quad\text{when }X\text{ generates }\mathbf A.
$$

**needs** a `hom` · **yields** the image side of every factorization · **links** = $\langle g[X]\rangle$ for an evaluation, the bridge to the kernel quotient.

> **`gen-closure`** ⚙ **ENGINE** · Generated closure
>
> The least subuniverse containing `X` exists and is computed by stages; "closed under the operations and containing the generators" is a valid induction hypothesis.
>
> $$
> P(x)\ (\forall x\in X)\ \wedge\ \big[P(a_i)\,\forall i\Rightarrow P(f^{\mathbf A}(\vec a))\big]\ \Longrightarrow\ P\ \text{on }\langle X\rangle_{\mathbf A}.
> $$
>
> **drives** generators ⟶ everything they generate.
> **powered by** least-fixed-point existence for a monotone one-step closure.
> **enables** structural induction; the image description of homomorphisms; the formal carrier of term algebras.

> [!warning] Generatedness ≠ freeness
> `⟨X⟩` says $X$ *reaches* everything (induction works). Freeness will say in addition that $X$ reaches everything *uniquely* (recursion works). Generatedness is necessary for both; freeness is the extra unique-reading condition introduced in I.5–I.6.

```mermaid
flowchart LR
    A["Σ-Alg A"] --> SUB["B ≤ A"]
    X["generators X"] -->|"⚙ gen-closure"| GEN["⟨X⟩ = ⋃ X^(n)"]
    GEN -->|"induction"| IND["prove on X, through ops"]
    GEN -. "= im of evaluation" .-> IMG["⟨g[X]⟩ (I.16)"]
```

**Hands up.** The generated-closure engine and the generatedness/freeness distinction. The next room turns closure on relations into congruences and quotients.

---

## I.4 · Kernels, congruences, and quotients

*Closure applied to relations produces congruences; congruences license quotients. This room builds the kernel–congruence–quotient cycle and closes it with the first isomorphism theorem, the universal hinge between maps and quotients.*

**`\ker h`** · Kernel of a homomorphism — the pairs a map identifies.

$$
a\,(\ker h)_s\,b\iff h_s(a)=h_s(b).
$$

**needs** a `hom` · **yields** the measure of how much `h` collapses · **links** kernels are exactly congruences; the input to factorization.

**`\theta`** · Congruence — an operation-compatible equivalence.

$$
\theta=(\theta_s)_{s\in S},\qquad a_i\,\theta_{s_i}\,b_i\ (\forall i)\ \Longrightarrow\ f^{\mathbf A}(\vec a)\,\theta_s\,f^{\mathbf A}(\vec b).
$$

**needs** `\mathbf A` · **yields** the quotient `A/θ`; the descent obligation · **links** carrier of all collapse phenomena in the atlas.

**`\operatorname{Cg}(R)`** · Congruence generated by a relation — the least congruence containing `R`.

$$
\operatorname{Cg}(R)=\bigcap\{\theta\in\operatorname{Con}(\mathbf A):R\subseteq\theta\}.
$$

**needs** a relation `R` on a carrier · **yields** presented congruences; equational closures · **links** another least-closure object, like `⟨X⟩` for relations.

**`\mathbf A/\theta`** · Quotient algebra — the algebra of equivalence classes.

$$
(\mathbf A/\theta)_s=A_s/\theta_s,\qquad f^{\mathbf A/\theta}([a_1],\ldots,[a_n])=[\,f^{\mathbf A}(\vec a)\,].
$$

**needs** a congruence `θ` · **yields** representative-level computation · **links** every "syntax modulo equivalence" object is an instance of this.

**`q_\theta`** · Quotient projection — the class map.

$$
q_\theta:\mathbf A\to\mathbf A/\theta,\qquad a\mapsto[a]_\theta.
$$

**needs** `A/θ` · **yields** the surjection every quotient construction factors through · **links** $\ker q_\theta=\theta$.

> **`first-iso`** ⚙ **ENGINE** · First isomorphism theorem
>
> A homomorphism factors through a quotient exactly when the quotient relation is below its kernel, and its image is the quotient by its own kernel.
>
> $$
> \theta\subseteq\ker h\ \Longrightarrow\ h\ \text{factors as}\ \bar h\circ q_\theta;\qquad \mathbf A/\ker h\ \cong\ \operatorname{im}(h).
> $$
>
> **drives** map ⟶ quotient-by-kernel description of its image.
> **powered by** kernels are congruences plus representative-independence of the induced map.
> **enables** generated algebras as syntax-modulo-equations (I.17), term models, Lindenbaum–Tarski.

> [!result] Core quotient facts
> - Kernels of homomorphisms are congruences.
> - Quotient operations are well-defined exactly because `θ` respects every operation.
> - `h` factors through `A/θ` iff `θ ⊆ ker h`.
> - `A/ker h ≅ im(h)`.

```mermaid
flowchart LR
    H["hom h: A→B"] -->|"ker"| KER["θ = ker h (a congruence)"]
    KER --> QUOT["A/θ"]
    A["A"] -->|"q_θ"| QUOT
    QUOT -->|"⚙ first-iso"| IMG["A/ker h ≅ im(h)"]
    R["relation R"] -. "Cg(R)" .-> KER
```

**Hands up.** Congruences, quotients, the projection `q_θ`, and the first-iso engine. The next room produces the object the whole atlas turns on: the free algebra.

---

## I.5 · Free algebras and the universal mapping property

*The central room of Part I. A free algebra is a generated algebra with no relations among its generators beyond those the operations force. Its defining property — the UMP — is the single engine behind recursion, substitution, evaluation, and transfer.*

**`\eta`** · Generator insertion — variables placed as atomic elements.

$$
\eta=(\eta_s:X_s\hookrightarrow \mathrm T_\Sigma(X)_s)_{s\in S}.
$$

**needs** the carrier of the free algebra · **yields** the comparison condition $\widehat g\circ\eta=g$ that pins extensions down · **links** each $\eta_s$ is injective; its image generates.

**`\mathbf T_\Sigma(X)`** · Free algebra on `X` — the syntax object.

$$
(\mathbf T_\Sigma(X),\eta),\qquad \mathrm T_\Sigma(X)=(\mathrm T_\Sigma(X)_s)_{s\in S}.
$$

**needs** `Σ`, sorted generators `X` · **yields** formal syntax, structural recursion, substitution, evaluation, transfer · **links** the canonical logic-side instance is $\mathbf{Term}_L$.

> **`UMP`** ⚙ **ENGINE** · Universal mapping property
>
> Every sorted assignment of generators into a target algebra extends to a *unique* homomorphism agreeing with it on generators.
>
> $$
> g:X\to U\mathbf A\ \Longrightarrow\ \exists!\,\widehat g:\mathbf T_\Sigma(X)\to\mathbf A\ \text{with}\ \widehat g\circ\eta=g,
> $$
>
> $$
> \operatorname{Hom}_\Sigma(\mathbf T_\Sigma(X),\mathbf A)\ \cong\ \operatorname{Set}^S(X,U\mathbf A).
> $$
>
> **drives** generator assignment ⟶ unique interpretation of all syntax.
> **powered by** existence (least closure builds the carrier) plus freeness (unique reading makes the extension single-valued).
> **enables** the *same* mechanism at four targets — syntax (substitution, I.10), a semantic algebra (evaluation, I.16), another presentation (transfer, I.9), and the kernel quotient (I.17). One theorem, four tools, distinguished only by the target.

> [!result] Freeness package
> - **Existence**: `T_Σ(X)` exists for every `Σ`, `X`.
> - **Uniqueness over generators**: the extension `ĝ` is the only homomorphism with `ĝ∘η = g`.
> - **Generatedness**: `η(X)` generates `T_Σ(X)`; induction over generators is valid.
> - **Rigidity**: any two free algebras on `X` are isomorphic by a *unique* generator-preserving isomorphism.
> - **Sorted UMP**: the statement holds verbatim with `X`, `A`, `g`, `ĝ` read sortwise — many-sortedness changes nothing but the bookkeeping.

```mermaid
flowchart LR
    SIG["Σ"] --> FREE["T_Σ(X) + η"]
    X["X"] --> FREE
    FREE -->|"⚙ UMP"| USE["recursion · substitution · evaluation · transfer"]
    G["g: X→A"] --> EXT["ĝ: T_Σ(X)→A"]
    FREE --> EXT
    FREE -. "instance" .-> TERM["Term_L (II.2)"]
```

**Hands up.** `T_Σ(X)`, `η`, the UMP, and the recursion/induction asymmetry (induction needs generatedness; recursion needs freeness). The next room realizes this abstract free object as raw term syntax.

---

## I.6 · Raw term algebras

*The free algebra realized concretely: formal expressions built from variables and operation symbols. The room certifies that this construction is free — unique readability is exactly the no-confusion condition that turns generated syntax into recursive syntax.*

**`\operatorname{Term}`** · Formal term formation — the inductively generated expression family.

$$
x\in X_s\Rightarrow x\in\operatorname{Term}_s,\qquad c\in\operatorname{Op}_{(),s}\Rightarrow c\in\operatorname{Term}_s,
$$

$$
f:w\to s,\ t_i\in\operatorname{Term}_{s_i}\Rightarrow f(t_1,\ldots,t_n)\in\operatorname{Term}_s.
$$

**needs** `Σ`, `X` · **yields** the carrier of `T_Σ(X)`; variable, constant, and compound terms · **links** least closure under the formal constructors.

**`f^{\mathbf T}`** · Formal constructor operation — the operation symbol acting as a syntax builder.

$$
f^{\mathbf T}(t_1,\ldots,t_n):=f(t_1,\ldots,t_n).
$$

**needs** term formation · **yields** the algebra structure on `Term` making it a `Σ`-algebra · **links** $f^{\mathbf T}$ is injective with range disjoint from variables and from other symbols' ranges.

**`\cong`-to-`T_\Sigma(X)`** · Term algebra is the free algebra — the certification.

$$
(\operatorname{Term},(f^{\mathbf T}))\ \cong\ \mathbf T_\Sigma(X)\quad\text{over }X.
$$

**needs** term formation as a `Σ`-algebra · **yields** all UMP consequences for concrete terms · **links** the abstract `T_Σ(X)` and concrete `Term` are identified by their shared UMP.

> **`unique-read`** ⚙ **ENGINE** · Unique readability
>
> Every non-variable term decomposes uniquely as a top symbol applied to an argument tuple; variables, constants, and compounds are pairwise distinguishable.
>
> $$
> f(\vec t)=g(\vec u)\ \Longrightarrow\ f=g,\ \vec t=\vec u;\qquad \text{no variable is a compound.}
> $$
>
> **drives** generated syntax ⟶ *freely* generated syntax.
> **powered by** the disjoint-range / injective-constructor conditions on $f^{\mathbf T}$ (no-confusion).
> **enables** structural recursion: define a function by one clause per constructor and it is well-defined and total.

> [!warning] Syntax equality vs semantic equality
> $f(t)=g(u)$ as *terms* means the same expression (decided by unique readability). $f^{\mathbf A}(a)=g^{\mathbf A}(b)$ as *values* in an algebra is a different relation, decided by the algebra. The whole evaluation/kernel story (I.16–I.17) measures the gap between them.

```mermaid
flowchart LR
    SIG["Σ"] --> FORM["formal terms"]
    X["X"] --> FORM
    FORM --> CONS["f^T constructors"]
    CONS -->|"⚙ unique-read"| FREE["≅ T_Σ(X)"]
    FREE --> RECUR["structural induction · recursion"]
    FREE -. "presented by" .-> CARRIERS["trees · strings · tuples (I.8)"]
```

**Hands up.** A concrete free term carrier and the unique-readability engine that makes recursion legal. The next room abstracts the certification: which *candidate* carriers count as free syntax.

---

## I.7 · Constructor presentations and free-syntax certification

*A general test for "is this concrete carrier the free syntax?" without re-deriving everything by hand. The criterion is two conditions — no-junk and no-confusion — that together force a candidate carrier to be isomorphic to the abstract term algebra over the generators.*

**`(\mathbf P,\iota,(c_f))`** · Constructor system — a candidate carrier with an insertion and a builder per symbol.

$$
\iota:X\to P,\qquad c_f:P_w\to P_s\ \ (f:w\to s).
$$

**needs** a sorted set `P`, maps `ι`, `c_f` · **yields** a candidate `Σ`-algebra on `P` · **links** trees, strings, tuples, and ASTs are all constructor systems.

**`\rho`** · Comparison map — the canonical homomorphism from abstract syntax.

$$
\rho:\mathbf T_\Sigma(X)\to\mathbf P,\qquad \rho\circ\eta=\iota\quad(\text{by UMP}).
$$

**needs** a constructor system · **yields** the single map whose bijectivity decides faithfulness · **links** always exists and is unique; the only question is whether it is an isomorphism.

**no-junk** · Generatedness of the candidate — `ι(X)` generates `P` under the `c_f`.

$$
\langle \iota(X)\rangle_{\mathbf P}=P\quad\Longleftrightarrow\quad \rho\ \text{surjective.}
$$

**needs** the constructor system · **yields** surjectivity of `ρ` · **links** "no extra elements outside what the constructors build."

**no-confusion** · Injectivity of constructors — distinct builds give distinct elements.

$$
c_f\ \text{injective, ranges disjoint, disjoint from }\iota(X)\quad\Longrightarrow\quad \rho\ \text{injective.}
$$

**needs** the constructor system · **yields** injectivity of `ρ` · **links** the abstract form of unique readability. The converse can fail when the candidate carrier `P` contains *junk* on which constructors collide outside the image of `ρ`: globally, no-confusion is strictly stronger than `ρ`-injectivity. Equivalence is restored after no-junk (then constructor injectivity and disjointness are equivalent to `ρ`-injectivity), or by restricting attention to the generated subalgebra $\langle\iota(X)\rangle_{\mathbf P}$.

> **`constructor-cert`** ⚙ **ENGINE** · Free-syntax certification
>
> A constructor system is a faithful presentation of free syntax exactly when it satisfies no-junk and no-confusion; then the comparison map is an isomorphism over the generators.
>
> $$
> \text{no-junk}\ \wedge\ \text{no-confusion}\ \Longrightarrow\ \rho:\mathbf T_\Sigma(X)\xrightarrow{\cong}\mathbf P.
> $$
>
> **drives** candidate carrier ⟶ certified free syntax.
> **powered by** surjectivity from generatedness, injectivity from constructor disjointness, both routed through the UMP.
> **enables** defining once on abstract syntax and transporting to any certified carrier (I.9).

```mermaid
flowchart LR
    CAND["constructor system (P, ι, c_f)"] -->|"UMP"| RHO["ρ: T_Σ(X)→P"]
    NJ["no-junk"] --> RHO
    NC["no-confusion"] --> RHO
    RHO -->|"⚙ constructor-cert"| ISO["ρ iso ⇒ P is free syntax"]
```

**Hands up.** The certification engine and the no-junk/no-confusion criterion. The next room runs it on the standard concrete carriers.

---

## I.8 · Concrete syntax carriers

*The carriers people actually compute with. Each is a constructor system; each is certified free by the previous room. The room's real content is the distinction between a carrier and the invariant syntax object it presents.*

**`\mathrm{Expr}`** · Recursive expression syntax — terms as nested constructor applications.

$$
\mathrm{Expr}\ni f(t_1,\ldots,t_n),\quad t_i\in\mathrm{Expr}.
$$

**needs** a constructor system on expressions · **yields** the default inductive datatype carrier · **links** certified free by no-junk/no-confusion.

**`\mathrm{Tree}`** · Tree syntax — labelled ordered trees, symbol at each node, children = arguments.

$$
\text{node label }f:w\to s,\quad \deg=|w|.
$$

**needs** ordered labelled trees over `|Σ| ∪ X` · **yields** positions, subterms, occurrences (I.12) · **links** the carrier that exposes addresses; faithful as an algebra.

**`\mathrm{AddrTree}`** · Addressed syntax trees — trees with explicit position addresses.

$$
\text{position}\ p\in\mathbb N^{<\omega},\quad t|_p=\text{subtree at }p.
$$

**needs** `Tree` plus an addressing scheme · **yields** positional surgery; replacement · **links** addresses are presentation-bound, not invariant syntax data.

**`\mathrm{Tup}`** · Tagged-tuple syntax — terms as tagged tuples $(f,t_1,\ldots,t_n)$.

$$
(f,\vec t),\quad f:w\to s.
$$

**needs** disjoint tagging · **yields** a set-theoretic carrier with trivial unique readability · **links** the von Neumann-style explicit encoding.

**`\mathrm{Str}`** · String syntax — terms as parenthesized symbol strings.

$$
f(t_1,\ldots,t_n)\ \text{as a string over an alphabet.}
$$

**needs** a parsing/hygiene discipline (matched delimiters, unique parse) · **yields** an I/O carrier · **links** faithful only once parsing is unambiguous.

**`\mathrm{DAG}`** · DAG / implementation carrier — shared-subterm representation.

$$
\text{shared node}\ \Rightarrow\ \text{one node for repeated subterms.}
$$

**needs** a hashing/sharing scheme · **yields** an efficient carrier · **links** sharing identity is presentation-bound; the underlying term is the invariant.

> [!warning] Carrier vs syntax object
> A tree, a string, a tuple, and a DAG can all present the *same* term. Statements about addresses, substrings, parse stacks, pointer identity, or sharing are about the carrier, not the term. Only what is definable from the algebra structure and `η` is invariant syntax.

```mermaid
flowchart LR
    ABS["abstract syntax T_Σ(X)"] -. "presented by" .-> EXPR["Expr"]
    ABS -. .-> TREE["Tree / AddrTree"]
    ABS -. .-> TUP["Tup"]
    ABS -. .-> STR["Str"]
    ABS -. .-> DAG["DAG"]
    TREE --> POS["positions · addresses (presentation-bound)"]
```

**Hands up.** A family of certified carriers and the carrier/invariant distinction. The next room makes "define once, transport everywhere" precise.

---

## I.9 · Presentation-neutral syntax and transfer

*Syntax is the abstract free object; the carriers of I.8 are its presentations. This room exports the licence to define a construction once, on whichever carrier is convenient, and transport it to all of them by conjugation — together with the exact boundary of what transports.*

**`abstract syntax`** · The invariant object — `T_Σ(X)` up to unique generator-preserving isomorphism.

$$
\mathbf T_\Sigma(X)\ \text{considered up to the unique }\theta\text{ over }X.
$$

**needs** `Σ`, `X` · **yields** the definitions all presentations must agree on · **links** operations, induction, recursion, substitution, contexts live here; addresses and pointers do not.

**`\mathcal P=(\mathbf P,\iota,\rho)`** · Faithful presentation — a certified concrete model.

$$
\rho:\mathbf T_\Sigma(X)\xrightarrow{\cong}\mathbf P,\qquad \rho\circ\eta=\iota.
$$

**needs** a constructor system passing certification (I.7) · **yields** a usable carrier · **links** faithful iff `ρ` is an isomorphism.

**`\tau_{P,Q}`** · Transfer map between presentations — the canonical carrier comparison.

$$
\tau_{P,Q}:=\rho_Q\circ\rho_P^{-1}:\mathbf P\xrightarrow{\cong}\mathbf Q.
$$

**needs** two faithful presentations · **yields** the unique generator-preserving comparison · **links** instance of rigidity.

**presentation-bound data** · Encoding-specific structure that does not transfer.

$$
\text{tree address},\quad \text{string index},\quad \text{pointer identity},\quad \text{DAG sharing}.
$$

**needs** a chosen carrier · **yields** useful notation/implementation data · **links** quarantined unless an invariance theorem ties it back.

> **`transfer`** ⚙ **ENGINE** · Conjugation across presentations
>
> An invariant operation on abstract syntax transports to any faithful presentation by conjugation, and all comparison isomorphisms commute.
>
> $$
> F_{\mathcal P}:=\rho\circ F\circ(\rho^{-1})^{\times n};\qquad \tau_{P,Q}\big(F_P(\vec p)\big)=F_Q\big(\tau_{P,Q}(\vec p)\big).
> $$
>
> **drives** invariant definition ⟶ presentation-level operation.
> **powered by** rigidity: any two faithful presentations are uniquely isomorphic over `X`.
> **enables** proving operations, substitution, contexts, induction, recursion *once*; frees logic from caring what a term "really is."

> [!result] Invariance criterion
> A construction transfers iff it is preserved by every generator-preserving isomorphism. Operations, substitution, evaluation, and contexts pass. Positions and addresses fail — which is exactly why positional surgery (I.12) needs a chosen carrier and reappears only where binding demands occurrences.

```mermaid
flowchart LR
    ABS["abstract syntax = T_Σ(X)"] -->|"⚙ transfer"| PRES["faithful presentation (P, ι, ρ)"]
    PRES -. "faithful = ρ iso" .-> ABS
    PRES --> CARRY["operations · subst · contexts (transport)"]
    PRES --> BOUND["positions · addresses (presentation-bound)"]
```

**Hands up.** Abstract syntax, faithful presentations, the transfer engine, and the invariance criterion. Every later construction is defined on the abstract object; carriers are chosen only for convenience. The next room defines the first such construction — substitution.

---

## I.10 · Substitution as syntax-valued evaluation

*The first reuse of the UMP with a syntactic target. Substitution is not textual replacement: it is the unique homomorphism extending a syntax-valued assignment. Its laws — identity, composition, evaluation compatibility — are exactly the monad laws of free syntax.*

**`\sigma`** · Syntax-valued assignment — variables sent to terms.

$$
\sigma:X\to U\mathbf T_\Sigma(Y).
$$

**needs** `T_Σ(Y)` · **yields** the data substitution extends · **links** in logic $X=Y=\operatorname{Var}$.

**`\widehat\sigma`** · Substitution extension — the homomorphism it induces.

$$
\widehat\sigma:\mathbf T_\Sigma(X)\to\mathbf T_\Sigma(Y),\qquad \widehat\sigma\circ\eta_X=\sigma.
$$

**needs** `σ`, the UMP · **yields** substitution as a structure-preserving map · **links** the first exact reuse of `interpret` with a syntactic target.

**`\eta_X`** · Identity substitution — generators to themselves.

$$
\widehat{\eta_X}=\operatorname{id}_{\mathbf T_\Sigma(X)}.
$$

**needs** `η` · **yields** the unit law · **links** the monad unit.

**`\tau\star\sigma`** · Kleisli composition — substitute, then substitute.

$$
(\tau\star\sigma)(x):=\widehat\tau(\sigma(x)),\qquad \widehat{\tau\star\sigma}=\widehat\tau\circ\widehat\sigma.
$$

**needs** `σ:X→T(Y)`, `τ:Y→T(Z)` · **yields** associativity of substitution · **links** the monad multiplication; renaming is the special case where `σ` lands in `η(Y)`.

> **`subst`** ⚙ **ENGINE** · Substitution = evaluation into syntax
>
> A substitution is the homomorphic extension of a syntax-valued assignment; composing substitutions is interpreting one inside another.
>
> $$
> \widehat{\eta_X}=\operatorname{id},\qquad \widehat{\tau\star\sigma}=\widehat\tau\circ\widehat\sigma,\qquad \operatorname{ev}_v\circ\widehat\sigma=\operatorname{ev}_{v\star\sigma}.
> $$
>
> **drives** assignment `X→T(Y)` ⟶ map `T(X)→T(Y)`.
> **powered by** the UMP with target a free algebra.
> **enables** the substitution lemma, context plugging (I.11), clone superposition (I.14), and the term monad.

> [!result] Four-corner calculus
> For $\sigma:X\to T(Y)$, $v:Y\to A$, $h:\mathbf A\to\mathbf B$, every composite of substitution, evaluation, and homomorphism normalizes to a single evaluation:
> $$
> \operatorname{ev}_v\circ\widehat\sigma=\operatorname{ev}_{v\star\sigma},\qquad h\circ\operatorname{ev}_g=\operatorname{ev}_{h\circ g}.
> $$
> Both faces are the UMP's uniqueness applied to a map that agrees with an evaluation on generators.

```mermaid
flowchart LR
    SIGMA["σ: X→T(Y)"] -->|"⚙ subst"| EXT["σ̂: T(X)→T(Y)"]
    EXT --> MONAD["term monad: unit η, mult μ"]
    EXT --> KLEISLI["composition τ̂∘σ̂ = (τ⋆σ)^"]
    EXT -->|"ev_v ∘ σ̂ = ev_{v⋆σ}"| LEMMA["substitution lemma"]
```

**Hands up.** Substitution, its monad laws, and the four-corner calculus. The next room exposes holes inside syntax so that substitution can act at marked positions.

---

## I.11 · Contexts, holes, and plugging

*A context is a term with marked holes. Plugging a context is substitution restricted to the hole variables while ordinary variables stay fixed. Context composition is associative because substitution is. No tree address is needed — holes are just a distinguished generator family.*

**`H` / `E_n`** · Hole variables — a distinguished sorted family of generators.

$$
H=(H_s)_{s\in S},\qquad E_n=\{\square_1,\ldots,\square_n\}.
$$

**needs** `S` · **yields** marked positions as generators · **links** holes are ordinary generators kept disjoint from `X`.

**`\operatorname{Ctx}_H(X)`** · Hole-extended syntax — terms over variables and holes.

$$
\operatorname{Ctx}_H(X):=\mathbf T_\Sigma(X\sqcup H).
$$

**needs** the coproduct generator family · **yields** the carrier of contexts · **links** a one-hole context uses a single distinguished generator in one sort.

**`C[\,\square_1,\ldots,\square_n\,]`** · Multi-hole context — an element of hole-extended syntax.

$$
C\in\mathbf T_\Sigma(X\sqcup E_n)_s.
$$

**needs** `Ctx_H(X)` · **yields** the object plugging acts on · **links** repeated holes give nonlinear contexts; distinct holes used once give linear contexts.

**`C[\vec t]`** · Plugging — fill holes, keep variables fixed.

$$
\alpha:H\to U\mathbf T_\Sigma(X),\qquad C[\alpha]:=\widehat\sigma(C)\ \text{with}\ \sigma|_X=\eta_X,\ \sigma|_H=\alpha.
$$

**needs** a context and a sorted filling · **yields** the filled term · **links** plugging *is* substitution at holes.

> **`plug`** ⚙ **ENGINE** · Plugging = substitution at holes
>
> Filling the holes of a context is the substitution that maps holes to fillings and fixes ordinary variables.
>
> $$
> C[\alpha]=\widehat{(\eta_X\sqcup\alpha)}(C).
> $$
>
> **drives** context + filling ⟶ filled term.
> **powered by** the coproduct generator family `X ⊔ H` and the substitution engine.
> **enables** context composition, induced (polynomial) operations, and congruence tests by unary contexts.

> [!result] Context laws
> - **Composition**: $(C\circ D)[\alpha]=C[\,D[\alpha]\,]$ — associative because substitution is associative.
> - **Distribution**: substitution distributes over plugging, $\widehat\sigma(C[\alpha])=(\widehat\sigma C)[\widehat\sigma\circ\alpha]$.
> - **Identity context**: a single hole $\square$ is the identity for composition.
> - In the **single-sorted** case, one-hole contexts under composition form a monoid acting on syntax. In the **many-sorted** case (I.13), one-hole contexts form a *category* whose objects are sorts and whose arrows are one-hole contexts with matching hole and output sorts; endo-contexts at a fixed sort then form a monoid; multi-hole contexts form a *multicategory* (coloured operad) whose colours are sorts.

```mermaid
flowchart LR
    HOLES["holes H"] --> CTX["Ctx_H(X) = T(X⊔H)"]
    CTX -->|"⚙ plug"| FILLED["C[α] = filled term"]
    ALPHA["filling α: H→T(X)"] --> FILLED
    CTX --> COMP["context composition (monoid)"]
    CTX -. "presented by" .-> TREE["one-hole tree contexts (I.12)"]
```

**Hands up.** Holes, contexts, plugging, and the context monoid. The next room gives the concrete tree picture of contexts — the one place where positional data legitimately enters.

---

## I.12 · Trees, positions, extraction, and replacement

*The presentation-bound room. On a tree carrier, terms acquire positions; subterm extraction, context extraction, and replacement become available. These are exactly the constructions the invariance criterion quarantined — useful, but defined on a chosen carrier.*

**`p`** · Tree position — an address in a term tree.

$$
p\in\mathbb N^{<\omega},\qquad \varepsilon\ \text{the root.}
$$

**needs** a tree presentation · **yields** the index set for subterms and occurrences · **links** presentation-bound; does not transfer.

**`t|_p`** · Subtree extraction — the subterm at a position.

$$
t|_\varepsilon=t,\qquad f(t_1,\ldots,t_n)|_{i\cdot p}=t_i|_p.
$$

**needs** a position in a term · **yields** occurrences and the subterm partial order · **links** feeds replacement and context extraction.

**`C_{t,p}`** · Context extraction at a position — the one-hole context left by removing a subterm.

$$
t=C_{t,p}[\,t|_p\,].
$$

**needs** a term and a position · **yields** the master decomposition of a term into context plus subterm · **links** reconciles the carrier-free context (I.11) with the tree picture.

**`t[p:=u]`** · Replacement at a position — substitute one subterm.

$$
t[p:=u]:=C_{t,p}[u].
$$

**needs** a term, a position, a replacement (sort-matched) · **yields** local surgery on syntax · **links** = plugging the extracted context.

> [!result] Master decomposition
> Every term factors as $t=C_{t,p}[t|_p]$: a one-hole context times the subterm at `p`. Replacement is plugging; extraction is its inverse. Address arithmetic under plugging composes positions: filling at `p` then reading at `q` reads at `p·q`.

> [!warning] Tree-relative vs carrier-free
> The *context object* $C_{t,p}$ is invariant (it is a one-hole context, I.11). The *position* `p` and the address arithmetic are tree-relative. Keep the invariant context separate from the address that produced it.

```mermaid
flowchart LR
    TREE["term as tree"] --> POS["position p"]
    POS --> SUB["subtree t|_p"]
    POS --> CTX["context C_{t,p}"]
    SUB --> DECOMP["t = C_{t,p}[t|_p]"]
    CTX --> DECOMP
    DECOMP --> REPL["replacement t[p:=u] = C_{t,p}[u]"]
    CTX -. "is invariant" .-> ONEHOLE["one-hole context (I.11)"]
```

**Hands up.** Positions, extraction, the master decomposition, and replacement — with the invariant context separated from its address. The next room types the holes, making contexts profile-aware.

---

## I.13 · Typed contexts and sort-correct filling

*The many-sorted wrapper for contexts. Holes carry sorts; a context carries an input profile and an output sort; filling is legal only when sorts match. This is the profile discipline of I.0 applied to plugging — the same engine, sort-indexed.*

**`\square_i:s_i`** · Typed holes — holes tagged by sort.

$$
H=(H_s)_{s\in S},\qquad \square_i\in H_{s_i}.
$$

**needs** `S` · **yields** sort-tagged marked positions · **links** a hole of sort `s` accepts only terms of sort `s`.

**`C:(s_1,\ldots,s_n)\Rightarrow s`** · Context profile — input hole sorts and output sort.

$$
C\in\mathbf T_\Sigma(X\sqcup\{\square_1{:}s_1,\ldots,\square_n{:}s_n\})_s.
$$

**needs** typed holes · **yields** the typing judgement for contexts · **links** the arrow `⇒` records hole profile and output sort.

**`C[\vec t]`** · Sort-correct filling — plugging that respects sorts.

$$
t_i\in\mathbf T_\Sigma(X)_{s_i}\ \Longrightarrow\ C[t_1,\ldots,t_n]\in\mathbf T_\Sigma(X)_s.
$$

**needs** a typed context, sort-matched fillings · **yields** a well-typed filled term · **links** ill-typed filling is simply not defined.

**`C\circ D`** · Profiled context composition — output sort meets matching hole sort.

$$
\big[(s_1,\ldots,s_n)\Rightarrow s\big]\circ\big[(r_1,\ldots,r_m)\Rightarrow s_i\big]\ \text{plugs at hole }i.
$$

**needs** composable profiles · **yields** for one-hole contexts ($n=1$), a category whose **objects are sorts** and whose arrows are typed one-hole contexts; for multi-hole contexts, a **multicategory (coloured operad)** whose colours are sorts and whose multi-arrows are typed contexts of profile $(s_1,\ldots,s_n)\Rightarrow s$ · **links** the typed analogue of the single-sorted context monoid; the one-hole, fixed-sort endo-arrows reduce to a monoid.

> [!result] Sorted plugging
> Typed plugging is sort-indexed substitution: it is exactly the engine of I.11 with `X ⊔ H` read sortwise and the filling required to match hole sorts. Nothing new is proved; the profile bookkeeping is the whole content.

```mermaid
flowchart LR
    HOLES["typed holes □_i:s_i"] --> CTX["context C: (s_1…s_n)⇒s"]
    CTX -->|"sort-correct filling"| FILLED["C[t⃗]: s"]
    TERMS["t_i : s_i"] --> FILLED
    CTX --> CAT["sorted context multicategory<br/>(colours = sorts, multi-arrows = typed contexts)"]
```

**Hands up.** Typed holes, context profiles, sort-correct filling, and the context category by sorts. The next room organizes these typed term-operations into a clone.

---

## I.14 · Syntax clone and superposition

*Terms in finitely many marked variables are operations. Collecting them by arity (single-sorted) or profile (many-sorted) gives the syntactic clone, where composition is substitution. Presentation transfer becomes a clone isomorphism.*

**`\operatorname{SynClo}(\Sigma)_{w,s}`** · Fixed-profile term set — terms in distinguished variables, by profile.

$$
\operatorname{SynClo}(\Sigma)_{w,s}=\mathbf T_\Sigma(x_1{:}s_1,\ldots,x_n{:}s_n)_s.
$$

**needs** terms on finite profiled generators · **yields** the graded carrier of formal operations · **links** single-sorted case indexes by arity `n`.

**`\pi_i`** · Projection — a distinguished variable as an operation.

$$
\pi_i:=x_i\in\operatorname{SynClo}(\Sigma)_{(s_1,\ldots,s_n),s_i}.
$$

**needs** the variable generators · **yields** the clone's projection operations · **links** projections are the identities for superposition in each coordinate.

**`\circ`** · Superposition — simultaneous substitution of terms into a term.

$$
t\circ(u_1,\ldots,u_n):=\widehat\sigma(t),\qquad \sigma(x_i)=u_i.
$$

**needs** a term and an argument tuple of terms · **yields** the clone composition · **links** superposition *is* substitution.

> **`clone`** ⚙ **ENGINE** · Syntax clone
>
> The fixed-profile term sets, with projections and superposition, form a clone whose laws are precisely the substitution laws; presentation transfer is a clone isomorphism.
>
> $$
> \text{associativity, projection laws}\ \Longleftrightarrow\ \text{Kleisli laws of substitution.}
> $$
>
> **drives** terms ⟶ operations organized by profile.
> **powered by** substitution (composition) and the projections (variables).
> **enables** interpretation as a clone homomorphism into any algebra (I.16), and the operation-level kernel (I.17).

```mermaid
flowchart LR
    TERMS["profiled terms x_i:s_i"] --> SYN["SynClo(Σ)_{w,s}"]
    PROJ["projections π_i"] --> SYN
    SYN -->|"⚙ clone (superposition=subst)"| LAWS["clone laws"]
    SYN -. "transfer = clone iso" .-> PRES["presentation clones"]
    SYN --> INTERP["interpretation → Clo(A) (I.16)"]
```

**Hands up.** The syntactic clone, superposition, and the clone laws. The next room compares three closely related syntax-side gadgets — terms, templates, contexts — before semantics begins.

---

## I.15 · Templates and context operations

*A short reconciliation room. Terms with argument variables, templates with parameters, and contexts with holes are three faces of the same syntax-valued machinery; the room fixes how each acts on syntax and how contexts close relations.*

**`t(x_1,\ldots,x_n)`** · Term with argument variables — a term viewed as awaiting argument terms.

$$
t\in\mathbf T_\Sigma(x_1,\ldots,x_n)_s.
$$

**needs** distinguished argument variables · **yields** a term operation by superposition · **links** the clone element of I.14.

**`P[p_1,\ldots,p_k]`** · Template with parameters — a term with marked parameter slots filled by substitution.

$$
P\in\mathbf T_\Sigma(X\sqcup\{p_1,\ldots,p_k\}),\quad\text{parameters held fixed across a family.}
$$

**needs** parameter generators · **yields** parametric families of terms · **links** parameters held fixed yield polynomial operations.

**`C[\square_1,\ldots,\square_n]`** · Context with holes — a template whose marked slots are holes.

$$
C\in\mathbf T_\Sigma(X\sqcup H).
$$

**needs** hole generators · **yields** plugging (I.11) · **links** holes vs argument variables differ only in role, not in mechanism.

**`\theta^{\mathrm{ctx}}`** · Context closure of a relation — close a relation under all one-hole contexts.

$$
a\,R\,b\ \Longrightarrow\ C[a]\,\theta^{\mathrm{ctx}}\,C[b]\quad(\forall\text{ one-hole }C).
$$

**needs** a relation `R`, the context monoid · **yields** the *compatible* closure of `R` (the smallest compatible relation containing `R`) · **links** **the congruence generated by `R` is obtained by additionally taking the equivalence closure**: $\operatorname{Cg}(R) = \mathrm{EqCl}(\theta^{\mathrm{ctx}}(R))$, equivalently the reflexive, symmetric, transitive closure of the context closure. Context closure alone is not yet a congruence; the calculus of contexts and the calculus of congruences agree only modulo equivalence closure.

> [!result] Hole-variable vs argument-variable
> Argument variables, parameters, and holes are all distinguished generators; what differs is the *role* — arguments are superposed (I.14), parameters are held fixed (polynomial operations), holes are plugged (I.11). One substitution mechanism underlies all three. Context closure of a relation gives its compatible closure; closing additionally under equivalence reproduces `Cg(R)` exactly.

```mermaid
flowchart LR
    TERM["term t(x⃗)"] -->|"superpose"| OPN["term operation"]
    TEMPL["template P[p⃗]"] -->|"hold params fixed"| POLY["polynomial operation"]
    CTX["context C[□⃗]"] -->|"plug"| FILL["filled term"]
    REL["relation R"] -->|"context closure"| COMP["compatible closure"]
    COMP -->|"equivalence closure"| CONG["Cg(R) (= I.4)"]
```

**Hands up.** The three syntax-side roles unified, and context closure identified with congruence generation. The next room finally points syntax at a semantic target.

---

## I.16 · Evaluation into target algebras

*The third reuse of the UMP — this time with a semantic target. An assignment of variables into an algebra extends uniquely to evaluation; its image is the generated subalgebra; build-then-evaluate equals evaluate-then-build. This is the algebraic prototype of term denotation in a structure.*

**`\mathbf B`** · Target algebra — the semantic codomain.

$$
\mathbf B=\big(B,(f^{\mathbf B})\big).
$$

**needs** `Σ` · **yields** the target evaluation maps into · **links** a first-order structure's algebraic reduct is this kind of object (II.8).

**`g:X\to B`** · Generator assignment into a target — a valuation of variables.

$$
g=(g_s:X_s\to B_s)_{s\in S}.
$$

**needs** `X`, `B` · **yields** the data evaluation extends · **links** in logic this is a variable assignment into a structure.

**`\operatorname{ev}_g`** · Term evaluation — the unique homomorphic extension of `g`.

$$
\operatorname{ev}_g=\widehat g:\mathbf T_\Sigma(X)\to\mathbf B,\qquad \widehat g\circ\eta=g.
$$

**needs** `g`, the UMP · **yields** the value of every term under the valuation · **links** sorted evaluation sends a term of sort `s` to an element of `B_s`.

**`\langle g[X]\rangle_{\mathbf B}`** · Generated semantic subalgebra — the image of evaluation.

$$
\operatorname{im}(\operatorname{ev}_g)=\langle g[X]\rangle_{\mathbf B}.
$$

**needs** `ev_g` · **yields** the reachable part of `B` · **links** image = generated subalgebra (I.3); the bridge to the kernel quotient (I.17).

> **`evaluate`** ⚙ **ENGINE** · Evaluation = homomorphic extension
>
> Evaluating terms under a valuation is the UMP extension into a semantic algebra; its image is precisely what the values generate.
>
> $$
> \operatorname{ev}_g=\widehat g,\qquad \operatorname{im}(\operatorname{ev}_g)=\langle g[X]\rangle_{\mathbf B}.
> $$
>
> **drives** valuation `g` ⟶ value of every term.
> **powered by** the UMP with a semantic target.
> **enables** the evaluation kernel and the first-iso comparison (I.17); in logic, term denotation (II.9).

> [!result] Build–evaluate
> Evaluation is a homomorphism, so it commutes with the operations: $\operatorname{ev}_g(f(\vec t))=f^{\mathbf B}(\operatorname{ev}_g(\vec t))$. Build-then-evaluate (form the term, then evaluate) equals evaluate-then-build (evaluate arguments, then apply the operation). This is the recursion clause of denotation.

```mermaid
flowchart LR
    G["valuation g: X→B"] -->|"⚙ evaluate (UMP)"| EV["ev_g: T_Σ(X)→B"]
    FREE["T_Σ(X)"] --> EV
    B["target algebra B"] --> EV
    EV --> IMG["im(ev_g) = ⟨g[X]⟩"]
    EV -. "instance" .-> DEN["term denotation ev_M,a (II.9)"]
```

**Hands up.** Evaluation, its image as a generated subalgebra, and the build–evaluate clause. The next room measures what evaluation collapses.

---

## I.17 · Semantic collapse and quotient comparison

*Evaluation forgets distinctions: different terms can have the same value. The evaluation kernel records exactly which, and the first isomorphism theorem identifies the image with syntax modulo that kernel. The room also separates one-valuation collapse from all-valuation identities.*

**`\kappa_g`** · Evaluation kernel — terms identified by one valuation.

$$
\kappa_g:=\ker(\operatorname{ev}_g),\qquad (t,u)\in\kappa_g\iff \operatorname{ev}_g(t)=\operatorname{ev}_g(u).
$$

**needs** `ev_g` · **yields** the measure of semantic collapse under that valuation · **links** a congruence on `T_Σ(X)`.

**`=_g`** · Semantic equality under one assignment — the relation `κ_g` decides.

$$
t=_g u\iff \operatorname{ev}_g(t)=\operatorname{ev}_g(u).
$$

**needs** a fixed valuation `g` · **yields** value-level identification · **links** distinct from syntactic equality; a single-valuation notion.

**`\operatorname{Id}(\mathbf B)`** · Operation-level collapse / identities — terms equal under *all* valuations.

$$
(t,u)\in\operatorname{Id}(\mathbf B)\iff \operatorname{ev}_g(t)=\operatorname{ev}_g(u)\ \text{for all }g.
$$

**needs** the clone interpretation (I.14) · **yields** the equational theory of `B` · **links** the kernel of the clone homomorphism `SynClo(Σ)→Clo(B)`; an all-assignments notion, not a one-assignment one.

> **`collapse`** ⚙ **ENGINE** · Kernel factorization for evaluation
>
> The generated semantic image is syntax modulo exactly the identifications the valuation forces.
>
> $$
> \mathbf T_\Sigma(X)/\kappa_g\ \cong\ \langle g[X]\rangle_{\mathbf B}.
> $$
>
> **drives** valuation ⟶ syntax-modulo-semantic-collapse.
> **powered by** kernels are congruences plus the first isomorphism theorem.
> **enables** term models, presented algebras, and every later quotient-of-syntax construction (Lindenbaum–Tarski, II.16; canonical models, II.15).

> [!warning] One kernel vs the other
> $\kappa_g$ identifies terms equal under *one* fixed valuation `g`. $\operatorname{Id}(\mathbf B)$ identifies terms equal under *all* valuations. The first is element-level collapse; the second is the equational theory. A typed equation $t=u$ between sort-`s` terms is the all-valuations statement within sort `s`.

```mermaid
flowchart LR
    EV["ev_g: T_Σ(X)→B"] -->|"ker"| KAP["κ_g (one valuation)"]
    KAP -->|"⚙ collapse"| ISO["T_Σ(X)/κ_g ≅ ⟨g[X]⟩"]
    CLONE["SynClo→Clo(B)"] -->|"ker"| ID["Id(B) (all valuations)"]
    ID -. "equational theory" .-> EQ["typed equations t =_s u"]
```

**Hands up.** The evaluation kernel, the collapse engine, and the one-valuation/all-valuations distinction. The next room makes the quotient side systematic: which constructions descend.

---

## I.18 · Quotient syntax and descent

*A quotient forgets distinctions; descent is the proof that an operation or map never needed the forgotten information. This room collects the descent obligations for every syntax operation and identifies the unconditional cases — exactly the ones the logic half will rely on.*

**`\mathbf T_\Sigma(X)/\theta`** · Quotient syntax — syntax modulo a congruence.

$$
\theta\in\operatorname{Con}(\mathbf T_\Sigma(X)),\qquad \mathbf T_\Sigma(X)/\theta.
$$

**needs** a syntactic congruence · **yields** equivalence-class syntax · **links** term models and Lindenbaum–Tarski are instances.

**`\operatorname{nat}_\theta`** · Quotient projection on syntax — the class map.

$$
\operatorname{nat}_\theta:\mathbf T_\Sigma(X)\to\mathbf T_\Sigma(X)/\theta.
$$

**needs** `θ` · **yields** the surjection descent factors through · **links** the natural transformation every descended map commutes with.

**`\widetilde F`** · Descended operation — an operation lifted to classes.

$$
\widetilde F([t_1],\ldots,[t_n]):=[F(t_1,\ldots,t_n)]\quad\text{(when well-defined).}
$$

**needs** an operation `F` and a congruence `θ` · **yields** quotient-level structure · **links** well-defined iff `F` respects `θ`.

> **`descend`** ⚙ **ENGINE** · Compatibility = well-definedness
>
> A representative-defined operation, map, substitution, or context operation descends to a quotient exactly when it respects the congruence.
>
> $$
> \operatorname{nat}_\theta\circ F=\widetilde F\circ(\operatorname{nat}_\theta)^{\times n}\ \Longleftrightarrow\ \big[t_i\,\theta\,u_i\,\forall i\Rightarrow F(\vec t)\,\theta\,F(\vec u)\big].
> $$
>
> **drives** raw construction ⟶ quotient-level construction.
> **powered by** representative-independence.
> **enables** quotient algebras (I.4), alpha-quotient operations (II.6), term models (II.15), Lindenbaum–Tarski (II.16).

> [!result] What descends, and what owes a proof
> - **Unconditional**: every basic term operation $f^{\mathbf T}$ and every polynomial / one-hole context operation $C[\,\cdot\,]$ preserves every congruence — so plugging a fixed context descends automatically.
> - **Conditional (substitution)**: an arbitrary substitution $\widehat\sigma$ is *not* automatic on a given congruence `θ`. The implication $s\,\theta\,t\Rightarrow \widehat\sigma(s)\,\theta\,\widehat\sigma(t)$ requires `θ` to be **substitution-stable**, i.e. *fully invariant* — closed under all substitutions. When that holds, substitution descends to the quotient and the quotient carries substitution — the seed of equational logic and schema instantiation.
> - **Conditional (general)**: arbitrary syntax-inspecting operations (those reading positions or representatives) owe a compatibility proof.

```mermaid
flowchart LR
    THETA["congruence θ"] --> QUOT["T_Σ(X)/θ"]
    SYN["T_Σ(X)"] -->|"nat_θ"| QUOT
    OP["operation F"] --> TEST["compatibility test"]
    THETA --> TEST
    TEST -->|"⚙ descend"| DESC["F̃ on classes"]
    DESC -. "unconditional for" .-> POLY["polynomial · context operations"]
    DESC -. "needs fully invariant θ for" .-> SUBST["arbitrary substitution"]
```

**Hands up.** Quotient syntax, the descent engine, and the unconditional/conditional split. The next room consolidates the entire left side into layers and ledgers.

---

## I.19 · Algebraic-syntax synthesis

*The left-side hands-up room. It names the five layers the movement built, records the map-type and equality ledgers local to algebraic syntax, and draws the single diagram the logic half will instantiate.*

**Free syntax layer** · `T_Σ(X)`, `η`, the UMP — construct and interpret. The invariant object; everything else is defined on it.

**Concrete presentation layer** · faithful presentations, `transfer`, the invariance criterion — choose a carrier, transport invariant constructions, quarantine addresses.

**Internal syntax-operation layer** · substitution `σ̂`, contexts `Ctx_H(X)`, plugging, the syntax clone — the UMP reused with syntactic targets; superposition = substitution; context closure = congruence generation.

**Semantic evaluation layer** · evaluation `ev_g`, image `⟨g[X]⟩`, build–evaluate — the UMP reused with semantic targets.

**Kernel / image / quotient / descent layer** · `κ_g`, first-iso `T_Σ(X)/κ_g ≅ ⟨g[X]⟩`, quotient syntax, the descent engine — collapse and quotient, with basic term operations and polynomial/context operations descending unconditionally; arbitrary substitutions descend only on a fully invariant (substitution-stable) congruence.

> [!result] Left-side map-type ledger
> generator insertion `η` · comparison/transfer `ρ, τ` · substitution `σ̂` · context operation / plugging · evaluation `ev_g` · homomorphism `h` · quotient projection `nat_θ` · descended map `F̃`.

> [!result] Left-side equality ledger
> raw syntax equality (unique readability) · presentation equality / transferred equality (`τ`-conjugate) · semantic equality under one valuation (`=_g`, kernel `κ_g`) · operation equality / identities (`Id(B)`, all valuations) · quotient equality (`θ`-classes).

```mermaid
flowchart LR
    FREE["free syntax T_Σ(X), η, UMP"] -->|"⚙ transfer"| PRES["presentations"]
    FREE -->|"⚙ subst / plug"| OPS["substitution · contexts · clone"]
    FREE -->|"⚙ evaluate"| SEM["ev_g, ⟨g[X]⟩"]
    SEM -->|"⚙ collapse"| KER["κ_g, first-iso"]
    OPS -->|"⚙ descend"| QUOT["quotient syntax"]
    KER --> QUOT
    FREE -. "instance Σ↦Σ_L" .-> LOGIC["Term_L and the logic half"]
```

**Hands up — left side complete.** The free algebra, the UMP, presentation transfer, substitution and contexts, evaluation, kernels, and descent. Every one of these is now invoked in Part II *only at the exact point where logic runs on it* — and nowhere else.

---

# PART II · First-Order Logic

*Now the atlas develops first-order logic as logic. The language is logical vocabulary; terms denote objects; atoms and formulas make assertions; binding, semantics, deduction, theories, and models are built from their own primitives. Universal algebra is invoked only where an already-built engine genuinely powers a logical construction — term formation, term denotation, term substitution, term models, formula quotients — and nowhere else. Every room here reads correctly even if Part I were deleted; the UA notes are exact transfers, not metaphors.*

---

## II.0 · Logic-side standing convention

*A short convention room. It fixes the discipline for the whole movement: logic motivates each object in its own terms, the term layer is separated from the formula layer, binding is treated as a new layer, and a universal-algebra transfer note appears only at an exact construction point.*

**logic-first** · Develop each object logically first. State the logical role, then the formal datum; insert a UA transfer note only where an exact engine applies.

**term ≠ formula layer** · The functional signature builds terms (a free algebra). Relations, equality, connectives, and quantifiers build formulas (an inductive closure). These are different layers.

**binding is new** · Quantifiers introduce variable binding, which is not present in term algebra. Free/bound occurrence, alpha-equivalence, and capture-avoidance are genuinely new data.

**single-sorted display, sorted where needed** · Display single-sorted formation when clearer; give the profiled/sorted wrapper where sort discipline matters. Many-sortedness is a profile wrapper, not a late appendix.

> [!warning] UA-insertion limit
> A logic room takes 0 or 1 universal-algebra transfer notes as normal; 2 only for terms, term substitution, and term models. More than that is overfitting logic to an algebraic shape. The whole functional content of a language lives in its functional reduct; relations, binding, and truth are not algebra.

**Hands up.** The standing discipline. The next room lays out the language datum.

---

## II.1 · First-order language data

*The nonlogical vocabulary, plus the variable supply and logical symbols. The single algebraically relevant move is the extraction of the functional reduct — the one place Part I attaches.*

**`L`** · First-order language — the nonlogical vocabulary.

$$
L=(S,\operatorname{Func}_{L},\operatorname{Rel}_{L}),\qquad \operatorname{Func}_L=(\operatorname{Func}_{L,w,s}),\qquad \operatorname{Rel}_L=(\operatorname{Rel}_{L,w}),
$$

all symbol sets pairwise disjoint; write $f:w\to s$ and $R:w$.

**needs** a sort set `S` · **yields** terms, atoms, formulas, structures · **links** constants are the $()\to s$ function symbols; there is **no formula sort**.

**`\operatorname{Var}`** · Variable supply — sorted, pairwise-disjoint, infinite families.

$$
\operatorname{Var}=(\operatorname{Var}_s)_{s\in S},\qquad \text{each }\operatorname{Var}_s\ \text{infinite.}
$$

**needs** `S` · **yields** the generators of terms · **links** infinitude powers freshness and renaming (II.5–II.6); disjointness recovers a variable's sort.

**`\operatorname{Func}_L`, `c`** · Function and constant symbols — *not yet* term constructors, but the symbols that *induce* them.

$$
f\in\operatorname{Func}_{L,w,s}\ (f:w\to s),\qquad c\in\operatorname{Func}_{L,(),s}.
$$

**needs** `L` · **yields** the data from which term-formation operations are built · **links** each symbol $f$ induces a constructor operation $f^{\mathbf T}$ on `Term_L` (preserving the Part I distinction between $f$ and $f^{\mathbf T}$, I.5–I.7); constants are nullary function symbols — no separate primitive.

**`\operatorname{Rel}_L`, `=`** · Relation symbols and equality — *not yet* atom builders, but the symbols that induce them.

$$
R\in\operatorname{Rel}_{L,w},\qquad =_s\ \text{a logical relation per sort.}
$$

**needs** `L`, `S` · **yields** the data from which atom-formation operations are built · **links** each $R$ induces an atom-formation operation taking a term tuple to an atom (II.3); relation symbols consume term tuples but build **no terms**; equality is logical, not a nonlogical symbol.

**`\neg,\to,\forall`** · Logical symbols — *not yet* formula constructors, but the symbols that induce them.

$$
\neg,\ \to,\ (\forall x)_{x\in\operatorname{Var}}.
$$

**needs** nothing from `L` · **yields** the data from which the formula-constructor signature is built (II.4) · **links** each logical symbol induces a formation operation on $\operatorname{Form}^{\mathrm{raw}}_L$; not members of `Func` or `Rel`; $\wedge,\vee,\leftrightarrow,\exists$ are defined abbreviations.

**`\Sigma_L`** · Functional reduct — the algebraic signature inside `L`.

$$
\Sigma_L:=\big(S,(\operatorname{Func}_{L,w,s})_{(w,s)}\big).
$$

**needs** the function-symbol part of `L` · **yields** the signature term formation runs on · **links** **this is `Σ` from Part I, instantiated**; relations and logical symbols are deliberately absent.

> [!result] Language decomposition
> `L` splits cleanly as `(Σ_L, Rel_L)` with no shared primitive. The functional reduct carries all algebraic content; the relational part feeds only the atomic layer. This split is the entire interface between Part I and Part II.

```mermaid
flowchart LR
    L["L = (S, Func, Rel)"] -->|"split"| SIGL["Σ_L (functional reduct)"]
    L -->|"split"| RELL["Rel_L"]
    S["S"] --> VAR["Var"]
    SIGL -. "instance of Σ (Part I)" .-> P1["T_Σ(X)"]
    SIGL --> TERM["Term_L (II.2)"]
    VAR --> TERM
    RELL --> ATOM["Atom_L (II.3)"]
```

**Hands up.** The language datum, the variable supply, the logical symbols, and the functional reduct `Σ_L`. The next room builds terms — the one logic-side object that *is* universal algebra.

---

## II.2 · Terms

*Terms are the object-denoting expressions of the language. Logically, they are generated from variables and constants by function application. This is the exact point where the free-algebra engine attaches: the term family is the free `Σ_L`-algebra on the variables.*

**`\operatorname{Term}_L`** · Term family — object-denoting expressions.

$$
x\in\operatorname{Var}_s\Rightarrow x\in\operatorname{Term}_{L,s},\qquad c:()\to s\Rightarrow c\in\operatorname{Term}_{L,s},
$$

$$
f:w\to s,\ t_i\in\operatorname{Term}_{L,s_i}\Rightarrow f(t_1,\ldots,t_n)\in\operatorname{Term}_{L,s}.
$$

**needs** `L`, `Var` · **yields** term induction, recursion, substitution, denotation · **links** terms feed atomic formulas (II.3).

**`x`, `c`, `f(\vec t)`** · Term constructors — the three formation cases.

$$
\text{variable } x,\qquad \text{constant } c,\qquad \text{application } f(\vec t).
$$

**needs** term formation · **yields** the case analysis for every recursion on terms · **links** unique readability separates the three and recovers the outer symbol.

**`\operatorname{Var}(t)`** · Variables occurring in a term — the finite sorted support.

$$
\operatorname{Var}(x)=\{x\},\quad \operatorname{Var}(c)=\varnothing,\quad \operatorname{Var}(f(\vec t))=\textstyle\bigcup_i\operatorname{Var}(t_i).
$$

**needs** term recursion · **yields** support, freshness, locality of denotation · **links** assignment dependence (II.9).

**`t[\sigma]`** · Term substitution — replacement of variables by terms.

$$
\sigma:\operatorname{Var}\to\operatorname{Term}_L,\qquad t[\sigma]=\widehat\sigma(t).
$$

**needs** a term assignment `σ` · **yields** substituted terms · **links** the homomorphic-extension engine (I.10), here with `X=Y=Var`.

> **`term-construct`** ⚙ **ENGINE** · Terms as the free algebra
>
> The logical formation of terms *is* the free-algebra construction on the variables for the functional reduct.
>
> $$
> \mathbf{Term}_L\ \cong\ \mathbf T_{\Sigma_L}(\operatorname{Var}).
> $$
>
> **drives** logical vocabulary ⟶ object-denoting syntax.
> **powered by** the construct engine (I.5–I.6) at `Σ = Σ_L`, `X = Var`. No new mechanism — the term layer is universal algebra.
> **enables** term induction, recursion, substitution, and denotation, all inherited verbatim from Part I.
> **boundary** relation symbols are not term constructors; they enter only at the atomic layer.

> [!result] Inherited term facts
> Term induction and recursion are the generatedness and UMP faces of the free object. Unique readability holds. Finite support holds. Term substitution is the homomorphic extension; its identity, composition, and substitution-lemma laws are exactly those of I.10. These are *imported*, not re-proved.

```mermaid
flowchart LR
    SIGL["Σ_L"] -->|"⚙ term-construct (= Part I construct)"| TERM["Term_L ≅ T_{Σ_L}(Var)"]
    VAR["Var"] --> TERM
    TERM --> OUT["induction · recursion · substitution"]
    TERM --> SUPP["Var(t): finite support"]
    TERM --> ATOM["atomic formulas (II.3)"]
    TERM -. "instance" .-> FREE["T_Σ(X) (Part I)"]
```

**Hands up.** `Term_L` as the exact free-algebra instance, with term induction, recursion, substitution, and support imported from Part I. The next room changes layers: terms become inputs to relations and equality, producing atomic formulas.

---

## II.3 · Atomic formulas

*The first formula-producing layer. Terms denote; atoms assert. Equality compares two same-sort terms; a relation symbol predicates of a sort-matched term tuple. This is the term→formula boundary — a layer change, not an extension of `Σ_L`.*

**`t=_s u`** · Equality atom — a same-sort term pair as an assertion.

$$
t,u\in\operatorname{Term}_{L,s}\ \Longrightarrow\ (t=_s u)\in\operatorname{Atom}_L.
$$

**needs** two terms of a common sort · **yields** the equality atoms · **links** equality is logical and sort-indexed; mixed-sort equality is not formed.

**`R(\vec t)`** · Relation atom — a relation symbol on a profile-matching tuple.

$$
R\in\operatorname{Rel}_{L,w},\ \vec t\in\operatorname{Term}_{L,w}\ \Longrightarrow\ R(\vec t)\in\operatorname{Atom}_L.
$$

**needs** a relation symbol, a sort-correct term tuple · **yields** the relation atoms · **links** relations consume terms but never become term operations.

**`\operatorname{Atom}_L`** · Atomic formula set — equality atoms and relation atoms together.

$$
\operatorname{Atom}_L=\{t=_s u\}\ \sqcup\ \{R(\vec t)\}.
$$

**needs** `Term_L`, equality, `Rel_L` · **yields** the base cases of formula formation · **links** the seam between term denotation and truth.

> [!warning] The term→formula layer change
> An atom is *not* a term and *not* an element of any sort. Passing from `Term_L` to `Atom_L` leaves the free `Σ_L`-algebra entirely: relations and equality are not operations of the term signature. "Syntax is a free algebra" stops being literally true here and is recovered for formulas only by the separate constructor layer of II.4.

```mermaid
flowchart LR
    TERM["Term_L"] --> EQ["equality atoms t =_s u"]
    TERM --> RT["relation atoms R(t⃗)"]
    REL["Rel_L"] --> RT
    EQ --> ATOM["Atom_L"]
    RT --> ATOM
    ATOM --> RAW["raw formulas (II.4)"]
```

**Hands up.** The atomic layer — equality and relation atoms over terms. The next room closes atoms under connectives and quantifiers into raw formulas.

---

## II.4 · Raw formulas

*Formulas are generated from atoms by negation, implication, and quantification. This is an inductive closure with its own constructor signature — a free algebra for that signature, but emphatically not the term algebra. Formula recursion runs on these constructors, not on the UMP of `Term_L`.*

**`\operatorname{Form}^{\mathrm{raw}}_L`** · Raw formula set — the least closure of atoms under the constructors.

$$
\operatorname{Atom}_L\subseteq\operatorname{Form}^{\mathrm{raw}}_L,\quad \varphi,\psi\in\operatorname{Form}^{\mathrm{raw}}_L\Rightarrow \neg\varphi,\ (\varphi\to\psi),\ \forall x\,\varphi\in\operatorname{Form}^{\mathrm{raw}}_L.
$$

**needs** `Atom_L`, the constructors `¬`, `→`, `∀x` · **yields** formula induction and recursion · **links** generated independently of semantics.

**`\neg,\to,\forall_x`** · Logical constructors — the formula builders.

$$
\neg:\mathrm{Form}\to\mathrm{Form},\quad \to:\mathrm{Form}^2\to\mathrm{Form},\quad \forall_x:\mathrm{Form}\to\mathrm{Form}\ (x\in\operatorname{Var}).
$$

**needs** the formula set · **yields** the constructor signature of formulas · **links** a *separate* signature from `Σ_L`; quantifier constructors are indexed by a variable.

**formula tree** · Constructor view — a formula as a tree over its own constructors.

$$
\text{nodes: atoms (leaves), }\neg,\to,\forall_x\ \text{(internal).}
$$

**needs** raw formula formation · **yields** unique readability for formulas · **links** the basis of formula recursion.

> **`form-close`** ⚙ **ENGINE** · Formula formation (least closure)
>
> Raw formulas are the least set containing the atoms and closed under the logical constructors; recursion on formulas is defined by one clause per constructor.
>
> $$
> \operatorname{Form}^{\mathrm{raw}}_L=\mu Z.\ \big(\operatorname{Atom}_L\cup \neg Z\cup (Z\to Z)\cup\textstyle\bigcup_x\forall_x Z\big).
> $$
>
> **drives** atoms ⟶ all formulas.
> **powered by** least closure under the constructor signature, with its own unique readability.
> **enables** free-variable analysis (II.5), substitution clauses (II.7), and truth clauses (II.10).
> **boundary** this is **not** the UMP of `Term_L`; it is recursion for a separate constructor algebra.

> [!result] Formula layer facts
> Formula induction follows from least closure; formula recursion follows from constructor unique readability; finite support holds. Defined connectives $\wedge,\vee,\leftrightarrow,\exists$ add notation, not primitive formation power, unless explicitly promoted to constructors. Raw formulas may be viewed as a free algebra for the *formula* constructor signature — an additional construction, not part of `T_{Σ_L}(Var)`.

```mermaid
flowchart LR
    ATOM["Atom_L"] -->|"⚙ form-close"| RAW["Form^raw_L"]
    NEG["¬"] --> RAW
    IMP["→"] --> RAW
    ALL["∀x"] --> RAW
    RAW --> REC["formula induction · recursion"]
    RAW -. "free for formula signature, ≠ Term_L" .-> SEP["separate constructor algebra"]
    RAW --> BIND["binding analysis (II.5)"]
```

**Hands up.** Raw formulas, their constructor signature, and formula recursion — kept distinct from the term algebra. The next room analyses the variable occurrences the quantifiers create.

---

## II.5 · Variables, occurrence, and binding

*Quantifiers introduce binding — genuinely new data absent from terms. The room distinguishes free from bound occurrences, computes free-variable sets by formula recursion, defines sentences, and sets up freshness, the resource that makes renaming possible.*

**occurrence** · Variable occurrence — a position of a variable in a formula tree.

$$
\text{an occurrence of }x\ \text{at a leaf of the formula tree.}
$$

**needs** the formula tree (II.4) · **yields** the substrate for free/bound classification · **links** occurrences are tree-relative; the classification is invariant.

**free / bound** · Free vs bound occurrence — relative to enclosing quantifiers.

$$
x\ \text{bound at an occurrence}\iff\text{it lies under some }\forall x;\quad\text{else free.}
$$

**needs** binding scope · **yields** the free/bound split · **links** the same variable can occur both free and bound in one formula.

**`\operatorname{FV}(\varphi)`** · Free-variable set — variables with a free occurrence.

$$
\operatorname{FV}(R(\vec t))=\textstyle\bigcup\operatorname{Var}(t_i),\quad \operatorname{FV}(\neg\varphi)=\operatorname{FV}(\varphi),\quad \operatorname{FV}(\varphi\to\psi)=\operatorname{FV}(\varphi)\cup\operatorname{FV}(\psi),
$$

$$
\operatorname{FV}(\forall x\,\varphi)=\operatorname{FV}(\varphi)\setminus\{x\}.
$$

**needs** formula recursion · **yields** the variables whose values can affect the formula · **links** feeds substitution guards (II.7) and semantic locality (II.10).

**`\operatorname{Sent}_L`** · Sentences — closed formulas.

$$
\sigma\in\operatorname{Sent}_L\iff \operatorname{FV}(\sigma)=\varnothing.
$$

**needs** `FV` · **yields** formulas whose truth needs no assignment · **links** theories are sets of sentences (II.14).

**`\operatorname{fresh}`** · Fresh variable — a same-sort variable outside a finite support.

$$
y\in\operatorname{Var}_s\setminus F\quad(F\ \text{finite}).
$$

**needs** infinite `Var_s`, a finite support · **yields** a name safe for renaming · **links** the resource behind alpha-equivalence and capture-avoidance.

> [!result] Binding facts
> Free-variable sets are finite and computed by formula recursion; quantification removes exactly the bound variable from one sort component. Because each `Var_s` is infinite and every formula has finite support, a fresh same-sort variable always exists. Binding scope and renaming boundaries are determined by the quantifier nodes of the formula tree.

```mermaid
flowchart LR
    RAW["Form^raw_L"] --> OCC["occurrences"]
    OCC --> FB["free / bound (under ∀x)"]
    FB --> FV["FV(φ)"]
    FV --> SENT["Sent_L (FV = ∅)"]
    INF["infinite Var_s"] --> FRESH["fresh variable"]
    FV --> FRESH
    FRESH --> ALPHA["alpha-equivalence (II.6)"]
```

**Hands up.** Free/bound occurrence, free-variable sets, sentences, and freshness. The next room forgets bound-variable names by quotienting under alpha-equivalence.

---

## II.6 · Alpha-equivalence

*Bound-variable names are inessential. Alpha-equivalence is the least constructor-compatible equivalence generated by capture-free renaming of bound variables; the quotient is binding-aware formulas. This is the descent engine of Part I applied to a logical congruence.*

**bound renaming** · Fresh renaming step — rename a bound variable to a fresh one.

$$
\forall x\,\varphi\ \rightsquigarrow\ \forall y\,(\varphi[x\!\mapsto\! y]),\qquad y\ \text{fresh, capture-free.}
$$

**needs** `fresh` (II.5), capture-free substitution of a variable · **yields** the generating steps of `≡_α` · **links** legitimate only when `y` is fresh for `φ`.

**`\equiv_\alpha`** · Alpha-equivalence — equality up to consistent capture-free bound renaming.

$$
\equiv_\alpha\ :=\ \text{least constructor-compatible equivalence containing the renaming steps.}
$$

**needs** renaming steps, closure under the formula constructors · **yields** name-insensitive formula identity · **links** preserves free variables and (later) satisfaction.

**`\operatorname{Form}_L`** · Binding-aware formulas — raw formulas modulo `≡_α`.

$$
\operatorname{Form}_L:=\operatorname{Form}^{\mathrm{raw}}_L/\!\equiv_\alpha.
$$

**needs** `Form^raw_L`, `≡_α` · **yields** the formulas all later constructions descend to · **links** capture-avoiding substitution and satisfaction live here.

**alpha-compatible operation** · An operation descending to alpha-classes.

$$
\varphi\equiv_\alpha\varphi'\Rightarrow F(\varphi)\equiv_\alpha F(\varphi').
$$

**needs** a raw-formula operation · **yields** a quotient-level operation · **links** every operation used on `Form_L` owes this descent proof.

> **`alpha-quotient`** ⚙ **ENGINE** · Alpha quotient (descent of binding)
>
> Forgetting bound-variable names is the quotient by alpha-equivalence; an operation acts on `Form_L` exactly when it is alpha-compatible.
>
> $$
> \operatorname{Form}^{\mathrm{raw}}_L\ \xrightarrow{\ /\equiv_\alpha\ }\ \operatorname{Form}_L,\qquad \text{operation descends}\iff\text{alpha-compatible.}
> $$
>
> **drives** raw formulas ⟶ binder-insensitive formulas.
> **powered by** the descent engine (I.18): compatibility is well-definedness, here for the congruence `≡_α`.
> **enables** total capture-avoiding substitution (II.7) and alpha-invariant satisfaction (II.10).

> [!result] Alpha facts
> Alpha-equivalence preserves free-variable sets. Every finite obstruction admits a fresh same-sort variable, so any two bound names can be reconciled. Connectives and quantifiers are alpha-compatible, so they descend; but each new operation on classes still owes its own compatibility proof.

```mermaid
flowchart LR
    RAW["Form^raw_L"] --> REN["capture-free bound renaming"]
    REN --> ALPHA["≡_α (constructor-compatible)"]
    RAW -->|"⚙ alpha-quotient (descent)"| FORM["Form_L"]
    ALPHA --> FORM
    FORM --> OPS["alpha-compatible operations only"]
    ALPHA -. "preserves" .-> FV["FV(φ)"]
```

**Hands up.** Alpha-equivalence and binding-aware formulas, with the descent obligation made explicit. The next room defines substitution through binders without capture.

---

## II.7 · Term substitution inside formulas

*Substituting terms for free variables inside a formula is delicate: a quantifier can capture a variable the substitution introduces. The room records the capture obstruction, the raw admissibility guard, and the resolution — total capture-avoiding substitution on alpha-classes.*

**`\sigma`** · Term substitution datum — sort-preserving terms for variables.

$$
\sigma:\operatorname{Var}\to\operatorname{Term}_L.
$$

**needs** `Var`, `Term_L` · **yields** the data formula substitution uses at atomic leaves · **links** extends homomorphically on terms (II.2); formulas apply that extension only at atoms.

**substitution at leaves** · Atomic action — apply `σ̂` inside atoms.

$$
(R(\vec t))[\sigma]=R(\widehat\sigma(\vec t)),\qquad (t=u)[\sigma]=(\widehat\sigma t=\widehat\sigma u).
$$

**needs** term substitution (II.2) · **yields** substitution on atoms · **links** the only place terms are touched; connectives recurse.

**`\operatorname{Cap}_{x,\sigma}(\varphi)`** · Capture obstruction — a binder would capture a substituted variable.

$$
\operatorname{Cap}\iff \exists y\in\operatorname{FV}(\varphi),\ x\in\operatorname{FV}(\sigma(y))\ \text{under }\forall x.
$$

**needs** `FV`, the supports of the `σ(y)` · **yields** the danger condition · **links** negating it is part of the raw guard.

**`\operatorname{SubstOK}`** · Raw admissibility guard — the safe domain of raw substitution.

$$
\varphi[\sigma]\ \text{defined on raw formulas only where no capture occurs.}
$$

**needs** `Cap`, binder-erased substitutions · **yields** a *partial* operation on raw formulas · **links** makes the failure of naive textual replacement explicit.

> **`avoid-capture`** ⚙ **ENGINE** · Capture-avoiding substitution
>
> On alpha-classes, substitution is total: rename bound variables to fresh names before descending under a binder, then substitute.
>
> $$
> (\forall x\,\varphi)[\sigma]:=\forall x'\,\big(\varphi[x\!\mapsto\! x'][\sigma]\big),\qquad x'\ \text{fresh for }\varphi,\sigma.
> $$
>
> **drives** guarded raw substitution ⟶ total substitution on `Form_L`.
> **powered by** finite support + infinite same-sort supplies + alpha-renaming + descent.
> **enables** schema instantiation, the substitution lemma, and the quantifier rules of deduction (II.12) — without accidental rebinding.

> [!result] Substitution-lemma boundary
> Capture-avoiding substitution exists on alpha-classes and is independent of representatives and fresh-name choices. The *semantic* substitution lemma is proved later (II.10): truth of `φ[σ]` under an assignment equals truth of `φ` under the pulled-back assignment. Raw substitution remains legitimately partial when no renaming convention has been fixed.

```mermaid
flowchart LR
    SIG["σ: Var→Term_L"] --> LEAF["substitute at atomic leaves"]
    RAW["Form^raw_L"] --> GUARD["Cap + SubstOK (partial)"]
    SIG --> GUARD
    FRESH["fresh + ≡_α"] -->|"⚙ avoid-capture"| TOTAL["total subst on Form_L"]
    GUARD --> TOTAL
    TOTAL --> LEMMA["substitution lemma (II.10)"]
```

**Hands up.** Capture-avoiding term substitution inside formulas, total on `Form_L`. The next room introduces the semantic side: structures and assignments.

---

## II.8 · Structures and assignments

*Semantics begins. A structure interprets the nonlogical vocabulary in carriers; an assignment interprets variables. The single algebraic observation is that the function-symbol part of a structure is a `Σ_L`-algebra — the target term denotation will use.*

**`\mathcal M`** · Structure — a sort-correct interpretation of `L`.

$$
\mathcal M=\big((M_s)_{s\in S},\,(f^{\mathcal M}),\,(R^{\mathcal M})\big),\quad f^{\mathcal M}:M_w\to M_s,\ R^{\mathcal M}\subseteq M_w,
$$

each `M_s` nonempty.

**needs** `L` · **yields** the semantic universe · **links** functions belong to the algebraic reduct; relations are extra structure.

**`\mathcal M_{\mathrm{alg}}`** · Algebraic reduct — forget the relations.

$$
\mathcal M_{\mathrm{alg}}=\big((M_s)_{s\in S},(f^{\mathcal M})_f\big).
$$

**needs** `\mathcal M` · **yields** the target of term denotation · **links** **this is a `Σ_L`-algebra** — the one place evaluation attaches; it is not the whole structure.

**`f^{\mathcal M}`, `c^{\mathcal M}`, `R^{\mathcal M}`** · Symbol interpretations.

$$
f^{\mathcal M}:M_w\to M_s,\qquad c^{\mathcal M}\in M_s,\qquad R^{\mathcal M}\subseteq M_w.
$$

**needs** `\mathcal M` · **yields** the data atoms are checked against · **links** equality is interpreted as genuine identity on `M_s`, not as a relation symbol.

**`a`** · Assignment — a sorted interpretation of variables.

$$
a=(a_s:\operatorname{Var}_s\to M_s)_{s\in S}.
$$

**needs** `Var`, the carriers of `\mathcal M` · **yields** values for free variables · **links** an assignment *is* a generator assignment into `\mathcal M_{alg}`.

**`a[x\mapsto m]`** · Assignment update — vary at one variable within its sort.

$$
a[x\!\mapsto\! m](y)=\begin{cases}m & y=x\\ a(y)&\text{else,}\end{cases}\quad x\in\operatorname{Var}_s,\ m\in M_s.
$$

**needs** `a`, `x`, `m` · **yields** the quantifier clause's variation · **links** supplies satisfaction of `∀` (II.10).

> [!warning] Equality atom vs meta-equality
> `=_s` in the object language is interpreted by *actual identity* on `M_s`; it is not a relation symbol and is not the meta-level "=" used to state the semantics. Keeping the two apart is essential when relations are quotiented (II.15).

```mermaid
flowchart LR
    L["L"] --> M["structure M"]
    M --> RED["M_alg (Σ_L-algebra)"]
    M --> REL["R^M ⊆ M_w"]
    VAR["Var"] --> A["assignment a"]
    M --> A
    A --> UPD["a[x↦m] (quantifier variation)"]
    RED -. "target of evaluation" .-> EV["term denotation (II.9)"]
```

**Hands up.** Structures, their algebraic reducts, assignments, and updates. The next room evaluates terms in a structure — the evaluation engine of Part I, refired.

---

## II.9 · Term denotation

*A term denotes an element of the structure under an assignment. Logically this is "read off the value by recursion on the term"; algebraically it is the unique homomorphic extension of the assignment into the algebraic reduct — the evaluation engine at the logic target.*

**`\operatorname{ev}^{\mathcal M}_a`** · Term denotation — the value of a term under an assignment.

$$
\operatorname{ev}^{\mathcal M}_a:\mathbf{Term}_L\to\mathcal M_{\mathrm{alg}},\qquad \operatorname{ev}^{\mathcal M}_a=\widehat a.
$$

**needs** `Term_L`, `M_alg`, `a` · **yields** a value in `M_s` for each term of sort `s` · **links** the UMP extension of `a`.

**denotation clauses** · The three recursion cases.

$$
\operatorname{ev}_a(x)=a(x),\quad \operatorname{ev}_a(c)=c^{\mathcal M},\quad \operatorname{ev}_a(f(\vec t))=f^{\mathcal M}(\operatorname{ev}_a(\vec t)).
$$

**needs** term recursion · **yields** the compositional value · **links** the build–evaluate clause (I.16).

**locality** · Assignment dependence — denotation depends only on occurring variables.

$$
a\!\restriction_{\operatorname{Var}(t)}=a'\!\restriction_{\operatorname{Var}(t)}\ \Longrightarrow\ \operatorname{ev}_a(t)=\operatorname{ev}_{a'}(t).
$$

**needs** finite support (II.2) · **yields** the locality used by satisfaction · **links** only free data matters.

> **`evaluate`** ⚙ **ENGINE** · Term denotation = homomorphic extension *(refired)*
>
> Term denotation is the evaluation engine of Part I with target the algebraic reduct of the structure.
>
> $$
> \operatorname{ev}^{\mathcal M}_a=\widehat a:\mathbf T_{\Sigma_L}(\operatorname{Var})\to\mathcal M_{\mathrm{alg}}.
> $$
>
> **drives** assignment `a` ⟶ value of every term.
> **powered by** the UMP into `M_alg` — Part I's `evaluate` (I.16) at `B = M_alg`.
> **enables** the atomic truth clauses (II.10) and the term-substitution compatibility lemma.

> [!result] Substitution compatibility
> For a term substitution `σ` and the pulled-back assignment $a_\sigma(x)=\operatorname{ev}^{\mathcal M}_a(\sigma(x))$,
> $$
> \operatorname{ev}^{\mathcal M}_a(\widehat\sigma(t))=\operatorname{ev}^{\mathcal M}_{a_\sigma}(t).
> $$
> This is the four-corner identity $\operatorname{ev}_v\circ\widehat\sigma=\operatorname{ev}_{v\star\sigma}$ (I.10) read in the structure. It is the term half of the substitution lemma.

```mermaid
flowchart LR
    A["assignment a"] -->|"⚙ evaluate (UMP)"| EV["ev_M,a"]
    TERM["Term_L"] --> EV
    RED["M_alg"] --> EV
    EV --> LOCAL["locality on Var(t)"]
    EV --> COMPAT["ev_a(σ̂ t) = ev_{a_σ}(t)"]
    EV --> AT["atomic truth clauses (II.10)"]
```

**Hands up.** Term denotation as homomorphic extension, with locality and substitution compatibility. The next room defines truth of every formula.

---

## II.10 · Satisfaction

*Truth is defined by recursion on formula formation: atoms compare denotations and test relations, connectives recurse, quantifiers range over a carrier by assignment variation. Truth descends to alpha-classes. This is a genuinely logical recursion — the formula engine, not the term UMP.*

**`\mathcal M\models\varphi[a]`** · Satisfaction — truth of a formula under an assignment.

$$
\mathcal M\models (t=u)[a]\iff \operatorname{ev}_a(t)=\operatorname{ev}_a(u),\qquad \mathcal M\models R(\vec t)[a]\iff (\operatorname{ev}_a(\vec t))\in R^{\mathcal M},
$$

$$
\mathcal M\models\neg\varphi[a]\iff \mathcal M\not\models\varphi[a],\qquad \mathcal M\models(\varphi\to\psi)[a]\iff (\mathcal M\models\varphi[a]\Rightarrow\mathcal M\models\psi[a]),
$$

$$
\mathcal M\models\forall x\,\varphi[a]\iff \text{for all }m\in M_s,\ \mathcal M\models\varphi[a[x\!\mapsto\! m]].
$$

**needs** term denotation, relation interpretations, assignment update · **yields** the truth value of every formula · **links** equality atoms compare denotations; relation atoms test membership.

**locality of satisfaction** · Truth depends only on free variables.

$$
a\!\restriction_{\operatorname{FV}(\varphi)}=a'\!\restriction_{\operatorname{FV}(\varphi)}\ \Longrightarrow\ (\mathcal M\models\varphi[a]\iff\mathcal M\models\varphi[a']).
$$

**needs** `FV`, denotation locality · **yields** assignment-independence of sentences · **links** sentence truth needs no assignment.

> **`satisfy`** ⚙ **ENGINE** · Truth recursion
>
> Satisfaction extends atomic truth through the logical constructors by recursion on formula formation, with quantifiers ranging via assignment variation.
>
> $$
> \text{atoms (via ev)}\ \rightarrow\ \neg,\to\ (\text{recurse})\ \rightarrow\ \forall x\ (\text{vary }a\ \text{at }x).
> $$
>
> **drives** evaluated atoms ⟶ truth of every formula.
> **powered by** formula recursion (II.4) plus assignment update (II.8); *not* the UMP of `Term_L`.
> **enables** semantic consequence, model classes, and all of model theory.

> [!result] Substitution lemma and alpha-invariance
> The full substitution lemma is the binding-aware analogue of II.9:
> $$
> \mathcal M\models\varphi[\sigma][a]\iff \mathcal M\models\varphi[a_\sigma].
> $$
> Satisfaction depends only on free variables and is invariant under `≡_α`, so it descends to `Form_L`. Sentence truth is assignment-independent: write `\mathcal M\models\sigma`.

```mermaid
flowchart LR
    EV["term denotation"] --> AT["atom truth"]
    M["relations R^M"] --> AT
    AT -->|"⚙ satisfy (recursion)"| SAT["M ⊨ φ[a]"]
    UPD["a[x↦m]"] --> SAT
    SAT --> LOCAL["locality on FV(φ)"]
    SAT -. "alpha-invariant" .-> FORM["descends to Form_L"]
    SAT --> CONS["semantic consequence (II.11)"]
```

**Hands up.** Satisfaction, the substitution lemma, and alpha-invariance. The next room lifts truth to consequence between sentences.

---

## II.11 · Semantic consequence

*From truth in a structure to relations between sentences: a model satisfies a set; consequence is truth-preservation across all models; validity and satisfiability are the extremes. This is purely semantic — derivability is not yet in sight.*

**`\mathcal M\models\Gamma`** · Model of a set — a structure satisfying every member.

$$
\mathcal M\models\Gamma\iff \mathcal M\models\sigma\ \text{for all }\sigma\in\Gamma.
$$

**needs** satisfaction, `Γ ⊆ Sent_L` · **yields** the model relation · **links** the model class `Mod(Γ)` (II.14, II.17).

**`\Gamma\models\varphi`** · Semantic consequence — truth preserved in every model and assignment.

$$
\Gamma\models\varphi
\iff
\forall\,\mathcal M,\,a\ \Big[\big(\forall\gamma\in\Gamma\;\mathcal M\models\gamma[a]\big)\Rightarrow \mathcal M\models\varphi[a]\Big].
$$

**needs** satisfaction · **yields** the semantic consequence relation · **links** when $\Gamma\subseteq\operatorname{Sent}_L$ the assignment plays no role in $\Gamma$ and the definition collapses to $\forall\mathcal M\,(\mathcal M\models\Gamma\Rightarrow\forall a\,\mathcal M\models\varphi[a])$; compared with derivability only after a calculus is fixed (II.13).

**validity / satisfiability** · The extremes of consequence.

$$
\models\varphi\iff \varnothing\models\varphi;\qquad \Gamma\ \text{satisfiable}\iff \operatorname{Mod}(\Gamma)\neq\varnothing.
$$

**needs** consequence · **yields** logical truth and consistency-of-meaning · **links** satisfiability is the model-existence question completeness answers.

**`\operatorname{Th}(\mathcal M)`** · Theory of a structure — its true sentences.

$$
\operatorname{Th}(\mathcal M)=\{\sigma\in\operatorname{Sent}_L:\mathcal M\models\sigma\}.
$$

**needs** satisfaction · **yields** a complete, consistent set · **links** elementary equivalence: $\mathcal M\equiv\mathcal N\iff\operatorname{Th}(\mathcal M)=\operatorname{Th}(\mathcal N)$.

> [!result] Consequence facts
> Validity is consequence from no premises; satisfiability is a nonempty model class. `Th(M)` is complete and consistent. Elementary equivalence is sameness of complete theory and is implied by — but does not imply — isomorphism. Semantic consequence is defined with no reference to any proof system.

```mermaid
flowchart LR
    SAT["satisfaction"] --> MOD["M ⊨ Γ"]
    MOD --> CONS["Γ ⊨ φ"]
    CONS --> VAL["validity ⊨φ"]
    CONS --> SATis["satisfiability"]
    SAT --> TH["Th(M) (complete)"]
    TH -. "M ≡ N" .-> EE["elementary equivalence"]
```

**Hands up.** Semantic consequence, validity, satisfiability, and `Th(M)`. The next room introduces the syntactic counterpart — a deductive calculus.

---

## II.12 · Deductive calculi

*A proof system is additional data: syntax and semantics do not select axioms or rules. The room records the calculus datum, schemata, derivations, and derivability as the least closure under the rules, with structural induction on derivations as its proof principle.*

**`\mathsf C`** · Calculus datum — axioms and finitary rules over a judgement form.

$$
\mathsf C=(\text{axiom schemata},\ \text{inference rules},\ \text{side conditions}).
$$

**needs** `Form_L`, explicit side conditions · **yields** a proof system (Hilbert, natural deduction, sequents) · **links** quantifier and equality rules depend on substitution, freshness, and sort discipline.

**schema** · Schematic axiom/rule — parameters, admissible substitutions, side conditions, output.

$$
\text{a controlled family of instances, not one formula.}
$$

**needs** a parameter domain, an instantiation map · **yields** axiom and rule instances · **links** prevents a metalinguistic ellipsis from masquerading as a single object; instantiation uses capture-avoiding substitution (II.7).

**derivation** · Proof object — a finite tree/sequence from assumptions, axioms, rules.

$$
\text{a finite witness for a judgement } \Gamma\vdash\varphi.
$$

**needs** `\mathsf C`, premises `Γ` · **yields** a checkable certificate · **links** supports induction on the last rule.

**`\Gamma\vdash_{\mathsf C}\varphi`** · Derivability — the least consequence relation generated by `C`.

$$
\Gamma\vdash_{\mathsf C}\varphi\iff \exists\ \text{a finite derivation of }\varphi\ \text{from }\Gamma.
$$

**needs** `\mathsf C`, `Γ` · **yields** syntactic consequence · **links** distinct from `Γ ⊨ φ` until soundness/completeness connect them.

> **`rule-close`** ⚙ **ENGINE** · Closure under rules
>
> Derivability is the least set of judgements containing the axioms and closed under the rules; derivations are its witnesses.
>
> $$
> \vdash\ =\ \mu Z.\ (\text{axioms}\cup\{c\,:\,\text{premises of a rule}\in Z\}).
> $$
>
> **drives** assumptions + axioms + rules ⟶ `⊢`.
> **powered by** least finitary closure (I.3 closure, on judgements).
> **enables** proof search, metatheorems, structural induction on derivations, and substitution instances of rules.

> [!result] Calculus facts
> Derivability is calculus-relative and finitary: every derivation uses finitely many assumptions. Structural induction on derivations proves properties of `⊢` by the last rule applied. Substitution instances of rules are governed by the same capture-avoidance discipline as schema instantiation.

```mermaid
flowchart LR
    DATA["axioms + rules + side conditions"] -->|"⚙ rule-close"| DER["derivations"]
    SCHEMA["schemata"] --> DATA
    DER --> PROV["Γ ⊢ φ"]
    PROV --> IND["structural induction on derivations"]
    PROV -. "≠ (yet)" .-> SEM["Γ ⊨ φ (II.11)"]
```

**Hands up.** The calculus, derivations, and derivability. The next room connects `⊢` and `⊨` through soundness and completeness.

---

## II.13 · Soundness and completeness

*The two theorems that tie syntax to semantics. Soundness is a rule-by-rule check lifted by induction on derivations. Completeness is proved by building a model from a consistent theory — the Henkin construction, where free syntax, provable equality, descent, and satisfaction meet.*

**`\Gamma\vdash\varphi\Rightarrow\Gamma\models\varphi`** · Soundness — derivable implies semantically forced.

$$
\Gamma\vdash\varphi\ \Longrightarrow\ \Gamma\models\varphi.
$$

**needs** a calculus and semantics · **yields** semantic reliability of proofs · **links** established rule-by-rule, lifted by derivation induction.

**consistency** · Syntactic consistency — no contradiction is derivable.

$$
\Gamma\ \text{consistent}\iff \Gamma\nvdash\bot.
$$

**needs** `⊢` · **yields** the hypothesis of model existence · **links** completeness is proved contrapositively from consistency.

**maximal consistent set** · A consistent set deciding every sentence.

$$
\Gamma^*\ \text{consistent and}\ \forall\sigma\,(\sigma\in\Gamma^*\ \text{or}\ \neg\sigma\in\Gamma^*).
$$

**needs** a Lindenbaum extension · **yields** a complete syntactic theory · **links** the index from which the term model reads truth.

**Henkin witnesses** · Witness data — fresh constants and witnessing axioms.

$$
\exists x\,\varphi\ \rightsquigarrow\ \varphi[x\!\mapsto\! c_\varphi]\ \text{for a fresh constant }c_\varphi.
$$

**needs** a consistent theory, an expanded language · **yields** named witnesses for every existential · **links** supplies the elements of the canonical model. The Henkin extension `L'` must contain **at least one closed term in every sort** (the witnessing constants ensure this for every inhabited sort).

**term model** · Canonical syntactic model — *closed* terms of the Henkin language modulo provable equality.

$$
M_s=\operatorname{Term}_{L',s}^{\mathrm{closed}}/\!\equiv_T,\qquad t\equiv_T u\iff T\vdash t=_s u.
$$

**needs** Henkin data (closed term per sort), provable equality · **yields** a structure read off the syntax · **links** functions and relations are representative-defined; needs the descent conditions of Part I.

> **`henkin`** ⚙ **ENGINE** · Henkin model construction
>
> A consistent theory is extended to a Henkin-complete maximal consistent theory and its **closed-term model** is built; the truth lemma equates membership in the theory with satisfaction *for sentences*.
>
> $$
> T\ \text{consistent}\ \Rightarrow\ \exists\,\mathcal M\models T;\qquad \text{for every sentence }\sigma:\ \mathcal M\models\sigma\iff \sigma\in T^*.
> $$
>
> **drives** consistent theory ⟶ witnessed maximal extension ⟶ closed-term model ⟶ truth lemma on sentences.
> **powered by** fresh constants (one per existential, hence at least one closed term per sort), Lindenbaum extension, quotient/descent (I.18), and the first-iso collapse (I.17) on syntax.
> **enables** completeness and, via it, compactness.
>
> **variant** if instead the term model is built from *all* terms of `L'` (not only closed ones) modulo `≡_T`, the truth lemma must take the canonical assignment $a_{\mathrm{can}}(x):=[x]$; the closed-term presentation above and the all-term presentation are two distinct, equivalent constructions and must not be mixed.

> [!result] The two theorems
> **Completeness**: $\Gamma\models\varphi\Rightarrow\Gamma\vdash\varphi$, proved contrapositively by building a model of $\Gamma\cup\{\neg\varphi\}$ from its consistency. **Compactness**: $\Gamma$ is satisfiable iff every finite subset is — immediate from completeness and the finitary character of `⊢`. Soundness and completeness make `⊢` and `⊨` coincide, but their *constructions* remain distinct.

```mermaid
flowchart LR
    PROV["Γ ⊢ φ"] -->|"⚙ soundness induction"| SEM["Γ ⊨ φ"]
    CONS["consistent Γ"] --> HEN["Henkin witnesses + maximal extension"]
    HEN -->|"⚙ descend / collapse"| TM["term model M/≡_T"]
    TM --> TRUTH["truth lemma"]
    TRUTH --> COMP["Γ ⊨ φ ⇒ Γ ⊢ φ"]
    COMP --> CPT["compactness"]
```

**Hands up.** Soundness, the Henkin construction, completeness, and compactness. The next room organizes sentences into theories.

---

## II.14 · Theories

*A theory is a set of sentences, with two closures — semantic and deductive — that coincide for a sound and complete calculus. The room records completeness and consistency of theories, their extensions, and the morphisms between them.*

**`T`** · Theory — a set of sentences.

$$
T\subseteq\operatorname{Sent}_L.
$$

**needs** `Sent_L` · **yields** a model class and closures · **links** an axiomatized theory need not already be closed.

**`\operatorname{Cn}^{\models}(T)`, `\operatorname{Cn}^{\vdash}(T)`** · Semantic and deductive closure — kept notationally apart.

$$
\operatorname{Cn}^{\models}(T)=\{\sigma:T\models\sigma\},\qquad \operatorname{Cn}^{\vdash}(T)=\{\sigma:T\vdash\sigma\}.
$$

**needs** consequence / derivability · **yields** two *a priori distinct* closure operators · **links** soundness gives $\operatorname{Cn}^{\vdash}(T)\subseteq\operatorname{Cn}^{\models}(T)$; completeness gives the reverse inclusion; only after both is one entitled to write a single `Cn(T)`.

**complete `T` / consistent `T` / satisfiable `T`** · Three distinct properties, two coinciding under completeness.

$$
\text{complete}:\ \forall\sigma\,(T\vdash\sigma\ \text{or}\ T\vdash\neg\sigma);\qquad \text{consistent}:\ T\nvdash\bot;\qquad \text{satisfiable}:\ \operatorname{Mod}(T)\neq\varnothing.
$$

**needs** `T` · **yields** the classification of theories · **links** syntactic consistency and satisfiability are **equivalent by soundness and completeness**, not by definition; soundness gives satisfiable $\Rightarrow$ consistent, the Henkin construction gives the converse. `Th(M)` is satisfiable, complete, and consistent (II.11).

**extension / `T'\supseteq T`** · Adding axioms.

$$
T\subseteq T'\ \Rightarrow\ \operatorname{Mod}(T')\subseteq\operatorname{Mod}(T).
$$

**needs** two theories · **yields** the order on theories · **links** conservative extensions add no new theorems in the old language.

**theory morphism** · Reduct/expansion translation between theories.

$$
\text{a symbol translation taking theorems to theorems.}
$$

**needs** a language map · **yields** reducts and expansions of theories · **links** generated theories are deductive closures of axiom sets.

> [!result] Theory facts
> Semantic and deductive closure coincide for a sound and complete calculus. A theory is complete iff all its models are elementarily equivalent. Consistency equals having a model (by completeness). Extensions shrink the model class; conservative extensions preserve the old-language theory.

```mermaid
flowchart LR
    SENT["Sent_L"] --> T["theory T"]
    T --> CN["Cn(T) = deductive closure"]
    T --> MODC["Mod(T)"]
    T --> CLASS["complete / consistent"]
    T --> EXT["extensions T' ⊇ T"]
    T --> MOR["theory morphisms"]
```

**Hands up.** Theories, their closures, completeness/consistency, extensions, and morphisms. The next room builds canonical models out of terms — the descent engine again.

---
## II.15 · Term models and definable quotients

*The completeness room built a model out of syntax but left the construction implicit. This room makes it explicit: closed terms become the carrier, provable equality becomes the congruence, and the function and relation symbols descend onto equivalence classes. The result is the canonical term model — the descent engine applied to logic.*

**`\operatorname{ClTerm}_L`** · Closed terms — variable-free object expressions.

$$
\operatorname{ClTerm}_L=\{t\in\operatorname{Term}_L:\operatorname{Var}(t)=\varnothing\}.
$$

**needs** `Term_L` · **yields** the carrier of the canonical model · **links** the subalgebra of `Term_L` generated by constants alone; nonempty exactly when the language has a constant or witnesses are added.

**`\approx_T`** · Provable equality on terms — terms a theory forces equal.

$$
t\approx_T u\iff T\vdash t= u.
$$

**needs** a theory `T`; closed terms · **yields** the identification used to build the model · **links** an equivalence relation; congruence with respect to every function symbol by the equality axioms.

> [!result] Provable equality is a congruence
> Reflexivity, symmetry, transitivity, and the congruence rule for function symbols are exactly the equality axioms of the calculus. So `≈_T` is a congruence on the closed-term algebra for the functional reduct `Σ_L`.

**`\operatorname{TM}(T)`** · Term model carrier — closed terms modulo provable equality.

$$
\operatorname{TM}(T)=\operatorname{ClTerm}_L/{\approx_T},\qquad [t]=\{u:T\vdash t= u\}.
$$

**needs** `ClTerm_L`, `≈_T` · **yields** the underlying set of the canonical structure · **links** instance of the quotient-syntax construction `A/θ` from I.4 and I.18.

> **`descend`** ⚙ **ENGINE** · Symbol interpretation on classes
>
> Function and relation symbols descend from closed terms to provable-equality classes because `≈_T` is a congruence and provable relation membership respects it.
>
> $$
> f^{\operatorname{TM}(T)}([t_1],\ldots,[t_n])=[f(t_1,\ldots,t_n)],
> $$
>
> $$
> R^{\operatorname{TM}(T)}([t_1],\ldots,[t_n])\iff T\vdash R(t_1,\ldots,t_n).
> $$
>
> **drives** syntactic theory `\to` genuine structure.
>
> **powered by** independence of representatives — the descent test of I.18 applied to `≈_T`.
>
> **enables** the canonical model whose satisfaction of an atom is its provability, the engine inside completeness.
>
> **boundary** relation descent needs $T\vdash t= u \Rightarrow (T\vdash R(\ldots t\ldots)\leftrightarrow T\vdash R(\ldots u\ldots))$, which is again an equality axiom, not an extra hypothesis.

**`\operatorname{TM}(T)` as structure** · The canonical model.

$$
\operatorname{TM}(T)=\big(\operatorname{TM}(T),(f^{\operatorname{TM}(T)}),(R^{\operatorname{TM}(T)})\big).
$$

**needs** descended interpretations · **yields** a structure in which closed atomic truth is provability · **links** with Henkin witnesses added, satisfaction equals provability for all sentences (the truth lemma of II.13).

```mermaid
flowchart LR
    CLT["ClTerm_L"] --> EQ["≈_T = provable equality"]
    EQ -->|"⚙ descend"| TMC["TM(T) = ClTerm_L / ≈_T"]
    TMC --> FUN["f on classes"]
    TMC --> REL["R on classes = provability"]
    FUN --> CANON["canonical term model"]
    REL --> CANON
    TMC -. "instance of A/θ" .-> AQ["quotient syntax (I.18)"]
```

**Hands up.** Closed terms, provable equality as a congruence, the descended interpretations, and the canonical term model. The next room runs the same quotient construction one layer up — on formulas modulo provable equivalence — to recover the algebra of the logic itself.

---
## II.16 · Lindenbaum–Tarski quotients

*Terms modulo provable equality gave an algebra of objects. Formulas modulo provable equivalence give an algebra of propositions. Raw formulas are already a free algebra for the **formula** constructor signature (II.4); the Lindenbaum–Tarski construction quotients them by `≡_T`, descending connectives to Boolean operations and quantifiers to cylindric/polyadic operators. The resulting algebra `LT(T)` is a genuine algebra, but in general **not free** — it is a quotient of the free formula algebra by a fully invariant congruence, and only in degenerate cases (e.g. the propositional skeleton with no theory) does it remain free.*

**`\equiv_T`** · Provable equivalence — formulas a theory proves interderivable.

$$
\varphi\equiv_T\psi\iff T\vdash\varphi\leftrightarrow\psi.
$$

**needs** theory `T`; formulas · **yields** the identification used to algebraize formulas · **links** an equivalence relation; with $T=\varnothing$ over a propositional skeleton it is tautological equivalence `≡_taut`.

**`\operatorname{LT}(T)`** · Lindenbaum–Tarski algebra — formulas modulo provable equivalence.

$$
\operatorname{LT}(T)=\operatorname{Form}_L/{\equiv_T},\qquad [\varphi]=\{\psi:T\vdash\varphi\leftrightarrow\psi\}.
$$

**needs** `Form_L`, `≡_T` · **yields** a Boolean algebra carrying the logical operations · **links** the formula quotient analogue of the term quotient `TM(T)`; for propositional logic `LT(P)=\operatorname{Fm}(P)/\equiv_{\mathrm{taut}}` is the free Boolean algebra on `P`.

> **`lindenbaum-tarski`** ⚙ **ENGINE** · Descent of logical constructors
>
> Connectives and quantifiers respect provable equivalence, so they descend to operations on classes — turning the formula layer into an algebra.
>
> $$
> [\varphi]\wedge[\psi]:=[\varphi\wedge\psi],\quad
> [\varphi]\vee[\psi]:=[\varphi\vee\psi],\quad
> \neg[\varphi]:=[\neg\varphi],
> $$
>
> $$
> \exists x.[\varphi]:=[\exists x\,\varphi]\ \text{(a cylindric/quantifier operator, not a Boolean op).}
> $$
>
> **drives** logical equivalence `\to` algebra of propositions.
>
> **powered by** the descent engine: each constructor preserves `≡_T`, the well-definedness obligation of I.18.
>
> **enables** the Boolean structure of provability, Stone-type representation, and the algebraic reading of completeness — consistent theories are proper filters, complete consistent theories are ultrafilters.
>
> **boundary** quantifiers are not Boolean operations; they need variable data and yield a cylindric/polyadic enrichment, the precise place the term-level free-algebra story stops being enough.

**`[\varphi]` Boolean order** · The provability order on classes.

$$
[\varphi]\le[\psi]\iff T\vdash\varphi\to\psi.
$$

**needs** `LT(T)` · **yields** $\mathbf 0=[\bot]$, $\mathbf 1=[\top]$, complementation by $\neg$ · **links** `T` is consistent iff $\mathbf 0\neq\mathbf 1$. Completeness decides **sentences**, not arbitrary open formulas: the cleanest two-element collapse holds for the **sentence Lindenbaum algebra** $\operatorname{LT}^{\mathrm{sent}}(T)=\operatorname{Sent}_L/{\equiv_T}$, not for the full `LT(T)` on all formulas with free variables.

> [!result] Completeness, algebraically (on sentences)
> A consistent theory corresponds to a nontrivial Boolean quotient of `Sent_L`; a **complete** consistent theory collapses the **sentence** Lindenbaum algebra $\operatorname{LT}^{\mathrm{sent}}(T)$ to $\{\mathbf 0,\mathbf 1\}$, i.e. an ultrafilter on the propositional skeleton of sentences. This does **not** say `LT(T)` on all formulas is two-element — open formulas with free variables generically remain undecided by `T`. Maximal consistent extensions (II.13) are exactly ultrafilters of the sentence Lindenbaum algebra — the algebraic face of the Henkin construction.

```mermaid
flowchart LR
    FORM["Form_L"] --> EQT["≡_T = provable equivalence"]
    EQT -->|"⚙ lindenbaum-tarski"| LT["LT(T) = Form_L / ≡_T"]
    LT --> BOOL["Boolean ops ∧ ∨ ¬"]
    LT --> QUANT["quantifier operators ∃ ∀"]
    LT --> ORD["order [φ]≤[ψ] ⟺ T⊢φ→ψ"]
    ORD -. "ultrafilter = complete theory" .-> COMP["completeness (II.13)"]
```

**Hands up.** Provable equivalence, the Lindenbaum–Tarski algebra, the descent of connectives and quantifiers, and the algebraic reading of consistency/completeness. The final logic room opens up the model class itself: substructures, embeddings, elementary maps, types, and the two genuinely first-order theorems.

---
## II.17 · Model-theoretic layer

*The closing logic room turns from single structures to the category of models of a theory. Substructures and embeddings refine the homomorphisms of I.2; elementary maps refine them again by preserving all of first-order truth. Two results here are genuinely first-order — not universal-algebra consequences — and the room marks them as such.*

**`\mathbf N\subseteq\mathbf M`** · Substructure — a structure on a closed subdomain.

$$
N\subseteq M\ \text{closed under all }f^{\mathbf M},\ \text{with induced }f^{\mathbf N},R^{\mathbf N}=R^{\mathbf M}\!\restriction N.
$$

**needs** a structure `M`; a domain subset closed under functions and containing constants · **yields** the notion of generated substructure and embedding · **links** the closure condition is exactly the subalgebra condition `⟨X⟩` of I.3 on the algebraic reduct; relations are merely restricted.

**`\langle A\rangle_{\mathbf M}`** · Generated substructure — least substructure containing a set.

$$
\langle A\rangle_{\mathbf M}=\text{closure of }A\text{ under }f^{\mathbf M}\text{ and constants}.
$$

**needs** `M`, a subset `A` · **yields** finitely generated models · **links** carried entirely by the functional reduct — the relation symbols add no closure obligation.

**`h:\mathbf M\hookrightarrow\mathbf N`** · Embedding — injective, relation-reflecting morphism.

$$
h\ \text{injective},\quad R^{\mathbf M}(\vec a)\iff R^{\mathbf N}(h\vec a),\quad h(f^{\mathbf M}\vec a)=f^{\mathbf N}(h\vec a).
$$

**needs** two structures · **yields** isomorphic copies, chains, unions · **links** a hom of algebraic reducts that additionally reflects relations and equality.

**`h:\mathbf M\preceq\mathbf N`** · Elementary embedding — preserves all formulas.

$$
\mathbf M\models\varphi[\vec a]\iff\mathbf N\models\varphi[h\vec a]\quad\text{for every }\varphi.
$$

**needs** an embedding; agreement on all first-order formulas · **yields** elementary substructures `M ≺ N`, elementary chains · **links** strictly stronger than embedding; the relation that makes Löwenheim–Skolem meaningful.

**`\operatorname{Diag}(\mathbf M)`** · Diagram — the atomic (or elementary) theory of named elements.

$$
\operatorname{Diag}(\mathbf M)=\{\text{atomic and negated-atomic }\varphi(\vec c_a):\mathbf M\models\varphi\},\quad \operatorname{Diag}_{\mathrm{el}}(\mathbf M)\text{ uses all }\varphi.
$$

**needs** `M` expanded with a constant per element · **yields** the diagram lemma: models of `Diag(M)` are exactly structures embedding `M` · **links** the engine behind extension and amalgamation arguments.

**`p(\bar x)`** · Type — a *finitely satisfiable* set of formulas in fixed variables (a "partial" type); **complete type** when additionally maximal: for every $\varphi(\bar x)$, either $\varphi\in p$ or $\neg\varphi\in p$.

$$
p(\bar x)\subseteq\operatorname{Form}_L(\bar x),\quad T\cup p(\bar x)\ \text{finitely satisfiable}\quad(\text{maximal if complete}).
$$

**needs** a theory `T`; a variable tuple · **yields** realizing/omitting distinctions, type spaces (`S_n(T)` = space of complete `n`-types) · **links** realized when some model has an element tuple satisfying all of `p`; omitted otherwise. A general type need not decide every formula; only complete types correspond to points of the Stone space.

> **`compactness`** ⚙ **ENGINE** · Finite satisfiability suffices
>
> A set of sentences with a model for every finite subset has a model.
>
> $$
> \big(\forall\,\text{finite }T_0\subseteq T)\ \operatorname{Mod}(T_0)\neq\varnothing\ \Longrightarrow\ \operatorname{Mod}(T)\neq\varnothing.
> $$
>
> **drives** finite consistency `\to` global models.
>
> **powered by** completeness (derivations are finite) or directly by an ultraproduct.
>
> **enables** Löwenheim–Skolem, nonstandard models, type realization, elementary extensions.
>
> **boundary** this is a theorem of first-order logic, not a universal-algebra consequence; it fails for second-order logic and is the dividing line of the whole subject.

> [!warning] Where the algebra stops
> Compactness, Löwenheim–Skolem, and the existence of nonstandard models are first-order phenomena. They are not instances of UMP, descent, or first-isomorphism. The universal-algebra engine builds and quotients syntax; it does not deliver these model-existence theorems. The ultraproduct construction below is the genuinely model-theoretic engine that does.

**`\prod_{\mathcal U}\mathbf M_i`** · Ultraproduct — reduced product over an ultrafilter.

$$
\textstyle\prod_{\mathcal U}\mathbf M_i=\big(\prod_i M_i\big)/{\sim_{\mathcal U}},\qquad [\vec a]\!\sim_{\mathcal U}\![\vec b]\iff\{i:a_i=b_i\}\in\mathcal U.
$$

**needs** structures `(M_i)`; an ultrafilter `U` · **yields** Łoś's theorem: truth in the ultraproduct is truth on a `U`-large index set · **links** a quotient construction whose congruence is supplied by the ultrafilter; gives a one-line proof of compactness.

> [!result] Löwenheim–Skolem and Łoś
> Downward LS: a structure in a countable language has an elementary substructure of size at most $\aleph_0$ (or $|\,\text{formulas}\,|$). Upward LS: an infinite model has elementary extensions of every larger cardinality. Łoś's theorem: $\prod_{\mathcal U}\mathbf M_i\models\varphi[[\vec a]]$ iff $\{i:\mathbf M_i\models\varphi[\vec a]\}\in\mathcal U$. Together they fix what first-order theories can and cannot pin down.

```mermaid
flowchart LR
    M["structure M"] --> SUB["N ⊆ M (substructure)"]
    SUB --> EMB["embedding M ↪ N"]
    EMB --> ELEM["elementary M ≼ N"]
    ELEM --> DIAG["Diag(M) → embeddings"]
    ELEM --> TYPES["types p(x̄)"]
    TYPES -->|"⚙ compactness"| REAL["realized in some elementary extension"]
    TYPES -. "Omitting Types Theorem (separate)" .-> OMIT["can be omitted (under conditions)"]
    M -. "ultraproduct quotient" .-> ULTRA["∏_U M_i (Łoś)"]
    ULTRA -->|"⚙ compactness"| REAL
```

**Hands up.** Substructures and generated substructures (algebraic-reduct closure), embeddings and elementary embeddings, diagrams, types, and the two first-order engines — compactness and ultraproducts — with Löwenheim–Skolem. This closes Part II. Part III now reads back across both halves: the engines used, the kinds of maps and equalities encountered, and the precise points where universal algebra entered the logic.

---
# PART III · Cross-Spine Synthesis

*Parts I and II built objects. Part III reads back across them. It does not introduce new mathematics; it tabulates the recurring engines, the recurring kinds of maps, and — the central payload — the kinds of equality that the atlas keeps carefully apart. It then states exactly where universal algebra entered the logic half and nowhere else, and closes with the dependency maps of the whole development.*

---

## III.1 · Engine ledger

*Every engine that fired, what it consumed and produced, and the single fact that powers it. An engine is a move, not a definition: it appears in the atlas only where it does work, and each row below points back to the rooms where it did.*

| Engine | Consumes → produces | Powered by | Fired in |
|---|---|---|---|
| **generated closure** | base set + operations → least closed subalgebra | least-fixed-point of one-step closure | I.3, I.16; II.17 (substructures) |
| **UMP / homomorphic extension** | generator assignment → unique homomorphism | freeness of `T_Σ(X)` | I.5, I.16; II.2, II.9 |
| **unique readability** | raw constructors → free-syntax certificate | no-junk + no-confusion | I.6, I.7; II.2, II.4 |
| **presentation transfer** | one faithful presentation → another | unique generator-preserving iso | I.8, I.9 |
| **syntax-valued substitution** | syntax assignment → syntax endomorphism | UMP into a free algebra (term monad) | I.10, I.14; II.7 |
| **context plugging** | context + fillings → term | substitution on `X ⊔ H` | I.11, I.12, I.13, I.15 |
| **semantic evaluation** | structure + assignment + term → value | UMP into the algebraic reduct | I.16; II.9 |
| **first-isomorphism collapse** | homomorphism → quotient by kernel | kernel is a congruence | I.4, I.17; II.13, II.15 |
| **quotient descent** | compatible raw operation → operation on classes | independence of representatives | I.18; II.6, II.15, II.16 |
| **truth recursion / satisfy** | structure + assignment + formula → truth | recursion on formula formation | II.10 |
| **rule closure** | base data + inference rules → least closed set | induction on generation | II.4, II.12, II.14 |
| **Henkin / completeness** | consistent theory → model | maximal consistency + witnesses | II.13 |
| **Lindenbaum–Tarski** | formulas + provable equivalence → Boolean algebra | descent of connectives | II.16 |
| **compactness / ultraproduct** | finite satisfiability → model | first-order compactness / Łoś | II.17 |

> [!result] Engine reuse, not engine multiplication
> Four engines do most of the work and recur under different targets: UMP (one theorem, four uses — recursion, substitution, evaluation, transfer), first-isomorphism collapse, descent, and rule/closure. The Lindenbaum–Tarski engine is *not* a new engine in this sense — it is exactly the descent / quotient machinery applied to the formula layer, and so reduces to the algebraic toolkit. The genuinely new engines in the logic half — those *not* reducible to the algebraic toolkit — are **truth recursion**, **Henkin completeness**, and **compactness / ultraproducts**.

---

## III.2 · Map-type ledger

*The atlas uses a small number of map species repeatedly. Distinguishing them is how the development avoids calling everything "a function." Each is fixed by what it preserves.*

| Map | Form | Preserves / characterized by | Where |
|---|---|---|---|
| **generator insertion** `η` | $X\to T_\Sigma(X)$ | universal among maps from `X` | I.5; II.2 |
| **homomorphism** `h` | $\mathbf A\to\mathbf B$ | all operations | I.2 |
| **presentation comparison** `ρ`, `τ` | $T_\Sigma(X)\xrightarrow{\cong}\mathbf P$ | generator-preserving iso | I.9 |
| **parser / read-off** | concrete carrier $\to$ abstract syntax | inverse of a faithful presentation | I.8 |
| **substitution** `σ̂` | $T_\Sigma(X)\to T_\Sigma(Y)$ | operations, extends `σ` on generators | I.10; II.7 |
| **context operation / plug** | $\operatorname{Ctx}\times\text{fillings}\to T_\Sigma(X)$ | substitution at holes | I.11–I.13 |
| **evaluation** `ev = ĝ` | $T_\Sigma(X)\to\mathbf M_{\mathrm{alg}}$ | operations, into a semantic target | I.16; II.9 |
| **quotient projection** `π_θ` | $\mathbf A\to\mathbf A/\theta$ | surjective hom with kernel `θ` | I.4; II.15, II.16 |
| **descended map** `F̃` | $\mathbf A/\theta\to\mathbf B/\psi$ | well-defined on classes | I.18; II.6 |
| **embedding** `↪` | $\mathbf M\hookrightarrow\mathbf N$ | injective, reflects relations | II.17 |
| **elementary embedding** `≼` | $\mathbf M\preceq\mathbf N$ | all formulas | II.17 |
| **derivation / proof transform** | premises $\to$ conclusion | rule-closed | II.12, II.13 |

> [!warning] Two maps that look alike but are not
> Substitution `σ̂` and evaluation `ev` are both UMP extensions, distinguished only by target: substitution maps into a *free algebra* (output is syntax), evaluation into a *semantic algebra* (output is a value). The four-corner law of I.10 is precisely the statement that these two commute correctly; conflating them is the most common error the atlas is built to prevent.

---
## III.3 · Equality taxonomy

*The central payload of the synthesis. The word "equal" carries at least ten distinct meanings across the atlas, and most confusion in syntax-and-semantics comes from sliding between them. Each row gives the relation, the objects it relates, and the engine or condition that governs it. They are listed roughly from most syntactic to most semantic.*

| # | Equality | Relates | Holds when | Governed by |
|---|---|---|---|---|
| 1 | **raw syntax equality** | terms/raw formulas as abstract free elements | identical elements of `T_Σ(X)` / `Form^{raw}_L` | unique readability (I.6) |
| 2 | **presentation equality** | concrete carriers (trees, strings) | equal in a chosen presentation | presentation-bound; in a **faithful** presentation it corresponds **exactly** to (1) via the comparison iso `ρ` (I.8); only on an unfaithful candidate carrier can it differ from (1) |
| 3 | **transferred equality** | elements across presentations | corresponding under `τ_{P,Q}` | transfer / invariance criterion (I.9) |
| 4 | **alpha-equivalence** `≡_α` | raw formulas with binders | differ only by bound renaming | alpha-quotient descent (II.6) |
| 5 | **semantic equality under an assignment** | terms | `ev_{M,a}(t)=ev_{M,a}(u)` | evaluation kernel `κ_a` (I.17, II.9) |
| 6 | **equality in a structure** | elements / equality atoms | `M,a ⊨ t = u` | interpretation of `=` (II.8, II.10) |
| 7 | **provable equality** `≈_T` | terms | `T ⊢ t = u` | equality axioms, a congruence (II.15) |
| 8 | **quotient equality** | classes in `A/θ`, `TM(T)`, `LT(T)` | same `θ`/`≈_T`/`≡_T` class | descent (I.18, II.15, II.16) |
| 9 | **operation equality / identity** | term operations | equal under *all* assignments | `Id(A)`, clone kernel (I.17) |
| 10 | **definitional equality in a presentation** | defined vs primitive symbols | equal by a definitional extension | conservative definition (II.14) |

> [!warning] The four collapses that must never be silently merged
> (1) raw `≠` (5) semantic: distinct terms can evaluate equally. (5) one-assignment `≠` (9) all-assignment: equal under a valuation is weaker than an identity. (6) structure equality `≠` (7) provable equality: `M ⊨ t=u` for one model is weaker than `T ⊢ t=u`. (1) raw `≠` (4) alpha: $\forall x\,\varphi$ and $\forall y\,\varphi[y/x]$ are alpha-equal but not raw-equal. Every quotient in the atlas exists precisely to turn one of these weaker equalities into genuine identity of classes — and is legal only when descent (row 8) has been checked.

> [!result] The taxonomy as a refinement order
> Reading down the semantic columns: raw equality (1) refines into provable equality (7) by adding the theory's axioms, and provable equality refines into structure equality (6) in each model (soundness). Conversely completeness says structure equality in *all* models climbs back up to provable equality. Identities (9) are the all-assignment ceiling of one-assignment semantic equality (5). The atlas is, in one sentence, the bookkeeping that keeps these levels distinct and names the engine that moves between adjacent ones.

---

## III.4 · Where universal algebra enters logic

*The boundary statement of the whole atlas. Universal algebra is used in the logic half at exactly the following points and nowhere else. Each entry names the logical construction, the algebraic engine it invokes, and the precise reason the invocation is legitimate.*

1. **Functional reduct of a language.** The function and constant symbols of `L`, stripped of relations and logical symbols, are a signature `Σ_L`. *Legitimate because* a signature is exactly operation-symbol data; relations are deliberately excluded (II.1).

2. **Term formation as free algebra.** $\operatorname{Term}_L\cong T_{\Sigma_L}(\operatorname{Var})$. *Legitimate because* term formation is least-closure under the operation symbols with variables as generators — the defining property of the free algebra (II.2).

3. **Term denotation as homomorphic extension.** $\operatorname{ev}_{M,a}=\widehat{a}:T_{\Sigma_L}(\operatorname{Var})\to M_{\mathrm{alg}}$. *Legitimate because* an assignment is a generator map into the algebraic reduct, and the UMP extends it uniquely (II.9).

4. **Term substitution as syntax-valued extension.** $\widehat\sigma:T_{\Sigma_L}(X)\to T_{\Sigma_L}(Y)$ with the term monad's Kleisli law. *Legitimate because* substitution is the UMP applied with a *free* algebra as target (II.7, with capture-avoidance the extra logical obligation).

5. **Term model quotient by provable equality.** $\operatorname{TM}(T)=\operatorname{ClTerm}_L/{\approx_T}$. *Legitimate because* `≈_T` is a congruence on `Σ_L` (the equality axioms), so the quotient algebra and its descended interpretations exist (II.15).

6. **Descent checks for quotient-level syntax.** Connectives and quantifiers descend to `≡_α`-classes and `≡_T`-classes; relation symbols descend to `≈_T`-classes. *Legitimate because* each constructor preserves the relevant congruence — the well-definedness obligation of I.18 (II.6, II.15, II.16).

7. **Closure patterns for theories and derivations.** Deductive closure, rule closure, and generated theories are least-closed-set constructions. *Legitimate because* they are instances of the same closure engine as generated subalgebras, now over formulas and derivations rather than carriers (II.12, II.14).

> [!warning] Where universal algebra does *not* enter
> Relation symbols, equality atoms, Boolean connectives, quantifiers, binding, alpha-equivalence, satisfaction, soundness, completeness, compactness, Löwenheim–Skolem, and ultraproducts are **not** universal-algebra constructions. Formula formation is a separate inductive layer over the term algebra, not another free algebra (until deliberately algebraized at Lindenbaum–Tarski). The logic half reads correctly as logic with all seven entry points above deleted; they are accelerations, not foundations.

---
## III.5 · Final dependency maps

*Five maps close the atlas: the left-side algebraic-syntax spine, the right-side logic spine, the targeted transfer between them, the equality/descent skeleton, and the map of maps. None is the everything-graph the package warns against; each answers one question.*

**Left-side algebraic-syntax map** — *what Part I builds and hands forward.*

```mermaid
flowchart LR
    SIG["Σ"] --> FREE["T_Σ(X) + η"]
    FREE -->|"⚙ UMP"| MOVE["recursion · substitution · evaluation · transfer"]
    SIG --> CONG["θ, A/θ"]
    FREE -->|"evaluation"| KER["κ_g"]
    KER -->|"⚙ first-iso"| IMG["⟨g[X]⟩ ≅ T_Σ(X)/κ_g"]
    CONG -->|"⚙ descend"| QS["quotient syntax"]
    FREE --> CTX["contexts · clone · templates"]
```

**Right-side logic map** — *what Part II builds, logic-first.*

```mermaid
flowchart LR
    L["L"] --> SIGL["Σ_L"]
    SIGL --> TERM["Term_L"]
    TERM --> ATOM["Atom_L"]
    ATOM --> RAW["Form^raw_L"]
    RAW -->|"⚙ alpha"| FORM["Form_L"]
    STR["M + assignment a"] --> EVAL["term denotation"]
    TERM --> EVAL
    EVAL --> SAT["⊨ satisfaction"]
    FORM --> SAT
    SAT --> SEM["consequence ⊨"]
    FORM -->|"⚙ rule closure"| DED["⊢ deduction"]
    SEM <-->|"sound + complete"| DED
    DED --> THY["theories · TM(T) · LT(T)"]
    THY --> MT["models · types · compactness"]
```

**Targeted UA-transfer map** — *the seven entry points of III.4, and only those.*

```mermaid
flowchart LR
    SIG["Σ (UA)"] -. "functional reduct" .-> SIGL["Σ_L"]
    FREE["T_Σ(X) (UA)"] -. "term formation" .-> TERM["Term_L"]
    UMP["⚙ UMP (UA)"] -. "term denotation" .-> EVAL["ev_M,a"]
    UMP -. "term substitution" .-> SUBST["σ̂ on Term_L"]
    DESC["⚙ descend (UA)"] -. "term/formula quotient" .-> QUOT["TM(T) · LT(T)"]
    CLOSE["⚙ closure (UA)"] -. "theories · derivations" .-> CLOS["Cn(T) · ⊢-closure"]
```

**Equality / descent skeleton** — *the refinement ladder of III.3.*

```mermaid
flowchart TD
    RAW["1 · raw syntax ="] --> ALPHA["4 · ≡_α"]
    RAW --> PROV["7 · provable = (≈_T)"]
    PROV --> STRUCT["6 · = in a structure (one M)"]
    SEMA["5 · semantic = under a"] --> IDENT["9 · identity (all a)"]
    ALPHA -->|"⚙ descend"| QUOTE["8 · quotient ="]
    PROV -->|"⚙ descend"| QUOTE
    PROV <-->|"sound / complete"| ALLM["= in **all** models<br/>(semantic consequence on equations)"]
    STRUCT -. "one model is weaker than all" .-> ALLM
```

**Final atlas map of maps** — *the three movements and the single thread between them.*

```mermaid
flowchart LR
    subgraph PI["PART I · algebraic syntax"]
        A1["free syntax"] --> A2["operations · evaluation"] --> A3["kernels · quotients · descent"]
    end
    subgraph PII["PART II · first-order logic"]
        B1["language · terms"] --> B2["formulas · binding · semantics"] --> B3["deduction · theories · models"]
    end
    subgraph PIII["PART III · synthesis"]
        C1["engines"] --- C2["maps"] --- C3["equalities"] --- C4["transfer points"]
    end
    A1 -. "term formation" .-> B1
    A2 -. "denotation · substitution" .-> B2
    A3 -. "term/LT quotients" .-> B3
    PI --> PIII
    PII --> PIII
```

**Hands up — the whole atlas.** Universal algebra supplies one reusable engine room: free syntax, the UMP, kernels, and descent. First-order logic is developed in its own terms and reaches into that engine room at exactly seven points — functional reduct, term formation, denotation, substitution, term-model quotient, descent checks, and closure — while supplying its own irreducible content in binding, satisfaction, completeness, and the model theory that compactness and ultraproducts make possible. The discipline of the atlas is to name each transfer precisely, keep the term layer apart from the formula layer, fix the equivalence before quotienting, and prove descent before using representatives.

$$
\boxed{\text{free algebra builds terms; inductive closure builds formulas; the term UMP interprets terms, structural recursion interprets formulas; kernels measure collapse; descent licenses quotients.}}
$$
