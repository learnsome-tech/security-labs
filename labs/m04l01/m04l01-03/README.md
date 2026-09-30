# m04l01-03 · A real handshake, both ends in one process

**Lesson:** [TLS And The Handshake](https://learnsome.tech/learn/security-course/m04l01) (lesson 4.1, module 4: API Security) · Pro  
**Check:** Read along

## Goal

You can say exactly what a completed handshake proves and what it leaves open, read a certificate verification error and name the reason, and tell the difference between a client that checks a chain and a client that only encrypts.

In the lesson: Now a genuine session, with both ends inside one program. The server side loads the certificate and its matching private key, then listens on the loopback address with port zero, so the operating system hands us a free port and nothing is written down. A background thread accepts one connection and wraps it. The client builds a trust store holding only our own authority, connects, and asks for the name orders dot internal. Watch the four lines it prints. The protocol version was negotiated rather than chosen by us. The cipher suite was agreed during the handshake. The peer subject was read out of the certificate the server presented. Then application bytes cross a channel that is now encrypted.

## Files

- [`starter/mkcert.sh`](starter/mkcert.sh)
- [`starter/tls_session.py`](starter/tls_session.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/tls_session.py` alongside the lesson.
2. Follow it the way the lesson builds it:
   - Lines 1–7: the loopback address with port zero
   - Lines 8–13: A background thread
   - Lines 14–21: Watch the four lines

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m04l01-03` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/security-course/m04l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
