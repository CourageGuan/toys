#-*- coding:utf-8 -*-
import smtplib
from email.mime.text import MIMEText

class MailSender(object):

	mail_server="smtp.ym.163.com"
	mail_username="reminder@gyh.me"
	mail_password="" #...
	server = None

	def __init__(self):
		self.server = self.init_server()

	def __del__(self):
		self.close_server()
	
	def init_server(self):
		try:
			server = smtplib.SMTP()
			#server.set_debuglevel(1)
			server.connect(self.mail_server)
			server.starttls()
			server.login(self.mail_username, self.mail_password)
			return server
		except Exception, e:
			print e
			return None
	
	def close_server(self):
		if self.server:
			self.server.close()
	
	def send_email(self, to_list, title, content):
		msg = MIMEText(content, 'plain', 'utf-8')
		msg["Accept-Charset"]="ISO-8859-1,utf-8"
		msg['Subject'] = title
		msg['From'] = self.mail_username
		msg['To'] = ";".join(to_list)
		try:
			self.server.sendmail(self.mail_username, to_list, msg.as_string())
			return True
		except Exception, e:
			print e
			return False
	
if __name__ == '__main__':

	ms = MailSender()

	mailto_list=["i@gyh.me"]
	if ms.send_email(mailto_list, 'title', 'content'):
		print 'Yes'
