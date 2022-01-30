list = []
def entry():
    if var == 'search':
        get_element(input('searched item: '))
    if var == 'add':
        add_element(input('Entry name: '))
    if var == 'remove':
        rmv_element(input('Entry name: '))
    if var == 'print':
        print_elements()
    if var == 'sort':
        srt_elements(input('How should the list be sorted ? '))
    if var == 'exit':
        exit()
def get_element(ele):
    pos = 0
    all = 0
    fou = False
    for element in range(len(list)):
        if list[pos] == ele:
            all = all+1
            fou = True
            print('found position: '+ str(pos))
        pos = pos+1
    if fou == False:
        print('\033[0;31;40mItem not found\033[0;0m')
    else:
        if all == 1:
           all = str(all)
           print('There was a total of '+ all +' entry' )
        else:
           all = str(all)
           print('There was a total of '+ all +' entries' )
def add_element(name):
    list.append(name)
    print('\033[0;32;40mOk ' + name +' was added \033[0;0m')
def rmv_element(name):
    pos = 0
    fou = False
    for element in range(len(list)):
        if list[pos] == name:
            fou = True
        pos = pos+1
    if fou == False:
        print('\033[0;31;40mItem not found\033[0;0m')
    else:
        list.remove(name)
        print('\033[0;32;40mOk ' + name +' was removed \033[0;0m')
def print_elements():
    print(list)
def exit():
    print('ok, goodbye')
def srt_elements(style):
    if style == 'a-z':
        list.sort()
    if style == 'z-a':
        list.sort(reverse=True)
    print('\033[0;32;40mThe list has been sorted from  '+ style + ' \033[0;0m')
var = (input('''Hello
What would you like to do ? '''))
entry()
while var != 'exit':
    var = (input('What would you like to do ? '))
    entry()
