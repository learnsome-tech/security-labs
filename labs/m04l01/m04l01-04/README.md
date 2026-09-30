# m04l01-04 · Exploit: the client that verifies nothing

**Lesson:** [TLS And The Handshake](https://learnsome.tech/learn/security-course/m04l01) (lesson 4.1, module 4: API Security) · Pro  
**Check:** Read along

## Goal

You can say exactly what a completed handshake proves and what it leaves open, read a certificate verification error and name the reason, and tell the difference between a client that checks a chain and a client that only encrypts.

In the lesson: Here is the failure you will meet most often in real code, usually added to make a test pass on a Friday afternoon. The client context sets check hostname to false and verify mode to certificate none. These two lines are the whole vulnerability. Then it connects and asks for payments dot internal, while the server is holding a certificate that names the orders service instead. Run the exploit. The handshake completes. The version and the cipher suite look identical to the good session. And the certificate the client validated prints as an empty dictionary, because it validated nothing. You have privacy from a passive listener and no defence whatever against anybody who can answer in the server's place.

## Files

- [`starter/mkcert.sh`](starter/mkcert.sh)
- [`starter/tls_off.py`](starter/tls_off.py): the listing from the lesson
- [`starter/tlsserver.py`](starter/tlsserver.py)
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/tls_off.py` alongside the lesson.
2. Notes from the lesson:
   - Line 5: these two lines are the whole vulnerability, and they look like config

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m04l01-04` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/security-course/m04l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
