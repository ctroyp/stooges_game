class GameObject:
    class_name = ''
    desc = ''
    objects = {}

    def __init__(self, name):
        self.name = name
        GameObject.objects[self.class_name] = self

    def get_desc(self):
        return self.class_name + '\n' + self.desc


class Goblin(GameObject):
    class_name = 'goblin'
    desc = 'A foul creature'

goblin = Goblin('Gobbly')


def examine(noun):
    if noun in GameObject.objects:
        return GameObject.objects[noun].get_desc()
    else:
        return f'There is no {noun} here.'


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

    print(len(command))
    if len(command) >= 2:
        noun_word = command[1]
        print(verb(noun_word))
    else:
        print(verb('nothing'))


def say(noun):
    return f'You said "{noun}".'


def poke(noun):
    return f'You poked {noun}!'


verb_dict = {
    'say': say,
    'poke': poke
}

if __name__ == '__main__':
    while True:
        run()
