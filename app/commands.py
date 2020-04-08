from mybot import router
from rocketgram import commonfilters, ChatType, SendMessage
from rocketgram import context2


@router.handler
@commonfilters.chat_type(ChatType.private)
@commonfilters.command('/start')
async def start_command():
    """This is asynchronous handler. You can use here any async code."""

    await SendMessage(context2.message.user.user_id,
                      '🔹 Hello there. This is the demo bot for Rocketgram framework.\n\n'
                      'See source code here:\n'
                      'github.com/vd2org/rocketgram-template\n\n'
                      'And Rocketgram framework source here:\n'
                      'github.com/vd2org/rocketgram\n\n'
                      'You can list all commands by type /help.\n\n'
                      'Support group: @RocketBots.',
                      disable_web_page_preview=True).send()


@router.handler
@commonfilters.chat_type(ChatType.private)
@commonfilters.command('/help')
def help_command():
    """Handler can also be simple function.

    But remember - in async environment you shouldn't use here hard synchronous code.

    This handler also demonstrates how to make webhook-request.

    If you use webhook executor this will be send as reply of received a webhook.
    Otherwise bot's router will fallback to send by regular call."""

    SendMessage(context2.message.user.user_id,
                "🔹 Bot's help.\n"
                "\n"
                "/start - Print welcome message.\n"
                "/help - Show this message."
                "\n"
                "\n"
                "/keyboard - Shows keyboard.\n"
                "/keyboard_location - Shows keyboard with location button.\n"
                "/keyboard_contact - Shows keyboard with contact button.\n"
                "/cancel - Removes current keyboard.\n"
                "\n"
                "/simple_inline_keyboard - Shows simple inline keyboard.\n"
                "/arranged_inline_keyboard - Shows how to arrange inline keyboard.\n"
                "/arranged_scheme_inline_keyboard - Shows how to arrange inline keyboard by scheme.\n"
                "\n"
                "/send - Shows how send files.\n"
                "\n"
                "/echo - Waiting next request in same handler.\n"
                "\n"
                "/inline - Shows how to use inline mode.\n"
                "\n"
                "/enigma - Enigma cypher machine").webhook()
