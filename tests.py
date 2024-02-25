from main import BooksCollector
import pytest
class TestBooksCollector:

    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        assert len(collector.books_genre) == 2

    def test_add_new_book_name_exceeds_41_characters(self):
        collector = BooksCollector()

        collector.add_new_book('Слишком длинное имя книги, чтобы проходило проверку')

        assert 'Слишком длинное имя книги, чтобы проходило проверку' not in collector.books_genre

    def test_set_book_genre_book_and_genre_specified(self):
        collector = BooksCollector()

        collector.add_new_book('Солярис')
        collector.set_book_genre('Солярис', 'Фантастика')
        assert collector.books_genre['Солярис'] == 'Фантастика'

    def test_set_book_genre_book_not_defined(self):
        collector = BooksCollector()

        collector.set_book_genre('Дракула', 'Ужасы')

        assert 'Дракула' not in collector.books_genre


    def test_set_book_genre_genre_not_existing(self):
        collector = BooksCollector()

        collector.add_new_book('Дон Кихот')
        collector.set_book_genre('Дон Кихот', 'Роман')

        assert 'Роман' not in collector.books_genre

    def test_get_book_genre(self):
        collector = BooksCollector()

        collector.add_new_book('Хирург')
        collector.set_book_genre('Хирург', 'Детективы')

        assert collector.get_book_genre('Хирург') == 'Детективы'

    def test_get_books_with_specific_genre(self):
        collector = BooksCollector()

        collector.add_new_book('Сияние')
        collector.set_book_genre('Сияние', 'Ужасы')

        assert collector.get_books_with_specific_genre('Ужасы') == ['Сияние']


    def test_get_books_genre_returns_full_list(self):
        collector = BooksCollector()

        collector.add_new_book('Сияние')
        collector.set_book_genre('Сияние','Ужасы')
        collector.add_new_book('Хирург')
        collector.set_book_genre('Хирург', 'Детективы')

        assert collector.books_genre == {'Сияние': 'Ужасы', 'Хирург': 'Детективы'}


    def test_get_books_for_children_book_appended_in_books_for_children(self):
        collector = BooksCollector()

        collector.add_new_book('Маша и медведи')
        collector.set_book_genre('Маша и медведи', 'Мультфильмы')

        assert 'Маша и медведи' in collector.get_books_for_children()

    def test_get_books_for_children_book_not_appended_in_books_for_children(self):
        collector = BooksCollector()

        collector.add_new_book('Сияние')
        collector.set_book_genre('Сияние', 'Ужасы')

        assert 'Сияние' not in collector.get_books_for_children()

    def test_book_in_favourites_check_added_in_favourites(self):
        collector = BooksCollector()

        collector.add_new_book('Этюд в багровых тонах')
        collector.add_book_in_favorites('Этюд в багровых тонах')

        assert 'Этюд в багровых тонах' in collector.favorites

    def test_delete_book_from_favorites_check_deleted_from_favourites(self):
        collector = BooksCollector()

        collector.add_new_book('Этюд в багровых тонах')
        collector.add_book_in_favorites('Этюд в багровых тонах')
        collector.delete_book_from_favorites('Этюд в багровых тонах')

        assert 'Этюд в багровых тонах' not in collector.favorites

    def test_get_list_of_favorites_books_two_books_added_in_favourites(self):
        collector = BooksCollector()

        collector.add_new_book('Солярис')
        collector.add_book_in_favorites('Солярис')
        collector.add_new_book('Этюд в багровых тонах')
        collector.add_book_in_favorites('Этюд в багровых тонах')

        assert collector.favorites == ['Солярис', 'Этюд в багровых тонах']

