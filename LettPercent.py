def percentageLetter(self, s, letter):
    quan = s.count(letter)
    total = len(s)
    percentage = (quan / total) * 100
    return int(percentage)
        
