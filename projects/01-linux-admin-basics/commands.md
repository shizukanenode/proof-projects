# Commands Used

## Identity and Host Checks

whoami
-Current user: nick
hostname
-Hostname: lab-srv01

## Network Check

ip a
-Main interface: enp0s1
IPv4: 192.168.64.2

## Storage Checck

df -h
-Root filesystem /: 11G total
-Used: 4.7G
-Available: 5.5G

## Memory Check

free -h

-RAM: 3.8Gi
-Swap: 2.1Gi

## SSH Service Check

systemctl status ssh
sudo systemctl enable --now ssh
system status shh

-SSH installed
-SSH enabled
-SSH active and running

## Package Updates

sudo apt update && apt upgrade -y

-System package lists updated
-Installed package upgrades successfully

## User Creations

sudo adduser opsuser
sudo usermod -aG sudo opsuser
id opsuser

-Created secondary admin practice user: opsuser
-Added opsuser to sudo group
-Verified group membership with id

## File Permission Test

touch testfile.txt
ls -l
chmod 664 testfile.txt
ls -l
chmod 600 testfile.txt
ls -l testfile.txt

-Verified file creation
-Verified permission changes from 664 to 600

## Cron Service Check

sudo systemctl enable --now cron
systemctl status cron

-Cron enabled
-Cron active and running

## Crone Job Test

crontab -e
crontab -l
cat /home/nick/cron_test.log

-Created test cron job to append timestamp every minute
-Verified cron job executed succefully
-Removed test cron job after validation

## Remote SSH Test from Mac

ssh nick@192.168.64.2
touch ~/ssh_created.txt && ls -l ~/ssh_created.txt

-SSH connection from Mac to VM succeeded
-Created file remotely over SSH
-Verified sudo over SSH returned root
