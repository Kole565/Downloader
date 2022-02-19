class DownloadsCollection():
    
    """DownloadsCollection class

    Contains a list of downloads.
    The item in the list is an instance of the "Download" class.

    """

    def __init__(self, downloads=[]):
        """Get a list of downloads, save as a collection"""
        self.collection = downloads
    
    def get(self):
        """Return collection"""
        return self.collection
    
    def add(self, download):
        """Add "Download" at the end of the collection"""
        self.collection.append(download)
        