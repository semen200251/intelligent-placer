import os
import matplotlib.pyplot as plt
from func import get_fill_masks, algorithm, painting


for n in range(1, 9):
    str = f"test{n}.jpg"
    img = plt.imread(os.path.join("tests", str))
    img, _, polys, _ = get_fill_masks(img.copy())
    success = False

    for t in range(0, 8):
        cnts = algorithm(polys[:])
        if cnts:
            success = True
            painting(img, polys, cnts)
            cnts.clear()
            break

    print(f"Test number {n} {success}")
