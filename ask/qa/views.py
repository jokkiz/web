from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404#, HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage
#from django.contrib.auth import login, authenticate
#from django.contrib.auth.models import User
from django.views.decorators.http import require_GET#, require_POST
import qa.models as m

# Create your views here.
def test(request, *args, **kwargs):
    return HttpResponse("OK")

def paginate(request, qs):
    try:
        limit = int(request.GET.get('limit', 10))
    except ValueError:
        limit = 10
    if limit > 100:
        limit = 10
    try:
        page = int(request.GET.get('page', 1))
    except ValueError:
        raise Http404
    paginator = Paginator(qs, limit)
    try:
        page = paginator.page(page)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)
    return paginator, page

@require_GET
def main(request):
    quest = m.Question.objects.order_by('-id')
    paginator, page = paginate(request, quest)
    return render(request, 'main.html', {'paginator': paginator, 'page': page, 'questions': page.object_list})

@require_GET
def popular(request):
    quest = m.Question.objects.order_by('-rating')
    paginator, page = paginate(request, quest)
    return render(request, 'popular.html', {'paginator': paginator, 'page': page, 'questions': page.object_list})

def question(request, id):
    quest = get_object_or_404(m.Question, id=id)
    try:
        answers = m.Answer.objects.filter(question=quest).all()
    except m.Answer.DoesNotExist:
        answers = []
    #a = Answer(question=quest, author=request.user)
    return render(request, 'question.html', {'quest': quest, 'answers': answers})

