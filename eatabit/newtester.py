# def pentagonal(num):
#     if num == 1:
#         return 1
#     else:
#         return pentagonal(num - 1) + (5*(num-1))
    


# lst = [1,2,3,4]
# print(sum(lst))

# def series_resistance(lst):
# 	a = sum(lst)
# 	if a > 1:
# 		return f'{a} ohms'
# 	else:
# 		return f'{a} ohm'

# print(series_resistance(lst))


# def consecutive_combo(lst1, lst2):
# 	b = sorted(list(set((lst1+lst2))))
# 	print(b)
# 	return True if sum(b[ind+1] - i for ind,i in enumerate(b) if ind+1 != len(b)) == len(b)-1 else False

# # print(consecutive_combo([1,2,3],[4,6,5]))
# print(consecutive_combo([33, 34, 40], [39, 38, 37, 36, 35, 32, 31, 30]))
# 	# print(sum(b[ind+1] - i for ind,i in enumerate(b) if ind+1 != len(b)))
