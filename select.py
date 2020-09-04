import csv
import random

with open('reads.csv', 'r') as infile:
    reader = csv.reader(infile)
    reading_list = [row for row in reader]

pool = []
already_read = []

for row in reading_list:
    multiplier = int(row[0])
    title = row[1]

    if not multiplier:
        already_read.append(title)
        continue

    for i in range(multiplier):
        pool.append(title)

def select_random():
    selection = random.choice(pool)
    if random.random() < .05 : # 1 / 20 chance of rereading something
        selection = random.choice(already_read)
    return selection

choices = [select_random() for x in range(3)]

print('CHOICES:')
for ch in choices:
    print(ch)
