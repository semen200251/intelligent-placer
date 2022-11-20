import cv2
import matplotlib.pyplot as plt


def getMasks(image):
    cop = image.copy()

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # преобразование фотографии из одного цветового пространства в другое

    blur = cv2.GaussianBlur(gray, (1, 1), 0)  # удаление гауссовского шума, блюр картинки

    edged = cv2.Canny(blur, 100, 400)  # определение границ объектов на фотографии

    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (15, 15))  # задание ядра

    closed = cv2.morphologyEx(edged, cv2.MORPH_CLOSE, kernel)  # удаление шумов внутри объекта

    contours, _ = cv2.findContours(closed, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)  # поиск контуров

    for c in contours:
        if cv2.contourArea(c) > 1000:
            cv2.drawContours(image, [c], -1, (0, 255, 0), 2)  # построение контуров
            cv2.fillPoly(closed, pts=[c], color=(255, 0, 0))  # заливка контуров внутри

    imageContours = image

    return cop, closed, imageContours


def findImages(path):
    paths = []

    for pTest in path.glob("*.jpg"):
        paths.append(pTest)

    return paths


def paintImages(pathToImage):
    image = cv2.imread(pathToImage)
    cop = image.copy()
    _, binary, contours = getMasks(image)

    imgs = []
    imgs.append(cop)
    imgs.append(binary)
    imgs.append(contours)

    axs = plt.subplots(1, 3, figsize=(12, 12))[1]
    axs = axs.flatten()

    for im, ax in zip(imgs, axs):
        ax.imshow(im)

    axs[0].set_title("image")
    axs[1].set_title("binary")
    axs[2].set_title('contours')

    return


def checkSquare(contours):
    figSqr = 0  # площадь многоугольника
    sumObj = 0  # площадь всех объектов

    for c in contours:  # для всех контуров, которые были найдены
        if cv2.contourArea(c) > 1000:  # для контуров, площадь которых больше 1000. Чтобы убрать лишние контуры, которые не являются ни объектами, ни фигурой
            if figSqr == 0:  # так как контуры расположены снизу вверх, то первым определяется площадь фигуры, так как в требовании предметы должны находиться выше листа с многоугольником
                figSqr = cv2.contourArea(c)
            else:
                sumObj = cv2.contourArea(c)  # суммируются все остальные контуры, которые являются предметами

    if sumObj > figSqr:
        print("false")
    if sumObj == 0:
        print("false")


paintImages("C:\\Users\\semen\\intelligent-placer\\images\\object1.jpg")
