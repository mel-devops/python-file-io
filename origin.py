#print the message "opening origin.py"
print("opening origin.py")
#open the file origin.txt in read mode
with open('origin.txt', 'r') as in_stream:
    print('Opening origin.txt')
#open the file exercise_output.txt in write mode and assign the file object to the variable out_stream
    with open('origin_excercise_output.txt', 'w') as out_stream:
#iterate over the lines, for each line:
#strip the line of whitespace.
#split the line into a list of words.
#increment the line number.
#ithe word contains the string "inherit":
#write the line number and the word to the file origin_exercise_output.
        line_num = 0
        for line in in_stream:
            line = line.strip()
            word_list = line.split()
            line_num += 1
            for word in word_list:
                if 'inherit' in word:
                    out_stream.write(str(line_num) + '{0}\n'.format(word))
print('Done!')
print('origin.txt is closed?', in_stream.closed)
print('origin.txt is closed?', out_stream.closed)