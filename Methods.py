genome = 0
def initgenome():

	gen[];
		// Randomize the speed
	for i in range(0,16):
			gen.push((-1.0 + 2.0*Math.random()).toFixed(8));

		// Randomize the duration.
	for i in range(16,32):
			gen.push(10 + Math.floor(190*Math.random()));	

return gen

def mutate(gen):

	index = Math.floor(Math.random()*32)
	if (index == 32) :
			index = 31
	if (index < 16) :
			gen[index] = (-1.0 + 2.0*Math.random()).toFixed(8)
 	else :
			gen[index] = Math.floor(10 + Math.floor(190*Math.random()))	

return gen

def setGenome(gen):
	
	genome = gen 
return 0