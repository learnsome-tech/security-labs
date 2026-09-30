session='victim'
token='form-token'
request={'cookie':session,'token':None}
accepted = request['cookie']==session and request['token']==token
print('state change accepted:', accepted)
