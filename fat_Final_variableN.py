from mininet.topo import Topo
from mininet.node import OVSSwitch
 
class OVSBridgeSTP( OVSSwitch ):
    """Open vSwitch Ethernet bridge with Spanning Tree Protocol
       rooted at the first bridge that is created"""
    prio = 1000
    def start( self, *args, **kwargs ):
        OVSSwitch.start( self, *args, **kwargs )
        OVSBridgeSTP.prio += 1
        self.cmd( 'ovs-vsctl set-fail-mode', self, 'standalone' )
        self.cmd( 'ovs-vsctl set-controller', self )
        self.cmd( 'ovs-vsctl set Bridge', self,
                  'stp_enable=true',
                  'other_config:stp-priority=%d' % OVSBridgeSTP.prio )
 
switches = { 'ovs-stp': OVSBridgeSTP }

class FatTree( Topo ):

    def __init__( self ):

        # Topology settings
        K = 4                           # K-ary FatTree
  #      podNum = K                      # Pod number in FatTree
        coreSwitchNum = (K/2)    # Core switches 
        edgeSwitchNum = (K)       # edge switches
        hostNum = (K/2)      # Hosts in K-ary FatTree

        # Initialize topology
        Topo.__init__( self )

        coreSwitches = []
        edgeSwitches = []

        # Core
        for core in range(0, coreSwitchNum):
            coreSwitches.append(self.addSwitch("cs_"+str(core)))

        # Edge
        for edge in range(0, edgeSwitchNum):
            edgeThis = self.addSwitch("es_"+"_"+str(edge))
            edgeSwitches.append(edgeThis)
            for x in range(0,(K/2)):
                self.addLink(edgeThis, coreSwitches[x])
    # Host
            for x in range(0, hostNum):
                print("%")
                self.addLink(edgeThis, self.addHost("h_"+str(edge)+"_"+str(x)))

topos = { 'fattree': ( lambda: FatTree() ) }
