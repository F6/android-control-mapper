'''
For some android devices (those using Linux kernel), recording 
input events is possible with the "getevent" command. Combining 
the command with adb, it's possible to record a series of 
inputs performed on an android device, then use the record to 
replay the inputs.


To replay the record precisely, we need to push the record and a replayer program onto the device, then replay the record with the program. Cartucho's android-touch-record-replay library can be used.
'''

import subprocess

def replay_input(input_device='/dev/input/event5', record_filename='record.txt'):
    command_list = []
    # push the binary to the device
    command_list.append('adb push android-touch-record-replay/mysendevent /data/local/tmp/')
    # push the record to the device storage /sdcard/
    command_list.append(
        'adb push {record_filename} /sdcard/'.format(record_filename=record_filename))
    # replay the record
    command_list.append('adb shell /data/local/tmp/mysendevent "{input_device}" /sdcard/{record_filename}'.format(
        input_device=input_device, record_filename=record_filename))

    for command in command_list:
        subprocess.run(command, shell=True)

replay_input()