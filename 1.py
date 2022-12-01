lines = [line.strip() for line in open('1.in', 'r').readlines()] + ['']

elf = 1
calories_acc = 0
calories_per_elf = {}

for l in lines:
    if l == '':
        calories_per_elf[elf] = calories_acc
        elf += 1
        calories_acc = 0
        continue
    calories_acc += int(l)

print(calories_per_elf)

elf_with_most_calories = max(calories_per_elf, key=calories_per_elf.get)

print(elf_with_most_calories, calories_per_elf[elf_with_most_calories])

highest_calories = sorted(calories_per_elf.items(), key=lambda x: x[1], reverse=True)[:3]
print(sum([calories[1] for calories in highest_calories]))