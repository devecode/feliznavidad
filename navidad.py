from random import choice
from random import random
import base64
from time import sleep 

def progreso(percent=0, width=205):
    left = width * percent // 100
    right = width - left
    print ('\r[', '#' * left, ' ' * right, ']',
            f'{percent:.0f}%',
            sep='', end='', flush=True)

for i in range(101):
    progreso(i)
    sleep(0.1)
def main():
    SIZE = 21
    print(makeTree(SIZE))
    foo = "wqFGRUxJWiBOQVZJREFEIExFUyBERVNFQSBKUkNPREUh"
    print(base64.b64decode(foo))
 
def makeTree(size):
    prob_gr = 0.6
    colours = [31, 33, 34, 35, 36, 37]
    decs = ['@', '&', '*', chr(169), chr(174)]
    blink_col = "\033[5;{0}m{1}\033[0m"
    leaf = "\033[32m#\033[0m"
    width = 1
    tree = "\n{}*\n".format(' ' * (size))
    for pad in range(size - 1, -1, -1):
        width += 2
        temp = ""
        for j in range(width):
            if random() < prob_gr:
                temp += leaf
            else:
                temp += blink_col.format(choice(colours), choice(decs))
        tree += "{0}{1}\n".format(' ' * pad, temp)
    return tree + "{0}{1}\n".format(' ' * (size - 1), "000") * 2
 
if __name__ == "__main__":
    main()