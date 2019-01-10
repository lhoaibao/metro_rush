class Station:
    def __init__(self, line_name, id_station, station_name=None, conn=None):
        self.line_name = line_name
        self.id_station = id_station
        self.station_name = station_name
        self.conn = conn
        self.train = []

    def __repr__(self):
        return '{}({}: {})'.format(self.station_name,
                                   self.line_name, self.id_station)

    def __str__(self):
        return '{}({}: {})'.format(self.station_name,
                                   self.line_name, self.id_station)

    def compare(self, other):
        return (self.line_name == other.line_name and
                self.id_station == other.id_station)
