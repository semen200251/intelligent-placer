from random import randint

import matplotlib
from matplotlib import pyplot as plt
from matplotlib.patches import Rectangle
from matplotlib import animation

# операции над матрицами
import numpy as np

# загрузка и сохранение изображений
from imageio import imread, imsave

# работа над изображениями
from skimage.color import rgb2gray, rgba2rgb
from skimage.feature import canny
from skimage.filters import sobel, gaussian, threshold_local, try_all_threshold, threshold_otsu, threshold_isodata
from skimage.data import page
from skimage.morphology import binary_opening, binary_dilation, binary_erosion, binary_closing
from skimage.measure import regionprops
# импортируем функцию label под другим именем, чтобы не терять её, если появляется переменная label
from skimage.measure import label as sk_measure_label
import cv2

# вывод
from IPython.display import HTML

# работа с таблицами
import pandas as pd

# для работы с путями к файлам
import os


def get_edges(image):
    gray = cv2.cvtColor(image,
                        cv2.COLOR_BGR2GRAY)  # преобразование фотографии из одного цветового пространства в другое
    blur = cv2.GaussianBlur(gray, (1, 1), 0)  # удаление гауссовского шума, блюр картинки
    edged = cv2.Canny(blur, 100, 400)  # определение границ объектов на фотографии
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (7, 7))  # задание ядра
    return cv2.morphologyEx(edged, cv2.MORPH_CLOSE, kernel)  # удаление шумов внутри объекта


