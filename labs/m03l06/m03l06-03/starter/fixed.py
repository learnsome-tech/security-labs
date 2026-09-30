allowed={'public.example'}
for target in ['https://public.example/report','http://169.254.169.254/latest']:
 host=target.split('/')[2]
 print(target,'accepted:',host in allowed)
