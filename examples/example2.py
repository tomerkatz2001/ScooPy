# In this example we can see that the user gave (at least a start of) partition. When synthesizing the outer scope we can skip all the 
# partitions that don't agree with the given partition.

y = 2
z = 3

for i in range(3):
    #! Start of synth number 1 of: t
    #! 1) i = 0, y = 2, z = 3 => t = 6
    #! 2) i = 1, y = 2, z = 3 => t = 8
    #! 3) i = 2, y = 2, z = 3 => t = 10
    if i > 0:
    	t = y + t
    else:
    	#! Start of synth number: 2 of: t
        #! 1) i = 0, y = 2, z = 3 => t = 6
        #! 2) i = 2, y = 2, z = 3 => t = 10 #manually added here
        t = z + z
        #! End of synth number: 2
#! End of synth number 1
