def X ():
    total_price = int(input('合計金額を教えてね(円):'))
    number_of_people = int(input('人数を教えてね(人): '))

# print(total_price)
# print(number_of_people)

    ans = total_price // number_of_people
    remainder = total_price % number_of_people

    print('1人あたり:' + str(ans) + '円' + ', 端数:' + str(remainder) + '円')

X ()