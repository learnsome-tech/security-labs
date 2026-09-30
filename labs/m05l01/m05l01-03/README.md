# m05l01-03 · Install time: code runs before you run anything

**Lesson:** [Dependency Risk And Typosquatting](https://learnsome.tech/learn/security-course/m05l01) (lesson 5.1, module 5: The Supply Chain) · Pro  
**Check:** Graded

## Goal

You can describe the trust surface a single install command opens, detect a name that is one edit away from a package you meant, and name the four defences that shrink the surface without stopping delivery.

In the lesson: Installing is not copying files. A source distribution asks the packaging frontend to build it, and building means importing the backend the project declares and calling its hooks. On screen is such a backend. Beside it, shipped as a sibling file, is a frontend that does what a real installer does in principle. Watch what happens when we merely ask the package what its build requires. The hook prints, reads the environment and writes a file, and none of that needed your permission, because the build is already running as you, in your shell, with your tokens. Real attacks use exactly this step. Note the final line: something that was never part of the package is now sitting on your disk.

## Files

- [`starter/command.txt`](starter/command.txt)
- [`starter/hooks.py`](starter/hooks.py): the listing from the lesson
- [`starter/installer.py`](starter/installer.py)
- [`starter/pyproject.toml`](starter/pyproject.toml)
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m05l01/m05l01-03/starter`
2. Read `hooks.py`.
3. Notes from the lesson:
   - Line 7: a side effect on disk, from a hook nobody asked to run
4. Run it: `python3 installer.py`.
5. Check it from the repository root: `./check m05l01-03`.

## Expected output

```text
installer: the package declares a build backend
installer: asking the backend what it needs
  [hook] arbitrary code, before a single file is installed
  [hook] can i read the environment: True
  [hook] can i write to the disk: yes, see below
installer: asking the backend to build
installer: got friendly_utils-1.0.0-py3-none-any.whl
left behind by the build: True
```

## How to check

`./check m05l01-03` copies `starter/` into a scratch directory and runs `python3 installer.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/security-course/m05l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
