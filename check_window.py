#!/usr/bin/env python
# -*- coding: utf-8 -*-

import Tkinter
import tkFileDialog
import tkMessageBox
import file_scan
import threading


top = Tkinter.Tk()
top.title(u'文件内容检索')
top.minsize(500, 400)
top.maxsize(500, 600)


lbl1 = Tkinter.StringVar()
label1 = Tkinter.Label(top, textvariable=lbl1, relief=Tkinter.FLAT).place(x=10, y=15)
lbl1.set(u"选择检索路径：")

lbl2 = Tkinter.StringVar()
label2 = Tkinter.Label(top, textvariable=lbl2, relief=Tkinter.FLAT).place(x=10, y=65)
lbl2.set(u"检索关键字：")

text1 = Tkinter.Text(top, relief=Tkinter.SOLID)
text1.place(x=100, y=17, width=310, height=20)

text2 = Tkinter.Text(top, relief=Tkinter.SOLID)
text2.place(x=100, y=67, width=310, height=20)

text3 = Tkinter.Text(top, relief=Tkinter.SOLID)
text3.place(x=100, y=107, width=310, height=260)

def choose_path():
    path = tkFileDialog.askdirectory()
    text1.delete(u"1.0", Tkinter.END)  # delete the content of Text
    text1.insert(Tkinter.INSERT, path)

def start_searching():
    global file_path
    file_path = text1.get(1.0, u"end-1c")  # get the content of Text
    # print text1.get(1.0, Tkinter.END)  # 这样获取的内容会多出一个空行
    if file_path == '':
        tkMessageBox.showinfo(u"提示", u"请选择检索的文件路径")
        return
    else:
        global keyword
        keyword = text2.get(1.0, u'end-1c')
        if keyword == '':
            tkMessageBox.showinfo(u"提示", u"请输入要检索的关键字")
            return
        com_thread = threading.Thread(target=get_file_path)
        com_thread.start()

def get_file_path():
    global Text
    included_files = file_scan.keyword_check(file_path, keyword)
    Text = '\r\n'.join(included_files)
    top.event_generate("<<GETFILELIST>>", when="tail")

top.bind("<<GETFILELIST>>", lambda evt: text3.insert("insert", Text))


btn1 = Tkinter.Button(top, text=u"  选  择  ", command=choose_path).place(x=420, y=10)
btn2 = Tkinter.Button(top, text=u"开始检索", command=start_searching).place(x=420, y=60)


top.mainloop()
