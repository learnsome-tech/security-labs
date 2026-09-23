# Application Security & Threat Modeling for Engineers — lesson m06l01 — Static Application Security Testing
# https://learnsome.tech/courses/security-course/watch?lesson=m06l01
# © LearnSome.tech
import os
def report(request):
    raw = request.args.get('host')
    os.system('ping ' + raw)
def report_fixed(request):
    raw = request.args.get('host')
    safe = raw.replace(';', '')
    os.system('ping ' + safe)
