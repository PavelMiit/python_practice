#Реализуйте функцию is_leap_year(), которая определяет, является ли год високосным. 
#Год будет високосным, если он делится без остатка на 400, или он одновременно делится без 
#остатка на 4 и не делится на 100
def  is_leap_year(year):
    return  year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)
print(is_leap_year(2016))


#Реализуйте функцию string_or_not(), которая проверяет является ли переданный параметр строкой. 
#Если да, то возвращается строка yes, иначе no.
def  string_or_not(string):
    result_1 = isinstance(string, str)
    return result_1 == True and 'yes' or 'no'
    
    
#Реализуйте функцию normalize_url(), которая выполняет так называемую нормализацию данных. 
#Она принимает адрес сайта и возвращает его с https:// в начале.
#Функция принимает адреса в виде:
#АДРЕС
#http://АДРЕС
#https://АДРЕС (нормализованный)
#Функция всегда возвращает адрес в виде https://АДРЕС.
def normalize_url(adress):
    if adress[:8] == 'https://':
     return(adress)

    elif adress[:7] == 'http://':
      return 'https://' + adress[7:]
      
    else:
      return('https://' + adress)

