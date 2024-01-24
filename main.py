from genericpath import isdir
from importlib import import_module
from lib.files import getPath
from lib.i_o import choice, cls
from os import listdir, path as osPath

def removeInList(array: list, values: list):
	for value in values:
		if value in array: array.remove(value)
	return array

defaultFolder = "template_type"

cls()
path = defaultFolder

try:
	while isdir(path):
		templateName = path.replace(f'{defaultFolder}/','',1)
		files = listdir(osPath.join(getPath(__file__), path))
		removeInList(files,["scripts","__pycache__"])
		files = [file.removesuffix(".py") for file in files]

		cls()
		match len(files):
			case 0:
				print("No template found")
				exit()
			case 1:
				chosenType = files[0]
			case _:
				if len(templateName) > 0:
					print(f"Template type chosen: {templateName}\n")
				chosenType = files[choice("Wich template do you want? ",files)]
		path = osPath.join(path, chosenType)

	templateName = path.replace(f'{defaultFolder}/','',1)
	print(f"template chosen: {templateName}\n")

	import_module(path.replace('/','.')) # run the selected script
except KeyboardInterrupt:
	print("\nCancel")
