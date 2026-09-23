# Application Security & Threat Modeling for Engineers — lesson m04l04 — Rate Limiting And Resource Consumption
# https://learnsome.tech/courses/security-course/watch?lesson=m04l04
# © LearnSome.tech
secret='hunter2'
guesses=['123456','password','qwerty','letmein','dragon','monkey','hunter2']
answered=0
for guess in guesses:
    answered += 1
    if guess == secret:
        break
print('requests answered:', answered)
print('password recovered:', guess)
print('limit enforced:', False)
