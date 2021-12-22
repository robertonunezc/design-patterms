from subject import Subject
from subscriber import Subscriber


class ConcreteSubscriber(Subscriber):
    def update(self, subject: Subject):
        if subject._state < 3:
            print("ConcreteObserverA: Reacted to the event")


class OtherConcreteSubscriber(Subscriber):
    def update(self, subject: Subject):
        if subject._state > 3:
            print("OtherConcreteSubscriber: Reacted to the event")