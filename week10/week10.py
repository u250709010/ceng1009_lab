# mylist = [76, 92.3, "hello", True, 4, 76]
#
# mylist.append('apple')
# mylist.append('76')
# mylist.insert(3, 'apple')
# mylist.insert(0, 99)
# print(mylist)
#
# print(mylist.index('hello'))
# print(mylist.count(76))
# mylist.remove(76)
# print(mylist)
# mylist.pop(mylist.index(True))
# print(mylist)



# def sum_of_squares(xs):
#     sum = 0
#     for x in xs:
#         sum = sum + x**2
#     return sum
#
# nums = [2, 3, 4]
# print(sum_of_squares(nums))



# def sum_even(xs):
#     total = 0
#     for x in xs:
#         if x % 2 == 0:
#             total += x
#     return total
# print(sum_even([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))



# def count_five_letter(words):
#     counter = 0
#     for word in words:
#         if len(word) == 5:
#             counter += 1
#     return counter
#
# my_list = ["hello", "world", "cat", "python", "styoblanun"]
# print(count_five_letter(my_list))



# def sum_until_even(xs):
#     total = 0
#     for x in xs:
#         if x % 2 == 0:
#             break
#         total += x
#     return total
#
# nums = [1, 3, 5, 6, 7, 8, 9, 10]
# print(sum_until_even(nums))



# def count_until_sam(words):
#     count = 0
#     for word in words:
#         count += 1
#         if word == "sam":
#             break
#     return count
#
# words = ["jsşrğptmp", "drld", "dalai", "sam", "susam"]
# print(count_until_sam(words))



# def replace(s, old, new):
#     words = s.split(old)
#     result = new.join(words)
#     return result
#
# print(replace("hello world hello", "hello", "hi"))



# def replace(s, old, new):
#     pieces = s.split(old)
#     return new.join(pieces)
#
# def test(actual, expected):
#     if actual == expected:
#         print("PASSED")
#     else:
#         print("FAİLED")
#
# test(replace("Mississippi", "i", "I"),"MIssIssIppI")


# def max(numbers):
#     biggest = numbers[0]
#
#     for number in numbers:
#         if number > biggest:
#             biggest = number
#
#     return biggest
