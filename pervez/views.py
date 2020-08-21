from django.shortcuts import render, redirect
from .models import *

def home(request):
    notes = Notes.objects.all()
    context = {
        'notes':notes
    }
    return render(request, 'pervez/home.html', context)


def Notess(request, cls):
    cl = Cls.objects.get(clss=cls)
    subject = Subject.objects.get(sub_type='Physics')
    subject2 = Subject.objects.get(sub_type='Chemistry')
    subject3 = Subject.objects.get(sub_type='Biology')
    subject4 = Subject.objects.get(sub_type='Maths')
    notes = cl.notes_set.all()

    # if request.method == 'POST':
    #     return redirect('')
    context = {
        'notes':notes,
        'subject':subject,
        'subject2':subject2,
        'subject3':subject3,
        'subject4':subject4,
    }
    return render(request, 'pervez/notes.html', context)

def notes_page(request):
    return render(request, 'pervez/notes_page.html')

def question_answers(request, cls):
    cl = Cls.objects.get(clss=cls)
    sub1 = Subject.objects.get(sub_type='Physics')
    sub2 = Subject.objects.get(sub_type='Chemistry')
    sub3 = Subject.objects.get(sub_type='Biology')
    sub4 = Subject.objects.get(sub_type='Maths')
    que_ans = cl.questionanswer_set.all()

    context = {
        'que_ans':que_ans,
        'sub1':sub1,
        'sub2':sub2,
        'sub3':sub3,
        'sub4':sub4,
        
    }

    return render(request, 'pervez/question&answers.html', context)

def lectures_subjects(request, cls):
    lectures = Lectures.objects.filter(clss=cls)
    context = {
        'lectures':lectures
    }
    return render(request, 'pervez/lectures_subject.html', context)


def per_video(request, sub, chap_name):
    
    subtop = SubTopic.objects.filter(chapter__sub__contains=sub).filter(chapter__chapter__contains=chap_name)
    length = len(subtop)
    context = {
        'subtop':subtop,
        'length':length
    }

    return render(request, 'pervez/indi_chap.html', context)







# # lec = Lectures.objects.filter(clss__exact=7)
# lectures = Lectures.objects.filter(clss=7)
# for lecture in lectures:
#     if lecture.sub == 'Physics':
#         print(lecture.chapter)
#     if lecture.sub == 'Chemistry':
#         print(lecture.sub)



# subtop = SubTopic.objects.filter(chapter__sub__contains='Physics').filter(chapter__chapter__contains='forces')

# for subs in subtop:
#     print(subs)
# # if lec.sub == 'Physics':
#     print("hello world")
# if lec.sub == 'Chemistry':
#     print('hello universe')
# print(lectures)



# subtop = SubTopic.objects.filter(sub_topic='velocity')

# print(subtop)