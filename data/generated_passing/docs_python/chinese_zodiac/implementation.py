 
# coding: utf-8
 
from __future__ import print_function
from datetime import datetime
 
pinyin = {
  '': 'ji',
  '': 'y',
  '': 'bng',
  '': 'dng',
  '': 'w',
  '': 'j',
  '': 'gng',
  '': 'xn',
  '': 'rn',
  '': 'gi',
 
  '': 'z',
  '': 'chu',
  '': 'yn',
  '': 'mo',
  '': 'chn',
  '': 's',
  '': 'w',
  '': 'wi',
  '': 'shn',
  '': 'yu',
  '': 'x',
  '': 'hi'
}
 
animals = ['Rat', 'Ox', 'Tiger', 'Rabbit', 'Dragon', 'Snake',
           'Horse', 'Goat', 'Monkey', 'Rooster', 'Dog', 'Pig']
elements = ['Wood', 'Fire', 'Earth', 'Metal', 'Water']
 
celestial = ['', '', '', '', '', '', '', '', '', '']
terrestrial = ['', '', '', '', '', '', '', '', '', '', '', '']
aspects = ['yang', 'yin']
 
 
def calculate(year):
    BASE = 4
    year = int(year)
    cycle_year = year - BASE
    stem_number = cycle_year % 10
    stem_han = celestial[stem_number]
    stem_pinyin = pinyin[stem_han]
    element_number = stem_number // 2
    element = elements[element_number]
    branch_number = cycle_year % 12
    branch_han = terrestrial[branch_number]
    branch_pinyin = pinyin[branch_han]
    animal = animals[branch_number]
    aspect_number = cycle_year % 2
    aspect = aspects[aspect_number]
    index = cycle_year % 60 + 1
    print("{}: {}{} ({}-{}, {} {}; {} - year {} of the cycle)"
          .format(year, stem_han, branch_han,
                  stem_pinyin, branch_pinyin, element, animal, aspect, index))
 
 
current_year = datetime.now().year
years = [1935, 1938, 1968, 1972, 1976, current_year]
for year in years:
    calculate(year)