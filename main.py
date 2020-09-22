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
from Wrapper import Trapper
from Wrapper import triangle2D
# from Wrapper import triangle2DList

if __name__ == "__main__":
    file_path = "./resource/input.txt"
    wrapper = Trapper(file_path)
    triangle_pos_list = wrapper.FileToPositionArray()
    

    for i in range(0,len(triangle_pos_list)):
        triangle2DInstance = triangle2D(triangle_pos_list[i])
        print(triangle2DInstance.triangle2DList[i].getArea())
    # print(triangle2DInstance.triangle2DList[0].getArea())
    # print(triangle2DInstance.triangle2DList[0].getStdDev())

    # data = f.readlines()
    # triangle_pos_list=[]

    # for line in data:
    #     vertices=line.split()
    #     pose_array=[]
    #     for data in vertices:
    #         pos = data.split(',')
    #         #print(pos[1])
    #         for value in pos:
    #             pose_array.append(float(value))
    #     #print(pose_array)
    #     triangle_pos_list.append(pose_array)

    # print(triangle_pos_list[2][5])