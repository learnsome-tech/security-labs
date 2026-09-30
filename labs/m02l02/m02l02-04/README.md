# m02l02-04 · Exploit: the diagnostics dump prints it too

**Lesson:** [The Environment Variable Trap](https://learnsome.tech/learn/security-course/m02l02) (lesson 2.2, module 2: Secrets And Identity) · Pro  
**Check:** Graded

## Goal

You can explain why an environment variable beats a hardcoded credential and still is not a secret store, narrow what a child process inherits, and read a secret from a permission restricted file instead.

In the lesson: The second gap is that the environment is data, so it gets dumped like data. Here a service fails while rendering, catches the error, and prints diagnostics, and the diagnostics include the environment, because that is the standard thing to attach. It even tries to be tidy, skipping names that begin with an underscore. Run the diagnostics demo. The token is listed as calmly as the locale is. This is not hypothetical: error pages, crash reporters, support bundles and container inspection commands all do some version of this, and the result usually travels to somebody outside the team that owns the secret.

## Files

- [`starter/dump_env.py`](starter/dump_env.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m02l02/m02l02-04/starter`
2. Read `dump_env.py`.
3. Notes from the lesson:
   - Line 13: even a dump that tries to be tidy still prints the credential
4. Run it: `python3 dump_env.py`.
5. Check it from the repository root: `./check m02l02-04`.

## Expected output

```text
internal error: template step failed
diagnostics, environment follows:
 - API_TOKEN = sk-live-4d1f-demo
 - LANG = C.UTF-8
 - PATH = /usr/bin
 - SERVICE = billing
```

## How to check

`./check m02l02-04` copies `starter/` into a scratch directory and runs `python3 dump_env.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/security-course/m02l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
