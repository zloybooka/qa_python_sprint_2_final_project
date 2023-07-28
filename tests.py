from main import BooksCollector
import pytest

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    @pytest.mark.parametrize('book, genre', [['Гордость предубеждение и зомби', 'Ужасы'], ['Оно', 'Ужасы'], ['Пробуждение Ктулху', 'Ужасы'],
                                             ['Фламандская доска', 'Детективы']])
    def test_set_book_genre_and_get_it(self, book, genre):
        collector = BooksCollector()
        collector.add_new_book(book)

        collector.set_book_genre(book, genre)

        assert collector.get_book_genre(book) == genre

    def test_get_books_with_specific_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость предубеждение и зомби')
        collector.add_new_book('Оно')
        collector.add_new_book('Пробуждение Ктулху')
        collector.add_new_book('Фламандская доска')

        collector.set_book_genre('Гордость предубеждение и зомби', 'Ужасы')
        collector.set_book_genre('Оно', 'Ужасы')
        collector.set_book_genre('Пробуждение Ктулху', 'Ужасы')
        collector.set_book_genre('Фламандская доска', 'Детективы')

        assert collector.get_books_with_specific_genre('Ужасы') == ['Гордость предубеждение и зомби', 'Оно', 'Пробуждение Ктулху']

    def test_get_books_genre(self):
        collector = BooksCollector()

        collector.add_new_book('Гордость предубеждение и зомби')
        collector.add_new_book('Солярис')
        collector.add_new_book('Алиса в стране чудес')
        collector.add_new_book('Фламандская доска')

        collector.set_book_genre('Гордость предубеждение и зомби', 'Ужасы')
        collector.set_book_genre('Солярис', 'Фантастика')
        collector.set_book_genre('Алиса в стране чудес', 'Мультфильмы')
        collector.set_book_genre('Фламандская доска', 'Детективы')

        assert collector.get_books_genre() == {'Гордость предубеждение и зомби': 'Ужасы',
                                               'Солярис': 'Фантастика',
                                               'Алиса в стране чудес': 'Мультфильмы',
                                               'Фламандская доска': 'Детективы'
                                               }

    def test_get_book_for_children(self):
        collector = BooksCollector()

        collector.add_new_book('Гордость предубеждение и зомби')
        collector.add_new_book('Солярис')
        collector.add_new_book('Алиса в стране чудес')
        collector.add_new_book('Фламандская доска')

        collector.set_book_genre('Гордость предубеждение и зомби', 'Ужасы')
        collector.set_book_genre('Солярис', 'Фантастика')
        collector.set_book_genre('Алиса в стране чудес', 'Мультфильмы')
        collector.set_book_genre('Фламандская доска', 'Детективы')

        assert collector.get_books_for_children() == ['Солярис', 'Алиса в стране чудес']

    def test_add_book_in_favorites_and_get_it(self):
        collector = BooksCollector()

        collector.add_new_book('Гордость предубеждение и зомби')
        collector.add_new_book('Солярис')
        collector.add_new_book('Алиса в стране чудес')
        collector.add_new_book('Фламандская доска')

        collector.set_book_genre('Гордость предубеждение и зомби', 'Ужасы')
        collector.set_book_genre('Солярис', 'Фантастика')
        collector.set_book_genre('Алиса в стране чудес', 'Мультфильмы')
        collector.set_book_genre('Фламандская доска', 'Детективы')

        collector.add_book_in_favorites('Фламандская доска')
        collector.add_book_in_favorites('Алиса в стране чудес')

        assert collector.get_list_of_favorites_books() == ['Фламандская доска', 'Алиса в стране чудес']

    def test_add_book_in_favorites_remove_part_of_it_and_get_list(self):
        collector = BooksCollector()

        collector.add_new_book('Гордость предубеждение и зомби')
        collector.add_new_book('Солярис')
        collector.add_new_book('Алиса в стране чудес')
        collector.add_new_book('Фламандская доска')

        collector.set_book_genre('Гордость предубеждение и зомби', 'Ужасы')
        collector.set_book_genre('Солярис', 'Фантастика')
        collector.set_book_genre('Алиса в стране чудес', 'Мультфильмы')
        collector.set_book_genre('Фламандская доска', 'Детективы')

        collector.add_book_in_favorites('Фламандская доска')
        collector.add_book_in_favorites('Алиса в стране чудес')
        collector.add_book_in_favorites('Солярис')

        collector.delete_book_from_favorites('Солярис')
        assert collector.get_list_of_favorites_books() == ['Фламандская доска', 'Алиса в стране чудес']

    def test_check_what_new_book_without_genre(self):
        collector = BooksCollector()

        collector.add_new_book('Гордость предубеждение и зомби')

        assert collector.get_book_genre('Гордость предубеждение и змоби') == None

    def test_change_book_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость предубеждение и зомби')

        collector.set_book_genre('Гордость предубеждение и зомби', 'Ужасы')
        collector.set_book_genre('Гордость предубеждение и зомби', 'Комедии')

        assert collector.get_book_genre('Гордость предубеждение и зомби') == 'Комедии'


