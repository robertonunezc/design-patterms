from abc import ABC, abstractmethod

from subscriber import Subscriber


class Subject(ABC):
    @abstractmethod
    def subscribe(self, subscriber: Subscriber) -> None:
        """
        Attach the subscribers behavior to the subject
        :param subscriber:
        :return: NOne
        """
        pass

    @abstractmethod
    def remove(self, subscriber: Subscriber):
        """
        Remove a subscribers from the notification list
        :param subscriber:
        :return:
        """
    @abstractmethod
    def notify(self):
        """
        Notify to all subscribers
        :return:
        """