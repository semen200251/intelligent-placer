# intelligent-placer

## Постановка задача.
Имеется выборка предметов. На вход поступает фотография на светлой горизонтальной поверхности с многоугольником произвольного размера, нарисованным на листе А4, и несколькими предметами из выборки. Лист с многоугольником и хотя бы один предмет обязательно должны присутствовать на фотографии. Требуется по фотографии понять, помещаются ли предметы внутрь многоугольника. Предметы помещаются внутрь, если их можно расположить так, что никакая часть предметов не выходит за границы многоугольника.

## Требования.
### Общие требования.

* Программа получает на вход путь до изображения со всеми объектами и нарисованным на листе многоугольником

* Программа должна возвращаться true-в случае, если предметы помещаются в многоугольник и false-в противном случае

* Ответ выводится в стандартный поток вывода

### Для фотографий.

* Изображение резкое, без смазанных фрагментов, не шумное

* Изображения должны подаваться в формате *.jpg

* Фотографии сделаны под прямым углом к нормали поверхности с допущением небольшого отклонения до 10°

* Предметы не пересекаются друг с другом и не имеют общих границ

* Предметы должны отличаться друг от друга, то есть иметь разную форму, разный цвет

* Многоугольник и предметы должны помещаться на фото

* Предметы должны находиться за пределами многоугольника

* Лист с многоугольником должен полностью помещаться на фотографии

### Для многоугольников

* Границы многоугольника должны быть четко видны и обозначены черным цветом

* Многоугольник должен быть выпуклым и замкнутым

### Для предметов

* Предмет не должен сливаться с фоном


## Изображения предметов

[Исходные данные](https://github.com/semen200251/intelligent-placer/tree/develop/Фотки%20предметов)

## Тесты

[Проверка на то что 1 маленький объект может поместиться в большой многоугольник](https://github.com/semen200251/intelligent-placer/blob/develop/Фотки%20тестов/test1.jpg)

Ответ: true


[Проверка на то что все имеющиеся объекты могут уложиться в наибольший (по площади) многоугольник](https://github.com/semen200251/intelligent-placer/blob/develop/Фотки%20тестов/test2.jpg)

Ответ: false

[Проверка на то что объект еле-еле но вмещается](https://github.com/semen200251/intelligent-placer/blob/develop/Фотки%20тестов/test3.jpg)

Ответ: true

[Проверка на то что объект уже не вмещается](https://github.com/semen200251/intelligent-placer/blob/develop/Фотки%20тестов/test4.jpg)

Ответ: false

[Проверка поведения при отсутствии многоугольника](https://github.com/semen200251/intelligent-placer/blob/develop/Фотки%20тестов/test5.jpg)

Ответ: false

[Проверка поведения при отсутствии объектов](https://github.com/semen200251/intelligent-placer/blob/develop/Фотки%20тестов/test6.jpg)

Ответ: True

[Проверка поведения при невыпуклом многоугольнике](https://github.com/semen200251/intelligent-placer/blob/develop/Фотки%20тестов/test7.jpg)

Ответ: false

[Проверка двух объектов, каждый по отдельности помещается, но вместе нет](https://github.com/semen200251/intelligent-placer/blob/develop/Фотки%20тестов/test8.jpg)

Ответ: false

[Проверка двух объектов, каждый по отдельности помещается, и вместе тоже](https://github.com/semen200251/intelligent-placer/blob/develop/Фотки%20тестов/test9.jpg)

Ответ: True

[Проверка двух объектов, один помещается, а другой нет](https://github.com/semen200251/intelligent-placer/blob/develop/Фотки%20тестов/test10.jpg)

Ответ: false

[Проверка двух объектов, оба не помещаются](https://github.com/semen200251/intelligent-placer/blob/develop/Фотки%20тестов/test11.jpg)

Ответ: false
