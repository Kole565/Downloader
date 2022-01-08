"""DownloadManager script

Provide REPL system of gathering downloads data from user.
Execute gathered downloads with exception handling.

"""
import requests

from downloader import Downloader
from downloads_collection import DownloadsCollection
from download import Download


downloads = DownloadsCollection([])

print("DOWNLOADER", end = "\n\n")

dir = input("Enter destination folder (empty for 'downloads' in root):")
if not dir:
    dir = "downloads/"

downloader = Downloader(dir)

print()

while True:
    url = file = ""

    url = input("Enter URL: ")
    file = input("Enter file name without extension: ")

    if (url == "end") or (file == "end"):
        break

    try:
        download = Download(url, file)
        downloads.add(download)
    except Exception as e:
        print(e)
    else:
        print("\nDownload added in queue\n")
    

try:
    downloader.download(downloads)
except Exception as e:
    print(e)
else:
    print("\nDownload(s) completed")
finally:
    input()
