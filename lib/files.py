from json import dump
from os import makedirs, name as osName, path as osPath, system

def getPath(path:str):
	"""
	Get the path of the folder where a file is stored
	"""
	return path.removesuffix(osPath.basename(path))
def make_file(path: str, content: str|list[str] = ""):
	"""
	Make a file + parents folder
	"""
	make_folder(getPath(path))
	with open(path, "w+") as f:
		f.write(content if isinstance(content, str) else '\n'.join(content))
def make_folder(path: str):
	"""
	Make folder and subfolders
	"""
	if path: makedirs(path, exist_ok=True)
def make_json(path: str, content: dict):
	"""
	Make a json file + parents folder
	"""
	make_folder(getPath(path))
	with open(path, "w+") as f:
		dump(content, f, indent="\t")
def make_tree(tree: dict[str|dict[str,str]], path: str = ""):
	"""
	Make the folders, subfolders and files as set in the dictionary
	"""
	for tree_element in tree:
		new_path = osPath.join(path, tree_element)
		content = tree[tree_element]
		if isinstance(content, dict):
			make_folder(new_path)
			make_tree(content, new_path)
		elif isinstance(content, (str, list)):
			make_file(new_path,content)
