# m05l03-02 · Generating one, in the shape a tool would

**Lesson:** [Software Bill Of Materials](https://learnsome.tech/learn/security-course/m05l03) (lesson 5.3, module 5: The Supply Chain) · Pro  
**Check:** Graded

## Goal

You can generate a machine readable bill of materials for a build, answer whether a new advisory affects you by querying it with a correct version comparison, and say what such a document does not cover.

In the lesson: The format is less interesting than the fields, so here is a generator that emits the shape a real tool emits. A header naming the specification, then one entry per component with a type, a name, a version, a licence, and a package URL. A package URL is the field that makes the document queryable: it encodes the ecosystem, the name and the version in one string that an advisory database can match without guessing. Run the generator. Four components, each with an identifier a machine can compare. Note what we did not do: we did not write this by hand, and we did not write it afterwards. It came out of the same data the build resolved.

## Files

- [`starter/components.json`](starter/components.json)
- [`starter/sbom.py`](starter/sbom.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m05l03/m05l03-02/starter`
2. Read `sbom.py`.
3. Notes from the lesson:
   - Line 10: the package url: ecosystem, name and version in one string
4. Run it: `python3 sbom.py`.
5. Check it from the repository root: `./check m05l03-02`.

## Expected output

```text
CycloneDX 1.5 document written
components recorded: 4
  pkg:pypi/requests@2.32.3 Apache-2.0
  pkg:pypi/urllib3@1.26.5 MIT
  pkg:pypi/urllib3@2.2.3 MIT
  pkg:pypi/jinja2@3.1.4 BSD-3-Clause
```

## How to check

`./check m05l03-02` copies `starter/` into a scratch directory and runs `python3 sbom.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/security-course/m05l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
