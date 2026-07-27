from celery import shared_task


@shared_task
def update_currency_rates():
    """Оновлення курсів валют з ПриватБанку (щодня о 9:00)"""
    pass


@shared_task
def check_profanity(listing_id: int):
    """Перевірка оголошення на нецензурну лексику"""
    pass


@shared_task
def notify_manager(listing_id: int):
    """Надіслати лист менеджеру якщо оголошення не пройшло перевірку"""
    pass
