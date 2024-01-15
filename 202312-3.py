# 树上搜索
n,m = map(int,input().split(" "))
number_reverse = list(range(n, 0, -1))

number2_reverse = list(range(n, 1, -1))

rate = list(map(int,input().split(" ")))

dict_number_rate = dict(zip(number_reverse,reversed(rate))) # 从大到小排列

number_upper = list(map(int,input().split(" ")))
dict_number_upper = dict(zip(number2_reverse,reversed(number_upper))) # 从大到小排列

number_test = []
for i in range(m):
    number_test.append(int(input()))

def number_race(dict_number_upper):
    dict_number_race = {}
    for i in number_reverse:
        dict_number_race[i] = [i]
    for value in dict_number_race.values():
        for key2 in dict_number_upper:
            if value[-1] == key2 and value[-1] != 1:
                value.append(dict_number_upper[key2])
            elif value == key2:
                value.append(dict_number_upper[key2])
    return dict_number_race

def w_delta_calc(dict_number_rate,dict_number_upper,number_reverse):
    temp_dict_number_rate = dict_number_rate.copy()
    temp_dict_number_upper = dict_number_upper.copy()
    w_delta = []
    sum = 0
    for key in temp_dict_number_rate:
        sum += temp_dict_number_rate[key]
    for key in temp_dict_number_rate:
        if key == 1:
            w_delta.append(abs(sum))
        elif not any(key == value for value in temp_dict_number_upper.values()):
            w_delta.append(abs(sum - temp_dict_number_rate[key] - temp_dict_number_rate[key]))
        else:
            for key2 in temp_dict_number_upper:
                if key == temp_dict_number_upper[key2]:
                    temp_dict_number_rate[key] += temp_dict_number_rate[key2]
            w_delta.append(abs(sum - temp_dict_number_rate[key] - temp_dict_number_rate[key]))
    return dict(zip(number_reverse,w_delta))

def min_dict_w_delta_key(dict_w_delta):
    min_w_delta = min(dict_w_delta.values())
    for key in dict_w_delta:
        if dict_w_delta[key] == min_w_delta:
            min_key = key
    return min_key

dict_number_race = number_race(dict_number_upper)    

for i in number_test:
    temp_dict_number_rate2 = dict_number_rate.copy()
    temp_dict_number_upper2 = dict_number_upper.copy()
    temp_dict_number_race2 = dict_number_race.copy()
    temp_number_reverse = number_reverse.copy()
    list_number = []
    while len(temp_dict_number_rate2) > 1:
        dict_w_delta = w_delta_calc(temp_dict_number_rate2,temp_dict_number_upper2,temp_number_reverse)
        min_key = min_dict_w_delta_key(dict_w_delta)
        if min_key not in dict_number_race[i]:# 旁支，删除该类别及其后代类别
            list_number.append(min_key) #只记录min_key类别，其后代类别只删除，不记录
            for key in list(temp_dict_number_race2):
                if min_key in temp_dict_number_race2[key]:
                    del temp_dict_number_rate2[key]
                    del temp_dict_number_race2[key]
                    temp_number_reverse.remove(key)
                    if key >= 2:
                        del temp_dict_number_upper2[key]
        elif min_key in dict_number_race[i]: # min_key处于同支，进一步讨论
            list_number.append(min_key)
            if min_key == i:# 找到目标类别，仅保留该类别及其后代类别
                for key in list(temp_dict_number_race2):
                    if min_key not in temp_dict_number_race2[key]:
                        del temp_dict_number_rate2[key]
                        del temp_dict_number_race2[key]
                        temp_number_reverse.remove(key)
                        if key >= 2:
                            del temp_dict_number_upper2[key]
            elif min_key != i:
                if len(dict_number_race[min_key]) > len(dict_number_race[i]):
                # min_key目标类别的后代类别，删除该类别及其后代类别
                    for key,value in dict_number_race.items():
                        if min_key in value:
                            del temp_dict_number_rate2[key]
                            if key >= 2:
                                del temp_dict_number_upper2[key]
                            del temp_dict_number_race2[key]
                            temp_number_reverse.remove(key)
    for i in list_number:
        print(i,end=" ")
    print()
