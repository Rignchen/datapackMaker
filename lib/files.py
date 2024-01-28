from json import dump
from os import makedirs, path as osPath
from shutil import copy
from lib.i_o import choice, ask
from lib._private import getLicense, request, removeHtml

def getPath(path:str):
	"""
	Get the path of the folder where a file is stored
	"""
	return path.removesuffix(osPath.basename(path))
def makeFile(path: str, content: str|list[str] = ""):
	"""
	Make a file + parents folder
	"""
	makeFolder(getPath(path))
	with open(path, "w+") as f:
		f.write(content if isinstance(content, str) else '\n'.join(content))
def makeFolder(path: str):
	"""
	Make folder and subfolders
	"""
	if path: makedirs(path, exist_ok=True)
def makeJson(path: str, content: dict):
	"""
	Make a json file + parents folder
	"""
	makeFolder(getPath(path))
	with open(path, "w+") as f:
		dump(content, f, indent="\t")
def makeTree(tree: dict[str|dict[str,str]], path: str = ""):
	"""
	Make the folders, subfolders and files as set in the dictionary
	"""
	for tree_element in tree:
		new_path = osPath.join(path, tree_element)
		content = tree[tree_element]
		if isinstance(content, dict):
			makeFolder(new_path)
			makeTree(content, new_path)
		elif isinstance(content, (str, list)):
			makeFile(new_path,content)
def addLicense(path: str = "", content: str = None):
	"""
	Add a licence in the root of the project\n
	When the content isn't specified, the user will be asked to choose a license otherswise, the license can also be imposed by the template.\n
	Chosing a license can wither be done by choosing it's name if it's on the github api or by writing it's content.\n
	List of licenses available on github on 2024-01-24:
	- GNU Affero General Public License v3.0
	- Apache License 2.0
	- BSD 2-Clause "Simplified" License
	- BSD 3-Clause "New" or "Revised" License
	- Boost Software License 1.0
	- Creative Commons Zero v1.0 Universal
	- Eclipse Public License 2.0
	- GNU General Public License v2.0
	- GNU General Public License v3.0
	- GNU Lesser General Public License v2.1
	- MIT License
	- Mozilla Public License 2.0
	- The Unlicense
	"""
	licenses = getLicense({r["name"]: r["url"] for r in request("https://api.github.com/licenses")})
	licenseNames = [l for l in licenses.licenseList]
	if content == None:
		errorFunction = lambda x,y: x if len(x) > 0 and x[0].isalpha() else (x if x == "0" else None)
		while True:
			print("Choose a licence or write the content of the licence you want. Enter 0 if you don't want any license:")
			license = choice("", licenseNames, errorFunction)

			if license == "0":
				if ask("You chose not to have a license, are you sure?"):
					return
			elif isinstance(license, str):
				licenseContent = licenses.getLicense(license)
				break
			else:
				licenseContent = licenses.getLicense(licenseNames[license])
				if ask(f"You chose the {licenseContent.name} license wich is:\n {removeHtml(licenseContent.description)}\nDo you want to keep it?"):
					break
	# the license is imposed by the template
	else:
		licenseContent = licenses.getLicense(content)
	makeFile(osPath.join(path, "LICENSE.md"), licenseContent.content)
def copyFile(ressource_path: str, new_path: str):
	"""
	Copy a file from a path in the assets folder to another
	"""
	copy(osPath.join(getPath(osPath.dirname(__file__)), "assets", ressource_path), new_path)
