from collections import deque


def cards(first_player_cards, second_player_cards, n):
    first_pl_cards = deque(first_player_cards)
    second_pl_cards = deque(second_player_cards)
    i = 0
    time_limit = 10 ** 6
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


first_player_cards = list(map(int, input().split()))
second_player_cards = list(map(int, input().split()))

ans = cards(first_player_cards, second_player_cards, 9)
print(ans)
