import smtplib
#from email.mime.multipart import MIMEMultipart
#from email.mime.text import MIMEText

fromaddr = ''
toaddr = ''
text = 'test message sent from python'

username = 'cesaromar.lopez'
password = ''

#msg = MIMEMultipart()
#msg['From'] = fromaddr
#msg['To'] = toaddr
#msg['Subject'] = 'Test'
#msg.attach(MIMEText(text))

server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
#server.ehlo()
server.login(username, password)
#server.sendmail(fromaddr, toaddr, msg.as_string())
server.sendmail(fromaddr, toaddr, text)
server.quit()
