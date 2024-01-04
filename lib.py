from json import dump
from os import makedirs, name as osName, path as osPath, system

def askDefault(text:str, default: tuple[bool, str]):
	"""
	Ask the user for a question, if the user doesn't answer, take the default value if there is one, otherwise ask again
	"""
	if default[0]: text += f"({default[1]})"
	ans = ""
	while ans == "":
		ans = input(text)
		if ans == "" and default[0]:
			ans = default[1]
			break
	return ans
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
	"""
	Clear the shell
	"""
	system("cls" if osName == 'nt' else "clear")
class getData():
	"""
	Ask the user for the requiered data (datapack name, namespace, version)
	"""
	def __init__(self):
		"""
		Ask the user for pack name, namespace and version
		"""
		self.datapackName = askDefault("What's the name of the pack? ",(False))
		self.namespace = askDefault("What's the namespace of the pack? ",(False)).lower().replace(" ","_")
		self.version = int(askDefault("For wich version is it made? ",(False)))
	def getAuthor(self):
		"""
		Get the name of the author
		"""
		try:
			default = (True, self.mcName)
		except:
			default = (False)
		self.author = askDefault("Who's the author of this datapack? ", default)
		return self
	def getMcName(self):
		"""
		Get the minecraft username of the author
		"""
		try:
			default = (True, self.author)
		except:
			default = (False)
		self.mcName = askDefault("What's the minecraft username of the author? ", default)
		return self
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
	makedirs(path, exist_ok=True)
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
