Custom Network Topology using Mininet Python API with
	X : No. of hosts
	Y : No. of Switches

Hosts are distributed among the switches.

All the switches are connected.
Odd hosts can ping only odd hosts and even hosts can ping only even hosts.
For odd hosts bandwidth is 1 mbps and for even hosts bandwith is 2 mbps.

e.g. For 8 hosts and 3 switches:
	s1 : h1,h2,h3
	s2 : h4,h5,h6
	s3 : h7,h8

Host connectivity will be as follows:
h1 -> X h3 X h5 X h7 X 
h2 -> X X h4 X h6 X h8 
h3 -> h1 X X h5 X h7 X 
h4 -> X h2 X X h6 X h8 
h5 -> h1 X h3 X X h7 X 
h6 -> X h2 X h4 X X h8 
h7 -> h1 X h3 X h5 X X 
h8 -> X h2 X h4 X h6 X 
