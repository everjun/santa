import abc
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class BaseEmailSender(metaclass=abc.ABCMeta):
    config = None

    @abc.abstractmethod
    def send_message(self, to, message):
        pass

    def init_configuration(self, config):
        self.config = config


class ConsoleEmailSender(BaseEmailSender):
    def send_message(self, to, message):
        print("---------------------------------")
        print(f"Message to {to}")
        print(message)
        print("---------------------------------")

    def init_configuration(self, config):
        pass


class GoogleEmailSender(BaseEmailSender):
    def send_message(self, to, message):
        smtp_settings = self.config
        from_addr = smtp_settings['user']

        msg = MIMEText(message, 'plain', 'utf-8')
        msg['Subject'] = "Santa"
        msg['From'] = from_addr
        msg['To'] = to
        server = smtplib.SMTP(host=smtp_settings['host'], port=smtp_settings['port'])
        server.ehlo()
        server.starttls()
        server.login(smtp_settings['user'], smtp_settings['password'])
        server.sendmail(from_addr, [to], msg.as_string())
        server.quit()
