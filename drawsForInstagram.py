import re
import sys

def search(data):


    return res

if __name__ == '__main__':

    # parameters
    input = sys.argv[1]
    output = sys.argv[2]

    # read the data
    file = open(input, 'r')
    text = file.read()
    file.close()

    # process the data
    res = search(text)

    # write in the output
    file = open(output, 'w')
    file.write(text)
    file.close()
