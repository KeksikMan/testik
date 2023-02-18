import threading
import time


def mus():
    while True:
        print('mus')
        time.sleep(0.9)


def dis(arg1, arg2):
    while True:
        print('dis({}, {})'.format(repr(arg1), repr(arg2)))
        time.sleep(1.5)


def test(arg1, arg2):
    threads = (
        threading.Thread(target=mus),
        threading.Thread(target=dis, args=(arg1, arg2))
    )

    for t in threads:
        t.start()

    print('started')

    for t in threads:
        t.join()


test('arg1', 'arg2')