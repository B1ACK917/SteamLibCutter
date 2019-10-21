import tkinter as tk
import tkinter.messagebox as msg
from tkinter.filedialog import askopenfilename, asksaveasfilename
from SteamLibCutter.frame_cut import *

dic = {'row': 1, 'col': 1, 'width': 100, 'height': 100, 'x_': 0, 'y_': 0, 'inter_w': 10, 'inter_h': 10}
frame = 0
typeisgif = False


def up_row(var):
    global dic, frame
    if dic['row'] == 10:
        return
    dic['row'] += 1
    var.config(text=dic['row'])
    new_img = pre_cut_one_frame(frame, dic['row'], dic['col'], dic['width'], dic['height'], dic['x_'], dic['y_'],
                                dic['inter_w'], dic['inter_h'])
    cv2.imshow('image', new_img)


def down_row(var):
    global dic, frame
    if dic['row'] == 1:
        return
    dic['row'] -= 1
    var.config(text=dic['row'])
    new_img = pre_cut_one_frame(frame, dic['row'], dic['col'], dic['width'], dic['height'], dic['x_'], dic['y_'],
                                dic['inter_w'], dic['inter_h'])
    cv2.imshow('image', new_img)


def up_col(var):
    global dic, frame
    if dic['col'] == 10:
        return
    dic['col'] += 1
    var.config(text=dic['col'])
    new_img = pre_cut_one_frame(frame, dic['row'], dic['col'], dic['width'], dic['height'], dic['x_'], dic['y_'],
                                dic['inter_w'], dic['inter_h'])
    cv2.imshow('image', new_img)


def down_col(var):
    global dic, frame
    if dic['col'] == 1:
        return
    dic['col'] -= 1
    var.config(text=dic['col'])
    new_img = pre_cut_one_frame(frame, dic['row'], dic['col'], dic['width'], dic['height'], dic['x_'], dic['y_'],
                                dic['inter_w'], dic['inter_h'])
    cv2.imshow('image', new_img)


def width_scale_arg(v):
    global dic, frame
    v = float(v)
    dic['width'] = int(v * 100) + 100
    new_img = pre_cut_one_frame(frame, dic['row'], dic['col'], dic['width'], dic['height'], dic['x_'], dic['y_'],
                                dic['inter_w'], dic['inter_h'])
    cv2.imshow('image', new_img)


def height_scale_arg(v):
    global dic, frame
    v = float(v)
    dic['height'] = int(v * 100) + 100
    new_img = pre_cut_one_frame(frame, dic['row'], dic['col'], dic['width'], dic['height'], dic['x_'], dic['y_'],
                                dic['inter_w'], dic['inter_h'])
    cv2.imshow('image', new_img)


def x_scale_arg(v):
    global dic, frame
    v = float(v)
    dic['x_'] = int(v * 100)
    new_img = pre_cut_one_frame(frame, dic['row'], dic['col'], dic['width'], dic['height'], dic['x_'], dic['y_'],
                                dic['inter_w'], dic['inter_h'])
    cv2.imshow('image', new_img)


def y_scale_arg(v):
    global dic, frame
    v = float(v)
    dic['y_'] = int(v * 100)
    new_img = pre_cut_one_frame(frame, dic['row'], dic['col'], dic['width'], dic['height'], dic['x_'], dic['y_'],
                                dic['inter_w'], dic['inter_h'])
    cv2.imshow('image', new_img)


def inter_w_scale_arg(v):
    global dic, frame
    v = float(v)
    dic['inter_w'] = int(v * 100) + 10
    new_img = pre_cut_one_frame(frame, dic['row'], dic['col'], dic['width'], dic['height'], dic['x_'], dic['y_'],
                                dic['inter_w'], dic['inter_h'])
    cv2.imshow('image', new_img)


def inter_h_scale_arg(v):
    global dic, frame
    v = float(v)
    dic['inter_h'] = int(v * 100) + 10
    new_img = pre_cut_one_frame(frame, dic['row'], dic['col'], dic['width'], dic['height'], dic['x_'], dic['y_'],
                                dic['inter_w'], dic['inter_h'])
    cv2.imshow('image', new_img)


def select_path():
    global frame, typeisgif
    path_ = askopenfilename(filetypes=[('image or video', '*.gif;*.png;*.jpg;*.mp4')])
    file_type = path_[path_.find('.'):]
    if file_type == '.jpg' or file_type == '.png':
        frame = cv2.imread(path_)
        typeisgif = False
    elif file_type == '.gif':
        frame = readgif(path_)
        typeisgif = True
    elif file_type == '.mp4':
        msg.showerror('Alert', '不支持的文件类型')
    else:
        return
    new_img = pre_cut_one_frame(frame, dic['row'], dic['col'], dic['width'], dic['height'], dic['x_'], dic['y_'],
                                dic['inter_w'], dic['inter_h'])
    cv2.imshow('image', new_img)


