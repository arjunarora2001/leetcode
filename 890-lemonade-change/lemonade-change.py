class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        numFives = 0
        numTens = 0
        for customer in bills:
            match customer:
                case 5:
                    numFives += 1
                case 10:
                    if numFives == 0:
                        return False
                    else:
                        numFives -= 1
                        numTens += 1
                case 20:
                    if numTens >= 1 and numFives >= 1:
                        numTens -= 1
                        numFives -= 1
                    elif numTens == 0 and numFives >= 3:
                        numFives -= 3
                    else:
                        return False
                case _:
                    return False
        return True