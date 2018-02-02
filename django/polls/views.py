from django.shortcuts import render
from django.http import HttpResponse, Http404

#from django.template import loader

from .models import Question, Choice

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # output = ', '.join([q.question_text for q in latest_question_list])
    context = {
        'latest_question_list': latest_question_list,
    }

    # template = loader.get_template('polls/index.html')
    # return HttpResponse(template.render(context, request))

    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    """
    question_id에 해당하는 Question객체를 탬플릿에 전달
        key: "question"
        template: polls/templates/polls/detail.html
    템플릿에서는
    1. 전달받은 question의 question_text를 출력
    2. question이 가진 모든 Choice들을 ul > li로 출력
    :param request:
    :param question_id:
    :return:
    """
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404('Question does not exist')
    context = {
        'question': question,
    }
    return render(request, 'polls/detail.html', context)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)