#!/usr/bin/python
"""Dewarp a given image."""

# -*- coding: utf-8 -*-
# -----------------------------------------
# author      : Ahmet Ozlu
# mail        : ahmetozlu93@gmail.com
# date        : 05.05.2019
# -----------------------------------------

import cv2
import imutils
import numpy as np
from utils.transform import four_point_transform


def dewarp_book(image):
    """Fix and image warp (dewarp an image).

    Parameters
    ----------
    image : numpy ndarray
        The input image.

    Returns
    -------
    numpy ndarray
        The dewarped image.

    """
    # get input image ration to keep best output resolution quality
    ratio = image.shape[0] / 500.0
    # copy source image for filter operations
    orig = image.copy()
    # resize the input image
    image = imutils.resize(image, height=500)

    # convert rgb input image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (5, 5), 0)

    # sigma parameter is used for automatic Canny edge detection
    sigma = 0.33

    # compute the median of the single channel pixel intensities
    v = np.median(image)

    # apply automatic Canny edge detection using the computed median
    lower = int(max(0, (1.0 - sigma) * v))
    upper = int(min(255, (1.0 + sigma) * v))
    edged = cv2.Canny(image, lower, upper)

    # perform dilate morphological filter to connect teh image pixel points
    '''kernel = np.ones((5,5),np.uint8)
    edged = cv2.dilate(edged,kernel,iterations = 1)'''

    # find contours
    cnts = cv2.findContours(edged.copy(), cv2.RETR_LIST,
                            cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    cnts = sorted(cnts, key=cv2.contourArea, reverse=True)[:5]
    # loop over the contours
    for c in cnts:
        peri = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.02 * peri, True)

        if len(approx) == 4:
            screenCnt = approx
            break
    # apply the four point transform for book dewarping
    warped = four_point_transform(orig, screenCnt.reshape(4, 2) * ratio)
    return warped
