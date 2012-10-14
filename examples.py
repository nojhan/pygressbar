import sys
import random
import time

try:
    import urllib2 as urllib
except:
    import urllib.request


from pygressbar import (SimpleProgressBar,
                        CustomProgressBar,
                        SimplePercentProgressBar,
                        SimpleAnimatedProgressBar,
                        SimpleColorBar)


def show_simple_animation():
    bar = SimpleProgressBar()
    bar.show_progress_bar()
    while(not bar.completed()):
        time.sleep(0.1)
        bar.increase(5)
        bar.show_progress_bar()


def show_custom_animation():
    total = 50
    fill_char = '|'
    empty_char = '_'
    head = None
    left_limit = ''
    right_limit = ''
    scale_start = 0
    scale_end = 1000
    bar = CustomProgressBar(length=total,
                            left_limit=left_limit,
                            right_limit=right_limit,
                            head_repr=head,
                            empty_repr=empty_char,
                            filled_repr=fill_char,
                            start=0,
                            scale_start=scale_start,
                            scale_end=scale_end)
    bar.show_progress_bar()
    while(not bar.completed()):
        time.sleep(0.03)
        bar.increase(10)
        bar.show_progress_bar()


def show_simple_percent_animation():
    bar = SimplePercentProgressBar()
    bar.show_progress_bar()
    while(not bar.completed()):
        time.sleep(0.3)
        bar.increase(random.randint(1, 10))
        bar.show_progress_bar()


def show_head_animation():

    bar = SimpleAnimatedProgressBar(speed=1000)
    bar.hide_cursor()
    bar.show_progress_bar()
    bar.increase(50)

    while(not bar.completed()):

        if random.randint(1, 500000) == random.randint(1, 500000):
            bar.increase(50)

        bar.show_progress_bar()

    bar.show_cursor()


def show_up_down_animation():
    bar = SimplePercentProgressBar()
    bar.show_progress_bar()

    up = False

    for i in range(5):

        if up:
            up = False
            bar.decrease(1)
        else:
            up = True
            bar.increase(1)

        while(bar.progress > 0 and bar.progress < 100):
            time.sleep(0.1)
            factor = random.randint(1, 10)
            if up:
                bar.increase(factor)
            else:
                bar.decrease(factor)
            bar.show_progress_bar()


def show_color_animation():
    bar = SimpleColorBar()
    bar.show_progress_bar()
    while(not bar.completed()):
        time.sleep(0.2)
        bar.increase(1)
        bar.show_progress_bar()


def download_file():
    big_file_url = "https://gist.github.com/raw/3885120/803c00" +\
                   "b809c7a9c4a44626320374d18933b63b48/big.txt"

    # Download the file
    if sys.version_info[0] == 3:
        f = urllib.request.urlopen(big_file_url)
    else:
        f = urllib.urlopen(big_file_url)

    # Get the total length of the file
    scale = int(f.headers["content-length"])
    chunk_size = 500

    bar = CustomProgressBar(length=50,
                            left_limit='[',
                            right_limit=']',
                            head_repr=None,
                            empty_repr=' ',
                            filled_repr='|',
                            start=0,
                            scale_start=0,
                            scale_end=scale)

    print("Downloading a big txt file: ")

    print_flag = 0
    # Load all the data chunk by chunk
    while not bar.completed():
        f.read(chunk_size)
        bar.increase(chunk_size)

        # Don't print always
        if print_flag == 100:
            bar.show_progress_bar()
            print_flag = 0
        else:
            print_flag += 1

    bar.show_progress_bar()
    print("")
    print("Finished :)")

if __name__ == "__main__":
    print("Simple bar: ")
    show_simple_animation()
    print("")

    print("Custom bar: ")
    show_custom_animation()
    print("")

    print("Animated head bar: ")
    show_head_animation()
    print("")

    print("Simple with percent bar: ")
    show_simple_percent_animation()
    print("")

    print("Increase and decrease bar: ")
    show_up_down_animation()
    print("")

    print("Color bar: ")
    show_color_animation()
    print("")

    download_file()
    print("")
