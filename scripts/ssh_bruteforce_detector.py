import re # regular expression, search texts for patterns

log_file = "/var/log/auth.log" # Linux authentication log

failed_attempts = {}

with open(log_file, "r") as file:
    for line in file:
        if "Failed password" in line: # find failed password attempts
            ip = re.search(r'from (\d+\.\d+\.\d+\.\d+)', line) # IPv4

            if ip:
                ip = ip.group(1)

                if ip not in failed_attempts: # if the found address is in the dictionary add, if not create new key-value pair
                    failed_attempts[ip] = 0

                failed_attempts[ip] += 1

for ip, count in failed_attempts.items(): # if there are 5 or more failed attempts alert possible brute force
    if count >= 5:
        print(f"Possible brute force attack from {ip} ({count} attempts)")
