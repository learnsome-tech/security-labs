# m04l03-03 · Exploit: an update that changes the owner

**Lesson:** [Mass Assignment](https://learnsome.tech/learn/security-course/m04l03) (lesson 4.3, module 4: API Security) · Pro  
**Check:** Read along

## Goal

You can recognise a handler that copies a request body into a model, replace it with a per-operation allowlist that rejects unknown fields loudly, and serialise responses from a named field list so private columns never reach a client.

In the lesson: Creation is the famous case, but updates are worse, because an update reaches an object that already exists and already matters. This endpoint is documented as a way to attach a delivery note to an order. Run the second exploit. The first call does what the documentation says. The second call carries three more keys and, in one request, marks the order paid, marks it refunded, and moves it to a different owner. Think about what those three fields mean downstream: a fulfilment job that ships on paid, a finance report that sums refunds, an authorisation check elsewhere that reads the owner and now agrees the attacker owns it. The note field was never the risk.

## Files

- [`starter/apilab.py`](starter/apilab.py)
- [`starter/mass_update.py`](starter/mass_update.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/mass_update.py` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m04l03-03` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/security-course/m04l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
