"""Adjust the brightness and contrast of an image."""
import cv2

contrast = 0
brightness = 0


def funcBrightContrast(img, bright=0):
    """Adjust the image contrast/brightness.

    Parameters
    ----------
    img : numpy ndarray
        The input image.
    bright : int
        The brightness level.

    Returns
    -------
    numpy ndarray
        The image whose brightness/contrast is adjusted.

    """
    effect = apply_brightness_contrast(img, bright, contrast)
    # save the final output image
    # cv2.imwrite("./outputs/" + output_img, effect)
    return effect


def apply_brightness_contrast(input_img, brightness=255, contrast=127):
    """Perform the color correction of an input image.

    Parameters
    ----------
    input_img : numpy ndarray
        The input image.
    brightness : int
        the brightness level.
    contrast : int
        the contrast level.

    Returns
    -------
    numpy ndarray
        The image whose brightness is adjusted .

    """
    brightness = 80
    contrast = 60

    # if brightness is not equal to 0
    if (brightness != 0):
        if (brightness > 0):
            shadow = brightness
            highlight = 255
        else:
            shadow = 0
            highlight = 255 + brightness
        # calculating the alpha value
        alpha_b = (highlight - shadow) / 255
        # set the gamma value
        gamma_b = shadow
        # to change the brightness in order to use the cv2.addWeighted()
        buf = cv2.addWeighted(input_img, alpha_b, input_img, 0, gamma_b)
    else:
        buf = input_img.copy()
    # if contrast does not equal 0
    if contrast != 0:
        f = float(131 * (contrast + 127)) / (127 * (131 - contrast))
        # calculating the alpha value
        alpha_c = f
        # set the gamma value
        gamma_c = 127*(1-f)
        # to change the contrast in order to use the cv2.addWeighted()
        buf = cv2.addWeighted(buf, alpha_c, buf, 0, gamma_c)
    # return color corrected image
    return buf
