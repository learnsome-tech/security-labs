# Application Security & Threat Modeling for Engineers — lesson m06l01 — Static Application Security Testing
# https://learnsome.tech/courses/security-course/watch?lesson=m06l01
# © LearnSome.tech
# do not use eval(data) in new code
def score(data):
    return int(data['points']) + 1

def risky(payload):
    result = eval(
        payload['expr'])
    return result
