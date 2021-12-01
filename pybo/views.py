from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
#from django.http import HttpResponse
from .models import Question, Answer
from .forms import QuestionForm
# Create your views here.

def index(request):
    """
        pybo 목록 출력
    """
    question_list = Question.objects.order_by('-create_date')
    context = {'question_list' : question_list}
    return render(request, 'pybo/question_list.html', context)
    #return HttpResponse("Welcome to Pybo!")
    
def detail(request, question_id):
    """
        pybo 내용 출력
    """
    question = get_object_or_404(Question, pk = question_id)
    context = {'question' : question}
    return render(request, 'pybo/question_detail.html', context)

def answer_create(request, question_id):
    """
        pybo 답변등록
    """
    question = get_object_or_404(Question, pk = question_id)
    answer = Answer(question=question,
                    content = request.POST.get('content'),
                    create_date =timezone.now()        
            )
    answer.save()
    # question.answer_set.create(
    #     content = request.POST.get('content'),
    #     create_date = timezone.now()    
    # ) !!!!same!!!!
    return redirect('pybo:detail', question_id = question.id)

def question_create(request):
    ## 질문 등록하기 버튼 과 저장하기 버튼 둘다 question_create를 호출함 : 구분을 post와 get으로 한다.
    """
        pybo 질문등록 : 질문등록 함수를 호출할 때 '저장하기'버튼 : post
        '질문 등록하기' 버튼 : get 
    """
    #post
    
    if request.method == 'POST':
        form = QuestionForm(request.POST) #request.POST 에는 subject와 content가 들어있음
        if form.is_valid():
            question = form.save(commit=False)
            question.create_date = timezone.now()
            question.save()
            return redirect('pybo:index')
    else:
        form = QuestionForm() #get
    context = {'form' : form}
    return render(request, 'pybo/question_form.html', context)