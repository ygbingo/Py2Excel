output = open('res_via', 'r+')
input = open('loc_res')

lines = input.readlines()

for ii in range(0, len(lines)):
    tail = lines[ii].find('类')
    value = lines[ii][:tail]
    output.write(value + '类' + '\n')
    output.write(value + '频道' + '\n')
    output.write(value + '调频' + '\n')
    output.write(value + '广播' + '\n')
    output.write(value + '电台' + '\n')