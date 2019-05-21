class GameObject:
    class_name = ''
    desc = ''
    objects = {}

    def __init__(self, name, desc=''):
        self.class_name = name
        self.desc = desc
        GameObject.objects[self.class_name] = self

    def get_desc(self):
        return f'{self.class_name}\n{self.desc}'


class Stooge(GameObject):
    def __init__(self, name, desc='Short and just another stooge'):
        self.class_name = 'stooge'
        self.health = 3
        self._desc = desc
        super().__init__(name, desc)

    @property
    def desc(self):
        if self.health >= 3:
            return self._desc
        elif self.health == 2:
            health_line = 'He has a wound on its knee.'
        elif self.health == 1:
            health_line = 'He is crippled!'
        elif self.health <= 0:
            health_line = 'He is no longer with us.'
        return f'{self._desc}\n{health_line}'

    @desc.setter
    def desc(self, value):
        self._desc = value

moe = Stooge('Moe', 'He\'s the boss-short, bowl-cut hair, and grumpy')
larry = Stooge('Larry', 'He\'s has an endless supply of hair when '
                'you pull on it')
curly = Stooge('Curly', 'He\'s not the smartest stooge on the stage')
shemp = Stooge('Shemp', 'He\'s the tall goofy stooge that loves '
                'jumping beans')

def run():
    command = input(' -> ').split()
    verb_word = command[0].lower()

    if verb_word in verb_dict:
        verb = verb_dict[verb_word]
    elif verb_word.lower() in {'q', 'quit'}:
        print('Thanks for playing, ya stooge!')
        exit(0)
    else:
        print(f'Unknown verb {verb_word}')
        return

    if len(command) >= 2:
        noun_word = command[1]
        print(verb(noun_word))
    else:
        print(verb('nothing'))


def say(noun):
    return f'You said "{noun}".'

def poke(noun):
    return f'You poked {noun}!'

def hit(noun):
    if noun in GameObject.objects:
        thing = GameObject.objects[noun]
        if type(thing) == Stooge:
            thing.health = thing.health - 1
            if thing.health <= 0:
                msg = "You may have killed a stooge!"
            else:
                msg = f'You hit {thing.class_name}'
    else:
        msg = f'There is no {noun} here.'
    return msg

def examine(noun):
    if noun in GameObject.objects:
        return GameObject.objects[noun].get_desc()
    else:
        return f'There is no {noun} here.'

verb_dict = {
    'say': say,
    'poke': poke,
    'hit': hit,
    'examine': examine
}

if __name__ == '__main__':
    while True:
        run()
