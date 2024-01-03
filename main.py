from os import listdir
from importlib import import_module
from lib import choice

names = [i.removesuffix(".py") for i in listdir("template_type")]
if "__pycache__" in names: names.remove("__pycache__")

templateType = names[choice("Wich template do you want? ",names)]

import_module(f"template_type.{templateType}")
