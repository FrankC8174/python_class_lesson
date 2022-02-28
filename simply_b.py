class Reg_clean:
    def __init__(self, vac, toilets, dust, floors):
        self.vac = vac
        self.toilets = toilets
        self.dust = dust
        self.floors = floors
        self.base_boards = False
        self.rooms = []
        
    def  clean_baseboards(self):
        self.base_boards = True
        

house_1 = Reg_clean("vac", "toilets", "dust", "floors")
house_2 = Reg_clean("vac", "toilets", "dust", "floors")


house_1.clean_baseboards()
print(house_1.base_boards)

class info:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        # self. Is single = false

mikes_info = info("mike", "21")

print(mikes_info. name, mikes_info.age)