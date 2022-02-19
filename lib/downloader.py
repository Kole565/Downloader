import requests


class Downloader():
    
    """Downloader class
    
    Provide methods for downloading files over the HTTP.
    
    """

    def __init__(self, save_dir="../downloads/"):
        """Create an instance with a folder to save"""
        self.save_dir = save_dir
    
    def get_request(self, link):
        """Get request over 'requests' lib"""
        request = requests.get(link, allow_redirects = True)
        
        return request
    
    def download(self, collection):
        """Load a collection of downloads as files"""
        downloads = collection
        
        # for i in range(len(downloads)):
        #     self.download_by(downloads[i].url, downloads[i].file)
        for download in downloads:
            self.download_by(download.url, download.file)
    
    def download_by(self, url, file):
        """Load one file by url, name"""
        request = self.get_request(url)

        open(self.save_dir + file, "wb").write(request.content)
        