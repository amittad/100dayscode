# ####### list ####### #
# Q 1
# car_name = ["bmw", "swift", "thar", "scorpied"]
# print(car_name[0:4]) # list slice
# print(car_name[-1])
# print(car_name[0:-1])
# car_name[1:2]= "bullet"
# print(car_name)

# =========  output   =========================================
# ['bmw', 'swift', 'thar', 'scorpied']
# scorpied
# ['bmw', 'swift', 'thar']
# ['bmw', 'b', 'u', 'l', 'l', 'e', 't', 'thar', 'scorpied']
# =================================================================
#



# # Q 2 slicing
# car_name = ["bmw", "swift", "thar", "scorpied"]
# car_name[1:3] = "bullet"
# print(car_name) # output is  ['bmw', 'b', 'u', 'l', 'l', 'e', 't', 'scorpied']
# car_name[1:7] = ["fortuner"]
# print(car_name) # output is    ['bmw', 'fortuner', 'scorpied']
#
# car_name[1:1]=["thar", "mahindra"]
# print(car_name) # output ['bmw', 'thar', 'mahindra', 'fortuner', 'scorpied']
#




# Q 3

# car_name = ["bmw", "swift", "thar", "scorpied"]
#
# for car in car_name:
#     print(car, end="_") # output  bmw_swift_thar_scorpied_


# Q4 insert && pop && remove

# car_name = ["bmw", "swift", "thar", "scorpied"]
# car_name.insert(2,"bailgadi")
# print(car_name) # output ['bmw', 'swift', 'bailgadi', 'thar', 'scorpied'] # insert element in list
# car_name.pop()
# print(car_name) # output ['bmw', 'swift', 'bailgadi', 'thar']   # last element is pop
# car_name.remove("bailgadi")
# print(car_name) # output  ['bmw', 'swift', 'thar'] # remove bailgadi from list


# Q5
# square_num =[c**2 for c in range(21)]
# print(square_num) # output [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400]

# Q 6
# cube_num =[x**3 for x in range(11)]
# print(cube_num) # output is [0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]