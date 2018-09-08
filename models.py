from sqlalchemy import Column, Integer, String, DateTime, Text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# build classes
class Events(Base):
    __tablename__='events'
    eid = Column(Integer, primary_key=True, autoincrement=True)
    traveler = Column(Text)

    def __init__(self, traveler):
        self.traveler = traveler

    def __repr__(self):
        return "<events({}, {})>".format(self.eid, self.traveler)
    '''
class Device(Base):
    tablename = 'device'
    devID = Column(Integer, primary_key=True, autoincrement=True)
    macAddr = Column(String(12))
    description = Column(String(200))
    username = Column(String(45))
    password = Column(String(15))
    ipAddr = Column(String(16))
    platform = Column(String(48))
    version = Column(String(45))
    interface = Column(String(26))
    vlan = Column(Integer)
    lastup = Column(DateTime)
    type = Column(Integer)

def __init__(self, macAddr, description, username, password,
             ipAddr, platform, version, interface, vlan, lastup, type):
    self.macAddr = macAddr
    self.description = description
    self.username = username
    self.password = password
    self.ipAddr = ipAddr
    self.platform = platform
    self.version = version
    self.interface = interface
    self.vlan = vlan
    self.lastup = lastup
    self.type = type

def __repr__(self):
    return "<device({}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {})>".format(
        self.devID, self.macAddr, self.description, self.username, self.password,
        self.ipAddr, self.platform, self.version, self.interface,
        self.vlan, self.lastup, self.type)

    '''
