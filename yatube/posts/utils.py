from django.core.paginator import Paginator
from django.conf import settings


def pagination(request, post_list, POSTS_AMOUNT=settings.POSTS_AMOUNT):
    paginator = Paginator(post_list, POSTS_AMOUNT)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return page_obj
