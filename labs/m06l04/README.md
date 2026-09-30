# m06l04 · Secret Scanning

Module 6: Scanning And The Pipeline · lesson 6.4 · Pro · [Open the lesson](https://learnsome.tech/learn/security-course/m06l04)

**Goal:** You can detect common credential shapes and high entropy strings, explain why scanning history matters, and stop a new secret before it reaches the repository.

## Labs

| Lab | What it is | Check |
| --- | --- | --- |
| [m06l04-02](m06l04-02/) | Recognise named credential shapes | Graded |
| [m06l04-03](m06l04-03/) | Entropy finds secrets without a known prefix | Graded |
| [m06l04-04](m06l04-04/) | A working tree can be clean while history is not | Graded |
| [m06l04-05](m06l04-05/) | Stop a new secret at the commit boundary | Graded |

## Exercises

Open exercises from the lesson, to try on your own. They have no answer files: work them out, and use the labs above as reference.

### Remove one real secret safely

1. Run a detector over the current tree and recent history.
2. Rotate every value it finds before editing source.
3. Move configuration to the approved secret path.
4. Add a central gate and test it with a fake token.

> **Hint:** Use a fake token in the test so the exercise cannot create a second incident.

## Check yourself

- Why does deleting a secret from the current file not revoke the exposure?
- What does entropy add beyond named credential patterns?
- Why rotate before investigating where the value travelled?
- Where should a secret gate run if local hooks can be skipped?
- How can scanner output avoid spreading the secret further?

---

[Course README](../../README.md) · [Application Security & Threat Modeling for Engineers on LearnSome.tech](https://learnsome.tech/courses/security-course)
