# m01l03 · Least Privilege In IAM And RBAC

Module 1: The Security Mindset · lesson 1.3 · Free · [Open the lesson](https://learnsome.tech/learn/security-course/m01l03)

**Goal:** You can read a cloud identity policy and a Kubernetes role for what they actually permit, name the permissions that let a principal grant itself more, and narrow both to the actions and resources a workload really uses.

## Labs

| Lab | What it is | Check |
| --- | --- | --- |
| [m01l03-02](m01l03-02/) | Exploit: what a wildcard policy actually grants | Graded |
| [m01l03-03](m01l03-03/) | Fix: name the action and name the resource | Graded |
| [m01l03-04](m01l03-04/) | The permissions that grant permissions | Graded |
| [m01l03-05](m01l03-05/) | A Kubernetes Role is the same idea, in YAML | Read along |
| [m01l03-06](m01l03-06/) | Exploit: the asterisk in a Kubernetes rule | Graded |
| [m01l03-07](m01l03-07/) | Fix: the verbs and resources the workload uses | Graded |

## Exercises

Open exercises from the lesson, to try on your own. They have no answer files: work them out, and use the labs above as reference.

### Narrow one real policy

1. Take one policy or role from your own infrastructure that contains an asterisk.
2. List the actions the workload really makes, from its logs or from its code.
3. Rewrite the policy naming only those actions and only the resources they touch.
4. Check separately whether anything in it can create, attach or pass identities.

> **Hint:** Cloud providers publish the calls each service makes; access logs are better evidence than memory.

## Check yourself

- Which two dimensions does a cloud policy narrow, and what does an asterisk in each one cost you?
- Why can a role with no storage permissions still delete a bucket?
- What does a Kubernetes Role permit before it is bound to a subject?
- Why is read access to secrets in a namespace treated as administrative?
- Why does starting wide and narrowing later rarely happen in practice?

---

[Course README](../../README.md) · [Application Security & Threat Modeling for Engineers on LearnSome.tech](https://learnsome.tech/courses/security-course)
