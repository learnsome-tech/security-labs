import os
def report(request):
    raw = request.args.get('host')
    os.system('ping ' + raw)
def report_fixed(request):
    raw = request.args.get('host')
    safe = raw.replace(';', '')
    os.system('ping ' + safe)
