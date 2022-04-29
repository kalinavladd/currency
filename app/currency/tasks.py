from bs4 import BeautifulSoup
from celery import shared_task

from . import consts
from . import custom_choices as cmc
from .utils import get_or_create, to_decimal

import requests


@shared_task
def parse_privatbank():
    from .models import Rate
    source = get_or_create(consts.CODE_NAME_PRIVATBANK, 'Privatbank')

    response = requests.get(consts.API_PRIVATBANK_URL)
    response.raise_for_status()
    rates = response.json()
    available_currency_types = {
        'USD': cmc.RateTypeChoices.USD,
        'EUR': cmc.RateTypeChoices.EUR,
    }

    for rate in rates:
        buy = to_decimal(rate['buy'])
        sale = to_decimal(rate['sale'])
        currency_type = rate['ccy']

        if currency_type not in available_currency_types:
            continue

        last_rate = Rate.objects \
            .filter(type=available_currency_types[currency_type], source=source) \
            .order_by('-created') \
            .first()

        if last_rate is None or \
                last_rate.buy != buy or \
                last_rate.sale != sale:
            Rate.objects.create(
                buy=buy,
                sale=sale,
                type=available_currency_types[currency_type],
                source=source,
            )


@shared_task
def parse_monobank():
    from .models import Rate

    source = get_or_create(consts.CODE_NAME_MONOBANK, 'Monobank')

    response = requests.get(consts.API_MONOBANK_URL)
    response.raise_for_status()
    rates = response.json()[0:3]
    available_currency_types = {
        840: cmc.RateTypeChoices.USD,
        978: cmc.RateTypeChoices.EUR,
    }

    for rate in rates:
        buy = to_decimal(rate['rateBuy'])
        sale = to_decimal(rate['rateSell'])
        currency_type = rate['currencyCodeA']

        if currency_type not in available_currency_types:
            continue

        last_rate = Rate.objects \
            .filter(type=available_currency_types[currency_type], source=source) \
            .order_by('-created') \
            .first()

        if last_rate is None or \
                last_rate.buy != buy or \
                last_rate.sale != sale:

            Rate.objects.create(
                buy=buy,
                sale=sale,
                type=available_currency_types[currency_type],
                source=source,
            )


@shared_task
def parse_vkurse():
    from .models import Rate

    source = get_or_create(consts.CODE_NAME_VKURSE, 'Vkurse')

    response = requests.get(consts.API_VKURSE_URL)
    response.raise_for_status()
    rates = response.json()
    available_currency_types = {
        'Dollar': cmc.RateTypeChoices.USD,
        'Euro': cmc.RateTypeChoices.EUR,
    }

    for rate in rates:
        buy = to_decimal(rates[rate]['buy'])
        sale = to_decimal(rates[rate]['sale'])
        currency_type = rate

        if currency_type not in available_currency_types:
            continue

        last_rate = Rate.objects \
            .filter(type=available_currency_types[currency_type], source=source) \
            .order_by('-created') \
            .first()

        if last_rate is None or \
                last_rate.buy != buy or \
                last_rate.sale != sale:

            Rate.objects.create(
                buy=buy,
                sale=sale,
                type=available_currency_types[currency_type],
                source=source,
            )


