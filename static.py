stats_translate = {
    "hp":"健康", "neu":"神经效率", "brt":"呼吸效率",
    "str":"力量", "bld":"血液过滤效率", "mlk":"解毒效率",
    "def":"防御", "nut":"营养获取效率", "stm":"耐力",
    "dgs":"消化效率", "reg":"新陈代谢效率", "lug":"肺活量",
    "spd":"速度", "cry":"结晶", "luk":"幸运"
    }

#  名称，类型，基础属性，激活属性，食品属性
Normal_Organ_List = { 
    "遗物金属板":{"name":"遗物金属板", "types":["relics"], "normal_stats":{
    "hp":0.25, "neu":0.25, "brt":0.25,
    "str":0.25, "bld":0.25, "mlk":0.25,
    "def":0.125, "nut":0.125, "stm":0.25,
    "dgs":0.125, "reg":0.125, "lug":0.125,
    "spd":0.25}, "activate_stats":{}, "food_stats":()}, 
    
    "心脏":{"name":"心脏", "types":[], "normal_stats":{"hp":1}, "activate_stats":{}, "food_stats":(3,0.6)},
    "腐烂的心脏":{"name":"腐烂的心脏", "types":[], "normal_stats":{"hp":0.5}, "activate_stats":{}, "food_stats":(4,0.1)}

}
