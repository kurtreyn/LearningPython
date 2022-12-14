import smtplib

my_email = "kurttempemailaddress@gmail.com"
password="loqrelthqzatelih"


with smtplib.SMTP("smtp.gmail.com") as connection:
	connection.starttls()
	connection.login(user=my_email, password=password)
	connection.sendmail(from_addr=my_email, to_addrs="pparker07041983@gmail.com", msg="Subject:Hello\n\nThis is the body of the email")
# connection.close()













