import sys
import os
from doc_word_count import *
#we don need merging the dicts right now, since we are not concerned 
#about the word count of all words universally, we just need a universal
#list of words, which we can do by using fromkeys, or instead we can just
#use a list
#from merge_dict_keys import *
from print_dict import *

if __name__ == '__main__':
    if len(sys.argv) > 1:
        file_wc_map = {}
        for txt_file in os.listdir(sys.argv[1]):
            txt_file = os.path.join(sys.argv[1], txt_file)
            if os.path.isfile(txt_file) and txt_file.endswith(".txt"):
                file_wc_map[txt_file] = count_words(txt_file)
            else:
                print txt_file, " : File is not a valid text file"
        #now let us try to build a dict of all words
        #I am using a dict with update and fromkeys since this 
        #does not require extra effort to eliminate word recurrences
        all_words  = {}
        for key in file_wc_map.keys():
            print key 
            print_d(file_wc_map[key],1)
            all_words.update(all_words.fromkeys(file_wc_map[key],0))

        print all_words.keys()

        #once we have the list of all words, we have to fill zeros for the 
        #individual file Word Counts whenever a word is not present at all
        #this will bring the word count vectors to equal sizes and order
        for word in sorted(all_words.keys()):
            for txt_file in file_wc_map.keys():
                file_wc_map[txt_file][word] = file_wc_map[txt_file].get(word,0)

        #lets print the list of words in sorted order
        print "[ ",
        for word in sorted(all_words.keys()):
            print word,
        print " ]"
        #lets print the final equal sized Word Count vectors
        # we will print them to a file if the '-f' option is specified.
        if "-f" in sys.argv:
            if len(sys.argv)<= sys.argv.index("-f")+1:
                print "Please give the file name to write to"
                sys.exit(0)
            else:
                output_file = file(sys.argv[sys.argv.index("-f")+1],"w")
            for key in file_wc_map.keys():
                print >>output_file, key
                print_d(file_wc_map[key],1, output_file )
        else:
            for key in file_wc_map.keys():
                print key 
                print_d(file_wc_map[key],1)


    else:
        print "Please give the path where the text files are present"
        sys.exit(0)






