import socket
from datetime import datetime

print("=" * 50)
print("BASIC VULNERABILITY SCANNER")
print("=" * 50)

target = input("Enter target IP (Example: 127.0.0.1): ")

ports = {
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    443: "HTTPS"
}

open_ports = []

print("\nScanning...\n")

for port, service in ports.items():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)

    result = sock.connect_ex((target, port))

    if result == 0:
        print(f"[OPEN] Port {port} - {service}")
        open_ports.append((port, service))

    sock.close()

with open("report.txt", "w") as report:
    report.write("VULNERABILITY SCAN REPORT\n")
    report.write("=" * 30 + "\n")
    report.write(f"Target: {target}\n")
    report.write(f"Date: {datetime.now()}\n\n")

    if open_ports:
        report.write("OPEN PORTS:\n")

        for port, service in open_ports:
            report.write(f"\nPort {port} - {service}\n")

            if port == 23:
                report.write("Risk: Telnet is insecure.\n")

            elif port == 21:
                report.write("Risk: FTP may transmit data in plain text.\n")

            elif port == 80:
                report.write("Risk: HTTP traffic is not encrypted.\n")

    else:
        report.write("No open ports found.\n")

print("\nScan Complete!")
print("Report saved as report.txt")
