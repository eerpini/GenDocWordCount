def multiple_sep_split(string,maxsplit, spacealso,args):
    """Call the function as multiple_sep_split(<string to be split>,<the max number of splits, 0 if there is no limit>,<if space is also included as a separator, 1 for yes>,<a tuple/list of separators>)"""
    return_list = []
    final_list = []
    args_list = []
    args_list.extend(args)
    #first we do a split with ' '
    if(spacealso == 1):
        args_list.append(args_list[0])
        args_list[0]=' '
    if maxsplit > 0:
        prev_split=0
        split_count=0
        for i in range(len(string)):
            if string[i] in args_list:
                return_list.append(string[prev_split:i])
                prev_split=i+1
                split_count = split_count+1
            if split_count == maxsplit: 
                    break
        if prev_split != len(string):
            return_list.append(string[prev_split:])
    else:
        prev_split=0
        for i in range(len(string)):
            if string[i] in args_list:
                return_list.append(string[prev_split:i])
                prev_split=i+1
        if prev_split != len(string):
            return_list.append(string[prev_split:])
    #removing blank members, I do not know how to do this more elegantly 
    for val in return_list:
        if val != '':
            final_list.append(val)

    return final_list


def count_words(path):
    separators = (',','.',':',';','/','\\','(',')','{','}','<','>','?','"','\'','\n','\t')
    fileh = file(path)
    words = multiple_sep_split(fileh.read(), -1, 1, separators)
    word_count_dict={}
    #print words
    for value in words:
        word_count_dict[value] = word_count_dict.get(value, 0)+1
    return word_count_dict

