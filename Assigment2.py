from random import *
from matplotlib import pyplot as plt

class VOQ:
    dic ={}
    def __init__(self, fs) -> None:
        self.fabric_size = fs
        for i in range(1,fs+1):
            self.dic.update({i:{}})
            for j in range(1,fs+1):
                self.dic[i].update({j:0})
            for _ in range(1000):
                tempOutput = randrange(1,fs+1)
                self.dic[i][tempOutput] += 1
    
    def randomchoice(self, list):
        if len(list) == 0:
            return 0
        else:    
            return choice(list)
        
    def createMatrix(self):
        retDic = {}
        fs = self.fabric_size
        for i in range(1, fs+1):
            retDic.update({i:[]})

        return retDic

    def step(self):
        loopCount = 0
        listFreeOutput = list(range(1, self.fabric_size+1))
        listFreeInput = list(range(1, self.fabric_size+1))
        while(1):
            requestMatrix = self.createMatrix()
            grantMatrix = self.createMatrix()
            matchCount = 0
            for i in listFreeInput:
                for j in listFreeOutput:
                    if self.dic[i][j] > 0:
                        requestMatrix[j].append(i)
                        matchCount += 1
            if matchCount == 0:
                break
            for a in listFreeOutput:
                x = self.randomchoice(requestMatrix[a])
                if x>0:
                    grantMatrix[x].append(a)

            for b in listFreeInput:
                y = self.randomchoice(grantMatrix[b])
                if y in listFreeOutput:
                    listFreeInput.remove(b)
                    listFreeOutput.remove(y)
                    self.dic[b][y] -= 1

            loopCount += 1
        return loopCount
    def start(self):
        avrLoop = 0
        for _ in range(1000):
            avrLoop +=self.step()
        
        self.avrLoop = avrLoop/1000

        a = 0
        for i in range(1, self.fabric_size+1):
            for j in range(1, self.fabric_size+1):
                a += self.dic[i][j]

        self.throughPut = (1 - a/(self.fabric_size*1000))*100
x = [1, 2, 4, 8, 16, 32, 64, 128]
y = []
z = []

averageLoop = {}
for i in x:
    averageLoop.update({i:[]})
    for _ in range(30):
        test = VOQ(i)
        test.start()
        averageLoop[i].append(test.avrLoop)
    print(f'Average value of PIM with fabric size = {i}: {sum(averageLoop[i])/len(averageLoop[i]):.3f}')

for i in range(len(x)):
    test = VOQ(x[i])
    test.start()
    y.append(test.throughPut)

plt.plot(x,y, color ="r")
plt.xlabel("Fabric size")
plt.ylabel("Throughput")
plt.show()