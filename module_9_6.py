def all_variants(text):
    n = len(text)
    for i in range(1 << n):
        variant = ""
        for j in range(n):
            if (i >> j) & 1:
                variant += text[j]
        yield variant
a = all_variants("abc")
for i in a:
    print(i)
