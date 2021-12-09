from fly_behaviour import FlyBehaviour


class Duck:

    def __init__(self, fly_behaviour: FlyBehaviour):
        self._fly_behaivor = fly_behaviour

    def execute_fly(self):
        self._fly_behaivor.fly()

    def set_fly(self, fly_behaviour: FlyBehaviour):
        self._fly_behaivor = fly_behaviour

    def display():
        return "GENERAL"
