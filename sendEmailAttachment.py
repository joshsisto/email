import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

# # comment implies that the field needs to be filled in

fromaddr = ""    # from email address
toaddr = ""      # destination email address
smtp_user = ""    # SMTP username used for authentication
smtp_pass = ""    # SMTP password used for authentication
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = ""    # subject

body = ""    # body
msg.attach(MIMEText(body, 'plain'))

filename = ""    # filename including extension
attachment = open(r"", "rb")    # e.g. (r"C:\pic\pic.jpg", "rb")

part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

msg.attach(part)

server = smtplib.SMTP('', 587)    # e.g. ('in-v3.mailjet.com', 587)
server.starttls()
server.login(smtp_user, smtp_pass)
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()
