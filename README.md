# intelligent-placer

## Постановка задача.
Имеется выборка предметов. На вход поступает фотография на светлой горизонтальной поверхности с многоугольником произвольного размера, нарисованным на листе А4, и несколькими предметами из выборки. Требуется по фотографии понять, помещаются ли предметы внутрь многоугольника. Предметы помещаются внутрь, если их можно расположить так, что никакая часть предметов не выходит за границы многоугольника.

## Требования.
### Общие требования.

*Программа получает на вход путь до изображения со всеми объектами и нарисованным на листе многоугольником

*Программа должна возвращаться true-в случае, если предметы помещаются в многоугольник и false-в противном случае

*Ответ выводится в стандартный поток вывода
### Для фотографий.

*Изображение резкое, без смазанных фрагментов, не шумное

*Изображения должны подаваться в формате *.png

*Фотографии сделаны под прямым углом к нормали поверхности с допущением небольшого отклонения до 10°

*На фотографии должны быть четко различимы предметы и многоугольники

*Многоугольник и предмет должны помещаться на фото

*Предметы должны находиться за пределами многоугольника

### Для многоугольников

*Границы многоугольника должны быть четко видны и обозначены черным цветом

*Многоугольник должен быть выпуклым и замкнутым
### Для предметов

*Предмет не должен сливаться с фоном

*Предметы не пересекаются друг с другом и не имеют общих границ

*Предметы должны отличаться друг от друга

##Изображения предметов

[Исходные данные] (https://github.com/semen200251/intelligent-placer/tree/develop/Фотки%20предметов)

##Тесты

[Тесты] ()
