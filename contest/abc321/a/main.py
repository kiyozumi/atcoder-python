N = list(input())
print("Yes") if N == sorted(set(N), reverse=True) else print("No")
