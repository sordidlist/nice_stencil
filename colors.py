from fabulous import color


def bg_black(text):
    return color.bg256('black', text)


def black(text):
    return color.fg256('black', text)


def bg_green(text):
    return color.bg256('green', text)


def green(text):
    return color.fg256('green', text)


def bg_maroon(text):
    return color.bg256('maroon', text)


def maroon(text):
    return color.fg256('maroon', text)


def bg_olive(text):
    return color.bg256('olive', text)


def olive(text):
    return color.fg256('olive', text)


if __name__ == '__main__':
    print("{}\t{}".format(black("black"), bg_black("black")))
    print("{}\t{}".format(green("green"), bg_green("green")))
    print("{}\t{}".format(maroon("maroon"), bg_maroon("maroon")))
    print("{}\t{}".format(olive("olive"), bg_olive("olive")))
