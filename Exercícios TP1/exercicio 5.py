def greatestNumber(array):
    greatest = float('-inf')
    
    for num in array:
        if num > greatest:
            greatest = num
    
    return greatest


array = [3, 5, 7, 2, 8, 1]
print(greatestNumber(array))

# Saída: 8
