from __future__ import generators
from myhdl import Signal, delay, Simulation, intbv

def bin2gray(width, B, G):
    """ Gray encoder.

    width -- bit width
    B -- input intbv signal, binary encoded
    G -- output intbv signal, gray encoded
    """
    while 1:
        yield B
        for i in range(width):
            G.next[i] = B.val[i+1] ^ B.val[i]

bin = intbv.bin # shorthand alias
def test():
    
    width = 4
    B = Signal(intbv(0))
    G = Signal(intbv(0))
    
    dut = bin2gray(width, B, G)

    def stimulus():
        for i in range(2**width):
            B.next = intbv(i)
            yield delay(10)
            print "input: %4s | output: %4s" % (bin(B.val), bin(G.val))

    return (dut, stimulus())

Simulation(test()).run()
    

            