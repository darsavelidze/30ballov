print('введите любое имя')
a=str(input())
while 'Саныч' in a or 'САНЫЧ' in a or 'саныч' in a or 'сАНЫЧ' in a:
    print('введите другое имя')
    a=str(input())
print(a,'хуесос')