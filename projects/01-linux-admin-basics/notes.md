# Notes

- Built first Ubuntu Server VM in UTM on Apple Silicon.
- Used Ubuntu Server 24.04.4 LTS ARM64.
- Left network on DHCP during install.
- Skipped proxy and Ubuntu Pro.
- Installed OpenSSH server during setup.
- Did not install featured snaps.
- Had to eject the ISO after install so the VM would boot from disk.
- SSH was installed but not active until manually enabled with:
  `sudo systemctl enable --now ssh`
- Cron worked after enabling it with:
  `sudo systemctl enable --now cron`
- Confirmed remote administration from Mac using SSH.
- Created secondary admin practice account: `opsuser`.
- Practiced file permission changes with `chmod 644` and `chmod 600`.
