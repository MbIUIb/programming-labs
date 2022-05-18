from pathlib import Path
import lab10

data_of_lab9_path = Path('../Lab9/Data')
key = (data_of_lab9_path /  'key').read_text()
lab10.decrypt(data_of_lab9_path / 'lab9_logs.txt', 'Data/decryptlogs', key)
