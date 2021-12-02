from django import forms
from pybo.models import Question, Answer

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question #사용할 모델
        fields = ['subject', 'content'] #QuestionForm에서 사용할 Question 모델의 속성
        
        #QuestionForm에 부트스트랩 적용을 위해 추가
        # widgets = { #이름도 곡 "widgets" 여야 함
        #     'subject' : forms.TextInput(attrs={'class' : 'form-control'}),
        #     'content' : forms.Textarea(attrs={'class' : 'form-control', 'rows' : 10}),
        # }
        
        labels= { # 영어로 나오는걸 한글로 바꾸고 싶다면
            'subject' : '제목',
            'content' : '내용',
        }
        
class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields =['content']
        labels={
            'content' :'답변내용',
        }