loc_file = 'loc_res'
loc_res = 'res_location2'
# loc_file = 'loc_res'
# loc_res = 'res_location2'

poi_file = 'res_poitype'
f1 = open(loc_res, 'r+')
# f2 = open(poi_file,'r+')
res_lis = []

with open(loc_file) as loc, open(poi_file) as poi:
    locations = loc.readlines()
    poitypes = poi.readlines()
    for location in locations:
        if location not in poitypes:
            res_lis.append(location)
    res_dic = list(set(res_lis))
    for ii in range(0, len(res_dic)):
        f1.write(res_dic[ii])
    # result = set(all_dict)

loc.close()
poi.close()
f1.close()