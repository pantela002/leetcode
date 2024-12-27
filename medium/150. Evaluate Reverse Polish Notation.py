class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i not in ['+','-','*','/']:
                stack.append(int(i))
            else:
                pom1 = stack.pop()
                pom2 = stack.pop()
                if i == '+':
                    stack.append(pom2+pom1)
                elif i == '-':
                    stack.append(pom2-pom1)
                elif i == '*':
                    stack.append(pom2*pom1)
                elif i == '/':
                    stack.append(int(pom2/pom1))
        return stack[0]
