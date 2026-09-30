# m02l01-03 · Exploit: the helpful exception handler

**Lesson:** [Why Secrets Leak](https://learnsome.tech/learn/security-course/m02l01) (lesson 2.1, module 2: Secrets And Identity) · Pro  
**Check:** Graded

## Goal

You can name the ordinary routes a secret takes out of a system, prove that deleting a committed file does not remove it, and stop a configuration object or a request logger from printing a live credential.

In the lesson: Now an exception handler, written by somebody being helpful. When the upstream call times out, the handler prints the error and then prints the context, so whoever reads the log can see what the client was configured with. The configuration object holds the host and the token together, because that is how configuration objects are built. Run the exploit and read the second line. The token is now in the log file, in the log shipper, in the search index, and in whatever dashboard the team keeps open. Nothing was attacked. One helpful line of code did all of the work, and it will do it again on the next timeout.

## Files

- [`starter/dump_vuln.py`](starter/dump_vuln.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m02l01/m02l01-03/starter`
2. Read `dump_vuln.py`.
3. Notes from the lesson:
   - Line 12: dumping the whole object is how a secret reaches a log search index
4. Run it: `python3 dump_vuln.py`.
5. Check it from the repository root: `./check m02l01-03`.

## Expected output

```text
request failed: upstream did not answer
context: {'host': 'api.example.com', 'token': 'sk-live-4d1f-demo'}
```

## How to check

`./check m02l01-03` copies `starter/` into a scratch directory and runs `python3 dump_vuln.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/security-course/m02l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
