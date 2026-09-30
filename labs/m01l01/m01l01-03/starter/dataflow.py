FLOWS = [
    ("browser", "web app", "card number", "internet"),
    ("web app", "payments API", "card number", "vendor"),
    ("web app", "database", "order", "same VPC"),
    ("web app", "log service", "card number", "vendor"),
]

for source, sink, data, network in FLOWS:
    crossing = network != "same VPC"
    edge = "CROSSES" if crossing else "internal"
    print(edge, source, "to", sink, "carrying", data)
    if crossing and data == "card number":
        print("  -> must be encrypted, minimised or not sent at all")
