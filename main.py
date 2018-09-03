from tkinter import *
from PIL import Image, ImageTk
import random
import tkinter.messagebox
import pygame
import numpy as np
from tkinter import ttk


pygame.init()
root = Tk()
root.minsize(550, 600)
root.title('谁是卧底开发版之—BlackChristmas')
root.config(bg='black')

photo = PhotoImage(file='image/photo.png')
imgLabel = Label(root, image=photo)
imgLabel.config(bg='black', width=300, height=300)
imgLabel.pack(side=TOP, pady=5)

game_title = Label(root, text='BlackChristmas')
game_title.config(bg='black', fg='#980707', font=('Times', 20, 'bold italic'))
game_title.pack(side=TOP, pady=10)

info = """      传说在古老的旧世界森林里，流传着一段诡异的怪谈：自从塔南被旧世界的圣灵救赎后，每当平安夜的夜幕来临时，村里就会离奇的消失一位村民，而第二天找到时，已是
悬挂在森林树上的腐烂掉的尸体。村民们对此一直惶恐不已。终于在平安夜傍晚，一辆马车载着一位年迈的名叫罗格斯的瘸腿瞎子法师来到了村里。他也听了这段怪谈。于是他告诉村民们这其
实是“黑圣诞”在捣鬼。塔南遗留下来的邪能的影响，他会在平安夜随机附身在一位村民的身上，并偷偷控制着他到森林里，取走他了灵魂。要想战胜黑圣诞，只有通过罗格斯手里的一副占卜卡牌...
游戏规则如下：
游戏有被附身的人和普通平民2 种身份。
游戏开始后，在场人数大部分玩家拿到同一词语，其余一名玩家会拿到与之相关的另一词语。每人每轮用一句话描述自己拿到的卡牌内容，既不能说出卡牌内容，也要给其他玩家以暗示。
每轮描述完毕，所有在场的人陈述怀疑谁是卧底，并说明理由，并进行投票，得票最多的人出局。若被附身的人出局，则游戏结束。若未出局，游戏继续，反复此流程。若被附身的人撑
到最后一轮（剩余总人数小于卧底初始人数的二倍时），则“黑圣诞”获胜，反之，则村民胜利..."""


content_text = Text(root, wrap='word')
quote = info
content_text.insert(END, quote)
content_text.config(bg='#2a2d2d', fg='white', font=('Microsoft YaHei', 12))
content_text.pack(expand='no', fill='both')


class Game:
    # def __init__(self, words, P_num, player_id):
    # 	self.words = words
    # 	self.player_num = P_num
    # 	self.vote_num = vote_num
    # 	self.player_id = player_id
    # 选择游戏单词
    def choose_database(self):
        words_database = {'1': ['钢笔', '铅笔']}
        proxy = random.choice(list(words_database))
        value = words_database[proxy]
        return value

    def choose_words(self):

        # print(value)
        value = self.choose_database()
        wodi_value = random.choice(value)
        index1 = value.index(wodi_value)
        if index1 == 0:
            pinming_value = value[1]
        else:
            pinming_value = value[0]

        print(value)

        return [wodi_value, pinming_value]

    def game_over(self):

        content_text.delete(1.0, END)
        # check_word_button.config(state=DISABLED)
        # start_button.config(state=DISABLED)
        quote2 = """黑圣诞已被击杀！"""
        content_text.insert(END, quote)
        content_text.config(bg='white', fg='yellow',
                            font=('Microsoft YaHei', 12))
        frame.config(bg='white')
        content_text.pack(expand='no', fill='both')
        print('游戏结束')


def closeWindow():
    if tkinter.messagebox.askokcancel('谁是卧底开发版之—BlackChristmas', '确定要退出游戏吗？'):
        root.destroy()


root.protocol('WM_DELETE_WINDOW', closeWindow)


g = Game()


def choose_wodi():
    num_list = np.arange(int(get_player_num()))
    num_list = num_list.remove(int(vote_player_num()))
    wodi_num = random.choice(num_list)
    print('卧底值是', wodi_num)
    print('生成的数据范围为：', num_list)
    return wodi_num
    # pinming_num = num_list.remove(wodi_num)


