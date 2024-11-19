from mininet.topo import Topo


class Lattice(Topo):
    def __init__(self, w=3):
        Topo.__init__(self)

        switches = {}
        for i in range(1, w + 1):
            for j in range(1, w + 1):
                switches[(i, j)] = self.addSwitch(f"s{(i-1)*w + j}")

        for i in range(1, w + 1):
            for j in range(1, w + 1):
                if i + 1 <= w:
                    self.addLink(switches[(i, j)], switches[(i + 1, j)])
                if j + 1 <= w:
                    self.addLink(switches[(i, j)], switches[(i, j + 1)])

        h1 = self.addHost("h1")
        self.addLink(h1, switches[(1, 1)])
        h2 = self.addHost("h2")
        self.addLink(h2, switches[(1, w)])
        h3 = self.addHost("h3")
        self.addLink(h3, switches[(w, w)])
        h4 = self.addHost("h4")
        self.addLink(h4, switches[(w, 1)])


topos = {"lattice": Lattice}
