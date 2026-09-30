# m04l01 · TLS And The Handshake

Module 4: API Security · lesson 4.1 · Pro · [Open the lesson](https://learnsome.tech/learn/security-course/m04l01)

**Goal:** You can say exactly what a completed handshake proves and what it leaves open, read a certificate verification error and name the reason, and tell the difference between a client that checks a chain and a client that only encrypts.

## Labs

| Lab | What it is | Check |
| --- | --- | --- |
| [m04l01-02](m04l01-02/) | Signing a certificate with your own authority | Graded |
| [m04l01-03](m04l01-03/) | A real handshake, both ends in one process | Read along |
| [m04l01-04](m04l01-04/) | Exploit: the client that verifies nothing | Read along |
| [m04l01-05](m04l01-05/) | Fix: verification on, and read the complaints | Read along |
| [m04l01-06](m04l01-06/) | Pinning: trusting one key instead of an authority | Read along |

## Exercises

Open exercises from the lesson, to try on your own. They have no answer files: work them out, and use the labs above as reference.

### Prove your own clients really check

1. List every place your code builds an HTTP client, a socket wrapper or a driver.
2. Search for verify equals false, insecure skip verify and certificate none.
3. Point one client at a service whose certificate names something else; confirm it refuses.
4. Add an alarm on days remaining for every certificate you serve or depend on.

> **Hint:** Test frameworks, container base images and internal service meshes are where verification quietly goes missing.

## Check yourself

- In one sentence, what does a completed handshake prove about the peer?
- Name two things it does not prove, and give an example of each.
- What is the difference between a hostname mismatch and an unknown issuer error?
- Why is a client with verification disabled worse than an obviously plain connection?
- What does certificate pinning buy you, and what outage does it invite?

---

[Course README](../../README.md) · [Application Security & Threat Modeling for Engineers on LearnSome.tech](https://learnsome.tech/courses/security-course)
