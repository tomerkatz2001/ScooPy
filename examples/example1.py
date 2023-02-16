# In this example we can see that y by itself is not good condidate for e_cond since the user added the second example in synth number 2
# in contrast to e_cond the synthesizer choose in the first synth.

y = 2
z = 3

#! Start of synth number 1 of: x
#! 1) y = 2, z = 3 => x = 0
#! 2) y = 3, z = 3 => x = 5 #manually added
if y > 2:
    x = z + 2
else: 
    #! Start of synth number 2 of: x
    #! 1) y = 2, z = 3 => x = 5
    #! 2) y = 4, z = 3 => x = 5 #manually added
    x = y + z
    #! End of synth number 2
#! End of synth number 1
