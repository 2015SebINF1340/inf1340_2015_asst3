#!/usr/bin/env python3

""" Module to test papers.py  """

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"

__copyright__ = "2014 Susan Sim"
__license__ = "MIT License"

__status__ = "Prototype"

# imports one per line
"""import pytest"""
import os
from exercise2 import decide

DIR = "test_jsons/"
os.chdir(DIR)


def test_returning():
    """
    Travellers are returning to KAN.
    """
    assert decide("test_returning_citizen.json", "countries.json") ==\
        ["Accept", "Accept", "Quarantine"]



test_returning()

[
  {
    "passport": "JMZ0S-89IA9-OTCLY-MQILJ-P7CTY",
    "first_name": "ELIZABETH",
    "last_name": "WENDT",
    "birth_date": "1958-08-22",
    "home": {
      "city": "Bala",
      "region": "ON",
      "country": "KAN"
    },
    "entry_reason": "returning",
    "from": {
      "city": "Weasel",
      "region": "Rodent",
      "country": "BRD"
    }
  },
  {
    "passport": "I7LWE-N5O9P-HDNAG-1JGF1-WR44S",
    "first_name": "VENITA",
    "last_name": "CULP",
    "birth_date": "1936-03-25",
    "home": {
      "city": "Eureka",
      "region": "NU",
      "country": "KAN"
    },
    "entry_reason": "returning",
    "from": {
      "city": "Desmond",
      "region": "Ohio",
      "country": "JIK"
    }
  },
  {
    "passport": "I7LWE-N5O9P-HDNAG-1JGF1-WR44S",
    "first_name": "VENITA",
    "last_name": "CULP",
    "birth_date": "1936-03-25",
    "home": {
      "city": "Eureka",
      "region": "NU",
      "country": "KAN"
    },
    "entry_reason": "returning",
    "from": {
      "city": "a",
      "region": "a",
      "country": "LUG"
    }
  }
]
{
  "ALB": {
    "code": "ALB",
    "name": "Duchy of Alberdore",
    "visitor_visa_required": "0",
    "transit_visa_required": "0",
    "medical_advisory": ""
  },
  "BRD": {
    "code": "BRD",
    "name": "Eminent Plutarchy of Vemenin",
    "visitor_visa_required": "1",
    "transit_visa_required": "1",
    "medical_advisory": ""
  },
  "CFR": {
    "code": "CFR",
    "name": "Republic of Carefree",
    "visitor_visa_required": "1",
    "transit_visa_required": "0",
    "medical_advisory": ""
  },
  "DSK": {
    "code": "DSK",
    "name": "People's Utopia of Headdeskia",
    "visitor_visa_required": "0",
    "transit_visa_required": "0",
    "medical_advisory": ""
  },
  "ELE": {
    "code": "ELE",
    "name": "Kingdom of Elebrondus",
    "visitor_visa_required": "0",
    "transit_visa_required": "0",
    "medical_advisory": "RICKETS"
  },
  "FRY": {
    "code": "FRY",
    "name": "Principality of Frye",
    "visitor_visa_required": "1",
    "transit_visa_required": "1",
    "medical_advisory": ""
  },
  "GOR": {
    "code": "GOR",
    "name": "Theocracy of Gordunk",
    "visitor_visa_required": "0",
    "transit_visa_required": "1",
    "medical_advisory": ""
  },
  "HJR": {
    "code": "HJR",
    "name": "Hjrabnicka",
    "visitor_visa_required": "0",
    "transit_visa_required": "0",
    "medical_advisory": ""
  },
  "III": {
    "code": "III",
    "name": "Isle of Ii",
    "visitor_visa_required": "1",
    "transit_visa_required": "1",
    "medical_advisory": ""
  },
  "JIK": {
    "code": "JIK",
    "name": "Jikland",
    "visitor_visa_required": "0",
    "transit_visa_required": "0",
    "medical_advisory": ""
  },
  "KRA": {
    "code": "KRA",
    "name": "Kraznoviklandstan",
    "visitor_visa_required": "0",
    "transit_visa_required": "0",
    "medical_advisory": ""
  },
  "LUG": {
    "code": "LUG",
    "name": "Democratic Republic of Lungary",
    "visitor_visa_required": "1",
    "transit_visa_required": "1",
    "medical_advisory": "MUMPS"
  }
}