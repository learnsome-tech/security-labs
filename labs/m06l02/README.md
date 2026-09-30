# m06l02 · Dynamic Scanning

Module 6: Scanning And The Pipeline · lesson 6.2 · Pro · [Open the lesson](https://learnsome.tech/learn/security-course/m06l02)

**Goal:** You can use a running service as a test target, demonstrate a reflected injection and an unauthorised state change, and turn those probes into a repeatable dynamic scan against the fixed service.

## Labs

| Lab | What it is | Check |
| --- | --- | --- |
| [m06l02-02](m06l02-02/) | A reflected payload proves a live path is unsafe | Read along |
| [m06l02-03](m06l02-03/) | Probe a state change without credentials | Read along |
| [m06l02-04](m06l02-04/) | The same probes pass against the fixed service | Read along |
| [m06l02-05](m06l02-05/) | Check headers as well as application content | Read along |

## Exercises

Open exercises from the lesson, to try on your own. They have no answer files: work them out, and use the labs above as reference.

### Turn one attack into a regression probe

1. Choose one endpoint in a disposable test deployment.
2. Write a request that demonstrates the unsafe response or state change.
3. Fix the service and make the same assertion pass.
4. Run the probe after every deployment and keep its result.

> **Hint:** The best probe names the request, the expected response, and the state that must not change.

## Check yourself

- What does a dynamic scan observe that static analysis cannot prove?
- Why should a scanner check state after a successful response?
- What makes a dynamic target safe to attack repeatedly?
- Why keep the request and response with the build result?
- How does a regression probe differ from a one time security demo?

---

[Course README](../../README.md) · [Application Security & Threat Modeling for Engineers on LearnSome.tech](https://learnsome.tech/courses/security-course)
