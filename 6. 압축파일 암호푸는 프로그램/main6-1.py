import itertools

passwd_string = "012345789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

for len in range(1,4):
    to_attempt = itertools.product(passwd_string, repeat=len)
    for attempt in to_attempt:
        password = ''.join(attempt)
        print(password)