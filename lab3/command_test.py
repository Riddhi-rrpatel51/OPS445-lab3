#!/usr/bin/env python3
import os

# Test os.system()
os.system('ls')
os.system('whoami')
os.system('ifconfig')

# Compare outputs with return values
ls_return = os.system('ls')
print('The contents of ls_return:', ls_return)
whoami_return = os.system('whoami')
print('The contents of whoami_return:', whoami_return)
ifconfig_return = os.system('ifconfig')
print('The contents of ifconfig_return:', ifconfig_return)

# Try a command that doesn't exist
ipconfig_return = os.system('ipconfig')
print('The contents of ipconfig_return:', ipconfig_return)
