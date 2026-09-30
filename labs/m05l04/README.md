# m05l04 · Provenance And Signing

Module 5: The Supply Chain · lesson 5.4 · Pro · [Open the lesson](https://learnsome.tech/learn/security-course/m05l04)

**Goal:** You can explain what provenance records, verify that a release was signed by the expected builder, and reject an artefact whose bytes or origin no longer match the release policy.

## Labs

| Lab | What it is | Check |
| --- | --- | --- |
| [m05l04-02](m05l04-02/) | A digest catches one changed byte | Graded |
| [m05l04-03](m05l04-03/) | Signing and verifying the exact artefact | Graded |
| [m05l04-04](m05l04-04/) | Provenance makes the build claim testable | Graded |
| [m05l04-05](m05l04-05/) | Reject the wrong builder before deployment | Graded |
| [m05l04-06](m05l04-06/) | A real signing tool in the pipeline | Read along |

## Exercises

Open exercises from the lesson, to try on your own. They have no answer files: work them out, and use the labs above as reference.

### Trace one artefact end to end

1. Choose an image or package that your team deploys.
2. Find its digest, source revision, builder identity and signature.
3. Write the exact policy that would reject a laptop build.
4. Rotate a test key and document how verifiers learn the change.

> **Hint:** If you cannot find one field, that missing link is a supply chain control to add.

## Check yourself

- What question does a digest answer, and what question does it leave open?
- Why should a deployment policy check builder identity as well as a signature?
- Name four fields a useful provenance statement records.
- Where should a private signing key live, and what happens when it is rotated?
- Why is a signature not evidence that code is safe?

---

[Course README](../../README.md) · [Application Security & Threat Modeling for Engineers on LearnSome.tech](https://learnsome.tech/courses/security-course)
