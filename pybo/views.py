from django.core import paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
#from django.http import HttpResponse
from .models import Question
from .forms import QuestionForm, AnswerForm
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
    """
        pybo 목록 출력
    """
    
    #입력 파라미터
    page = request.GET.get('page', '1') #페이지
    #pybo/?page=1 처럼 get방식으로 호출된 url에서 page값을 가져오는데 사용
    # 만약 pybo/ 처럼 page값 없이 호출된다면 디폴트 1
    #조회
    question_list = Question.objects.order_by('-create_date')
    
    #페이징처리
    paginator = Paginator(question_list, 10) #페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)
    
    context = {'question_list' : page_obj}
    return render(request, 'pybo/question_list.html', context)
    #return HttpResponse("Welcome to Pybo!")
    
def detail(request, question_id):
    """
        pybo 내용 출력
    """
    question = get_object_or_404(Question, pk = question_id)
    context = {'question' : question}
    return render(request, 'pybo/question_detail.html', context)

@login_required(login_url = 'common:login')
def answer_create(request,question_id):
    ## 질문 등록하기 버튼 과 저장하기 버튼 둘다 question_create를 호출함 : 구분을 post와 get으로 한다.
    """
        pybo 답변등록 : post
        get 은 그냥 형식 통일상 ㅇㅇ
    """
    #post
    question = get_object_or_404(Question, pk=question_id)
    if request.method == 'POST':
        form = AnswerForm(request.POST) #request.POST 에는 subject와 content가 들어있음
        if form.is_valid():
            answer = form.save(commit=False) # 임시저장 : creat_date 정보가 없기 때문
            answer.author = request.user
            answer.create_date = timezone.now()
            answer.question = question
            answer.save()
            return redirect('pybo:detail', question_id=question_id)
    else:
        form = AnswerForm() #get
    context = {'form' : form, 'question' :question}
    return render(request, 'pybo/question_detail.html', context)

@login_required(login_url = 'common:login')
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
            question = form.save(commit=False) # 임시저장 : creat_date 정보가 없기 때문
            question.author = request.user
            question.create_date = timezone.now()
            question.save()
            return redirect('pybo:index')
    else:
        form = QuestionForm() #get
    context = {'form' : form}
    return render(request, 'pybo/question_form.html', context)