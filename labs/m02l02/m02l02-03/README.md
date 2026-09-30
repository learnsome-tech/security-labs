# m02l02-03 · Exploit: every child process inherits it

**Lesson:** [The Environment Variable Trap](https://learnsome.tech/learn/security-course/m02l02) (lesson 2.2, module 2: Secrets And Identity) · Pro  
**Check:** Graded

## Goal

You can explain why an environment variable beats a hardcoded credential and still is not a secret store, narrow what a child process inherits, and read a secret from a permission restricted file instead.

In the lesson: The first gap is blast radius, and it follows from how processes work. A child inherits the parent's environment unless somebody says otherwise. Our service sets a token, starts a helper, and the helper prints what it can see. Run the exploit. The child has the credential and it never asked for it. Now widen that out: the image conversion binary you shell out to, the archive tool, the crash reporter that gathers diagnostics before uploading them, the profiler, the shell somebody opens during an incident. Every one of them inherits the same copy. A dependency does not have to be malicious to leak your token, only talkative.

## Files

- [`starter/child_vuln.py`](starter/child_vuln.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m02l02/m02l02-03/starter`
2. Read `child_vuln.py`.
3. Notes from the lesson:
   - Line 9: no environment argument means: hand the child everything we hold
4. Run it: `python3 child_vuln.py`.
5. Check it from the repository root: `./check m02l02-03`.

## Expected output

```text
child sees API_TOKEN: sk-live-4d1f-demo
the service holds the token
every helper it shells out to receives the same copy
```

## How to check

`./check m02l02-03` copies `starter/` into a scratch directory and runs `python3 child_vuln.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/security-course/m02l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
