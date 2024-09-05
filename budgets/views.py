import json
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from .models import Income
from django.core.exceptions import ValidationError
from django.utils.dateparse import parse_date

@csrf_exempt
@require_http_methods(["POST"])
def create_income(request):
    try:
        data = json.loads(request.body)
        title = data.get('title')
        amount = data.get('amount')
        date_str = data.get('date')
        category = data.get('category')
        description = data.get('description')

        if not title or not amount or not date_str or not category or not description:
            return JsonResponse({'message': 'All fields are required'}, status=400)

        if amount <= 0 or not isinstance(amount, (int, float)):
            return JsonResponse({'message': 'Amount must be a positive number'}, status=400)

        date = parse_date(date_str)
        if not date:
            return JsonResponse({'message': 'Invalid date format'}, status=400)

        income = Income(
            title=title,
            amount=amount,
            date=date,
            category=category,
            description=description
        )
        income.save()
        return JsonResponse({'message': 'Income added successfully'}, status=200)

    except ValidationError as e:
        return JsonResponse({'message': str(e)}, status=400)

@csrf_exempt
@require_http_methods(["GET"])
def get_incomes(request):
    incomes = Income.objects.all().order_by('-created_at')
    income_list = list(incomes.values())
    return JsonResponse({
        'result': len(income_list),
        'data': income_list
    }, status=200)

@csrf_exempt
@require_http_methods(["DELETE"])
def delete_income(request, id):
    try:
        income = Income.objects.get(id=id)
        income.delete()
        return JsonResponse({'message': 'Income deleted successfully'}, status=200)
    except Income.DoesNotExist:
        return JsonResponse({'message': 'Income not found'}, status=404)
