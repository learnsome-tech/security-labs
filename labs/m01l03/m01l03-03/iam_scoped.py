# Application Security & Threat Modeling for Engineers — lesson m01l03 — Least Privilege In IAM And RBAC
# https://learnsome.tech/courses/security-course/watch?lesson=m01l03
# © LearnSome.tech
from fnmatch import fnmatch

POLICY = [{"Effect": "Allow", "Action": ["s3:GetObject"],
           "Resource": ["arn:aws:s3:::reports/*"]}]
ASKS = [
    ("s3:GetObject", "arn:aws:s3:::reports/june.csv"),
    ("s3:DeleteBucket", "arn:aws:s3:::production-backups"),
    ("s3:PutBucketPolicy", "arn:aws:s3:::production-backups"),
]

def allowed(action, resource):
    for rule in POLICY:
        for pattern in rule["Action"]:
            for target in rule["Resource"]:
                if fnmatch(action, pattern) and fnmatch(resource, target):
                    return rule["Effect"] == "Allow"
    return False

for action, resource in ASKS:
    print("ALLOW" if allowed(action, resource) else "deny", action, resource)
