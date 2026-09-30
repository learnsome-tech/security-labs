# m02l01-05 · Exploit: the request logger that records everything

**Lesson:** [Why Secrets Leak](https://learnsome.tech/learn/security-course/m02l01) (lesson 2.1, module 2: Secrets And Identity) · Pro  
**Check:** Graded

## Goal

You can name the ordinary routes a secret takes out of a system, prove that deleting a committed file does not remove it, and stop a configuration object or a request logger from printing a live credential.

In the lesson: Logging deserves its own example, because it is the leak with the widest reach. A request logger writes the method, the path and the query string, which is a reasonable thing to want. Then one caller puts an application key in the query string, because an integration guide told them to, and your logger records it faithfully. Run it. The first line is harmless. The second line carries a live credential, and it is now duplicated across every retention tier you own. Think about who can read logs at your company. It is almost always far more people than can read the secret store, and that asymmetry is the whole problem.

## Files

- [`starter/log_vuln.py`](starter/log_vuln.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m02l01/m02l01-05/starter`
2. Read `log_vuln.py`.
3. Run it: `python3 log_vuln.py`.
4. Check it from the repository root: `./check m02l01-05`.

## Expected output

```text
INFO GET /v1/charges?limit=10 -> 200
INFO POST /v1/webhooks?api_key=sk-live-4d1f-demo -> 200
```

## How to check

`./check m02l01-05` copies `starter/` into a scratch directory and runs `python3 log_vuln.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/security-course/m02l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
