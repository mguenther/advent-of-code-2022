lines = [line.strip() for line in open('1.in', 'r').readlines()] + ['']

elf = 1
calories_acc = 0
calories_by_elf = {}

for line in lines:
    if line == '':
        calories_by_elf[elf] = calories_acc
        elf += 1
        calories_acc = 0
        continue
    calories_acc += int(line)

highest_calories = sorted(calories_by_elf.items(), key=lambda x: x[1], reverse=True)[:3]

print(calories_by_elf[max(calories_by_elf, key=calories_by_elf.get)])
print(sum([calories[1] for calories in highest_calories]))