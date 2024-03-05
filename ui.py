import tkinter as tk
from tkinter import ttk
from logic import *

class InteractiveGrid:
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.items = [[None for _ in range(columns)] for _ in range(rows)]

        self.root = tk.Tk()
        self.root.title("Fluoroscopy——胸腔模拟器")
        self.root.geometry('750x400+100+200')

        self.chest = Chest()

        self.frame1 = ttk.Frame(self.root)
        self.frame1.grid(row=0, column=0)
        self.frame2 = ttk.Frame(self.root)
        self.frame2.grid(row=1,column=0)
        self.textbox = tk.Text(self.frame2, height=15, width=60)
        self.textbox.pack()
        self.textbox.insert("1.0","欢迎使用器官模拟器\n点击每个位置上的按钮可以设定器官\n")
        self.create_grid()

    def create_grid(self):
        for i in range(self.rows):
            for j in range(self.columns):
                button = tk.Button(self.frame1, text=f"无内容", command=lambda i=i, j=j: self.show_item_selector(i, j))
                button.grid(row=i, column=j)
        
        restButton = tk.Button(self.frame1, text="重置", command=self.reset)
        calculateButton = tk.Button(self.frame1, text="结算", command=self.calculate)
        saveButton = tk.Button(self.frame1, text="保存", command=self.save)
        restButton.grid(row=0, column=9)
        calculateButton.grid(row=1, column=9)
        saveButton.grid(row=2, column=9)

        
    
    def reset(self):
        # 在这里可以添加重置界面，例如清空所有按钮上的文字、清空所有物品等
        for i in range(self.rows):
            for j in range(self.columns):
                self.frame1.grid_slaves(row=i, column=j)[0].config(text=f"Cell {i+1}-{j+1}")
        self.chest.reset()
        self.textbox.delete("1.0", tk.END)
    def calculate(self):
        self.output_text = self.chest.sum_stat_normal()
        self.textbox.delete("1.0", tk.END)
        self.textbox.insert("1.0", self.output_text)

        return

    def save(self):

        pass

    def show_item_selector(self, row, column):
        item_selector = tk.Toplevel(self.root)
        item_selector.geometry('300x200+200+300')
        item_selector.title(f"选择器官，位置为 {row+1}-{column+1}")

        organ_name = tk.StringVar()
        organ_select_box = ttk.Combobox(item_selector, textvariable=organ_name)
        organ_select_box.pack()
        organ_select_box["value"] = [Normal_Organ_List[i]["name"] for i in Normal_Organ_List]

        confirm_button = tk.Button(item_selector, text="Confirm", command=lambda: self.confirm_item(row, column, organ_name.get(), item_selector))
        confirm_button.pack()

    def confirm_item(self, row, column, organ_name, item_selector):
        self.items[row][column] = Normal_Organ(self.chest, organ_name, row, column)
        self.frame1.grid_slaves(row=row, column=column)[0].config(text=f"{organ_name}")
        item_selector.destroy()

    def run(self):
        self.root.mainloop()
        

# 创建一个3行9列的交互网格
grid = InteractiveGrid(rows=3, columns=9)
grid.run()
