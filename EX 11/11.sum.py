import sys
def main():
    left_operand = sys.argv[1]
    right_operand = sys.argv[2]
    operator = sys.argv[3]
    print(eval(left_operand + operator + right_operand))
main()
