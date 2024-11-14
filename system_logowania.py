import functools
import os

class Logger:
    def log_info(self, message):
        raise NotImplemented

    def log_debug(self, message):
        raise NotImplemented

    def log_error(self, message):
        raise NotImplemented



class ConsoleLogger(Logger):
    def log_info(self, message):
        print(f'[INFO] - {message}')

    def log_debug(self, message):
        print(f'[DEBUG] - {message}')

    def log_error(self, message):
        print(f'[ERROR] - {message}')



class FileLogger(Logger):
    def __init__(self, filename):
        self.filename = filename   
        if not os.path.exists(filename):
            with open(filename, 'w'): pass
    
    def log_info(self, message):
        with open(self.filename, 'a') as file:
            file.write(f'[INFO] - {message}')

    def log_debug(self, message):
        with open(self.filename, 'a') as file:
            file.write(f'[DEBUG] - {message}')

    def log_error(self, message):
        with open(self.filename, 'a') as file:
            file.write(f'[ERROR] - {message}')




def log_operation_console(level):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(self, *args, **kwargs):
            logger = ConsoleLogger()
            if level == 'INFO':
                logger.log_info(f'Calling {func.__name__} with args {args} and kwargs {kwargs}')
            elif level == 'DEBUG':
                logger.log_debug(f'Calling {func.__name__} with args {args} and kwargs {kwargs}')
            elif level == 'Error':
                logger.log_error(f'Calling {func.__name__} with args {args} and kwargs {kwargs}')
            return func(self, *args, **kwargs)     
        return wrapper
    return decorator    


class User:
    def __init__(self, name):
        self.name = name
    
    @log_operation_console('INFO')
    def login(self):
        print(f'{self.name} has logged in')
    
    log_operation_console('Error')
    def logout(self):
        print(f'{self.name} has logged out')

user = User('Josh')
user.login()