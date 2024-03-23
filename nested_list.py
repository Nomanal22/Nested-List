rcds=[]
scor=[]
stds=[]
for _ in range(int(input())):
    name = input()
    score = float(input())
    student=[name,score]
    rcds.append(student)
    scor.append(score)

scores=sorted(set(scor))

for i in rcds:
    if i[1]==scores[1]:
        stds.append(i[0])

for i in sorted(stds):
    print(i)