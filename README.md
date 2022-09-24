# intelligent-placer

## Постановка задача.
Имеется выборка предметов. На вход поступает фотография на светлой горизонтальной поверхности с многоугольником произвольного размера, нарисованным на листе А4, и несколькими предметами из выборки. Лист с многоугольником и хотя бы один предмет обязательно должны присутствовать на фотографии. Требуется по фотографии понять, помещаются ли предметы внутрь многоугольника. Предметы помещаются внутрь, если их можно расположить так, что никакая часть предметов не выходит за границы многоугольника.

## Требования.
### Общие требования.

* Программа получает на вход путь до изображения со всеми объектами и нарисованным на листе многоугольником

* Программа должна возвращаться true-в случае, если предметы помещаются в многоугольник и false-в противном случае

* Ответ выводится в стандартный поток вывода

* На вход подаётся путь до изображения со всеми объектами и нарисованным на листе многоугольником
### Для фотографий.

* Изображение резкое, без смазанных фрагментов, не шумное

* Изображения должны подаваться в формате *.jpg

* Фотографии сделаны под прямым углом к нормали поверхности с допущением небольшого отклонения до 10°

* На фотографии должны быть четко различимы предметы и многоугольники

* Многоугольник и предмет должны помещаться на фото

* Предметы должны находиться за пределами многоугольника

* Лист с многоугольником должен полностью помещаться на фотографии

### Для многоугольников

* Границы многоугольника должны быть четко видны и обозначены черным цветом

* Многоугольник должен быть выпуклым и замкнутым
### Для предметов

* Предмет не должен сливаться с фоном

* Предметы не пересекаются друг с другом и не имеют общих границ

* Предметы должны отличаться друг от друга

## Изображения предметов

[Исходные данные](https://github.com/semen200251/intelligent-placer/tree/develop/Фотки%20предметов)

## Тесты

[Проверка на то что 1 маленький объект может поместиться в большой многоугольник](https://github.com/semen200251/intelligent-placer/blob/develop/Фотки%20тестов/SDmo5pa7pqvRDceQ2N6mXqIkcBwr1MXsLtJNATYJJkGzRuVTEkAJ9nYi8WyvV0bzF7ElGOcjrDamB6Bdu9prRTKX.jpg)

Ответ: true


[Проверка на то что все имеющиеся объекты могут уложиться в наибольший (по площади) многоугольник](https://github.com/semen200251/intelligent-placer/blob/develop/Фотки%20тестов/1GwIbwEJm018Q00Qt7uXpukXFlGNTZX1F-3CrRc_AVfnK3hoMW39QFRLNa0iRAj-UZdW_VKLAEfpsKLSb4OQoVCQ.jpg)

Ответ: false

[Проверка на то что объект еле-еле но вмещается](https://github.com/semen200251/intelligent-placer/blob/develop/Фотки%20тестов/rhN1hEeChoxo9DkkNEyiFOXEeA6agHlR3pf4fphWovMG4x9dMzWm-wgwtYCekRhbKgqYjL61ePpaun8t-yyyUm8A.jpg)

Ответ: true

[Проверка на то что объект уже не вмещается](https://github.com/semen200251/intelligent-placer/blob/develop/Фотки%20тестов/LbsFFZp3LNGp2FDpM-0GuYlOHsUVxye5nt-btvmbhjwoC2Uc9PAABDZOJc3cEqwqWJBpvVPZPJ4zKcnPQYCBXvIS.jpg)

Ответ: false

[Проверка поведения при отсутствии многоугольника](https://github.com/semen200251/intelligent-placer/blob/develop/Фотки%20тестов/F8q-QWiw36gWLAYcn2Oi-fUuX16gD1Do_808LHzKYe5nVbs6pG4E5mZnBu-XzsvTj6_zK2TSSnHTlIEYVXAJ7rMM.jpg)

Ответ: false

[Проверка поведения при отсутствии объектов](https://github.com/semen200251/intelligent-placer/blob/develop/Фотки%20тестов/Md0mPDT6P1mywEtS4jZwdci-KQY4u6U2pftDeGe3wQPGGOLZyQbGGuglhCrF2cIHT1sDz02o6s1OsF3aCCdHlFHy.jpg)

Ответ: True

[Проверка поведения при невыпуклом многоугольнике](https://github.com/semen200251/intelligent-placer/blob/develop/Фотки%20тестов/Md0mPDT6P1mywEtS4jZwdci-KQY4u6U2pftDeGe3wQPGGOLZyQbGGuglhCrF2cIHT1sDz02o6s1OsF3aCCdHlFHy.jpg)

Ответ: false

[Проверка двух объектов, каждый по отдельности помещается, но вместе нет](https://github.com/semen200251/intelligent-placer/blob/develop/Фотки%20тестов/uzVXCTgZxgKSTqxZ3mr2zdJJd3-yN8osLzQtmrh6pbQUHJIcqnPQyCI8a73kHIRu0AA1gR8JR3nV0bKay3ZFguIZ.jpg)

Ответ: false

[Проверка двух объектов, каждый по отдельности помещается, и вместе тоже](https://github.com/semen200251/intelligent-placer/blob/develop/Фотки%20тестов/UaKQ5gaaQZMkQ3TmzVtgir0TvE9pEEkfnM7udKJeKyu1-0w-dkhf77sZClE07Zkp6dvVXA8y_fsU4xVvCJ7SdEne.jpg)

Ответ: True

[Проверка двух объектов, один помещается, а другой нет](https://github.com/semen200251/intelligent-placer/blob/develop/Фотки%20тестов/s5SZ0zqZz3Guj0BAWq6qLsUU8le5wx6GuS5tHFqMYeUffeezu8ykxNy7SSyyOveGmhge7iGkRRRha5eO8tWj7ZKM.jpg)

Ответ: false

[Проверка двух объектов, оба не помещаются](https://github.com/semen200251/intelligent-placer/blob/develop/Фотки%20тестов/guZlC6qdUOOnrKRi9cq_IYpRYx8pEwWmGtBW7yxOq3V87Je9nTmfd_2c0B6x_xV3bPP3S_aT0vToLEAZu4Vbh4CE.jpg)

Ответ: false
