kubectl create role order-reader \
  --verb=get --verb=list \
  --resource=pods \
  --dry-run=client -o yaml
