import random 

with open('input1.txt', 'w') as f :
    n = random.randint(6*10**5, 10**6)
    f.writelines(str(n) + "\n")
    prev = random.uniform(0, 10**9)
    for i in range(0, 10**6) :
        prev = random.uniform(prev, prev + 1000000000)
        f.write(str("{:.7f}".format(prev)) + " ")

with open('input2.txt', 'w') as f :
    n = random.randint(6*10**5, 10**6)
    f.writelines(str(n) + "\n")
    prev = random.uniform(0, 10**9)
    for i in range(0, 10**6) :
        prev = random.uniform(prev-1000000000, prev)
        f.write(str("{:.7f}".format(prev)) + " ")

for i in range(3, 7) :
    name = f"input{i}.txt"
    with open(name, 'w') as f :
        n = random.randint(6*10**5, 10**6)
        f.writelines(str(n) + "\n")
        for i in range(0, 10**6) :
            f.write(str("{:.7f}".format(random.uniform(-10**18, 10**18))) + " ")

for i in range(7, 11) :
    name = f"input{i}.txt"
    with open(name, 'w') as f :
        n = random.randint(6*10**5, 10**6)
        f.writelines(str(n) + "\n")
        for i in range(0, 10**6) :
            f.write(str(random.randint(-10**18, 10**18)) + " ")