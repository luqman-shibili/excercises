def check_palindrome(n):
    reverse = 0
    temp = n
    while temp != 0:
        reverse = reverse * 10 + temp % 10
        temp = temp // 10
    return reverse == n

n =int(input("enter a number to check:"))
if check_palindrome(n):
      print("Yes")
else:
      print("No")