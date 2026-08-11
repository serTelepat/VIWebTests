import functools
import inspect
import allure


def allure_locator_step(step_pattern):
    def decorator(func):
        sig = inspect.signature(func)

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            bound = sig.bind(*args, **kwargs)
            bound.apply_defaults()

            step_variables = {}

            def _extract_name(value):
                if isinstance(value, (str, int, float, bool)):
                    return str(value)

                if isinstance(value, (tuple, list)):
                    if len(value) > 2:
                        return str(value[2])
                    elif len(value) == 2:
                        return str(value[1])
                    return str(value)

                if hasattr(value, '__doc__') and value.__doc__:
                    return value.__doc__.strip().split('\n')[0]

                if hasattr(value, 'name') and value.name:
                    return str(value.name)

                return str(value)

            for param_name, param_value in bound.arguments.items():
                if param_name in ('self', 'cls'):
                    continue

                clean_value = _extract_name(param_value)
                step_variables[param_name] = clean_value

                if 'locator' in param_name or 'element' in param_name:
                    step_variables['element_name'] = clean_value

            try:
                step_text = step_pattern.format(**step_variables)
            except KeyError as e:
                step_text = f"{step_pattern} (Missing argument: {e})"

            with allure.step(step_text):
                return func(*args, **kwargs)

        return wrapper
    return decorator

