# Application Security & Threat Modeling for Engineers — lesson m04l01 — TLS And The Handshake
# https://learnsome.tech/courses/security-course/watch?lesson=m04l01
# © LearnSome.tech
set -e
CA="-addext keyUsage=critical,keyCertSign,cRLSign"
openssl req -x509 -newkey rsa:2048 -nodes -keyout ca.key -out ca.pem \
  -subj "/CN=Course Root CA" -days 1 $CA >/dev/null 2>&1
openssl req -newkey rsa:2048 -nodes -keyout srv.key -out srv.csr \
  -subj "/CN=orders.internal" >/dev/null 2>&1
openssl x509 -req -in srv.csr -CA ca.pem -CAkey ca.key -days 1 \
  -extfile ext.cnf -out srv.pem >/dev/null 2>&1
echo "what the authority actually signed:"
openssl x509 -in srv.pem -noout -subject -issuer
openssl x509 -in srv.pem -noout -ext subjectAltName \
  | sed -n 's/^ *DNS:/valid for the name: /p'
echo "does the chain verify:"
openssl verify -CAfile ca.pem srv.pem
