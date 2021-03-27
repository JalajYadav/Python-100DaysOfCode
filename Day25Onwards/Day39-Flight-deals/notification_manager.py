import os
# twilio###########################################
account_sid  = os.environ["<Your TwilioApi SID>"]
auth_token = os.environ["<Your TwilioApi AuthToken>"]
###################################################
my_email = os.environ["<The Admin Email ID>"]
email_password= os.environ["<The Admin Email Password>"]

###################################################
from twilio.rest import Client
import smtplib
class NotificationManager:
    def send_message(self,text):
        client = Client(account_sid, auth_token)

        message = client.messages \
            .create(
            body=f"{text}",
            from_=os.environ['Twilio Provided Temp Number'],
            to=os.environ['Your Registered Mobile Number for Testing']
        )

        print(message.sid)

    def send_emails(self,text,receivers_list):
        for subscriber in receivers_list:
            #print(subscriber['email'])
            with smtplib.SMTP('smtp.gmail.com', 587) as connection:
                connection.starttls()
                connection.login(user=my_email, password=email_password)
                connection.sendmail(
                    from_addr=my_email,
                    to_addrs=subscriber['email'],
                    msg=f"Subject:Cheap Flights\n\n{text}")




