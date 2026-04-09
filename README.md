# Home SOC Lab

This project simulates a small Security and Network Operations Center environment running on my Ubuntu server at home. 
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
This script, written in Python, is used to capture any failed SSH login attempts that could be interpreted as brute force attacks.

The script analyzes the '/var/log/auth.log' file for failed attempts, if there is a pattern of 5 or more failed login attempts from the same
IP address the IP address is flagged and added to 'soc_alerts.log'

________________________________________________________________

### Brute Force Detection Code
This screenshot shows the code implemented onto my Ubuntu server.

Here I use a dictionary to store key-value pairs. If an IP address has a failed login attempt it is added to the 'failed_attempts' dictionary.
If the value exceeds 4 failed attempts the IP address is listed in the report.

![Brute Force Code](screenshots/ssh_bruteforce_detector_code.png)

### Failed Entry and Failed Entry Detection
In the following screenshot I purposely used the incorrect password to SSH into my Ubuntu Server.

![Brute Force Code](screenshots/wrong_password_entry.png)

Here you can see my failed attempts were logged, along with another possible brute force attack from another test I ran.

![Brute Force Detected](screenshots/brute_force_detected.png)

### Automating the Brute Force Detection Script
Finally, I used crontab to automate this system. Now, the script will run everyday at 2am and print results into soc_alerts.log.

![Brute Force Detected](screenshots/automating_brute_force_detector.png)

### What I Learned and How I can Improve the System
From this activity I have learned how to read log activity, produce a report, and log the report all automatically.
Like I said in the beginning of this README, my goal is to gain hands-on experience and come into the cyber world prepared for whatever I am asked.

The system could use some improvement. It would be nice to be able to get more information from the culprit than just their IP address.
I would also like an automated way of checking whether a threat is actually present. This would be listed in the report and each instance would flagged as urgent or low priority.

*All IP addresses shown in this project are from a private lab environment used for testing.*

