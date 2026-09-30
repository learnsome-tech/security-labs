import json

bom = {"bomFormat": "CycloneDX", "specVersion": "1.5", "version": 1,
       "components": []}
for dep in json.load(open("components.json")):
    bom["components"].append({
        "type": "library",
        "name": dep["name"],
        "version": dep["version"],
        "purl": "pkg:pypi/" + dep["name"] + "@" + dep["version"],
        "licenses": [{"license": {"id": dep["license"]}}],
    })
with open("sbom.json", "w") as handle:
    json.dump(bom, handle, indent=2)
print(bom["bomFormat"], bom["specVersion"], "document written")
print("components recorded:", len(bom["components"]))
for part in bom["components"]:
    print(" ", part["purl"], part["licenses"][0]["license"]["id"])
