import urllib, re

class InstagramPost(object):
    def __init__(self, link):
        self.uniqueName = link.split("/")[4]
        self.type = ""
        self.fileBytes = ""
        self.fileExtention = ""
        self.createObj(link)
     
    def getPageContentFromURL(self, URL):
        return urllib.urlopen(URL).read()
        
        
    def getPostTypeFromPageContent(self,pageContent):
        postType = re.compile(' <meta property="og:type" content="(.*)\" />').search(pageContent).group(1)
        
        if postType == "instapp:photo":
            return "photo"
            
        return postType
        
    def createObj(self, link):
        pageContent = self.getPageContentFromURL(link)
        self.type = self.getPostTypeFromPageContent(pageContent)
    
        if self.type == "photo":
            self.fileExtention = ".jpg"
            pattern = '\<meta property="og:image" content="(.*)\" />'
            
        if self.type == "video":
            self.fileExtention = ".mp4"
            pattern = '\<meta property="og:video" content="(.*)\" />'

        
        fileURL = re.compile(pattern).search(pageContent).group(1)
        self.fileBytes = urllib.urlopen(fileURL).read()
        
    def save(self, filePath):
        file = open(filePath + self.fileExtention, "wb")
        file.write(self.fileBytes)
        file.close()