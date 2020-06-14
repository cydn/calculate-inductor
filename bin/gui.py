#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tkinter import *
import time
from .main import *

LOG_LINE_NUM = 0

class MY_GUI():
    def __init__(self,init_window_name):
        self.init_window_name = init_window_name


    #设置窗口
    def set_init_window(self):
        self.init_window_name.title("获取电感量 v1.0.0")           #窗口名
        #self.init_window_name.geometry('320x160+10+10')                         #290 160为窗口大小，+10 +10 定义窗口弹出时的默认展示位置
        self.init_window_name.geometry('1068x681+10+10')
        self.init_window_name["bg"] = "pink"                                    #窗口背景色，其他背景色见：blog.csdn.net/chl0000/article/details/7657887
        #self.init_window_name.attributes("-alpha",0.9)                          #虚化，值越小虚化程度越高
        #标签
        self.init_L_label = Label(self.init_window_name, text="长度l（单位为 m）")
        self.init_L_label.grid(row=0, column=0)

        self.init_R_label = Label(self.init_window_name, text="半径R（单位为 m）")
        self.init_R_label.grid(row=5, column=0)

        self.result_data_label = Label(self.init_window_name, text="电感量（单位为 H）")
        self.result_data_label.grid(row=0, column=12)

        self.log_label = Label(self.init_window_name, text="日志")
        self.log_label.grid(row=12, column=0)
        
        #文本框
        self.init_L_Text = Text(self.init_window_name, width=67, height=5)  #原始R录入框
        self.init_L_Text.grid(row=1, column=0, rowspan=1, columnspan=5)

        self.init_R_Text = Text(self.init_window_name, width=67, height=5)  #原始L录入框
        self.init_R_Text.grid(row=6, column=0, rowspan=1, columnspan=5)

        self.result_data_Text = Text(self.init_window_name, width=70, height=49)  #处理结果展示
        self.result_data_Text.grid(row=1, column=12, rowspan=15, columnspan=10)

        self.log_data_Text = Text(self.init_window_name, width=66, height=9)  # 日志框
        self.log_data_Text.grid(row=13, column=0, columnspan=10)
        #按钮
        self.get_l_button = Button(self.init_window_name, text="获取电感量", bg="lightblue", width=10,command=self.get_my_L)  # 调用内部方法  加()为直接调用
        self.get_l_button.grid(row=1, column=11)


    #功能函数
    def get_my_L(self):
        self.result_data_Text.delete(1.0,END)
        try:
            l = float(self.init_L_Text.get(1.0,END))
            R = float(self.init_R_Text.get(1.0,END))
        except:
            self.result_data_Text.insert(1.0,"plseae input int or float numbers.")
            self.write_log_to_Text("电感量计算失败")
            return
        #print("src =",R)
        
        try:
            my_L = getL(R,l)
            #print(myMd5_Digest)
            #输出到界面
            self.result_data_Text.insert(1.0,my_L)
            self.write_log_to_Text("成功计算电感量")
        except:
            self.result_data_Text.delete(1.0,END)
            self.result_data_Text.insert(1.0,"计算电感量失败")

    #获取当前时间
    def get_current_time(self):
        current_time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
        return current_time


    #日志动态打印
    def write_log_to_Text(self,logmsg):
        global LOG_LINE_NUM
        current_time = self.get_current_time()
        logmsg_in = str(current_time) +" " + str(logmsg) + "\n"      #换行
        if LOG_LINE_NUM <= 7:
            self.log_data_Text.insert(END, logmsg_in)
            LOG_LINE_NUM = LOG_LINE_NUM + 1
        else:
            self.log_data_Text.delete(1.0,2.0)
            self.log_data_Text.insert(END, logmsg_in)


def gui_start():
    init_window = Tk()              #实例化出一个父窗口
    ZMJ_PORTAL = MY_GUI(init_window)
    # 设置根窗口默认属性
    ZMJ_PORTAL.set_init_window()

    init_window.mainloop()          #父窗口进入事件循环，可以理解为保持窗口运行，否则界面不展示
