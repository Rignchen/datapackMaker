from os import name as osName, system

def askDefault(text:str, default: str|None = None):
	"""
	Ask the user for a question, if the user doesn't answer, take the default value if there is one, otherwise ask again
	"""
	if default: text += f"({default})"
	ans = ""
	while ans == "":
		ans = input(text)
		if ans == "" and default:
			ans = default
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
class getData():
	"""
	Ask the user for data requiered to make a datapack
	"""
	def __init__(self):
		"""
		Ask the user for data requiered to make a datapack
		"""
	def getDatapackName(self):
		"""
		Get the name of the datapack
		"""
		self.datapackName = askDefault("What's the name of the pack? ")
		return self
	def getNamespace(self):
		"""
		Get the namespace of the datapack
		"""
		self.namespace = askDefault("What's the namespace of the pack? ").lower().replace(" ","_")
		return self
	def getMcVersion(self):
		"""
		Get the Minecraft version
		"""
		mcVersion = ""
		while not (len(mcVersion) > 0 and mcVersion.isdigit() and int(mcVersion) >= 4):
			mcVersion = input("For wich version is it made? ")
		self.mcVersion = int(mcVersion)
		return self
	def getVersion(self):
		"""
		Get the version of the datapack
		"""
		self.version = askDefault("What's the version of the pack? ", "1.0.0")
		if "." in self.version:
			self.version = self.version.split(".")
			if len(self.version) < 3:
				self.version += ["0"] * (3 - len(self.version))
			elif len(self.version) > 3:
				self.version = self.version[:3]
			self.version = "".join([v.zfill(2) for v in self.version])
		else:
			self.version = self.version.zfill(6)
		return self
	def getAuthor(self):
		"""
		Get the name of the author
		"""
		try:
			default = self.mcName
		except:
			default = None
		self.author = askDefault("Who's the author of this datapack? ", default)
		return self
	def getMcName(self):
		"""
		Get the minecraft username of the author
		"""
		try:
			default = self.author
		except:
			default = None
		self.mcName = askDefault("What's the minecraft username of the author? ", default)
		return self

def cls():
	"""
	Clear the shell
	"""
	system("cls" if osName == 'nt' else "clear")
