from django.contrib import admin
from django.db.models import Sum

from . import models


class GlobalAdminMixin(admin.ModelAdmin):
    def get_fields(self, request, obj=None):
        fields = super().get_fields(request, obj)
        for f in ["description", "is_active"]:
            if f in fields:
                fields.remove(f)
                fields.append(f)
        return fields


@admin.register(models.Kharj)
class KharjAdmin(GlobalAdminMixin):
    list_display = ["id", "str_display"]
    list_display_links = list_display
    filter_horizontal = ["type"]
    list_filter = ["type", "day_of_month", "month", "year"]
    search_fields = ["title", "day_of_month", "month", "year", "price"]

    def str_display(self, obj):
        return str(obj)

    str_display.short_description = "نمایش خرج"

    def changelist_view(self, request, extra_context=None):
        response = super().changelist_view(request, extra_context=extra_context)
        try:
            queryset = response.context_data["cl"].queryset
            total_price = queryset.aggregate(total=Sum("price"))["total"] or 0
            response.context_data["summary_total"] = total_price
        except (AttributeError, KeyError):
            return response
        return response


@admin.register(models.KharjType)
class KharjTypeAdmin(GlobalAdminMixin):
    list_display = ["id", "title", "code"]
    list_display_links = list_display


@admin.register(models.MoneyHolder)
class MoneyHolderAdmin(GlobalAdminMixin):
    list_display = ["id", "title", "balance"]
    list_display_links = list_display
    list_filter = ["title"]
    search_fields = ["title", "balance"]

    def changelist_view(self, request, extra_context=None):
        response = super().changelist_view(request, extra_context=extra_context)
        try:
            queryset = response.context_data["cl"].queryset
            total_balance = queryset.aggregate(total=Sum("balance"))["total"] or 0
            response.context_data["summary_total"] = total_balance
        except (AttributeError, KeyError):
            return response
        return response


@admin.register(models.Income)
class IncomeAdmin(GlobalAdminMixin):
    list_display = ["id", "title", "amount"]
    list_display_links = list_display
    list_filter = ["title"]
    search_fields = ["title", "amount"]

    def changelist_view(self, request, extra_context=None):
        response = super().changelist_view(request, extra_context=extra_context)
        try:
            queryset = response.context_data["cl"].queryset
            total_amount = queryset.aggregate(total=Sum("amount"))["total"] or 0
            response.context_data["summary_total"] = total_amount
        except (AttributeError, KeyError):
            return response
        return response


@admin.register(models.LentFrom)
class LentFromAdmin(GlobalAdminMixin):
    list_display = ["id", "title", "amount"]
    list_display_links = list_display
    list_filter = ["title"]
    search_fields = ["title", "amount"]

    def changelist_view(self, request, extra_context=None):
        response = super().changelist_view(request, extra_context=extra_context)
        try:
            queryset = response.context_data["cl"].queryset
            total_amount = queryset.aggregate(total=Sum("amount"))["total"] or 0
            response.context_data["summary_total"] = total_amount
        except (AttributeError, KeyError):
            return response
        return response


@admin.register(models.LentTo)
class LentToAdmin(GlobalAdminMixin):
    list_display = ["id", "title", "amount"]
    list_display_links = list_display
    list_filter = ["title"]
    search_fields = ["title", "amount"]

    def changelist_view(self, request, extra_context=None):
        response = super().changelist_view(request, extra_context=extra_context)
        try:
            queryset = response.context_data["cl"].queryset
            total_amount = queryset.aggregate(total=Sum("amount"))["total"] or 0
            response.context_data["summary_total"] = total_amount
        except (AttributeError, KeyError):
            return response
        return response


@admin.register(models.ReminderLents)
class ReminderLentsAdmin(GlobalAdminMixin):
    list_display = ["id", "title", "amount"]
    list_display_links = list_display
    list_filter = ["title"]
    search_fields = ["title", "amount"]

    def changelist_view(self, request, extra_context=None):
        response = super().changelist_view(request, extra_context=extra_context)
        try:
            queryset = response.context_data["cl"].queryset
            total_amount = queryset.aggregate(total=Sum("amount"))["total"] or 0
            response.context_data["summary_total"] = total_amount
        except (AttributeError, KeyError):
            return response
        return response
