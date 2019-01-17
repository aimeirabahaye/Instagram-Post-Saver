# encoding: utf-8
from Tkinter import *
import urllib, re, Tkconstants, tkFileDialog
from InstagramPost import *
import os

global link
         
def postSaver():
    try:
        link = postLinkTextBox.get()
        postURL = link
        
        post = InstagramPost(link)
        
        root.filename = tkFileDialog.asksaveasfilename(initialdir = "/",title = "Select file",filetypes = (("JPEG files","*.jpg"),("all files","*.*")))
        post.save(root.filename)
    except IOError:
        print "error"

def batchDownload():
    #open textfile
    filePath = tkFileDialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("Text files","*.txt"),("all files","*.*")))
    file = open(filePath, "r").readlines()
    #for each textline
    dir = os.path.dirname(filePath)
    newPicCount = 0
    for link in file:

        post = InstagramPost(link)
        
        #save if file doesnt already exist
        path = dir + '/batch/' + post.uniqueName
        imgExist = os.path.isfile(path + ".mp4")
        vidExist = os.path.isfile(path + ".jpg")
        if not (imgExist or vidExist):
            post.save(path)
            newPicCount += 1
 
        else:
            print "%s already exists" % (post.uniqueName)
    
    print ("Done %s new picture(s), %s total") % (newPicCount, len(file))
            
root = Tk()
root.title("Instagram Post Saver")
root.geometry("350x130")
root.resizable(0, 0)
linkTextBox = Label(root, text="Instagram Post Link : ")
linkTextBox.pack()
postLinkTextBox = Entry(root)
postLinkTextBox.pack()
root.iconbitmap('ico.ico')
downloadButton = Button(root, text= "Download post", width=18, command = postSaver)
downloadButton.pack()
linkTextBox = Label(root, text="or")
linkTextBox.pack()
batchDownloadButton = Button(root, text= "Batch download", width=18, command = batchDownload)
batchDownloadButton.pack()

root.mainloop()
