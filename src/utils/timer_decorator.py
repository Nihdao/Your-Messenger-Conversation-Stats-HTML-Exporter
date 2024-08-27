import time
from typing import Callable, Any, Dict

debug = True  #Var to activate/deactivate functions

def timer_decorator(func: Callable[..., Any]) -> Callable[..., Any]:
    """
    Decorator function that times the execution of another function.

    Args:
        func (Callable): The function to be timed.

    Returns:
        Callable: The wrapped function.

    """
    def wrapper(*args: Any, **kwargs: Dict[str, Any]) -> Any:
        """
        Wrapped function that times the execution of another function.

        Args:
            *args: Positional arguments passed to the function.
            **kwargs: Keyword arguments passed to the function.

        Returns:
            Any: The return value of the function.

        """
        if debug:
            start_time: float = time.time()
            result: Any = func(*args, **kwargs)
            end_time: float = time.time()
            print(f"Timer {func.__name__} : {round(end_time - start_time, 2)} seconds")
            return result
        else:
            return func(*args, **kwargs)
    return wrapper
