# m03l01-02 · Injection one: the database

**Lesson:** [Injection In All Its Forms](https://learnsome.tech/learn/security-course/m03l01) (lesson 3.1, module 3: Web Vulnerabilities) · Pro  
**Check:** Graded

## Goal

You can recognise injection as one bug in many interpreters, name the interpreter a piece of code is talking to, and choose the strongest defence available: parameters first, an allowlist where the grammar has no parameters, and escaping only as a last resort.

In the lesson: Start with the database, because it is the classic. This program builds a tiny table of documents in memory and one lookup function. The function assembles its query by gluing the owner name into the middle of a string, between two single quote characters. Printing the assembled query is the trick of this lesson: you see exactly what the database was asked to do. Run it. The first call passes the name bob and gets back his lunch note, which is the case everybody tests. The second call passes a name containing a quote character, the word or, and a comparison that is always true. Look at the second printed query. The quotation closed early, the condition became a permanent yes, and every row came back.

## Files

- [`starter/concat_sql.py`](starter/concat_sql.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m03l01/m03l01-02/starter`
2. Read `concat_sql.py`.
3. Notes from the lesson:
   - Line 9: the caller's text is glued between two quote characters
4. Run it: `python3 concat_sql.py`.
5. Check it from the repository root: `./check m03l01-02`.

## Expected output

```text
sql: SELECT body FROM doc WHERE owner = 'bob'
normal: ['lunch']
sql: SELECT body FROM doc WHERE owner = 'bob' OR '1'='1'
attack: ['budget', 'lunch']
```

## How to check

`./check m03l01-02` copies `starter/` into a scratch directory and runs `python3 concat_sql.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/security-course/m03l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
