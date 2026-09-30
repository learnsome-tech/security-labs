<p>
  <a href="https://learnsome.tech/courses/security-course">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset=".github/assets/wordmark-inverse.svg">
      <img src=".github/assets/wordmark.svg" alt="LearnSome.tech" width="260">
    </picture>
  </a>
</p>

# Application Security & Threat Modeling for Engineers

**OWASP Top 10, Cryptography, OAuth2 Pitfalls & Zero-Trust**

6 modules, 28 lessons: The Security Mindset; Secrets And Identity; Web Vulnerabilities; API Security; The Supply Chain; Scanning And The Pipeline. Advanced level, about 2 hours.

This repository holds the labs of the LearnSome.tech course [Application Security & Threat Modeling for Engineers](https://learnsome.tech/courses/security-course): each lab's starter files, a README with the goal, the steps and the expected output, and `./check`, which tests your work the way the site does.

## Start

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/learnsome-tech/security-labs?quickstart=1)

- **Codespaces:** the badge opens this repository in a dev container with Python 3.14.7 and Git 2.34 (Ubuntu 22.04's), as in the site's lab sandbox.
- **On your machine:**

  ```sh
  git clone https://github.com/learnsome-tech/security-labs.git
  cd security-labs
  ./check m01l01-03
  ```

  You need Python 3 for `./check`, and for the labs themselves Python 3.14.7 and Git 2.34 (Ubuntu 22.04's). Other versions mostly work, but only the sandbox's versions are sure to print what the site prints. VS Code's Dev Containers extension builds the same container as Codespaces (x86-64).

## Doing a lab

1. Open the lesson on LearnSome.tech and the lab folder beside it: `labs/<lesson>/<lab>/`. The lab README has the goal, the steps and the expected output.
2. Work in the lab's `starter/` folder.
3. From the repository root, run `./check <lab>` (for example `./check m01l01-03`), or `./check <lesson>` for all labs of a lesson, or `./check --all`. `./check --list` shows every lab and how it is checked.

`./check` runs your starter the way the site's lab sandbox does: in a scratch copy that is its working directory and `HOME`, with `LANG=C.UTF-8`, `TZ=UTC`, `input.txt` on standard input, 10 seconds and 256 KiB of output per stream. It then compares the output with the site's own rules, so a pass here is a pass on the site.

| Check | What `./check` does | Labs |
| --- | --- | --- |
| Graded | Runs the program and compares its output with `expected.txt`. | 83 |
| Read along | Nothing to run here: the site shows the listing read-only, and the lab README says honestly what it needs (Docker, a cluster, a cloud account...). | 31 |

## What is published, and what is not

Every lab's starter is the code the lesson shows on screen, which is also what the lab editor on the site opens with. Where that code is the whole program, such as a recorded shell session or a script from the video, it is published as it is: it is the lesson content. Nothing beyond the lesson is published. There are no reference solutions and no answers to the lesson exercises, and nothing the site keeps private.

Pro lessons' labs are here as starters too. LearnSome.tech runs and grades your labs in its sandbox, hosts the videos and keeps your progress; running and grading a Pro lab on the site needs Pro.

## Modules and lessons

### Module 1: The Security Mindset

| # | Lesson | Labs | Access |
| --- | --- | --- | --- |
| 1.1 | [The Threat Model Habit](https://learnsome.tech/learn/security-course/m01l01) | [3 labs](labs/m01l01/) | Free |
| 1.2 | [Authentication Versus Authorisation](https://learnsome.tech/learn/security-course/m01l02) | [5 labs](labs/m01l02/) | Free |
| 1.3 | [Least Privilege In IAM And RBAC](https://learnsome.tech/learn/security-course/m01l03) | [6 labs](labs/m01l03/) | Free |
| 1.4 | [Secure Defaults](https://learnsome.tech/learn/security-course/m01l04) | [4 labs](labs/m01l04/) | Free |

### Module 2: Secrets And Identity

| # | Lesson | Labs | Access |
| --- | --- | --- | --- |
| 2.1 | [Why Secrets Leak](https://learnsome.tech/learn/security-course/m02l01) | [5 labs](labs/m02l01/) | Pro |
| 2.2 | [The Environment Variable Trap](https://learnsome.tech/learn/security-course/m02l02) | [5 labs](labs/m02l02/) | Pro |
| 2.3 | [Moving To A Secret Manager](https://learnsome.tech/learn/security-course/m02l03) | [6 labs](labs/m02l03/) | Pro |
| 2.4 | [Workload Identity](https://learnsome.tech/learn/security-course/m02l04) | [4 labs](labs/m02l04/) | Pro |

### Module 3: Web Vulnerabilities

| # | Lesson | Labs | Access |
| --- | --- | --- | --- |
| 3.1 | [Injection In All Its Forms](https://learnsome.tech/learn/security-course/m03l01) | [4 labs](labs/m03l01/) | Pro |
| 3.2 | [SQL Injection: The Exploit](https://learnsome.tech/learn/security-course/m03l02) | [2 labs](labs/m03l02/) | Pro |
| 3.3 | [SQL Injection: The Fix](https://learnsome.tech/learn/security-course/m03l03) | [2 labs](labs/m03l03/) | Pro |
| 3.4 | [Cross-Site Scripting](https://learnsome.tech/learn/security-course/m03l04) | [2 labs](labs/m03l04/) | Pro |
| 3.5 | [Cross-Site Request Forgery](https://learnsome.tech/learn/security-course/m03l05) | [2 labs](labs/m03l05/) | Pro |
| 3.6 | [Server-Side Request Forgery](https://learnsome.tech/learn/security-course/m03l06) | [2 labs](labs/m03l06/) | Pro |

### Module 4: API Security

| # | Lesson | Labs | Access |
| --- | --- | --- | --- |
| 4.1 | [TLS And The Handshake](https://learnsome.tech/learn/security-course/m04l01) | [5 labs](labs/m04l01/) | Pro |
| 4.2 | [Broken Object Level Authorization](https://learnsome.tech/learn/security-course/m04l02) | [5 labs](labs/m04l02/) | Pro |
| 4.3 | [Mass Assignment](https://learnsome.tech/learn/security-course/m04l03) | [5 labs](labs/m04l03/) | Pro |
| 4.4 | [Rate Limiting And Resource Consumption](https://learnsome.tech/learn/security-course/m04l04) | [3 labs](labs/m04l04/) | Pro |

### Module 5: The Supply Chain

| # | Lesson | Labs | Access |
| --- | --- | --- | --- |
| 5.1 | [Dependency Risk And Typosquatting](https://learnsome.tech/learn/security-course/m05l01) | [5 labs](labs/m05l01/) | Pro |
| 5.2 | [Lockfiles And Reproducible Builds](https://learnsome.tech/learn/security-course/m05l02) | [5 labs](labs/m05l02/) | Pro |
| 5.3 | [Software Bill Of Materials](https://learnsome.tech/learn/security-course/m05l03) | [4 labs](labs/m05l03/) | Pro |
| 5.4 | [Provenance And Signing](https://learnsome.tech/learn/security-course/m05l04) | [5 labs](labs/m05l04/) | Pro |
| 5.5 | [Container Security: Minimal Bases And Non Root](https://learnsome.tech/learn/security-course/m05l05) | [5 labs](labs/m05l05/) | Pro |

### Module 6: Scanning And The Pipeline

| # | Lesson | Labs | Access |
| --- | --- | --- | --- |
| 6.1 | [Static Application Security Testing](https://learnsome.tech/learn/security-course/m06l01) | [5 labs](labs/m06l01/) | Pro |
| 6.2 | [Dynamic Scanning](https://learnsome.tech/learn/security-course/m06l02) | [4 labs](labs/m06l02/) | Pro |
| 6.3 | [Image Scanning And Trivy](https://learnsome.tech/learn/security-course/m06l03) | [3 labs](labs/m06l03/) | Pro |
| 6.4 | [Secret Scanning](https://learnsome.tech/learn/security-course/m06l04) | [4 labs](labs/m06l04/) | Pro |
| 6.5 | [How To Stop Drowning In Findings](https://learnsome.tech/learn/security-course/m06l05) | [4 labs](labs/m06l05/) | Pro |

**Free** lessons are open to anyone with a free LearnSome.tech account; **Pro** lessons need a Pro membership to watch, run and grade on the site.

## Licence

- **Code** (starter files, `check` and `.learnsome/`, the dev container and the workflows) is under the [MIT licence](LICENSE).
- **Written text** (the READMEs, lab instructions, lesson text, exercises and questions) is under [CC BY-NC-SA 4.0](LICENSE-text.md): share and adapt it with attribution to LearnSome.tech, not commercially, under the same licence.
- The LearnSome.tech name and logo are not covered by either licence.

## Contributing and security

This repository is generated from the course. Report a broken lab or a content error [as an issue](../../issues/new/choose); see [CONTRIBUTING.md](CONTRIBUTING.md). Security reports go to [SECURITY.md](SECURITY.md).

© 2026 LearnSome.tech
