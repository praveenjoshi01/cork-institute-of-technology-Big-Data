# --------------------------------------------------------
#           PYTHON PROGRAM
# Here is where we are going to define our set of...
# - Imports
# - Global Variables
# - Functions
# ...to achieve the functionality required.
# When executing > python 'this_file'.py in a terminal,
# the Python interpreter will load our program,
# but it will execute nothing yet.
# --------------------------------------------------------

import codecs

# ------------------------------------------
# FUNCTION my_map
# ------------------------------------------
def my_map(funct, my_list):
    # 1. We create the output variable
    res = []

    # 2. We populate the list with the higher application
    for item in my_list:
        sol = funct(item)
        res.append(sol)

    # 3. We return res
    return res

# ------------------------------------------
# FUNCTION my_city
# ------------------------------------------
def my_city(x, value):
    resB =False
    # 1. If city == value
    if (x[0] == value):
        resB = True

    # 2. We return res
    return resB

# ------------------------------------------
# FUNCTION my_acc
# ------------------------------------------
def my_acc(res, item, value):

    # 1. If city == value
    if (item[0] == value):
        res = res+1

    # 2. We return res
    return res

# ------------------------------------------
# FUNCTION my_filter
# ------------------------------------------
def my_filter(funct, my_list):
    # 1. We create the output variable
    res = []

    # 2. We populate the list with the higher application
    for item in my_list:
        # 2.1. If an item satisfies the function, then it passes the filter
        if funct(item) == True:
            res.append(item)

    # 3. We return res
    return res

# ------------------------------------------
# FUNCTION my_fold
# ------------------------------------------
def my_fold(funct, accum, my_list):
    # 1. We create the output variable
    res = accum

    # 2. We populate the list with the higher application
    for item in my_list:
        res = funct(res, item)

    # 3. We return res
    return res

# ------------------------------------------
# FUNCTION my_file_reading
# ------------------------------------------
def my_file_reading(i_file_name):
    # 1. We create the output variable
    res = []

    # 2. We open the dataset file to read from it
    my_input_file = codecs.open(i_file_name, "r", encoding='utf-8')

    # 3. We parse the content of the file
    for line in my_input_file:
        # 3.1. We append the content to file_content
        res.append(line)

    # 4. We close the file
    my_input_file.close()

    # 5. We return res
    return res

# ------------------------------------------
# FUNCTION process_line
# ------------------------------------------
def process_line(line, coordinates):
    # We want it to return a list of elements with the following format:
    # res = (point_id, level, day, hour)
    #        integer, float, String, String)

    line = line.rstrip('\n')
    line = line.split("\t")

    dateTime = line[1].split("T")
    level = line[2]
    co_ord = (line[3],line[4])

    city= 2

    if co_ord[0] == str(coordinates[0][0])  :
        city =1

    # print(city,level,dateTime[0],dateTime[1])
    return(city,level,dateTime[0],dateTime[1])

# ------------------------------------------
# FUNCTION block1
# ------------------------------------------
def block1(dataset_dir, coordinates):
    # 1. We load the dataset into a list
    inputLIST = my_file_reading(dataset_dir)

    # 2. We count the number of measurements
    res = len(inputLIST)

    # 3. We print by the screen the result computed in resVAL
    print(res)

# ------------------------------------------
# FUNCTION block2
# ------------------------------------------
def block2(dataset_dir, coordinates):
    # 1. We load the dataset into a list
    inputLIST = my_file_reading(dataset_dir)

    # 2. We process each line
    # We call to my_map with process_line to find the information we want per item.
    resTuple = my_map(lambda x : process_line(x,coordinates), inputLIST)

    # print(type(res))
    # 3. We filter the measurements belonging to each point
    # We call to my_filter twice, first to filter the ones with point 1 and then the ones with point 2.
    file1_res = my_filter( lambda item : my_city(item, 1), resTuple)
    file2_res = my_filter( lambda item : my_city(item, 2), resTuple)

    # 4. We count the number of measurements per point
    count1_res =len(file1_res)
    count2_res = len(file2_res)

    # 5. We print by the screen the result computed in resVAL
    print(count1_res)
    print(count2_res)

# ------------------------------------------
# FUNCTION block3
# ------------------------------------------
def block3(dataset_dir, coordinates):
    # 1. We load the dataset into a list
    inputLIST = my_file_reading(dataset_dir)

    # 2. We process each line
    # We call to my_map with process_line to find the information we want per item.
    resTuple = my_map(lambda x : process_line(x,coordinates), inputLIST)

    # 3. Operation A1: We count the measurements per point with fold
    # We call to my_fold to accumulate the results.
    resTupleForCity1 = my_fold( lambda accum, item : my_acc(accum, item, 1), 0, resTuple)
    resTupleForCity2 = my_fold( lambda accum, item : my_acc(accum, item, 2), 0, resTuple)
    
    # 4. We print by the screen the collection computed in resVAL
    print('City 1: ',resTupleForCity1)
    print('City 2: ',resTupleForCity2)
# ------------------------------------------
# FUNCTION my_main
# ------------------------------------------
def my_main(dataset_dir, coordinates):
    print("Total number of measurements")
    block1(dataset_dir, coordinates)

    print("Total number of measurements per point")
    block2(dataset_dir, coordinates)

    print("Total number of measurements per point with fold")
    block3(dataset_dir, coordinates)

# ---------------------------------------------------------------
#           PYTHON EXECUTION
# This is the main entry point to the execution of our program.
# It provides a call to the 'main function' defined in our
# Python program, making the Python interpreter to trigger
# its execution.
# ---------------------------------------------------------------
if __name__ == '__main__':
    # 1. We provide the path to the input folder  and output folder
    dataset_file = "../my_dataset/river_lee_levels.txt"

    # 2. We add any extra variable we want to use
    coordinates = [(51.897843, -8.56668), (51.894643, -8.512962)]

    # 3. We call to our main function
    my_main(dataset_file, coordinates)