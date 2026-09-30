import logging

logging.basicConfig(format="%(levelname)s %(message)s", level=logging.INFO)
log = logging.getLogger("access")

def handle(method, path, query):
    log.info("%s %s?%s -> 200", method, path, query)

handle("GET", "/v1/charges", "limit=10")
handle("POST", "/v1/webhooks", "api_key=sk-live-4d1f-demo")
