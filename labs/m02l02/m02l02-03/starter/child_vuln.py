import os, subprocess, sys

os.environ["API_TOKEN"] = "sk-live-4d1f-demo"

PROBE = ("import os;"
         "print('child sees API_TOKEN:', os.environ.get('API_TOKEN'))")

print("the service holds the token")
subprocess.run([sys.executable, "-c", PROBE])
print("every helper it shells out to receives the same copy")
