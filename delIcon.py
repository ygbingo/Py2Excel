from openpyxl import load_workbook

input = open('slotsWithIcon','r+')
output = open('slotsWithoutIcon', 'r+')

lines = input.readlines()

for line in lines:
    if '|' in line:
        allLine = line.split('|')
        for line in allLine:
            line.replace(' ', '')
            line.replace('\n', '')
            line.replace('    ','')
            if '[' in line:
                index = line.find('[')
                tail = line[index + 1]
                line = line[:index]
                if '\n' in line:
                    output.write(line + tail)
                else:
                    output.write(line + tail + '\n')
            if '\n' in line:
                output.write(line)
            else:
                output.write(line + '\n')
    else:
        line.replace(' ', '')
        line.replace('\n', '')
        line.replace('    ', '')
        if '[' in line:
            index = line.find('[')
            tail = line[index + 1]
            line = line[:index]
            if '\n' in line:
                output.write(line + tail)
            else:
                output.write(line + tail + '\n')
        if '\n' in line:
            output.write(line)
        else:
            output.write(line + '\n')

input.close()