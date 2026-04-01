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
This script, written in Python, is used to capture any failed SSH login attempts that could be interpreted as brute force attacks.

The script analyzes the '/var/log/auth.log' file for failed attempts, if there is a pattern of 5 or more failed login attempts from the same
IP address the IP address is flagged and added to 'soc_alerts.log'

__________________________________________________________________________________________________________________________________________________

![Brute Force Code](screenshots/ssh_bruteforce_detector_code.png)

The screenshot above shows the code implemented onto my Ubuntu server.

![Brute Force Code](screenshots/wrong_password_entry.png)

![Brute Force Detected](screenshots/brute_force_detected.png)

Above you can see an example of incorrect password entry and two instances of possible brute force activity reported.

![Brute Force Detected](screenshots/automating_brute_force_detection.png)

Finally, above I used crontab to automate this system. Now, the script will run everyday at 2am and print results into soc_alerts.log.

__________________________________________________________________________________________________________________________________________________

From this activity I have learned how to read log activity, produce a report, and log the report all automatically.
Like I said in at the beginning of this README, my goal is to gain hands-on experience and come into the cyber world prepared for whatever I am asked.

