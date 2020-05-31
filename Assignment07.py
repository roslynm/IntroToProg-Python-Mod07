# ------------------------------------------------- #
# Title: Assignment07 - Pickling Example
# Description: Example of using Pickling
# ChangeLog: (Who, When, What)
# Roslyn Melookaran, 5/27/20, Created Script
# Roslyn Melookaran, 5/29/20, Added shelving
# Roslyn Melookaran, 5/30/20, Added error handling
# ------------------------------------------------- #
# First step is to import modules
import pickle # Allows you to pickle and store more complex data in a file
import shelve # Allows you to store and randomly access pickled objects in a file
import sys
# Data -------------------------------------------- #
fltDewPtTempF=None # Dew point temperature in Fahrenheit
fltAirTempF=None # Air temperature in Fahrenheit
fltDewPtTempC=None # Dew point temperature in Celsius
fltAirTempC=None # Air temperature in Celsius
fltSatVapPres= None # Saturated vapor pressure in millibars
fltActVapPres= None # Actual vapor pressure in millibars
fltRelHumidity= None # Relative humidity (percent)
FileName="WeatherInfo.dat"
FileName2= "WeatherInfo2.dat" # This file is used when demonstrating shelving
dictWeather={} # Weather sats
# Processing -------------------------------------- #
class Processor:
    """  Performs Processing tasks """

    @staticmethod
    def temp_conversion(temp_in_F):
        """ Converts temperature in Fahrenheit to temperature in Celsius
            :param temp_in_F: (float) temp in F:
            :return temp_in_C: (float) temp in C:
            """
        temp_in_C=(5/9)*(temp_in_F-32)
        temp_in_C=round(temp_in_C,2)
        return temp_in_C

    @staticmethod
    def saturated_vapor_pressure(temp_C):
        """ Calculates the saturated vapor pressure
            :param temp_in_F: (float) temp in F:
            :return sat_vpr_pressure: (float) saturated vapor pressure:
            """
        sat_vpr_pressure=(10**((7.5*temp_C)/(237.3+temp_C)))*6.11
        sat_vpr_pressure=round(sat_vpr_pressure,2)
        return sat_vpr_pressure

    @staticmethod
    def actual_vapor_pressure(dew_temp_C):
        """ Calculates the actual vapor pressure
            :param temp_in_F: (float) dew point temp in F:
            :return act_vpr_pressure: (float) saturated vapor pressure:
            """
        act_vpr_pressure=(10**((7.5*dew_temp_C)/(237.3+dew_temp_C)))*6.11
        act_vpr_pressure=round(act_vpr_pressure,2)
        return act_vpr_pressure

    @staticmethod
    def rel_humidity(sat_vap_press, act_vap_press):
        """ Calculates the actual vapor pressure
            :param sat_vap_press: (float) saturated vapor pressure:
            :param act_vap_press: (float) actual vapor pressure:
            :return relative humidity: (float) relative humidity:
            """
        rel_hum=(act_vap_press/sat_vap_press)*100
        rel_hum=round(rel_hum,2)
        return rel_hum

