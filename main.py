import os
import time
admpass = os.environ['ADM_PASS']
my_secret = os.environ['OwnerMCode']
print('Code start log: Log num 52834569617')
time.sleep(2)
seconds=time.time()
local_time = time.ctime(seconds)
print("Time of log entry:", local_time)
time.sleep(1)
print('System loaded')
time.sleep(2)
print('Main OS: Environ/Python3.7/Linux(offline)')
time.sleep(1)
print('Loading: 0%')
time.sleep(0.5)
print('Loading: 32%')
time.sleep(0.5)
print('Loading: 74%')
time.sleep(0.5)
print('Loading: 90%')
time.sleep(0.5)
print('Loading: 99%')
time.sleep(0.5)
print('Loaded: 100%')
time.sleep(2)
name=input('Enter your name. ')
adm=input('Are you an admin of this system? (Y or N) ')
adm=adm.lower()
if adm ==('y'):
	print('Enter the Admin Passcode: ')
	ladm=input('')
	if ladm == (admpass):
		print('Clear The Console')
		time.sleep(5)
		print('Welcome',name+', Is this your first login? (Y or N) ')
		login=input('')
		login=login.lower
		if login==('y'):
			print('Getting List Of Commands')
			time.sleep(3)
			print('Program error')
			time.sleep(2)
			print('File shutdown')
			time.sleep(0.5)
			print('Closing program')
		else:
			print('Ok do you need to know the command list? (Y or N) ')
			cmds=input('')
			cmds=cmds.lower
			print('Error. System shutdown')
	else:
		print('Corruption detected, closing...')
else:
	print('Are you a member of this server? (Y or N) ')
	member=input('')
	member=member.lower()
	if member ==('y'):
		print('Enter your member code: ')
		memcode=input('')
		if memcode==OwnerMCode:
			print()
		elif memcode==:
	else:
		print()