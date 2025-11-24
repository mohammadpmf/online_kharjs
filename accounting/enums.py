from django.db import models


class MONTHS(models.IntegerChoices):
    FARVARDIN = 1, "فروردین"
    ORDIBEHESHT = 2, "اردیبهشت"
    KHORDAD = 3, "خرداد"
    TIR = 4, "تیر"
    MORDAD = 5, "مرداد"
    SHAHRIVAR = 6, "شهریور"
    MEHR = 7, "مهر"
    ABAN = 8, "آبان"
    AZAR = 9, "آذر"
    DEY = 10, "دی"
    BAHMAN = 11, "بهمن"
    ESFAND = 12, "اسفند"


class DAYS_OF_WEEK(models.IntegerChoices):
    SATURDAY = 1, "شنبه"
    SUNDAY = 2, "یکشنبه"
    MONDAY = 3, "دوشنبه"
    TUESDAY = 4, "سه‌شنبه"
    WEDNESDAY = 5, "چهارشنبه"
    THURSDAY = 6, "پنجشنبه"
    FRIDAY = 7, "جمعه"
