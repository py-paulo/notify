import enum


class TypeLog(enum.Enum):

    WARNING = (
        '#ffea00',
        ':warning:',
        'https://www.abmaxeducacional.com.br/wp-content/uploads/2020/11/warning.png')
    CRITICAL = (
        '#ff1744',
        ':x:',
        'https://www.shareicon.net/data/2015/08/18/86945_warning_512x512.png')
    INFO = (
        '#00b0ff',
        ':whale:',
        'https://cdn.iconscout.com/icon/free/png-256/'
        'info-circle-symbol-information-letter-31343.png')
    ERROR = (
        '#ff4081',
        ':exclamation:',
        'https://www.shareicon.net/data/2015/08/18/86945_warning_512x512.png')


def get_color_type_log(type_log: TypeLog) -> str:
    return type_log.value[0]


def get_emoji_type_log(type_log: TypeLog) -> str:
    return type_log.value[1]


def get_image_type_log(type_log: TypeLog) -> str:
    return type_log.value[2]
