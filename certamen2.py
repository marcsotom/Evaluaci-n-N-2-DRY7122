import urllib.parse

import requests


while True:

    main_api = "https://www.mapquestapi.com/directions/v2/route?"

    orig = input("ingrese ciudad de origen:\n")

    dest = input("ingrese ciudad de destino:\n")

    key = "hCUUqviNcnonBG0GYMjOrPgPzsdTDPf6"

    if orig == "q" or dest == "q":

        break

    

    url = main_api + urllib.parse.urlencode({"key" :key, "from" :orig, "to" :dest})


    json_data = requests.get(url).json()

    json_status = json_data ["info"] ["statuscode"]


    print(url,"es la url")


    if json_status == 0:

        print("API Status: " + str(json_status) + " = A successful route call.\n")

        print("=============================================")

        print("Directions from " + (orig) + " to " + (dest))

        print("Trip Duration:   " + (json_data["route"]["formattedTime"]))

        print("Kilometers:      " + str("{:.2f}".format((json_data["route"]["distance"])*1.61)))

        print("=============================================")
import urllib.parse

import requests


while True:

    main_api = "https://www.mapquestapi.com/directions/v2/route?"

    orig = input("ingrese ciudad de origen:\n")

    dest = input("ingrese ciudad de destino:\n")

    key = "SE INSERTA EL KEY DE MAQQUEST"

    if orig == "q" or dest == "q":

        break

    

    url = main_api + urllib.parse.urlencode({"key" :key, "from" :orig, "to" :dest})


    json_data = requests.get(url).json()

    json_status = json_data ["info"] ["statuscode"]


    print(url,"es la url")


    if json_status == 0:

        print("API Status: " + str(json_status) + " = A successful route call.\n")

        print("=============================================")

        print("Directions from " + (orig) + " to " + (dest))

        print("Trip Duration:   " + (json_data["route"]["formattedTime"]))

        print("Kilometers:      " + str("{:.2f}".format((json_data["route"]["distance"])*1.61)))
import urllib.parse

import requests


while True:

    main_api = "https://www.mapquestapi.com/directions/v2/route?"

    orig = input("ingrese ciudad de origen:\n")

    dest = input("ingrese ciudad de destino:\n")

    key = "SE INSERTA EL KEY DE MAQQUEST"

    if orig == "q" or dest == "q":

        break

    

    url = main_api + urllib.parse.urlencode({"key" :key, "from" :orig, "to" :dest})


    json_data = requests.get(url).json()

    json_status = json_data ["info"] ["statuscode"]


    print(url,"es la url")


    if json_status == 0:

        print("API Status: " + str(json_status) + " = A successful route call.\n")

        print("=============================================")

        print("Directions from " + (orig) + " to " + (dest))

        print("Trip Duration:   " + (json_data["route"]["formattedTime"]))

        print("Kilometers:      " + str("{:.2f}".format((json_data["route"]["distance"])*1.61)))

        print("=============================================")

        for each in json_data["route"]["legs"][0]["maneuvers"]:

            print((each["narrative"]) + " (" + str("{:.2f}".format((each["distance"])*1.61) + " km)"))

            print("=============================================\n")


        break

    elif json_status == 402:

        print("**********************************************")

        print("Status Code: " + str(json_status) + "; Invalid user inputs for one or both locations.")

        print("**********************************************\n")

    elif json_status == 611:

        print("**********************************************")

        print("Status Code: " + str(json_status) + "; Missing an entry for one or both locations.")

        print("**********************************************\n")

    else:

        print("************************************************************************")

        print("For Staus Code: " + str(json_status) + "; Refer to:")

        print("https://developer.mapquest.com/documentation/directions-api/status-codes")

        print("************************************************************************\n")


        print("=============================================")

        for each in json_data["route"]["legs"][0]["maneuvers"]:

            print((each["narrative"]) + " (" + str("{:.2f}".format((each["distance"])*1.61) + " km)"))

            print("=============================================\n")


        break

    elif json_status == 402:

        print("**********************************************")

        print("Status Code: " + str(json_status) + "; Invalid user inputs for one or both locations.")

        print("**********************************************\n")

    elif json_status == 611:

        print("**********************************************")

        print("Status Code: " + str(json_status) + "; Missing an entry for one or both locations.")

        print("**********************************************\n")

    else:

        print("************************************************************************")

        print("For Staus Code: " + str(json_status) + "; Refer to:")

        print("https://developer.mapquest.com/documentation/directions-api/status-codes")

        print("************************************************************************\n")


        for each in json_data["route"]["legs"][0]["maneuvers"]:

            print((each["narrative"]) + " (" + str("{:.2f}".format((each["distance"])*1.61) + " km)"))

            print("=============================================\n")


        break

    elif json_status == 402:

        print("********************import urllib.parse

import requests


while True:

    main_api = "https://www.mapquestapi.com/directions/v2/route?"

    orig = input("ingrese ciudad de origen:\n")

    dest = input("ingrese ciudad de destino:\n")

    key = "SE INSERTA EL KEY DE MAQQUEST"

    if orig == "q" or dest == "q":

        break

    

    url = main_api + urllib.parse.urlencode({"key" :key, "from" :orig, "to" :dest})


    json_data = requests.get(url).json()

    json_status = json_data ["info"] ["statuscode"]


    print(url,"es la url")


    if json_status == 0:

        print("API Status: " + str(json_status) + " = A successful route call.\n")

        print("=============================================")

        print("Directions from " + (orig) + " to " + (dest))

        print("Trip Duration:   " + (json_data["route"]["formattedTime"]))

        print("Kilometers:      " + str("{:.2f}".format((json_data["route"]["distance"])*1.61)))

        print("=============================================")

        for each in json_data["route"]["legs"][0]["maneuvers"]:

            print((each["narrative"]) + " (" + str("{:.2f}".format((each["distance"])*1.61) + " km)"))

            print("=============================================\n")


        break

    elif json_status == 402:

        print("**********************************************")

        print("Status Code: " + str(json_status) + "; Invalid user inputs for one or both locations.")

        print("**********************************************\n")

    elif json_status == 611:

        print("**********************************************")

        print("Status Code: " + str(json_status) + "; Missing an entry for one or both locations.")

        print("**********************************************\n")

    else:

        print("************************************************************************")

        print("For Staus Code: " + str(json_status) + "; Refer to:")

        print("https://developer.mapquest.com/documentation/directions-api/status-codes")

        print("************************************************************************\n")

**************************")

        print("Status Code: " + str(json_status) + "; Invalid user inputs for one or both locations.")

        print("**********************************************\n")

    elif json_status == 611:

        print("**********************************************")

        print("Status Code: " + str(json_status) + "; Missing an entry for one or both locations.")

        print("**********************************************\n")

    else:

        print("************************************************************************")

        print("For Staus Code: " + str(json_status) + "; Refer to:")

        print("https://developer.mapquest.com/documentation/directions-api/status-codes")

        print("************************************************************************\n")

