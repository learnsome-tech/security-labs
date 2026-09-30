# m02l02-06 · Fix: a file only the service account can read

**Lesson:** [The Environment Variable Trap](https://learnsome.tech/learn/security-course/m02l02) (lesson 2.2, module 2: Secrets And Identity) · Pro  
**Check:** Graded

## Goal

You can explain why an environment variable beats a hardcoded credential and still is not a secret store, narrow what a child process inherits, and read a secret from a permission restricted file instead.

In the lesson: The second fix stops using the environment as the channel at all. Write the value to a file that only the service account can read, and open it at the moment you need it. Run the file based version. The mode is owner read and write, group and other are refused, the token comes back through an ordinary file handle, and there is nothing in the environment to inherit or to dump. Container platforms do exactly this when they mount a secret as a file instead of injecting a variable, and it is the better of the two choices they offer you. Read it late, keep it in one place, and do not copy it onward.

## Files

- [`starter/file_fixed.py`](starter/file_fixed.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m02l02/m02l02-06/starter`
2. Read `file_fixed.py`.
3. Notes from the lesson:
   - Line 5: created with a restrictive mode, rather than created and then fixed
4. Run it: `python3 file_fixed.py`.
5. Check it from the repository root: `./check m02l02-06`.

## Expected output

```text
mode on the secret file: 0o600
group or other can read it: False
token read from the file: sk-live-demo
token in the environment: None
```

## How to check

`./check m02l02-06` copies `starter/` into a scratch directory and runs `python3 file_fixed.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/security-course/m02l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
