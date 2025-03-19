# !!! the list function can turn strings / numbers into a list 
# using "//" will divid it by two and no reminder


term = 12321

term_inp = list(str(abs(term)))

def check(term_inp):
    for i in range(0, len(term_inp)):
        if term_inp[i] == term_inp[-(i + 1)]:
            pass
        else:
            return False
    return True
    
print(check(term_inp))

