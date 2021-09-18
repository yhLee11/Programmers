a='abc'
b='abd'
a=list(a)
b=list(b)
for i in range(3):
    if a[i]==b[i]:
        print(a[i])
