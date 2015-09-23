import ftplib
import sys

filename = sys.argv[1]

connect = ftplib.FTP("192.168.0.35")
connect.login("ftpuser","start123")

file = open(filename, "rb")
connect.storbinary("STOR " + filename, file)
