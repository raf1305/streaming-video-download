import os
import urllib.request
cur_path = os.getcwd()
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'}

opener = urllib.request.build_opener()
opener.addheaders = [('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36')]
urllib.request.install_opener(opener)


def download_file(base_url, custom_url, file_name, folder_name):
	url = base_url + custom_url
	urllib.request.urlretrieve(url, cur_path+f'/{folder_name}/'+file_name)
	print(f'Downloaded {file_name}')
