
# $Id: hsmtst.py 1162 2009-02-23 23:54:31Z tpschmit $

# ==================================================================
"""
Hsmtst - Interactive example using the Hierarchical State Machine (HSM)
class defined in the "miros" Python module  (i.e. one that implements
behavioral inheritance). It implements the UML state chart shown in the
accompanying image "hsmtst-chart.gif".  

It is based on the excellent work of Miro Samek (hence the module name
"miros"). This implementation closely follows an older C/C++
implementation published in the 8/2000 edition of "Embedded Systems"
magazine by Miro Samek and Paul Montgomery under the title "State
Oriented Programming". The article and code can be found here:
http://www.embedded.com/2000/0008.

A wealth of more current information can be found at Miro's well kept
site: http://www.state-machine.com/.
 
As far as I know this is the first implementation of Samek's work in
Python. It was tested with Python 2.5

It is licensed under the same terms as Python itself.

-----------------------------------------------------------
Change history.
Date        Comments
-----------------------------------------------------------

2/15/09    Tom Schmit, Began porting from Lua version.
2/22/09    TS, test_non_interactive() and test_interactive() run as expected.

"""
# ===================================================================

import miros

# =========================================================
# helpers

import sys
def printf(format, *args):
	sys.stdout.write(format % args)

# 
# ==============================================
# Define event handlers for states. For clarity, the functions are named
# for the states they handle (though this is not required). For details
# see the UML state chart shown in the accompanying image
# "hsmtst-chart.gif".

# ====================================
# Top/root state is state d.

def top(self):
	if self.tEvt['sType'] == "init":
		# display event
		printf("top-%s;", self.tEvt['sType'])
		# transition to state d2.
		self.stateStart(d2)
		# returning a 0 indicates event was handled
		return 0
	elif self.tEvt['sType'] == "entry":
		# display event, do nothing 
		# else except indicate it was handled
		printf("top-%s;", self.tEvt['sType'])
		return 0
	elif self.tEvt['sType'] == "exit":
		printf("top-%s;", self.tEvt['sType'])
		self.tEvt['nFoo'] = 0
		return 0
	elif self.tEvt['sType'] == "e":
		printf("top-%s;", self.tEvt['sType'])
		self.stateTran(d11)
		return 0
	return self.tEvt['sType']

# ====================================                 

def d1(self):
	if self.tEvt['sType'] == "init":
		printf("d1-%s;", self.tEvt['sType'])
		self.stateStart(d11)
		return 0
	elif self.tEvt['sType'] == "entry":
		printf("d1-%s;", self.tEvt['sType'])
		return 0
	elif self.tEvt['sType'] == "exit":
		printf("d1-%s;", self.tEvt['sType'])
		return 0
	elif self.tEvt['sType'] == "a":
		printf("d1-%s;", self.tEvt['sType'])
		self.stateTran(d1)
		return 0
	elif self.tEvt['sType'] == "b":
		printf("d1-%s;", self.tEvt['sType'])
		self.stateTran(d11)
		return 0
	elif self.tEvt['sType'] == "c":
		printf("d1-%s;", self.tEvt['sType'])
		self.stateTran(d2)
		return 0
	elif self.tEvt['sType'] == "f":
		printf("d1-%s;", self.tEvt['sType'])
		self.stateTran(d211)
		return 0
	return self.tEvt['sType']

# 
# ====================================

def d11(self):
	if self.tEvt['sType'] == "entry":
		printf("d11-%s;", self.tEvt['sType'])
		return 0
	elif self.tEvt['sType'] == "exit":
		printf("d11-%s;", self.tEvt['sType'])
		return 0
	elif self.tEvt['sType'] == "d":
		printf("d11-%s;", self.tEvt['sType'])
		self.stateTran(d1)
		self.tEvt['nFoo'] = 0
		return 0
	elif self.tEvt['sType'] == "g":
		printf("d11-%s;", self.tEvt['sType'])
		self.stateTran(d211)
		return 0
	elif self.tEvt['sType'] == "h":
		printf("d11-%s;", self.tEvt['sType'])
		self.stateTran(top)
		return 0
	return self.tEvt['sType']

# ====================================

def d2(self):
	if self.tEvt['sType'] == "init":
		printf("d2-%s;", self.tEvt['sType'])
		self.stateStart(d211)
		return 0
	elif self.tEvt['sType'] == "entry":
		printf("d2-%s;", self.tEvt['sType'])
		if self.tEvt['nFoo'] != 0:
			self.tEvt['nFoo'] = 0
		return 0
	elif self.tEvt['sType'] == "exit":
		printf("d2-%s;", self.tEvt['sType'])
		return 0
	elif self.tEvt['sType'] == "c":
		printf("d2-%s;", self.tEvt['sType'])
		self.stateTran(d1)
		return 0
	elif self.tEvt['sType'] == "f":
		printf("d2-%s;", self.tEvt['sType'])
		self.stateTran(d11)
		return 0
	return self.tEvt['sType']

# 
# ====================================

