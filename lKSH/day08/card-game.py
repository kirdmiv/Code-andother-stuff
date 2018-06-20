from collections import deque


def cards(first_player_cards, second_player_cards, n):
    first_pl_cards = deque(first_player_cards)
    second_pl_cards = deque(second_player_cards)
    i = 0
    time_limit = 2 * (10 ** 5)
    while i <= time_limit:
        if len(first_pl_cards) == 0:
            return 'second ' + str(i)
        if len(second_pl_cards) == 0:
            return 'first ' + str(i)
        first_card = first_pl_cards.popleft()
        second_card = second_pl_cards.popleft()
        if first_card == 0 and second_card == n:
            first_pl_cards.append(first_card)
            first_pl_cards.append(second_card)
        elif second_card == 0 and first_card == n:
            second_pl_cards.append(first_card)
            second_pl_cards.append(second_card)
        elif first_card > second_card:
            first_pl_cards.append(first_card)
            first_pl_cards.append(second_card)
        else:
            second_pl_cards.append(first_card)
            second_pl_cards.append(second_card)
        i += 1
    return 'botva'


cards_in = open('input.txt', 'r')
cards_out = open('output.txt', 'w')

n = int(cards_in.readline())
first_player_cards = list(map(int, cards_in.readline().split()))
second_player_cards = list(map(int, cards_in.readline().split()))
cards_in.close()

ans = cards(first_player_cards, second_player_cards, n - 1)
print(ans, file=cards_out)
cards_out.close()
