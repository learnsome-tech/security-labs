# Application Security & Threat Modeling for Engineers — lesson m03l05 — Cross-Site Request Forgery
# https://learnsome.tech/courses/security-course/watch?lesson=m03l05
# © LearnSome.tech
session='victim'
token='form-token'
request={'cookie':session,'token':None}
accepted = request['cookie']==session and request['token']==token
print('state change accepted:', accepted)
