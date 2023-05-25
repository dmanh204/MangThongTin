from random import *
import matplotlib.pyplot as mpl
class HOL:
    dic = {}
    
    def __init__(self, fs):
        self.fabric_size = fs
        for i in range(1,fs+1):
            self.dic.update({i:[]})
            for _ in range(1000):
                self.dic[i].append(randrange(1,fs+1))
    def step(self):
        # List nay gom fabric_size gia tri 1, tuong trung cho cac output.
        # Neu goi dau hang huong toi mot output co gia tri 1, no se duoc phep di qua.
        # Sau khi goi nay di qua, cong output se bi danh dau la 0.
        # Cac goi tiep theo co cung so cong output trong luot nay se khong duoc phep di nua.
        lis = [1]*self.fabric_size    
        for i in range(1,self.fabric_size+1):
            a = self.dic[i][0]
            if(lis[a-1] == 1):
                self.dic[i].pop(0)
                lis[a-1] = 0
    
    def start(self, mode):
        if(mode == 1):
            for _ in range(1000):
                self.step()
        elif(mode == 0):
            for _ in range(1000):
                self.stepRandom()

        a = 0
        for i in range(1, self.fabric_size+1):
            a += len(self.dic[i])

        self.throughPut = (1 - a/(self.fabric_size*1000))*100
    def stepRandom(self):
        # List nay chua cac chi so xac dinh cong input.
        # Chung ta co cac input tu 1 den fabric_size, tuong ung voi cac chi so trong parameterList.
        # De chon ngau nhien cong input, ta chon ngau nhien chi so trong parameterList, sau do remove chi so nay.
        # Tiep tuc lap lai voi parameterList fabric_size lan.
        parameterList = list(range(1, self.fabric_size+1))
        # List nay gom fabric_size gia tri 1, tuong trung cho cac output.
        # Neu goi dau hang huong toi mot output co gia tri 1, no se duoc phep di qua.
        # Sau khi goi nay di qua, cong output se bi danh dau la 0.
        # Cac goi tiep theo co cung so cong output trong luot nay se khong duoc phep di nua.
        checkList = [1]*self.fabric_size
        for _ in range(self.fabric_size):
            para = choice(parameterList) # Chon ngau nhien tham so trong tap parameterList
            outputNum = self.dic[para][0]       # Lay ra dia chi output goi dau hang cua cong input tuong ung
            if(checkList[outputNum-1] == 1):    # Neu cong output dang la 1
                self.dic[para].pop(0)           # Loai bo goi dau hang
                checkList[outputNum-1] = 0      # Danh dau cong output tuong ung = 0 (Dang ban)
                parameterList.remove(para)      # Loai bo tham so nay khoi parameteList
            else:
                parameterList.remove(para)      # Neu cong da la 0, khong lam gi, chi loai bo tham so khoi parameterList
x = [1, 2, 4, 8, 16, 32, 64, 128]
y = []
z = []
for i in range(len(x)):
    test = HOL(x[i])
    test.start(1)
    y.append(test.throughPut)

for i in range(len(x)):
    test = HOL(x[i])
    test.start(0)
    z.append(test.throughPut)
mpl.plot(x,y, color ="r", label = "uu tien cong nho hon")
mpl.plot(x,z, color = "g", label = "chon cong ngau nhien")

mpl.xlabel("Fabric size")
mpl.ylabel("Throughput")
mpl.legend()
mpl.show()