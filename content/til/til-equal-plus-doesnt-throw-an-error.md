Title: TIL: =+ doesn't throw an error
Date: 2024-12-04
Tags: TIL, python
Slug: til-equal-plus-doesnt-throw-an-error
Summary: Mistyping `=+` instead of `+=` can lead to some sneaky bugs


A while ago I decided to switch to the Ansi (aka US) layout for my keyboard. The process was fairly painless: I adapted to the new movements fairly quickly and typing symbols has become way simpler. One of the things I still struggle though is `=+`, as in all the layouts I have used in the past the key combination was the opposite if the US one, i.e. `=` would require me to press shift and `+` wouldn't. So it's not uncommon for me to hit `+` instead of `=` and vice versa, which led me to stumble on an interesting bug.

In python you can increment a variable by using the shorthand `+=`, i.e.

```python
foo = 5
foo += 1
print(foo)  # foo is now 6
```

Now, due to my layout switch, `+=` has a high chance of mistyping for me. However, I had always assumed that either the interpreter or my editor would have screamed at me if I were to type it in reverse. That turned out not to be the case.

```python
foo = 5
foo =+ 1  # note the typo
# I was expecting an error here, but nope.
print(foo)  # foo is now 1
```

Basically, python considers `foo =+ 1` the same as `foo = +1`. And that explains why there was no error and why the output of my script was completely wrong. The dark side of it is that the typo is not the easiest one to spot, which might lead to quite some confusion and debugging time (as it happened to me today).

Oh well, today I learned. And from now on I'll know what to double check for.
