class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Need to change to sliding window :(
        size = len(s1)
        counter = dict(Counter(s1))
        print(counter)
        for i in range(len(s2) - size + 1):
            print(dict(Counter(s2[i:i+size])))
            if dict(Counter(s2[i:i+size])) == counter:
                return True
        return False
            # if i in d:
            #     if d[i] > 0:
            #         if not changed:
            #             changed = True
            #         currLength += 1
            #         d[i] -= 1
            #     else:
            #         changed = False
            #         d = counter # reset
            # else:
            #     if currLength == size:
            #         return True
            #     elif changed:
            #         currLength = 0
            #         d = counter # reset
            #     else:
            #         continue