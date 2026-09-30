# m05l01-05 · Treat a new dependency the way you treat code

**Lesson:** [Dependency Risk And Typosquatting](https://learnsome.tech/learn/security-course/m05l01) (lesson 5.1, module 5: The Supply Chain) · Pro  
**Check:** Graded

## Goal

You can describe the trust surface a single install command opens, detect a name that is one edit away from a package you meant, and name the four defences that shrink the surface without stopping delivery.

In the lesson: The defence that actually scales is boring. Keep a table of names and versions somebody has looked at, refuse anything that is not pinned to one exact version, and refuse any name that is not in the table until a human adds it in a reviewed change. Run the gate over four requested lines. Two pass. One is rejected because a range is not a decision, it is a promise to accept whatever appears later. One is rejected because nobody has ever heard of it, which is precisely the state a typosquat arrives in. Notice that this gate is code in your repository, so adding a dependency becomes a diff with an author and a reviewer, like every other change.

## Files

- [`starter/gate.py`](starter/gate.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m05l01/m05l01-05/starter`
2. Read `gate.py`.
3. Notes from the lesson:
   - Line 4: a range is not a decision: it delegates the choice to a stranger
4. Run it: `python3 gate.py`.
5. Check it from the repository root: `./check m05l01-05`.

## Expected output

```text
allow  requests==2.32.3
REJECT urllib3>=2.0 - not pinned to a single version
allow  colorama==0.4.6
REJECT leftpad-py==0.0.1 - unreviewed name, open a review
```

## How to check

`./check m05l01-05` copies `starter/` into a scratch directory and runs `python3 gate.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/security-course/m05l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
