from lib._private import correctChoiceErrorCheck
from os import name as osName, system

## Input
def ask(text:str) -> bool:
	"""
	Ask the user a yes or no question, return True if the answer is yes, False otherwise
	"""
	while True:
		ans = input(f"{text} (y/n)").lower()
		if ans in ["y", "yes", "n", "no"]:
			break
	return ans in ["y", "yes"]
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
def inputIn(text:str, choices: list[str], errorFunction: callable = lambda x,y: None) -> str:
	"""
	Ask the user to input a value that is in the list, return the value\n
	If the user inputs a value that isn't in the list, call the errorFunction with arguments (the input, the list of choices)\n
	if the errorFunction returns a value, return that value
	"""
	if len(choices) < 2: raise IndexError("There needs to be at least 2 options to chose")
	while True:
		ans = input(text)
		if (ans in choices):
			break
		else:
			error = errorFunction(ans, choices)
			if error != None:
				return error
	return ans
def choice(text:str, choices: list[str], errorFunction: callable = lambda x,y: None) -> any:
	"""
	Ask the user to chose between the options, return the index of the option
	"""
	if len(choices) == 0: raise IndexError("There needs to be at least 1 option to chose")
	elif len(choices) == 1: return 0

	for i, choice in enumerate(choices):
		print(f"{i+1}. {choice}")

	correctedErrorFunction = lambda x,y: correctChoiceErrorCheck(x,y,errorFunction)

	ans = inputIn(text, [str(i+1) for i in range(len(choices))], correctedErrorFunction)

	return int(ans) - 1 if isinstance(ans, str) else ans[0]
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

## Output
def cls():
	"""
	Clear the shell
	"""
	system("cls" if osName == 'nt' else "clear")
class color():
	"""
	List of colors to add in the text to change how it looks
	"""
	default = '\033[0m'
	purple = '\033[95m'
	blue = '\033[94m'
	cyan = '\033[96m'
	green = '\033[92m'
	yellow = '\033[93m'
	red = '\033[91m'
	bold = '\033[1m'
	underline = '\033[4m'
