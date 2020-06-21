import json

filename = '3'
height = 768
width = 768
file = open(filename+'.txt', mode='r',encoding='utf-8')



itemArray = []
for item in file: #read in the file without RGB and dimensions
    if(len(item) > 4):
        newItem = item.replace("\n", "")
        itemArray.append(newItem)

# gray = (red + green + blue) / 3 SIMPLE AVERAGE
# gray = (.25 * red) + (.5 * green) + (.25 * blue) MEDIUM AVERAGE
# gray = (.299 * red) + (.587 * green) + (.114 * blue) HARD AVERAGE


f = open("Hard_Average_"+filename+".txt", 'w')
f.write("RGB\n")
f.write("768\n")
f.write("768\n")

for item in itemArray:#write to new file, use len to figure out how to read the string
    if(len(item) == 11): # "251 251 251"
        red = int(item[0:3])
        green = int(item[4:7])
        blue = int(item[8:11])
        gray = str(int((.299 * red) + (.587 * green) + (.114 * blue)))
        grayScale = gray + " " + gray + " " + gray + "\n"
        f.write(grayScale)

    elif(len(item) == 10): #"155 128 99"
        red = int(item[0:3])
        green = int(item[4:6])
        blue = int(item[7:9])
        gray = str(int((.299 * red) + (.587 * green) + (.114 * blue)))
        grayScale = gray + " " + gray + " " + gray + "\n"
        f.write(grayScale)
    elif(len(item) == 9):#"251 12 12"
        red = int(item[0:3])
        green = int(item[4:6])
        blue = int(item[7:9])
        gray = str(int((.299 * red) + (.587 * green) + (.114 * blue)))
        grayScale = gray + " " + gray + " " + gray + "\n"
        f.write(grayScale)
    elif(len(item) == 8): #22 22 22

        red = int(item[0:2])
        green = int(item[3:5])
        blue = int(item[6:8])
        gray = str(int((.299 * red) + (.587 * green) + (.114 * blue)))
        grayScale = gray + " " + gray + " " + gray + "\n"
        f.write(grayScale)
    elif(len(item) == 7):
        red = int(item[0:2])
        green = int(item[3:5])
        blue = int(item[6:7])
        gray = str(int((.299 * red) + (.587 * green) + (.114 * blue)))
        grayScale = gray + " " + gray + " " + gray + "\n"
        f.write(grayScale)
    elif(len(item) == 6):
        red = int(item[0:2])
        green = int(item[3:4])
        blue = int(item[5:6])
        gray = str(int((.299 * red) + (.587 * green) + (.114 * blue)))
        grayScale = gray + " " + gray + " " + gray + "\n"
        f.write(grayScale)
    else: # "0 0 0"
        red = int(item[0])
        green = int(item[2])
        blue = int(item[4])
        gray = str(int((.299 * red) + (.587 * green) + (.114 * blue)))
        grayScale = gray + " " + gray + " " + gray + "\n"
        f.write(grayScale)


