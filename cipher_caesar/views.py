# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .cipher_algorithm import algorithm


def main_page(request):
    return render(request, 'cipher_caesar/cipher_translate.html')


@csrf_exempt
def decode(request):
    return HttpResponse(algorithm.AlgorithmDecode().get_json_result(request.body), content_type="application/json")


@csrf_exempt
def encode(request):
    return HttpResponse(algorithm.AlgorithmEncode().get_json_result(request.body), content_type="application/json")
