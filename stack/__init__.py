

# Stack algorithms

# 1 special stack with min element in O(1)

# a stack has the operations:
# pop from stack, that removes the first element in O(1)
# push into stack, that inserts element
# isEmpty and isFull that are O(1) too
#
# a stack is FIFO
# alternative solution: https://stackoverflow.com/questions/685060/design-a-stack-such-that-getminimum-should-be-o1

#########################################################################################################


class Stack:

    def __init__(self):
        self.items = []
        self.count = 0

        self.minimums = []
        self.minimum = None

    def push(self, element):
        if self.minimum is None or element <= self.minimum:
            self.minimums.append(element)
            self.minimum = element

        self.items.append(element)

    def get_minimum(self):
        if not self.minimums:
            return None

        return self.minimums[len(self.minimums) - 1]

    def pop(self):
        item = self.items.pop()
        if item <= self.minimum:
            self.minimums.pop()
            if self.minimums:
                self.minimum = self.minimums[len(self.minimums) - 1]

        return item


stack = Stack()
stack.push(5)
stack.push(3)
stack.push(3)
stack.push(3)
print(stack.get_minimum())
stack.push(2)
print(stack.get_minimum())
stack.pop()
print(stack.get_minimum())

print(stack.minimums)
print(stack.items)

stack.pop()
print(stack.get_minimum())

stack.pop()
print(stack.get_minimum())

stack.pop()
print(stack.get_minimum())

stack.pop()
print(stack.get_minimum())

print(stack.items)


#########################################################################################################

# 2 calculate postfix notation

expression = [15, 7, 1, 1, '+', '-', '/', 3, '*', 2, 1, 1, '+', '+', '-']


def evaluate(number_1, number_2, operator):
    if operator == '+':
        return number_1 + number_2

    if operator == '-':
        return number_1 - number_2

    if operator == '/':
        return number_1 / float(number_2)

    if operator == '*':
        return number_1 * number_2


def evaluate_postfix(exp):
    # Can this expression be empty or malformed?
    operators = ['+', '-', '/', '*']
    operator_stack = []
    numbers = []
    for value in reversed(exp):
        if value in operators:
            operator_stack.append(value)
        else:
            numbers.append(value)
            if len(numbers) >= 2:
                # evaluate with the last operator on stack
                result = evaluate(numbers[1], numbers[0], operator_stack.pop())
                numbers = [result]

    print(numbers)
