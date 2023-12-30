def vizualize(data):
    data_to_print = ''.join([format(int(d, 16), '04b') for d in data])
    for i in range(8):
        s = ''

        for j in range(i, len(data_to_print), 8):
            s += data_to_print[j]
        print(s.replace('0', ' '))

digits = {'0': '007E8181817E0000',
          '1': '00002040FF000000',
          '2': '0061838589710000',
          '3': '00428191916E0000',
          '4': '00F80808FF080000',
          '5': '00619191918E0000',
          '6': '007E9191914E0000',
          '7': '0080808080FF0000',
          '8': '006E9191916E0000',
          '9': '00728989897E0000',
          '-': '0010101010100000',
          '+': '0010107C10100000'}


adc = int(input(), 2)
voltage = adc * 5.0 / 1023.0
tempreture = round((voltage - 0.75) / 0.010 + 25)
str_temp = '+' + str(tempreture) if tempreture > 0 else str(tempreture)
while len(str_temp) < 4:
    str_temp = "{}{}{}".format(str_temp[:1], '0', str_temp[1:])
output = ''.join([digits[d] for d in str_temp])
print(output)