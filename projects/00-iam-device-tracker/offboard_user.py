import csv
import json
from datetime import datetime

username_to_disable = "jdoe"
timestamp = datetime.now().isoformat()
updated_rows = []

audit_event = {
	"timestamp": timestamp,
	"action": "user_offboarded",
	"username": username_to_disable,
	"status": "success"
}

with open("users.csv", "r", newline="") as file:
	reader = csv.DictReader(file)
	for row in reader:
		if row["username"] == username_to_disable:
			row["status"] = "disabled"
		updated_rows.append(row)

with open("users.csv", "w", newline="") as file:
	writer = csv.DictWriter(file, fieldnames=["username", "full_name", "department", "role", "status"])
	writer.writeheader()
	writer.writerows(updated_rows)

with open("audit_log.jsonl", "a") as file:
	file.write(json.dumps(audit_event) + "\n")
