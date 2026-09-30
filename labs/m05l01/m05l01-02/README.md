# m05l01-02 · How wide is one dependency, really

**Lesson:** [Dependency Risk And Typosquatting](https://learnsome.tech/learn/security-course/m05l01) (lesson 5.1, module 5: The Supply Chain) · Pro  
**Check:** Graded

## Goal

You can describe the trust surface a single install command opens, detect a name that is one edit away from a package you meant, and name the four defences that shrink the surface without stopping delivery.

In the lesson: Here is a dependency graph shipped as data, so the numbers come from a real traversal rather than from a slide. One top level package, a breadth first walk over everything it pulls in, and a set of the maintainer accounts attached to every node we reach. Run the walk. One name in your requirements file became nine installed packages, four levels deep, with ten separate accounts able to publish a version you will accept tomorrow morning without noticing. That last number is the one to keep. It is not a count of libraries you trust. It is a count of people and their credentials, and compromising any single one of them is enough to reach your build.

## Files

- [`starter/closure.py`](starter/closure.py): the listing from the lesson
- [`starter/deps.json`](starter/deps.json)
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m05l01/m05l01-02/starter`
2. Read `closure.py`.
3. Notes from the lesson:
   - Line 13: every node reached contributes its publishers to one set
4. Run it: `python3 closure.py`.
5. Check it from the repository root: `./check m05l01-02`.

## Expected output

```text
you typed one install command for: report-cli
packages actually installed: 9
deepest transitive level: 4
accounts that can ship you code: 10
any one of those accounts is enough
```

## How to check

`./check m05l01-02` copies `starter/` into a scratch directory and runs `python3 closure.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/security-course/m05l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
