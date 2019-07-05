from django.test import TestCase
from eventex.subscriptions.forms import SubscriptionForm
from django.shortcuts import resolve_url as r


class SubscriptionFormTest(TestCase):
    def test_form_has_fields(self):
        """Form must have 4 fields"""
        expected = ['name', 'cpf', 'email', 'phone']
        form = SubscriptionForm()
        self.assertSequenceEqual(expected, list(form.fields))

    def test_cpf_is_digit(self):
        """CPF must only accept digits."""
        form = self.make_validated_form(cpf='ABCD5678901')
        # self.assertFormErrorMessage(form, 'cpf', 'CPF deve conter apenas números.')
        self.assertFormErrorCode(form, 'cpf', 'digits')

    def test_cpf_has_11_digits(self):
        """CPF must have 11 digits"""
        form = self.make_validated_form(cpf='1234')
        self.assertFormErrorCode(form, 'cpf', 'lenght')

    def test_name_must_be_captalized(self):
        """ Name must be captalized. """
        # FELIPE gomes -> Felipe Gomes
        form = self.make_validated_form(name='FELIPE gomes')
        self.assertEqual('Felipe Gomes', form.cleaned_data['name'])

    def test_email_is_optional(self):
        """Email is optional"""
        form = self.make_validated_form(email='')
        self.assertFalse(form.errors)

    def test_phone_is_optional(self):
        """Phone is optional"""
        form = self.make_validated_form(phone='')
        self.assertFalse(form.errors)

    def test_form_must_inform_email_or_phone(self):
        """Email and Phone are optional, but one must be informed"""
        form = self.make_validated_form(email='', phone='')
        self.assertListEqual(['__all__'], list(form.errors))

    #

    def assertFormErrorCode(self, form, field, code):
        errors = form.errors.as_data()
        errors_list = errors[field]
        exception = errors_list[0]
        self.assertEqual(code, exception.code)

    def assertFormErrorMessage(self, form, field, msg):
        errors = form.errors
        errors_list = errors[field]
        self.assertEqual([msg], errors_list)

    def make_validated_form(self, **kwargs):
        valid_data = dict(name='Felipe Gomes', cpf='12345678901',
                    email='felipe@gomes.com', phone='22-993388001')
        data = dict(valid_data, **kwargs)
        form = SubscriptionForm(data)
        form.is_valid()
        return form

class TestRegressionTest(TestCase):
    def test_template_has_non_field_errors(self):
        invalid_data = dict(name="Felipe Gomes", cpf='12345678901')
        response = self.client.post(r('subscriptions:new'), invalid_data)
        self.assertContains(response, '<ul class="errorlist nonfield">')
