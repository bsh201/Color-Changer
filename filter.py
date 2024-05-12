import json

import cv2
import numpy as np

import pandas as pd

# image = cv2.imread('image\image.png')

# with open ("_INTENSITY.json", "r") as f :
#     data = json.load(f)

# data = pd.DataFrame(data)
# INTENSITY = data['intensity']

################################## [case 1] ##################################

def make_filter(image, R, G, B) :
    height, width = image.shape[0], image.shape[1]

    red_filter = np.full((height, width, 3), (R, 0, 0), dtype=np.uint8)
    green_filter = np.full((height, width, 3), (0, G, 0), dtype=np.uint8)
    blue_filter = np.full((height, width, 3), (0, 0, B), dtype=np.uint8)

    filter = red_filter + green_filter + blue_filter
    return filter

def sample_image(image, filter) :
    blended = cv2.addWeighted(image, 0.8, filter, 0.2, 0)
    return blended

# image = cv2.resize(image, (800, 333))
# filter = make_filter(image)

# result = sample_image(image, filter)
# cv2.imshow('test',result)

# cv2.waitKey(0)
# cv2.destroyAllWindows()

################################## [case 1] ##################################


################################## [case 2] ##################################

# def make_red_filter(image) :
#     img = image.copy()
#     img[:, :, 0] = 0
#     img[:, :, 1] = 0
#     return img

# def make_green_filter(image) :
#     img = image.copy()
#     img[:, :, 0] = 0
#     img[:, :, 2] = 0
#     return img

# def make_blue_filter(image) :
#     img = image.copy()
#     img[:, :, 1] = 0
#     img[:, :, 2] = 0
#     return img

# def sample_image(image, INTENSITY) :

#     red_filter = make_red_filter(image)
#     blue_filter = make_blue_filter(image)
#     green_filter = make_green_filter(image)

#     blended = image*(1-sum(INTENSITY)) + red_filter*(INTENSITY[0])    \
#                                     + green_filter*(INTENSITY[1])  \
#                                     + blue_filter*(INTENSITY[2])
#     blended = blended.astype(np.uint8)
#     return blended

# sample_image = sample_image(image, INTENSITY)
# # sample_image = cv2.resize(sample_image, (800, 333))

# # red_filter = make_red_filter(sample_image)
# # blue_filter = make_blue_filter(sample_image)
# # green_filter = make_green_filter(sample_image)

# cv2.imshow('', sample_image)
# # cv2.imshow('red', red_filter)
# # cv2.imshow('blue', blue_filter)
# # cv2.imshow('green', green_filter)


# cv2.waitKey(0)
# cv2.destroyAllWindows()

################################## [case 2] ##################################