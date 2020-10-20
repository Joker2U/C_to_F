# F = C * (9 / 5) + 32
# C = (F - 32) * (5 / 9)
degree = int(input('攝氏溫度: '))
C = degree
F = C * (9 / 5) + 32
print(f'你輸入的溫度為 {C} ,華氏溫度為 {F}')
print('你輸入的溫度為', C , ',華氏溫度為', F)
print('你輸入的溫度為 {} ,華氏溫度為 {}'.format(C,F))
print('你輸入的溫度為 %d ,華氏溫度為 %d' %(C,F))
print('你輸入的溫度為 '+ str(C)+' ,華氏溫度為 '+ str(F))