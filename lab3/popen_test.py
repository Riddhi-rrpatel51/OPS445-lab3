#!/usr/bin/env python3
import os

# Test os.popen()
ls_return = os.popen('ls').read()
print('The contents of ls_return:', ls_return)

whoami_return = os.popen('whoami').read()
print('The contents of whoami_return:', whoami_return)

ifconfig_return = os.popen('ifconfig').read()
print('The contents of ifconfig_return:', ifconfig_return)

# Try with a command that doesn't exist
ipconfig_return = os.popen('ipconfig').read()
print('The contents of ipconfig_return:', ipconfig_return)
