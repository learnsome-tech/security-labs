# m05l05 · Container Security: Minimal Bases And Non Root

Module 5: The Supply Chain · lesson 5.5 · Pro · [Open the lesson](https://learnsome.tech/learn/security-course/m05l05)

**Goal:** You can reduce an image attack surface with a minimal base and a non root user, inspect those properties in a Dockerfile, and place an image scan where it can block an unsafe release.

## Labs

| Lab | What it is | Check |
| --- | --- | --- |
| [m05l05-02](m05l05-02/) | Count the packages a base image brings | Graded |
| [m05l05-03](m05l05-03/) | A Dockerfile can make root explicit | Graded |
| [m05l05-04](m05l05-04/) | The process really runs with a reduced identity | Graded |
| [m05l05-05](m05l05-05/) | Drop capabilities and make the filesystem read only | Graded |
| [m05l05-06](m05l05-06/) | Scan the image before it becomes a release | Read along |

## Exercises

Open exercises from the lesson, to try on your own. They have no answer files: work them out, and use the labs above as reference.

### Harden one image you own

1. List every package and executable in the current runtime image.
2. Change the Dockerfile to use a smaller base and an explicit user.
3. Run the image as non root with a read only root filesystem.
4. Add a scan gate that blocks high and critical findings.

> **Hint:** If a debugging tool is needed in production, first ask whether it belongs in a separate diagnostic image.

## Check yourself

- Why does a minimal base reduce impact after an application exploit?
- What does an explicit non root user change inside a container?
- Why pair a non root user with a read only root filesystem?
- Where should an image scan run, and what should its exit status do?
- Why pin a base image by digest and still rebuild it regularly?

---

[Course README](../../README.md) · [Application Security & Threat Modeling for Engineers on LearnSome.tech](https://learnsome.tech/courses/security-course)
