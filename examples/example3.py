# The inner envs are equals except the values of i and flag. So we might want to start enumerate e_cond from flag or i.
a = 'aa'
b = 'bb'
flag = True #added later

for i in range(2):
    #! Start of synth number: 1 of: s
    #! 1) i = 0, a = 'aa', b = 'bb' => s = 0
    #! 2) i = 1, a = 'aa', b = 'bb' => s = 0
    if i > 0:
        #! 1) i = 1, a = 'aa', b = 'bb', flag = True => s = 'aa' #manually added
    	s = a
    else:
        #! 1) i = 0, a = 'aa', b = 'bb', flag = False => s = 'bb' #manually added
    	s = b
#! End of synth number: 1
