from collections import Counter

failed_ips = []

with open("sample_logs/auth.log", "r") as file:
	for line in file:
		if "Failed password" in line:
			ip_address = line.split("from ")[1].split(" port")[0]
			failed_ips.append(ip_address)
ip_counts = Counter(failed_ips)
threshold = 3
suspicious_ips = [ip for ip, count in ip_counts.items() if count >= threshold]
print("Suspicious IPs:",  suspicious_ips)
