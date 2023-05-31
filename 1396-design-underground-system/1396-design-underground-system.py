class UndergroundSystem:

    def __init__(self):
        self.routes=defaultdict(list)
        self.checkins=defaultdict(list)
    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkins[id].append([stationName,t])

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        if id in self.checkins:
            res=self.checkins[id][0]
            del self.checkins[id]
        name=str(res[0])+'-'+str(stationName)
        self.routes[name].append(t-res[1])
    def getAverageTime(self, startStation: str, endStation: str) -> float:
        name=startStation+'-'+endStation
        ans=self.routes[name]
        return sum(ans)/len(ans)
        

# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)