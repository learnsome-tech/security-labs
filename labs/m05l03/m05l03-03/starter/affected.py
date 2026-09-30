import json

ADVISORY = {"id": "PYSEC-2023-192", "package": "urllib3",
            "introduced": "1.26.0", "fixed": "1.26.17"}

def number(text):
    return tuple(int(part) for part in text.split("."))

for part in json.load(open("sbom.json"))["components"]:
    if part["name"] != ADVISORY["package"]:
        print("not affected:", part["purl"], "- other package")
        continue
    hit = number(ADVISORY["introduced"]) <= number(part["version"]) < \
        number(ADVISORY["fixed"])
    print("AFFECTED:" if hit else "not affected:", part["purl"])
print("a text compare would have said fixed:", "1.26.5" > "1.26.17")
