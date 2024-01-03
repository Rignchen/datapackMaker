from json import dump
from os import makedirs, name as osName, path as osPath, system

def choice(text:str, choices: list[str]):
	"""
	Ask the user to select one of the choice, return the index of it's choice
	"""
	if len(choices) == 0: raise IndexError("There needs to be at least 1 option to chose")
	if len(choices) == 1: return 0
	for i in range(len(choices)):
		print(f"{i+1}) {choices[i]}")
	ans = ""
	while not (len(ans) > 0 and ans.isdigit() and 0 < int(ans) <= len(choices)):
		ans = input(text)
	return int(ans) -1
def cls():
	system("cls" if osName == 'nt' else "clear")
class getData():
	def __init__(self):
		"""
		Ask the user for pack name, namespace and version
		"""
		self.datapackName = ""
		self.namespace = ""
		self.version = ""
		while self.datapackName == "":
			self.datapackName = input("What's the name of the pack? ")
		while self.namespace == "":
			self.namespace = input("What's the namespace of the pack? ")
		while self.version == "" or not self.version.isdigit():
			self.version = input("For wich version is it made? ")
	def getAuthor(self):
		"""
		Get the name of the author
		"""
		self.author = ""
		while self.author == "":
			self.author = input("Who's the author of this datapack? ")
		return self
def getPath(path:str):
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
	makedirs(path, exist_ok=True)
def make_json(path: str, content: dict):
	"""
	Make a json file + parents folder
	"""
	make_folder(getPath(path))
	with open(path, "w+") as f:
		dump(content, f, indent="\t")


def make_tree(tree: dict[str|dict[str,str]], path: str = ""):
	for tree_element in tree:
		new_path = osPath.join(path, tree_element)
		content = tree[tree_element]
		if isinstance(content, dict):
			make_folder(new_path)
			make_(content, new_path)
		elif isinstance(content, (str, list)):
			make_file(new_path,content)
