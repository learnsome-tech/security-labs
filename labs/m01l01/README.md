# m01l01 · The Threat Model Habit

Module 1: The Security Mindset · lesson 1.1 · Free · [Open the lesson](https://learnsome.tech/learn/security-course/m01l01)

**Goal:** You can threat model a change in a few minutes by naming its data flows, its trust boundaries and its entry points, walking STRIDE over each one, and writing down only the answers that change what you build.

## Labs

| Lab | What it is | Check |
| --- | --- | --- |
| [m01l01-03](m01l01-03/) | Question one: where does the data actually go? | Graded |
| [m01l01-05](m01l01-05/) | The open questions are the output | Graded |
| [m01l01-06](m01l01-06/) | Attack surface, counted rather than felt | Graded |

## Exercises

Open exercises from the lesson, to try on your own. They have no answer files: work them out, and use the labs above as reference.

### Threat model the thing you are working on now

1. List the data flows of your current change, with what each carries and which network it uses.
2. Mark every flow that crosses a trust boundary, and say what protects the crossing.
3. Walk the six STRIDE prompts over the newest entry point; note the ones you cannot answer.
4. Turn each unanswered prompt into a ticket with an owner, or a written decision to accept it.

> **Hint:** If the exercise takes longer than ten minutes, your scope is a system rather than a change.

## Check yourself

- What are the four questions, and which one do teams most often skip?
- Why does the first question ask for data flows rather than components?
- What does STRIDE stand for, and what is the useful output of walking it?
- Why is a route path containing the word internal not a security control?
- What triggers a threat model in the habit version, and where do the open questions live?

---

[Course README](../../README.md) · [Application Security & Threat Modeling for Engineers on LearnSome.tech](https://learnsome.tech/courses/security-course)
