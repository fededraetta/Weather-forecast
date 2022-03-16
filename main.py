import geopy, requests, os, json
from datetime import datetime
from geopy.geocoders import Nominatim

nom = Nominatim(user_agent="my_application")
continua = True
while continua == True:
    continua_1 = True
    print("--------------------------------------------------------")
    location = input("Inserisci un luogo: (città, via, piazza, monumento)\n")
    n = nom.geocode(location)
    while continua_1 == True:
        scelta3 = input("---------------------------------------------------\n"
                        "Cosa vuoi fare?\n"
                        "-------------------------------------------------- \n"
                        "1. Indirizzo               4. Previsione di T     |\n"
                        "2. Coordinate              5. Previsione di P     |\n"
                        "3. Meteo attuale           6. Prob. di P          |\n"
                        "-------------------------------------------------- \n")
        if scelta3 == "1":
            print("----------------------------------------------------------------------------")
            print("L'indirizzo del luogo ricercato è:", n)
            print("----------------------------------------------------------------------------")
        elif scelta3 == "2":
            print("----------------------------------------------------------------------------")
            print("Le coordinate geografiche sono:", n.latitude, "[LAT]", n.longitude, "[LON]")
            print("----------------------------------------------------------------------------")
        elif scelta3 == "3":
            user_api = "39f4ff1222318f37387c9306a34fe359"
            complete_api_link = "http://api.openweathermap.org/data/2.5/weather?q=" + location + "&appid=" + str(
                user_api)
            # use the requests module
            api_link = requests.get(complete_api_link)
            api_data = api_link.json()
            # print(api_data)
            if api_data["cod"] == "404":
                print("###################################################")
                print("Nome città non corretto, controlla il nome inserito")
                print("###################################################")
            else:
                temp_city = ((api_data["main"]["temp"]) - 273.15)
                weather_desc = api_data["weather"][0]["description"]
                hmdt = api_data["main"]["humidity"]
                wind_spd = api_data["wind"]["speed"]
                date_time = datetime.now().strftime("%d %b %Y | %I:%M;%S %p")
                print("----------------------------------------------------------------------------")
                print("Meteo per - {} || {}".format(location.upper(), date_time))
                print("La temperatura attuale è di: {:.2f} C°".format(temp_city))
                print("Attualmente:", weather_desc)
                print("Umidità [%]:", hmdt, "%")
                print("Velocità del vento:", wind_spd, "Km/h")
                print("----------------------------------------------------------------------------")
        elif scelta3 == "4":
            user_api = "39f4ff1222318f37387c9306a34fe359"
            complete_api_link = "http://api.openweathermap.org/data/2.5/forecast?q=" + location + "&appid=" + str(
                user_api)
            api_link = requests.get(complete_api_link)
            api_data = api_link.json()
            if api_data["cod"] == "404":
                print("###################################################")
                print("Nome città non corretto, controlla il nome inserito")
                print("###################################################")
            else:
                for i in range(len(api_data["list"])):
                    print("La temperatura [°C] per l'ora", api_data["list"][i]["dt_txt"], "è:\n",
                          api_data["list"][i]["main"]["temp"] - 273.15,
                          "\n  min =", api_data["list"][i]["main"]["temp_min"] - 273.15, "\n   max =",
                          api_data["list"][i]["main"]["temp_max"] - 273.15,"\n",
                          "\n",
                          "----------------------------------------------------------------------------\n")
        elif scelta3 == "5":
            user_api = "39f4ff1222318f37387c9306a34fe359"
            complete_api_link = "http://api.openweathermap.org/data/2.5/forecast?q=" + location + "&appid=" + str(
                user_api)
            api_link = requests.get(complete_api_link)
            api_data = api_link.json()
            if api_data["cod"] == "404":
                print("###################################################")
                print("Nome città non corretto, controlla il nome inserito")
                print("###################################################")
            else:
                for i in range(len(api_data["list"])):
                    if ("rain" in api_data["list"][i]):
                        print("La pioggia [mm] prevista per l'ora", api_data["list"][i]["dt_txt"], "è:",
                              api_data["list"][i]["rain"]["3h"])
                    elif ("snow" in api_data["list"][i]):
                        print("La neve [mm] prevista per l'ora", api_data["list"][i]["dt_txt"], "è:",
                              api_data["list"][i]["snow"]["3h"],
                              "----------------------------------------------------------------------------\n")
                    else:
                        print("### Nessuna precipitazione prevista per l'ora", api_data["list"][i]["dt_txt"],"###")
        elif scelta3 == "6":
            user_api = "39f4ff1222318f37387c9306a34fe359"
            complete_api_link = "http://api.openweathermap.org/data/2.5/forecast?q=" + location + "&appid=" + str(
                user_api)
            api_link = requests.get(complete_api_link)
            api_data = api_link.json()
            if api_data["cod"] == "404":
                print("###################################################")
                print("Nome città non corretto, controlla il nome inserito")
                print("###################################################")
            else:
                for i in range(len(api_data["list"])):
                    print("Prob. di precipitazione per l'ora:", api_data["list"][i]["dt_txt"],
                          api_data["list"][i]["pop"] * 100, "%",
                          "----------------------------------------------------------------------------\n")
        esci_1 = input("\n"
                       "-----------------------------------------------------------------------------\n"
                       "Ti serve altro per questa città?\n"
                       "-----------------------------------------------------------------------------\n")
        if esci_1 == ("si" or "SI" or "Si" or "Sì" or "sì" or "Y" or "yes" or "YES" or "Yes"):
            continua_1 = True
        else:
            continua_1 = False
    esci_2 = input("\n"
                   "-----------------------------------------------------------------------------\n"
                   "Ricominci con un'altra città o esci?\n"
                   "-----------------------------------------------------------------------------\n")
    if esci_2 == ("ricomincia" or "Ricomincio" or "ricomincia" or "Ricomincia"):
        continua = True
    else:
        continua = False
