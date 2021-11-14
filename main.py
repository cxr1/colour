import webcolors
import time
import pyautogui
import tkinter as tk


def getRealtimeMouseCoordinates():
    try:
        xOld = 0
        yOld = 0
        while True:
            xNew, yNew = pyautogui.position()
            if xOld != xNew and yOld != yNew:
                xOld = xNew
                yOld = yNew
                screenshot = pyautogui.screenshot()
                color = screenshot.getpixel((xNew, yNew))
                #print('X:', '{:>4}'.format(xNew), ', Y:', '{:>4}'.format(yNew), ', RGB:',
                      #'({:>3}, {:>3}, {:>3})'.format(color[0], color[1], color[2]))

                def closest_colour(requested_colour):
                    min_colours = {}
                    for key, name in webcolors.css3_hex_to_names.items():
                        r_c, g_c, b_c = webcolors.hex_to_rgb(key)
                        rd = (r_c - requested_colour[0]) ** 2
                        gd = (g_c - requested_colour[1]) ** 2
                        bd = (b_c - requested_colour[2]) ** 2
                        min_colours[(rd + gd + bd)] = name
                    return min_colours[min(min_colours.keys())]

                def get_colour_name(requested_colour):
                    try:
                        closest_name = actual_name = webcolors.rgb_to_name(requested_colour)
                    except ValueError:
                        closest_name = closest_colour(requested_colour)
                        actual_name = None
                    return actual_name, closest_name

                requested_colour = (color[0], color[1], color[2])
                actual_name, closest_name = get_colour_name(requested_colour)
                print("实际颜色:", actual_name, ", 最接近的颜色:", closest_name)
    except KeyboardInterrupt:
        print('Exit')


if __name__ == '__main__':
    getRealtimeMouseCoordinates()
