'''
SELECT - get the value provided a key
SELECTALL - get all the key value pairs 
INSERT - create value with key 
INCREMENT - increase value of INT 
DECREMENT - decrease value of INT 

INSERTLIST - create value of list with key value 
UPDATELIST - update a list with key value 
APPEND - append value to list with key value 

DELETE - delete a value with key 
STATUS - see the runtime status of all commands
'''

# to store the status of the commands 
STATS = {
        'SELECT' : {'success' : 0, 'error' : 0}, 
        'SELECTALL' : {'success' : 0, 'error' : 0}, 
        'INSERT' : {'success' : 0, 'error' : 0},
        'INSERTLIST' : {'success' : 0, 'error' : 0},
        'INCREMENT' : {'success' : 0, 'error' : 0},
        'DECREMENT' : {'success' : 0, 'error' : 0},
        'APPEND' : {'success' : 0, 'error' : 0},
        'DELETE' : {'success' : 0, 'error' : 0},        
        'UPDATE' : {'success' : 0, 'error' : 0},        
        'UPDATELIST' : {'success' : 0, 'error' : 0},        
        'STATUS' : {'success' : 0, 'error' : 0},        
}

key_only_commands = ['SELECT', 'DELETE']

key_value_commands = [ 'INSERT', 'UPDATE', 'INCREMENT', 'DECREMENT', 'INSERTLIST', 'APPEND', 'UPDATELIST']

general_commands = ['STATUS', 'SELECTALL', ]

# the main database 
DATA = {}


