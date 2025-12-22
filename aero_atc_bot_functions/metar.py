from typing import Literal

class Metar():

    def __init__(self, pressure: str, wind: str = "", temperature: str = "", dewpoint: str = "", clouds: str = "",
                 visibility: str = ""):
        self.pressure: str = pressure
        self.wind: str = wind
        self.temperature: str = temperature
        self.dewpoint: str = dewpoint
        self.clouds: str = clouds
        self.visibility: str = visibility

    # This function isn't very elegant but it gets the job done
    def to_string(self, fir: Literal["FAA", "CAA", "ICAO"]):
        metar: str = ""
        if (self.wind == "" and self.temperature == "" and self.dewpoint == "" and self.clouds == "" and
            self.visibility == ""):
            if fir == "FAA":
                return f"METAR UNAVAIL A{self.pressure}"
            return f"METAR UNAVAIL QNH {self.pressure}"
        match fir:
            case "FAA":
                if self.wind == "":
                    metar += "WIND UNAVAIL "
                else:
                    metar += f"{self.wind}KT "
                if self.visibility == "":
                    metar += "VISIBILITY UNAVAIL "
                else:
                    metar += f"{self.visibility}SM "
                if self.clouds == "":
                    metar += "CLOUDS UNAVAIL "
                else:
                    metar += f"{self.clouds} "
                if self.temperature == "":
                    metar += "TEMPERATURE UNAVAIL/"
                else:
                    metar += f"{self.temperature}/"
                if self.dewpoint == "":
                    metar += "DEWPOINT UNAVAIL "
                else:
                    metar += f"{self.dewpoint} "
                metar += f"A{self.pressure}"
            case "CAA":
                if self.wind == "":
                    metar += "WIND UNAVAIL "
                else:
                    metar += f"{self.wind}KT "
                if self.visibility == "":
                    metar += "VISIBILITY UNAVAIL "
                else:
                    metar += f"{self.visibility}M "
                if self.clouds == "":
                    metar += "CLOUDS UNAVAIL "
                else:
                    metar += f"{self.clouds} "
                if self.temperature == "":
                    metar += "TEMPERATURE UNAVAIL/"
                else:
                    metar += f"{self.temperature}/"
                if self.dewpoint == "":
                    metar += "DEWPOINT UNAVAIL "
                else:
                    metar += f"{self.dewpoint} "
                metar += f"QNH {self.pressure}"
            case "ICAO":
                if self.wind == "":
                    metar += "WIND UNAVAIL "
                else:
                    metar += f"WIND {self.wind}KT "
                if self.visibility == "":
                    metar += "VIS UNAVAIL "
                else:
                    metar += f"VIS {self.visibility}M "
                if self.clouds == "":
                    metar += "CLD UNAVAIL "
                else:
                    metar += f"{self.clouds} "
                if self.temperature == "":
                    metar += "T UNAVAIL "
                else:
                    metar += f"T{self.temperature} "
                if self.dewpoint == "":
                    metar += "DEWPOINT UNAVAIL "
                else:
                    metar += f"D{self.dewpoint} "
                metar += f"QNH {self.pressure}"
        return metar