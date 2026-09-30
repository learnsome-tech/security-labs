# m05l03-03 · Answering are we affected, properly

**Lesson:** [Software Bill Of Materials](https://learnsome.tech/learn/security-course/m05l03) (lesson 5.3, module 5: The Supply Chain) · Pro  
**Check:** Graded

## Goal

You can generate a machine readable bill of materials for a build, answer whether a new advisory affects you by querying it with a correct version comparison, and say what such a document does not cover.

In the lesson: Now the payoff. An advisory names a package and a half open range: introduced in one version, fixed in another. We walk the document and compare. Run the query. One component of the two that share a name is inside the range and is reported, the other is above the fix and is not, and the packages with other names are dismissed. The last line is the trap worth remembering: compared as text rather than as numbers, one point twenty six point five looks greater than one point twenty six point seventeen, so a naive check would have told you that you were already fixed. Version comparison is per ecosystem and it is not string ordering.

## Files

- [`starter/affected.py`](starter/affected.py): the listing from the lesson
- [`starter/sbom.json`](starter/sbom.json)
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m05l03/m05l03-03/starter`
2. Read `affected.py`.
3. Notes from the lesson:
   - Line 13: introduced in, fixed in: a half open range, compared as numbers
4. Run it: `python3 affected.py`.
5. Check it from the repository root: `./check m05l03-03`.

## Expected output

```text
not affected: pkg:pypi/requests@2.32.3 - other package
AFFECTED: pkg:pypi/urllib3@1.26.5
not affected: pkg:pypi/urllib3@2.2.3
not affected: pkg:pypi/jinja2@3.1.4 - other package
a text compare would have said fixed: True
```

## How to check

`./check m05l03-03` copies `starter/` into a scratch directory and runs `python3 affected.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/security-course/m05l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
