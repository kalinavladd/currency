from datetime import datetime, timedelta
from django.db import IntegrityError
from currency import consts
from currency.utils import get_or_create, to_decimal
from currency import custom_choices as mch
from currency.models import Rate
from django.core.management.base import BaseCommand
from django.utils import timezone
import requests


class Command(BaseCommand):
    help = "Parse archive Privatbank" # noqa

    def handle(self, *args, **options):
        url = 'https://api.privatbank.ua/p24api/exchange_rates'
        end_date = datetime.now(tz=timezone.utc)
        start_date = datetime.now(tz=timezone.utc) - timedelta(
            days=365 * 4)
        total_days = (end_date - start_date).days
        available_currency_types = {
            'USD': mch.RateTypeChoices.USD,
            'EUR': mch.RateTypeChoices.EUR,
        }
        source = get_or_create(consts.CODE_NAME_PRIVATBANK, 'Privatbank')
        for day in range(total_days):
            data = start_date + timedelta(days=day)
            params = {
                'json': '',
                'date': data.strftime("%d.%m.%Y"),
            }
            response = requests.get(url=url, params=params)
            rates = response.json()
            for rate in rates["exchangeRate"]:
                if 'currency' not in rate or rate['currency'] not in available_currency_types:
                    continue
                currency_type = available_currency_types.get(rate['currency'])
                if not currency_type:
                    continue
                base_type = available_currency_types.get(rate['baseCurrency'])
                sale = to_decimal(rate['saleRate'])
                buy = to_decimal(rate['purchaseRate'])
                try:
                    Rate.objects.get_or_create(source=source, type=base_type, sale=sale, buy=buy, created=data)
                except IntegrityError:
                    Rate.objects.get_or_create(source=source, type=base_type, sale=sale, buy=buy, created=data)
