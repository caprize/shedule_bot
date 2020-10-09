import pandas as pd
import json

file = "sched.xlsx"
df = pd.read_excel(file,  usecols="NV,NW")
sh = {"Понедельник": {"Четные": [], "Нечетные": []},
      "Вторник": {"Четные": [], "Нечетные": []},
      "Среда": {"Четные": [], "Нечетные": []},
      "Четверг": {"Четные": [], "Нечетные": []},
      "Пятница": {"Четные": [], "Нечетные": []},
      "Суббота": {"Четные": [], "Нечетные": []}
      }
keys = list(sh.keys())
for i in range(2, 74):
    df["Unnamed: 385"][i] = str(df["Unnamed: 385"][i])
    df["Unnamed: 385"][i] += " (" + str(df["Unnamed: 386"][i]) + ")"
    if i % 2 == 0 and i < 14:
        sh[keys[0]]["Нечетные"].append(df["Unnamed: 385"][i])
    elif (i % 2 == 1 and i < 14):
        sh[keys[0]]["Четные"].append(df["Unnamed: 385"][i])
    elif i % 2 == 0 and i < 26:
        sh[keys[1]]["Нечетные"].append(df["Unnamed: 385"][i])
    elif (i % 2 == 1 and i < 26):
        sh[keys[1]]["Четные"].append(df["Unnamed: 385"][i])
    elif i % 2 == 0 and i < 38:
        sh[keys[2]]["Нечетные"].append(df["Unnamed: 385"][i])
    elif (i % 2 == 1 and i < 38):
        sh[keys[2]]["Четные"].append(df["Unnamed: 385"][i])
    elif i % 2 == 0 and i < 50:
        sh[keys[3]]["Нечетные"].append(df["Unnamed: 385"][i])
    elif (i % 2 == 1 and i < 50):
        sh[keys[3]]["Четные"].append(df["Unnamed: 385"][i])
    elif i % 2 == 0 and i < 62:
        sh[keys[4]]["Нечетные"].append(df["Unnamed: 385"][i])
    elif (i % 2 == 1 and i < 62):
        sh[keys[4]]["Четные"].append(df["Unnamed: 385"][i])
    elif i % 2 == 0 and i < 74:
        sh[keys[5]]["Нечетные"].append(df["Unnamed: 385"][i])
    elif (i % 2 == 1 and i < 74):
        sh[keys[5]]["Четные"].append(df["Unnamed: 385"][i])
with open("schedule.json", "w") as write_file:
    json.dump(sh, write_file)
