#!/usr/bin/python
import math

gates_seq=range(6,0,-1)+range(1,7)
gates_seq=[4,5,6]+gates_seq*100
months_days=[29,30]*6
days_per_gate=2.5
direction=1;

def gate_representation(f):
	parts=divmod(f,1);
	return chr(ord("A")-1+int(parts[0]))+"+"+str(parts[1]);

def int_part(f):
	return int(divmod(f,1)[0])

def frac_part(f):
	return divmod(f,1)[1];

def repr_frac(f):
	return str(int(7*frac_part(f)))+"/7"

days_list=[];
for month in range(0,12):
	for day in range(0,months_days[month]):
		days_list.append(str(day+1)+"/"+str(month+1))

curr_day=0.00001;
curr_gate=0;

print "days per gate: " + str(days_per_gate)+"\r\n";
while 1:
	next_day=curr_day+days_per_gate;
	print "gate: " + str(gates_seq[curr_gate]) + "\t\tday: " + str((next_day))[0:5] + "\tdates: " + str(days_list[int_part(curr_day):int_part(next_day)])+"\r\n";
	if (int_part(curr_day)>len(days_list)): break
	curr_gate=curr_gate+1
	curr_day=next_day;

#print "<html><body><table border='1'><tr><th>date</th><th>gate</th></tr>";
#print days_list;
#print "</table></body></html>"