import os

from typing import List, Dict, Union

from ..utils import scape_double_quotes, get_filename_from_path
from ..structs import TypeLog
from ..structs import get_image_type_log, get_color_type_log


def _make_header(
        image_url: str, tool: str, module: str, title: str, type_log: TypeLog
) -> Dict[str, Union[str, List[Dict[str, str]]]]:
    ELEMENTS = [
        {
            "type": "image",
            "image_url": "%s" % image_url,
            "alt_text": "alt text"
        },
        {
            "type": "mrkdwn",
            "text": "*%s* [%s] [%s] %s." % (str(type_log).split('.')[-1], tool, module, title)
        }
    ]

    return {
        "type": "context",
        "elements": ELEMENTS
    }


def _make_content(
        content: str
) -> Dict[str, Union[str, Dict[str, str]]]:
    CONTENT = {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "```%s```" % content
        }
    }

    return CONTENT


def _make_fields(
        ipv4: str, script_name: str, pid: int, type_info: str
) -> Dict[str, Union[str, List[Dict[str, str]]]]:
    FIELDS = [
        {
            "type": "mrkdwn",
            "text": "*ORIGIN* : `%s`" % ipv4
        },
        {
            "type": "mrkdwn",
            "text": "*SCRIPT* : `%s`" % script_name
        },
        {
            "type": "mrkdwn",
            "text": "*PID*        : `%d`" % pid
        },
        {
            "type": "mrkdwn",
            "text": "*TYPE*     : `%s`" % type_info
        }
    ]

    return {
        "type": "section",
        "fields": FIELDS,
    }


def _make_divider() -> Dict[str, str]:
    return {"type": "divider"}


def make_message(
        title: str, body: str, tool_name: str, module: str, origin_ip: str, type_info: str,
        type_log: TypeLog
) -> List[Dict[str, Union[str, list]]]:

    image_url = get_image_type_log(type_log)
    if ('/' in module) or ('\\' in module):
        module = get_filename_from_path(module)
    header = _make_header(
        image_url=image_url, tool=tool_name, module=module, title=title, type_log=type_log)
    content = _make_content(
        scape_double_quotes(body))
    fields = _make_fields(ipv4=origin_ip, script_name=module, pid=os.getpid(), type_info=type_info)

    return [
        {
            "color": get_color_type_log(type_log),
            "fallback": "<fallbakc-here>",
            "blocks": [
                header,
                _make_divider(),
                content,
                _make_divider(),
                fields
            ],
        }]
