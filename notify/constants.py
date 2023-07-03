ERR_BODY_EXAMPLE = """
No error handlers are registered, logging exception.
Traceback (most recent call last):
  File "/home/opc/.pyenv/versions/FGU/lib/python3.8/site-packages/telegram/ext/dispatcher.py", line 442, in process_update
    handler.handle_update(update, self, check, context)
  File "/home/opc/.pyenv/versions/FGU/lib/python3.8/site-packages/telegram/ext/handler.py", line 160, in handle_update
    return self.callback(update, context)
  File "/home/opc/devops.prod/fgu/core/bot/bot.py", line 122, in receive_to_action
    if not asset_chatid(update.message.chat.id):
AttributeError: 'NoneType' object has no attribute 'chat'
"""
ERR_TITLE_EXAMPLE = "AttributeError: 'NoneType' object has no attribute 'chat'"
