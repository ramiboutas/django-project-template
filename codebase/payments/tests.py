from django.test import RequestFactory

from config.test import TestCase
from core.factories.users import UserFactory
from plans import create_stripe_session
from plans.factories import PremiumPlanFactory


class StripeSessionTests(TestCase):
    def test_create_stripe_session(self):
        plan = PremiumPlanFactory()
        request = RequestFactory().get(plan.checkout_url)
        request.user = UserFactory()
        session = create_stripe_session(request, plan=plan)
        self.assertTrue("checkout.stripe.com" in session["url"])
