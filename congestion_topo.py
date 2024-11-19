from mininet.topo import Topo
from mininet.link import TCLink


class Congestion(Topo):
    def __init__(self):
        Topo.__init__(self)

        leftHost = self.addHost("h1")
        rightHost = self.addHost("h2")
        leftSwitch = self.addSwitch("s1")
        rightSwitch = self.addSwitch("s2")

        self.addLink(leftHost, leftSwitch, delay="5ms", bw=100, cls=TCLink)
        self.addLink(
            leftSwitch, rightSwitch, delay="5ms", bw=10, cls=TCLink, max_queue_size=5
        )
        self.addLink(
            rightSwitch,
            rightHost,
            delay="5ms",
            bw=100,
            cls=TCLink,
        )


topos = {"congestion": Congestion}

# after setting queue size to 5, the iperf speed dropped to around 8.4Mbps
# but with congestion control set to BBR, the speed increased to around 9.5Mbps
# the reason for this is that BBR is designed to prevent buffer bloat, which is
# very likely to happen in this case due to the small queue size
