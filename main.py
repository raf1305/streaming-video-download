import os
import m3u8
import file_download, file_merge, index_download, pattern_matching
import time

index_url = 'https://hoichoihlsns.akamaized.net/vhoichoiindia2/Renditions/20200626/1593178102447_tt_ep_01_bng/hls/1593178102447_tt_ep_01_bng_480.m3u8?hdntl=exp=1656475421~acl=/*~data=hdntl~hmac=585d20107ebc2813a20b7a72554aa7dcebd6a428e078b156e532d288623a443c'

file_name = index_download.download_index_file(index_url)
folder_name = file_name.split('.')[0]
base_url = pattern_matching.search_base_url(index_url)
playlist = m3u8.load(file_name)  # this could also be an absolute filename

if not os.path.exists(folder_name):
    os.makedirs(folder_name)
# print(f'file name : {file_name}\n base url : {base_url} \n  {playlist.files}')

c = 0
start_time = time.time()
for sub_url in playlist.files:
	c += 1
	ts_file_name = pattern_matching.ts_file_name(sub_url)
	file_download.download_file(base_url, sub_url, ts_file_name,folder_name)
	if c == 15:
		break
file_size = file_merge.merge_files(folder_name)
end_time = time.time()
dload_time = end_time -start_time
print(dload_time)
print(file_size)
print(file_size/dload_time)
