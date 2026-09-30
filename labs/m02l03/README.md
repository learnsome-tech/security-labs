# m02l03 · Moving To A Secret Manager

Module 2: Secrets And Identity · lesson 2.3 · Pro · [Open the lesson](https://learnsome.tech/learn/security-course/m02l03)

**Goal:** You can name the five properties a secret manager adds over an environment variable, and build or drive one that enforces a per caller policy, records every read, versions values for rotation, and hands out short leases.

## Labs

| Lab | What it is | Check |
| --- | --- | --- |
| [m02l03-02](m02l03-02/) | The lease: a borrowed credential with an end date | Read along |
| [m02l03-03](m02l03-03/) | The manager: policy, versions and an audit list | Read along |
| [m02l03-04](m02l03-04/) | An authorised read, a refusal, and the audit trail | Graded |
| [m02l03-05](m02l03-05/) | Rotation: version two becomes current | Graded |
| [m02l03-06](m02l03-06/) | Leases: cache, refetch, and refuse an expired one | Graded |
| [m02l03-07](m02l03-07/) | The same shape, in a hosted manager | Read along |

## Exercises

Open exercises from the lesson, to try on your own. They have no answer files: work them out, and use the labs above as reference.

### Move one credential

1. Pick one credential and write down, by name, which callers should be able to read it.
2. Ask your manager who read it last month; if it cannot answer, that is the finding.
3. Turn one long lived value into a versioned one and rotate it without a redeploy.
4. Make one client cache a lease and refetch on expiry, rather than reading once at start up.

> **Hint:** A client that reads its secret once at start up can never benefit from rotation.

## Check yourself

- Which five properties does a manager add that an environment variable cannot provide?
- Why does the manager record a denied read as well as a granted one?
- What has to change in a client before rotation actually protects anything?
- Why does a lease print its version rather than its value?
- After rotation, what makes the previous version stop working?

---

[Course README](../../README.md) · [Application Security & Threat Modeling for Engineers on LearnSome.tech](https://learnsome.tech/courses/security-course)
