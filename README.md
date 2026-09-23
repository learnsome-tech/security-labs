<img src="https://learnsome.tech/logo.png" width="48" alt="LearnSome.tech">

# Application Security & Threat Modeling for Engineers

6 modules, 28 lessons: The Security Mindset; Secrets And Identity; Web Vulnerabilities; API Security; The Supply Chain; Scanning And The Pipeline.

## Watch and read

- **Course page**: [https://learnsome.tech/courses/security-course](https://learnsome.tech/courses/security-course)
- **Video player**: [https://learnsome.tech/courses/security-course/watch](https://learnsome.tech/courses/security-course/watch)
- **Handbook PDF**: [https://learnsome.tech/handbooks/security/book.pdf](https://learnsome.tech/handbooks/security/book.pdf)
- **On-site handbook**: [https://learnsome.tech/courses/security-course/book](https://learnsome.tech/courses/security-course/book)

## What is in this repository

This repository contains code artifacts, exercises and reference files for the lessons in this course.
28 lessons include a `labs/<lessonId>/` folder.
Each folder is named after the lesson identifier (e.g. `labs/m01l01/`) and contains the
artifact files shown in the course video, an `EXERCISES.md` with hands-on tasks, and
sub-directories named by artifact reference (e.g. `m01l01-02/`).

## Lessons

| # | Lesson | Watch | Labs | Handbook |
|---|--------|-------|------|----------|
| | **The Security Mindset** | | | |
| 1 | The Threat Model Habit | [▶](https://learnsome.tech/courses/security-course/watch?lesson=m01l01) | [labs/m01l01/](labs/m01l01/) | [§](https://learnsome.tech/courses/security-course/book#lesson-1-1) |
| 2 | Authentication Versus Authorisation | [▶](https://learnsome.tech/courses/security-course/watch?lesson=m01l02) | [labs/m01l02/](labs/m01l02/) | [§](https://learnsome.tech/courses/security-course/book#lesson-1-2) |
| 3 | Least Privilege In IAM And RBAC | [▶](https://learnsome.tech/courses/security-course/watch?lesson=m01l03) | [labs/m01l03/](labs/m01l03/) | [§](https://learnsome.tech/courses/security-course/book#lesson-1-3) |
| 4 | Secure Defaults | [▶](https://learnsome.tech/courses/security-course/watch?lesson=m01l04) | [labs/m01l04/](labs/m01l04/) | [§](https://learnsome.tech/courses/security-course/book#lesson-1-4) |
| | **Secrets And Identity** | | | |
| 5 | Why Secrets Leak | [▶](https://learnsome.tech/courses/security-course/watch?lesson=m02l01) | [labs/m02l01/](labs/m02l01/) | [§](https://learnsome.tech/courses/security-course/book#lesson-2-1) |
| 6 | The Environment Variable Trap | [▶](https://learnsome.tech/courses/security-course/watch?lesson=m02l02) | [labs/m02l02/](labs/m02l02/) | [§](https://learnsome.tech/courses/security-course/book#lesson-2-2) |
| 7 | Moving To A Secret Manager | [▶](https://learnsome.tech/courses/security-course/watch?lesson=m02l03) | [labs/m02l03/](labs/m02l03/) | [§](https://learnsome.tech/courses/security-course/book#lesson-2-3) |
| 8 | Workload Identity | [▶](https://learnsome.tech/courses/security-course/watch?lesson=m02l04) | [labs/m02l04/](labs/m02l04/) | [§](https://learnsome.tech/courses/security-course/book#lesson-2-4) |
| | **Web Vulnerabilities** | | | |
| 9 | Injection In All Its Forms | [▶](https://learnsome.tech/courses/security-course/watch?lesson=m03l01) | [labs/m03l01/](labs/m03l01/) | [§](https://learnsome.tech/courses/security-course/book#lesson-3-1) |
| 10 | SQL Injection: The Exploit | [▶](https://learnsome.tech/courses/security-course/watch?lesson=m03l02) | [labs/m03l02/](labs/m03l02/) | [§](https://learnsome.tech/courses/security-course/book#lesson-3-2) |
| 11 | SQL Injection: The Fix | [▶](https://learnsome.tech/courses/security-course/watch?lesson=m03l03) | [labs/m03l03/](labs/m03l03/) | [§](https://learnsome.tech/courses/security-course/book#lesson-3-3) |
| 12 | Cross-Site Scripting | [▶](https://learnsome.tech/courses/security-course/watch?lesson=m03l04) | [labs/m03l04/](labs/m03l04/) | [§](https://learnsome.tech/courses/security-course/book#lesson-3-4) |
| 13 | Cross-Site Request Forgery | [▶](https://learnsome.tech/courses/security-course/watch?lesson=m03l05) | [labs/m03l05/](labs/m03l05/) | [§](https://learnsome.tech/courses/security-course/book#lesson-3-5) |
| 14 | Server-Side Request Forgery | [▶](https://learnsome.tech/courses/security-course/watch?lesson=m03l06) | [labs/m03l06/](labs/m03l06/) | [§](https://learnsome.tech/courses/security-course/book#lesson-3-6) |
| | **API Security** | | | |
| 15 | TLS And The Handshake | [▶](https://learnsome.tech/courses/security-course/watch?lesson=m04l01) | [labs/m04l01/](labs/m04l01/) | [§](https://learnsome.tech/courses/security-course/book#lesson-4-1) |
| 16 | Broken Object Level Authorization | [▶](https://learnsome.tech/courses/security-course/watch?lesson=m04l02) | [labs/m04l02/](labs/m04l02/) | [§](https://learnsome.tech/courses/security-course/book#lesson-4-2) |
| 17 | Mass Assignment | [▶](https://learnsome.tech/courses/security-course/watch?lesson=m04l03) | [labs/m04l03/](labs/m04l03/) | [§](https://learnsome.tech/courses/security-course/book#lesson-4-3) |
| 18 | Rate Limiting And Resource Consumption | [▶](https://learnsome.tech/courses/security-course/watch?lesson=m04l04) | [labs/m04l04/](labs/m04l04/) | [§](https://learnsome.tech/courses/security-course/book#lesson-4-4) |
| | **The Supply Chain** | | | |
| 19 | Dependency Risk And Typosquatting | [▶](https://learnsome.tech/courses/security-course/watch?lesson=m05l01) | [labs/m05l01/](labs/m05l01/) | [§](https://learnsome.tech/courses/security-course/book#lesson-5-1) |
| 20 | Lockfiles And Reproducible Builds | [▶](https://learnsome.tech/courses/security-course/watch?lesson=m05l02) | [labs/m05l02/](labs/m05l02/) | [§](https://learnsome.tech/courses/security-course/book#lesson-5-2) |
| 21 | Software Bill Of Materials | [▶](https://learnsome.tech/courses/security-course/watch?lesson=m05l03) | [labs/m05l03/](labs/m05l03/) | [§](https://learnsome.tech/courses/security-course/book#lesson-5-3) |
| 22 | Provenance And Signing | [▶](https://learnsome.tech/courses/security-course/watch?lesson=m05l04) | [labs/m05l04/](labs/m05l04/) | [§](https://learnsome.tech/courses/security-course/book#lesson-5-4) |
| 23 | Container Security: Minimal Bases And Non Root | [▶](https://learnsome.tech/courses/security-course/watch?lesson=m05l05) | [labs/m05l05/](labs/m05l05/) | [§](https://learnsome.tech/courses/security-course/book#lesson-5-5) |
| | **Scanning And The Pipeline** | | | |
| 24 | Static Application Security Testing | [▶](https://learnsome.tech/courses/security-course/watch?lesson=m06l01) | [labs/m06l01/](labs/m06l01/) | [§](https://learnsome.tech/courses/security-course/book#lesson-6-1) |
| 25 | Dynamic Scanning | [▶](https://learnsome.tech/courses/security-course/watch?lesson=m06l02) | [labs/m06l02/](labs/m06l02/) | [§](https://learnsome.tech/courses/security-course/book#lesson-6-2) |
| 26 | Image Scanning And Trivy | [▶](https://learnsome.tech/courses/security-course/watch?lesson=m06l03) | [labs/m06l03/](labs/m06l03/) | [§](https://learnsome.tech/courses/security-course/book#lesson-6-3) |
| 27 | Secret Scanning | [▶](https://learnsome.tech/courses/security-course/watch?lesson=m06l04) | [labs/m06l04/](labs/m06l04/) | [§](https://learnsome.tech/courses/security-course/book#lesson-6-4) |
| 28 | How To Stop Drowning In Findings | [▶](https://learnsome.tech/courses/security-course/watch?lesson=m06l05) | [labs/m06l05/](labs/m06l05/) | [§](https://learnsome.tech/courses/security-course/book#lesson-6-5) |

## Exercises

Each lesson folder contains an `EXERCISES.md` with hands-on tasks drawn directly from the course material.
Open the file for a lesson to see the tasks and, where provided, hints.

---

© LearnSome.tech · support@iwantto.learnsome.tech
