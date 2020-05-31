# Module 7 Assignment
- Script: [Assignment 7 Code](https://github.com/roslynm/IntroToProg-Python-Mod07/blob/master/Assignment07.py)
- Documentation: [Assignment 7 Document](https://github.com/roslynm/IntroToProg-Python-Mod07/blob/master/Assignment07.pdf)
  
## Script Background
In this assignment, I created a script that allows the user to enter in the day's temperature and dew point temperature in Fahrenheit. This data can be easily looked up on any typical weather website. The script uses this information to output the saturated vapor pressure, actual vapor pressure and relative humidty. 

*What do these values mean?*

Actual Vapor Pressure-->Actual vapor pressure is a measurement of the amount of water vapor in a volume of air and increases as the amount of water vapor increases.

Saturated Vapor Pressure-->as many molecules returning to the liquid as there are escaping. At this point the vapor is said to be saturated.

Relative humidity-->the ratio of the actual to the saturation vapor pressure.

*Why does Relative Humidity matter?*

Meteorologists often use the relative humidity as a measurement to describe the weather at various places. It is a way of describing how much humidity is present in the air, compared to how much there could be. It also is a key component in climate control settings. Whether you’re storing goods or maintaining a buldings or vehicle's climate, maintaining the correct relative humidity is the only way to ensure mold, mildew, condensation, and ice don’t interfere with your everyday business.

## Introduction
In this module, we continue to work with functions and continue to work with reading and writing to files. In this module, however, we learn how to pickle data into a file. This allows us to store more complex data stores, and access them easier. In this assignment, I have created a script that demonstrates pickling and shelving. As well as demonstrates error handling and how to use exception classes in order to error handle. We also learn more about the capabilities of GitHub, and how we can use markdown language to create a webpage. 

## Pickling
Pickling allows you to save files in binary format instead of plain text. Storing in binary obscures the files content and can reduce file size. In order to use pickling functionality, you must first import the pickle module. The pickle module allows you to pickle and store more complex data in a file. When writing to a file, you simply write the pickled object to the file. Pickled objects have to be stored as a binary file. They cannot be stored in a text file. 

For this assignment, I have created a script that asks the user to input today’s temperature and dew point temperature in Fahrenheit. The script then runs through some functions that convert the temperature to Celsius, then calculates the saturated vapor pressure, actual vapor pressure, and relativity humidity. In Figure 1, you will see the main script of the function. Figure 2 and 3 show the functions that gather input from the user, then process that data. 

![Figure 1. Main body of script](https://roslynm.github.io/IntroToProg-Python-Mod07/blob/master/Photos/Figure1.png "Figure 1")

Figure 1. Main body of script

![Figure 2. Functions that gather input from users and prints data back out](https://github.com/roslynm/IntroToProg-Python-Mod07/blob/master/Photos/Figure2.png "Figure 2. Functions that gather input from users and prints data back out")

Figure 2. Functions that gather input from users and prints data back out

![Figure 3. Functions that calculate temperature in Celsius, the saturated vapor pressure, the actual vapor pressure, and the relativity humidity](https://github.com/roslynm/IntroToProg-Python-Mod07/blob/master/Photos/Figure3.png "Figure 3. Functions that calculate temperature in Celsius, the saturated vapor pressure, the actual vapor pressure, and the relativity humidity")

Figure 3. Functions that calculate temperature in Celsius, the saturated vapor pressure, the actual vapor pressure, and the relativity humidity

In Figure 4, below, you can see the script running in PyCharm.

![Figure 4. Running script in PyCharm](https://github.com/roslynm/IntroToProg-Python-Mod07/blob/master/Photos/Figure4.png "Figure 4. Running script in PyCharm")

Figure 4. Running script in PyCharm

In the first run of this script, I will pickle the dictionary of weather data, dictWeather into the file. I will then load the dictionary object back from the file. You can see the functions that are executing in order to dump and load a dictionary into the file in Figure 5. In Figure 6, you can see that the data is dumped into a file. 

![Figure 5. Pickling a dictionary](https://github.com/roslynm/IntroToProg-Python-Mod07/blob/master/Photos/Figure5.png "Figure 5. Pickling a dictionary")

Figure 5. Pickling a dictionary

![Figure 6. Data pickled into file](https://github.com/roslynm/IntroToProg-Python-Mod07/blob/master/Photos/Figure6.png "Figure 6. Data pickled into file")

Figure 6. Data pickled into file

The dump() function requires two arguments, the data to pickle, and the file. Note, when pickling, you load the entire object from the file. You can pickle a variety of objects, including lists, strings, numbers, touples. Since I am loading the data into the file in a dictionary, it is hard to access certain components of the dictionary from the file. Instead I have to load the object as a whole back into my script. Why does this matter? One of the main reasons pickling can be useful is being able to work with huge amounts of data. If I had a huge dictionary, then I would have to load the entire dictionary back into my memory, instead of being able to access key parts. In the script below, you can see examples of me dumping the weather data into a file as individual variables, instead of as a dictionary. In this way, I can also load the data piece by piece from the file. See functions in Figure 7. 

![Figure 7. Pickling data variable by variable](https://github.com/roslynm/IntroToProg-Python-Mod07/blob/master/Photos/Figure6.png "Figure 7. Pickling data variable by variable")

Figure 7. Pickling data variable by variable

It is very important to note that when pickling multiple objects, the order counts! That is, the first object that you pickle, will be the first object that is loaded back up. 

Taking pickling one step further, we can add the shelf module.  The shelve module allows you to store and randomly access pickled objects in a file. Using the shelve module, it acts like a dictionary that lets you access its components. In the example below, I show you the same program but instead of storing the weather data into a dictionary and pickling the dictionary, I shelve them as separate variables. In Figure 8, you can see that in the function where I am shelving all the variables, I am shelving them similar to how I created my original dictionary, dictWeather. In the function in which I am loading data from the file, you can see that I am randomly accessing just the relative humidity. 

![Figure 8. Example of shelving data](https://github.com/roslynm/IntroToProg-Python-Mod07/blob/master/Photos/Figure8.png "Figure 8. Example of shelving data")

Figure 8. Example of shelving data

I used [THIS](https://stackoverflow.com/questions/4103430/what-is-the-difference-between-pickle-and-shelve) stack overflow page to better understand the difference between pickling and shelving. I think this website gave good examples of how the modules are used differently. I tried to show this difference in my assignment 7 example.

## Error Handling

Up until this point, if there was an error in our program, the script would stop running and provide an error message. In python, you have capability to handle these errors in a more graceful way. What I mean by that is providing an error message that is easier to understand for the user. In Figure 9, you can see that I have added error handling to the temperature input functions. I have this set up such that it will keep prompting user to input a temperature if they try and enter a string instead of a number.

![Figure 9. Error Handling](https://github.com/roslynm/IntroToProg-Python-Mod07/blob/master/Photos/Figure9.png "Figure 9. Error Handling")

Figure 9. Error Handling 

Note that in the example above, I printed the value “e”. Whenever an exception occurs, it is associated with a value (argument). You can capture this argument and print it to the user if you by using the word “as” after the exception.  In Figure 10, you can see I used the general exception to catch the error. You can create multiple except statements to try and catch different types of errors. 

![Figure 10. General exception example](https://github.com/roslynm/IntroToProg-Python-Mod07/blob/master/Photos/Figure10.png "Figure 10. General exception example")

Figure 10. General exception example

I used [THIS](https://www.tutorialspoint.com/python/python_exceptions.htm) website as a guide in error handling. What I liked about this website was that it had a list of common error types to easily reference. It also provided many examples of error handling. 

In Figure 11, below, you can see the script running from the terminal and the binary file that was created. 

![Figure 11. Script running from terminal, and data that is saved to file.](https://github.com/roslynm/IntroToProg-Python-Mod07/blob/master/Photos/Figure11.png "Figure 11. Script running from terminal, and data that is saved to file. ")

Figure 11. Script running from terminal, and data that is saved to file. 

## Summary

In summary, there are many benefits to pickling and shelving data. When pickling, you can serialize objects in a single byte stream. The order in which you dump and load objects matters. Shelving builds onto this in that a serialized dictionary of pickled objects is created. Shelving allows you to associate each object with a key therefore allowing you to randomly access your data. We also added error handling to our scripts for the first time. This allows us to catch errors and provide a more helpful message about the error, rather than the canned python error response.















