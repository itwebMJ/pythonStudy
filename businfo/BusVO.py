class BusVo:
    def __init__(self, busRouteId=None,busRouteNm=None,stStationNm=None,edStationNm=None,term=None,firstBusTm=None,lastBusTm=None,corpNm=None):
        self.busRouteId = busRouteId
        self.busRouteNm = busRouteNm
        self.stStationNm = stStationNm
        self.edStationNm = edStationNm
        self.term = term
        self.firstBusTm = firstBusTm
        self.lastBusTm = lastBusTm
        self.corpNm = corpNm

    def __str__(self):
        return 'busRouteId : '+ str(self.busRouteId)+'\nbusRouteNm : '+str(self.busRouteNm)+'\nstStationNm : '\
               +self.stStationNm+'\nedStationNm : '+self.edStationNm+'\nterm :'+str(self.term)+'\nfirstBusTm :'\
               +str(self.firstBusTm)+'\nlastBusTm : '+str(self.lastBusTm)+'\ncorpNm : '+self.corpNm

class PointVo:
    def __init__(self, no=None, gpsX=None, gpsY=None):
        self.no = no
        self.gpsX = gpsX
        self.gpsY = gpsY

    def __str__(self):
        return 'no : '+str(self.no)+' ('+str(self.gpsX)+', '+str(self.gpsY)+')'

class StationVo:
    def __init__(self, seq=None, stationNm=None, arsId=None):
        self.seq = seq
        self.stationNm = stationNm
        self.arsId = arsId

    def __str__(self):
        return 'seq : '+str(self.seq)+'\nstationNm : '+self.stationNm+'\narsId : '+str(self.arsId)

