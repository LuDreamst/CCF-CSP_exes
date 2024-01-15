# 树上搜索
n,m = map(int,input().split(" "))
number = list(range(1, n+1, 1))
number_reverse = number[::-1]

number2 = list(range(2, n+1, 1))
number2_reverse = number2[::-1]

rate = list(map(int,input().split(" ")))
rate_reverse = rate[::-1]

dict_number_rate = dict(zip(number_reverse,rate_reverse))

number_upper = list(map(int,input().split(" ")))
number_upper_reverse = number_upper[::-1]
dict_number_upper = dict(zip(number2_reverse,number_upper_reverse))
# number_upper_reverse = number_upper[::-1]
number_test = []
for i in range(m):
    number_test.append(int(input()))

# print("number:",number)
# print("rate:",rate)
# print("dict_number_rate:",dict_number_rate)
# print("number_upper:",number_upper)
# print("dict_number_upper:",dict_number_upper)
# print("number_test:",number_test)

def number_race(dict_number_upper):
    dict_number_race = {}
    for i in number_reverse:
        dict_number_race[i] = [i]
    for value in dict_number_race.values():
        for key2 in dict_number_upper.keys():
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
    for key in temp_dict_number_rate.keys():
        sum += temp_dict_number_rate[key]
    # print("sum:", sum)
    for key in temp_dict_number_rate.keys():
        if key == 1:
            w_delta.append(abs(sum))
        elif not any(key == value for value in temp_dict_number_upper.values()):
            w_delta.append(abs(sum - temp_dict_number_rate[key] - temp_dict_number_rate[key]))
        else:
            for key2 in temp_dict_number_upper.keys():
                if key == temp_dict_number_upper[key2]:
                    temp_dict_number_rate[key] += temp_dict_number_rate[key2]
            w_delta.append(abs(sum - temp_dict_number_rate[key] - temp_dict_number_rate[key]))
    # print("w_delta:", w_delta)
    return dict(zip(number_reverse,w_delta))

def min_dict_w_delta_key(dict_w_delta):
    min_w_delta = min(dict_w_delta.values())
    for key in dict_w_delta.keys():
        if dict_w_delta[key] == min_w_delta:
            min_key = key
    return min_key

dict_number_race = number_race(dict_number_upper)    
# dict_w_delta = w_delta_calc(dict_number_rate,dict_number_upper)
# min_key = min_dict_w_delta_key(dict_w_delta)

# print("dict_number_race:", dict_number_race)
# print("dict_w_delta:", dict_w_delta)
# print("min_key:", min_key)

def ifisupper(dict_number_race, number1, number2):
    if len(dict_number_race[number1]) > len(dict_number_race[number2]):
        return False
    elif len(dict_number_race[number1]) < len(dict_number_race[number2]):
        return True

for i in number_test:
    # print("读入i:", i)
    temp_dict_number_rate2 = dict_number_rate.copy()
    temp_dict_number_upper2 = dict_number_upper.copy()
    temp_dict_number_race2 = dict_number_race.copy()
    temp_number_reverse = number_reverse.copy()
    # print(temp_dict_number_rate2)
    list_number = []
    # for j in range(len(temp_dict_number_race2)):
    while len(temp_dict_number_rate2) > 1:
        dict_w_delta = w_delta_calc(temp_dict_number_rate2,temp_dict_number_upper2,temp_number_reverse)
        # print("dict_w_delta:", dict_w_delta)
        min_key = min_dict_w_delta_key(dict_w_delta)
        # print("min_key:", min_key)
        if min_key not in dict_number_race[i]:# 旁支，删除该类别及其后代类别
            list_number.append(min_key) #只记录min_key类别，其后代类别只删除，不记录
            for key in list(temp_dict_number_race2.keys()):
                if min_key in temp_dict_number_race2[key]:
                    del temp_dict_number_rate2[key]
                    del temp_dict_number_race2[key]
                    temp_number_reverse.remove(key)
                    if key >= 2:
                        del temp_dict_number_upper2[key]
                    # list_number.append(key)
                    # print("del:", key)
                    # print("temp_dict_number_rate2:", temp_dict_number_rate2)
        elif min_key in dict_number_race[i]: # min_key处于同支，进一步讨论
            list_number.append(min_key)
            if min_key == i:# 找到目标类别，仅保留该类别及其后代类别
                for key in list(temp_dict_number_race2.keys()):
                    if min_key not in temp_dict_number_race2[key]:
                        del temp_dict_number_rate2[key]
                        # del temp_dict_number_upper2[key]
                        del temp_dict_number_race2[key]
                        temp_number_reverse.remove(key)
                        if key >= 2:
                            del temp_dict_number_upper2[key]
                        # print("del:", key)
            elif min_key != i:
                if ifisupper(temp_dict_number_race2, min_key, i) == False:# min_key目标类别的后代类别，删除该类别及其后代类别
                    for key,value in dict_number_race.items():
                        if min_key in value:
                            del temp_dict_number_rate2[key]
                            if key >= 2:
                                del temp_dict_number_upper2[key]
                            del temp_dict_number_race2[key]
                            temp_number_reverse.remove(key)
                            # print("del:", key)
                # elif ifisupper(temp_dict_number_race2, min_key, i) == True:# min_key目标类别的上级类别，删除上级类别，保留该类别及其后代类别
                #     for key,value in temp_dict_number_race2.items():
                #         if min_key not in value:
                #             del temp_dict_number_rate2[key]
                #             del temp_dict_number_upper2[key]
                #             del temp_dict_number_race2[key]
                #             temp_number_reverse.remove(key)
                #             print("del:", key)
    for i in list_number:
        print(i,end=" ")
    print()


# print(w_delta_calc(dict_number_rate,dict_number_upper))


                






