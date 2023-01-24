from datacenter.models import *
from random import choice
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned


def fix_marks(schoolkid):

    kid = get_schoolkit(schoolkid)
    bad_marks = Mark.objects.filter(schoolkid = kid, points__lte=3)
    for mark in bad_marks:
        mark.points = 5
        mark.save()
    print("All done")

def remove_chastisements(schoolkid):

    kid = get_schoolkit(schoolkid)
    chastisements = Chastisement.objects.filter(schoolkid=kid)
    for chais in chastisements:
        chais.delete()
    print("All done")


def create_commendations(schoolkid, subject_to_commendate):

    commendation_text=[
        "Гораздо лучше, чем я ожидал!",
        "Ты меня приятно удивил!",
        "Великолепно!",
        "Ты меня очень обрадовал!",
        "Именно этого я давно ждал от тебя!",
        "Сказано здорово – просто и ясно!",
        "Ты, как всегда, точен!",
        "Ты сегодня прыгнул выше головы!",
        "С каждым разом у тебя получается всё лучше!",
    ]

    kid = get_schoolkit(schoolkid)
    lesson = Lesson.objects.filter(year_of_study=6, group_letter="А", subject__title=subject_to_commendate).order_by("date").first()
    Commendation.objects.create(text=choice(commendation_text),
                                created=lesson.date, schoolkid=kid,
                                subject=lesson.subject,
                                teacher=lesson.teacher
                                )
    print("All done")


def get_schoolkit(schoolkid):

    try:
        return Schoolkid.objects.get(full_name__contains=schoolkid)
    except ObjectDoesNotExist:
        print(f'Учеников по запросу "{schoolkid}" не найдено')
    except MultipleObjectsReturned:
        print(f' Найдено несколько учеников по запросу "{schoolkid}"')





