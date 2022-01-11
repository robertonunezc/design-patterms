class Notification():
    """
    This is the interface with the common behaviour
    """
    def notify(self):
        """This is an interface"""
        pass


class EmailNotification(Notification):
    """
    This class implement the basic behaviour, this behaviour always must be executed
    """
    def notify(self):
        return "Email notification"


        