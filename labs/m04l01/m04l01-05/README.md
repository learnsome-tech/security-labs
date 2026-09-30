# m04l01-05 · Fix: verification on, and read the complaints

**Lesson:** [TLS And The Handshake](https://learnsome.tech/learn/security-course/m04l01) (lesson 4.1, module 4: API Security) · Pro  
**Check:** Read along

## Goal

You can say exactly what a completed handshake proves and what it leaves open, read a certificate verification error and name the reason, and tell the difference between a client that checks a chain and a client that only encrypts.

In the lesson: The fix is to let the library do its job, and the instructive part is the shape of its complaints. The helper builds a default context, which checks both the hostname and the chain, and then tries three connections. Asking for payments dot internal against the orders certificate raises a certificate verification error whose message is a hostname mismatch. Asking for the right name while trusting only the system authorities raises the same class of error with a different reason: unable to get local issuer certificate. Asking for the right name with our own authority trusted succeeds. Two distinct failures and one success, and every one of those lines came out of the library rather than off a slide.

## Files

- [`starter/mkcert.sh`](starter/mkcert.sh)
- [`starter/tls_on.py`](starter/tls_on.py): the listing from the lesson
- [`starter/tlsserver.py`](starter/tlsserver.py)
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/tls_on.py` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m04l01-05` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/security-course/m04l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
