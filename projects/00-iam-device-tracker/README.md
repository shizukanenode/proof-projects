# IAM Device Tracker

This project simulates a simple user onboarding and offboarding workflow with audit logging.

## Files
- `users.csv` - user records
- `devices.csv` - device assignment records
- `access_matrix.csv` - system access records
- `audit_log.jsonl` - audit events
- `least_privilege_policy.md` - basic access policy
- `onboard_user.py` - adds a new user record and logs the event
- `offboard_user.py` - disables a user record and logs the event

## Example Actions
- onboard a new user
- assign a device
- track access levels
- disable a user during offboarding
- record actions in an audit log
