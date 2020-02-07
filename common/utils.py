import time


def create_time_stamp():
    """
    生成秒级时间戳
    :return:
    """

    return time.time()


def json_response(data, message, code):
    """
    临时的封装返回数据
    :param data:
    :param message:
    :param code:
    :return:
    """
    return {'data': data, 'message': message, 'code': code}