def output_img():
    path_ = asksaveasfilename()
    if typeisgif:
        res = cut_gif(dic['width'], dic['height'], dic['row'], dic['col'])
        write_dyn(path_, res, dic['row'], dic['col'])
    else:
        res = cut_frame(frame, dic['width'], dic['height'])
        write_sta(path_, res, dic['row'], dic['col'])


def init_window():
    global dic
    window = tk.Tk()
    window.title('SteamCoverProducer')
    window.geometry('300x600')
    row_num = tk.Label(master=window, text=dic['row'], width=5, height=1)
    row_text = tk.Label(master=window, text='行数', width=5, height=1, font=13)
    col_num = tk.Label(master=window, text=dic['col'], width=5, height=1)
    col_text = tk.Label(master=window, text='列数', width=5, height=1, font=13)
    pic_width_scale = tk.Scale(master=window, from_=-1, to=1, orient=tk.HORIZONTAL, length=150, showvalue=0,
                               tickinterval=1, resolution=0.01, command=width_scale_arg)
    pic_width_text = tk.Label(master=window, text='宽度', width=5, height=1, font=13)
    pic_height_scale = tk.Scale(master=window, from_=-1, to=1, orient=tk.HORIZONTAL, length=150, showvalue=0,
                                tickinterval=1, resolution=0.01, command=height_scale_arg)
    pic_height_text = tk.Label(master=window, text='高度', width=5, height=1, font=13)
    ini_x_scale = tk.Scale(master=window, from_=0, to=1, orient=tk.HORIZONTAL, length=150, showvalue=0,
                           tickinterval=1, resolution=0.01, command=x_scale_arg)
    ini_x_text = tk.Label(master=window, text='初始x', width=5, height=1, font=13)
    ini_y_scale = tk.Scale(master=window, from_=0, to=1, orient=tk.HORIZONTAL, length=150, showvalue=0,
                           tickinterval=1, resolution=0.01, command=y_scale_arg)
    ini_y_text = tk.Label(master=window, text='初始y', width=5, height=1, font=13)
    inter_w_scale = tk.Scale(master=window, from_=0, to=1, orient=tk.HORIZONTAL, length=150, showvalue=0,
                             tickinterval=1, resolution=0.01, command=inter_w_scale_arg)
    inter_w_text = tk.Label(master=window, text='横间隔', width=5, height=1, font=13)
    inter_h_scale = tk.Scale(master=window, from_=0, to=1, orient=tk.HORIZONTAL, length=150, showvalue=0,
                             tickinterval=1, resolution=0.01, command=inter_h_scale_arg)
    inter_h_text = tk.Label(master=window, text='纵间隔', width=5, height=1, font=13)
    row_plus_button = tk.Button(master=window, text='+', width=3, height=1, command=lambda: up_row(row_num))
    row_minus_button = tk.Button(master=window, text='-', width=3, height=1, command=lambda: down_row(row_num))
    col_plus_button = tk.Button(master=window, text='+', width=3, height=1, command=lambda: up_col(col_num))
    col_minus_button = tk.Button(master=window, text='-', width=3, height=1, command=lambda: down_col(col_num))
    input_button = tk.Button(master=window, text='导入', width=3, height=1, command=lambda: select_path())
    output_button = tk.Button(master=window, text='导出', width=3, height=1, command=lambda: output_img())
    row_plus_button.place(x=150, y=50, anchor='nw')
    row_minus_button.place(x=250, y=50, anchor='nw')
    row_num.place(x=200, y=50, anchor='nw')
    row_text.place(x=10, y=50, anchor='nw')
    col_plus_button.place(x=150, y=100, anchor='nw')
    col_minus_button.place(x=250, y=100, anchor='nw')
    col_num.place(x=200, y=100, anchor='nw')
    col_text.place(x=10, y=100, anchor='nw')
    pic_width_scale.place(x=140, y=150, anchor='nw')
    pic_width_text.place(x=10, y=150, anchor='nw')
    pic_height_scale.place(x=140, y=200, anchor='nw')
    pic_height_text.place(x=10, y=200, anchor='nw')
    ini_x_scale.place(x=140, y=250, anchor='nw')
    ini_x_text.place(x=10, y=250, anchor='nw')
    ini_y_scale.place(x=140, y=300, anchor='nw')
    ini_y_text.place(x=10, y=300, anchor='nw')
    inter_h_scale.place(x=140, y=350, anchor='nw')
    inter_h_text.place(x=10, y=350, anchor='nw')
    inter_w_scale.place(x=140, y=400, anchor='nw')
    inter_w_text.place(x=10, y=400, anchor='nw')
    input_button.place(x=80, y=450, anchor='nw')
    output_button.place(x=200, y=450, anchor='nw')
    return window
