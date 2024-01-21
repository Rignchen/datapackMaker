from importlib import import_module
from lib.files import getPath
from lib.i_o import choice, cls
from os import listdir, path

names = [i.removesuffix(".py") for i in listdir(
	path.join(getPath(__file__), "template_type"))]
if "__pycache__" in names: names.remove("__pycache__")

try:
	cls()
	templateType = names[choice("Wich template do you want? ",names)]
	cls()
	print(f"{templateType} template chosen\n")

	import_module(f"template_type.{templateType}") # run the selected script
except KeyboardInterrupt:
	print("\nCancel")
