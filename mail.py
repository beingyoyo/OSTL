import smtplib
server=smtplib.SMTP('smtp.gmail.com',587)
server.ehlo()
server.starttls()
server.login("senders mail","senders password")
msg="Hello!"
server.sendmail("senders mail","receivers mail",msg)
server.close()
