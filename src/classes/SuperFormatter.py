from typing import Any, Dict, Union
import string
from ..utils.timer_decorator import timer_decorator


@timer_decorator
class SuperFormatter(string.Formatter):
    def format_field(self, value: Union[Any, Dict[str, Any]], spec: str) -> str:
        """
        Formats a field based on the provided specification.

        Args:
            value (Union[Any, Dict[str, Any]]): The value to be formatted.
            spec (str): The format specification.

        Returns:
            str: The formatted string.
        """
        if spec.startswith('repeat'):
            template = spec.partition(':')[-1]
            if isinstance(value, dict):
                value = value.items()
            return ''.join([template.format(item=item) for item in value])
        elif not spec:
            return str(value)
        else:
            return super().format_field(value, spec)

