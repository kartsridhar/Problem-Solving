# import itertools as it
# def makeNumber(number, digits):
#     return list(filter(lambda x: sum(x) == number, it.combinations_with_replacement(range(digits,10), digits)))

# combinations = makeNumber(4, 5)
# print((combinations))







# def makeNumber(number, digits, path = []):
#     if digits == 1:                   # base case when only 1 digit to play with
#         if number not in path:        # to stop duplications
#             path += [number]          # digit must be remaining number 
#             path.sort()               # sort to stop duplicates
#             if number < 10 and path not in combinations:   # make sure number is only 1-9
#                 combinations.append(path)    # add to combinations

#     else:
#         nums = list(range(1, min(number - digits + 2, 10)))   # all possible digits 
#         nums = list(set(nums).difference(path))               # get rid of those already in path 

#         for i in nums:
#             makeNumber(number - i, digits - 1, path + [i])    # recurse


# import itertools as it
# def makeNumber2(number, digits):
#     return list(filter(lambda x: sum(x) == number, it.combinations(range(1,10), digits)))

# combinations = []
# makeNumber(15,3)
# print(combinations)
# print(makeNumber2(15,3))









# def makeNumber(number, digits, path = []):
#     if digits == 1:                   # base case when only 1 digit to play with
#         if number not in path:        # to stop duplications
#             path += [number]          # digit must be remaining number 
#             path.sort()               # sort to stop duplicates
#             if number < 10 and path not in combinations:   # make sure number is only 1-9
#                 combinations.append(path)    # add to combinations

#     else:
#         nums = list(range(1, min(number - digits + 2, 10)))   # all possible digits 
#         nums = list(set(nums).difference(path))               # get rid of those already in path 

#         for i in nums:
#             makeNumber(number - i, digits - 1, path + [i])    # recurse
