from duck import Duck
from fly_behaviour import FlyWithWings, NoFly

if __name__ == "__main__":
    duck = Duck(fly_behaviour=FlyWithWings())
    duck.execute_fly()
    duck.set_fly(NoFly())
    duck.execute_fly()
