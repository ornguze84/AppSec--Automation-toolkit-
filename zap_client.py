from zapv2 import ZAPv2
import time

API_KEY = 'changeme'
ZAP_PROXY = 'http://127.0.0.1:8080'

class ZAPScanner:
    def __init__(self):
        self.zap = ZAPv2(apikey=API_KEY, proxies={'http': ZAP_PROXY, 'https': ZAP_PROXY})

    def spider(self, target):
        scan_id = self.zap.spider.scan(target)
        while int(self.zap.spider.status(scan_id)) < 100:
            print(f"Spider progress: {self.zap.spider.status(scan_id)}%")
            time.sleep(2)

    def active_scan(self, target):
        scan_id = self.zap.ascan.scan(target)
        while int(self.zap.ascan.status(scan_id)) < 100:
            print(f"Active scan progress: {self.zap.ascan.status(scan_id)}%")
            time.sleep(5)

    def get_alerts(self, target):
        return self.zap.core.alerts(baseurl=target)
