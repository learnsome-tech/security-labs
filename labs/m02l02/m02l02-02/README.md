# m02l02-02 · The step up: settings read at start up

**Lesson:** [The Environment Variable Trap](https://learnsome.tech/learn/security-course/m02l02) (lesson 2.2, module 2: Secrets And Identity) · Pro  
**Check:** Graded

## Goal

You can explain why an environment variable beats a hardcoded credential and still is not a secret store, narrow what a child process inherits, and read a secret from a permission restricted file instead.

In the lesson: Here is the step up, done properly. The service reads its settings from the environment at start up, and when a required name is missing it exits immediately with a clear message, rather than running with an empty string and failing somewhere confusing three hours later. The launcher supplies the value on the command line in front of the program. Run it through the launcher. The token loads, we print only a masked tail of it, and the source file itself contains no credential at all. This much is genuinely better than a literal in the code. Everything that follows is about what the environment still cannot do for you.

## Files

- [`starter/app.py`](starter/app.py): the listing from the lesson
- [`starter/command.txt`](starter/command.txt)
- [`starter/step.sh`](starter/step.sh)
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m02l02/m02l02-02/starter`
2. Read `app.py`.
3. Notes from the lesson:
   - Line 6: fail at start up, not on the first request that needed the setting
   - Line 9: step.sh runs: API_TOKEN=sk-live-4d1f-demo python3 app.py
4. Run it: `bash step.sh`.
5. Check it from the repository root: `./check m02l02-02`.

## Expected output

```text
token loaded from the environment: sk-live-demo
the source file holds no credential
the deployment holds it instead
```

## How to check

`./check m02l02-02` copies `starter/` into a scratch directory and runs `bash step.sh` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/security-course/m02l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
