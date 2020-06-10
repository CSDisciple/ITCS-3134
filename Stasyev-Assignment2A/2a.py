import json

filename = 'ostasyev_medium'
height = 512
width = 512
row1 = [[0, 0, 1], [0, 1, 0], [0, 0, 1], [0, 1, 0]]
row2 = [[0, 1, 0], [1, 0, 0], [0, 1, 0], [1, 0, 0]]

# def pick_color(row):
#     current_color = 'blue'
#
#
#     if (row[index].index(1) == 0):
#         value = 'red'
#         final_output = number_as_string + ' 0 0'
#
#     elif (row[index].index(1) == 1):
#         value = 'green'
#         final_output = '0 ' + number_as_string + ' 0'
#
#     elif (row[index].index(1) == 2):
#         value = 'blue'
#         final_output = '0 0 ' + number_as_string
#     return final_output


with open(filename + '.txt', 'r') as file:
    content_list = json.load(file)

    with open("output.txt", 'w') as out_file:
        out_file.write("RGB\n")
        out_file.write(str(height) + "\n")
        out_file.write(str(width) + "\n")


        size = height * width
        stackIntensities = []
        i = 0
        for x in range(0, size, width + i):
            i = x
            print(x)
            row = []
            for x in range(x, width + x, 1):
                row.append(content_list[x])
            stackIntensities.append(row)

        currentRow = 'BlueGreen'

        for row in stackIntensities:
            if (currentRow == 'BlueGreen'):
                currentColor = "blue"
                for intensity in row:
                    intensityString = str(intensity)
                    if (currentColor == 'blue'):
                        out_file.write('0 0 ' + intensityString+'\n')
                        currentColor = 'green'

                    else:
                        out_file.write('0 ' + intensityString + ' 0'+'\n')
                        currentColor = 'blue'


                currentRow = 'GreenRed'
            else:
                currentColor = 'green'
                for intensity in row:
                    intensityString = str(intensity)
                    if (currentColor == 'green'):
                        out_file.write('0 ' + intensityString + ' 0'+'\n')

                        currentColor = 'red'
                    else:
                        out_file.write(intensityString + ' 0 0'+'\n')
                        currentColor = 'green'

                currentRow = 'BlueGreen'

print('File has been converted.')
