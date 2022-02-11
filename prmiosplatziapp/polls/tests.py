import datetime
from django.utils import timezone
from django.test import TestCase

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