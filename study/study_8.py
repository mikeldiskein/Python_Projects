letters = {
    'J': '11',
    'Q': '12',
    'K': '13',
    'A': '14'
}


def check_player(cards):
    values = [card[0] for card in cards]
    suits = [card[1] for card in cards]
    counter = {}
    for val in values:
        counter[val] = counter.get(val, 0) + 1

    if cards[0][0] == '10' and cards[1][0] == '11' and cards[2][0] == '12' and cards[3][0] == '13' and cards[4][0] == '14':
        if len(set(suits)) == 1:
            return 9

    values.sort()
    if values[0] + 1 == values[1] and values[0] + 2 == values[2] and values[0] + 3 == values[3] and values[0] + 4 == values[4]:
        suits = set(card[1] for card in cards)
        if len(suits) == 1:
            return 8
        else:
            return 4

    if 4 in counter.values():
        return 7

    if 3 in counter.values() and 2 in counter.values():
        return 6

    if len(set(suits)) == 1:
        return 5

    if 3 in counter.values():
        return 3

    if len(list(filter(lambda x: x == 2, counter.values()))) == 2:
        return 2

    if 2 in counter.values():
        return 1

    return 0


with open('p054_poker.txt', 'r', encoding='utf-8') as file:
    main_counter = 0
    for line in file.readlines():
        cards = line.split()
        for i in range(len(cards)):
            if cards[i][0] in 'JQKA':
                cards[i][0] = letters[cards[i][0]]
        a = cards[:5]
        b = cards[5:]
        p1, p2 = check_player(a), check_player(b)
        if p1 > p2:
            main_counter += 1
        elif p1 == p2:
            if p1 == 8:
                if sum(card[0] for card in a) > sum(card[0] for card in b):
                    main_counter += 1
            elif p1 == 7:
                counter_1 = {}
                values_1 = [card[0] for card in a]
                for val in values_1:
                    counter_1[val] = counter_1.get(val, 0) + 1
                for key, val in counter_1.items():
                    if val == 4:
                        p1_1 = key
                counter_2 = {}
                values_2 = [card[0] for card in b]
                for val in values_2:
                    counter_2[val] = counter_2.get(val, 0) + 1
                for key, val in counter_2.items():
                    if val == 4:
                        p2_1 = key
                if p1_1 > p2_1:
                    main_counter += 1
            elif p1 == 6:
                counter_1 = {}
                values_1 = [card[0] for card in a]
                for val in values_1:
                    counter_1[val] = counter_1.get(val, 0) + 1
                for key, val in counter_1.items():
                    if val == 3:
                        p1_1 = key
                    elif val == 2:
                        p1_2 = key
                counter_2 = {}
                values_2 = [card[0] for card in b]
                for val in values_2:
                    counter_2[val] = counter_2.get(val, 0) + 1
                for key, val in counter_2.items():
                    if val == 3:
                        p2_1 = key
                    elif val == 2:
                        p2_2 = key
                if p1_1 > p2_1:
                    main_counter += 1
                elif p1_1 == p2_1:
                    if p1_2 > p2_2:
                        main_counter += 1
            elif p1 == 5:
                values_1 = [card[0] for card in a]
                values_2 = [card[0] for card in b]
                p1_high = max(values_1)
                p2_high = max(values_2)
                while p1_high == p2_high:
                    values_1.remove(p1_high)
                    values_2.remove(p2_high)
                    p1_high = max(values_1)
                    p2_high = max(values_2)
                if p1_high > p2_high:
                    main_counter += 1
            elif p1 == 4:
                if sum(card[0] for card in a) > sum(card[0] for card in b):
                    main_counter += 1
            elif p1 == 3:
                pass

        elif p1 == p2 == 0:
            p1_high = max(card[0] for card in a)
            p2_high = max(card[0] for card in b)
            while p1_high == p2_high:
                a.remove(max(p1_high))
                b.remove(max(p2_high))
                p1_high = max([card[0] for card in a])
                p2_high = max([card[0] for card in b])
            if p1_high > p2_high:
                main_counter += 1






