from genericpath import isdir
from importlib import import_module
from lib.files import getPath
from lib.i_o import choice, cls, color as color
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
		removeInList(files,["__scripts","__pycache__"])
		files = [file.removesuffix(".py") for file in files]

		cls()
		match len(files):
			case 0:
				print("No template found")
				exit()
			case 1:
				chosenType = 0
			case _:
				if len(templateName) > 0:
					print(f"Template type chosen: {templateName}\n")
				filesNames = [
					f"{color.blue}{color.bold}{file}{color.default}{color.bold}/{color.default}"
					if isdir(osPath.join(path, file)) else file
					for file in files]
				chosenType = choice("Wich template do you want? ", filesNames, lambda x, y: "0" if x == "0" else None)
		if isinstance(chosenType, int):
			path = osPath.join(path, files[chosenType])
		else:
			oldPath = path
			while True:
				if len(path) > len(defaultFolder):
					path = osPath.dirname(path)
				else:
					path = oldPath
					break
				if len(listdir(path)) > 1: break

	templateName = path.replace(f'{defaultFolder}/','',1)
	print(f"template chosen: {templateName}\n")

	import_module(path.replace('/','.')) # run the selected script
except KeyboardInterrupt:
	print("\nCancel")
