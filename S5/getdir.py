import ftplib

connect = ftplib.FTP("192.168.0.35")
connect.login("ftpuser", "start123")
data = []
connect.dir(data.append)
connect.quit()

for line in data:
    print(line)