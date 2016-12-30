import subprocess

class Mail():
	def __init__(self, name, from_email, to_email, subject, message):
		self.name = name
		self.from_email = from_email
		self.to_email = to_email
		self.subject = subject
		self.message = message

	def send(self):
		ps_echo = subprocess.Popen(('echo', ('From: {0} \n' + self.message).format(self.from_email)),
		 stdout=subprocess.PIPE)
		ps_mail = subprocess.Popen(('mail', '-s', self.subject, self.to_email), stdin=ps_echo.stdout)
