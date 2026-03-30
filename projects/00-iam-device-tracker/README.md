# 00 IAM Device Tracker

## Objective
Simulate a basic IAM onboarding and offboarding workflow, including user records, device assignment, access tracking, and audit logging.

## Environment
- Project type: local Python and CSV-based workflow
- Main scripts: `onboard_user.py`, `offboard_user.py`
- Data files: CSV and JSONL

## Tasks Completed
- Created a simple user onboarding workflow
- Recorded device assignments
- Tracked user access levels
- Simulated user offboarding
- Logged actions to an audit file

## Skills Demonstrated
- IAM workflow basics
- User lifecycle management
- Asset and access tracking
- Audit logging
- Python scripting
- Security documentation

## Files in This Project
- `users.csv` - user records
- `devices.csv` - device assignment records
- `access_matrix.csv` - system access records
- `audit_log.jsonl` - audit events
- `least_privilege_policy.md` - basic access policy
- `onboard_user.py` - adds a new user record and logs the event
- `offboard_user.py` - disables a user record and logs the event

## Key Takeaways
This project demonstrates a simple IAM process: create accounts, assign devices and access, remove access during offboarding, and keep an audit trail of changes.

## Next Improvements
- Add role-based access control examples
- Validate duplicate users and device conflicts
- Export summary reports
- Add manager approval or ticket references
