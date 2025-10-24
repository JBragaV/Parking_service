from time import sleep

from celery import shared_task
from playwright.sync_api import sync_playwright

from .models import Vehicle


def _fazer_scraping_lento(placa):
    dados_veiculos = {
        'ABC1234': {'brand': 'Fiat', 'model': 'Marea', 'color': 'Prata'},
        'DEF5678': {'brand': 'Chevrolet', 'model': 'Opala', 'color': 'Preto'},
        'GHI9012': {'brand': 'Chevrolet', 'model': 'Chevette', 'color': 'Branco'},
        'JKL3456': {'brand': 'Volkswagen', 'model': 'Fusca', 'color': 'Azul'},
        'MNO7890': {'brand': 'Volkswagen', 'model': 'Kombi', 'color': 'Cinza'},
        'PQR1122': {'brand': 'Ford', 'model': 'Corcel', 'color': 'Verde'},
        'STU3344': {'brand': 'Ford', 'model': 'Del Rey', 'color': 'Amarelo'},
        'VWX5566': {'brand': 'Chevrolet', 'model': 'Monza', 'color': 'Marrom'},
        'YZA7788': {'brand': 'Chevrolet', 'model': 'Opala', 'color': 'Preto'},
        'ZBC9900': {'brand': 'Volkswagen', 'model': 'Fusca', 'color': 'Branco'}
    }
    sleep(5)
    dados = dados_veiculos.get(placa, False)
    if dados:
        return dados
    return {}

@shared_task
def complete_vehicle_data(license_plate):
    print('Completar as info do carro')
    # url = 'https://pycodebr.com.br/placas-carros/'

    brand = None
    model = None
    color = None
    dados = _fazer_scraping_lento(license_plate)
    if dados:
        brand = dados['brand']
        model = dados['model']
        color = dados['color']
    # with sync_playwright() as p:
    #     browser = p.chromium.launch(headless=True)
    #     page = browser.new_page()
    #     page.goto(url)
    #     page.wait_for_selector('table')
    #     xpath_expression = f"//table//tr[td[1][normlize-space()='{license_plate}']]"
    #     row = page.query_selector(xpath_expression)
    #     if row:
    #         cells = row.query_selector_all('td')
    #         brand = cells[1].inner_text().strip()
    #         model = cells[2].inner_text().strip()
    #         color = cells[3].inner_text().strip()
    #     browser.close()

    if brand and model and color:
        Vehicle.objects.filter(
            license_plate=license_plate
        ).update(
            brand=brand, model=model, color=color
        )
