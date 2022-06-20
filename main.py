from selenium import webdriver
import time
import keyboard
from alive_progress import alive_bar

options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=400x400')

start_weight = input('input your max weight: ')
light_heavy_roll = int(input('input 1 for light roll, input 2 for medium roll, input 3 for heavy roll: '))
print(light_heavy_roll)
if light_heavy_roll == 1:
    Max_weight = float(start_weight) * .29
elif light_heavy_roll == 2:
    Max_weight = float(start_weight) * .69
elif light_heavy_roll == 3:
    Max_weight = float(start_weight)
else:
    print(
        'if you enter outside of 1-3 you will load to 100% Rolls are disabled. All other movement is slowed. resart if you want to change')
    Max_weight = float(start_weight)

print(Max_weight)

driver = webdriver.Chrome("E:\\Mason_Python\\chromedriver.exe")
driver.minimize_window()


# noinspection PyDeprecation
def helm():
    the_list = []
    dic = {}
    all_in_list = []

    driver.get("https://eldenring.wiki.fextralife.com/Helms")
    time.sleep(4)
    rows = driver.find_elements_by_xpath("//table/tbody/tr")
    print(len(rows))
    for i in range(1, len(rows) + 1):
        poise = driver.find_element_by_xpath(f'//*[@id="wiki-content-block"]/div[3]/table/tbody/tr[{i}]/td[14]').text
        weight = driver.find_element_by_xpath(f'//*[@id="wiki-content-block"]/div[3]/table/tbody/tr[{i}]/td[15]').text
        name = driver.find_element_by_xpath(f'//*[@id="wiki-content-block"]/div[3]/table/tbody/tr[{i}]/td[1]').text
        if not int(poise) == 0 or float(weight) == 0:
            score = float(weight) / float(poise)
            the_list.append(float(poise))
            the_list.append(float(weight))
            the_list.append(score)
            all_in_list.append(the_list)
            dic[name] = the_list
            # print(dic[name])
            the_list = []

    sorted_best_overall = {k: v for k, v in sorted(dic.items(), key=lambda item: item[1][2])}
    return sorted_best_overall


# noinspection PyDeprecation
def Chest_Armor():
    the_list = []
    dic = {}
    all_in_list = []

    driver.get("https://eldenring.wiki.fextralife.com/Chest+Armor")
    time.sleep(2)
    rows = driver.find_elements_by_xpath("//table/tbody/tr")
    print(len(rows))
    for i in range(1, len(rows) + 1):
        try:
            poise = driver.find_element_by_xpath(
                f'//*[@id="wiki-content-block"]/div[3]/table/tbody/tr[{i}]/td[14]').text
            # print(poise)
            weight = driver.find_element_by_xpath(
                f'//*[@id="wiki-content-block"]/div[3]/table/tbody/tr[{i}]/td[15]').text
            # print(weight)
            name = driver.find_element_by_xpath(f'//*[@id="wiki-content-block"]/div[3]/table/tbody/tr[{i}]/td[1]').text
            # print(name)
        except:
            name = 'null'
            weight = 0
            poise = 0
        try:
            float_poise = float(poise)
            float_weight = float(weight)
        except:
            float_poise = 0
            float_weight = 0

        if float(float_poise) != 0 or float(float_weight) != 0.1:
            try:
                score = float_weight / float_poise
            except:
                score = 100
            the_list.append(float_poise)
            the_list.append(float_weight)
            the_list.append(score)
            all_in_list.append(the_list)
            dic[name] = the_list
            # print(dic[name])
            the_list = []
        else:
            print('something')
    sorted_best_overall = {k: v for k, v in sorted(dic.items(), key=lambda item: item[1][2])}
    return sorted_best_overall


