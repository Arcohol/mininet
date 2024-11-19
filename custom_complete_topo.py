from mininet.topo import Topo


class Complete(Topo):
    def __init__(self, n=5):
        Topo.__init__(self)

        switches = []
        for i in range(1, n + 1):
            switch = self.addSwitch("s" + str(i))
            host = self.addHost("h" + str(i))
            self.addLink(switch, host)

            for s in switches:
                self.addLink(switch, s)

            switches.append(switch)


topos = {"complete": Complete}
