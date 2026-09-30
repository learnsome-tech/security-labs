# m02l01-06 · Fix: mask at the logger, not at every call site

**Lesson:** [Why Secrets Leak](https://learnsome.tech/learn/security-course/m02l01) (lesson 2.1, module 2: Secrets And Identity) · Pro  
**Check:** Graded

## Goal

You can name the ordinary routes a secret takes out of a system, prove that deleting a committed file does not remove it, and stop a configuration object or a request logger from printing a live credential.

In the lesson: A filter fixes this in one place, which matters because you will never audit every call site. The filter object receives each record before it is formatted, renders the message, replaces anything matching the shape of a live key with a masked form, and clears the arguments so the record cannot be formatted twice. Run the filtered version. The harmless line is untouched, and the credential has shrunk to a marker ending in the last four characters. Two warnings come with this. A pattern only catches shapes you thought of, so agree a prefix convention your keys really follow. And a filter is a net, not permission to hand secrets to the logger.

## Files

- [`starter/log_fixed.py`](starter/log_fixed.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m02l01/m02l01-06/starter`
2. Read `log_fixed.py`.
3. Notes from the lesson:
   - Line 8: match the shape your provider issues; keep a tail for triage
   - Line 9: clearing the arguments stops the formatter expanding the original again
4. Run it: `python3 log_fixed.py`.
5. Check it from the repository root: `./check m02l01-06`.

## Expected output

```text
INFO GET /v1/charges?limit=10 -> 200
INFO POST /v1/webhooks?api_key=sk-live-demo -> 200
```

## How to check

`./check m02l01-06` copies `starter/` into a scratch directory and runs `python3 log_fixed.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/security-course/m02l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
