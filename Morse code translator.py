_MORSE_CODE_DICT = { 'A':'.-','B':'-...','C':'-.-.','D':'-..',
'E':'.','F':'..-.','G':'--.','H':'....','I':'..',
'J':'.---','K':'-.-','L':'.-..','M':'--',
'N':'-.','O':'---','P':'.--.','Q':'--.-',
'R':'.-.','S':'...','T':'-','U':'..-',
'V':'...-','W':'.--','X':'-..-','Y':'-.--','Z':'--..',' ':'   ' }


def _menu():
    print('***********WELCOME TO WORLD OF MORSE CODE***********')
    print('Select an option:')
    print('(1)English to MORSE CODE\n(2)Quit')
    menu = int(input('Select (1,2):  '))

    while menu>2:
        print('Invalid option')
        menu = int(input('Select (1,2):  '))


    if menu == 1:
        _english_to_morse_code()

    else:
        input('Press ENTER to quit')
        quit()

            
            
    
def _english_to_morse_code():
    print()
    print('English to morse code translatar')
    print()
    global message
    message = input('Write your message: ')
    message = message.upper()
    _translate_message()

def _translate_message():
    print(message)
    translate = ''
    
    for letter in message:
        if letter != '':
            translate += _MORSE_CODE_DICT[letter] + ''
        else:
            translate += ''

    print(translate)
    backtomenu()
    return translate
    


def backtomenu():
    print()
    print()
    print('Thank you for using Morse Code translatar')
    print()
    print('1) TRANSLATE ANOTHER TEXT\n2)QUIT')
    option_=int(input('Select option(1~2): '))
    if option_ == 1:
        _english_to_morse_code()        
    elif option_ == 2:
        input('Press ENTER to Quit')
        quit()
    else:
        while option_ != 1 and option_ != 2:
            print('Invalid option')
            option_=int(input('Select option(1~2): '))
            
        
        

    
    

    



_menu()
message= input()
    
