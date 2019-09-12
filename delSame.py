dict_file = 'res_location2'

f2 = open('res_via','r+')

with open(dict_file) as df:
    dics = df.readlines()
    print('dics len: ' + str(len(dics)))
    dic = list(set(dics))
    print('dic len: ' + str(len(dic)))
    for ii in range(0, len(dic)):
        f2.write(dic[ii])

    # result = set(all_dict)

df.close()
f2.close()