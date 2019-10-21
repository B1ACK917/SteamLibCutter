from SteamLibCutter import data_str as d
import cv2
import imageio

rectangle_list = []
gif_frame = []
gif_time_gap = 0


def pre_cut_one_frame(frame, row, col, width, height, x_, y_, inter_w, inter_h):
    global rectangle_list
    res = frame.copy()
    rectangle_list = []
    for i in range(row):
        new_list = []
        for j in range(col):
            pt = d.Point(x_ + (width + inter_w) * j, y_ + (height + inter_h) * i)
            rec = d.Rectangle(pt, width, height)
            new_list.append(rec)
        rectangle_list.append(new_list)
    for rec_row in rectangle_list:
        for item in rec_row:
            lt, rb = item.get()
            cv2.rectangle(res, lt.get_xy(), rb.get_xy(), (255, 0, 0))
    return res


def cut_frame(frame, width, height):
    res_container = []
    for rec_row in rectangle_list:
        for item in rec_row:
            lt = item.get_lt()
            x_, y_ = lt.get_xy()
            temp_img = frame[y_:y_ + height, x_:x_ + width]
            res_container.append(temp_img)
    return res_container


def write_sta(filename, container, row, col):
    it = filename.find('.')
    path_bg = filename[:it]
    path_ed = filename[it:]
    for i in range(row):
        for j in range(col):
            temp_img = container[i * col + j]
            cv2.imwrite(path_bg + '_' + str(i) + '_' + str(j) + path_ed, temp_img)


def readgif(filename):
    global gif_time_gap
    gif = cv2.VideoCapture(filename)
    fps = gif.get(cv2.CAP_PROP_FPS)
    gif_time_gap = 1.0 / fps
    res, img = gif.read()
    frame = img
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    gif_frame.append(img)
    while 1:
        res, img = gif.read()
        if res:
            img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
            gif_frame.append(img)
        else:
            break
    return frame


def cut_gif(width, height, row, col):
    gif_container = []
    for i in range(row):
        for j in range(col):
            gif_container.append([])

    for frame in gif_frame:
        container = cut_frame(frame, width, height)
        for i in range(row):
            for j in range(col):
                idx = i * col + j
                temp_img = container[idx]
                gif_container[idx].append(temp_img)
    return gif_container


def write_dyn(filename, container, row, col):
    it = filename.find('.')
    path_bg = filename[:it]
    # path_ed = filename[it:]
    path_ed = '.png'
    for i in range(row):
        for j in range(col):
            gif_container = container[i * col + j]
            imageio.mimsave(path_bg + '_' + str(i) + '_' + str(j) + path_ed, gif_container, 'GIF',
                            duration=gif_time_gap)
