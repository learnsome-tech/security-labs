# Application Security & Threat Modeling for Engineers — lesson m03l06 — Server-Side Request Forgery
# https://learnsome.tech/courses/security-course/watch?lesson=m03l06
# © LearnSome.tech
allowed={'public.example'}
for target in ['https://public.example/report','http://169.254.169.254/latest']:
 host=target.split('/')[2]
 print(target,'accepted:',host in allowed)
