from fnmatch import fnmatch

POLICY = [{"Action": ["iam:*"], "Resource": ["*"]}]

def allowed(action):
    return any(fnmatch(action, p) for rule in POLICY for p in rule["Action"])

print("can the build role delete a bucket:", allowed("s3:DeleteBucket"))
print("can it attach a policy to itself:", allowed("iam:AttachRolePolicy"))
if allowed("iam:AttachRolePolicy"):
    POLICY.append({"Action": ["*"], "Resource": ["*"]})
    print("it attached AdministratorAccess to itself")
print("can it delete a bucket now:", allowed("s3:DeleteBucket"))
