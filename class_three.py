# itaretor 

for i in range(10):
    print(i)

# generator
def my_range(num):
    for i in range(num):
        yield i

for i in my_range(10):
    print(i)