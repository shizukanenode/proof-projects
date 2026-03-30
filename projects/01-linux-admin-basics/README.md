# 01 Linux Admin Basics

## Objective
Build and document a baseline Ubuntu Server VM and demonstrate core Linux administration skills.

## Environment
- Hypervisor: UTM
- Host machine: MacBook
- Guest OS: Ubuntu Server 24.04.4 LTS ARM64
- Hostname: `lab-srv01`
- Primary user: `nick`
- Secondary admin user: `opsuser`
- IP address: `192.168.64.2`

## Tasks Completed
- Installed Ubuntu Server in UTM
- Configured hostname and user account
- Verified network configuration with `ip a`
- Checked storage with `df -h`
- Checked memory with `free -h`
- Enabled and verified SSH
- Updated packages with `apt`
- Created a secondary user
- Added secondary user to the `sudo` group
- Created a test file and changed permissions with `chmod`
- Enabled and tested `cron`
- Connected remotely from Mac with SSH
- Verified `sudo` works over SSH

## Skills Demonstrated
- Linux server installation
- User and group management
- Service management with `systemctl`
- File permissions
- Package management
- Cron job basics
- Remote administration with SSH
- Basic system validation and troubleshooting

## Files in This Project
- `commands.md` - commands used and results
- `notes.md` - setup notes and observations
- `retrospective.md` - what worked, what was confusing, and what was learned
- `evidence/` - screenshots or terminal captures

## Key Takeaways
This lab established a working Linux server that can be administered locally and remotely. It also created a repeatable starting point for future networking, logging, and security projects.

## Next Improvements
- Add screenshots or sanitized terminal captures to `evidence/`
- Practice switching to `opsuser`
- Review SSH logs
- Add one more admin task such as package install/removal or log inspection
