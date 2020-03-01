def str_split(x):
    if(len(x)>0):
        new_lst=[]
        for i in x:
            new_lst=new_lst+i
        return new_lst
m=lambda x:x.split(' ')
words_starting_with_a = lambda x:x[0]=='a' or x[0]=='A'
lst=['Rather than having all of its functionality built into its core, Python was designed to be highly extensible. This compact modularity has made it particularly popular as a means of adding programmable interfaces to existing applications. Van Rossums vision of a small core language with a large standard library and easily extensible interpreter stemmed from his frustrations with ABC, which espoused the opposite approach.[31] While offering choice in coding methodology, the Python philosophy rejects exuberant syntax (such as that of Perl) in favor of a simpler, less-cluttered grammar. As Alex Martelli put it: "To describe something as clever is not considered a compliment in the Python culture.[50] Pythons philosophy rejects the Perl there is more than one way to do it approach to language design in favor of there should be one—and preferably only one—obvious way to do it.[49] Pythons developers strive to avoid premature optimization, and reject patches to non-critical parts of the CPython reference implementation that would offer marginal increases in speed at the cost of clarity.[51] When speed is important, a Python programmer can move time-critical functions to extension modules written in languages such as C, or use PyPy, a just-in-time compiler. Cython is also available, which translates a Python script into C and makes direct C-level API calls into the Python interpreter.']
print('Original String:',lst)
l=str_split(list(map(m,lst)))
words_with_A=list(filter(words_starting_with_a,l))
print('\n\n\n\n\n')
print('Words starting with a//A in the new list of strings are:\n',str_to_lst(words_with_A))




