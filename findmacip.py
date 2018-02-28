import re

macre = r'([0-9A-F]{2}[:-]){5}([0-9A-F]{2})'
ipre = r'((2[0-5]|1[0-9]|[0-9])?[0-9]\.){3}((2[0-5]|1[0-9]|[0-9])?[0-9])'


def mac_find(line):

    found = re.search(macre, line, re.I)

    return found


def ip_find(line):

    return re.search(ipre, line, re.I).group()


# load a file in and return a list of the lines
def load_file(filename):

    fileLines = []

    try:
        with open(filename) as readfile:
            for line in readfile:
                fileLines.append(line.strip())

    except IOError as msg:
        print("Error opening file " + filename)
        print(msg)

    return fileLines


def main():
    strings = load_file("filename.txt")
    output = []

    for s in strings:
        output.append(mac_find(s))

    for line in output:
        print(line)


if __name__ == '__main__':
    main()
