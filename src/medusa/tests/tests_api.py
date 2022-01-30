import datetime

import pytest
from django.urls import reverse

from medusa.web.models import Post


@pytest.mark.django_db
def test_api_list_smoke(client):
    url = reverse('api:news_list')
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_api_list_date_order(client):
    right_order_dates = [
        datetime.date(2022, 1, 2),
        datetime.date(2022, 1, 1),
        datetime.date(2021, 12, 31),
    ]

    # Создаем с датами не по порядку
    Post(date=right_order_dates[0], subject='title1', content='content').save()
    Post(date=right_order_dates[2], subject='title2', content='content').save()
    Post(date=right_order_dates[1], subject='title3', content='content').save()

    url = reverse('api:news_list')
    response = client.get(url)

    data = response.json()

    for i, item in enumerate(data):
        assert right_order_dates[i].strftime('%Y-%m-%d') == item['date']
