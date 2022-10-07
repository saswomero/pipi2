f = open("meters.txt", encoding='utf-8')
dictionaries = []
for i in range(10):
    s = f.readline()
    s1 = s.split(',')
    a = s1[3]
    a = a[:-1]
    s1[3] = a
    d = {"фио": s1[0], "пол": s1[1], "класс": s1[2], "время": s1[3]}
    dictionaries.append(d)

for i in range(10):
    if dictionaries[i].get("пол")=="ж":
        if dictionaries[i].get("класс")=="7":
            if float(dictionaries[i].get("время")) <= 9.8:
                dictionaries[i]["оценка"] = "5"
            elif (float(dictionaries[i].get("время")) > 9.8) and (float(dictionaries[i].get("время")) <= 10.6):
                dictionaries[i]["оценка"] = "4"
            elif (float(dictionaries[i].get("время")) > 10.6) and (float(dictionaries[i].get("время")) <= 11.4):
                dictionaries[i]["оценка"] = "3"
            else:
                dictionaries[i]["оценка"] = "2"
        else:
            if float(dictionaries[i].get("время")) <= 10.3:
                dictionaries[i]["оценка"] = "5"
            elif (float(dictionaries[i].get("время")) > 10.3) and (float(dictionaries[i].get("время")) <= 10.6):
                dictionaries[i]["оценка"] = "4"
            elif (float(dictionaries[i].get("время")) > 10.6) and (float(dictionaries[i].get("время")) <= 11.2):
                dictionaries[i]["оценка"] = "3"
            else:
                dictionaries[i]["оценка"] = "2"
    else:
        if dictionaries[i].get("класс")=="7":
            if float(dictionaries[i].get("время")) <= 9.4:
                dictionaries[i]["оценка"] = "5"
            elif (float(dictionaries[i].get("время")) > 9.4) and (float(dictionaries[i].get("время")) <= 10.2):
                dictionaries[i]["оценка"] = "4"
            elif (float(dictionaries[i].get("время")) > 10.2) and (float(dictionaries[i].get("время")) <= 11.0):
                dictionaries[i]["оценка"] = "3"
            else:
                dictionaries[i]["оценка"] = "2"
        else:
            if float(dictionaries[i].get("время")) <= 9.9:
                dictionaries[i]["оценка"] = "5"
            elif (float(dictionaries[i].get("время")) > 9.9) and (float(dictionaries[i].get("время")) <= 10.4):
                dictionaries[i]["оценка"] = "4"
            elif (float(dictionaries[i].get("время")) > 10.4) and (float(dictionaries[i].get("время")) <= 11.1):
                dictionaries[i]["оценка"] = "3"
            else:
                dictionaries[i]["оценка"] = "2"

girls = []
boys = []
for i in range(10):
    if dictionaries[i].get("пол")=="ж":
        girls.append(float(dictionaries[i].get("время")))
    else:
        boys.append(float(dictionaries[i].get("время")))

for i in range(10):
    if ((dictionaries[i].get("пол")=="ж") and (float(dictionaries[i].get("время"))==min(girls))) or ((dictionaries[i].get("пол")=="м") and (float(dictionaries[i].get("время"))==min(boys))):
        print(dictionaries[i].get("фио"), dictionaries[i].get("класс"),dictionaries[i].get("время") )

for i in range(10):
    print(dictionaries[i])











