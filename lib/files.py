from json import dump
from os import makedirs, path as osPath

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
