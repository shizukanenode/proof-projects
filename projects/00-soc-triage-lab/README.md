# SOC Triage Lab

This project parses a sample SSH authentication log, counts failed login attempts by IP address, and flags suspicious IPs that meet a defined threshold.

## Files
- `sample_logs/auth.log` - sample SSH authentication log
- `log_parser.py` - Python script that extracts and counts failed-login IP addresses
- `detections.md` - detection rule notes
- `incident_report.md` - short analyst-style incident report

## Detection Rule
Flag any IP address with 3 or more failed SSH login attempts as suspicious.
