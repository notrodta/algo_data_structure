n = int(input().strip())
a = list(map(int, input().strip().split(' ')))

swap_counter = 0

for i in range(0, n):
    for j in range(0, n - 1):
        if a[j] > a[j + 1]:
            temp = a[j]
            a[j] = a[j + 1]
            a[j + 1] = temp
            swap_counter += 1

print("Array is sorted in " + str(swap_counter) + " swaps.")
print("First Element: " + str(a[0]))
print("Last Element: " + str(a[-1]))
