# This is a sample Python script.
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
#def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
#    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
# Press the green button in the gutter to run the script.
#if __name__ == '__main__':
#    print_hi('PyCharm')
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
from Wrapper import Reader
from Wrapper import c_triangle2D
from Wrapper import c_vector
from Wrapper import c_matrix
from Wrapper import c_affine_transform
import math
import numpy as np
from matplotlib import pyplot as plt

# from Wrapper import triangle2DList

if __name__ == "__main__":
    # Read Triangle Information from input.txt
    file_path = "./resource/input.txt"
    wrapper = Reader(file_path)
    triangle_pos_list = wrapper.FileToPositionArray()
    # print(triangle_pos_list)
    # Register Triangle
    area_max = 0 # For pretty Frequency Table
    for i in range(0,len(triangle_pos_list)):
        triangle2DInstance = c_triangle2D(triangle_pos_list[i])
        if area_max<triangle2DInstance.getArea():
            area_max = triangle2DInstance.getArea()

    # Drawing Frequency Table
    interval_unit = 5 # set Frequency Table Interval
    number_unit = math.floor(area_max/interval_unit)
    count_list = []
    xlabel_list = []
    for i in range(0,number_unit+1):
        count_interval = 0
        for j in range(0,len(triangle_pos_list)):
            if i*interval_unit <= triangle2DInstance.triangle2DList[j].area < (i+1)*interval_unit:
                count_interval +=1
        count_list.append(count_interval)
        xlabel_list.append(str(i*interval_unit)+'-'+str((i+1)*interval_unit))



    """
    Plot Frequency Table
    """
    plt.figure(1)
    ax = plt.subplot()
    ax.bar(range(len(count_list)),count_list)
    plt.title('Frequency Table', pad = 10)
    plt.xlabel('Area', labelpad = 10)
    plt.ylabel('Number of Triangle',labelpad = 10)
    ax.set_xticks(range(0,len(count_list)))
    ax.set_xticklabels(xlabel_list)
    plt.show(block=False)

    """
    Problem 2
    """
    rotation_matrix = [[2, 0], [0, 2]]
    translation_matrix = [0, 1]
    plt.figure(2)
    for i in range(0, len(triangle_pos_list)):
        pos1 = [triangle_pos_list[i][0],triangle_pos_list[i][1]]
        pos2 = [triangle_pos_list[i][2],triangle_pos_list[i][3]]
        pos3 = [triangle_pos_list[i][4],triangle_pos_list[i][5]]

        c_translation_matrix = c_vector(translation_matrix)
        c_rotation_matrix = c_matrix(rotation_matrix)

        c_vec1 = c_affine_transform(pos1)
        c_vec2 = c_affine_transform(pos2)
        c_vec3 = c_affine_transform(pos3)

        c_vec1.affine_transform(c_rotation_matrix,c_translation_matrix)
        c_vec2.affine_transform(c_rotation_matrix,c_translation_matrix)
        c_vec3.affine_transform(c_rotation_matrix,c_translation_matrix)
        triangle2DInstance = c_triangle2D([c_vec1.x,c_vec1.y,c_vec2.x,c_vec2.y,c_vec3.x,c_vec3.y])
        triangle2DInstance.drawTriangle()
    plt.show()
