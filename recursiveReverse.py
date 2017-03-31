def recursive_reverse_str(sent):
    if len(sent) <= 1:
        return sent
    else:
        return recursive_reverse_str(sent[1:]) + sent[0]

def recursive

print(recursive_reverse_str("varun"))



def moveTower(height,fromPole, toPole, withPole):
    if height >= 1:
        moveTower(height-1,fromPole,withPole,toPole)
        moveDisk(fromPole,toPole)
        moveTower(height-1,withPole,toPole,fromPole)