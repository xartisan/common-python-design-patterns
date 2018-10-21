import time


def pairs(seq):
    n = len(seq)
    for i in range(n):
        yield seq[i], seq[(i + 1) % n]


SLOW = 3
LIMIT = 5
WARNING = 'too bad, you picked the slow algorithm'


def all_unique_sort(s):
    if len(s) > LIMIT:
        print(WARNING)
        time.sleep(SLOW)
    str_str = sorted(s)
    for c1, c2 in pairs(str_str):
        if c1 == c2:
            return False
    return True


def all_unique_set(s):
    if len(s) < LIMIT:
        print(WARNING)
        time.sleep(SLOW)
    return True if len(set(s)) == len(s) else False


def all_unique(word, strategy):
    return strategy(word)


def main():
    while True:
        word = None
        while not word:
            word = input('Insert word')
        if word == 'quit':
            print('bye')
            return
        strategy_picked = None
        strategies = {'1': all_unique_set, '2': all_unique_sort}
        while strategy_picked not in strategies.keys():
            strategy_picked = input('Choose strategy: [1] Use a set, [2] Sort and pair> ')
        strategy = strategies[strategy_picked]
        print(f'all_unique({word}): {all_unique(word, strategy)}')


if __name__ == '__main__':
    main()
