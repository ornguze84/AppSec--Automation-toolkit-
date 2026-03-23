import json

def generate_report(alerts):
    findings = []

    for alert in alerts:
        findings.append({
            "name": alert.get("alert"),
            "risk": alert.get("risk"),
            "url": alert.get("url"),
            "description": alert.get("description")
        })

    with open("report.json", "w") as f:
        json.dump(findings, f, indent=4)

    print("[+] Report saved as report.json")
