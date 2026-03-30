# Lab 2 - Network Services

## Objective
Verify remote access and deploy a basic web service on the Ubuntu VM.

## Environment
- Host machine: macOS
- VM: Ubuntu Server
- Hostname: lab-srv01
- VM IP: 192.168.64.2

## Tasks Completed
- Verified SSH was active on the VM
- Installed Nginx
- Enabled Nginx to start at boot
- Confirmed SSH was listening on port 22
- Confirmed Nginx was listening on port 80
- Confirmed local HTTP response on the VM
- Confirmed remote network connectivity from the Mac to ports 22 and 80
- Confirmed HTTP response from the Mac to the VM
- Checked Ubuntu firewall status

## Results
- SSH status: active
- Nginx status: active
- Nginx boot status: enabled
- Nginx version: 1.24.0 (Ubuntu)
- Firewall status: inactive
- HTTP result: 200 OK

## Evidence
- Terminal transcript: `evidence/terminal-session-lab02.txt`
- Screenshots: `evidence/screenshots/`
