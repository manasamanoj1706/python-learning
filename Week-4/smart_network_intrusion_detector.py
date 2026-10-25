
import random
from datetime import datetime

class NetworkPacket:
    def __init__(self, source_ip, port, data_size, login_attempts):
        self.source_ip = source_ip
        self.port = port
        self.data_size = data_size
        self.login_attempts = login_attempts


class IntrusionDetector:
    def __init__(self):
        self.safe_ports = {80, 443, 22, 53}
        self.alerts = []

    def analyze_packet(self, packet):
        issues = []

        if packet.login_attempts > 5:
            issues.append("Excessive login attempts")

        if packet.data_size > 5000:
            issues.append("Unusually large data transfer")

        if packet.port not in self.safe_ports:
            issues.append("Unexpected port")

        if issues:
            self.alerts.append((packet.source_ip, issues))
            return "SUSPICIOUS", issues

        return "NORMAL", []

    def show_report(self, packets):
        print("\n" + "=" * 60)
        print("       SMART NETWORK INTRUSION DETECTOR")
        print("=" * 60)
        print("Scan time:", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

        for packet in packets:
            status, issues = self.analyze_packet(packet)

            print(f"\nSource IP : {packet.source_ip}")
            print(f"Port      : {packet.port}")
            print(f"Data size : {packet.data_size} KB")
            print(f"Logins    : {packet.login_attempts}")
            print(f"Status    : {status}")

            for issue in issues:
                print("  ALERT:", issue)

        print("\n" + "-" * 60)
        print("Packets analyzed :", len(packets))
        print("Suspicious packets:", len(self.alerts))
        print("-" * 60)


def generate_demo_traffic(count=12):
    packets = []

    for i in range(count):
        packets.append(
            NetworkPacket(
                source_ip=f"192.168.1.{random.randint(2, 254)}",
                port=random.choice([22, 53, 80, 443, 8080, 9999]),
                data_size=random.randint(100, 10000),
                login_attempts=random.randint(0, 10)
            )
        )

    return packets


def main():
    detector = IntrusionDetector()
    traffic = generate_demo_traffic()
    detector.show_report(traffic)

    print("\nNote: This project uses simulated traffic only.")
    print("It does not monitor real network connections.")


if __name__ == "__main__":
    main()
