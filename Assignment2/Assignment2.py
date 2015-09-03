from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import OVSController,CPULimitedHost
from mininet.link import TCLink
from mininet.util import irange,dumpNodeConnections
from mininet.log import setLogLevel


no_hosts=int(raw_input("Enter Number of hosts:"))
no_switches=int(raw_input("Enter Number of switches:"))

class MyTopo( Topo ):

	def __init__( self ):
		Topo.__init__( self )

		# contains the switches
		switch_list=[]

		#creating the switches as s1,s2 and so on
		for i in range(no_switches):
			switch_list.append(self.addSwitch('s'+str(int(i+1))))

		#adding links between switches
		for index in range(len(switch_list)-1):
			self.addLink(switch_list[index],switch_list[index+1])

		host_switch=no_hosts/no_switches
		rem_host=no_hosts%no_switches

		num_host=1

		#creating hosts and distributing them to switches and adding links
		for j in range(len(switch_list)):
			for k in range(host_switch):
				#creating hosts as h1,h2 and so on
				host_name=self.addHost('h'+str(num_host))
				if num_host%2 == 1 :
					# for odd hosts bandwidth is 1mbps
					self.addLink(switch_list[j],host_name,bw=1)
				else:
					self.addLink(switch_list[j],host_name,bw=2)
				num_host+=1
			if rem_host > 0:
				host_name=self.addHost('h'+str(num_host))
				if num_host%2 == 1 :
					self.addLink(switch_list[j],host_name,bw=1)
				else:
					self.addLink(switch_list[j],host_name,bw=2)
				num_host+=1
				rem_host=rem_host-1

setLogLevel('info')

#for even even host connections and for odd odd host connections
net = Mininet(topo=MyTopo(),host=CPULimitedHost,link=TCLink,controller=OVSController)
cnt=1
for i in range(2,no_hosts+1,2):
	ipstr="127.0.0."+str(cnt)
	cnt+=1
	hn=net.get("h"+str(i))
	hn.setIP(ipstr,24)
cnt=1
for i in range(2,no_hosts+1,2):
	ipstr="192.168.0."+str(cnt)
	cnt+=1
	hn=net.get("h"+str(i))
	hn.setIP(ipstr,29)
net.start()
dumpNodeConnections(net.hosts)
net.pingAll()
net.stop()
