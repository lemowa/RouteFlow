
from mininet.topo import Topo

class rftest3(Topo):
    "RouteFlow Demo s5tup"

    def __init__( self, enable_all = True ):
        "Create custom topo."

        Topo.__init__( self )

        h1 = self.addHost("h1",
                          ip="172.31.1.100/24",
                          defaultRoute="gw 172.31.1.1")

        h2 = self.addHost("h2",
                          ip="172.31.2.100/24",
                          defaultRoute="gw 172.31.2.1")

        h3 = self.addHost("h3",
                          ip="172.31.3.100/24",
                          defaultRoute="gw 172.31.3.1")

        h4 = self.addHost("h4",
                          ip="172.31.4.100/24",
                          defaultRoute="gw 172.31.4.1")

        h5 = self.addHost("h5",
                          ip="172.31.5.100/24",
                          defaultRoute="gw 172.31.5.1")

        h6 = self.addHost("h6",
                          ip="172.31.6.100/24",
                          defaultRoute="gw 172.31.6.1")

        s1 = self.addSwitch("s1")
        s2 = self.addSwitch("s2")
        s3 = self.addSwitch("s3")
        s4 = self.addSwitch("s4")
        s5 = self.addSwitch("s5")
        s6 = self.addSwitch("s6")

        self.addLink(h1, s1,0,1)
        self.addLink(h2, s2,0,1)
        self.addLink(h3, s3,0,1)
        self.addLink(h4, s4,0,1)

        self.addLink(h5, s5,0,1)
        self.addLink(h6, s6,0,1)

        self.addLink(s1, s2,2,2)
        self.addLink(s2, s4,3,2)
        self.addLink(s4, s3,3,2)
        self.addLink(s3, s1,3,3)
        self.addLink(s1, s4,4,4)

        self.addLink(s3, s5,4,2)
        self.addLink(s4, s6,5,2)
        self.addLink(s5, s6,3,3)



topos = { 'rftest3': ( lambda: rftest3() ) }
