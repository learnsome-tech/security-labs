# Application Security & Threat Modeling for Engineers — lesson m05l05 — Container Security: Minimal Bases And Non Root
# https://learnsome.tech/courses/security-course/watch?lesson=m05l05
# © LearnSome.tech
trivy image --exit-code 1 --severity HIGH,CRITICAL registry.example/app:release
