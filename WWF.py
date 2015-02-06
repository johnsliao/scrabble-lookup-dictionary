#!/usr/bin/python

print "Content-type: text/html\n\n";

import cgi

form = cgi.FieldStorage()
letters = form["word"].value.upper()

print "<h1>Scrabble Score Calculator</h1>"
print "<p>"
print "<strong>Summary</strong>: Returns the highest-scoring scrabble word based on input letters"
print "<p>"
print "Your tiles: ", letters, "<p>"
print "<hr>"
print "<strong> Results... </strong> <p>"

highest_word_points = 0
dictionary, letter_length_indicies = [], []
tile_positions = 20*['0']
text_file = open("WWF.txt", "r")
lines = text_file.readlines()

def init():
        previous_word_length = 0
        
        for x in enumerate(lines):
                dictionary.append(x[1])
                
                if(len(x[1])>previous_word_length):
                        letter_length_indicies.append(x[0])
                previous_word_length = len(x[1])

def exists_in_dictionary(user_tiles, dic_word):
        dic_word = dic_word[:len(dic_word)-1]
        dic_check = [True] * len(dic_word)
        user_check = [True] * len(user_tiles)

        for u_index, u in enumerate(user_tiles):
                for d_index, d in enumerate(dic_word):
                        if(d == u and dic_check[d_index] and user_check[u_index]):
                                dic_check[d_index]=False
                                user_check[u_index]=False
        if(all(dic_check == False for dic_check in dic_check)):
                return True
        else:
                return False

def calculate_word_score(word):
        word = word[:len(word)-1]
        total = 0
        
        dict = {'A' : 1,
                'B' : 4,
                'C' : 4,
                'D' : 2,
                'E' : 1,
                'F' : 4,
                'G' : 3,
                'H' : 3,
                'I' : 1,
                'J' : 10,
                'K' : 5,
                'L' : 2,
                'M' : 4,
                'N' : 2,
                'O' : 1,
                'P' : 4,
                'Q' : 10,
                'R' : 1,
                'S' : 1,
                'T' : 1,
                'U' : 2,
                'V' : 5,
                'W' : 4,
                'X' : 8,
                'Y' : 3,
                'Z' : 10}

        for let in enumerate(word):
                total = total+dict.get(let[1])
        
        return total

init()

for x in dictionary:
        if(exists_in_dictionary(letters,x)
           and calculate_word_score(x)>highest_word_points):
                print 'Highest scoring word points changed from ', highest_word_points
                highest_word_points = calculate_word_score(x)
                print ' to ', highest_word_points
                print ' with word ', x, "(",highest_word_points," points )"
                print '<p>'

text_file.close()

