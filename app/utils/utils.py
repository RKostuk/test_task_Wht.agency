def return_result(result: bool, info: str = None, data: dict = None) -> dict:
    """
    Creating a return result
    :param result:
    :param info:
    :param data:
    :return dict:
    """
    if data is not None:
        if info is not None:
            return {
                'result': result,
                'info': info,
                'data': data,
            }
        else:
            return {
                'result': result,
                'data': data,
            }
    else:
        return {
            'result': result,
            'info': info,
        }
