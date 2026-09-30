# m04l01-06 · Pinning: trusting one key instead of an authority

**Lesson:** [TLS And The Handshake](https://learnsome.tech/learn/security-course/m04l01) (lesson 4.1, module 4: API Security) · Pro  
**Check:** Read along

## Goal

You can say exactly what a completed handshake proves and what it leaves open, read a certificate verification error and name the reason, and tell the difference between a client that checks a chain and a client that only encrypts.

In the lesson: Pinning narrows trust further. Instead of accepting anything your authority signs, the client carries a hash of the exact certificate or public key it expects and refuses everything else. This program verifies the chain in the ordinary way, then compares a hash taken from the live peer with the hash it was shipped with. The shipped pin matches. A pin from an older certificate does not, and that is the honest cost of pinning: on the day you rotate the key, every client carrying the old pin stops working. Mutual authentication is the other direction of the same idea, where the server demands a certificate from the caller as well, so both ends prove a name.

## Files

- [`starter/mkcert.sh`](starter/mkcert.sh)
- [`starter/pinning.py`](starter/pinning.py): the listing from the lesson
- [`starter/tlsserver.py`](starter/tlsserver.py)
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/pinning.py` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m04l01-06` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/security-course/m04l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
