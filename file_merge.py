import shutil
import os
import subprocess
import ffmpeg

cwd = os.getcwd()
files = []


def merge_files(folder_name):
	for i in os.listdir(f'{cwd}/{folder_name}'):
		if i.endswith('.ts'):
			files.append(i)

	with open(f'{folder_name}/merged.ts', 'wb') as merged:
		for i in range(1, len(files)+1):
			with open(f'{folder_name}/{str(i)}.ts', 'rb') as mergefile:
				shutil.copyfileobj(mergefile, merged)

	# to convert ts file to mp4 but takes long time
	# subprocess.run(['ffmpeg', '-i', 'p/merged.ts', 'p/merged.mp4'])
