courses = ["Java-разработчик с нуля", "Fullstack-разработчик на Python", "Python-разработчик с нуля",
           "Frontend-разработчик с нуля"]
mentors = [
    ["Филипп Воронов", "Анна Юшина", "Иван Бочаров", "Анатолий Корсаков", "Юрий Пеньков", "Илья Сухачев",
     "Иван Маркитан", "Ринат Бибиков", "Вадим Ерошевичев", "Тимур Сейсембаев", "Максим Батырев", "Никита Шумский",
     "Алексей Степанов", "Денис Коротков", "Антон Глушков", "Сергей Индюков", "Максим Воронцов", "Евгений Грязнов",
     "Константин Виролайнен", "Сергей Сердюк", "Павел Дерендяев"],
    ["Евгений Шмаргунов", "Олег Булыгин", "Александр Бардин", "Александр Иванов", "Кирилл Табельский",
     "Александр Ульянцев", "Роман Гордиенко", "Адилет Асканжоев", "Александр Шлейко", "Алена Батицкая", "Денис Ежков",
     "Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Максим Филипенко", "Елена Никитина"],
    ["Евгений Шмаргунов", "Олег Булыгин", "Дмитрий Демидов", "Кирилл Табельский", "Александр Ульянцев",
     "Александр Бардин", "Александр Иванов", "Антон Солонилин", "Максим Филипенко", "Елена Никитина", "Азамат Искаков",
     "Роман Гордиенко"],
    ["Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Валерий Хаслер", "Татьяна Тен", "Александр Фитискин",
     "Александр Шлейко", "Алена Батицкая", "Александр Беспоясов", "Денис Ежков", "Николай Лопин", "Михаил Ларченко"]
]
durations = [14, 20, 12, 20]


def get_durations() -> list[str]:
    courses_list = []
    for course, mentor, duration in zip(courses, mentors, durations):
        course_dict = {"title": course,
                       "mentors": mentor,
                       "duration": duration}
        courses_list.append(course_dict)

    mins = min(durations)
    maxs = max(durations)

    maxes = []
    minis = []
    for i, time in enumerate(durations):
        if time == maxs:
            maxes.append(i)
        elif time == mins:
            minis.append(i)

    courses_min = []
    courses_max = []
    for id in minis:
        courses_min.append(courses_list[id]['title'])
    for id in maxes:
        courses_max.append(courses_list[id]['title'])

    min_answer = (f'Самый короткий курс(ы): {", ".join(courses_min)} - {mins} месяца(ев)')
    max_answer = (f'Самый длинный курс(ы): {", ".join(courses_max)} - {maxs} месяца(ев)')
    return [min_answer, max_answer]

# Самый короткий курс(ы): Python-разработчик с нуля - 12 месяца(ев)
# Самый длинный курс(ы): Fullstack-разработчик на Python, Frontend-разработчик с нуля - 20 месяца(ев)
