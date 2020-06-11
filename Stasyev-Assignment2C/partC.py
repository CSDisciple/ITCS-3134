import json

filename = 'ostasyev_hard'
height = 512
width = 512
print(height, width)

with open(filename + '.txt', 'r') as file:
    content_list = json.load(file)

    with open(filename+"_partC.txt", 'w') as out_file:
        out_file.write("RGB"+"\n")
        out_file.write(str(height-1) + "\n")
        out_file.write(str(width-1) + "\n")

        size = height * width
        stackIntensities = []
        sizeCheck = []
        i = 0
        for x in range(0, size, width + i):
            i = x

            row = []
            for x in range(x, width + x, 1):
                row.append(content_list[x])

            stackIntensities.append(row)

        rowType = "TypeA"

        for i in range(0, height-1, 1):
            row1 = stackIntensities[i]
            row2 = stackIntensities[i+1]
            if rowType == "TypeA":
                gridType = "GridA"
                for j in range(0, width-1, 1):
                    if  gridType == "GridA":
                        blue = row1[j]
                        green1 = row1[j+1]
                        green2 = row2[j]
                        red = row2[j+1]

                        green = int((green1 + green2) / 2)

                        pixel = str(red) + " " + str(green) + " " + str(blue)

                        sizeCheck.append(pixel)
                        out_file.write(pixel+"\n")
                        gridType = "GridB"
                    else:
                        green1 = row1[j]
                        blue = row1[j + 1]
                        red = row2[j]
                        green2 = row2[j + 1]

                        green = int((green1 + green2) / 2)

                        pixel = str(red) + " " + str(green) + " " + str(blue)

                        sizeCheck.append(pixel)
                        out_file.write(pixel + "\n")

                        gridType = "GridA"

                rowType = "TypeB"
            else:
                gridType = "GridA"
                for j in range(0, width - 1, 1):
                    if gridType == "GridA":
                        green1 = row1[j]
                        red = row1[j + 1]
                        blue = row2[j]
                        green2 = row2[j + 1]

                        green = int((green1 + green2) / 2)

                        pixel = str(red) + " " + str(green) + " " + str(blue)
                        sizeCheck.append(pixel)
                        out_file.write(pixel + "\n")

                        gridType = "GridB"
                    else:
                        red = row1[j]
                        green1 = row1[j + 1]
                        green2 = row2[j]
                        blue = row2[j + 1]

                        green = int((green1 + green2) / 2)

                        pixel = str(red) + " " + str(green) + " " + str(blue)
                        sizeCheck.append(pixel)
                        out_file.write(pixel + "\n")

                        gridType = "GridA"

                rowType = "TypeA"

print(len(sizeCheck))
print('File has been converted.')
