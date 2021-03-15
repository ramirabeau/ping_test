#!/bin/usr/env python3

import os

# Create the variable to write the results to the file as directed
results_pass_file = open("ping_pass_results.txt", "a+")
results_fail_file = open("ping_fail_results.txt", "a+")

#ip_list will be an empty string
ip_list = []

# Enter the ip range that needs to be tested
for ip in range(1, 256):
    ip_list.append("192.168.1." + str(ip))

for ip in ip_list:
    response = os.popen(f"ping {ip} -n 1").read()
    if "Received = 1" and "Approximate" in response:
        results_pass_file.write(f"Up {ip} Ping Successful" + "\n")
        print(f"{ip} UP")
    else:
        results_fail_file.write(f"Down {ip} Ping Unsuccessful" + "\n")
        print(f"{ip} DOWN")

results_pass_file.close()
results_fail_file.close()

