# Retrospective

## What went well
- Ubuntu Server installed successfully in UTM.
- The VM booted correctly after removing the ISO.
- DHCP networking worked without needing manual configuration.
- SSH connectivity from the Mac to the VM worked.
- `sudo` worked both locally and over SSH.
- Creating a secondary admin user was straightforward.
- File permission changes with `chmod` behaved as expected.
- Cron was enabled and the test job successfully wrote timestamps to a log file.

## What was confusing
- The installer screen about removing installation media looked like an error at first.
- `sleep 65` looked like the terminal froze, but it was just waiting silently.
- The difference between `ls -1` and `ls -l` was easy to miss.
- The difference between `crontab -1` and `crontab -l` was easy to miss.
- SSH being installed but not running after setup was unexpected.

## What broke or caused friction
- SSH was initially installed but inactive.
- Cron commands were easy to mistype.
- Some commands were copied before fully understanding what each flag did.
- A few terminal typos caused command errors and slowed things down.

## How I fixed issues
- Enabled SSH manually with `sudo systemctl enable --now ssh`.
- Enabled cron manually with `sudo systemctl enable --now cron`.
- Corrected command typos and reran the commands.
- Removed the cron test job after verifying that it worked.
- Ejected the ISO so the VM would boot from the installed disk instead of the installer media.

## What I learned
- How to install Ubuntu Server in a VM on Apple Silicon.
- How to identify the current user, hostname, IP address, memory, and disk usage.
- How to manage Linux services with `systemctl`.
- How to create users and add them to the sudo group.
- How to change and verify file permissions with `chmod` and `ls -l`.
- How cron scheduling syntax works at a basic level.
- How to SSH from a Mac into a Linux server and run admin commands remotely.

## Next improvements
- Create a nontrivial cron job with clearer operational value.
- Practice switching users with `su - opsuser`.
- Test failed SSH login behavior and review logs.
- Add screenshots or sanitized terminal captures to the evidence folder.
- Document command meanings more consistently during future labs.
