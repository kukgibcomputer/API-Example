import requests, json

### FROM https://wall.alphacoders.com/ ###

api_key= "INSERT API KEY HERE"
## GET API KEY FROM LINE ID: hertot ###

def failOverAPI():
    try:
        result = requests.get("https://api.boteater.xyz",timeout=0.5)
        if result.status_code == 200:
            return "https://api.boteater.xyz"
        else:
            return "https://api.boteater.us"
    except:
        return "https://api.boteater.us"
    

def search():
    if api_key == "INSERT API KEY HERE":
        print("GET API KEY FROM LINE ID: hertot")
        raise Exception("Wrong API Key")
    search = input("Search query: ") #example naruto
    result = json.loads(requests.get(failOverAPI()+"/alphacoders?search="+search+"&auth="+api_key).text)
    for img in result["result"]:
        print("")
        print("Image Name: "+img["name"])
        print("Link Image: "+img["url"])

search()
