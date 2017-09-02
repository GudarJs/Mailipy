import os
import csv
import smtplib

from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import encoders
from os import listdir
from os.path import isfile, join
from optparse import OptionParser

from modules import markdown2

path = os.path.dirname(os.path.abspath(__file__)) + "/attachments/"

def sendmail(subject, message, to, attachments):
    fromaddr = options.email
    toaddr = to
    
    msg = MIMEMultipart()
    
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = subject
    
    body = message
    
    msg.attach(MIMEText(body, 'html'))
    
    for file_name in attachments:
        filename = file_name
        attachment = open(path + file_name, "rb")

        part = MIMEBase('application', 'octet-stream')
        part.set_payload((attachment).read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
        
        msg.attach(part)
    
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromaddr, options.password)
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()

def readCSVFile():
    emails = []
    with open(path + '../data.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            email = row[0]
            emails.append(email)
    return emails

def getAttachments():
    return [f for f in listdir(path) if isfile(join(path, f))]

def getBody():
    return markdown2.markdown_path(path + "../body.md")

def main():
    attachments = getAttachments()
    body = getBody()
    emails = readCSVFile()
    for email in emails:
        sendmail(options.subject, body, email, attachments)

if __name__ == "__main__":
    parser = OptionParser()
    parser.add_option("-s", "--subject", help="Email subject", default="")
    parser.add_option("-e", "--email", help="Your email", default="")
    parser.add_option("-p", "--password", help="Your email password", default="")
    (options, args) = parser.parse_args()
    
    if options.subject == "":
        parser.error("Please set a subject.")
    if options.email == "":
        parser.error("Please set your email.")
    if options.password == "":
        parser.error("Please set your email password.")

    main()
