from django.db import models
from django.core.validators import (
    MinValueValidator,
    MaxValueValidator,
)

from accounting.enums import DAYS_OF_WEEK, MONTHS
from accounting.helper_functions import (
    current_shamsi_day_of_month,
    current_shamsi_day_of_week,
    current_shamsi_month,
    current_shamsi_year,
)


class GlobalMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="زمان ایجاد")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="زمان آخرین ویرایش")
    is_active = models.BooleanField(default=True, verbose_name="فعال")
    description = models.TextField(blank=True, verbose_name="توضیحات")

    class Meta:
        abstract = True


class MoneyHolder(GlobalMixin):
    title = models.CharField(max_length=255, verbose_name="نام", unique=True)
    balance = models.DecimalField(
        max_digits=51, decimal_places=1, default=0, verbose_name="باقیمانده"
    )

    def __str__(self):
        return f"{self.title}: {self.balance} تومان"


class KharjType(GlobalMixin):
    title = models.CharField(max_length=255, verbose_name="نوع خرج", unique=True)
    code = models.IntegerField(
        unique=True,
        validators=[
            MinValueValidator(100),
            MaxValueValidator(999),
        ],
        verbose_name="کد خرج",
    )

    def __str__(self):
        return f"{self.title} ({self.code})"


class Kharj(GlobalMixin):
    title = models.CharField(max_length=255, verbose_name="عنوان خرج")
    type = models.ManyToManyField(to=KharjType, verbose_name="نوع خرج")
    day_of_week = models.IntegerField(
        choices=DAYS_OF_WEEK,
        default=current_shamsi_day_of_week,
        verbose_name="روز هفته",
    )
    day_of_month = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(31)],
        default=current_shamsi_day_of_month,
        verbose_name="روز ماه",
    )
    month = models.IntegerField(
        choices=MONTHS, default=current_shamsi_month, verbose_name="ماه"
    )
    year = models.IntegerField(default=current_shamsi_year, verbose_name="سال")
    price = models.DecimalField(
        max_digits=51,
        decimal_places=1,
        validators=[MinValueValidator(0)],
        verbose_name="قیمت",
    )

    def __str__(self):
        return f"{self.title} ({self.price} تومان) ({self.get_day_of_week_display()} {self.day_of_month} {self.get_month_display()} {self.year})"


class Income(GlobalMixin):
    title = models.CharField(max_length=255, verbose_name="مقر درآمد")
    amount = models.DecimalField(
        max_digits=51,
        decimal_places=1,
        validators=[MinValueValidator(0)],
        verbose_name="مقدار درآمد",
    )

    def __str__(self):
        return f"{self.title}: {self.amount} تومان"


class LentFrom(GlobalMixin):
    title = models.CharField(
        max_length=255, verbose_name="شخص یا جایی که ازش قرض گرفتم"
    )
    amount = models.DecimalField(
        max_digits=51,
        decimal_places=1,
        validators=[MinValueValidator(0)],
        verbose_name="مقداری که قرض گرفتم",
    )

    def __str__(self):
        return f"بدهی به: {self.title}: {self.amount} تومان"


class LentTo(GlobalMixin):
    title = models.CharField(max_length=255, verbose_name="شخص یا جایی که بهش قرض دادم")
    amount = models.DecimalField(
        max_digits=51,
        decimal_places=1,
        validators=[MinValueValidator(0)],
        verbose_name="مقداری که قرض دادم",
    )

    def __str__(self):
        return f"طلب از: {self.title}: {self.amount} تومان"


class ReminderLents(GlobalMixin):
    title = models.CharField(max_length=255, verbose_name="مورد")
    amount = models.DecimalField(
        max_digits=51,
        decimal_places=1,
        validators=[MinValueValidator(0)],
        verbose_name="مقداری که قرض دادم",
    )

    def __str__(self):
        return f"یادآور طلب: {self.title}: {self.amount} تومان"
