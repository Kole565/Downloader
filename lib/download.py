class Download():
    
    """Download class
    
    Contain download data like url, file and etc.

    """

    def __init__(self, url, file_name):
        """Construct instance by url, file name"""
        self.url = url

        self.file_name = file_name
        self.file_format = url.split(".")[-1]

        self.file = "{0}.{1}".format(self.file_name, self.file_format)
