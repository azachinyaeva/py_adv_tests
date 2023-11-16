from Homework_duration import courses, mentors, durations, get_durations
from Homework_unique_names import get_names
from Homework_sorted_duration import get_sorted_durations
import pytest


@pytest.mark.parametrize("names", "Уникальные имена преподавателей: Адилет, Азамат, Александр, Алексей, Алена, Анатолий, Анна, "
                                  "Антон, Вадим, Валерий, Владимир, Денис, Дмитрий, Евгений, Елена, Иван, Илья, Кирилл, "
                                  "Константин, Максим, Михаил, Никита, Николай, Олег, Павел, Ринат, Роман, Сергей, Татьяна, "
                                  "Тимур, Филипп, Эдгар, Юрий")
class TestHomeworkNames:
    def test_names(self, names):
        result = get_names()
        assert(names, result)


@pytest.mark.parametrize("minmaxcourses", ['Самый короткий курс(ы): Python-разработчик с нуля - 12 месяца(ев)',
                                           'Самый длинный курс(ы): Fullstack-разработчик на Python, '
                                           'Frontend-разработчик с нуля - 20 месяца(ев)'])
class TestDuration:
    def test_duration(self, minmaxcourses):
        result = get_durations()
        assert(minmaxcourses, result)


@pytest.mark.parametrize("sorted_duration", ['Python-разработчик с нуля - 12 месяцев', 'Java-разработчик с нуля - 14 месяцев',
                                             'Fullstack-разработчик на Python - 20 месяцев', 'Frontend-разработчик с нуля - 20 месяцев'])
class TestSortedDuration:
    def test_sorted_duration(self, sorted_duration):
        result = get_sorted_durations()
        assert(sorted_duration, result)
