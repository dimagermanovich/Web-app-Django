from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import table, tableIncapables
from .forms import tableForm, tableIncapablesForm
from django.views.generic import DetailView, UpdateView, DeleteView


def sia(request):
    lists = table.objects.all()
    lists2 = tableIncapables.objects.all()
    return render(request, 'sick_leave/leaves.html', {'lists': lists, 'lists2': lists2})


class LeaveDetailView(DetailView):
    model = table
    template_name = 'sick_leave/details_view.html'
    context_object_name = 'key_table'


def testfunc(request, pk):
    list1 = table.objects.filter(incapable=pk)
    return render(request, 'sick_leave/test.html', {'list1': list1})


class IncapablesDetailView(DetailView):
    model = tableIncapables
    template_name = 'sick_leave/details_view_incapable.html'
    context_object_name = 'incapable_table'


class DetailUpdateView(UpdateView):
    model = table
    template_name = 'sick_leave/create.html'
    form_class = tableForm


class DetailIncapableUpdateView(UpdateView):
    model = tableIncapables
    template_name = 'sick_leave/edit_incapable.html'
    form_class = tableIncapablesForm


class DetailDeleteView(DeleteView):
    model = table
    template_name = 'sick_leave/delete.html'
    success_url = '/sick_leave'


class DetailIncapableDeleteView(DeleteView):
    model = tableIncapables
    template_name = 'sick_leave/delete.html'
    success_url = '/sick_leave/incapable'


def create(request):
    error = ''
    if request.method == 'POST':
        form = tableForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sick_leaves')
        else:
            error = 'Form is uncorrect'

    form = tableForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'sick_leave/create.html', data)


def infoIncapables(request):
    lists1 = tableIncapables.objects.all()
    lists2 = tableIncapables.objects.all()
    return render(request, 'sick_leave/incapables.html', {'lists1': lists1, 'lists2': lists2})


def createIncapable(request):
    error = ''
    if request.method == 'POST':
        form = tableIncapablesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('incapable')
        else:
            error = 'Form is uncorrect'

    form = tableIncapablesForm()
    data = {
        'form': form,
        'error1': error
    }
    return render(request, 'sick_leave/createPerson.html', data)


