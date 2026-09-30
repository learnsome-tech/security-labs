# m05l03 · Software Bill Of Materials

Module 5: The Supply Chain · lesson 5.3 · Pro · [Open the lesson](https://learnsome.tech/learn/security-course/m05l03)

**Goal:** You can generate a machine readable bill of materials for a build, answer whether a new advisory affects you by querying it with a correct version comparison, and say what such a document does not cover.

## Labs

| Lab | What it is | Check |
| --- | --- | --- |
| [m05l03-02](m05l03-02/) | Generating one, in the shape a tool would | Graded |
| [m05l03-03](m05l03-03/) | Answering are we affected, properly | Graded |
| [m05l03-04](m05l03-04/) | Two different documents: source and image | Graded |
| [m05l03-05](m05l03-05/) | What a dedicated generator adds | Read along |

## Exercises

Open exercises from the lesson, to try on your own. They have no answer files: work them out, and use the labs above as reference.

### Time your own answer

1. Pick a recent advisory for a library your organisation plausibly uses.
2. Answer whether you run it, and in which services, without asking anybody.
3. Time yourself, then find where the answer would have come from faster.
4. Add a build step that stores an inventory beside each artefact.

> **Hint:** If the answer required reading a lockfile by hand in more than one repository, that is the gap the inventory fills.

## Check yourself

- What question is a bill of materials built to answer, and how long does that answer take without one?
- Why does a package URL make the document more useful than a list of names?
- Give a version pair where text comparison and version comparison disagree.
- Why is an inventory of your source not enough for something you ship as an image?
- Name two kinds of component a generator can legitimately miss.

---

[Course README](../../README.md) · [Application Security & Threat Modeling for Engineers on LearnSome.tech](https://learnsome.tech/courses/security-course)
