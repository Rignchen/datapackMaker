from os import listdir, path
from importlib import import_module
from lib import choice, cls, getPath

names = [i.removesuffix(".py") for i in listdir(
	path.join(getPath(__file__), "template_type"))]
if "__pycache__" in names: names.remove("__pycache__")

cls()
templateType = names[choice("Wich template do you want? ",names)]
cls()
print(f"{templateType} template chosen\n")

try:
	import_module(f"template_type.{templateType}")
except KeyboardInterrupt:
	print("\nCancel")
