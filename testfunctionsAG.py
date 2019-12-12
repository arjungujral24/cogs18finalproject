"""Below are the test cases for the functions that I created in the
myfunctions file. I only will test clean_word, generate_state, and
generate_capital, my three custom made functions """

import pytest
from myfunctions import *

def test_clean_word():
    """Testing the clean_word function"""
    assert callable(clean_word)
    assert isinstance(clean_word("HELLO"), str)
    assert clean_word("Hello") == "hello"

def test_generate_state():
    """Testing the generate_state function"""
    assert callable(generate_state)
    assert isinstance(generate_state(), str)

def test_generate_capital():
    """Testing the generate_state function"""
    state_capitals = {
        'Alabama': 'Montgomery',
        'Alaska': 'Juneau',
        'Arizona':'Phoenix',
        'Arkansas':'Little Rock',
        'California': 'Sacramento',
        'Colorado':'Denver',
        'Connecticut':'Hartford',
        'Delaware':'Dover',
        'Florida': 'Tallahassee',
        'Georgia': 'Atlanta',
        'Hawaii': 'Honolulu',
        'Idaho': 'Boise',
        'Illinois': 'Springfield',
        'Indiana': 'Indianapolis',
        'Iowa': 'Des Moines',
        'Kansas': 'Topeka',
        'Kentucky': 'Frankfort',
        'Louisiana': 'Baton Rouge',
        'Maine': 'Augusta',
        'Maryland': 'Annapolis',
        'Massachusetts': 'Boston',
        'Michigan': 'Lansing',
        'Minnesota': 'St. Paul',
        'Mississippi': 'Jackson',
        'Missouri': 'Jefferson City',
        'Montana': 'Helena',
        'Nebraska': 'Lincoln',
        'Nevada': 'Carson City',
        'New Hampshire': 'Concord',
        'New Jersey': 'Trenton',
        'New Mexico': 'Santa Fe',
        'New York': 'Albany',
        'North Carolina': 'Raleigh',
        'North Dakota': 'Bismarck',
        'Ohio': 'Columbus',
        'Oklahoma': 'Oklahoma City',
        'Oregon': 'Salem',
        'Pennsylvania': 'Harrisburg',
        'Rhode Island': 'Providence',
        'South Carolina': 'Columbia',
        'South Dakota': 'Pierre',
        'Tennessee': 'Nashville',
        'Texas': 'Austin',
        'Utah': 'Salt Lake City',
        'Vermont': 'Montpelier',
        'Virginia': 'Richmond',
        'Washington': 'Olympia',
        'West Virginia': 'Charleston',
        'Wisconsin': 'Madison',
        'Wyoming': 'Cheyenne' }
    states = list(state_capitals.keys())
    assert callable(generate_capital)
    assert isinstance(generate_capital("California"), str)
    assert (generate_capital("California") == "sacramento")
