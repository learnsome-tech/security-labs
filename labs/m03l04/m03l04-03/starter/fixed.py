from html import escape
payload='<script>steal()</script>'
body='<p>'+escape(payload)+'</p>'
print('tag returned as markup:',payload in body)
print(body)
