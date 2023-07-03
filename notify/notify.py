import socket

from typing import Any

import pymsteams

from jsonschema import validate, ValidationError
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

from .default import (
    DEFAULT_SLACK_ENABLED, DEFAULT_TEAMS_ENBALED, DEFAULT_TELEGRAM_ENABLED,
    DEFAULT_ERRORS_ENABLED)
from .default import (
    DEFAULT_LOG_TYPE, DEFAULT_NOTIFY, DEFAULT_TOOL_NAME, DEFAULT_TITLE_MESSAGE,
    DEFAULT_TITLE_DESCRIPTION)
from .schema import (
    SCHEMA_SLACK, SCHEMA_TEAMS)

from .err import try_except
from .structs import TypeLog, get_emoji_type_log

from .slack.build import (make_message as slack_make_message)
from .teams.build import (make_message as teams_make_message)


class Notify:

    def __init__(
            self,
            origin_ip: str = None,
            enable_slack: bool = DEFAULT_SLACK_ENABLED,
            enable_telegram: bool = DEFAULT_TEAMS_ENBALED,
            enable_teams: bool = DEFAULT_TELEGRAM_ENABLED,
            slack_token: str = None,
            slack_channel: str = None,
            telegram_token: str = None,
            telegram_chatid: str = None,
            teams_webhook_url: str = None,
            enable_errors: bool = DEFAULT_ERRORS_ENABLED,
            **kwargs
    ) -> None:
        """
        Define e habilita quais tecnologias serão utilizadas nos alertas.

        Args:
            enable_slack (bool, optional): enable/no-enable. Defaults to DEFAULT_SLACK_ENABLED.
            enable_telegram (bool, optional): enable/no-enable. Defaults to DEFAULT_TEAMS_ENBALED.
            enable_teams (bool, optional): enable/no-enable. Defaults to DEFAULT_TELEGRAM_ENABLED.
            slack_token (str, optional): TOKEN Defaults to None.
            slack_channel (str, optional): #channel or chat. Defaults to None.
            telegram_token (str, optional): token-telegram. Defaults to None.
            telegram_chatid (str, optional): telegram-chatid. Defaults to None.
            teams_webhook_url (str, optional): teams-webhook-url. Defaults to None.
            enable_errors (bool, optional): enable/no-enable. Defaults to DEFAULT_ERRORS_ENABLE.
        """
        self.origin_ip = origin_ip if origin_ip else socket.gethostbyname(socket.gethostname())

        self.enable_slack = enable_slack
        self.enable_telegram = enable_telegram
        self.enable_teams = enable_teams
        self.enable_errors = enable_errors
        self.slack_token = slack_token
        self.slack_channel = slack_channel
        self.telegram_token = telegram_token
        self.telegram_chatid = telegram_chatid
        self.teams_webhook_url = teams_webhook_url

        self.slack_client = None

        if self.enable_slack:
            try:
                validate(
                    instance={
                        "channel": self.slack_channel, "token": self.slack_token
                    }, schema=SCHEMA_SLACK)
            except ValidationError as err:
                try_except(err, show=self.enable_errors)
                self.enable_slack = False
            else:
                if not self.slack_channel.startswith('#'):
                    self.slack_channel = '#' + self.slack_channel

                self.slack_client = WebClient(token=self.slack_token)

        if self.enable_teams:
            try:
                validate(
                    instance={
                        "webhook-url": self.teams_webhook_url
                    }, schema=SCHEMA_TEAMS
                )
            except ValidationError as err:
                try_except(err, show=self.enable_errors)
                self.enable_teams = False

    def log(
            self,
            content: Any,
            title: str = DEFAULT_TITLE_MESSAGE,
            tool: str = DEFAULT_TOOL_NAME,
            type_log: str = DEFAULT_LOG_TYPE,
            notify: bool = DEFAULT_NOTIFY,
            **kwargs
    ) -> bool:
        """
        Criar alerta nas plataformas habilitadas.

        Args:
            content (Any): Corpo da mensagem para alerta.
            title (str, optional): titulo para card de alerta. Defaults to DEFAULT_TITLE_MESSAGE.
            tool (str, optional): ferramenta que está partindo o log. Defaults to DEFAULT_TOOL_NAME.
            type_log (str, optional): DEBUG|INFO|WARNING|ERROR|DANGET. Defaults to DEFAULT_LOG_TYPE.
            notify (bool, optional): habilitar envio para tecnologias. Defaults to DEFAULT_NOTIFY.

        Returns:
            bool: true se os logs forem enviados com sucesso
        """
        _ret_bool = True

        _type_log = TypeLog.INFO
        for t in TypeLog:
            _type = str(t).split('.')[-1]
            if _type == type_log:
                _type_log = t
                break
        _level = str(_type_log).split('.')[-1].upper()

        if self.enable_slack and notify:
            built_slack_message = slack_make_message(
                title=title,
                body=content,
                tool_name=tool,
                module=__file__,
                origin_ip=self.origin_ip,
                type_log=_type_log,
                type_info='EXCEPTION')
            try:
                self.slack_client.chat_postMessage(
                    channel=self.slack_channel,
                    attachments=built_slack_message, icon_emoji=get_emoji_type_log(_type_log),
                    text=DEFAULT_TITLE_DESCRIPTION % tool)
            except SlackApiError as err:
                try_except(err)
                _ret_bool = False

        if self.enable_teams and notify:
            connector_card = pymsteams.connectorcard(self.teams_webhook_url)
            connector_card = teams_make_message(
                title=title,
                body=content,
                tool_name=tool,
                module=__file__,
                origin_ip=self.origin_ip,
                type_log=_type_log,
                type_info='EXCEPTION',
                connector_card=connector_card)
            connector_card.send()

        return _ret_bool
