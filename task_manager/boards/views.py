from django.views.generic import ListView, DetailView
from .models import Board
from django.contrib.auth.mixins import LoginRequiredMixin


class BoardListView(LoginRequiredMixin, ListView):
    model = Board
    template_name = 'board_list.html'
    context_object_name = 'boards'

    def get_queryset(self):
        return self.request.user.boards.all()


class BoardDetailView(LoginRequiredMixin, DetailView):
    model = Board
    template_name = 'board_detail.html'
    context_object_name = 'board'
