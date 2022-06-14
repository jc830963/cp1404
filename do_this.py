infile = open('cp1111.csv', 'r')
# read one line at one time
line_to_print = 2
counter = 0
for line in infile:
    counter += 1
    if counter ==line_to_print:
        print(line.strip())
    infile.close()

except