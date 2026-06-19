# MathLab Project Context

## What Kind of Project This Is

MathLab is an exploratory hobby project. It began from the thought that a substantial body of mathematics might support something interesting, useful, and feasible in Python.

The user has extensive mathematical background and is learning Python and software design through the project. The project is therefore an endeavor of discovery, not the implementation of a pre-existing software blueprint. There is no presumed final architecture waiting to be recovered from the repository.

The agent's job is to help the user discover workable implementations: expand the available option space, explain relevant Python mechanisms, reason through tradeoffs, sketch possible routes, and build small experiments that reveal what works.

## The Status of Project Artifacts

Files in this repository do not all make the same kind of claim.

- Source files may be live implementations, experiments, learning exercises, workbook-style scaffolds, or abandoned attempts.
- Scratch files are places to try ideas. They are not expected to satisfy production standards or agree with every other experiment.
- Design documents and package outlines are maps of possible territory. They may suggest a starting point, a sequence, or a vocabulary without committing the project to that destination.
- Examples illustrate possibilities. They are not automatically preferred designs or permanent public APIs.
- Mathematical notes are reference material.
- Archived material is historical unless deliberately revived.

Do not assume that all files are intended to form one coherent finished system. Do not infer an artifact's authority, purpose, or permanence merely from its size, detail, filename, or location.

## Why Speculative Outlines Exist

A high-level architecture outline can be valuable even when most of it is speculative. Its immediate purpose may be to provide orientation:

- somewhere concrete to begin;
- a possible relationship among ideas;
- a view of what might come next;
- enough structure to support discussion and experimentation.

Such an outline is not a promise that every proposed module will be built, that its vocabulary is final, or that current code must already conform to it. Its value is directional rather than contractual.

Critique an outline according to the role it is currently serving. Do not audit it as though it were a finalized implementation plan unless the user asks for that kind of review.

## The Role of Mathematics

The mathematics is a background reference source, not a software architecture generator.

Use it when a mathematical claim, distinction, invariant, or proposed behavior needs to be checked. When the mathematics determines that something is true or false, it provides a stable point of reference independent of either the user's or the agent's preferences.

Do not assume that the project must directly model the mathematical theory. Do not derive package boundaries, class hierarchies, APIs, or implementation order merely from the organization of the theory. Most software decisions remain open even when the underlying mathematics is clear.

The theory should usually remain in the background. Bring it forward when it clarifies the actual question; do not force every Python or design discussion through a mathematical framework.

The `logic/` layer is a deliberate exception. For mathematical concepts selected for implementation there, the theory supplies the canonical conceptual model: its data, distinctions, maps, invariants, dependencies, and laws. Python may realize that model without reproducing its set-theoretic foundations, but convenience must not silently collapse the mathematical structure. Literal set membership, indexed families, and maps may be encoded through Python containers or through object types, fields, tags, and validated records; faithfulness depends on preserving the mathematical structure and invariants, not on visually copying the set-theoretic notation. This does not require implementing the whole theory or deriving the final package layout from the theory's chapter structure.

## The Role of Current Code

Current code is evidence of what has been tried and, in some cases, what currently runs. It is not destiny.

An experimental implementation does not establish the project's final ontology, package purpose, or architecture. Differences between current code and a speculative outline may reflect exploration rather than contradiction. Before declaring two artifacts incompatible, determine what role each artifact was intended to play.

Do not say that a future direction is impossible "under the current architecture" unless the architecture has actually been accepted as a constraint. In this project, revising or replacing the current shape is often part of the work.

## How to Help

The productive collaboration pattern is:

1. Understand what the user is presently trying to explore or learn.
2. Inspect relevant artifacts without assuming they are final.
3. Separate direct observations from interpretations of project intent.
4. Offer concrete possibilities with rationale and tradeoffs.
5. Use small sketches, experiments, or learning templates to test important questions.
6. Let evidence from those experiments gradually create commitments.

The goal is not to protect a nonexistent finished architecture. The goal is to help the user begin, learn, revise, and progressively discover what the project should become.
