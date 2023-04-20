##import needed modules
import urllib.parse
import requests
#
##create RESTful API call to MapQuest
#
base_api_url = "https://www.mapquestapi.com/directions/v2/route"
#start_location = "Lagos"
#destination = "Abuja"
api_key = "HFfW30P4HtujL8JZK0lKvVWToh2MiD3i"

while True:
    start_location = input("Please enter your starting location or 'q' to quit: ")
    if start_location == "q":
        break
    destination = input("Please enter your destination or 'q' to quit: ")
    if destination == "q":
        break
    url = base_api_url + "?" + urllib.parse.urlencode({"key": api_key, "from": start_location, "to": destination})

    json_response = requests.get(url).json()
    #print(json_response)
    print(url)

    #Check status of RESTful API call
    returned_status = json_response["info"]["statuscode"]
    mapquest_copyright = json_response["info"]["copyright"]["text"]
    
    if returned_status == 0:
        print ("The status of your API call was: " + str(returned_status))
        print(mapquest_copyright)
        print("##############################################################")
        print("For your directions the following values were found:")
        print("The total number of miles will be: " + str(json_response["route"]["distance"]))
        #print("The total amount of fuel used will be: " + str(json_response["route"]["fuelUsed"]))
        
        print("##############################################################")
        print("For your directions the following metric system values were found:")
        print("The total number of kilometers will be: " + str(json_response["route"]["distance"]*1.61))
        print("##############################################################")
        
        for turn in json_response["route"]["legs"][0]["maneuvers"]:
            print((turn["narrative"]) + " (" + str(turn["distance"]) + " miles)") 
            #print((turn["directionName"]) + " " + str(turn["formattedTime"]))
            
        print("##############################################################")
    elif returned_status == 402:
        print("##############################################################")
        print("Status Code: " + str(returned_status) + "; Invalid user input for one or both locations!")
        print("##############################################################")
    else:
        print("##############################################################")
        print("For Status Code: " + str(returned_status) + "; Refer to the Following:")
        print("https://developer.mapquest.com/documentation/direction-api/status-codes")
        status_message = json_response["info"]["messages"][0]
        print("The reason for the status code " + str(returned_status) + " is: " + status_message)
        print("##############################################################")
#
# END OF FILE
