from zap_client import ZAPScanner
from report import generate_report

TARGET = "http://testphp.vulnweb.com"

def main():
    zap = ZAPScanner()

    print("[+] Starting Spider Scan...")
    zap.spider(TARGET)

    print("[+] Starting Active Scan...")
    zap.active_scan(TARGET)

    print("[+] Fetching Alerts...")
    alerts = zap.get_alerts(TARGET)

    print(f"[+] Found {len(alerts)} vulnerabilities")

    generate_report(alerts)

if __name__ == "__main__":
    main()
