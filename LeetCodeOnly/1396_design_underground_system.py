class UndergroundSystem:

    def __init__(self):
        self.ongoing = {}
        self.ave_time = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        if id in self.ongoing:
            return
        self.ongoing[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        if id not in self.ongoing:
            return
        check_in_station, check_in_time = self.ongoing[id]
        if (check_in_station, stationName) in self.ave_time:
            pre_sum, pre_cnt = self.ave_time[(check_in_station, stationName)]
            self.ave_time[(check_in_station, stationName)] = (pre_sum + t - check_in_time, pre_cnt + 1)
        else:
            self.ave_time[(check_in_station, stationName)] = (t - check_in_time, 1)
        del self.ongoing[id]

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        if (startStation, endStation) not in self.ave_time:
            return -1
        s, cnt = self.ave_time[(startStation, endStation)]
        return s / cnt

# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)