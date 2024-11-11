ENABLE SERVICES IN WSL

service --status-all
service {service} start/stop/restart

(-) = not running
(+) = running

 [ - ]  apparmor
 [ ? ]  apport
 [ - ]  atd
 [ - ]  console-setup.sh
 [ + ]  cron
 [ ? ]  cryptdisks
 [ ? ]  cryptdisks-early
 [ - ]  dbus
 [ ? ]  hwclock.sh
 [ + ]  irqbalance
 [ - ]  iscsid
 [ - ]  keyboard-setup.sh
 [ - ]  kmod
 [ - ]  lvm2
 [ - ]  lvm2-lvmpolld
 [ - ]  multipath-tools
 [ + ]  open-iscsi
 [ - ]  open-vm-tools
 [ ? ]  plymouth
 [ ? ]  plymouth-log
 [ - ]  procps
 [ - ]  rsync
 [ - ]  rsyslog
 [ - ]  screen-cleanup
 [ - ]  ssh
 [ - ]  udev
 [ - ]  ufw
 [ - ]  unattended-upgrades
 [ - ]  uuidd
 [ - ]  x11-common


git commands:
 git clone <repo>
 git branch - if need approvals
  - do the changes
 git status
 git add .
 git commit -m <commit description>
 git push origin main

 user: user_name
 password: PAT (personal access token)
