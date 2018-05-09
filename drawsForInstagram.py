import re
import sys

def search(data):
    res = re.sub(r'(\s*@\S*)+','', data)

    # string to list
    res = list(res.split("\n"))

    # order the list
    res = sorted(res, key=str.lower)

    print(res)
    return res

if __name__ == '__main__':

    # parameters
    input = sys.argv[1]
    output = sys.argv[2]

    # read the data
    file = open(input, 'r')
    text = file.read()
    file.close()

    # process the data and returns a list
    res = search(text)

    # write in the output
    file = open(output, 'w')
    file.write('\n'.join(res))
    file.close()
