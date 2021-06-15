# class Solution:
#     """
#     @param gas: An array of integers
#     @param cost: An array of integers
#     @return: An integer
#     """
#
#     def canCompleteCircuit(self, gas, cost):
#         # write your code here
#         if not gas or not cost:
#             return
#
#         gas_circle = gas * 2
#         cost_circle = cost * 2
#         n = len(gas)
#         for start in range(n):
#             if gas_circle[start] < cost_circle[start]:
#                 continue
#             if self.can_travel(gas_circle[start:start+n], cost_circle[start:start+n]):
#                 return start
#
#         return -1
#
#     def can_travel(self, gas_circle, cost_circle):
#         gas_balance = 0
#         for i in range(len(gas_circle)):
#             gas_balance += gas_circle[i]
#             if gas_balance < cost_circle[i]:
#                 return False
#             gas_balance -= cost_circle[i]
#
#         return True


class Solution:
    """
    @param gas: An array of integers
    @param cost: An array of integers
    @return: An integer
    """

    def canCompleteCircuit(self, gas, cost):
        if not gas:
            return None
        if sum(gas) < sum(cost):
            return -1

        gas_balance = 0
        start = 0
        for i in range(len(gas)):
            gas_balance += gas[i] - cost[i]
            if gas_balance < 0:
                gas_balance = 0
                start = i + 1

        return start



if __name__ == '__main__':
    s = Solution()
    gas = [1,1,3,1]
    cost = [2,2,1,1]

    print(s.canCompleteCircuit(gas, cost))