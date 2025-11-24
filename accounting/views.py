from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import Sum

from accounting.forms import AddKharjForm
from accounting.models import Income, Kharj, LentFrom, LentTo, MoneyHolder


class AllKharjs(LoginRequiredMixin, UserPassesTestMixin, generic.ListView):
    model = Kharj
    template_name = "all_kharjs.html"


class AddKharj(LoginRequiredMixin, UserPassesTestMixin, generic.CreateView):
    model = Kharj
    template_name = "add_kharj.html"
    form_class = AddKharjForm

    def test_func(self):
        user = self.request.user
        return user.is_staff


def balance(request):
    current = MoneyHolder.objects.all().aggregate(total=Sum("balance"))["total"]
    first = MoneyHolder.objects.all().aggregate(total=Sum("balance"))["total"]
    income = Income.objects.all().aggregate(total=Sum("amount"))["total"]
    kharj = Kharj.objects.all().aggregate(total=Sum("price"))["total"]
    lent_from = LentFrom.objects.all().aggregate(total=Sum("amount"))["total"]
    lent_to = LentTo.objects.all().aggregate(total=Sum("amount"))["total"]
    # balance = current - (first + income - kharj + lent_from - lent_to)
    balance = first + income - kharj + lent_from - lent_to
    context = {"balance": balance}
    print(current)
    print(first)
    return render(request, "balance.html", context)
