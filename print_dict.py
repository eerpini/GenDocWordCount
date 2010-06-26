import sys 

def print_d(dict, asarray=0, file_handle=sys.stdout):
    """print the key value pairs in the dictionary in a neat way
    pass the second argument as 1 in case you want the values in the 
dictionary to be printed in a array like vector fashion. And pass the file
handle of the file if you want the function to print to a file"""
    if asarray ==1 :
        print >>file_handle, "[ ",
        for value in sorted(dict.keys()):
            print >>file_handle, "%d " % dict[value],
        print >>file_handle, " ]"
    else:
        for value in sorted(dict.keys()):
            print >>file_handle, " %10s   :   %3d" % (value, dict[value])
