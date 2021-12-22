from abc import ABC, abstractmethod


class Subscriber(ABC):
    @abstractmethod
    def update(self, subject: "Subject"):
        pass

