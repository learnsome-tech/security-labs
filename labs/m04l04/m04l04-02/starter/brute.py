secret='hunter2'
guesses=['123456','password','qwerty','letmein','dragon','monkey','hunter2']
answered=0
for guess in guesses:
    answered += 1
    if guess == secret:
        break
print('requests answered:', answered)
print('password recovered:', guess)
print('limit enforced:', False)