class CommandCenter():
        ''' Util class for Pythonic NoSQL DB with Python Dictionary. '''    
        
        ''' commands for keys with non-list values (string / int) '''
        def handle_select(self, key): 
                ''' 
                Description: Handler method for retriving data from the DATA. 
                Return: Tuple - True if data found with the value, False if data not found with message. 
                '''
                
                if key not in DATA: 
                        return (False, 'ERROR: Key [{}] not found. Please provide correct key.'.format(key))
                else: 
                        return (True, {'data' : DATA[key], 'data_type' : type(DATA[key])})
                
         
        def handle_insert(self, key, value, insert_list_command=False): 
                ''' 
                Description: Handler method to create a record in database
                Return: Tuple - True with success message.  False if key already present with error message. 
                '''
                
                if key in DATA: 
                        return (
                                False, 'ERROR: Key [{}] is already present in database. You can update the data with (UPDATE;key;value;int/str) for INT/STR key or (UPDATELIST;key;value;list) to update list key'.format(key)
                        )
                        
                # enforcing to use INSERTLIST command for list type data create if the command is used INSERT 
                if isinstance(value, list): 
                        if not insert_list_command: 
                                return (False, 'ERROR: The value [{}] is a list. Did you forget to run (INSERTLIST;key;[items];list) to create a list record in database).'.format(value))
                
                # if INSERTLIST command used, enforcing to pass list data type only. 
                if insert_list_command: 
                        if not isinstance(value, list): 
                                return (False, 'ERROR: The type of the value [{}] is [{}]. Did you forget to add "LIST" datatype in INSERTLIST command.'.format(value, type(value)))
                
                DATA[key] = value 
                return (True, 'SUCCESS: Key [{}] is SET to value [{}] successfully'.format(key, value))
                
        
        def handle_update(self, key, update_value, update_list_command=False): 
                '''
                Description: Handler method to update an existing key in database with current value 
                Return: Tuple - True with success message. False with error message. 
                '''
                
                return_value = exists, value = self.handle_select(key)
                
                # key does not exist, return the error message received from the self.handle_select method 
                if not exists: 
                        return return_value 
                
                saved_value = value.get('data')
                
                if update_list_command: 
                        ''' if the saved value is not list, then prompt to give UPDATE command to update non-list value '''
                        if not isinstance(saved_value, list): 
                                return (False, 'ERROR: Key [{}] contains non-list item [{}] of which data type is [{}]. The value provided [{}] is of [{}] data type. Did you fortget to run (UPDATE;key;value;int/str) to update int/str key).'.format(key, saved_value, type(saved_value), update_value, type(update_value)))
                
                
                # if update_list_command if False, it means UPDATE command is run. 
                if not update_list_command: 
                        ''' if UPDATE command is run to update a list, Enforce to use UPDATELIST command to update list. '''
                        if isinstance(saved_value, list): 
                                return (False, 'ERROR: Key [{}] contains list item [{}] but UPDATE command is run. Did you fortget to run  (UPDATELIST;key;value;list) to update list key.'.format(key, saved_value))
                
                
                # check if saved value matches with provided value type 
                if isinstance(saved_value, int): 
                        if not isinstance(update_value, int): 
                                return (False, 'ERROR: Provided value [{}] to update for Key [key={}, which holds [{}] type value] contains non-integer value of which data type is [{}]. Did you forget to run (UPDATE;key;value;int) to update int key'.format(update_value, key, type(saved_value), type(update_value)))
                
                elif isinstance(saved_value, str): 
                        if not isinstance(update_value, str):
                                return (False, 'ERROR: Provided value [{}] to update for Key [key={}, which holds [{}] type value] contains non-str value of which data type is [{}]. Did you forget to run (UPDATE;key;value;str) to update str key'.format(update_value, key, type(saved_value), type(update_value)))
                
                elif isinstance(saved_value, list): 
                        if not isinstance(update_value, list): 
                                return (False, 'ERROR: Provided value [{}] to update for Key [key={}, which holds [{}] type value] contains non-list item of which data type is [{}]. Did you forget to run (UPDATELIST;key;value;list) to update list key'.format(update_value, key, type(saved_value), type(update_value)))
                
                
                # update the value 
                DATA[key] = update_value 
                return (True, 'SUCCESS: Key [{}] is UPDATED to value [{}] successfully. Resulting value is [{}]'.format(key, update_value, DATA[key]))
                
        
        def handle_increment(self, key, increment_value=None): 
                '''
                Description: Handler method to increment INT type value with increment_value else increment with 1  
                Return: Tuple - True with success message. False with error message. 
                '''
                
                return_value = exists, value = self.handle_select(key)
                res = 0
                
                # key does not exist, return the error message received from the self.handle_select method 
                if not exists: 
                        return return_value
                
                elif not isinstance(increment_value, int): 
                        return (False, 'ERROR: Provided value to increment for Key [{}] is non-integer [{}] and it"s  data type is [{}]. INT value can not be incremented with provided Non-INT value'.format(key, increment_value, type(increment_value)))
                
                elif not isinstance(value['data'], int): 
                        return (False, 'ERROR: Key [{}] contains non-integer value [{}] and it"s data type is [{}]. Non-INT key can not be incremented'.format(key, value['data'], type(DATA['data'])))
                
                else: 
                        if increment_value: 
                                res = DATA[key] = value['data'] + increment_value
                        else: 
                                res = DATA[key] = value['data'] + 1
                                
                                
                return (True, 'SUCCESS: Key [{}] is incremented with value [{}]. Resulting value is [{}]'.format(key, increment_value, res))
                
                
        
        def handle_decrement(self, key, decrement_value=None): 
                '''
                Description: Handler method to decrement INT type value with decrement_value else decrement with 1  
                Return: Tuple - True with success message. False with error message. 
                '''
                                
                return_value = exists, value = self.handle_select(key)
                res = 0
                
                # key does not exist, return the error message received from the self.handle_select method 
                if not exists: 
                        return return_value
                
                elif not isinstance(decrement_value, int): 
                        return (False, 'ERROR: Provided value to decrement for Key [{}] is non-integer [{}] and it"s  data type is [{}]. INT value can not be decremented with provided Non-INT value'.format(key, decrement_value, type(decrement_value)))
                
                elif not isinstance(value['data'], int): 
                        return (False, 'ERROR: Key [{}] contains non-integer value [{}] and it"s data type is [{}]. Non-INT value can not be deremented'.format(key, value['data'], type(DATA['data'])))
                
                else: 
                        if decrement_value: 
                                res = DATA[key] = value['data'] - decrement_value
                        else: 
                                res = DATA[key] = value['data'] - 1
                                
                                
                return (True, 'SUCCESS: Key [{}] is decremented with value [{}]. Resulting value is [{}]'.format(key, decrement_value, res))
                        



        ''' commands for keys with list value '''

        def handle_insertlist(self, key, value): 
                ''' 
                Description: Handler method to create a list type data
                Return: Tuple - True with success message.  False if key already present with error message. 
                '''
                print('insertlist: here  ')
                return self.handle_insert(key, value, insert_list_command=True)
        
        
        

        def handle_updatelist(self, key, value): 
                '''
                Description: Handler method to update an existing list key with current value 
                Return: Tuple - True with success message. False with error message. 
                '''

                return self.handle_update(key, value, update_list_command=True)
        
        
        
        def handle_append(self, key, append_value): 
                ''' 
                Description: Handler method to append a list in list key 
                Return: Tuple - True with success message.  False if key already present with error message. 
                '''
                
                exists, value = self.handle_select(key)
                return_value = exists, value
                
                if exists: 
                        saved_value = value['data']
                        if not isinstance(saved_value, list): 
                                return (False, 'ERROR: Key [{}] contains non-list item [{}]. To append a list, you must append in an existing list.'.format(key, saved_value))
                        
                        # ok. append the list. 
                        for item in append_value: 
                                DATA[key].append(item)
                        return (True, 'SUCCESS: Key [{}] is appended with [{}] value. Resulting value is [{}]'.format(key, append_value, DATA[key]))
                
                else: 
                        # some error occured from self.handle_select method 
                        return return_value
                        
                
        ''' general purpose commands '''
        def handle_delete(self, key): 
                ''' 
                Description: Handler method to delete an entry from the database 
                Return: Tuple - True with success message.  False if key already present with error message. 
                '''
                
                return_value = exists, value = self.handle_select(key)
                
                # key does not exist. return the error message received from the self.handl_select method. 
                if not exists: 
                        return return_value
                
                # key exists. delete the value. 
                else: 
                        value = DATA[key]
                        del DATA[key]
                        return (True, 'SUCCESS: Key [{}] is deleted with the value [{}].'.format(key, value))
        
        
        def handle_select_all(self, print_data=True): 
                ''' 
                Description: Handler method to print all the data of database. This is similart to SELECT * of SQL. 
                Return: None 
                '''
                
                if print_data: 
                        if len(DATA) == 0: 
                                print('No Data In Database!\n')
                                
                        else: 
                                for key, value in DATA.items(): 
                                        print('    KEY:    ', key, '.   ', '    VALUE:    ', value, '.    VALUE TYPE:    ', type(value))
                                print()
        
        
        def handle_update_stats(self, command, success): 
                ''' 
                Description: Handler method to update the database command status based on success or error occured. This method will be called directly. 
                Return: None 
                '''
                
                if success: 
                        STATS[command]['success'] += 1 
                else: 
                        STATS[command]['error'] += 1 
                        
        def handle_get_stats(self, print_data=False): 
                ''' 
                Description: Handler method to print the STATS dict 
                Return: None 
                '''
                
                if print_data: 
                        
                        print()
                        print('------------------------------ All Command Status ------------------------------\n')                         
                        for command, messages in STATS.items(): 
                                print('        ', command, ' - ', end='')
                                print('         Success: ', messages['success'], '          Error: ', messages['error']) 
                                print()
                        
                        print('------------------------------------ Complete ------------------------------------')       
                        print('\n')
                         
                        
                

        

