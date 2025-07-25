# Linux Basics for DevOps: Most Used Commands

Linux skills are vital for DevOps engineers because most server environments run on Linux. Below are the essential Linux commands and concepts you’ll use daily in real-world DevOps roles.

## Basic Directory and File Navigation

- `pwd` — Show current directory.
- `ls` — List files in a directory.
    - `ls -l` (long listing), `ls -a` (show hidden files)
- `cd [dir]` — Change directory.
    - `cd /home/user`  
    - `cd ..` (go up one level)
- `mkdir [dir]` — Create a new directory.
- `rm [file]` — Delete a file.
    - `rm -r [dir]` (remove directory and contents)
- `cp [src] [dest]` — Copy files/directories.
    - `cp -r` for directories.
- `mv [old] [new]` — Move or rename files.

## Viewing and Editing Files

- `cat [file]` — Display file contents.
- `less [file]` — View large files page by page.
- `head [file]` / `tail [file]` — View first/last lines of a file.
    - `tail -f [file]` (live update; useful for logs)
- `nano [file]` or `vim [file]` — Edit text files in the terminal.

## Searching and Filtering

- `grep 'pattern' [file]` — Search for text in files.
    - `grep -r 'pattern' [dir]` (recursive)
- `find [path] -name "*.log"` — Find files matching a pattern.
- `sort`, `uniq`, `wc -l` — Sort, remove duplicates, count lines.
- `cut` and `awk` — Extract and process columns from text.

## File Permissions and Ownership

- `ls -l` — View permissions.
- `chmod [permissions] [file]` — Change permissions (e.g., `chmod 755 script.sh`)
- `chown [user]:[group] [file]` — Change ownership.

## System Monitoring

- `top` / `htop` — Live monitoring of system resources.
- `ps aux` — List running processes.
- `df -h` — Show disk usage.
- `du -sh [dir]` — Directory size.
- `free -h` — Memory usage.
- `uptime` — System running time and load.

## Networking Commands

- `ifconfig` or `ip a` — Network interface info.
- `ping [host]` — Check connectivity.
- `curl [url]` or `wget [url]` — Download or test APIs.
- `netstat -tuln` — List open ports.
- `ss -tuln` — (Modern alternative to `netstat`)
- `ssh [user]@[host]` — Securely connect to remote servers.
- `scp [file] [user]@[host]:[path]` — Secure file copy between hosts.

## Package Management (Common Examples)

- **Debian/Ubuntu:** `apt update`, `apt install [package]`
- **RHEL/CentOS:** `yum install [package]`
- **Universal:** `dpkg`, `rpm`

## Useful Advanced Commands

- `tar -czvf archive.tar.gz [dir]` — Create a compressed archive.
- `chmod +x [file]` — Make a script executable.
- `export VAR=value` — Set environment variable in shell.
- `cron` / `crontab -e` — Schedule tasks.

## Tips for DevOps

- Learn to chain commands using `|` (pipes). Ex: `cat app.log | grep ERROR | wc -l`
- Use tab completion and command history for speed (`history`).
- Practice editing with `vim`, as it is available on almost every system.

## Summary Table: Essential Commands

| Task                   | Most Used Command Example        |
|------------------------|----------------------------------|
| List files             | `ls -l`                         |
| Check location         | `pwd`                           |
| Copy files             | `cp file1.txt /tmp/`            |
| Edit text              | `nano config.yaml`              |
| Search logs            | `grep "error" app.log`          |
| View system usage      | `top`                           |
| Connect to server      | `ssh user@host`                 |
| Network troubleshoot   | `ping 8.8.8.8`                  |
| Install package        | `apt install nginx`             |

Mastering these Linux commands will enable you to troubleshoot, automate tasks, and manage servers effectively—the core of DevOps work. Practice them frequently to gain speed and confidence.