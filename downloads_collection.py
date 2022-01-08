class DownloadsCollection():
    
    """DownloadsCollection class

    Contain a list of downloads.
    Item in list - instance of 'download' class.

    """

    def __init__(self, downloads=[]):
        """Get list of downloads, save as collection"""
        self.collection = downloads
    
    def __call__(self):
        return self.get()
    
    def get(self):
        return self.collection
    
    def add(self, download):
        self.collection.append(download)
        