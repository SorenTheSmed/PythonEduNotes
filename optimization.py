

def generateNumbers():
    for a in range(500000):
        yield a


genResults = generateNumbers()

print(next(generateNumbers()), next(generateNumbers()), next(generateNumbers()))