dict_file = 'res_via'

f2 = open('res_location2','r+')

with open(dict_file) as df:
    dics = df.readlines()

    for ii in range(0, len(dics)):
        if '\n' in dics[ii]:
            f2.write('|' + dics[ii])
        else:
            f2.write('|' + dics[ii] + '\n')


    # result = set(all_dict)

df.close()
f2.close()