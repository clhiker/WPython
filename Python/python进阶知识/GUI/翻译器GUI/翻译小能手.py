import json
import requests
from tkinter import *


class FanYiQi():
    #构造函数
    def __init__(self):
        self.root = Tk()
        self.data = ""
        self.from_language = "zh"
        self.to_language = "jp"
        self.result = "Nothing"
        self.input_text = None
        self.output_text = None
        self.input_button = None
        self.output_button = None
    # 获取文本
    def getText(self):
        self.data = self.input_text.get('0.0',END)
    # 输出结果
    def outResult(self):
        self.output_text.delete('0.0',END)
        self.output_text.insert('insert', self.result)

    #初始化窗口
    def setWindow(self):
        self.root.title('翻译器')
        self.root.geometry('600x500')  # 窗口大小
        self.root.resizable(width=False, height=True)  # 宽和高都设置为可变的
    #标签
    def setLabel(self):
        #frm = Frame(self.root)
        #left_frame = Frame(frm)
        #right_frame = Frame(frm)
        input_label = Label(self.root,
                         text=' input anything:',
                         bg='pink',
                         font=('Arial',12),
                         width=25,height=1
                         ).grid(row=0,column=0)
        #left_frame.pack(side=LEFT)
        output_label = Label(self.root,
                         text=' the result:',
                         bg='yellow',
                         font=('Arial', 12),
                         width=25, height=1
                         ).grid(row=0,column=2)
        #right_frame.pack(side=RIGHT)
        #frm.pack()
    #单行文本
    def setInText(self):
        self.input_text = Text(self.root,
                                 background='lavender',
                                 #borderwidth=30,
                                 font=('Helvetica',12,'bold'),
                                 foreground='red',
                                 highlightbackground='yellow',# highlightcolor='yellow',
                                 highlightthickness=4,
                                 insertbackground='blue',#insertborderwidth=10
                                 relief='sunken',
                                 width=25,
                                 )
        self.input_text.grid(row=4,column=0)

    #输入语言响应函数
    def setInEnglish(self):
        self.from_language = 'en'
        self.input_button["text"] = 'English'
    def setInChinese(self):
        self.from_language = 'zh'
        self.input_button["text"] = 'Chinese'
    def setInJapanese(self):
        self.from_language = 'jp'
        self.input_button["text"] = 'Japanese'

    # 输出语言响应函数
    def setOutEnglish(self):
        self.to_language = 'en'
        self.output_button["text"] = 'English'
    def setOutChinese(self):
        self.to_language = 'zh'
        self.output_button["text"] = 'Chinese'
    def setOutJapanese(self):
        self.to_language = 'jp'
        self.output_button["text"] = 'Japanese'

    # 单级按钮
    # def setButton(self):
    #     Button(self.root, text='English', command=self.setEnglish).pack(side=LEFT)   #command这里如果加上括号则函数自动运行切只运行一次
    #     Button(self.root, text='Chinese', command=self.setChinese).pack(side=RIGHT)
    #     Button(self.root, text='interpreter', command=self.interpreter).pack(side=TOP)
    #多级菜单按钮
    def setButtonMenu(self):
        #setenter
        Button(self.root, text='interpreter', command=self.interpreter).grid(row=1,column=1)
        #setin
        self.input_button = Menubutton(self.root,
                               text='Chinese',
                               foreground='blue',
                               highlightbackground='black',  # highlightcolor='yellow',
                               highlightthickness=1,
                               relief='sunken',
                               width=10,
                              )
        self.input_button.grid(row=2,column=0)
        self.input_button.menu = Menu(self.input_button)
        self.input_button.menu.add_command(label='Chinese',command=self.setInChinese)
        self.input_button.menu.add_command(label='English',command=self.setInEnglish)
        self.input_button.menu.add_command(label='Japanese',command=self.setInJapanese)
        self.input_button['menu'] = self.input_button.menu

        #setout
        self.output_button = Menubutton(self.root,
                                text='Janpanese',
                                foreground = 'red',
                                highlightbackground = 'yellow',  # highlightcolor='yellow',
                                highlightthickness = 1,
                                relief = 'sunken',
                                width = 10,
                                )
        self.output_button.grid(row=2,column=2)
        self.output_button.menu = Menu(self.output_button)
        self.output_button.menu.add_command(label='Chinese', command=self.setOutChinese)
        self.output_button.menu.add_command(label='English', command=self.setOutEnglish)
        self.output_button.menu.add_command(label='Japanese', command=self.setOutJapanese)
        self.output_button['menu'] = self.output_button.menu

    def setOutText(self):
        self.output_text = Text(self.root,
                                background = 'lightgreen',
                                #borderwidth = 30,
                                font = ('Helvetica', 12, 'bold'),
                                foreground = 'red',
                                highlightbackground = 'yellow',  # highlightcolor='yellow',
                                highlightthickness = 4,
                                insertbackground = 'blue',  # insertborderwidth=10
                                relief = 'sunken',
                                width = 25,
        )
        self.output_text.grid(row=4,column=2)
    #list窗口
    def setListWindows(self):
        input_one = ['输入方：']
        output_one = ['输出方：']
        input_list = Listbox(self.root)
        output_list = Listbox(self.root)
        input_list.insert(0, input_one)
        output_list.insert(0, output_one)
        input_list.pack()
        output_list.pack()
    #GUI出口
    def show(self):
        self.setWindow()
        self.setLabel()
        self.setButtonMenu()
        self.setInText()
        self.setOutText()
        self.root.mainloop()
    #翻译函数
    def interpreter(self):
        self.getText()
        data = self.data
        url = "http://fanyi.baidu.com/basetrans"
        data = {
            "query": data,
            "from": self.from_language,
            "to": self.to_language,
        }

        headers = {
            "User-Agent": "Mozilla/5.0 (Linux; Android 5.1.1; Nexus 6 Build/LYZ28E) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Mobile Safari/537.36",
        }

        response = requests.post(url, data=data, headers=headers)
        dir = response.content.decode('unicode-escape')
        begin = int(dir.find(r'"dst":'))
        end = int(dir.find(r'"prefixWrap"'))
        self.result = dir[begin + 7:end - 2]
        self.outResult()

def main():
    fayiqi = FanYiQi()
    fayiqi.show()

main()

