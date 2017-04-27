#!/usr/bin/env python
#-*- coding: utf-8-*-
from mininet.topo import Topo
from mininet.net import Mininet

class MyTopo(Topo):
	def __init__(self):
		Topo.__init__(self)
		Host1 = self.addHost('h1')
		Host2 = self.addHost('h2')
		Switch1 = self.addSwitch('s1')
		Switch2 = self.addSwitch('s2')
		Switch3 = self.addSwitch('s3')
		Switch4 = self.addSwitch('s4')
		Switch5 = self.addSwitch('s5')


		self.addLink( Host1, Switch1 )
		self.addLink( Switch1, Switch2 )
		self.addLink( Switch2, Switch5 )
		self.addLink( Switch5, Host2 )
		self.addLink( Switch4, Switch5 )
		self.addLink( Switch3, Switch4 )
		self.addLink( Switch1, Switch3 )
		self.addLink( Switch3, Switch2 )

topos={'mytopo':(lambda:MyTopo())}
