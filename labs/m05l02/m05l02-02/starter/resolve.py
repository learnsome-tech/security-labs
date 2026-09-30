import json

def number(text):
    return tuple(int(part) for part in text.split("."))

def resolve(low, high, versions):
    fits = [v for v in versions if number(low) <= number(v) < number(high)]
    return max(fits, key=number)

for snapshot in ("index-in-june.json", "index-in-july.json"):
    with open(snapshot) as handle:
        index = json.load(handle)
    print(snapshot, "gives httpx", resolve("2.0.0", "3.0.0", index["httpx"]))
print("one requirements line, two builds, two different programs")
