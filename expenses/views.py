import json
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from .models import Expense
from django.core.exceptions import ValidationError
from django.utils.dateparse import parse_date

@csrf_exempt
@require_http_methods(["POST"])
def create_expense(request):
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

        expense = Expense(
            title=title,
            amount=amount,
            date=date,
            category=category,
            description=description
        )
        expense.save()
        return JsonResponse({'message': 'Expense added successfully'}, status=200)

    except ValidationError as e:
        return JsonResponse({'message': str(e)}, status=400)

@csrf_exempt
@require_http_methods(["GET"])
def get_expense(request):
    expenses = Expense.objects.all().order_by('-created_at')
    expense_list = list(expenses.values())
    return JsonResponse({
        'result': len(expense_list),
        'data': expense_list
    }, status=200)

@csrf_exempt
@require_http_methods(["DELETE"])
def delete_expense(request, id):
    try:
        expense = Expense.objects.get(id=id)
        expense.delete()
        return JsonResponse({'message': 'Expense deleted successfully'}, status=200)
    except Expense.DoesNotExist:
        return JsonResponse({'message': 'Expense not found'}, status=404)
