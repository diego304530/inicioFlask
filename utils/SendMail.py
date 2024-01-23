import smtplib
from email.message import EmailMessage
from Config.config import Config


class SendMail():

    def __init__(self):

        self.msg = EmailMessage()
        self.passEmail = Config.getConfigJson()["passEmail"]
        self.userEmail = Config.getConfigJson()["userEmail"]
        self.smtpServer = Config.getConfigJson()["smtpServer"]
        self.smtpPort = Config.getConfigJson()["smtpPort"]

    def sendMail(self):
        mail = smtplib.SMTP(self.smtpServer, self.smtpPort)
        mail.starttls()
        mail.ehlo()
        mail.login(self.userEmail, self.passEmail)
        mail.send_message(self.msg)
        mail.quit()
        self.msg = EmailMessage()

    def formatMessage(self, dataEmail):
        self.msg.set_content(dataEmail['contenido'])
        self.msg['Subject'] = dataEmail['asunto']
        self.msg['From'] = self.userEmail
        self.msg['to'] = dataEmail['destinatarios']
        self.sendMail()
        return {'msj': "mensaje enviado correctamente"}
