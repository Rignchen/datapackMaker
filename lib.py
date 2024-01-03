def choice(text:str, choices: list[str]):
	if len(choices) == 0: raise IndexError("There needs to be at least 1 option to chose")
	if len(choices) == 1: return 0
	for i in range(len(choices)):
		print(f"{i+1}) {choices[i]}")
	ans = ""
	while not (len(ans) > 0 and ans.isdigit() and 0 < int(ans) <= len(choices)):
		ans = input(text)
	return int(ans) -1