def get_cut_images(image, closed, contours):
    height, width = image.shape[:2]
    for cnt in contours:
        if cv2.contourArea(cnt) > (height - 200) * (width - 200):
            x, y, w, h = cv2.boundingRect(cnt)
            image = image[y + 50:y + h - 50, x + 50:x + w - 50]
            closed = closed[y + 50:y + h - 50, x + 50:x + w - 50]
            contours, _ = cv2.findContours(closed.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            break
    return image, closed, contours


def draw_contours_mask(binary, contours):
    # зададим список для найденных масок
    masks_coords = []
    # а также для контуров
    cnts = []
    for cnt in contours:
        area = cv2.contourArea(cnt)
        # обнаруженные небольшие дефекты исключаем, задав минимальную площадь
        if area > 1000:
            cnts.append(cnt)
            peri = cv2.arcLength(cnt, True)
            # аппроксимируем найденный контур многоугольником
            approx = cv2.approxPolyDP(cnt, 0.000001 * peri, True)
            masks_coords.append(approx)
            cv2.drawContours(binary, [approx], -1, (0, 0, 0), 5)
            cv2.fillPoly(binary, pts=[approx], color=(0, 0, 0))
    return cnts, masks_coords, binary


def checkSquare(contours):
    figSqr = 0  # площадь многоугольника
    sumObj = 0  # площадь всех объектов

    for c in contours:  # для всех контуров, которые были найдены
        if cv2.contourArea(
                c) > 1000:  # для контуров, площадь которых больше 1000. Чтобы убрать лишние контуры, которые не являются ни объектами, ни фигурой
            if figSqr == 0:  # так как контуры расположены снизу вверх, то первым определяется площадь фигуры, так как в требовании предметы должны находиться выше листа с многоугольником
                figSqr = cv2.contourArea(c)
            else:
                sumObj = cv2.contourArea(c)  # суммируются все остальные контуры, которые являются предметами


def get_fill_masks(image):
    # ищем границы
    closed = get_edges(image)
    # находим контуры
    contours, _ = cv2.findContours(closed.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    # если самый большой контур - это контур листа, то удаляем его и ищем внутренние контуры
    image, closed, cnt = get_cut_images(image, closed, contours)
    # применяем бинаризацию
    _, binary_img = cv2.threshold(image, 150, 250, cv2.THRESH_BINARY)
    binary = cv2.cvtColor(binary_img, cv2.COLOR_BGR2GRAY)
    cnts, masks_coords, binary = draw_contours_mask(binary, cnt)
    return image, binary, masks_coords, cnts


def myComb(polys):
    random_index = []
    i = 0
    while i < len(polys) - 1:
        random_index.append(randint(1, len(polys) - 1))
        i = i + 1
        for j in range(0, len(random_index)):
            if random_index[j] == random_index[i - 1] and j != i - 1:
                i = i - 1
                random_index.pop()
                break
    return random_index


def algorithm(polys):
    if len(polys) == 1:
        return False

    mypolys = []
    cnts = []
    coords_max = []
    random = myComb(polys[:])
    mypolys.append(polys[0])
    Hprev = []
    Wprev = []

    for i in range(0, len(random)):
        mypolys.append(polys[random[i]])

    for poly in mypolys:
        x, y, w, h = cv2.boundingRect(poly)
        coords_max.append(x)
        coords_max.append(y)
        coords_max.append(w)
        coords_max.append(h)

    coords_of_gran_x = coords_max[0]
    coords_of_gran_y = coords_max[1]
    coords_of_gran_w = coords_max[2]
    coords_of_gran_h = coords_max[3]
    start_pos_x = coords_of_gran_x
    start_pos_y = coords_of_gran_y
    level = 0
    countj = 0
    jstart = 0
    count = 0
    for i in range(1, len(mypolys)):

        if level == 0:
            if (coords_of_gran_x + coords_max[2 + 4 * i] > start_pos_x + coords_of_gran_w):
                Wprev.append(start_pos_x + coords_of_gran_w)
                Hprev.append(start_pos_y)
                coords_of_gran_x = start_pos_x
                level = 1
            if (coords_of_gran_y + coords_max[3 + 4 * i] > start_pos_y + coords_of_gran_h):
                return False
        if level != 0:
            countj = jstart
            while True:
                while coords_max[2 + 4 * i] > Wprev[countj] - coords_of_gran_x:
                    countj = countj + 1
                    if countj > len(Wprev) - 1:
                        countj = countj - 1
                        break
                for k in range(jstart, countj + 1):
                    if coords_max[3 + 4 * i] > start_pos_y + coords_of_gran_h - Hprev[k]:
                        jstart = -1
                        break
                if jstart == -1:
                    count = count + 1
                    jstart = count
                    countj = count
                    coords_of_gran_x = Wprev[countj - 1]
                    if countj > len(Wprev) - 1:
                        return False
                else:
                    if coords_max[2 + 4 * i] > Wprev[countj] - coords_of_gran_x:
                        return False
                    a = Hprev[jstart]
                    for z in range(jstart + 1, countj + 1):
                        if a < Hprev[z]:
                            a = Hprev[z]
                    coords_of_gran_y = a
                    break
        if jstart == -1:
            return False
        razX = coords_of_gran_x - coords_max[4 * i]
        razY = coords_of_gran_y - coords_max[1 + 4 * i]
        cnts.append(mypolys[i])
        if level == 0:
            Hprev.append(coords_of_gran_y + coords_max[3 + 4 * i])
            Wprev.append(coords_of_gran_x + coords_max[2 + 4 * i])
        for j in range(len(mypolys[i])):
            cnts[len(cnts) - 1][j][0][0] = mypolys[i][j][0][0] + razX
            cnts[len(cnts) - 1][j][0][1] = mypolys[i][j][0][1] + razY
        if level == 0:
            coords_of_gran_x = coords_of_gran_x + coords_max[2 + 4 * i]
        else:

            Wprev.insert(countj, coords_of_gran_x + coords_max[2 + 4 * i])
            Hprev.insert(countj, coords_of_gran_y + coords_max[3 + 4 * i])
            for h in range(jstart, countj):
                Wprev.pop(jstart)
                Hprev.pop(jstart)
            jstart = 0
            count = 0

    return cnts


def painting(img, polys, cnts):
    bbox = img.copy()
    contours = img.copy()

    for poly in polys:
        x, y, w, h = cv2.boundingRect(poly)
        bbox = cv2.rectangle(bbox, (x, y), (x + w, y + h), (0, 0, 0), 5)
        cv2.drawContours(img, polys, -1, (255, 255, 255), 5)

    imgs = []
    imgs.append(img)
    imgs.append(bbox)

    cv2.drawContours(contours, cnts, -1, (255, 255, 255), 5)

    imgs.append(contours)
    _, axs = plt.subplots(1, 3, figsize=(12, 12))
    axs = axs.flatten()
    axs[0].set_title("Image")
    axs[1].set_title("With bbox")
    axs[2].set_title("With contours")

    for im, ax in zip(imgs, axs):
        ax.imshow(im)
    plt.show()

    imgs.pop()
