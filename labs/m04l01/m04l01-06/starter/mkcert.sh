set -e
cat > ext.cnf <<'EOF'
subjectAltName = DNS:orders.internal
basicConstraints = CA:FALSE
EOF
openssl req -x509 -newkey rsa:2048 -nodes -keyout ca.key -out ca.pem \
  -subj "/CN=Course Root CA" -days 1 \
  -addext "keyUsage=critical,keyCertSign,cRLSign" >/dev/null 2>&1
openssl req -newkey rsa:2048 -nodes -keyout srv.key -out srv.csr \
  -subj "/CN=orders.internal" >/dev/null 2>&1
openssl x509 -req -in srv.csr -CA ca.pem -CAkey ca.key -days 1 \
  -extfile ext.cnf -out srv.pem >/dev/null 2>&1
