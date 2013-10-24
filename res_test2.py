#!/usr/bin/python

"""
This example shows how to create an empty Mininet object
(without a topology object) and add nodes to it manually.
"""

from mininet.net import Mininet
from mininet.node import Controller, RemoteController, OVSSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel, info

def int2dpid( dpid ):
        try:
            dpid = hex( dpid )[ 2: ]
            dpid = '0' * ( 16 - len( dpid ) ) + dpid
            return dpid
        except IndexError:
            raise Exception( 'Unable to derive default datapath ID - '
                             'please either specify a dpid or use a '
                             'canonical switch name such as s23.' )

def emptyNet():

    "Create a simulated condo of condos network"

    net = Mininet( controller=lambda a: RemoteController(a, ip='128.208.125.59' ))
    #net = Mininet( controller=Controller , switch=OVSSwitch)

    info( '*** Adding controller\n' )
    net.addController( 'c0' )

    info( '*** Adding hosts\n' )
    h1 = net.addHost( 'h1', ip='10.200.0.1' )
    h2 = net.addHost( 'h2', ip='10.200.0.2' )
    h3 = net.addHost( 'h3', ip='10.200.0.3' )
    h4 = net.addHost( 'h4', ip='10.200.0.4' )

    print "DPID: %s \n" % int2dpid(101)
    s1 = net.addSwitch( 's1' )
    s2 = net.addSwitch( 's2' )


    info( '*** Creating host links\n' )
    net.addLink( h1, s1 )
    net.addLink( h2, s2 )
    net.addLink( h3, s2 )
    net.addLink( h4, s2 )

    info( '*** Creating backbone links\n' ) 
    net.addLink( s1 , s2 )


    info( '*** Starting network\n')
    net.start()

    info( '*** Running CLI\n' )
    CLI( net )

    info( '*** Stopping network' )
    net.stop()

if __name__ == '__main__':
    setLogLevel( 'info' )
    emptyNet()
