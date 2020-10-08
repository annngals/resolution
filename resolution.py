import numpy as np
import matplotlib.pyplot as plt

def load_image(filename):
    
    file = open(filename)
    width = float(file.readline())
    lines = file.readlines()[1:] 
    file.close()

    image = []
    for line in lines:
        line = line.split()
        image.append(line)

    return width, np.array(image, dtype='int32')

w1, img1 = load_image('figure1.txt')
w2, img2 = load_image('figure2.txt')
w3, img3 = load_image('figure3.txt')
w4, img4 = load_image('figure4.txt')
w5, img5 = load_image('figure5.txt')
w6, img6 = load_image('figure6.txt')


plt.subplot(161)
plt.imshow(img1)

plt.subplot(162)
plt.imshow(img2)

plt.subplot(163)
plt.imshow(img3)

plt.subplot(164)
plt.imshow(img4)

plt.subplot(165)
plt.imshow(img5)

plt.subplot(166)
plt.imshow(img6)

def count_resolution(w, image):

    max_row = 0

    for y in range(image.shape[0]):
        if max_row < np.sum(image[y]):
            max_row = np.sum(image[y])

    if max_row == 0:
        return 0

    return w/max_row

print('Resolution1:', count_resolution(w1, img1))
print('Resolution2:', count_resolution(w2, img2))
print('Resolution3:', count_resolution(w3, img3))
print('Resolution4:', count_resolution(w4, img4))
print('Resolution5:', count_resolution(w5, img5))
print('Resolution6:', count_resolution(w6, img6))
