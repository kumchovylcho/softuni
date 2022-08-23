class Email:
    def __init__(self, sender, receiver, content):
        self.is_sent = False
        self.sender = sender
        self.receiver = receiver
        self.content = content

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"


emails = []
email_info = input()
while email_info != "Stop":
    email_info = email_info.split()
    sender = email_info[0]
    receiver = email_info[1]
    content = email_info[2]
    email = Email(sender, receiver, content)
    emails.append(email)
    email_info = input()

send_emails = [int(index) for index in input().split(", ")]
for email in send_emails:
    emails[email].send()

for email in emails:
    print(email.get_info())