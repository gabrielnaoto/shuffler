# Create your views here.
from random import shuffle

from django.shortcuts import render
from django.views.generic import TemplateView

from core.models import Student


class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['students'] = Student.objects.all()
        return context

    def post(self, request, **kwargs):
        selected_students = self.request.POST.getlist('student', list())
        ids = [int(item) for item in selected_students]
        a_students = list(Student.objects.filter(id__in=ids, rank='A'))
        b_students = list(Student.objects.filter(id__in=ids, rank='B'))
        shuffle(a_students)
        shuffle(b_students)
        odds = list()
        if len(a_students) % 2 != 0:
            odds.append(a_students.pop(-1))
        if len(b_students) % 2 != 0:
            odds.append(b_students.pop(-1))
        a_half = int(len(a_students) / 2)
        b_half = int(len(b_students) / 2)
        group_a = a_students[0:a_half] + b_students[0:b_half]
        group_b = a_students[a_half:] + b_students[b_half:]
        if len(odds) == 2:
            group_a.append(odds[0])
            group_b.append(odds[1])
        elif len(odds) == 1:
            group_a.append(odds[0])
        context = {
            'group_a': sorted(group_a, key=lambda x: x.name),
            'group_b': sorted(group_b, key=lambda x: x.name)
        }
        return render(request, template_name='result.html', context=context)
