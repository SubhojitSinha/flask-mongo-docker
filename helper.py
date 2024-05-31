import traceback

# def handle_errors(cls):
#     """
#     Class decorator to handle all errors in a class.
#     """
#     def wrap_methods(method):
#         """
#         Decorator function to wrap each method in the class with error handling.
#         """
#         def wrapped(*args, **kwargs):
#             try:
#                 return {
#                     'status' : True,
#                     'message': "Success",
#                     'data'   : method(*args, **kwargs)
#                 }
#             except Exception as e:
#                 return {
#                     'status' : False,
#                     'message': f"Error in {cls.__name__}.{method.__name__}: {e}",
#                     'data'   : traceback.format_exc()
#                 }
#         return wrapped

#     for name, method in vars(cls).items():
#         if callable(method):
#             setattr(cls, name, wrap_methods(method))

#     return cls


import traceback

def handle_errors(obj):
    """
    Decorator to handle all errors in a function or class.
    """
    if isinstance(obj, type):
        # Handle class
        def wrap_methods(method):
            """
            Decorator function to wrap each method in the class with error handling.
            """
            def wrapped(*args, **kwargs):
                try:
                    return {
                        'status' : True,
                        'message': "Success",
                        'data'   : method(*args, **kwargs)
                    }
                except Exception as e:
                    return {
                        'status' : False,
                        'message': f"Error in {obj.__name__}.{method.__name__}: {e}",
                        'data'   : traceback.format_exc()
                    }
            return wrapped

        for name, method in vars(obj).items():
            if callable(method):
                setattr(obj, name, wrap_methods(method))

        return obj

    else:
        print("HERE")
        # Handle function
        def wrapped(*args, **kwargs):
            try:
                return {
                    'status' : True,
                    'message': "Success",
                    'data'   : obj(*args, **kwargs)
                }
            except Exception as e:
                return {
                    'status' : False,
                    'message': f"Error in {obj.__name__}: {e}",
                    'data'   : traceback.format_exc()
                }
        return wrapped
