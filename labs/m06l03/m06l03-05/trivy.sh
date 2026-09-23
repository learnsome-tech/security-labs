# Application Security & Threat Modeling for Engineers — lesson m06l03 — Image Scanning And Trivy
# https://learnsome.tech/courses/security-course/watch?lesson=m06l03
# © LearnSome.tech
trivy image --exit-code 1 --severity HIGH,CRITICAL \
  registry.example/app@sha256:deadbeef
