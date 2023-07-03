import os

import pymsteams

from ..structs import TypeLog, get_color_type_log, get_image_type_log
from ..utils import get_filename_from_path
from ..default import (DEFAULT_TITLE_DESCRIPTION, DEFAULT_TITLE_MESSAGE)


def make_message(
        title: str, body: str, tool_name: str, module: str, origin_ip: str, type_info: str,
        type_log: TypeLog, **kwargs
) -> pymsteams.connectorcard:

    _module = module
    if ('/' in module) or ('\\' in module):
        _module = get_filename_from_path(module)

    message: pymsteams.connectorcard = kwargs['connector_card']

    message.title("ERROR [%s] [%s] %s." % (tool_name, _module, title))
    message.color(get_color_type_log(type_log))
    message.text(DEFAULT_TITLE_DESCRIPTION % tool_name)

    message_section = pymsteams.cardsection()
    message_section.activitySubtitle(DEFAULT_TITLE_MESSAGE)
    message_section.activityTitle("Oops... alert coming from the file %s" % module)
    message_section.activityImage(get_image_type_log(type_log))
    message_section.activityText("to acess server: ssh opc@%s" % origin_ip)
    message_section.addFact("origin", "`%s`" % origin_ip)
    message_section.addFact("filename", "`%s`" % _module)
    message_section.addFact("pid", "`%d`" % os.getpid())
    message_section.addFact("type", "`%s`" % type_info)
    message_section.text('```' + body + '```')

    message.addSection(message_section)

    return message
