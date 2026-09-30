aws secretsmanager create-secret \
  --name billing/stripe-key \
  --secret-string sk-live-4d1f-demo

aws secretsmanager get-secret-value \
  --secret-id billing/stripe-key \
  --version-stage AWSCURRENT \
  --query SecretString --output text

aws secretsmanager rotate-secret \
  --secret-id billing/stripe-key \
  --rotation-rules AutomaticallyAfterDays=30
