# 131223, Wednesday, 10.00 pm 

from utils import command_center, command_parser, key_only_commands, key_value_commands, general_commands, COMMAND_HANDLERS




print( 
''' 

        ### Welcome To Python NoSQL Dictionary Database ### 


        Command Lists.  Commands are case-insensitive. 

        Data Types - INT, STR, LIST 

        Key Only Commands: SELECT, DELETE  [Example: command;key;; ]

        Key, Value Commands: INSERT, UPDATE, INCREMENT, DECREMENT, INSERTLIST, APPEND, UPDATELIST  [Example: command;key;value;data_type]

        Non Parameter Command: STATUS (all commands runtime status) [Example: status;;;]

        Note: Put three " ; " in the command. Do not give space after seimicolon. 

        Correct Command:  insert;name;My nam is Mahboob Alam.;str 

        Incorrect Command: insert;  name;  My nam is Mahboob Alam;  str | Notice the space after semicolon. Bad Command. 

'''
        )
print('\n\n')


def main(): 
        
        while 1: 
                
                ok = False 
                stats = False 
                
                command_prompt = input('Enter valid command prompt. (To exit, press q): ')
                if command_prompt.lower() == 'q': 
                        print()
                        print('Thank You for trying the database!')
                        print()
                        break
                
                command, key, value, data_type, is_parsed = command_parser(command_prompt)
                
                command = command.upper()
                
                print()
                print('COMMAND: ', command)
                
                if is_parsed == 'improper_semicolon': 
                        is_parsed = False
                        response = (False, 'ERROR: You must provide three semicolon in the commnd - " ; " ')
                        print()
                        print('RESPONSE: ', response)
                        print()
                        
                elif is_parsed == 'improper_command': 
                        is_parsed = False
                        response = (False, 'ERROR: Your command could not be parsed. Please provide correct command. ')
                        print()
                        print('RESPONSE: ', response)
                        print()
                        print('''
Available Commads are:  SELECT, INSERT, UPDATE, DELETE, INSERTLIST, INCREMENT, DECREMENT, APPEND, UPDATELIST. 
For command documentation, see above welcome message. 
                        ''')
                
                elif not is_parsed: 
                        print()
                        print('RESPONSE: ', '(False,', 'ERROR: The COMMAND [{}] is INVALID or the VALUE FORMAT [{}] for the DATA TYPE [{}] is INVALID. If you are sure data type/command is correct, then please check if correct value is passed for correct data type, and proper value format is maintained. For example - non coma seperated value for INT/STR datatype. Non-integer value for INT etc. Also check if correct command is used for certain operations.)'.format(command, value, data_type))
                        print()
                
                
                elif command in general_commands: 
                        print()
                        command_center.handle_update_stats(command=command, success=True)
                        print()
                        COMMAND_HANDLERS[command](print_data=True)
                        print()
                
                         
                elif command in key_only_commands: 
                        response = COMMAND_HANDLERS[command](key)
                        ok = True 
                        
                elif command in key_value_commands: 
                        response = COMMAND_HANDLERS[command](key, value)
                        ok = True 
                        
                else:
                        response = (False, 'ERROR: Command [{}] is invalid.'.format(command))


                if ok: 
                        command_center.handle_update_stats(command=command, success=response[0])
                        print()
                        print('RESPONSE: ', response)
                        print()

                        


if __name__ == '__main__': 
        main()