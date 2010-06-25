def print_d(dict, asarray=0):
    if asarray ==1 :
        print "[ ",
        for value in sorted(dict.keys()):
            print "%d " % dict[value],
        print " ]"
    else:
        for value in sorted(dict.keys()):
            print " %10s   :   %3d" % (value, dict[value])
