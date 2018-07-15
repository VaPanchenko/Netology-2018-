import osa
import requests
import xml.etree.ElementTree as ET


def average_temp_from_file(file):

    with open(file, 'r') as f:
        data_list = []
        summa = 0
        while True:
            data = f.readline().strip().split()
            if not data:
                break
            data_list.append(data)
        for i in data_list:
            summa += int(i[0])
        average_temp = summa / len(data_list)
    return average_temp


def add(temps):

    headers = {'Content-Type':'text/xml'}
    data = f'''<?xml version="1.0" encoding="utf-8"?>
<soap12:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap12="http://www.w3.org/2003/05/soap-envelope">
  <soap12:Body>
    <FahrenheitToCelsius xmlns="https://www.w3schools.com/xml/">
      <Fahrenheit>{temps}</Fahrenheit>
    </FahrenheitToCelsius>
  </soap12:Body>
</soap12:Envelope>'''

    res = requests.post('https://www.w3schools.com/xml/tempconvert.asmx', data=data, headers=headers)
    return res.text


root = ET.fromstring(add(str(average_temp_from_file('temps.txt'))))



def get_cost_fly(file):

    with open (file, 'r') as f:
        data_list = []
        while True:
            data = f.readline().strip().split()
            if not data:
                break
            data_list.append(data)

    return data_list


def convert_currency(fromCurrency, amount):
    client = osa.Client('http://fx.currencysystem.com/webservices/CurrencyServer4.asmx?WSDL')
    response = client.service.ConvertToNum(fromCurrency=fromCurrency, toCurrency='RUB', amount=amount, rounding=True)
    return response


def main():
    fly_data = (get_cost_fly('currencies.txt'))
    sum = 0
    for i in fly_data:
        sum += convert_currency(i[2], i[1])
    return round(sum)


print('Средняя температура в градусах : ', ET.fromstring(add(str(average_temp_from_file('temps.txt'))))[0][0][0].text)
print('Сумма перелетов в рублях = ', main())



