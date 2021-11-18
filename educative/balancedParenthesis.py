def generate_valid_parentheses(num):
    if not num:
        return ''

    result = [['()']]
            
    # TODO: Write your code here

    return result


def main():
    print("All combinations of balanced parentheses are: " +
          str(generate_valid_parentheses(2)))
    print("All combinations of balanced parentheses are: " +
          str(generate_valid_parentheses(3)))


main()
