# -*- coding = utf-8 -*-
# @Time : 2022/1/25 上午 12:51
# @Author : Fe
# @File : OOP_example.py
# @Software : PyCharm

# 定義一個 Vtuber 類別
class Vtuber():
    # 建構元
    def __init__(self, name, hair_color, eye_color):
        # 屬性
        self.name = name
        self.hair_color = hair_color
        self.eye_color = eye_color

    # 方法
    def greet(self):
        print(f"はじめまして，私は{self.name}です")


rushia = Vtuber("潤羽るしあ", "綠色", "紅色")    # 將 Vtuber 類別實體化創建 rushia 物件
rushia.greet()  # 調用 rushia 物件中的 greet() 方法