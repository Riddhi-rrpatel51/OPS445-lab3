#!/usr/bin/env python3
import subprocess

p = subprocess.Popen(['date'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
output = p.communicate()
print(output)  # Outputs a tuple of stdout and stderr

stdout = output[0].decode('utf-8').strip()
print(stdout)  # Display the date in string format
