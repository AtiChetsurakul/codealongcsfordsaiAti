test = [
  [0, 1, 0, 0],
  [0, 0, 1, 0],
  [0, 1, 0, 1],
  [1, 1, 0, 0]
]
ret = [
    [11, 9, 11, 11], 
    [11, 3, 9, 11], 
    [11, 9, 4, 9], 
    [9, 9, 11, 11]
    ]
def get_mine_data(map):
    ltr = []
    for index_i, i in enumerate(map):
        innerltr = []
        for index_j, j in enumerate(i):

            if j == 1:
                innerltr.append(9)

            else:
                if index_i - 1 >= 0 and index_i + 1 != len(map):
                    if index_j - 1 >= 0 and index_j + 1 != len(map):
                        tapd = 0
                        for testi in range(index_i-1,index_i+2):
                            for testj in range(index_j-1,index_j+2):
                                if map[testi][testj] == 1:
                                    tapd += 1
                        innerltr.append(tapd)

                    elif index_j - 1 >= 0:
                        tapd = 0
                        for testi in range(index_i-1,index_i+2):
                            for testj in range(index_j-1,index_j+1):
                                if map[testi][testj]:
                                    tapd += 1
                        innerltr.append(tapd)

                    elif index_j + 1 != len(map):
                        tapd = 0
                        for testi in range(index_i-1,index_i+2):
                            for testj in range(index_j,index_j+2):
                                if map[testi][testj]:
                                    tapd += 1
                        innerltr.append(tapd)  

                    else: 
                        innerltr.append(11)
                        #TODO
                elif index_i - 1 >= 0:
                    if index_j - 1 >= 0 and index_j + 1 != len(map):
                        tapd = 0
                        for testi in range(index_i-1,index_i+1):
                            for testj in range(index_j-1,index_j+2):
                                if map[testi][testj] == 1:
                                    tapd += 1
                        innerltr.append(tapd)

                    elif index_j - 1 >= 0:
                        tapd = 0
                        for testi in range(index_i-1,index_i+1):
                            for testj in range(index_j-1,index_j+1):
                                if map[testi][testj]:
                                    tapd += 1
                        innerltr.append(tapd)

                    elif index_j + 1 != len(map):
                        tapd = 0
                        for testi in range(index_i-1,index_i+1):
                            for testj in range(index_j,index_j+2):
                                if map[testi][testj]:
                                    tapd += 1
                        innerltr.append(tapd)


                elif index_i + 1 != len(map):
                    if index_j - 1 >= 0 and index_j + 1 != len(map):
                        tapd = 0
                        for testi in range(index_i,index_i+2):
                            for testj in range(index_j-1,index_j+2):
                                if map[testi][testj] == 1:
                                    tapd += 1
                        innerltr.append(tapd)

                    elif index_j - 1 >= 0:
                        tapd = 0
                        for testi in range(index_i,index_i+2):
                            for testj in range(index_j-1,index_j+1):
                                if map[testi][testj]:
                                    tapd += 1
                        innerltr.append(tapd)

                    elif index_j + 1 != len(map):
                        tapd = 0
                        for testi in range(index_i,index_i+2):
                            for testj in range(index_j,index_j+2):
                                if map[testi][testj]:
                                    tapd += 1
                        innerltr.append(tapd)                         

                else:
                    innerltr.append(11)
                    #TODO

        ltr.append(innerltr)
    return(ltr)


import numpy as np
                    

print(np.array(get_mine_data(test)))







test = [
  [1, 0, 0, 0],
  [0, 1, 0, 0],
  [1, 0, 0, 0],
  [0, 0, 0, 1]
]

def get_index_data(map):
    for index_i, i in enumerate(map):
        for index_j, j in enumerate(i):
            if j == 1:
                print(f'{index_i}:{index_j}')
            

# get_index_data(test)

# x = [ (index_i,index_j) for index_i,i in enumerate(test) for index_j,j in enumerate(i) if j == 1]
# print([ (index_i,index_j) for index_i,i in enumerate([[1, 0, 0, 0],[0, 1, 0, 0],[1, 0, 0, 0],[0, 0, 0, 1]]) for index_j,j in enumerate(i) if j == 1])
