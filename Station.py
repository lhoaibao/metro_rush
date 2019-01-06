class Station:
    def __init__(self, line_name, id_station, station_name=None, conn=None):
        self.line_name = line_name
        self.id_station = id_station
        self.station_name = station_name
        self.conn = conn

    def compare(self, other):
        return (self.line_name == other.line_name and
                self.id_station == other.id_station)
