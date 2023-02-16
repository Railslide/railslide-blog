Title: TIL: strip does not do what I think it does
Date: 2023-02-15
Tags: TIL, python
Slug: til-strip-does-not-do-what-i-think-it-does
Summary: It turns out I have been using it wrong for all this time!

I always thought `strip`, `lstrip` and `rstrip` would simply match and strip whatever string it was passed to them. However, it turns out that's not how they work.

```python
"Hello world".strip("hel") 
# Expected outcome: 'lo world'
'o world'  # Actual outcome
```

What `strip`, `lstrip` and `rstrip` actually do is to remove **any** of the specified characters until a non-matching character is encountered. So in the example above, the second `l` still matches the provided set of chars and hence gets removed. 

I guess most of the time I just got lucky and never stumbled on the actual behavior. But what I should have used in most of the cases is actually `removeprefix` and `removesuffix`, as the docs suggest.

Today I learned.

## References

- [Docs for `strip`](https://docs.python.org/3/library/stdtypes.html?highlight=strip#str.rstrip) 
- [Docs for `lstrip`](https://docs.python.org/3/library/stdtypes.html?highlight=strip#str.lstrip) 
- [Docs for `rstrip`](https://docs.python.org/3/library/stdtypes.html?highlight=strip#str.rstrip) 
