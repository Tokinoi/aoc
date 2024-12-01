first = []
second = []
with open('input', 'r') as file:
    temp = file.read().split('\n')
    print(temp)
for e in temp:
    a = e.split('   ')
    first.append(a[0])
    second.append(a[1])

first.sort()
second.sort()

# STEP 1

diff = 0

for i in range(len(first)):
  diff += abs(int(first[i])-int(second[i]))

print("STEP 1 : " + str(diff))

# STEP 2

compatibilite = 0

for i in first:
    ctn = 0
    for e in second:
        if i == e:
            ctn += 1
    compatibilite += int(i)*ctn

print("STEP 2 : " + str(compatibilite))


