import csv
import sys


def cleanup(filepath):
    with open(filepath, 'r') as input_buffer:
        reader = csv.reader(input_buffer)
        for row in reader:
            if "".join(row).strip() != "":
                values = []
                for index in sys.argv[2:]:
                    try:
                        values.append(row[int(index)].strip())
                    except ValueError:
                        print "Bad Argument: {}".format(index)
                        sys.exit(1)
                print ",".join(values)

if __name__ == '__main__':
    if sys.argv and len(sys.argv) > 2:
        try:
            cleanup(sys.argv[1])
        except IOError:
            print "Could not read file: {}".format(sys.argv[0])
    else:
        print "You should enter a csv file to parse and the columns indexes!"
