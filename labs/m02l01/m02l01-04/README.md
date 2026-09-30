# m02l01-04 · Fix: a type that refuses to print itself

**Lesson:** [Why Secrets Leak](https://learnsome.tech/learn/security-course/m02l01) (lesson 2.1, module 2: Secrets And Identity) · Pro  
**Check:** Graded

## Goal

You can name the ordinary routes a secret takes out of a system, prove that deleting a committed file does not remove it, and stop a configuration object or a request logger from printing a live credential.

In the lesson: The fix is to give the secret a type of its own. A secret wrapper keeps the value in a private attribute and defines how it prints, returning only the last four characters, and the same method serves for text conversion so an interpolated string cannot expose it either. Reading the real value takes an explicit call named reveal, which is easy to search for in review. Run the fixed version. The context line still shows the host, which is what you wanted from a diagnostic, and the token has become a short marker. The final line proves the value is still there and still usable. None of the calling code had to change.

## Files

- [`starter/dump_fixed.py`](starter/dump_fixed.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m02l01/m02l01-04/starter`
2. Read `dump_fixed.py`.
3. Notes from the lesson:
   - Line 4: reading the real value needs a named call, which review can search for
   - Line 6: printing is a security decision, so let the type make it once
4. Run it: `python3 dump_fixed.py`.
5. Check it from the repository root: `./check m02l01-04`.

## Expected output

```text
request failed: upstream did not answer
context: {'host': 'api.example.com', 'token': Secret(ending demo)}
still usable: 17 characters
```

## How to check

`./check m02l01-04` copies `starter/` into a scratch directory and runs `python3 dump_fixed.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/security-course/m02l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
