from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Quote
import random
import json

def home(request):
    quotes = list(Quote.objects.all())
    return render(request, 'quotes/home.html', {'quote': random.choice(quotes) if quotes else None})

def all_quotes(request):
    return render(request, 'quotes/all_quotes.html', {'quotes': Quote.objects.all()})

def quote_data(quote):
    return {'id': quote.id, 'text': quote.text, 'author': quote.author}

def random_quote_api(request):
    quotes = list(Quote.objects.all())
    if not quotes:
        return JsonResponse({'error': 'No quotes found'}, status=404)
    return JsonResponse(quote_data(random.choice(quotes)))

@csrf_exempt
def quotes_api(request):
    if request.method == 'GET':
        return JsonResponse(list(Quote.objects.values('id', 'text', 'author')), safe=False)
    if request.method == 'POST':
        data = json.loads(request.body)
        quote = Quote.objects.create(text=data['text'], author=data['author'])
        return JsonResponse(quote_data(quote), status=201)
    return JsonResponse({'error': 'Method not allowed'}, status=405)

@csrf_exempt
def quote_detail_api(request, id):
    try:
        quote = Quote.objects.get(id=id)
    except Quote.DoesNotExist:
        return JsonResponse({'error': 'Quote not found'}, status=404)
    if request.method == 'GET':
        return JsonResponse(quote_data(quote))
    if request.method == 'PUT':
        data = json.loads(request.body)
        if 'text' in data:
            quote.text = data['text']
        if 'author' in data:
            quote.author = data['author']
        quote.save()
        return JsonResponse(quote_data(quote))
    if request.method == 'DELETE':
        quote.delete()
        return JsonResponse({'message': 'Quote deleted successfully'})
    return JsonResponse({'error': 'Method not allowed'}, status=405)
