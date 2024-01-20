from collections import defaultdict 
import re
def count_words(line):
    words = re.findall(r'\w+', line.lower())
    return words
inputfile = "input.txt"
outputfile = "output.txt"
wordcount = defaultdict(int)
with open(inputfile, 'r') as input_file, open(outputfile, 'w') as output_file:
        output_file.write('Word_Count:\n') 
        for line in input_file:
            line = line.strip()
            words = count_words(line)
            output_file.write(line + '\n')
            (variable) word: Any
             
        for word, count in wordcount. items ():
            output_file.write(f'{word}: {count}\n')
            