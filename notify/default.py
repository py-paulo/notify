from .version import __version__

DEFAULT_SLACK_ENABLED: bool = True
DEFAULT_TELEGRAM_ENABLED: bool = False
DEFAULT_TEAMS_ENBALED: bool = False

DEFAULT_LOG_TYPE: str = 'INFO'
DEFAULT_NOTIFY: bool = True

DEFAULT_ERRORS_ENABLED: bool = True

DEFAULT_TOOL_NAME: str = 'notify'
DEFAULT_TITLE_MESSAGE: str = ':construction: Notify ! tool created by paulo.beserra ' \
                             'with current version v%s :sparkles:' % __version__
DEFAULT_TITLE_DESCRIPTION: str = ('Oops, it looks like an exception or a trigger '
                                  'was activated by the "%s" tool, '
                                  'more details of the alert follow.')
