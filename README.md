# steamapi
A simple python wrapper around the unofficial steam api for accessing game information i.e. pricing.

    >>> from api import SteamGame
    >>> s = SteamGame(appid='105600', country='US')
    >>> s.get_price()
    9.99