# noinspection PyDeprecation
def Gauntlets():
    the_list = []
    dic = {}
    all_in_list = []
    row = 1

    driver.get("https://eldenring.wiki.fextralife.com/Gauntlets")
    time.sleep(2)
    rows = driver.find_elements_by_xpath("//table/tbody/tr")
    print(len(rows))
    for i in range(1, len(rows) + 1):
        try:
            poise = driver.find_element_by_xpath(
                f'//*[@id="wiki-content-block"]/div[3]/table/tbody/tr[{i}]/td[14]').text
            # print(poise)
            weight = driver.find_element_by_xpath(
                f'//*[@id="wiki-content-block"]/div[3]/table/tbody/tr[{i}]/td[15]').text
            # print(weight)
            name = driver.find_element_by_xpath(f'//*[@id="wiki-content-block"]/div[3]/table/tbody/tr[{i}]/td[1]').text
            # print(name)
        except:
            name = 'null'
            weight = 0
            poise = 0
        try:
            float_poise = float(poise)
            float_weight = float(weight)
        except:
            float_poise = 0
            float_weight = 0

        if float(float_poise) != 0 or float(float_weight) != 0.1:
            try:
                score = float_weight / float_poise
            except:
                score = 100
            the_list.append(float_poise)
            the_list.append(float_weight)
            the_list.append(score)
            all_in_list.append(the_list)
            dic[name] = the_list
            # print(dic[name])
            the_list = []
        else:
            print('something')
    sorted_best_overall = {k: v for k, v in sorted(dic.items(), key=lambda item: item[1][2])}
    print(sorted_best_overall)
    return sorted_best_overall


# noinspection PyDeprecation
def Feet():
    the_list = []
    dic = {}
    all_in_list = []
    row = 1

    driver.get("https://eldenring.wiki.fextralife.com/Leg+Armor")
    time.sleep(2)
    rows = driver.find_elements_by_xpath("//table/tbody/tr")
    print(len(rows))
    for i in range(1, len(rows) + 1):
        try:
            poise = driver.find_element_by_xpath(
                f'//*[@id="wiki-content-block"]/div[3]/table/tbody/tr[{i}]/td[14]').text
            # print(poise)
            weight = driver.find_element_by_xpath(
                f'//*[@id="wiki-content-block"]/div[3]/table/tbody/tr[{i}]/td[15]').text
            # print(weight)
            name = driver.find_element_by_xpath(f'//*[@id="wiki-content-block"]/div[3]/table/tbody/tr[{i}]/td[1]').text
            # print(name)
        except:
            name = 'null'
            weight = 0
            poise = 0
        try:
            float_poise = float(poise)
            float_weight = float(weight)
        except:
            float_poise = 0
            float_weight = 0

        if float(float_poise) != 0 or float(float_weight) != 0.1:
            try:
                score = float_weight / float_poise
            except:
                score = 100
            the_list.append(float_poise)
            the_list.append(float_weight)
            the_list.append(score)
            all_in_list.append(the_list)
            dic[name] = the_list
            # print(dic[name])
            the_list = []
        else:
            print('something')
    sorted_best_overall = {k: v for k, v in sorted(dic.items(), key=lambda item: item[1][2])}
    return sorted_best_overall


Helm_D = helm()
Chest_D = Chest_Armor()
Gauntles_D = Gauntlets()
Feet_D = Feet()

print(Helm_D)
print(Chest_D)
print(Gauntles_D)
print(Feet_D)

print(len(Helm_D), len(Chest_D), len(Gauntles_D), len(Feet_D))
# input()
count = 0

potential_list = []
# with alive_bar(len(Helm_D) * len(Chest_D) * len(Gauntles_D) * len(Feet_D), force_tty=True) as bar:
for a in Helm_D.items():
    print('up')
    count += 1
    print(count)
    # input()
    for b in Chest_D.items():
        for c in Gauntles_D.items():
            for d in Feet_D.items():
                if a[1][1] + b[1][1] + c[1][1] + d[1][1] <= Max_weight:
                    # print(a[1][1], b[1][1], c[1][1] , d[1][1])
                    temp_list = [list(a), list(b), list(c), list(d)]
                    potential_list.append(list(temp_list))
                    # bar()

print(potential_list)
print(sorted(potential_list, key=lambda x: x[0][1][0] + x[1][1][0] + x[2][1][0] + x[3][1][0]))

if keyboard.read_key() == "q":
    driver.close()


