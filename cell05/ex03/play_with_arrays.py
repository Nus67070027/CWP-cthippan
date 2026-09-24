arr: list = [2, 8, 9, 48, 8, 22, -12, 2]
print("Original array:", arr,"\nNew array:", set([i+2 for i in arr if i > 5]))
