# m02l04-02 · Static credentials stay valid until somebody rotates them

**Lesson:** [Workload Identity](https://learnsome.tech/learn/security-course/m02l04) (lesson 2.4, module 2: Secrets And Identity) · Pro  
**Check:** Graded

## Goal

You can explain how workload identity replaces a stored cloud key, verify a short lived exchange for an allowed service, and reject a caller whose identity or audience is wrong.

In the lesson: Start with the thing we are trying to remove. The application stores a cloud key, and this demonstration prints only its fingerprint. Run the static credential demo. The key remains valid after a week and remains valid after a leak until somebody finds it and rotates it. That is the operational problem with a static credential: the application has to possess it, every copy becomes a response task, and the useful lifetime is usually much longer than the request that needed access. The next program models the platform issuing a narrower token instead.

## Files

- [`starter/static.py`](starter/static.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m02l04/m02l04-02/starter`
2. Read `static.py`.
3. Run it: `python3 static.py`.
4. Check it from the repository root: `./check m02l04-02`.

## Expected output

```text
application stores a key: True
key fingerprint: 3653f0e105fe
valid after a week: True
valid after a leak: True
```

## How to check

`./check m02l04-02` copies `starter/` into a scratch directory and runs `python3 static.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/security-course/m02l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
