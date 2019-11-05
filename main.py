import json

from choose import BasicChooser, PseudoBlackListChooser, BlackListChooser
from mail import ConsoleEmailSender, GoogleEmailSender
from templates import basic_message_template, noncity_message_template


def get_participants():
    with open("participants.json") as json_file:
        data = json.load(json_file)
        return data


def get_config():
    with open("smtp.json") as json_file:
        return json.load(json_file)


def main():
    email_sender = GoogleEmailSender()
    email_sender.init_configuration(get_config())
    chooser = BlackListChooser()
    chooser.set_participants(get_participants())
    result = chooser.finalize_list()
    for res_name, res in result.items():
        if res['email'] != 'tsygankov.itis@gmail.com':
            continue
        friend = result[res['friend']]
        if friend['is_nonresident']:
            email_sender.send_message(res['email'], noncity_message_template.format(name=res_name, friend=res['friend'],
                                                                                    address=friend['address']))
        else:
            email_sender.send_message(res['email'], basic_message_template.format(name=res_name, friend=res['friend']))


if __name__ == '__main__':
    main()
