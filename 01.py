with open('01_input.txt') as f:
    text = f.read().splitlines()

numbers_found = []
for code in text:
    print(code)   
    # find first digit
    for i in range(len(code)):
        print(code[i])
        if code[i].isnumeric():
            first_digit = int(code[i])
            break
        else:
            if code[i:i+3] == 'one':   
                first_digit = 1
                break
            if code[i:i+3] == 'two':
                first_digit = 2
                break
            if code[i:i+5] == 'three':
                first_digit = 3
                break
            if code[i:i+4] == 'four':
                first_digit = 4
                break
            if code[i:i+4] == 'five':
                first_digit = 5
                break
            if code[i:i+3] == 'six':
                first_digit = 6
                break
            if code[i:i+5] == 'seven':
                first_digit = 7
                break
            if code[i:i+5] == 'eight':
                first_digit = 8
                break
            if code[i:i+4] == 'nine':
                first_digit = 9
                break

    # find second digit
    for j in range(len(code)):
        i = len(code) - j - 1
        if code[i].isnumeric():
            second_digit = int(code[i])
            break
        else:
            print(code[i-2:i+1])
            if code[i-2:i+1] == 'one':
                second_digit = 1
                break
            if code[i-2:i+1] == 'two':
                second_digit = 2
                break
            if code[i-4:i+1] == 'three':
                second_digit = 3
                break
            if code[i-3:i+1] == 'four':
                second_digit = 4
                break
            if code[i-3:i+1] == 'five':
                second_digit = 5
                break
            if code[i-2:i+1] == 'six':
                second_digit = 6
                break
            if code[i-4:i+1] == 'seven':
                second_digit = 7
                break
            if code[i-4:i+1] == 'eight':
                second_digit = 8
                break
            if code[i-3:i+1] == 'nine':
                second_digit = 9
                break

    # append to numbers found
    number = 10 * first_digit + second_digit
    numbers_found.append(number)

print(numbers_found)
print(sum(numbers_found))