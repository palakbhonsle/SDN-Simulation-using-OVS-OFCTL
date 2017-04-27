#!/usr/bin/env python
#-*- coding: utf-8-*-
from mininet.topo import Topo
from mininet.net import Mininet

class MyTopo(Topo):
	def __init__(self):
		Topo.__init__(self)
		Host1 = self.addHost('h1')
		Host2 = self.addHost('h2')
		Host3 = self.addHost('h3')
  		Host4 = self.addHost('h4')
		Host5 = self.addHost('h5')
		Host6 = self.addHost('h6')
		Host7 = self.addHost('h7')
		Host8 = self.addHost('h8')
  		Host9 = self.addHost('h9')
		Host10 = self.addHost('h10')
		Host11 = self.addHost('h11')
		Host12 = self.addHost('h12')
		Host13 = self.addHost('h13')
		Host14 = self.addHost('h14')
		Host15 = self.addHost('h15')
		Host16 = self.addHost('h16')
		Host17 = self.addHost('h17')
		Host18 = self.addHost('h18')

		Switch1 = self.addSwitch('s1')
		Switch2 = self.addSwitch('s2')
		Switch3 = self.addSwitch('s3')
		Switch4 = self.addSwitch('s4')
		Switch5 = self.addSwitch('s5')
		Switch6 = self.addSwitch('s6')
		Switch7 = self.addSwitch('s7')
		Switch8 = self.addSwitch('s8')
		Switch9 = self.addSwitch('s9')

		self.addLink( Host1, Switch1 )
		self.addLink( Host2, Switch1 )
		self.addLink( Host3, Switch1 )

		self.addLink( Host4, Switch2 )
		self.addLink( Host5, Switch2 )
		self.addLink( Host6, Switch2 )

		self.addLink( Host7, Switch3 )
		self.addLink( Host8, Switch3 )
		self.addLink( Host9, Switch3 )

		self.addLink( Host10, Switch4 )
		self.addLink( Host11, Switch4 )
		self.addLink( Host12, Switch4 )

		self.addLink( Host13, Switch5 )
		self.addLink( Host14, Switch5 )
		self.addLink( Host15, Switch5 )

		self.addLink( Host16, Switch6 )
		self.addLink( Host17, Switch6 )
		self.addLink( Host18, Switch6 )
		
                self.addLink( Switch1, Switch7 )
		self.addLink( Switch2, Switch7 )
		self.addLink( Switch3, Switch7 )
		self.addLink( Switch4, Switch7 )		
		self.addLink( Switch5, Switch7 )
		self.addLink( Switch6, Switch7 )

		self.addLink( Switch1, Switch8 )
		self.addLink( Switch2, Switch8 )
		self.addLink( Switch3, Switch8 )
		self.addLink( Switch4, Switch8 )		
		self.addLink( Switch5, Switch8 )
		self.addLink( Switch6, Switch8 )

		self.addLink( Switch1, Switch9 )
		self.addLink( Switch2, Switch9 )
		self.addLink( Switch3, Switch9 )
		self.addLink( Switch4, Switch9 )		
		self.addLink( Switch5, Switch9 )
		self.addLink( Switch6, Switch9 )		

              

topos={'mytopo':(lambda:MyTopo())}
