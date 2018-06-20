import vk
import time


def spam3():
    while True:
        for i in range(1, 169):
            api.messages.send(user_id=72917966, attachment="photo-109980138_456239133")
            time.sleep(10)


session = vk.Session(
    access_token='your long accsess token ^_^')
api = vk.API(session)
spam3()
# title()

# lst = list(input().split())
# max = int(input())
# spam(lst, max)
