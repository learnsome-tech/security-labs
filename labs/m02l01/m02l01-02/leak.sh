# Application Security & Threat Modeling for Engineers — lesson m02l01 — Why Secrets Leak
# https://learnsome.tech/courses/security-course/watch?lesson=m02l01
# © LearnSome.tech
set -e
export GIT_CONFIG_GLOBAL=/dev/null
g() { git -c user.email=course@example.com -c user.name=course "$@"; }
g init -q vault && cd vault
echo 'API_TOKEN=sk-live-4d1f-demo' > config.env
g add config.env && g commit -q -m "add config"
g rm -q config.env && g commit -q -m "remove the secret"
echo "files tracked at head: $(g ls-files | wc -l | tr -d ' ')"
echo "asking git for the file one commit back:"
g show HEAD~1:config.env
echo "a delete is another commit, not an erase"
