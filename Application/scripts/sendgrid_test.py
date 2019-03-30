import sendgrid
from sendgrid.helpers.mail import *

def sendmail():
    try:
        sg = sendgrid.SendGridAPIClient(apikey="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")
        from_email = Email('moonkl54@gmail.com')
        to_email = Email('sysmoon@gmail.com')
        subject = "moonid store - new printing #{}".format('123')
        content = Content("text/plain", 'test mail by sysmoon')
        mail = Mail(from_email, subject, to_email, content)
        response = sg.client.mail.send.post(request_body = mail.get())
        print('status_code:', response.status_code)
        print('body:', response.body)
        print('headers:', response.headers)
    except IOError as e:
        return e

if __name__ == '__main__':
    sendmail()
    print('main call')