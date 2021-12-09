from abc import ABC, abstractmethod


class FlyBehaviour(ABC):
    @abstractmethod
    def fly(self):
        pass


class FlyWithWings(FlyBehaviour):
    def fly(self):
        print("FLy with wings")


class NoFly(FlyBehaviour):
    def fly(self):
        print("No fly")
