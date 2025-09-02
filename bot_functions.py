import time
from random import randint

class ATIS:
    def __init__(self, airport: str, wind: str, temp: str, dewpoint: str):
        self.id
        self.airport = airport
        self.fir: str = get_fir(self.airport)
        self.wind = wind
        self.temp = temp
        self.dewpoint = dewpoint
    
    def to_string(self):
        if self.fir == "FAA":
            pass
        elif self.fir == "CAA":
            pass
        elif self.fir == "ICAO":
            pass

def find_frequency(airport: str) -> str:
    if airport.upper() == "KCIA":
        return "KCIA WIP"
    else:
        return "WIP"
    
def get_time_utc() -> str:
    return time.strftime("%H%MZ", time.gmtime(time.time()))

def generate_squawk() -> str:
    squawk: str = ""
    for i in range(0,4):
        squawk = squawk + str(randint(0,7))
    return squawk

def generate_atis(airport: str, wind: str, visibility: str, clouds: str, temp: str, dewpoint: str) -> str:
    atis: str = ""
    fir: str = get_fir(airport)
    if fir == "FAA":
        pass
    elif fir == "CAA":
        pass    
    elif fir == "ICAO":
        pass
    else:
        return "ERRAirport not found"
    atis += "`test success`"
    return atis

# TODO
def get_fir(airport: str):
    return "FAA"