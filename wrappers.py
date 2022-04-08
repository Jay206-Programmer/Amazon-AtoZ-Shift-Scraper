def operation(func):
    '''
        Implements Exception Handling on the Operations
        that returns nothing.
        
        Returns:
        -------
        `1` if Function Fails else `0`
    '''
    def wrapper(*args, **kwargs):
        try:
            func(*args, **kwargs)
            return 0
        except Exception as exc:
            print("Exception:",str(exc))
            return 1
    return wrapper