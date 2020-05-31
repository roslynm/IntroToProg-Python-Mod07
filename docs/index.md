# Module 7 Assignment
- Code file:[Assignment 7 Code](https://github.com/roslynm/IntroToProg-Python-Mod07/blob/master/Assignment07.py)
- Documentation of work:[Assignment 7 Document](https://github.com/roslynm/IntroToProg-Python-Mod07/blob/master/Assignment07.pdf)
  
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

![Figure 1. Main body of script](https://github.com/roslynm/IntroToProg-Python-Mod07/blob/master/Photos/Figure1.png "Figure 1")
Figure 1. Main body of script
![Figure 2. Functions that gather input from users and prints data back out](https://github.com/roslynm/IntroToProg-Python-Mod07/blob/master/Photos/Figure2.png "Figure 2. Functions that gather input from users and prints data back out")





