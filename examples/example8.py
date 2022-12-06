#When synthesizing the whole function again we can make an example by taking x_in and the final x_out. 
#In addition if the program's synthesized var is independent from other vars in the function we can return the composition of all the exps.
#If it's not the case we can try it but we can't guarantee it will work. for example here:

def bottomUP(x):
    steps = 3
    y = 1
    for step in range(steps):
        if step == 0:   
            #! Start of synth number: 1 of: x
            #! 1) x_in = 5 => x = 6
            x += y
            #! End of synth number: 1
        elif step == 1:
            y = 3
            #! Start of synth number: 2 of: x
            #! 1) x_in = 6 => x = 9  
            x += y
            #! End of synth number: 2
        elif step == 2:
            #! Start of synth number: 3 of: x
            #! 1) x_in = 9 => x = 7 
            x = x - step
            #! End of synth number: 3
    return x


bottomUP(5)
