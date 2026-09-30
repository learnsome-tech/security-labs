import subprocess
def report_fixed(request):
    raw = request.args.get('host')
    allowed = {'example.org', 'localhost'}
    if raw not in allowed:
        return 'rejected'
    return subprocess.run(['ping', '-c', '1', raw], check=True, shell=False)
