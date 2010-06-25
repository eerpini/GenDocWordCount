def print_d(dict, asarray=0):
    """print the key value pairs in the dictionary in a neat way
    pass the second argument as 1 in case you want the values in the 
dictionary to be printed in a array like vector fashion."""
    if asarray ==1 :
        print "[ ",
        for value in sorted(dict.keys()):
            print "%d " % dict[value],
        print " ]"
    else:
        for value in sorted(dict.keys()):
            print " %10s   :   %3d" % (value, dict[value])
