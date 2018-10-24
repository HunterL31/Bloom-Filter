import sys

dictionary = ''
input = ''
output3 = ''
output5 = ''

# Basic error checking on argument number and parsing of CL args
if len(sys.argv) != 8:
    print("Incorrect argument count")
else:
    for i in range(len(sys.argv)):
        if sys.argv[i] == '-d':
            dictionary = sys.argv[i + 1]
        elif sys.argv[i] == '-i':
            input = sys.argv[i + 1]
        elif sys.argv[i] == '-o':
            output3 = sys.argv[i + 1]
            output5 = sys.argv[i + 2]
    #print(dictionary, input, output3, output5)