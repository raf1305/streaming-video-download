import shutil
import os
import subprocess
import ffmpeg
from pathlib import Path

cwd = os.getcwd()
files = []


def merge_files(folder_name):
	for i in os.listdir(f'{cwd}/{folder_name}'):
		if i.endswith('.ts'):
			files.append(i)

	with open(f'{folder_name}/merged.ts', 'wb') as merged:
		for i in files:
			with open(f'{folder_name}/{i}', 'rb') as mergefile:
				shutil.copyfileobj(mergefile, merged)
	return Path(f'{folder_name}/merged.ts').stat().st_size / (1024 * 1024)
	# to convert ts file to mp4 but takes long time
	# subprocess.run(['ffmpeg', '-i', 'p/merged.ts', 'p/merged.mp4'])
