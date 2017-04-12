""" rftest2 topology

authors: Marcelo Nascimento (marcelon@cpqd.com.br)
         Allan Vidal (allanv@cqpd.com.br)

Four switches connected in mesh topology plus a host for each switch:

       h1 --- sA ---- sB --- h2
               |  \    |
               |   \   |
               |    \  |
               |     \ |
       h3 --- sC ---- sD --- h4

"""

from mininet.topo import Topo

class rftest2(Topo):
    "RouteFlow Demo Setup"

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

        sA = self.addSwitch("s1")
        sB = self.addSwitch("s2")
        sC = self.addSwitch("s3")
        sD = self.addSwitch("s4")

        self.addLink(h1, sA,0,1)
        self.addLink(h2, sB,0,1)
        self.addLink(h3, sC,0,1)
        self.addLink(h4, sD,0,1)
        self.addLink(sA, sB,2,2)
        self.addLink(sB, sD,3,2)
        self.addLink(sD, sC,3,2)
        self.addLink(sC, sA,3,3)
        self.addLink(sA, sD,4,4)
        
topos = { 'rftest2': ( lambda: rftest2() ) }
