import os


def scape_double_quotes(text: str):
    """Escapa aspas duplas ( " ) -> ( \\" ) de texto colocando um contrabarra.

    >>> string = '{"abc": "def"}'
    >>> new_string = scape_double_quotes(string)
    >>> type(new_string)
    <class 'str'>
    >>> string == '{\\"abc\\": \\"def\\"}'
    True

    Args:
        text (str): texto com aspas duplas

    Returns:
        str: texto com contrabarra antes da aspas duplas
    """
    return text.replace('"', '\\"')


def get_filename_from_path(path: str) -> str:
    """A partir do caminho de um arquivo completo é retornado o nome do arquivo.

    >>> full_path = '/home/opc/project/main.py'
    >>> filename = get_filename_from_path(full_path)
    >>> if os.name == 'nt':
    ...     filename == '/home/opc/project/main.py'
    ... else:
    ...     filename == 'main.py'
    True
    >>> full_path = 'users\\public\\documents\\main.py'
    >>> filename = get_filename_from_path(full_path)
    >>> if os.name == 'nt':
    ...     filename == 'main.py'
    ... else:
    ...     filename == 'users\\public\\documents\\main.py'
    True

    Args:
        path (str): caminho completo do arquivo

    Returns:
        str: nome do arquivo
    """
    return str(path).split('\\')[-1] if os.name == 'nt' else str(path).split('/')[-1]
