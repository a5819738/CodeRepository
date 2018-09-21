import tkinter
import re


class Regex(object):
    def __init__(self):
        self.lenth = 0
        # main window
        self.root = tkinter.Tk()
        # main window title
        self.root.title('正则表达式匹配')
        # input regex
        self.regex_input = tkinter.Entry(self.root, width=30)

        # input source text
        self.source_input = tkinter.Text(self.root, width=50)

        # display info list
        self.display_info = tkinter.Listbox(self.root, width=50)

        # button
        self.result_btn = tkinter.Button(self.root, command=self.matchRegex, text='match')


    # gui layout
    def gui_arrang(self):
        self.regex_input.pack()
        self.source_input.pack()
        self.display_info.pack()
        self.result_btn.pack()


    # regex match
    def matchRegex(self):
        # get input
        self.regex = self.regex_input.get()
        self.source = self.source_input.get("0.0", tkinter.END)

        # match
        pattern = re.compile(self.regex, re.S)
        # items is list
        self.items = re.findall(pattern, self.source)
        # item is tuple
        for item in self.items:
            for i in range(len(item)):
                pass
                # item[i] = item[i]

        # clear display info list
        self.display_info.delete(0, tkinter.END)

        # display list
        for item in reversed(self.items):
            self.display_info.insert(0, item)

        self.lenth = len(self.items)


def main():
    regex = Regex()
    regex.gui_arrang()
    tkinter.mainloop()
    pass


if __name__ == '__main__':
    main()
