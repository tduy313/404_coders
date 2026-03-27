import sys
from time import sleep
import time
import os

os.system('cls')

def print_lyrics():
    lines = [
        ("Tháng tư có em ", 0.1),
        ("ở đây nhìn tôi mỉm cười...", 0.15),
        ("Những cánh hoa phai tàn thật nhanh", 0.055),
        ("em có bay xa, em có đi xa mãi", 0.15),
        ("Tháng tư đôi khi thật mong manh", 0.08),
        ("để mình nói ra những câu chân thật", 0.1),
    ]

    delays = [ 0.5, 1, 1 , 0.5 , 0.5, 0.3]

    for i, (line, char_delay) in enumerate(lines):
        for char in line:
            print(char, end='')
            sys.stdout.flush()
            sleep(char_delay)
        time.sleep(delays[i])
        print('')

print_lyrics()