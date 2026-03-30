# 00 SOC Triage Lab

## Objective
Parse SSH authentication logs, identify suspicious failed login activity, and document the incident in a simple analyst-style workflow.

## Environment
- Project type: local Python and Markdown project
- Primary data source: `sample_logs/auth.log`
- Main script: `log_parser.py`

## Tasks Completed
- Reviewed a sample SSH authentication log
- Parsed failed login attempts by source IP
- Counted repeated failed logins
- Defined a simple threshold for suspicious activity
- Documented detection logic
- Wrote a short incident report

## Skills Demonstrated
- Log analysis
- Basic detection logic
- Security triage workflow
- Python scripting
- Security documentation

## Files in This Project
- `sample_logs/auth.log` - sample SSH authentication log
- `log_parser.py` - parses failed logins and counts suspicious IPs
- `detections.md` - notes on the detection rule
- `incident_report.md` - analyst-style writeup of findings

## Key Takeaways
This project shows a basic SOC-style workflow: review logs, apply a detection rule, identify suspicious activity, and document the result clearly.

## Next Improvements
- Add more sample log sources
- Expand the parser to support multiple event types
- Export results in CSV or JSON
- Add a small summary report script
