import requests
from bs4 import BeautifulSoup as BS

from parser.serializers import RatesSerializer

from parser.serializers import Rates
from rest_framework.decorators import api_view
from rest_framework.response import Response


# Create your views here.
@api_view(('GET',))
def money(request, c_from, c_to, value):
    r = requests.get('https://www.alta.ru/currency/')
    html = BS(r.content, 'html.parser')
    res1 = html.find_all('span', class_= 'gray col-50 t-left ml5 m-ml2')
    res2 = html.find_all('td', class_= 't-right')
    dataVal = {i.text:float(b.text.rstrip()) for i, b in zip(res1, res2)}
    dataVal['RUB'] = 1
    res = dataVal[c_from] * value / dataVal[c_to]
    serializer = RatesSerializer(Rates(result = res))
    print(serializer.data)
    return Response(serializer.data)