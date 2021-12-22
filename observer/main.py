from concrete_subject import ConcreteSubject
from concretes_subscribers import ConcreteSubscriber, OtherConcreteSubscriber

if __name__ == "__main__":
    subject = ConcreteSubject()

    subscriber_first = ConcreteSubscriber()
    subject.subscribe(subscriber_first)

    subscriber_second = OtherConcreteSubscriber()
    subject.subscribe(subscriber_second)

    subject.some_function()
    subject.some_function()

    subject.remove(subscriber_first)

    subject.some_function()