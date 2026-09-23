# Application Security & Threat Modeling for Engineers — lesson m06l01 — Static Application Security Testing
# https://learnsome.tech/courses/security-course/watch?lesson=m06l01
# © LearnSome.tech
import subprocess
def report_fixed(request):
    raw = request.args.get('host')
    allowed = {'example.org', 'localhost'}
    if raw not in allowed:
        return 'rejected'
    return subprocess.run(['ping', '-c', '1', raw], check=True, shell=False)
