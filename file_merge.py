import shutil
import os
import subprocess
import ffmpeg
from pathlib import Path
from natsort import os_sorted
cwd = os.getcwd()
files = []


def merge_files(folder_name):
	try:
		for i in os_sorted(os.listdir(f'{cwd}/{folder_name}')):
			if i.endswith('.ts') and i !='merged.ts':
				files.append(i)

		with open(f'{folder_name}/merged.ts', 'wb') as merged:
			for i in files:
				with open(f'{folder_name}/{i}', 'rb') as mergefile:
					shutil.copyfileobj(mergefile, merged)
		return Path(f'{folder_name}/merged.ts').stat().st_size / (1000 * 1000)
	except Exception as e:
		return repr(e)
		
	# to convert ts file to mp4 but takes long time
	# subprocess.run(['ffmpeg', '-i', 'p/merged.ts', 'p/merged.mp4'])

if __name__ == '__main__':
	import sys
	folder_name = sys.argv[1]
	file_size = merge_files(folder_name)
	print(file_size)
	print(folder_name)
	# subprocess.run(['ffmpeg', '-i', 'index-f2-v1-a1/merged.ts', 'index-f2-v1-a1/merged.mp4'])
