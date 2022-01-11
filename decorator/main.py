from notifications import Notification, EmailNotification
from decorator import NotifyFacebook, NotifySMS


def send_nofitications(notification: Notification):
    print(f"Sending : {notification.notify()}")


if __name__ == "__main__":
    notification = EmailNotification()
    print("Basic Notification")
    send_nofitications(notification)

    print("\n")

    fb_notification = NotifyFacebook(notification)
    sms_notification = NotifySMS(fb_notification)

    print("Call All notifications")
    print(sms_notification.notify())
