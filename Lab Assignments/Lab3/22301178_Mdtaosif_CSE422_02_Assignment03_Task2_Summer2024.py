# -*- coding: utf-8 -*-
"""cse322lab3_2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1j-28Ywe1ZJ9isOPitT9IXvA79IHtMGTc
"""

def pacman_game(c):
    leaf_s = [3,6,2,3,7,1,2,0]
    l_two_l = [min(leaf_s[0:2]), min(leaf_s[2:4])]
    l_two_r = [min(leaf_s[4:6]), min(leaf_s[6:8])]
    max_l = max(l_two_l)
    max_r = max(l_two_r)
    ndm = max(max_r,max_l)

    dml = max(leaf_s[0:4]) - c
    dmr = max(leaf_s[4:8]) - c

    udm = max(dmr,dml)

    if udm > ndm:
        return f"The new minimax value is {udm}. Pacman goes right and uses dark magic."
    else:
        return f"The minimax value is {ndm}. Pacman does not use dark magic."

input_file=open("/content/22301178_MdTaosif_CSE422_02_Assignment03_task2_Summer2024_InputFile.txt","r")
arr=[]
for i in input_file:
    temp= i.split(" ")
    for j in temp:
        arr.append(int(j))
for i in arr:
    print(pacman_game(i))