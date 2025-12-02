from django.views.generic import ListView, TemplateView

from .models import Book


class IndexView(TemplateView):
    template_name = "web/index.html"


class BookListView(ListView):
    model = Book
    template_name = "web/book_list.html"
    context_object_name = "books"

    def get_queryset(self):
        queryset = Book.objects.all()
        start_date = self.request.GET.get("start_date")
        end_date = self.request.GET.get("end_date")

        if start_date:
            queryset = queryset.filter(selled_date__gte=start_date)
        if end_date:
            queryset = queryset.filter(selled_date__lte=end_date)

        return queryset.order_by("selled_date")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["start_date"] = self.request.GET.get("start_date", "")
        context["end_date"] = self.request.GET.get("end_date", "")
        return context
