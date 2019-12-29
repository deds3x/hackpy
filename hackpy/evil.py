from hackpy.commands import *
from hackpy.settings import *
from hackpy.modules  import *

# Crash system
def bsod():
	require_module('bsod.exe')
	command.system(modules_path + 'bsod.exe', return_code = True)[1]
	if status == 0:
		return True
	else:
		return False

# Rotate screen
def rotateScreen(degrees = 0):
	require_module('rotate_screen.exe')
	if not degrees in (0, 90, 180, 270):
		raise Warning('rotateScreen() only can 0, 90, 180, 270')
		return False
	status = command.system(modules_path + 'rotate_screen.exe ' + str(degrees), return_code = True)[1]
	if status == 0:
		return True
	else:
		return False