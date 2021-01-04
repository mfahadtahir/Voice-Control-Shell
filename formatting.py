import math
#This file contains functions needed for formatting

#this function add the break line
def line(size = 77):
    print(''.ljust(size, '='))
    return

#this function will enclose the text in a box
def text_box(mytext, size = 77):
    start = 0
    end = size - 4
    no_of_lines = math.ceil(len(mytext)/end)
    line(size)
    for i in range(no_of_lines):
        print('| ' + mytext[start:end].ljust(size - 4, ' ') + ' |')
        start = start + end
        end = end + end
    line(size)
    return

#this function will add the heading
def head(mytext, size = 77):
    line(size)
    print('|' + mytext.center(size - 2, ' ') + '|')
    line(size)
    return

#this function will add the heading of a table
def table_head(left_text, right_text, left_size = 20, right_size = 50):
    size = left_size + right_size + 7
    line(size)
    print('| ' + left_text.center(left_size, ' ') + ' | ' + right_text.center(right_size, ' ') + ' |')
    line(size)
    return

#this function will add the contents of the table
def table_content(left_text, right_text, left_size = 20, right_size = 50):
    size = left_size + right_size + 7
    print('| ' + left_text.ljust(left_size, ' ') + ' | ' + right_text.ljust(right_size, ' ') + ' |')
    line(size)
    return
