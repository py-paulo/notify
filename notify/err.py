import traceback
import sys
import os

from loguru import logger


def try_except(exct: Exception, show: bool = True) -> str:
    mrkdwn = ''
    _, _, exc_tb = sys.exc_info()
    template = ('filename:{filename}-> line:{linenum}-> '
                'funcname:{funcname}-> source:{source}\n')
    for tb_info in traceback.extract_tb(exc_tb):
        filename, linenum, funcname, source = tb_info
        funcname = funcname + '()' if funcname != '<module>' else funcname
        mrkdwn += template.format(
            filename=os.path.basename(filename),
            linenum=linenum,
            source=source,
            funcname=funcname)

    if show:
        logger.error(exct)

    return mrkdwn
