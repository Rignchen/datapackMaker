import re
from requests import get as rget

def _request(url: str) -> dict[str,any]|list[any]:
	"""
	Make a request to the url and return the json
	"""
	request = rget(url)
	return request.json()
def _correctChoiceErrorCheck(ans: str, choices: list[str], errorFunction: callable) -> str:
	result = errorFunction(ans,choices)
	if result != None: return [result]