@shared_task
def parse_kredo():
    from .models import Rate

    source = get_or_create(consts.CODE_NAME_KREDO, 'Kredo')

    response = requests.get(consts.API_KREDO_URL)
    response.raise_for_status()
    soup = BeautifulSoup(response.content, 'lxml')
    table = soup.find('table')
    buy_usd = table.find_all('tr')[1].find_all('td')[3].text
    sale_usd = table.find_all('tr')[1].find_all('td')[2].text
    buy_euro = table.find_all('tr')[2].find_all('td')[3].text
    sale_euro = table.find_all('tr')[2].find_all('td')[2].text
    usd = {'ccy': 'USD', 'buy': buy_usd, 'sale': sale_usd}
    euro = {'ccy': 'EUR', 'buy': buy_euro, 'sale': sale_euro}
    rates = [usd, euro]
    available_currency_types = {
        'USD': cmc.RateTypeChoices.USD,
        'EUR': cmc.RateTypeChoices.EUR,
    }

    for rate in rates:
        buy = to_decimal(rate['buy'])
        sale = to_decimal(rate['sale'])
        currency_type = rate['ccy']

        if currency_type not in available_currency_types:
            continue

        last_rate = Rate.objects \
            .filter(type=available_currency_types[currency_type], source=source) \
            .order_by('-created') \
            .first()

        if last_rate is None or \
                last_rate.buy != buy or \
                last_rate.sale != sale:

            Rate.objects.create(
                buy=buy,
                sale=sale,
                type=available_currency_types[currency_type],
                source=source,
            )


@shared_task
def parse_otp():
    from .models import Rate

    source = get_or_create(consts.CODE_NAME_OTP, 'Otp')

    response = requests.get(consts.API_OTP_URL)
    response.raise_for_status()
    soup = BeautifulSoup(response.content, 'lxml')
    table = soup.find('table')
    buy_usd = table.find_all('tr')[1].find_all('td')[1].text
    sale_usd = table.find_all('tr')[1].find_all('td')[2].text
    buy_euro = table.find_all('tr')[2].find_all('td')[1].text
    sale_euro = table.find_all('tr')[2].find_all('td')[2].text
    usd = {'ccy': 'USD', 'buy': buy_usd, 'sale': sale_usd}
    euro = {'ccy': 'EUR', 'buy': buy_euro, 'sale': sale_euro}
    rates = [usd, euro]
    available_currency_types = {
        'USD': cmc.RateTypeChoices.USD,
        'EUR': cmc.RateTypeChoices.EUR,
    }

    for rate in rates:
        buy = to_decimal(rate['buy'])
        sale = to_decimal(rate['sale'])
        currency_type = rate['ccy']

        if currency_type not in available_currency_types:
            continue

        last_rate = Rate.objects \
            .filter(type=available_currency_types[currency_type], source=source) \
            .order_by('-created') \
            .first()

        if last_rate is None or \
                last_rate.buy != buy or \
                last_rate.sale != sale:

            Rate.objects.create(
                buy=buy,
                sale=sale,
                type=available_currency_types[currency_type],
                source=source,
            )


@shared_task
def parse_credit_agricole():
    from .models import Rate

    source = get_or_create(consts.CODE_NAME_CREDIT_AGRIKOLE, 'Credit_agricole')

    response = requests.get(consts.API_CREDIT_AGRIKOLE_URL)
    response.raise_for_status()
    soup = BeautifulSoup(response.content, 'lxml')
    table = soup.find('table')
    buy_usd = table.find_all('tr')[1].find_all('td')[1].text
    sale_usd = table.find_all('tr')[1].find_all('td')[2].text
    buy_euro = table.find_all('tr')[2].find_all('td')[1].text
    sale_euro = table.find_all('tr')[2].find_all('td')[2].text
    usd = {'ccy': 'USD', 'buy': buy_usd, 'sale': sale_usd}
    euro = {'ccy': 'EUR', 'buy': buy_euro, 'sale': sale_euro}
    rates = [usd, euro]
    available_currency_types = {
        'USD': cmc.RateTypeChoices.USD,
        'EUR': cmc.RateTypeChoices.EUR,
    }

    for rate in rates:
        buy = to_decimal(rate['buy'])
        sale = to_decimal(rate['sale'])
        currency_type = rate['ccy']

        if currency_type not in available_currency_types:
            continue

        last_rate = Rate.objects \
            .filter(type=available_currency_types[currency_type], source=source) \
            .order_by('-created') \
            .first()

        if last_rate is None or \
                last_rate.buy != buy or \
                last_rate.sale != sale:

            Rate.objects.create(
                buy=buy,
                sale=sale,
                type=available_currency_types[currency_type],
                source=source,
            )
