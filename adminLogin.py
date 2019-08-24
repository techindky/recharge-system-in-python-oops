import os
import json
import sys


def addPlan():
    print("Choose operator to add plan in it")
    print("1. Airtel")
    print("2. Vodafone")
    print("3. RelianceJio")
    a = int(input())
    # b = a
    if a == 1:
        fa = open("airtel_plans.json", "r")
        plans = json.load(fa)
        print("price: ")
        price = int(input())
        print("talktime: ")
        talktime = int(input())
        print("sms: ")
        sms = input()
        print("data: ")
        data = input()
        print("validity: ")
        validity = int(input())
        plans.append({"Price": price, "talktime": talktime,
                "sms": sms, "data": data, "validity": validity})
        fs = open("airtel_plans.json", "w")
        json.dump(plans, fs, indent=4)
        fs.close()
        fa.close()
    elif a == 2:
        fa = open("vodafone_plans.json", "r")
        plans = json.load(fa)
        print("price: ")
        price = int(input())
        print("talktime: ")
        talktime = int(input())
        print("sms: ")
        sms = input()
        print("data: ")
        data = input()
        print("validity: ")
        validity = int(input())
        plans.append({"Price": price, "talktime": talktime,
                "sms": sms, "data": data, "validity": validity})
        fs = open("vodafone_plans.json", "w")
        json.dump(plans, fs, indent=4)
        fs.close()
        fa.close()
    elif a == 3:
        fa = open("reliance_jio.json", "r")
        print("price: ")
        price = int(input())
        print("talktime: ")
        talktime = int(input())
        print("sms: ")
        sms = input()
        print("data: ")
        data = input()
        print("validity: ")
        validity = int(input())
        plans.append({"Price": price, "talktime": talktime,
                "sms": sms, "data": data, "validity": validity})
        fs = open("reliance_jio.json", "w")
        json.dump(plans, fs, indent=4)
        fs.close()
        fa.close()
    else:
        print("wrong choice")
        showAdminOptions()


def updatePlan():
    print("Choose operator to add plan in it")
    print("1. Airtel")
    print("2. Vodafone")
    print("3. RelianceJio")
    a = int(input())
    if a == 1:
        fs = open("airtel_plans.json", "r")
        a = json.load(fs)
        i = 1
        for x in a:
            print("{}. price = {}, talktime = {}, sms = {}, data = {}, validity = {}".format(i, int(
                x["price"]), int(x["talktime"]), int(x["sms"]), int(x["data"]), int(x["validity"])))
            i += 1

        print("Enter the plan no. you want to update")
        index = int(input())
        print("Enter the type and its new value you want to update")
        key = input()
        value = int(input())
        a[index - 1][key] = value
        fp = open("airtel_plans.json", "w")
        json.dump(a, fp, indent=4)
        fp.close()
        fs.close()
    elif a == 2:
        fs = open("vodafone_plans.json", "r")
        a = json.load(fs)
        i = 1
        for x in a:
            print("{}. price = {}, talktime = {}, sms = {}, data = {}, validity = {}".format(i, int(
                x["price"]), int(x["talktime"]), int(x["sms"]), int(x["data"]), int(x["validity"])))
            i += 1

        print("Enter the plan no. you want to update")
        index = int(input())
        print("Enter the type and its new value you want to update")
        key = input()
        value = int(input())
        a[index - 1][key] = value
        fp = open("vodafone_plans.json", "w")
        json.dump(a, fp, indent=4)
        fp.close()
        fs.close()
    elif a == 3:
        fs = open("reliance_jio.json", "r")
        a = json.load(fs)
        i = 1
        for x in a:
            print("{}. price = {}, talktime = {}, sms = {}, data = {}, validity = {}".format(i, int(
                x["price"]), int(x["talktime"]), int(x["sms"]), int(x["data"]), int(x["validity"])))
            i += 1

        print("Enter the plan no. you want to update")
        index = int(input())
        print("Enter the type and its new value you want to update")
        key = input()
        value = int(input())
        a[index - 1][key] = value
        fp = open("reliance_jio.json", "w")
        json.dump(a, fp, indent=4)
        fp.close()
        fs.close()
    else:
        print("wrong choice")
        showAdminOptions()


def deletePlan():
    print("Choose operator to add plan in it")
    print("1. Airtel")
    print("2. Vodafone")
    print("3. RelianceJio")
    a = int(input())
    if a == 1:
        fs = open("airtel_plans.json", "r")
        a = json.load(fs)
        i = 1
        for x in a:
            print("{}. price = {}, talktime = {}, sms = {}, data = {}, validity = {}".format(i, int(
                x["price"]), int(x["talktime"]), int(x["sms"]), int(x["data"]), int(x["validity"])))
            i += 1

        print("Enter the plan no. you want to delte")
        index = int(input())
        a[index - 1].clear()
        fp = open("airtel_plans.json", "w")
        json.dump(a, fp, indent=4)
        fp.close()
        fs.close()
    elif a == 2:
        fs = open("vodafone_plans.json", "r")
        a = json.load(fs)
        i = 1
        for x in a:
            print("{}. price = {}, talktime = {}, sms = {}, data = {}, validity = {}".format(i, int(
                x["price"]), int(x["talktime"]), int(x["sms"]), int(x["data"]), int(x["validity"])))
            i += 1

        print("Enter the plan no. you want to delte")
        index = int(input())
        a[index - 1].clear()
        fp = open("vodafone_plans.json", "w")
        json.dump(a, fp, indent=4)
        fp.close()
        fs.close()
    elif a == 3:
        fs = open("reliance_jio.json", "r")
        a = json.load(fs)
        i = 1
        for x in a:
            print("{}. price = {}, talktime = {}, sms = {}, data = {}, validity = {}".format(i, int(
                x["price"]), int(x["talktime"]), int(x["sms"]), int(x["data"]), int(x["validity"])))
            i += 1

        print("Enter the plan no. you want to delte")
        index = int(input())
        a[index - 1].clear()
        fp = open("reliance_jio.json", "w")
        json.dump(a, fp, indent=4)
        fp.close()
        fs.close()
    else:
        print("wrong choice")
        showAdminOptions()


def showAdminOptions():
    print("What do you want to do")
    print("1.ADD")
    print("2.UPDATE")
    print("3.DELETE")
    print("4.Exit")
    a = int(input())
    if a == 1:
        addPlan()
    elif a == 2:
        updatePlan()
    elif a == 3:
        deletePlan()
    elif a == 4:
        exit()
    else:
        print("Wrong choice")
        showAdminOptions()

def adminLoogin():
    if os.path.getsize("admin_login.json") == 0:
        fp = open("admim_login.json", "r")
        a = json.load(fp)
        print("No admin till yet..")
        print("First register yourself")
        print("Enter the email")
        email = input()
        print("Enter the password")
        ps = input()
        a["email"] = email
        a["password"] = ps
        fp.close()

        fs = open("admin_login.json", "w")
        json.dump(a, fs, indent=4)
        fs.close()

    fp = open("admin_login.json", "r")
    su = json.load(fp)
    print("Login ID: ")
    id = input()
    print("Password: ")
    p = input()

    if id == su["email"] and p == su["password"]:
        print("login successfully..")
        showAdminOptions()

    else:
        print("Incorrect credentials")