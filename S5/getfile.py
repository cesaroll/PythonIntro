import ftplib
import sys

#Get argument (filename)
filename = sys.argv[1]

#connect ftp server
connect = ftplib.FTP("192.168.0.35")
connect.login("ftpuser", "start123")

#retrieve lines of file
connect.retrlines("RETR " + filename)
connect.quit()

