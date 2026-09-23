# Application Security & Threat Modeling for Engineers — lesson m04l04 — Rate Limiting And Resource Consumption
# https://learnsome.tech/courses/security-course/watch?lesson=m04l04
# © LearnSome.tech
secret='hunter2'
limit=3
guesses=['123456','password','qwerty','letmein','hunter2']
codes=[]
for number, guess in enumerate(guesses, 1):
    if number > limit:
        codes.append(429)
        continue
    codes.append(200 if guess == secret else 401)
print('status codes:', codes)
print('checks performed:', limit)
print('password recovered:', 200 in codes)
