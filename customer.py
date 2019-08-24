import os
import json
import sys

email = None
password = None


def CheckBalance():
    data_customers = open("account_details.json", "r")
    customers = json.load(data_customers)

    for customer in customers:
        if customer["mobile"] == password:
            data = customer
            break

    if data:
        print("Choose type of balance")
        print("1. Talktime")
        print("2. Sms")
        print("3. Data")
        tp = int(input())
        if tp == 1:
            a = "talktime"
            print("Your current {} balance is Rs {} and valid for {} days".format(
                a, data[a], data["validity"]))
        elif tp == 2:
            a = "sms"
            print("Your current {} balance is {} sms and valid for {} days".format(
                a, data[a], data["validity"]))
        elif tp == 3:
            a = "data"
            print("Your current {} balance is {} GB and valid for {} days".format(
                a, data[a], data["validity"]))
        else:
            print("invalid choice")
            exit()

    else:
        print("sorry invalid mobile no entered")
        CheckBalance()

    data_customers.close()


def browsePlans():
    print("Which operator plans you want to see")
    print("1. Airtel")
    print("2. Vodafone")
    print("3. RelianceJio")
    print("4. Back")
    op = int(input())
    if op == 1:
        fs = open("airtel_plans.json", "r")
        a = json.load(fs)
        i = 1
        for x in a:
            print("{}. price = {}, talktime = {}, sms = {}, data = {}, validity = {}".format(i, int(
                x["price"]), int(x["talktime"]), int(x["sms"]), int(x["data"]), int(x["validity"])))
            i += 1

    elif op == 2:
        fs = open("vodafone_plans.json", "r")
        a = json.load(fs)
        i = 1
        for x in a:
            print("{}. price = {}, talktime = {}, sms = {}, data = {}, validity = {}".format(i, int(
                x["price"]), int(x["talktime"]), int(x["sms"]), int(x["data"]), int(x["validity"])))
            i += 1
    elif op == 3:
        fs = open("reliance_jio.json", "r")
        a = json.load(fs)
        i = 1
        for x in a:
            print("{}. price = {}, talktime = {}, sms = {}, data = {}, validity = {}".format(i, int(
                x["price"]), int(x["talktime"]), int(x["sms"]), int(x["data"]), int(x["validity"])))
            i += 1
    elif op == 4:
        customerOptions()

    else:
        print("wrong choice")
        browsePlans()


def recharge():
    print("Enter your mobile number: ")
    mbno = int(input())
    qs = open("account_details.json", "r")
    info = json.load(qs)
    i = 0
    for x in info:
        if x["mobile"] == mbno:
            count = 0
            break
        i += 1
    if count == 0:
        print("Choose your service provider")
        print("1. Airtel")
        print("2. Vodafone")
        print("3. RelianceJio")
        print("4. Back")
        a = int(input())
        if a == 1:
            fs = open("airtel_plans.json", "r")
            a = json.load(fs)
            j = 1
            for x in a:
                print("{}. price = {}, talktime = {}, sms = {}, data = {}, validity = {}".format(j, int(
                    x["price"]), int(x["talktime"]), int(x["sms"]), int(x["data"]), int(x["validity"])))
                j += 1
            fs.close()
            print("choose a plan to recharge")
            choice = int(input())
            data = a[choice - 1]
            info[i]["talktime"] = data["talktime"]
            info[i]["sms"] = data["sms"]
            info[i]["data"] = data["data"]
            info[i]["validity"] = data["validity"]
            rs = open("account_details.json", "w")
            json.dump(info, rs, indent=4)
            rs.close()
            qs.close()
        elif a == 2:
            fs = open("vodafone_plans.json", "r")
            a = json.load(fs)
            j = 1
            for x in a:
                print("{}. price = {}, talktime = {}, sms = {}, data = {}, validity = {}".format(j, int(
                    x["price"]), int(x["talktime"]), int(x["sms"]), int(x["data"]), int(x["validity"])))
                j += 1
            fs.close()
            print("choose a plan to recharge")
            choice = int(input())
            data = a[choice - 1]
            info[i]["talktime"] = data["talktime"]
            info[i]["sms"] = data["sms"]
            info[i]["data"] = data["data"]
            info[i]["validity"] = data["validity"]
            rs = open("account_details.json", "w")
            json.dump(info, rs, indent=4)
            rs.close()
            qs.close()
        elif a == 3:
            fs = open("reliance_jio.json", "r")
            a = json.load(fs)
            j = 1
            for x in a:
                print("{}. price = {}, talktime = {}, sms = {}, data = {}, validity = {}".format(j, int(
                    x["price"]), int(x["talktime"]), int(x["sms"]), int(x["data"]), int(x["validity"])))
                j += 1
            fs.close()
            print("choose a plan to recharge")
            choice = int(input())
            data = a[choice - 1]
            info[i]["talktime"] = data["talktime"]
            info[i]["sms"] = data["sms"]
            info[i]["data"] = data["data"]
            info[i]["validity"] = data["validity"]
            rs = open("account_details.json", "w")
            json.dump(info, rs, indent=4)
            rs.close()
            qs.close()
        elif a == 4:
            customerOptions()
        else:
            print("wrong choice")
            recharge()


