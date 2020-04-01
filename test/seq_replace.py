# 1.
string = 'TCTCGAAG'
str_ = ''
for i in string:
    if i == 'A':
        str_ = str_ + 'T'
    elif i =='T':
        str_ = str_ + 'A'
    elif i == 'C':
        str_ = str_ + 'G'
    elif i == 'G':
        str_ = str_ + 'C'
print(f'旧字符串：{string}\n新字符串：{str_}')

print('----------')

# 2.
string = 'TCTCGAAG'
str_ = ['ATCG'['TAGC'.index(i)] for i in string]
print('TAGC'.index('T'))
print(str_)
print(f'旧字符串：{string}\n新字符串：'+''.join(str_))

print('----------')

# 3.
print(''.join(['ATCG'['TAGC'.index(i)] for i in 'TCTCGAAG']))
