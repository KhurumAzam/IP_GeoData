from requests import get
import json

class IP_GeoData():

    def nextLine(self):
        print("---------------------------")
    
    def getIP_ipify(self):
            try:
                ip = get('https://api.ipify.org').text
                print("Ipify:"), self.nextLine(), print("My public IP address is: {}".format(ip)),self.nextLine()
                return ip
            except Exception as e:
                print("Error in request to ipify:", str(e))
                pass

    def getIP_API(self):
            try:
                url = 'http://ip-api.com/json/' + self.ip
                ip = get(url).text
                ip_json = json.loads(str(ip))
                ip_json_formatted_str = json.dumps(ip_json, indent=2)
                print('IP_API:'), self.nextLine(), print(ip_json_formatted_str), self.nextLine()
                return ip_json_formatted_str
            except Exception as e:
                print("Error in request to IP-API:", str(e))
                pass
