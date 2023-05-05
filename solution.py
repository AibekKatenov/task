from random import choices
import matplotlib.pyplot as plt

start_bigrams = {}
bigrams = {}
start_bigrams_probs = {}
bigrams_probs = {}
weights = []

def generate_name(bigrams_probs):
    names = list(bigrams_probs.keys())
    weights = [value for bigram, value in bigrams_probs.items()]
    name = choices(list(start_bigrams_probs.keys()), list(value for value in start_bigrams_probs.values()))[0]
    while True:
        letter = choices(names, weights)[0]
        name += letter[0]
        if letter[1] == '$':
            name += letter[1]
            break
        name += letter[1]
    return name
def showgraph(probs):
    x = list(probs.keys())
    y = list(probs.values())
    plt.bar(x, y)
    plt.xlabel('Bigrams')
    plt.ylabel('Probabilities')
    plt.show()


with open('names.txt', 'r') as f:
    names = f.read().splitlines()

for name in names:
    name = '^' + name.strip() + '$'
    for i in range(0, len(name) - 1):
        bigram = name[i] + name[i + 1]
        if i == 0:
            start_bigrams[bigram] = start_bigrams[bigram] + 1 if start_bigrams.get(bigram) else 1
            continue
        bigrams[bigram] = bigrams[bigram] + 1 if bigrams.get(bigram) else 1

for bigram, value in start_bigrams.items():
    start_bigrams_probs[bigram] = value / len(start_bigrams)
for bigram, value in bigrams.items():
    bigrams_probs[bigram] = value / len(bigrams)
# print(generate_name(bigrams_probs))
# showgraph(bigrams_probs)
# ЧТОБЫ ЗАПУСТИТЬ ФАЙЛ НАДО ПРОПИСАТЬ: py solution.py, для генерации имени разкомментируйте 47 строчку, для просмотра графика расскоментируйте 48 строчку