class ToDec:

    def __init__(self, bin_val):
        self.value = bin_val
    
    def convert(self):
        for i in self.value:
            if(i != '0' and i != '1'):
                print('This is not a binary!')
                return
        self.stack = []
        for i in self.value:
            self.stack.insert(0,i)
        extant = 0
        deci = 0
        for i in self.stack:
            deci = deci + int(i)*(2 ** extant)
            extant += 1
        
        print('Deci =', deci)
        
class ToBin:

    def __init__(self, dec_val):
        self.value = int(dec_val)

    def convert(self):
        stack = []
        while(self.value > 1):
            remainder = self.value % 2
            self.value = self.value // 2
            stack.insert(0, remainder)
        stack.insert(0, self.value)
        result = ''.join([str(i) for i in stack])
        print('Bin =', result)