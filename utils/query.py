import random

from prompt_toolkit.shortcuts import checkboxlist_dialog, message_dialog
from prompt_toolkit.styles import Style


def check_question(data, index, succes_rate, left):
    random.shuffle(data[index].a)
    results = checkboxlist_dialog(
        title=f"Pytanie: {index + 1}, wynik: {succes_rate:.2f}, pozostało: {left}",
        text=data[index].q,
        values=data[index].a,
        ok_text="Ok",
        cancel_text="Wyjdź",
    ).run()

    g = [ans[1] for ans in data[index].a if ans[0] in data[index].c]
    gs = '\n'.join(g)
    if not results:
        return -1

    if set(data[index].c) == set(results):
        message_dialog(
            title="Dobrze!",
            text=data[index].q + " " + gs,
        ).run()
        return 1
    else:
        message_dialog(
            title="Źle!",
            text="Poprawna odpowiedź: " + data[index].q + " " + gs,
        ).run()
        return 0
