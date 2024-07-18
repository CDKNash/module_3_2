def send_email(message, recipient, sender= "university.help@gmail.com"):
    send = "university.help@gmail.com"
    valid_sender = sender.endswith((".com", ".ru", ".net")) and "@" in sender
    valid_recipient = recipient.endswith((".com", ".ru", ".net")) and "@" in recipient
    if not valid_sender or not valid_recipient:
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
        return
    if recipient == sender:
        print("Нельзя отправить письмо самому себе!")
        return 
    if sender == send:
        print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}.')
        return
    else:
        print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.')



send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')