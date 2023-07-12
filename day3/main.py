import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    if n > 20 and n % 2 == 0:
        print('Not Weird')
    else:
        if n % 2 == 0 and 6 <= n <= 20:
            print('Weird')
        else:
            if n % 2 == 0 and 2 <= n <= 5:
                print('Not Weird')
            else:
                print('Weird')
