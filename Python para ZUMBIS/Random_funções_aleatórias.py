import random

random.randint(1, 100)

nomes = "ze lia pedro luiz".split()
random.choice(nomes)
random.shuffle(nomes)

print(nomes)


random.sample(range(100), 10)
