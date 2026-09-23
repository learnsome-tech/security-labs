# Application Security & Threat Modeling for Engineers — lesson m03l04 — Cross-Site Scripting
# https://learnsome.tech/courses/security-course/watch?lesson=m03l04
# © LearnSome.tech
from html import escape
payload='<script>steal()</script>'
body='<p>'+escape(payload)+'</p>'
print('tag returned as markup:',payload in body)
print(body)
