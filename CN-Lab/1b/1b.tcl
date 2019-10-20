#Q1. Simulate  three  nodes  point to point  networks  with  duplex  links 
#between  them.  Set the queue size and vary the bandwidth and find the number of packets dropped



#Create a simulator object
set ns [new Simulator]

set traceFile [open 1.tr w]
$ns trace-all $traceFile

set namFile [open out.nam w]
$ns namtrace-all $namFile

proc finish {} {
	global ns namFile traceFile
    
    $ns flush-trace
	
	#Close the trace files
    close $traceFile
    close $namFile
	exec awk -f stats.awk 1.tr &
	exec nam out.nam &
    exit 0
}


# set up three node
set n1 [$ns node]
set n2 [$ns node]
set n3 [$ns node]

# set up duplex links
$ns duplex-link $n1 $n2 0.5Mb 20ms DropTail
$ns duplex-link $n2 $n3 0.5Mb 20ms DropTail
$ns queue-limit $n1 $n2 10
$ns queue-limit $n2 $n3 10

$n1 shape hexagon
$n1 color red
$n3 shape square
$n3 color blue

# Create a UDP agent and attach it to node n1
set udp0 [new Agent/UDP]
$ns attach-agent $n1 $udp0

# Create a CBR traffic source and attach it to udp0
set cbr0 [new Application/Traffic/CBR]
$cbr0 set packetSize_ 512
$cbr0 set interval_ 0.005
$cbr0 attach-agent $udp0

# Create a null agent(sink) and attach it to n3
set null0 [new Agent/Null]
$ns attach-agent $n3 $null0


# Connect traffic source and sink and assign flow id color
$ns connect $udp0 $null0
# $udp0 set fid_ 2


$ns at 0.5 "$cbr0 start"
$ns at 2.0 "$cbr0 stop"
$ns at 2.0 "finish"


#Run the simulation
$ns run