def d21(self):
	if self.tEvt['sType'] == "init":
		printf("d21-%s;", self.tEvt['sType'])
		self.stateStart(d211)
		return 0
	elif self.tEvt['sType'] == "entry":
		printf("d21-%s;", self.tEvt['sType'])
		return 0
	elif self.tEvt['sType'] == "exit":
		printf("d21-%s;", self.tEvt['sType'])
		return 0
	elif self.tEvt['sType'] == "a":
		printf("d21-%s;", self.tEvt['sType'])
		self.stateTran(d21)
		return 0
	elif self.tEvt['sType'] == "b":
		printf("d21-%s;", self.tEvt['sType'])
		self.stateTran(d211)
		return 0
	elif self.tEvt['sType'] == "g":
		printf("d21-%s;", self.tEvt['sType'])
		self.stateTran(d1)
		return 0
	return self.tEvt['sType']

# ====================================

def d211(self):
	if self.tEvt['sType'] == "entry":
		printf("d211-%s;", self.tEvt['sType'])
		return 0
	elif self.tEvt['sType'] == "exit":
		printf("d211-%s;", self.tEvt['sType'])
		return 0
	elif self.tEvt['sType'] == "d":
		printf("d211-%s;", self.tEvt['sType'])
		self.stateTran(d21)
		return 0
	elif self.tEvt['sType'] == "h":
		printf("d211-%s;", self.tEvt['sType'])
		self.stateTran(top)
		return 0
	return self.tEvt['sType']

# 
# ==============================================
# create HSM instance and populate it with states

hsm = miros.Hsm()

# --------------------------------------------------------------------
#             name                               parent's
#              of              event             event
#             state            handler           handler
# --------------------------------------------------------------------
hsm.addState ( "top",           top,               None)
hsm.addState ( "d1",            d1,                top)
hsm.addState ( "d11",           d11,               d1)
hsm.addState ( "d2",            d2,                top)
hsm.addState ( "d21",           d21,               d2)
hsm.addState ( "d211",          d211,              d21)

# ====================================
# Non-interactive test.

def test_non_interactive():
	# hsm.dump()
	print("\nNon-interactive Hierarchical State Machine Example")
	print "Miros revision: " + hsm.revision	+ "\n"
	print("The following pairs of lines should all match each other and")
	print("the accompanying UML state chart 'hsmtst-chart.gif'.\n")
	# start/initialize HSM
	hsm.onStart(top)
	print("\ntop-entry;top-init;d2-entry;d2-init;d21-entry;d211-entry;\n")
	hsm.onEvent("a")
	print("\nd21-a;d211-exit;d21-exit;d21-entry;d21-init;d211-entry;\n")
	hsm.onEvent("b")
	print("\nd21-b;d211-exit;d211-entry;\n")
	hsm.onEvent("c")
	print("\nd2-c;d211-exit;d21-exit;d2-exit;d1-entry;d1-init;d11-entry;\n")
	hsm.onEvent("d")
	print("\nd11-d;d11-exit;d1-init;d11-entry;\n")
	hsm.onEvent("e")
	print("\ntop-e;d11-exit;d1-exit;d1-entry;d11-entry;\n")
	hsm.onEvent("f")
	print("\nd1-f;d11-exit;d1-exit;d2-entry;d21-entry;d211-entry;\n")
	hsm.onEvent("g")
	print("\nd21-g;d211-exit;d21-exit;d2-exit;d1-entry;d1-init;d11-entry;\n")
	hsm.onEvent("h")
	print("\nd11-h;d11-exit;d1-exit;top-init;d2-entry;d2-init;d21-entry;d211-entry;\n")
	hsm.onEvent("g")
	print("\nd21-g;d211-exit;d21-exit;d2-exit;d1-entry;d1-init;d11-entry;\n")
	hsm.onEvent("f")
	print("\nd1-f;d11-exit;d1-exit;d2-entry;d21-entry;d211-entry;\n")
	hsm.onEvent("e")
	print("\ntop-e;d211-exit;d21-exit;d2-exit;d1-entry;d11-entry;\n")
	hsm.onEvent("d")
	print("\nd11-d;d11-exit;d1-init;d11-entry;\n")
	hsm.onEvent("c")
	print("\nd1-c;d11-exit;d1-exit;d2-entry;d2-init;d21-entry;d211-entry;\n")
	hsm.onEvent("b")
	print("\nd21-b;d211-exit;d211-entry;\n")
	hsm.onEvent("a")
	print("\nd21-a;d211-exit;d21-exit;d21-entry;d21-init;d211-entry;\n")

# ====================================
# Interactive tester/explorer.

def test_interactive():
	# hsm.dump()
	print("\nInteractive Hierarchical State Machine Example")
	print "Miros revision: " + hsm.revision	+ "\n"
	print("Enter 'quit' to end.\n")
	# start/initialize HSM
	hsm.onStart(top)
	while True:
		# get letter of event
		sType = raw_input("\nEvent<-")
		if sType == "quit": return 
		if len(sType) != 1 or sType < "a" or sType > "h": 
			print "Event not defined.", 
		else:
			# dispatch event and display results
			hsm.onEvent(sType)

#  ====================================

# test_non_interactive()
test_interactive()

raw_input("Press return to continue")