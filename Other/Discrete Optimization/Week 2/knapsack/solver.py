#!/usr/bin/python
# -*- coding: utf-8 -*-

from collections import namedtuple
Item = namedtuple("Item", ['index', 'value', 'weight'])

def solve_it(input_data):
    # Modify this code to run your optimization algorithm

    # parse the input
    lines = input_data.split('\n') 

    firstLine = lines[0].split() 
    num_items = int(firstLine[0]) 
    capacity = int(firstLine[1]) 

    items = range(num_items)
    selected = [0] * num_items 

    all_lines = list()
    for i in range(1,num_items+1):
        all_lines.append([float(lines[i].split()[0]),
                          float(lines[i].split()[1]),
                          float(lines[i].split()[0])/float(lines[i].split()[1]),
                          i
                         ]
                        )
                        
    all_lines.sort(key= lambda items: (items[2],items[0]), reverse  = True)
#    all_lines.sort(key = lambda items: (items[1]), reverse = False)
    weight = 0
    value = 0
    placeholder = 0
    while capacity > 0 :
        if (all_lines[placeholder][1]) <= capacity:
            selected[all_lines[placeholder][3]-1] = 1
            weight += all_lines[placeholder][1]
            value += all_lines[placeholder][0]
            capacity -= all_lines[placeholder][1]
        
        placeholder += 1
        
        if placeholder > (num_items - 1):
            break
       
    # prepare the solution in the specified output format
    output_data = str(int(value)) + ' ' + str(0) + '\n'
    output_data += ' '.join(map(str, selected))
    return output_data
    
if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        file_location = sys.argv[1].strip()
        with open(file_location, 'r') as input_data_file:
            input_data = input_data_file.read()
        print(solve_it(input_data))
    else:
        print('This test requires an input file.  Please select one from the data directory. (i.e. python solver.py ./data/ks_4_0)')



