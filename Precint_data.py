import csv
f = open('book2.csv')
csv_f = csv.reader(f)
#for row in csv_f:
    #print(row)

#print(csv_f)

#for i in range(1160116112, 7253401029):



count_dict = {}
my_dict = {}





def check_col_1(row):
    ''' Checks the first column in a given row of data and adds 
        the corresponding data to a dicitonary.
    '''
    
    if row[0] == 'Precinct': # A specific exception I made.
        pass
    else:
        if row[0] == '':  #making sure we dont waste time on empty data cells
            pass

        else:
            if row[0] not in my_dict and row[1] != '':  #if the data in this cell is not yet a key in our dict, create it.
                my_dict[row[0]] = int(row[1])

            elif row[0] in my_dict and row[1] != '':  #if the data in this cell is already in the dict, then add this value to the existing key
                my_dict[row[0]] += int(row[1])

            else:  # if these conditions are not met, I do not want the data in my_dict.
                pass

def check_col_2(row):
    if row[3] == 'Precinct':
        pass
    else:    
        if row[3] == '':
            pass
        else:
            if row[3] not in my_dict and row[4] != '':
                my_dict[row[3]] = int(row[4])
            elif row[3] in my_dict and row[4] != '':
                my_dict[row[3]] += int(row[4])
            else:
                pass

def check_col_3(row):
    if row[3] == 'Precinct':
        pass
    else:
        if row[6] == '':
            pass
        else:
            if row[6] not in my_dict and row[7] != '':
                my_dict[row[6]] = int(row[7])
            elif row[6] in my_dict and row[7] != '':
                my_dict[row[6]] += int(row[7])
            else:
                pass


def count_col_1(row):
    if row[0] not in count_dict:
        count_dict[row[0]] = 1
    else:
        count_dict[row[0]] += 1
def count_col_2(row):
    if row[3] not in count_dict:
        count_dict[row[3]] = 1
    else:
        count_dict[row[3]] += 1
def count_col_3(row):
    if row[6] not in count_dict:
        count_dict[row[6]] = 1
    else:
        count_dict[row[6]] += 1




def build_my_dict():
    #print("where'd you get this code, the toilet store?")
    for row in csv_f:
        #print("checking...")
        check_col_1(row)
        #print("checking...")
        check_col_2(row)
        #print("checking...")
        check_col_3(row)
    

def build_count_dict():
    
    for row in csv_f:
        #print("counting!!!")
        count_col_1(row)
        #print("counting!!!")
        count_col_2(row)
        #print("counting!!!")
        count_col_3(row)
    
    

#def average_turnout():
    #build_my_dict()
    #build_count_dict()


build_count_dict()
f.seek(0)   
build_my_dict()




    



avg_dict = {}

for k, v in my_dict.items():
    count = count_dict[k]
    avg_dict[k] = (v / count)
    #print("v: " + str(v))
    #print("count: " + str(count_dict[k]))
    #print(v/count_dict[k])





#print(count_dict)
print(my_dict)
#print(avg_dict)
