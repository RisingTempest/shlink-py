from datetime import datetime
from typing import List, Optional, Dict, Union
from ..parse import Parse
from ..data import Data
from ..data.error import Error

class VisitData(Data):
    referer: Optional[str] = None
    date: Optional[datetime] = None
    userAgent: Optional[str] = None
    visitLocation: Optional[Dict[str, Union[str, float]]] = None
    potentialBot: Optional[bool] = None

    def __init__(self, referer: Optional[str] = None, date: Optional[datetime] = None,
                 userAgent: Optional[str] = None, visitLocation: Optional[Dict[str, Union[str, float]]] = None,
                 potentialBot: Optional[bool] = None) -> None:
        super().__init__()
        self.referer = referer
        self.date = date
        self.userAgent = userAgent
        self.visitLocation = visitLocation
        self.potentialBot = potentialBot

    def to_dict(self):
        date_str = None
        if self.date is not None:
            date_str = str(self.date)
        return {
            "referer": self.referer,
            "date": date_str,
            "userAgent": self.userAgent,
            "visitLocation": self.visitLocation,
            "potentialBot": self.potentialBot,
        }

    @staticmethod
    def parse(json: Dict) -> Union['Error', 'VisitData']:
        if "error" in json:
            return Error.parse(json)

        referer = json.get("referer")
        date = Parse.datetime(json.get("date"))
        userAgent = json.get("userAgent")
        visitLocation = json.get("visitLocation")
        potentialBot = json.get("potentialBot")

        return VisitData(
            referer=referer,
            date=date,
            userAgent=userAgent,
            visitLocation=visitLocation,
            potentialBot=potentialBot
        )