
S = input() # '0001100'
arr = list(S) # ['0','0','0','1','1','0','0']

# 0이 연속으로 나온 횟수
a = 0 
# 1이 연속으로 나온 횟수
b = 0

for i in range(len(arr)-1): # 0~6
    if i == 0: # 첫번째 숫자일 때
        if arr[i] == '0':
            a += 1
        else:
            b += 1
    else:       # 첫번째 숫자가 아닐 때
        if arr[i] == '0' and arr[i] != arr[i-1]:
            a += 1
        elif arr[i] == '0' and arr[i] == arr[i-1]:
            continue
        elif arr[i] == '1' and arr[i] == arr[i-1]:
            b += 1
        else:
            continue
            
print(min(a,b))
