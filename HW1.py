sentense = "Не знаю, как там в Лондоне, я не была. \
Может, там собака - друг человека. А у нас управдом - друг человека!"
# Task 1 - count the number of characters
count_characters = len(sentense)
print (count_characters)
# Task 2 - expand string
expand_string = sentense[::-1]
print (expand_string)
# Task 3 - every word is capitalized
capitalized_word = (str.title(sentense))
print (capitalized_word)
# Task 4 - all text in capital letters
capital_letter = (str.lower(sentense))
print (capital_letter)
# Task 5 - number of occurrences characters "нд", "ам", "о" in a string
first_ch = (sentense.count("нд"))
print (first_ch)
second_ch = (sentense.count("ам"))
print (second_ch)
third_ch = (sentense.count("о"))
print (third_ch)
# Task 6 - own exercises
# sentense x2
double_sentense = sentense * 2
print (double_sentense)
# extract characters
extract_characters = sentense[2:7]
print (extract_characters)
# split sentense
split_sentense = (sentense.split(', '))
print (split_sentense)
# all the words in capital letters
capital_letters = (sentense.upper())
print (capital_letters)
# find an id of sntense
find_an_id = (id(sentense))
print (find_an_id)
# Task 7 - expand sentense
reversed = sentense[::-1] 
str = reversed.split('. ')
print (reversed) 
# Task 8 - output the original string 
original_string = sentense
print (original_string)

