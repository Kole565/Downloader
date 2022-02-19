"""DownloadManager script

Provide a REPL system to collect download data from the user.
Executes the collected data with exception handling.

"""
import sys
import os

PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(PROJECT_DIR))

from lib.download import Download

from lib.downloader import Downloader
from lib.downloads_collection import DownloadsCollection


downloads = DownloadsCollection()

dir = input("Enter destination folder (empty for 'downloads' in root):")
if not dir:
    dir = "../downloads/"

downloader = Downloader(dir)

print()

while True:
    url = file = ""

    url = input("Enter URL (empty for exit): ")
    file = input("Enter file name without extension (empty for exit): ")

    if not url or not file:
        break

    try:
        download = Download(url, file)
        downloads.add(download)
    except Exception as e:
        print(e)
    else:
        print("\nDownload added in queue\n")    

downloader.download(downloads.get())
try:
    downloader.download(downloads.get())
except Exception as e:
    print(e)    
else:
    print("\nDownload(s) completed")
finally:
    input()
