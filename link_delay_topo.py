from mininet.topo import Topo
from mininet.link import TCLink
import random


class LinkDelay(Topo):
    def __init__(self):
        Topo.__init__(self)

        leftHost = self.addHost("h1")
        rightHost = self.addHost("h2")
        leftSwitch = self.addSwitch("s1")
        rightSwitch = self.addSwitch("s2")

        # Modify your topology to set the delay of each link to a random value between 0 ms and 10 ms.
        # In addition, set all link bandwidths to 10 Mbps.
        self.addLink(
            leftHost, leftSwitch, delay=f"{random.randint(0, 10)}ms", bw=10, cls=TCLink
        )
        self.addLink(
            leftSwitch,
            rightSwitch,
            delay=f"{random.randint(0, 10)}ms",
            bw=10,
            cls=TCLink,
        )
        self.addLink(
            rightSwitch,
            rightHost,
            delay=f"{random.randint(0, 10)}ms",
            bw=10,
            cls=TCLink,
        )


topos = {"link_delay": LinkDelay}
