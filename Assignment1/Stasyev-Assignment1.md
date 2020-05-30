
Oleksandr Stasyev
Professor Dhruv Dhamani
ITCS-3134-080
05/29/20

 - What object was inside your `_easy.txt` file? (ball, brick, or cylinder) Attach a screenshot of your visualization, and any code you wrote to do the same. [30 points]
  
 	- The represented image below showcases a clear case of a `cylinder` which was extracted from a txt file with the help of Excel. Excel was used for its Conditional Formatting feature which allowed us to create the image above.
 	![Cylinder](https://github.com/CSDisciple/ten-iq/blob/master/ostasyev-easy.gif?raw=true)


-   What object was inside your `_medium.txt` file? (ball, brick, or cylinder) Attach a screenshot of your visualization, and any code you wrote to do the same. [20 points]
	- The picture in the medium text file seemed to represent a brick as it did not fit any other given description.
![Brick](https://github.com/CSDisciple/ten-iq/blob/master/ostasyev-medium.gif?raw=true)

-   What object was inside your `_hard.txt` file? (ball, brick, or cylinder) Attach a screenshot of your visualization, and any code you wrote to do the same. It is unlikely any of the aforementioned methods would let you guess at what object was in there, to attempt this question you'd hopefully will need to do a little research. [10 extra credits]
	- Last is a quite large image, but based on Excel Conditional Formatting feature and a bit of Python it can be derived from the hard.txt file that the image is of a `Crayola Chalk 12 piece pack`
	![Crayola Chalk 12 pack](https://github.com/CSDisciple/ten-iq/blob/master/ostasyev-hard.gif?raw=true)
### The python code used

 

    import json  
  
    with open('ostasyev_hard.txt', 'r') as file:  
        content_list = json.load(file)  

    print(f"print the first element in the list: {content_list[0]}")  
  
    with open("out.txt", 'w') as out_file:  
      i = 0  
      for number in content_list:  
	      i = i+1  
	      element_as_string = str(number)  
	       # prints the element and adds a comma and a new line after 256 elements
	      out_file.write(element_as_string+', ')  
	                if(i%256==0):  
	                    out_file.write('\n')

