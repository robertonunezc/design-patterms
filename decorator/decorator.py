from notifications import Notification


class Decorator(Notification):
    """
    This class is the base to create the DECORATOR pattern design
    We need to hold a reference of the base object and all the new
    or specific behaviours must implement this class.
    THis class just call the interface methods
    """
    _notification: Notification = None

    def __init__(self, notification: Notification):
        self._notification = notification

    @property
    def notification(self):
        return self._notification

    def notify(self):
        return self._notification.notify()
        

class NotifyFacebook(Decorator):
    """
    This is a specific implementation that can be attached to the basic function
    """
    def notify(self):
        return f"{self._notification.notify()} + notify Facebook"

        
class NotifySMS(Decorator):
    """
    This is a specific implementation that can be attached to the basic function
    """
    def notify(self):
        return f"{self._notification.notify()} + notify SMS"
