# m01l04-04 · Fail closed: the new route nobody thought about

**Lesson:** [Secure Defaults](https://learnsome.tech/learn/security-course/m01l04) (lesson 1.4, module 1: The Security Mindset) · Free  
**Check:** Graded

## Goal

You can tell a permissive default from a safe one, make the unsafe setting the one that has to be asked for and refused in production, and design interfaces that fail closed so a new route or a new caller is denied rather than served.

In the lesson: Defaults are not only configuration. They are also what your code does in a case nobody wrote down. Here a table maps each route to an authorisation policy, and the question is what happens to a route that is not in the table. Run the three calls. The known route is served under its policy. The brand new refunds route, under the permissive rule, is served with no check whatever, which is the finding from the first lesson arriving by a different door. Under the fail closed rule the same route raises, because an undeclared route is a bug. Wire that check into startup or into a test and the failure lands on the engineer who added the route, which is the only person who can fix it cheaply.

## Files

- [`starter/failclosed.py`](starter/failclosed.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m01l04/m01l04-04/starter`
2. Read `failclosed.py`.
3. Notes from the lesson:
   - Line 8: an undeclared route is a bug, so it stops the build rather than serving
4. Run it: `python3 failclosed.py`.
5. Check it from the repository root: `./check m01l04-04`.

## Expected output

```text
known route: served under policy owner
brand new route, permissive: served without any check
Traceback (most recent call last):
  File "failclosed.py", line 13, in <module>
    print("brand new route, fail closed:", route("/refunds", False))
  File "failclosed.py", line 8, in route
    raise LookupError("no policy declared for " + path)
LookupError: no policy declared for /refunds
```

## How to check

`./check m01l04-04` copies `starter/` into a scratch directory and runs `python3 failclosed.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/security-course/m01l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
