import m3u8
import file_download, file_merge
base_url = 'https://hoichoihlsns.akamaized.net/vhoichoiindia2/Renditions/20220502/1651472678802_dour_streaming_now_trailer/hls/'
folder_name = 'download'
playlist = m3u8.load('dour_hoichoi.m3u8')  # this could also be an absolute filename

j = 1
for sub_url in playlist.files:
	# file_download.download_file(base_url, sub_url, f'{j}.ts',folder_name)
	j += 1

file_merge.merge_files(folder_name)

