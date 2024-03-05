import collections

from static import stats_translate, Normal_Organ_List


def translate(counter):
    output_text = ""
    for i in counter:
        stat_name = i
        stat = str(counter[i])
        if i in stats_translate:
            stat_name = stats_translate[i]
        output_text += stat_name+":"+stat+"\n"
    return output_text

class Chest:
    def __init__(self):
        self.container = [[[] for _ in range(9)], [[] for _ in range(9)], [[] for _ in range(9)]]
        self.stats = {}

    def regist_oragn(self, organ):
        self.container[organ.row][organ.col] = organ
    
    def sum_stat_normal(self):
        self.stats = {}
        counter = collections.Counter(self.stats)
        for i in range(3):
            for j in range(9):
                if self.container[i][j] != []:
                    current = collections.Counter(self.container[i][j].normal_stats)
                    counter.update(current)
        
        self.stats = counter
        output_text = translate(counter)
        return output_text
    

    def reset(self):
        self.container = [[[] for _ in range(9)], [[] for _ in range(9)], [[] for _ in range(9)]]

class Organ:
    def __init__(self, chest, name, types, row, col, normal_stats, activate_stats, food_stats):
        self.chest = chest
        self.name = name
        self.types = types
        self.row = row
        self.col = col
        self.normal_stats = normal_stats
        self.activate_stats = activate_stats
        self.food_stats = food_stats
        self.chest.regist_oragn(self)



class Normal_Organ(Organ):
    # 常规的器官，只包含常规属性、激活属性、文字描述等，不需要任何计算的内容
    def __init__(self, chest, id, row, col):
        Organ_stats = Normal_Organ_List[id]
        self.types = Organ_stats["types"]
        self.name = Organ_stats["name"]
        self.normal_stats = Organ_stats["normal_stats"]
        self.activate_stats = Organ_stats["activate_stats"]
        self.food_stats = Organ_stats["food_stats"]

        super().__init__(chest, self.name, self.types, row, col, self.normal_stats, self.activate_stats, self.food_stats)



def cancerGenerator(chest, row, col, normal_stats):

    cancer = Organ(chest, "无形肿瘤", ["infect"], row, col, normal_stats, {}, {})



if __name__ == "__main__":
    chest = Chest()
    metal0 = Normal_Organ(chest, "遗物金属板", 0, 0)
    metal1 = Normal_Organ(chest, "遗物金属板", 0, 1)
    heart = Normal_Organ(chest, "心脏", 1, 0)
    rotten_heart = Normal_Organ(chest, "腐烂的心脏", 1, 1)

    cancer0 = {"luk":3.25, "spd":1.125}

    cancerGenerator(chest, 2, 0, cancer0)

    print(metal0.normal_stats)
    print(metal1.normal_stats)
    print(heart.normal_stats)
    print(rotten_heart.normal_stats)
    p = chest.sum_stat_normal()
