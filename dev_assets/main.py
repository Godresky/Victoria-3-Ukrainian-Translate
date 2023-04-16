file = open('C:/Users/andri/OneDrive/Documents/Paradox Interactive/Victoria 3/mod/Український переклад/dev_assets/стан_перекладу.txt', 'r', encoding='utf-8')

translated = 0
original = 0
i = 0
for line in file.readlines():
    i += 1
    if i == 1:
        continue
    line2 = line.split(' | ')
    s2 = line2[1].split('/')
    if (s2[0] == "100%" or line2[0] == "names_l_english.yml" or line2[0] == "names_l_english.yml"):
        continue

    translated += int(s2[0])
    original += int(s2[1])

percent = translated / original * 100

print(f"Translated: {translated}\nOriginal: {original}\nPercent: {percent}%")