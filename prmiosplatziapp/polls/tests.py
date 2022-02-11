import datetime
from urllib import response
from django.utils import timezone
from django.test import TestCase
from django.urls import reverse

from .models import Question

class QuestionModelTests(TestCase):


    def test_was_published_recently_with_future_questions(self):
        """Was_published_recently returns Flase for questios whose pub_date is in the future"""

        time = timezone.now() + datetime.timedelta(days = 30)
        future_question = Question(question_text="Quien es el mejor course director de platzi",pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)


    def test_was_published_recently_with_past_questions(self):
        """Was_published_recently returns Flase for questios whose pub_date is in the past"""

        time = timezone.now() - datetime.timedelta(days = 30)
        future_question = Question(question_text="Quien es el mejor course director de platzi",pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)

    
    def test_was_published_recently_with_today_questions(self):
        """Was_published_recently returns Flase for questios whose pub_date is test_was_published_recently_with_today_questions"""

        time = timezone.now()
        future_question = Question(question_text="Quien es el mejor course director de platzi",pub_date=time)
        self.assertIs(future_question.was_published_recently(), True)


def create_question(question_text, days):
    """
    Create a question whit the given "question_test", and published the given
    number of days offset to now (nefative for questions published in the past,
    positive for questions that have yet to published)

    """
    time = timezone.now() + datetime.timedelta(days = days)
    return Question.objects.create(question_text=question_text, pub_date=time)


class QuestionIndexViewTests(TestCase):
    def test_no_questions(self):
        """if no question exist, an apropiate message is displayed"""
        response = self.client.get(reverse("polls:index"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No polls are avalible.")
        self.assertQuerysetEqual(response.context["latest_question_list"], [])

    
    def test_view_don_not_show_future_questions(self):
        """
        Questions with a pub_date in the future aren't displayed on the index page
        """
        create_question('future question', days = 30)
        response = self.client.get(reverse('polls:index'))
        self.assertContains(response,"No polls are avalible.")
        self.assertQuerysetEqual(response.context["latest_question_list"], [])


    def test_view_show_past_questions(self):
        """
        Questions with a pub_date in the past displayed on the index page
        """
        question = create_question('past question', days= -10)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(response.context["latest_question_list"], [question])
        