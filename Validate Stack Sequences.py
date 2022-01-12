class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack =[]
        N =len(popped)
        i =0
        for p in pushed :
            stack.append(p)
            while stack and i <N and stack [-1] ==popped[i] :
                i+=1
                stack.pop ()
        return stack==[]

class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:

        push = 0

        while len(pushed) > 0 and len(popped) > 0 and 0 <= push < len(pushed):

            # check if the element pushed matches 1st popped element
            if pushed[push] == popped[0]:
                pushed.pop(push)
                push -= 1
                if push <= 0: push = 0
                popped.pop(0)
                continue
            # if not then keep incrementing until we match
            push += 1

        # once we have removed all in-between operations
        # only those which can be sequentially pushed and popped
        # remain, thus check if the sequence matches the order
        return pushed == popped[::-1]