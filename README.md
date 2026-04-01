# Home SOC Lab

This project simulates a small Security Operations Center environment running on my Ubuntu server at home. 
The lab monitors network traffic and system logs to detect suspicious activity.

## Tools Used
- UFW (Firewall)
- Snort (Network IDS)
- TCPdump (Packet capture)
- Python (log analysis scripts)

## Project Goal
The goal of this project is to gain practical experience in cyber security

Through this project I have gained hands-on experience in:

- intrusion detection
- log analysis
- attack simulation
- automated alert generation

## Scripts - SSH Brute Force Detector
This script, written in Python, is used to capture any failed SSH login attempts that could be interpreted as brute forcce attacks

The script analyzes '/var/log/auth.log' file for failed attempts, if there is a pattern of 5 or more failed login attempts from the same
IP address the IP address is flagged and added to 'soc_alerts.log'

![Brute Force Code](screenshot/ssh_bruteforce_detector code.png)


