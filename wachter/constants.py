from enum import IntEnum, auto

# MESSAGES
on_set_new_message = 'Обновил сообщение.'
on_success_set_kick_timeout_response = 'Обновил таймаут кика.'
on_failed_set_kick_timeout_response = 'Таймаут должен быть целым положительным числом'
on_failed_kick_response = 'Я не справился.'
on_start_command = 'Выберите чат:'
help_message = '''HELP'''

default_kick_timeout = 0
notify_delta = 5


# ACTIONS
class Actions(IntEnum):
    select_chat = auto()
    set_on_new_chat_member_message_response = auto()
    set_notify_message = auto()
    set_on_successful_introducion_response = auto()
    set_on_known_new_chat_member_message_response = auto()
    set_kick_timeout = auto()