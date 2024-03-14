from tasks import add

s=add.delay(90,34)
print(s.get())