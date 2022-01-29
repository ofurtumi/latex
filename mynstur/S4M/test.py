i = 1
tolur = []
for i in range(16) :
    n = 10**i
    j = i**10*2**i
    tolur.append(n>j) 

print(tolur)

trueCounter = 0
for i in tolur:
    if i == True:
        trueCounter+=1

    

print("Trues: " + str(trueCounter))
print("Falses: " + str(len(tolur)-trueCounter))

