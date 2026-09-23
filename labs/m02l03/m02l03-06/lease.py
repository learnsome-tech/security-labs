# Application Security & Threat Modeling for Engineers — lesson m02l03 — Moving To A Secret Manager
# https://learnsome.tech/courses/security-course/watch?lesson=m02l03
# © LearnSome.tech
import time

class Expired(Exception): pass

class Lease:
    def __init__(self, value, version, expires_at):
        self._value = value
        self.version = version
        self.expires_at = expires_at

    def valid(self):
        return time.time() < self.expires_at

    def reveal(self):
        if not self.valid():
            raise Expired("lease on version " + str(self.version) + " ended")
        return self._value

    def __repr__(self):
        return "Lease(version " + str(self.version) + ")"
