from random import randrange
from typing import List

from subject import Subject
from subscriber import Subscriber


class ConcreteSubject(Subject):
    _state = None
    _subscribers: List[Subscriber] = []

    def subscribe(self, subscriber: Subscriber) -> None:
        self._subscribers.append(subscriber)

    def remove(self, subscriber: Subscriber):
        self._subscribers.remove(subscriber)

    def notify(self):
        for subscriber in self._subscribers:
            subscriber.update(self)

    def some_function(self):
        print("\nSubject: I'm doing something important.")
        self._state = randrange(0, 10)
        print(f"Subject: My state has just changed to: {self._state}")
        self.notify()