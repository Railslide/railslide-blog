Title: TG:HACK 2020 Writeup - A game of keys
Date: 2020-04-18
Tags: ctf, reverse
Slug: tghack-2020-writeup-a-game-of-keys
Summary: During Easter I played the TG:HACK 2020 CTF. Here' is my writeup for the _A game of keys_ challenge.

> Download this file and get the flag. You will also need this wordlist.

The provided files are a python compiled file (keygame.pyc) and a txt file with a list of gibberish words (wordlist.txt). The wordlist didn't seem very interesting, so I proceeded to decompile the python file

    :::bash
    $ uncompyle6 keygame.pyc > keygame.py

And had a look at the source code

    :::python
    import base64
    from itertools import cycle

    class myGame:

        def __init__(self, xdim=4, ydim=4):
            self.x = xdim
            self.y = ydim
            self.matrix = []
            for i in range(self.x):
                row = []
                for j in range(self.y):
                    row.append(0)

                self.matrix.append(row)

        def make_keys(self, *args, **kwargs):
            words = []
            with open('wordlist.txt') as (f):
                for line in f:
                    words.append(line.strip())

                for i in range(self.x):
                    for j in range(self.y):
                        self.matrix[j][i] = words[(i + j)]

            keyArray = []
            keyArray.append(self.matrix[args[0]][args[1]])
            keyArray.append(self.matrix[args[2]][args[3]])
            key = ''
            for k in keyArray:
                key = key.strip() + str(k).strip()

            print(key)
            return key

        def checkdata(self, key):
            f = base64.b64decode('NSYDUhoVWQ8SQVcOAAYRFQkORA4FQVMDQQ5fQhUEWUYMDl4MHA==')
            data = f.decode('ascii')
            c = ''.join((chr(ord(c) ^ ord(k)) for c, k in zip(data, cycle(key))))
            print('%s ^ %s = %s' % (data, key, c))


    if __name__ == '__main__':
        mgame = myGame(25, 25)
        x = input('input a number: ')
        y = input('input a number: ')
        x1 = input('input a number: ')
        y1 = input('input a number: ')
        data = mgame.make_keys(int(x), int(y), int(x1), int(y1))
        mgame.checkdata(data)

My take from it was that the programs takes four inputs and uses them for creating a key based on a matrix and on the wordlist. If the resulting key is the correct one, the `checkdata` function is going to print out the flag.

Running the program confirmed my theory

    :::bash
    $ python keygame.py
    input a number: 1
    input a number: 1
    input a number: 1
    input a number: 1
    aa0caa0c
    5&RYAW   DASA_BYF
                               ^
                                 ^ aa0caa0c = TG31{tils gmag!vhotmd c` oo!tei%mono}

Now, how to figure out what are the correct inputs? The sources shows that the game is created with a 25x25 matrix (`mgame = myGame(25, 25)`) and since the inputs are used as indexes for the matrix, any input greater than 24 should be invalid.

A quick run of the program confirmed this theory as well

    :::bash
    $ python keygame.py
    input a number: 25
    input a number: 25
    input a number: 25
    input a number: 25
    Traceback (most recent call last):
      File "keygame.py", line 56, in <module>
        data = mgame.make_keys(int(x), int(y), int(x1), int(y1))
      File "keygame.py", line 34, in make_keys
        keyArray.append(self.matrix[args[0]][args[1]])
    IndexError: list index out of range

So, I needed a way to test all the possible combinations of four inputs ranging from 0 to 24 and it turned out that python has a built-in way for doing just that. Enter `itertools.products`

    :::python
    import itertools
    from keygame import myGame

    inputs = [range(0, 25), range(0, 25), range(0, 25), range(0, 25)]
    possibilities = [p for p in itertools.product(*inputs)]

    mgame = myGame(25, 25)

    for p in possibilities:
        data = mgame.make_keys(*p)
        result = mgame.checkdata(data)
        if result.startswith('TG20{'):
            print(result, p)

I commented out the `print` statements from keygame.py to reduce the noise, and then waited for my script to spit out the flag

    :::bash
    'TG20{this flag should be on teh moon}'



