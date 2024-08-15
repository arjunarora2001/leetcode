class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        register = {
            5: 0,
            10: 0,
            20: 0
        }
        for customer in bills:
            match customer:
                case 5:
                    register[5] += 1
                case 10:
                    if register[5] == 0:
                        return False
                    else:
                        register[5] -= 1
                        register[10] += 1
                case 20:
                    if register[10] >= 1 and register[5] >= 1:
                        register[10] -= 1
                        register[5] -= 1
                    elif register[10] == 0 and register[5] >= 3:
                        register[5] -= 3
                        register[20] += 1
                    else:
                        return False
                case _:
                    return False
        return True