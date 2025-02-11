def soln1(numDigits):

    def addOne(numList):
        n = len(numList)
        remainder = 0
        for i in range(n-1, -1, -1):
            sumX = numList[i] + remainder
            if i == n-1:
                sumX += 1
            if sumX < 2:
                numList[i] = sumX
                break
            if sumX == 2:
                numList[i] = 0
                remainder = 1
        return

    digit = 1
    # while x >= 1:
    while digit < numDigits:
        prev = [0] * digit
        final = [1] * digit
        while prev != final:
            # print the number
            prev_str = ''.join([str(x) for x in prev])
            print(prev_str)

            # increment the number
            addOne(prev)
        final_str = ''.join([str(x) for x in final])
        print(final_str)
        digit += 1

soln1(7)