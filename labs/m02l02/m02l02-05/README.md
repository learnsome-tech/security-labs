# m02l02-05 · Fix: give the child an environment, do not hand over yours

**Lesson:** [The Environment Variable Trap](https://learnsome.tech/learn/security-course/m02l02) (lesson 2.2, module 2: Secrets And Identity) · Pro  
**Check:** Graded

## Goal

You can explain why an environment variable beats a hardcoded credential and still is not a secret store, narrow what a child process inherits, and read a secret from a permission restricted file instead.

In the lesson: The first fix narrows inheritance. Rather than letting the child take everything, we build the environment it receives, naming the two variables it actually needs. Run the narrowed version. The service still holds its token, and the child now sees nothing at all. This is cheap, and it is almost never done, which is why it is worth making a habit everywhere your code starts another process. Notice the shape of the fix. It is the same shape as least privilege from the previous module: give the next process the smallest context that lets it do its work, and decide that explicitly rather than by default.

## Files

- [`starter/child_fixed.py`](starter/child_fixed.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m02l02/m02l02-05/starter`
2. Read `child_fixed.py`.
3. Notes from the lesson:
   - Line 8: name what the child needs; inheritance is a default, not a decision
4. Run it: `python3 child_fixed.py`.
5. Check it from the repository root: `./check m02l02-05`.

## Expected output

```text
child sees API_TOKEN: None
the service still holds the token
the child was given an environment, not handed ours
```

## How to check

`./check m02l02-05` copies `starter/` into a scratch directory and runs `python3 child_fixed.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/security-course/m02l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
