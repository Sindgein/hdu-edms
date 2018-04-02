from itsdangerous import URLSafeTimedSerializer as utsr
from email.mime.text import MIMEText
from email.header import Header
from django.conf import settings
import base64
import re
import smtplib


class Token():
    def __init__(self, security_key):
        self.security_key = security_key
        self.salt = base64.encodestring(str.encode(security_key))

    def generate_validate_token(self, username):
        serializer = utsr(self.security_key)
        return serializer.dumps(username, self.salt)

    def confirm_validate_token(self, token, expiration=3600):
        serializer = utsr(self.security_key)
        return serializer.loads(token,
                                salt=self.salt,
                                max_age=expiration)

    def remove_validate_token(self, token):
        serializer = utsr(self.security_key)
        return serializer.loads(token, salt=self.salt)


token_confirm = Token(settings.SECRET_KEY)


def send_email(receiver, message):
    sender = '908998104@qq.com'
    code = 'qhxnofnroeeabcge'
    # receivers = ['fuermohao@outlook.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
    # 三个参数：第一个为文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码
    message = MIMEText(message, 'plain', 'utf-8')
    message['From'] = Header("CloudRiver", 'utf-8')
    message['To'] = Header("云江科技", 'utf-8')
    subject = 'CloudRiver用户注册验证'
    message['Subject'] = Header(subject, 'utf-8')

    try:
        server = smtplib.SMTP_SSL('smtp.qq.com', 465)
        # server.set_debuglevel(1)
        server.login(sender, code)
        server.sendmail(sender, receiver, message.as_string())
        print("邮件发送成功")
    except smtplib.SMTPException:
        print("Error: 无法发送邮件")


