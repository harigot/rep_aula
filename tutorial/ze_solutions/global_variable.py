day = 5


def foo():
    set_day(1)
    bar()
    return day


def bar():
    print(get_day())


def get_day():
    global day
    return day


def set_day(value):
    global day
    day = value


foo()
