import os
from threading import Thread
from queue import Queue

import m3u8
import file_download, file_merge, index_download, pattern_matching
import time

index_url = 'https://hoichoihlsns.akamaized.net/vhoichoiindia2/Renditions/20200626/1593178102447_tt_ep_01_bng/hls/1593178102447_tt_ep_01_bng_480.m3u8?hdntl=exp=1656475421~acl=/*~data=hdntl~hmac=585d20107ebc2813a20b7a72554aa7dcebd6a428e078b156e532d288623a443c'

file_name = index_download.download_index_file(index_url)
folder_name = file_name.split('.')[0]
base_url = pattern_matching.search_base_url(index_url)
playlist = m3u8.load(file_name)  # this could also be an absolute filename
qu = Queue()

if not os.path.exists(folder_name):
    os.makedirs(folder_name)
# print(f'file name : {file_name}\n base url : {base_url} \n  {playlist.files}')


class DownloadWorker(Thread):

    def __init__(self, queue):
        Thread.__init__(self)
        self.queue = queue

    def run(self):
        while True:
            # Get the work from the queue and expand the tuple
            sub_url = self.queue.get()
            ts_file_name = pattern_matching.ts_file_name(sub_url)
            try:
                file_download.download_file(base_url, sub_url, ts_file_name,folder_name)
            finally:
                self.queue.task_done()


c = 0
for x in range(8):
    worker = DownloadWorker(qu)
    # Setting daemon to True will let the main thread exit even though the workers are blocking
    worker.daemon = True
    worker.start()

start_time = time.time()
for sub_url in playlist.files:
    c += 1
    # ts_file_name = pattern_matching.ts_file_name(sub_url)
    # file_download.download_file(base_url, sub_url, ts_file_name,folder_name)
    qu.put(sub_url)
    if c == 15:
        break
qu.join()
end_time = time.time()
file_size = file_merge.merge_files(folder_name)
merge_time = time.time()
dload_time = end_time -start_time

f = open("dload_log.txt", "a")
f.write('\n\nThreadQue Method\n\n')
# f.write('\n\Single Method\n\n')
f.write(f'Download Time : {dload_time} \nMerge Time : {merge_time-end_time} \nFile Size : {file_size} \nAVG Dload {file_size/dload_time} MB/s')
f.close()
print(dload_time)
print(merge_time-end_time)
print(file_size)
print(file_size/dload_time)
