def mutate_string(string, position, character):
    mylist=list(string)
    mylist[position]=character
    mylist = ''.join(mylist)
    return mylist

