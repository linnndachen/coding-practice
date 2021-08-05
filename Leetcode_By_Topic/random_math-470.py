# The rand7() API is already defined for you.
def rand7():
    pass
# @return a random integer in the range 1 to 7

class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        num = 0
        for i in range(2):
            num = num*7 + rand7()-1

        while num >= 40:
            num = 0
            for i in range(2):
                num = num*7 + rand7()-1

        return num % 10 + 1


    # follow ups:
    # 1. expected value of rand(7) ?
    # 2*40/49 + 9/49*(2 + 2*40/49 + 9/49 * (2 + 2*40/49 + ....)) => 2.54
    # = 2 * (40/49 + 9/49*(2*40/49 + 9/49 * (2*40/49 + ...))    )
    # = 2*40/49 * 1/(1-9/49)

    # 2. 最多需要try 多少次?
    # rand(7) = log(7) => information entropy
    # how many rand(7) we need to provide a rand(10) information?
    # log(10) / log(7) => 1.183

    # 3. how can we ensure we get close to trying only 1.833 times?
    # use range(7^7-1) = 823542 -> 设一个10的倍数，as the retry cutoff point
    # for example if x >= 800000, retry. This means we get ~799999
    # 7[99999] the last 5 digits are evenly distributed
    # this means, we call rand7() 7 times and we get 5 randomly evenly distributed num
    # 7/5 ~1.2times