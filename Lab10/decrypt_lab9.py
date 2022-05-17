import lab10

with open('D:\Lab\programming_languages_labs\Lab9\Data\key') as f:
    key = f.read()
lab10.decrypt('D:\Lab\programming_languages_labs\Lab9\Data\lab9_logs.txt', 'Data\\decryptlogs', key)
