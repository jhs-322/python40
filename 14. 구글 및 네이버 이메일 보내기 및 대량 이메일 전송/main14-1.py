import smtplib
from email.mime.text import MIMEText

send_email = "jhsunny05@naver.com"
send_pwd = "hasun203110"
recv_email ="jhsunny05@naver.com"

smtp_name="smtp.naver.com"
smtp_port = 587

text = """
이 편지는 영국에서부터 시작되어
(이하생략)"""

msg = MIMEText(text)

msg['Subject'] = "이 편지를 발견한 당신은 즉시...더보기"
msg['From'] = send_email
msg['To'] = recv_email
print(msg.as_string())

s = smtplib.SMTP( smtp_name, smtp_port )
s.starttls()
s.login( send_email, send_pwd )
s.sendmail( send_email, recv_email, msg.as_string())
s.quit()