'''
For some android devices (those using Linux kernel), recording 
input events is possible with the "getevent" command. Combining 
the command with adb, it's possible to record a series of 
inputs performed on an android device, then use the record to 
replay the inputs.


We can use 

    getevent -lp 

to list all input devices. Then, we choose the appropriate 
device to be recorded, let's assume it's /dev/input/event5 . we 
can use 

    getevent -t /dev/input/event5 > record.txt

to record all the events, with timestamp, into a textual file 
called record.txt .


Combining the above method with adb, we can use

    adb shell getevent -t /dev/input/event5 > record.txt

to download the record to our local machine.
'''

import subprocess

input_device = '/dev/input/event5'
record_filename = 'record.txt'


def record_input(input_device='/dev/input/event5', record_filename='record.txt'):
    cmd = 'adb shell getevent -t {input_device} > {record_filename}'.format(input_device=input_device, record_filename=record_filename)
    return subprocess.run(cmd, shell=True)

record_input()