import cv2


def prepareImage(img):
    """Convert image to gray, apply adaptive inverse threshold, remove salt-and-pepper noise and return the image"""
    grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(grey, 0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
    # TODO: parametrise MedianFilter size based on image dim/resolution
    filtered = cv2.medianBlur(thresh, 9)
    return filtered

def findContours(img):
    """Find the contours of all white objects in the image and return them in no particular order"""
    contours, _ = cv2.findContours(img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    return contours

def getAreaAndCentroid(contour):
    """Given a contour, return area, x-position and y-position (centroid)"""
    moments = cv2.moments(contour)
    area = moments['m00']
    x = moments['m10']/area
    y = moments['m01']/area
    return area, x, y