def command_parser(data): 
        ''' 
        Description: Function to parse the command
        Return: Command, Key, Value from the command string
        '''
        
        try: 
                
                is_parsed = False 
                command = key = value = data_type = message = ''
                
                # getting the list of the command without the semicolon
                command_parts = data.split(';')
                
                command = command_parts[0].upper()
                
                # counting semicolons to measure the command is correct 
                semi_colon_count = 0
                for char in data: 
                        if char == ';': 
                                semi_colon_count += 1 
                
                # Enforcing exact three semicolon for appropriate command. No semicolon at the end of the command. 
                if semi_colon_count < 3 or semi_colon_count > 3:  
                        is_parsed = 'improper_semicolon'
                        message = (False, 'ERROR: You must provide three semicolon in the commnd - " ; " ')
                        return command, key, is_parsed, value, is_parsed, message
                        
                # only command and key is needed. 
                if command in key_only_commands: 
                        command, key = command_parts[:2] 
                        is_parsed = True 
                        
                elif command in key_value_commands: 
                        command, key, value, data_type = command_parts[:4]
                        
                        # make command and data type ot upper case. 
                        command = command.upper() 
                        data_type = data_type.upper()
                        
                        if data_type == 'LIST': 
                                value = value.split(',')
                                is_parsed = True 
                                
                        elif data_type == 'INT': 
                                ok = True 
                                
                                # if value is not passed, for INCREMENT or DECREMENT command, then provide default value 1. 
                                if command == 'INCREMENT' or command ==  'DECREMENT': 
                                        if value == '': 
                                                value = '1'
                                
                                # Enforce no coma separated value is provided. 
                                for char in value: 
                                        if char == ',': 
                                                ok = False
                                                is_parsed = 'int_has_coma_separated_value'
                                                message = message = (False, 'ERROR: INT has coma separated value. The data type is [{}] but the value provided is [{}] which is of type [{}] and has coma separated values. Please provide integer value for INT datatype.'.format(data_type, value, type(value))) 
                                
                                if ok: 
                                        # Enforce only digits are provided. 
                                        if not value.isdigit():  
                                                ok = False 
                                                is_parsed = 'int_has_string_value'
                                                message = (False, 'ERROR: The data type is [{}] but the value provided is [{}] which is of type [{}]. Please provide integer value for INT datatype.'.format(data_type, value, type(value))) 
                                
                                if ok: 
                                        # if no value is passed in INCREAMENT or DECREEMNT command, set the value to 1. 
                                        value = int(value)
                                        is_parsed = True 
                                        
                        elif data_type == 'STR': 
                                ok = True 
                                
                                if command == 'INCREMENT' or command == 'DECREMENT': 
                                        ok = False 
                                        is_parsed = 'str_increment_decrement'
                                        message = (False, 'ERROR: The command is [{}] but the data type is [{}]. [{}] command can not be used with [{}] data type'.format(command, data_type, command, data_type))
                                
                                if ok: 
                                        # Enforce no coma separatd value is provided. In STR data type, digits are also accepted as String value. 
                                        for char in value: 
                                                if char == ',': 
                                                        ok = False
                                                        is_parsed = False
                                if ok: 
                                        value = str(value)
                                        is_parsed = True 
                                        
                        # Invalid Data Type is provided. 
                        else: 
                                is_parsed = 'invalid_data_type'
                                message = (False, 'ERROR: The COMMAND [{}] is INVALID or the VALUE FORMAT [{}] for the DATA TYPE [{}] is INVALID. If you see empty [] list, it means you have not provided value for that portion. If you are sure data type/command is correct, then please check if correct value is passed for correct data type, and proper value format is maintained. For example - non coma seperated value for INT/STR datatype. Non-integer value for INT etc. Also check if correct command is used for certain operations.'.format(command, value, data_type))
                
                # STATS command. 
                elif command in general_commands: 
                        is_parsed = True 
                        
                # Invalid command, Invalid Command Structure, Everything Other Errors. 
                else: 
                        is_parsed = 'improper_command' 
                        message = (False, 'ERROR: Your command could not be parsed. Please provide correct command.')
                        return command, key, value, data_type, is_parsed, message
                
                # Command parsing is successful. Return the parsed values. 
                return command, key, value, data_type, is_parsed, message
                
        except Exception as e: 
                return (False, 'ERROR: Exception occurred while parsing the command - [{}]'.format(str(e)))
        
        
                

command_center = CommandCenter()

COMMAND_HANDLERS = {
        
        # INT / STR commands 
        'SELECT' : command_center.handle_select, 
        'INSERT' : command_center.handle_insert, 
        'UPDATE' : command_center.handle_update, 
        'INCREMENT' : command_center.handle_increment, 
        'DECREMENT' : command_center.handle_decrement, 
    
        # LIST commands 
        'INSERTLIST' : command_center.handle_insertlist, 
        'APPEND' : command_center.handle_append, 
        'UPDATELIST' : command_center.handle_updatelist, 
        
        # General commands 
        'SELECTALL' : command_center.handle_select_all, 
        'DELETE' : command_center.handle_delete, 
        'STATUS' : command_center.handle_get_stats, 
}




































