# m03l01-07 · The same three inputs, defended

**Lesson:** [Injection In All Its Forms](https://learnsome.tech/learn/security-course/m03l01) (lesson 3.1, module 3: Web Vulnerabilities) · Pro  
**Check:** Graded

## Goal

You can recognise injection as one bug in many interpreters, name the interpreter a piece of code is talking to, and choose the strongest defence available: parameters first, an allowlist where the grammar has no parameters, and escaping only as a last resort.

In the lesson: Now the same three inputs against defended code. The owner now travels as a bound parameter, marked in the query by a single question mark. The sort column has no parameter slot in the language, so it is checked against a small set of names the program itself owns. The command runs through an argument vector with no shell at all. Run the defended version. The normal lookup still works. The tautology returns an empty list, because the database went looking for a user literally named bob quote or one equals one, and no such person exists. The hostile column name is refused by name. The command sees one strange file name and reports it, rather than running a second command. Nothing was filtered and nothing was stripped.

## Files

- [`starter/defended.py`](starter/defended.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m03l01/m03l01-07/starter`
2. Read `defended.py`.
3. Notes from the lesson:
   - Line 10: the sort column is checked against a fixed set, never concatenated blind
   - Line 13: the owner arrives on a second channel and is only ever a value
4. Run it: `python3 defended.py`.
5. Check it from the repository root: `./check m03l01-07`.

## Expected output

```text
normal: ['lunch']
attack: []
bad order: rejected order column: body; DROP TABLE doc
no shell: No such file or directory
```

## How to check

`./check m03l01-07` copies `starter/` into a scratch directory and runs `python3 defended.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/security-course/m03l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
