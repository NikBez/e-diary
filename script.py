from datacenter.models import Mark, Chastisement, Lesson, Schoolkid, Commendation, Subject
from random import choice

COMMENDATION_TEXT = [
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

def fix_marks(schoolkid):

    kid = get_schoolkid(schoolkid)
    Mark.objects.filter(schoolkid = kid, points__lte=3).update(points=5)
    print("All done")

def remove_chastisements(schoolkid):

    kid = get_schoolkid(schoolkid)
    Chastisement.objects.filter(schoolkid=kid).delete()
    print("All done")

def create_commendations(schoolkid, subject_to_commendate):

    kid = get_schoolkid(schoolkid)
    subject_title = get_subject(subject_to_commendate)
    lesson = Lesson.objects.filter(year_of_study=6, group_letter="А", subject__title=subject_title).order_by("-date").first()
    Commendation.objects.create(text=choice(COMMENDATION_TEXT),
                                created=lesson.date, schoolkid=kid,
                                subject=lesson.subject,
                                teacher=lesson.teacher
                                )
    print("All done")


def get_schoolkid(schoolkid):
    try:
        return Schoolkid.objects.get(full_name__contains=schoolkid)
    except Schoolkid.DoesNotExist:
        print(f'Учеников по запросу "{schoolkid}" не найдено')
    except Schoolkid.MultipleObjectsReturned:
        print(f' Найдено несколько учеников по запросу "{schoolkid}"')


def get_subject(subject_title):
    try:
        return Subject.objects.get(title=subject_title)
    except Subject.DoesNotExist:
        print(f'Предмета по запросу "{subject_title}" не найдено')
    except Subject.MultipleObjectsReturned:
        print(f' Найдено несколько предметов по запросу "{subject_title}"')

