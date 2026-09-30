import logging, re

SECRET = re.compile(r"sk-live-[A-Za-z0-9-]+")

class Redact(logging.Filter):
    def filter(self, record):
        text = record.getMessage()
        record.msg = SECRET.sub(lambda m: "sk-live-" + m.group()[-4:], text)
        record.args = ()
        return True

logging.basicConfig(format="%(levelname)s %(message)s", level=logging.INFO)
log = logging.getLogger("access")
log.addFilter(Redact())

def handle(method, path, query):
    log.info("%s %s?%s -> 200", method, path, query)

handle("GET", "/v1/charges", "limit=10")
handle("POST", "/v1/webhooks", "api_key=sk-live-4d1f-demo")
