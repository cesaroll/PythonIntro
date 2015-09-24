import urllib, os

def separator():
    print(" ")
    print(" ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ")
    print(" ")


os.system("cls")

#myurl = urllib.urlopen("http://google.com")
myurl = urllib.urlopen("http://www.profmcmillan.com")
print(myurl)
separator()

contents = myurl.readlines()

#Print all contents
print(contents)
separator()


#Print first line from contents
print(contents[0])
separator()

#header info
headerinfo = myurl.info()
print(headerinfo.getheader("date"))
separator()

#content type
print(headerinfo.getheader("content-type"))
separator()

