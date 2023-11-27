# a = int(input('введите число: '))
# factorial = 1
# for a in range(2, a+1):
#     factorial *= a
# print(factorial)



# def func():
#     yield 1
#     yield 2
#     yield 3
#
# s = func()
# print(s)
# print(next(s))



# lst = [(1, 2), (3, 4)]
# # print({
# #     nums[0]: nums[1]
# #     for nums in lst
# # })




text = ('''Всем привет как дела тра та та''')
pure_text = text.lower().replace('', '')
letters = {
for letter in set(pure_text)
}
uniq_letters = set(pure_text)
letters = {}
for letter in uniq_letters:
    print(letter)
    letters[letter] = pure_text.count(letter)
print(letters)

