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
                
                command_prompt = input('Enter valid command prompt. (To exit, press q): ')
                if command_prompt.lower() == 'q': 
                        print()
                        print('Thank You for trying the database!')
                        print()
                        break
                
                # MESSAGES ONLY CONTAINS BELOW ERROR MESSAGES.  
                command, key, value, data_type, is_parsed, message = command_parser(command_prompt)
                command = command.upper()
                
                print()
                print('COMMAND: ', command,'.', 'KEY: ', key,'.',  'VALUE: ', value,'.', 'DATA TYPE: ', data_type,'.')
                
                if is_parsed == 'improper_semicolon': 
                        is_parsed = False
                        print()
                        print('RESPONSE: ', message)
                        print()
                        
                elif is_parsed == 'improper_command': 
                        is_parsed = False
                        print()
                        print('RESPONSE: ', message)
                        print()
                        print('''
Available Commands are:  SELECT, INSERT, UPDATE, DELETE, INSERTLIST, INCREMENT, DECREMENT, APPEND, UPDATELIST. 
For command documentation, see above welcome message. 
                        ''')
                
                elif is_parsed == 'invalid_data_type': 
                        is_parsed = False
                        print()
                        print('RESPONSE: ', message)
                        print()
                        
                elif is_parsed == 'str_increment_decrement': 
                        # if data type is STR and command is INCREMENT or DECREMENT. 
                        is_parsed = False 
                        print()
                        print('RESPONSE: ', message)
                        print()
                        
                elif is_parsed == 'int_has_string_value': 
                        is_parsed = False 
                        print()
                        print('RESPONSE: ', message)
                        print()
                
                elif is_parsed == 'int_has_coma_separated_value': 
                        is_parsed = False 
                        print()
                        print('RESPONSE: ', message)
                        print()
                
                # COMMAND CENTER | SHOWS SUCCESS OR ERROR OF COMMANDS. 
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