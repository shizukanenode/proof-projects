# Commands Used

## Remote access
- `ssh nick@192.168.64.2`
  - Connected from the Mac to the Ubuntu VM over SSH.

## Host and SSH verification
- `hostname`
  - Confirmed the VM hostname was `lab-srv01`.

- `systemctl status ssh --no-pager`
  - Verified the SSH service was active.
  - `--no-pager` = print directly to the terminal instead of opening a pager like `less`.

## Package install and service startup
- `sudo apt update`
  - Refreshed the Ubuntu package list.
  - `sudo` = run command as administrator.

- `sudo apt install -y nginx`
  - Installed Nginx.
  - `-y` = automatically answer yes to prompts.

- `sudo systemctl enable --now nginx`
  - Enabled Nginx to start at boot and started it immediately.
  - `--now` = start the service right away in addition to enabling it.

- `systemctl is-active nginx`
  - Confirmed Nginx was running.

## Network verification on the VM
- `hostname -I`
  - Displayed the VM IP addresses.
  - `-I` = show all network addresses.

- `ss -tulpn | grep -E '(:22|:80)'`
  - Confirmed ports 22 and 80 were listening.
  - `-t` = TCP
  - `-u` = UDP
  - `-l` = listening sockets only
  - `-p` = show process
  - `-n` = numeric output
  - `grep -E` = use extended regular expressions

- `curl -I http://localhost`
  - Confirmed the web server responded locally.
  - `-I` = fetch headers only.

## Firewall check
- `sudo ufw status verbose`
  - Checked firewall state and detailed policy.
  - `verbose` = show extra details.

## Connectivity tests from the Mac
- `nc -zv 192.168.64.2 22`
  - Confirmed the Mac could reach SSH on port 22.
  - `-z` = scan without sending data
  - `-v` = verbose output

- `nc -zv 192.168.64.2 80`
  - Confirmed the Mac could reach HTTP on port 80.
  - `-z` = scan without sending data
  - `-v` = verbose output

- `curl -I http://192.168.64.2`
  - Confirmed Nginx responded across the network.
  - `-I` = fetch headers only.

## Service persistence and version
- `systemctl is-enabled nginx`
  - Confirmed Nginx is enabled to start at boot.

- `nginx -v`
  - Displayed installed Nginx version.
  - `-v` = version.