# Presentation ------------------------------------ #
class IO:
    @staticmethod
    def temp_input():
        """ Gets user to input the temperature
            :return temp_in_F: (float) temp in F:
            """
        while True:
            try:
                temp_in_F=float(input("Please enter the temperature in Fahrenheit: "))
                break
            except ValueError as e:
                print("That was not a number! Please enter the Temperature value: ")
                print(e)
        return temp_in_F

    @staticmethod
    def temp_dew_input():
        """ Gets user to input the temperature
            :return dewpt_temp_in_F: (float) temp in F:
            """
        while True:
            try:
                dew_pt_temp_in_F=float(input("Please enter the dew point temperature in Fahrenheit: "))
                break
            except ValueError as e:
                print("That was not a number! Please enter the Temperature value: ")
                print(e)
        return dew_pt_temp_in_F

    @staticmethod
    def print_data_to_user(dict_weather):
        """ prints all data to user
            :param: dict_weather (string): Name of file to save
            :return: nothing:
            """
        for key in dict_weather:
            print(key, "-->", dict_weather[key])

    @staticmethod
    def save_data_to_file(file_name, dict_weather):
        """ saves data to file
            :param: file_name (string): Name of file to save
            :param: dict_weather (dictionary): Dictionary of weather data
            :return: nothing:
            """
        obj_file = open(file_name, "wb") # The "wb" = write to binary. If file exists, contents is overwritten. If not, it is created.
        pickle.dump(dict_weather, obj_file) # Dump function requires 2 arguments--> Data to dump, and file
        obj_file.close() # Always remember to close file!!

    @staticmethod
    def read_data_from_file(file_name):
        """ saves data to file
            :param: file_name (string): Name of file to save
            :return: dict_weather (dictionary): Dictionary of weather data:
            """
        obj_read_file=open(file_name, "rb") # The "rb" = read binary, if the file doesn't exist, you will get an error
        dict_weather=pickle.load(obj_read_file) # Loads entire diction
        obj_read_file.close()
        return dict_weather

    @staticmethod
    def save_ind_data_to_file(file_name,dew_temp_C, temp_C, sat_vpr_pressure, act_vpr_pressure, rel_hum):
        """ saves data to file
            :param: file_name (string): Name of file to save
            :param: dew_temp_C (float): Dew temp in Celsius
            :param: temp_C (float): Temp in Celsius
            :param: sat_vpr_pressure (float): Saturated vapor pressure in millibars
            :param: act_vpr_pressure (float): Actual vapor pressure in millibars
            :param: rel_hum (float): Percent relative humidity
            :return: nothing
            """
        obj_file = open(file_name, "wb")  # The "wb" = write to binary. If file exists, contents is overwritten. If not, it is created.
        pickle.dump(dew_temp_C, obj_file) # Dumps data variables individually
        pickle.dump(temp_C, obj_file) # Dumps data variables individually
        pickle.dump(sat_vpr_pressure, obj_file) # Dumps data variables individually
        pickle.dump(act_vpr_pressure, obj_file) # Dumps data variables individually
        pickle.dump(rel_hum, obj_file) # Dumps data variables individually
        obj_file.close()

    @staticmethod
    def read_ind_data_from_file(file_name):
        """ saves data to file
            :param: file_name (string): Name of file to save
            :return: nothing:
            """
        obj_read_file = open(file_name, "rb") # The "rb" = read binary, if the file doesn't exist, you will get an error
        dew_temp_C= pickle.load(obj_read_file) # This will load THE FIRST object pickled
        obj_read_file.close()
        print("The dew temperature in Celsius is: " + str(dew_temp_C)) # Prints the object the we just loaded

    @staticmethod
    def save_data_to_file_shelve(file_name,dew_temp_C, temp_C, sat_vpr_pressure, act_vpr_pressure, rel_hum):
        """ saves data to file using shelve method
                :param: file_name (string): Name of file to save
                :param: dew_temp_C (float): Dew temp in Celsius
                :param: temp_C (float): Temp in Celsius
                :param: sat_vpr_pressure (float): Saturated vapor pressure in millibars
                :param: act_vpr_pressure (float): Actual vapor pressure in millibars
                :param: rel_hum (float): Percent relative humidity
                :return: nothing
                """
        obj_file=shelve.open(file_name, "c")
        obj_file["Dew Pt Temp (C)"]=dew_temp_C
        obj_file["Temp (C)"]=temp_C
        obj_file["Saturated Vap Pressure (millibars)"]=sat_vpr_pressure
        obj_file["Actual Vap Pressure (millibars)"]=act_vpr_pressure
        obj_file["Relative Humidity (%)"]=rel_hum
        obj_file.sync() # This makes sure data is written to file
        obj_file.close()

    @staticmethod
    def read_data_from_file_shelve(file_name):
        """ saves data to file
            :param: file_name (string): Name of file to save
            :return: nothing:
            """
        try:
            obj_file = shelve.open(file_name,"r")
            print("The relative humidity is: " + str(obj_file["Relative Humidity (%)"]) + "%")  # Note that this is randomly accessing this variable
            obj_file.close()
        except Exception as e:
            print("Unable to open")
            print(e)
            sys.exit()
        else:
            return obj_file


# Main Body of Script  ----------------------------------------------------- #

# Functions to gather the temperature and dew point temperature from user (in Fahrenheit).
fltAirTempF=IO.temp_input()
fltDewPtTempF=IO.temp_dew_input()

# Functions to convert Fahrenheit to Celsius
fltAirTempC=Processor.temp_conversion(fltAirTempF)
fltDewPtTempC=Processor.temp_conversion(fltDewPtTempF)

# Function to calculate saturated vapor pressure (in millibars)
fltSatVapPres=Processor.saturated_vapor_pressure(fltAirTempC)
# Function to calculate actual vapor pressure (in millibars)
fltActVapPres=Processor.actual_vapor_pressure(fltDewPtTempC)
# Function to calculate the relative humidity
fltRelHumidity=Processor.rel_humidity(fltSatVapPres,fltActVapPres)

#Define dictionary with values
dictWeather={"Temp (C)": fltAirTempC,
             "Dew Pt Temp (C)":fltDewPtTempC,
             "Saturated Vap Pressure (millibars)":fltSatVapPres,
             "Actual Vap Pressure (millibars)":fltActVapPres,
             "Relative Humidity (%)":fltRelHumidity}

#Function to print output to user
IO.print_data_to_user(dictWeather)

#-----This block contains pickling dictionary examples, comment in/out as needed----#
# # Function to save DICTIONARY to file
# #IO.save_data_to_file(FileName,dictWeather)
# # Function to read DICTIONARY from file
# #IO.read_data_from_file(FileName)
#-----This block contains pickling variable examples, comment in/out as needed----#
# # Function to save INDIVIDUAL VARIABLES to file
# IO.save_ind_data_to_file(FileName,fltDewPtTempC, fltAirTempC, fltSatVapPres, fltActVapPres, fltRelHumidity)
# # Function to read INDIVIDUAL VARIABLES from file
# IO.read_ind_data_from_file(FileName)
#-----This block contains shelving variable examples, comment in/out as needed----#
# Function that saves data to file using the SHELVE module
IO.save_data_to_file_shelve(FileName2, fltDewPtTempC, fltAirTempC, fltSatVapPres, fltActVapPres, fltRelHumidity)
# Function that saves data to file using the SHELVE module
IO.read_data_from_file_shelve(FileName2)




