# m03l01-03 · Injection two: the command shell

**Lesson:** [Injection In All Its Forms](https://learnsome.tech/learn/security-course/m03l01) (lesson 3.1, module 3: Web Vulnerabilities) · Pro  
**Check:** Graded

## Goal

You can recognise injection as one bug in many interpreters, name the interpreter a piece of code is talking to, and choose the strongest defence available: parameters first, an allowlist where the grammar has no parameters, and escaping only as a last resort.

In the lesson: Same shape, different interpreter. Here the program shows a file by building a command line and handing it to a shell. A shell parses that string before anything runs, and the semicolon is a statement separator in that grammar, exactly as it is in many others. Run the second program. A plain file name behaves. A file name that carries a semicolon and a second command runs both, and the output of the attacker's command is printed by your own service. Notice there is no clever encoding here and no memory corruption. The attacker supplied punctuation that meant something to the parser, and the parser did its job faithfully. Web forms, file names from uploads and fields out of a queue all reach this code the same way.

## Files

- [`starter/concat_shell.py`](starter/concat_shell.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m03l01/m03l01-03/starter`
2. Read `concat_shell.py`.
3. Notes from the lesson:
   - Line 9: shell equals true asks a shell to parse the string first
4. Run it: `python3 concat_shell.py`.
5. Check it from the repository root: `./check m03l01-03`.

## Expected output

```text
shell: cat report.txt
normal: quarterly numbers
shell: cat report.txt; echo I-am-running-as-you
attack: quarterly numbers and then I-am-running-as-you
```

## How to check

`./check m03l01-03` copies `starter/` into a scratch directory and runs `python3 concat_shell.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/security-course/m03l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
