from schemas.pySchemas import ResponseSchema


def return_result(result: bool, info: str = None, data: dict = None) -> any:
    """
    Creating a return result
    :param result:
    :param info:
    :param data:
    :return dict:
    """
    if data is not None:
        if info is not None:
            return ResponseSchema(result=result, info=info, data=data)
        else:
            return ResponseSchema(result=result, data=data)
    else:
        return ResponseSchema(result=result, info=info)