def judge_game():
    result = choose_wodi()
    vote = vote_player_num()
    if vote == str(result):
        content_text.delete(1.0, END)
        quote2 = """黑圣诞已被击杀！"""
        content_text.insert(END, quote2)
        imgLabel.config(bg='white', width=300, height=300)
        game_title.config(bg='white', fg='black',
                          font=('Times', 20, 'bold italic'))
        content_text.config(bg='white', fg='black',
                            font=('Microsoft YaHei', 12))
        root.config(bg='white')
        content_text.pack(expand='no', fill='both')
        playmusic4()
    else:
        print('游戏继续')
        playmusic2()
        content_text.delete(1.0, END)
        quote = """黑圣诞正在寻找下一个目标。。。"""
        content_text.insert(END, quote)
        content_text.pack(expand='no', fill='both')


# 音乐模块

def playmusic():
    pygame.mixer.music.load('background_music/playmusic.mp3')
    pygame.mixer.music.play(-1)


def playmusic2():
    pygame.mixer.music.load('background_music/playmusic2.mp3')
    pygame.mixer.music.play(1)


def playmusic3():
    pygame.mixer.music.load('background_music/playmusic3.mp3')
    pygame.mixer.music.play(1)


def playmusic4():
    pygame.mixer.music.load('background_music/playmusic4.mp3')
    pygame.mixer.music.play(-1)


def stop_playing_music():
    pygame.mixer.music.stop()


def get_player_num(*args):  # 处理事件，*args表示可变参数
    player_num = comboxlist.get()
    player_num_left = player_num
    # 打印选中的值
    return player_num


def vote_player_num(*args):
    player_choose = player_list.get()
    return player_choose


def create_data(event):
    content_text.delete(1.0, END)
    playmusic3()
    start_button.config(state=DISABLED)
    quote2 = """黑圣诞已临近，请在音乐结束后回家，并关好门窗..."""
    content_text.insert(END, quote2)
    content_text.config(bg='#2a2d2d', fg='white', font=('Microsoft YaHei', 12))
    content_text.pack(expand='no', fill='both')
    g.choose_database()
    words = g.choose_words()


def callback():
    print('游戏开始')


# 选择词组
def check_words():
    if check_word_button['text'] == '抽取卡牌':
        check_word_button['text'] = '放回卡牌'
        content_text.delete(1.0, END)

        words = g.choose_words()

        print('你拿到的词语是：', words[0])
        quote = words[0]
        content_text.insert(END, quote)
        content_text.config(bg='#2a2d2d', fg='white',
                            font=('Microsoft YaHei', 12))
        content_text.pack(expand='no', fill='both')

    else:
        content_text.delete(1.0, END)
        check_word_button['text'] = '抽取卡牌'


def callback3():

    judge_game()
    print('投的是：', vote_player_num())


def callback4():
    print('重启游戏')
    root.config(bg='black')
    imgLabel.config(bg='black', width=300, height=300)
    game_title.config(bg='black', fg='#980707',
                      font=('Times', 20, 'bold italic'))
    start_button.config(state=NORMAL)
    content_text.delete(1.0, END)
    quote = info
    content_text.insert(END, quote)
    content_text.config(bg='#2a2d2d', fg='white', font=('Microsoft YaHei', 12))
    content_text.pack(expand='no', fill='both')
    playmusic()


# 播放背景音乐
playmusic()

# UI界面
frame = Frame(root)
frame.pack(side=BOTTOM, fill='x')
frame.config(width=50, height=50)

comvalue = tkinter.StringVar()  # 窗体自带的文本，新建一个值
comboxlist = ttk.Combobox(frame, width=10, textvariable=comvalue)  # 初始化
comboxlist["values"] = ("3", "4", "5", "6", "7")
comboxlist.current(0)  # 选择第一个
# 绑定事件,(下拉列表框被选中时，绑定go()函数)
comboxlist.bind("<<ComboboxSelected>>", get_player_num)
comboxlist.pack(side=LEFT)

start_button = Button(frame, text='开始', width=15, command=callback)
start_button.bind('<Button-1>', create_data)
start_button.pack(side=LEFT, padx=2)

check_word_button = Button(frame, text='抽取卡牌', width=10, command=check_words)
check_word_button.pack(side=LEFT, padx=2)

comvalue2 = tkinter.StringVar()
player_list = ttk.Combobox(frame, width=12, textvariable=comvalue2)
player_list['values'] = ('选择玩家号码', '0', '1', '2', '3', '4', '5', '6', '7')
player_list.current(0)
player_list.bind("<<ComboboxSelected>>", vote_player_num)
player_list.pack(side=LEFT, padx=1)


vote_button = Button(frame, text='投票', width=10, command=callback3)

vote_button.pack(side=LEFT, padx=2)

restart_button = Button(frame, text='重新开始', width=10, command=callback4)
restart_button.pack(side=LEFT, padx=2)


root.mainloop()
