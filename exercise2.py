#!/usr/bin/env python3

""" Assignment 3, Exercise 2, INF1340, Fall, 2015. Kanadia
Computer-based immigration office for Kanadia
"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"

import re
import datetime
import json

######################
## global constants ##
######################
REQUIRED_FIELDS = ["passport", "first_name", "last_name",
                   "birth_date", "home", "entry_reason", "from"]

######################
## global variables ##
######################
'''
countries:
dictionary mapping country codes (lowercase strings) to dictionaries
containing the following keys:
"code","name","visitor_visa_required",
"transit_visa_required","medical_advisory"
'''

COUNTRIES = None


#####################
# HELPER FUNCTIONS ##
#####################
def is_more_than_x_years_ago(x, date_string):
    """
    Check if date is less than x years ago.
    :param x: int representing years
    :param date_string: a date string in format "YYYY-mm-dd"
    :return: True if date is less than x years ago; False otherwise.
    """

    now = datetime.datetime.now()
    x_years_ago = now.replace(year=now.year - x)
    date = datetime.datetime.strptime(date_string, '%Y-%m-%d')

    return (date - x_years_ago).total_seconds() < 0


def decide(input_file, countries_file):
    """
    Decides whether a traveller's entry into Kanadia should be accepted
    :param input_file: The name of a JSON formatted file that contains
        cases to decide
    :param countries_file: The name of a JSON formatted file that contains
        country data, such as whether an entry or transit visa is required,
        and whether there is currently a medical advisory
    :return: List of strings. Possible values of strings are:
        "Accept", "Reject", and "Quarantine"
    """

    result = []

    """Loading JSON objects"""
    with open(input_file) as data_file:
        people = json.load(data_file)
    with open(countries_file) as data_file:
        COUNTRIES = json.load(data_file)


    """Converting JSON list names to strings for ease of use"""
    listCountries = []
    for rows in COUNTRIES:
        listCountries.append(str(rows))

    """Iterating through all values or the people json input file.
    If any of the values are missing access to kanadia is rejected"""

    for row in people:
        rejected = False
        for v in row:
            if v == None:
                result.append("Rejected")
                rejected = True
                continue

        if rejected != True:
            """If the person has all the required information we save each of the values to variables"""

            firstName = row["first_name"]
            lastName = row["last_name"]
            birthDate = row["birth_date"]
            passportNumber = row["passport"]
            homeLocation = row["home"]
            homeCity = homeLocation["city"]
            homeRegion = homeLocation["region"]
            homeCountry = homeLocation["country"]
            fromLocation = row["from"]
            fromCity = fromLocation["city"]
            fromRegion = fromLocation["region"]
            fromCountry = fromLocation["country"]
            reasonEntry = row["entry_reason"]

        """If person has a visa we grab its identifier value"""
        try:
            viaLocation = row["via"]
            visa = people["visa"]
        except:
            viaLocation = None
            visa = None


        """If all infiormation submitted is valid"""
        if validate_info(birthDate, passportNumber, homeCountry, fromCountry, listCountries):
            """Is the person returning or visiting Kanadia?
            If the person is returning we verify the medical advisory from the country he is arriving.
            If there is no medical advisory. The person is cleared to pass. Otherwise he is put into Quarantine.
            """
            if reasonEntry == "returning":
                if getAdvisory(fromCountry,COUNTRIES):
                    result.append("Accept")
                else:
                    result.append("Quarantine")
            else:
                """If the person is visiting the same rules apply. The difference being they may require a valid visa to enter
                   So we check to see if a Visa is required.
                   If that is the case we validate the persons visa.
                   The person will be rejected if their visa is invalid.
                """
                if getAdvisory(fromCountry,COUNTRIES):
                    if check_visa_requirement_transit(fromCountry,COUNTRIES):
                        if valid_visa_format(visa):
                            result.append("Accept")
                        else:
                            result.append("Reject")
                    else:
                        result.append("Accept")
                else:
                    result.append("Quarantine")


        else:
            result.append("Reject")

   
    return result

"""Call all information check methods"""
def validate_info(date, passport, homeCountry, fromCountry, listCountries):

    if valid_date_format(date):

        if valid_passport_format(passport):

            if validate_home_location(homeCountry, listCountries):

                if validate_from_location(fromCountry, listCountries):
                    return True

    return False

"""Make sure persons home country is listed"""
def validate_home_location(country, listCountries):
    if country == "KAN":
        return True
    for rows in listCountries:
        if rows == country:
            return True

    return False

"""Make sure persons country person is returning from is listed"""
def validate_from_location(country, listCountries):
    for rows in listCountries:
        if rows == country:
            return True

    return False

"""Verify VISA requirement"""
def check_visa_requirement_visitor(country,COUNTRIES):
    return COUNTRIES[country]["visitor_visa_required"] == 1

"""Verify VISA requirement"""
def check_visa_requirement_transit(country,COUNTRIES):
    return COUNTRIES[country]["transit_visa_required"] == 1

"""check if country has a medical advisory"""
def getAdvisory(country,COUNTRIES):
    return COUNTRIES[country]["medical_advisory"] == ""


"""Use Regex to determin passport_number validity"""
def valid_passport_format(passport_number):
    """
    Checks whether a pasport number is five sets of five alpha-number characters separated by dashes
    :param passport_number: alpha-numeric string
    :return: Boolean; True if the format is valid, False otherwise
    """
    filter = re.compile("[\d\w]{5}\-[\d\w]{5}\-[\d\w]{5}\-[\d\w]{5}\-[\d\w]{5}$")

    if re.match(filter, passport_number):
        return True

    return False

"""Use Regex to determin visa code validity"""
def valid_visa_format(visa_code):
    """
    Checks whether a visa code is two groups of five alphanumeric characters
    :param visa_code: alphanumeric string
    :return: Boolean; True if the format is valid, False otherwise
    """
    filter = re.compile("[\d\w]{5}\-[\d\w]{5}$")
    if re.match(filter, visa_code):
        return True

    return False

"""Use Regex to determin birthday validity"""
def valid_date_format(date_string):
    """
    Checks whether a date has the format YYYY-mm-dd in numbers
    :param date_string: date to be checked
    :return: Boolean True if the format is valid, False otherwise
    """
    filter = re.compile("^\d{4}\-(0?[1-9]|1[012])\-(0?[1-9]|[12][0-9]|3[01])$")
    if re.match(filter, date_string):
        return True

    return False
