import re
from requests import get as rget

def request(url: str) -> dict[str,any]|list[any]:
	"""
	Make a request to the url and return the json
	"""
	request = rget(url)
	return request.json()
def correctChoiceErrorCheck(ans: str, choices: list[str], errorFunction: callable) -> str:
	result = errorFunction(ans,choices)
	if result != None: return [result]
class license:
	def __init__(self, name: str, description: str, content: str):
		self.name = name
		self.description = description
		self.content = content
class getLicense:
	def __init__(self, licenseList: dict[str,str]):
		self.licenses: dict[str,license] = {}
		self.licenseList = licenseList
	def getLicense(self, prompt: str):
		if prompt in self.licenseList:
			if prompt not in self.licenses:
				content: dict[str,str] = request(self.licenseList[prompt])
				self.licenses[prompt] = license(prompt, content["description"], content["body"])
			return self.licenses[prompt]
		return license("Custom", "Custom license", prompt)
def removeHtml(text: str) -> str:
	"""
	Remove html tags from a string
	"""
	return re.sub("<[^<]+?>", "", text)
