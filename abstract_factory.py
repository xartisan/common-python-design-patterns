class Frog:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'<Frog({self.name})>'

    def interact_with(self, obstacle):
        act = obstacle.action()
        msg = f'{self} the Frog encounters {obstacle} and {act}'
        print(msg)


class Bug:
    def __str__(self):
        return 'a bug'

    def action(self):
        return 'eats it'


class FrogWorld:
    def __init__(self, name):
        print(self)
        self.player_name = name

    def make_character(self):
        return Frog(self.player_name)

    def make_obstacle(self):
        return Bug()

    def __repr__(self):
        return '\n\n\t------ Forg World ------'


class Wizard:
    def __init__(self, name):
        self.name = name

    def interact_with(self, obstacle):
        action = obstacle.action()
        msg = f'{self} the Wizard battles against{obstacle} and {action}'
        print(msg)

    def __repr__(self):
        return f'<Wizard({self.name})'


class Ork:
    def action(self):
        return 'kills it'

    def __repr__(self):
        return 'an evil ork'


class WizardWorld:
    def __init__(self, name):
        self.player_name = name

    def make_character(self):
        return Wizard(self.player_name)

    def make_obstacle(self):
        return Ork()

    def __repr__(self):
        return '\n\n\t------ Wizard World ------'


class GameEnv:

    def __init__(self, factory):
        self.hero = factory.make_character()
        self.obstacle = factory.make_obstacle()

    def play(self):
        self.hero.interact_with(self.obstacle)


def validate_age(name):
    try:
        age = input(f'Welcome {name}. How old are you? ')
        age = int(age)
    except ValueError as e:
        print(f"Age {age} is invalid, please try again...")
        return False, age
    return True, age


def main():
    name = input("Hello. What's your name ?")
    valid_age = False
    while not valid_age:
        valid_age, age = validate_age(name)
    game = FrogWorld if age < 18 else WizardWorld
    env = GameEnv(game(name))
    env.play()


if __name__ == '__main__':
    main()
