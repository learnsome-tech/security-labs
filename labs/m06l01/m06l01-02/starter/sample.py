# do not use eval(data) in new code
def score(data):
    return int(data['points']) + 1

def risky(payload):
    result = eval(
        payload['expr'])
    return result
