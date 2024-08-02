# Write a program in python to read sort a list of integer elements using the bubble sort method. Display the sorted element on the screen.
def bubbleSort(nlist):
    for passnum in range(len(nlist) - 1, 0, -1):
        for i in range(passnum):
            if nlist[i] > nlist[i + 1]:
                temp = nlist[i]
                nlist[i] = nlist[i + 1]
                nlist[i + 1] = temp

nlist = [14, 46, 43, 27, 57, 41, 45, 21, 70]
bubbleSort(nlist)
print(nlist)   