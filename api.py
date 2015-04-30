
import requests
import json


class SteamGame:

    def __init__(self, appid=None, country='US'):
        self.appid = str(appid)
        self.country = country
        self._request()

    def _request(self):
        url = 'http://store.steampowered.com/api/appdetails/'

        payload = {'appids':self.appid, 'cc': self.country, 'l': 'english', 'v': 1}

        #Spoof user agent
        user_agent = {
                      'User-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36',
                      'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                      'Accept-language': 'en-US,en;q=0.8',
                      'Accept-Encoding': 'gzip,deflate,sdch'
        }


        r = requests.get(url, headers=user_agent, params=payload)
        j = r.json()

        try:
            self.price = float(j[self.appid]['data']['price_overview']['final'])/100.00
            self.price = round(self.price, 2)
            self.name = j[self.appid]['data']['name']
        except ValueError:
            self.price = None
            print 'Steam Error: response does not contain a valid price'
        except KeyError:
            self.price = None
            print 'Steam Error: response was not valid'

    def get_name(self):
        return self.name

    def get_price(self):
        return self.price

    def get_url(self):
        return 'http://store.steampowered.com/app/{appId}/'.format(appId=self.appid)