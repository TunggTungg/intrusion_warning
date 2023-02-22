
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon
import cv2
import numpy as np

def draw_polygon (frame, points):
    for point in points:
        frame = cv2.circle( frame, (point[0], point[1]), 5, (0,0,255), -1)

    frame = cv2.polylines(frame, [np.int32(points)], False, (255,0, 0), thickness=2)
    return frame

def check_polygon(point, polygon):
    point = Point(point[0], point[1])
    polygon = Polygon([p for p in polygon])
    return polygon.contains(point)