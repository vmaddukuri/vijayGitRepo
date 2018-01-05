call_counter = 0


def demo():
    global call_counter
    call_counter += 1


demo()
demo()
demo()
print(call_counter)