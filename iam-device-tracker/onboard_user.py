import csv
import json
from datetime import datetime

username = "asmith"
full_name = "Alice Smith"
department = "IT"
role = "analyst"
status = "active"
timestamp = datetime.now().isoformat()
audit_event = {
	"timestamp": timestamp,
	"action": "user_onboarded",
	"username": username,
	"status": "success"
}

with open("users.csv", "a", newline="") as file:
	writer = csv.writer(file)
	writer.writerow([username, full_name, department, role, status])
with open("audit_log.jsonl", "a") as file:
	file.write(json.dumps(audit_event) + "\n")
