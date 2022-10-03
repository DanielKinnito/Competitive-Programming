class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        
        answer=[]
        for x in range(1,n+1):
            if x%3==0:
                if x%5==0:
                    answer.append('FizzBuzz')
                elif x%5!=0:
                    answer.append('Fizz')
            elif x%5==0:
                answer.append('Buzz')
            else:
                xn=str(x)
                answer.append(xn)
        return answer
