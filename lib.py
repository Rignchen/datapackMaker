def choice(text:str, choices: list[str]):
    for i in range(len(choices)):
        print(f"{i+1}) {choices[i]}")
    ans = ""
    while not (len(ans) > 0 and ans.isdigit() and 0 < int(ans) <= len(choices)):
        ans = input(text)
    return int(ans) -1
