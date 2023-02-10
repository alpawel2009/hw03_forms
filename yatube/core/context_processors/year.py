from django.utils import timezone

now = timezone.now()


def year(request):
    """Добавляет переменную с текущим годом."""
    return {
        'year': now.year
    }
