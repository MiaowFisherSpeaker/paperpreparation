from tkinter import *
import time


class MY_GUI():
    def __init__(self, window_name):
        self.window_name = window_name

    def set_init_window(self):
        self.window_name.title('pdf文字去空格')  # 设置标题
        self.window_name.geometry('1000x600+10+10')  # 设置窗体大小,以及弹出位置
        self.window_name.configure(background='AliceBlue')
        # 标签
        self.init_data_label = Label(self.window_name, fg='Chocolate', bg='AliceBlue', text='待处理文本')
        self.init_data_label.grid(row=0, column=0)
        self.result_data_label = Label(self.window_name, fg='Chocolate', bg='AliceBlue', text='处理结果')
        self.result_data_label.grid(row=0, column=12)

        # 文本框
        self.init_data_Text = Text(self.window_name, width=70, height=35)  # 原始数据录入框
        self.init_data_Text.grid(row=1, column=0, rowspan=15, columnspan=10)
        self.result_data_Text = Text(self.window_name, width=70, height=35)  # 处理结果展示
        self.result_data_Text.grid(row=1, column=12, rowspan=15, columnspan=10)

        # 按钮
        self.str_trans_nospacing = Button(self.window_name, bg='AliceBlue', fg='Black', text='转换',
                                          command=self.replace_spacing)
        self.str_trans_nospacing.grid(row=18, column=11)
        self.clearBox = Button(self.window_name, bg='AliceBlue', fg='Black', text='清除左边',
                               command=self.clear_init_data_Text)
        self.clearBox.grid(row=18, column=5)
        self.save_to_file = Button(self.window_name, bg='AliceBlue', fg='Black', text='保存至文件（敬请期待）')
        self.save_to_file.grid(row=18, column=15)

    # 功能函数
    '''    
    def demo_replace_spacing(self):#单独运行可以，没必要窗口
        remove_str = ' \n'  # 删除空格和换行
        n = 1
        while True:
            print(f'num {n}')
            fs = ''
            while True:
                s = input()
                if s == '0':
                    break
                fs += s
            for i in remove_str:
                s = s.strip().replace(i, '')
            print(fs)
            n += 1
            '''

    def replace_spacing(self):
        remove_str = ' \n'  # 删除空格和换行
        var = self.init_data_Text.get('0.0', 'end').strip()
        for i in remove_str:
            var = var.replace(i, '')
        if var != '':
            self.result_data_Text.insert('end', "%s\n\n" % var)
        else:
            self.result_data_Text.insert('end', "你输入为空,1s后删除此消息\n\n")
            time.sleep(2)
            self.clear_result_data_Text('-2.0', 'end')

    def clear_init_data_Text(self):
        self.init_data_Text.delete('0.0', 'end')

    def clear_result_data_Text(self, start='-2.0', end='end'):
        self.init_data_Text.delete(start, end)


def main():
    t1 = time.time()
    init_window = Tk()
    delspacing = MY_GUI(init_window)
    delspacing.set_init_window()

    init_window.mainloop()


if __name__ == '__main__':
    main()
