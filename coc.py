#!/usr/bin/python

"""
This example shows how to create an empty Mininet object
(without a topology object) and add nodes to it manually.
"""

from mininet.net import Mininet
from mininet.node import Controller, RemoteController
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

    net = Mininet( controller=lambda a: RemoteController(a, ip='128.208.125.60' ))
    #net = Mininet( controller=Controller )

    info( '*** Adding controller\n' )
    net.addController( 'c0' )

    info( '*** Adding hosts\n' )
    h1 = net.addHost( 'UW_h1', ip='10.200.0.1' )
    #h2 = net.addHost( 'Stanford_h1', ip='10.200.0.2' )
    #h3 = net.addHost( 'UofHawaii_h1', ip='10.200.0.3' )
    h4 = net.addHost( 'USC_h1', ip='10.200.0.4' )
    h5 = net.addHost( 'Utah_h1', ip='10.200.0.5' )
    h6 = net.addHost( 'ASU_h1', ip='10.200.0.6' )
    #h7 = net.addHost( 'Oklahoma_h1', ip='10.200.0.7' )
    h8 = net.addHost( 'Wisc_h1', ip='10.200.0.8' )
    h9 = net.addHost( 'OSC_h1', ip='10.200.0.9' )
    h10 = net.addHost( 'Harvard_h1', ip='10.200.0.10' )
    h11 = net.addHost( 'Clemson_h1', ip='10.200.0.11' )
    h12 = net.addHost( 'Emory_h1', ip='10.200.0.12' )
    h13 = net.addHost( 'SSERCA_h1', ip='10.200.0.13' )

    s101 = net.addSwitch( 'UW', dpid=int2dpid(201) )
    s102 = net.addSwitch( 'Stanford', dpid=int2dpid(202) )
    #s103 = net.addSwitch( 'UofHawaii', dpid=int2dpid(203) )
    s104 = net.addSwitch( 'USC', dpid=int2dpid(204) )
    s105 = net.addSwitch( 'Utah', dpid=int2dpid(205) )
    s106 = net.addSwitch( 'ASU', dpid=int2dpid(206) )
    s107 = net.addSwitch( 'Oklahoma', dpid=int2dpid(207) )
    s108 = net.addSwitch( 'Wisc', dpid=int2dpid(208) )
    s109 = net.addSwitch( 'OSC', dpid=int2dpid(209) )
    s110 = net.addSwitch( 'Harvard', dpid=int2dpid(210) )
    s111 = net.addSwitch( 'Clemson', dpid=int2dpid(211) )
    s112 = net.addSwitch( 'Emory', dpid=int2dpid(212) )
    s113 = net.addSwitch( 'SSERCA', dpid=int2dpid(213) )

    info( '*** Adding backbone switches\n' )
    s3 = net.addSwitch( 'I2_SEAT' , dpid=int2dpid(103) )
    s4 = net.addSwitch( 'I2_SUNN' , dpid=int2dpid(104) )
    s5 = net.addSwitch( 'I2_LOSA' , dpid=int2dpid(105) )
    s6 = net.addSwitch( 'I2_SALT' , dpid=int2dpid(106) )
    s7 = net.addSwitch( 'I2_DENV' , dpid=int2dpid(107) )
    s8 = net.addSwitch( 'I2_ELPA' , dpid=int2dpid(108) )
    s9 = net.addSwitch( 'I2_KANS' , dpid=int2dpid(109) )
    s10 = net.addSwitch( 'I2_HOUS' , dpid=int2dpid(110) )
    s11 = net.addSwitch( 'I2_CHIC' , dpid=int2dpid(111) )
    s12 = net.addSwitch( 'I2_CLEV' , dpid=int2dpid(112) )
    s13 = net.addSwitch( 'I2_NEWY' , dpid=int2dpid(113) )
    s14 = net.addSwitch( 'I2_WASH' , dpid=int2dpid(114) )
    s15 = net.addSwitch( 'I2_ATLA' , dpid=int2dpid(115) )
    s16 = net.addSwitch( 'I2_TULS' , dpid=int2dpid(116) )
    s17 = net.addSwitch( 'I2_BOST' , dpid=int2dpid(117) )

    info( '*** Creating host links\n' )
    # UW
    net.addLink( h1, s101 )
    net.addLink( s101, s3 )
    # Stanford
    #net.addLink( h2, s102 )
    net.addLink( s102, s4 )
    # UofHawai
    #net.addLink( h3, s103 )
    #net.addLink( s103, s3 )
    # USC
    net.addLink( h4, s104 )
    net.addLink( s104, s5 )
    # Utah
    net.addLink( h5, s105 )
    net.addLink( s105, s6 )
    # ASU
    net.addLink( h6, s106 )
    net.addLink( s106, s5 )
    # OU
    #net.addLink( h7, s107 )
    net.addLink( s107, s16 )
    # Wisc
    net.addLink( h8, s108 )
    net.addLink( s108, s11 )
    # OSC
    net.addLink( h9, s109 )
    net.addLink( s109, s11 )
    # Harvard
    net.addLink( h10, s110 )
    net.addLink( s110, s17 )
    # Clemson
    net.addLink( h11, s111 )
    net.addLink( s111, s15 )
    # Emory
    net.addLink( h12, s112 )
    net.addLink( s112, s15 )
    # SSERCA
    net.addLink( h13, s113 )
    net.addLink( s113, s15 )
   

    info( '*** Creating backbone links\n' ) 
    net.addLink( s3 , s4 )
    net.addLink( s3 , s6 )
    net.addLink( s3 , s11 )
   
    net.addLink( s4 , s6 )
    net.addLink( s4 , s5 )
     
    net.addLink( s5 , s6 )
    net.addLink( s5 , s8 )

    net.addLink( s6 , s7 )

    net.addLink( s7 , s8 )
    net.addLink( s7 , s9 )

    net.addLink( s8 , s10 )
  
    net.addLink( s9 , s16 )
    net.addLink( s9 , s11 )

    net.addLink( s10, s15 )
    net.addLink( s10, s16 )
   
    net.addLink( s11, s12 )
    net.addLink( s11, s15 ) 
   
    net.addLink( s12, s17 )
    net.addLink( s12, s14 )
    
    net.addLink( s13, s17 )
    net.addLink( s13, s14 )

    net.addLink( s14, s15 )


    info( '*** Starting network\n')
    net.start()

    info( '*** Running CLI\n' )
    CLI( net )

    info( '*** Stopping network' )
    net.stop()

if __name__ == '__main__':
    setLogLevel( 'info' )
    emptyNet()