def customerOptions():
    print("Choose actions")
    print("1. Check Balance")
    print("2. Browse Plans")
    print("3. Recharge")
    print("4. Exit")
    action = int(input())
    if action == 1:
        CheckBalance()
    elif action == 2:
        browsePlans()
    elif action == 3:
        recharge()
    elif action == 4:
        exit()
    else:
        print("Oops! Wrong choice")
        customerOptions()


def newCustomer():
    print("Enter your name: ")
    name = input()
    print("Enter your email: ")
    email = input()
    print("You are (M/F/Others)")
    gender = input()
    if gender == "M":
        gender = "male"
    elif gender == "F":
        gender = "female"
    else:
        gender = "Others"
    print("What is your nationality?")
    nationality = input()
    print("Enter your date of birth")
    dob = input()
    i = 0
    for i in range(0, 2):
        print("Enter your service provider from the following ones(Airtel/Vodafone/RelianceJio)")
        sp = input()
        if sp == "Airtel" or sp == "Vodafone" or sp == "RelianceJio" or sp == "airtel" or sp == "vodafone" or sp == "reliancejio":
            serviceProvider = sp
            break
        else:
            print("Sorry! Invalid choice of operators")
            i += 1
            print("You have only {} more chance left".format(i))
    print("Enter the mobile no you want: ")
    mbno = int(input())
    print("Your LOGIN_ID and PASSWORD will be your email and mobile number respectively")

    fp = open("customer.json", "r")
    if os.path.getsize("customer.json") == 0:
        customers = []
    else:
        customers = json.load(fp)

    newCustomer = {"name": name, "email": email, "gender": gender, "nationality": nationality,
                   "DOB": dob, "service_provider": serviceProvider, "mobile": mbno}
    customers.append(newCustomer)
    fp.close()

    fw = open("customer.json", "w")
    json.dump(customers, fw, indent=4)
    fw.close()

    fs = open("account_details.json", "r")
    if os.path.getsize("account_details.json") == 0:
        account_details = []
    else:
        account_details = json.load(fs)
    
    info = {"email": email, "mobile": mbno,
            "talktime": 0, "sms": 0, "data": 0, "validity": 0}
    account_details.append(info)
    fs.close()

    fa = open("account_details", "w")

    json.dump(account_details, fa, indent=4)
    fa.close()


def existingUser():
    global email
    global password
    print("Enter your login id: ")
    mail = input()
    print("Enter your password: ")
    p = int(input())
    email = mail
    password = p
    fp = open("customer.json", "r")
    details = json.load(fp)
    for customer in details:
        if customer["email"] == email and customer["mobile"] == password:
            print("Login successfully")
            existingUser = customer
            break

    fp.close()
    if existingUser:
        customerOptions()
