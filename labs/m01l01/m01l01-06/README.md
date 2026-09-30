# m01l01-06 · Attack surface, counted rather than felt

**Lesson:** [The Threat Model Habit](https://learnsome.tech/learn/security-course/m01l01) (lesson 1.1, module 1: The Security Mindset) · Free  
**Check:** Graded

## Goal

You can threat model a change in a few minutes by naming its data flows, its trust boundaries and its entry points, walking STRIDE over each one, and writing down only the answers that change what you build.

In the lesson: One more piece of question one, and it is the cheapest security review there is. List every route with two facts about each: does it require a caller to be authenticated, and does it change state. Run it over the table and one line comes back marked as a finding: a refund endpoint that anybody can call. That is not a hypothetical. It is the single most common serious finding in real reviews, and it usually arrives the way this one did, on a route somebody believed was private because of where it sat. The word internal in a path is a naming convention. It is not a network control and it is not a permission.

## Files

- [`starter/surface.py`](starter/surface.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m01l01/m01l01-06/starter`
2. Read `surface.py`.
3. Notes from the lesson:
   - Line 4: internal in the path is a naming convention, not a control
4. Run it: `python3 surface.py`.
5. Check it from the repository root: `./check m01l01-06`.

## Expected output

```text
GET /health anonymous ok
POST /orders auth ok
POST /internal/refund anonymous FINDING
GET /orders/{id} auth ok
routes: 4
anonymous and state changing: 1
```

## How to check

`./check m01l01-06` copies `starter/` into a scratch directory and runs `python3 surface.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/security-course/m01l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
