from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import View

from catalog.models import Tag, Task
from catalog.forms import TaskForm


class IndexView(generic.ListView):
    model = Task
    context_object_name = "task_list"
    template_name = "catalog/index.html"
    queryset = Task.objects.all()


class TagListView(generic.ListView):
    model = Tag
    template_name = "catalog/tag_list.html"
    queryset = Tag.objects.all()


class TagCreateView(generic.CreateView):
    model = Tag
    fields = "__all__"
    template_name = "catalog/tag_form.html"
    success_url = reverse_lazy("catalog:tag-list")


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = "__all__"
    template_name = "catalog/tag_form.html"
    success_url = reverse_lazy("catalog:tag-list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    template_name = "catalog/tag_confirm_delete.html"
    success_url = reverse_lazy("catalog:tag-list")


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm
    template_name = "catalog/task_form.html"
    success_url = reverse_lazy("catalog:index")


class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskForm
    template_name = "catalog/task_form.html"
    success_url = reverse_lazy("catalog:index")


class TaskDeleteView(generic.DeleteView):
    model = Task
    template_name = "catalog/task_confirm_delete.html"
    success_url = reverse_lazy("catalog:index")


class ToggleCompleteUndo(View):
    def post(self, request, *args, **kwargs):
        task = Task.objects.get(id=kwargs["pk"])
        if task.status:
            task.status = False
            task.save()
        elif not task.status:
            task.status = True
            task.save()
        return HttpResponseRedirect(reverse_lazy("catalog:index"))
