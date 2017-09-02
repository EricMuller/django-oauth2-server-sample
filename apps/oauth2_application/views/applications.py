
from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms.models import modelform_factory
from django.views.generic import CreateView, UpdateView

from oauth2_provider.models import get_application_model
from oauth2_provider.views.application import ApplicationOwnerIsUserMixin


class ApplicationRegistration(LoginRequiredMixin, CreateView):
    """
    View used to register a new Application for the request.user
    """
    template_name = "oauth2_provider/application_registration_form.html"

    def get_form_class(self):
        """
        Returns the form class for the application model
        """
        return modelform_factory(
            get_application_model(),
            fields=(
                "name", "client_id", "client_secret", "client_type",
                "authorization_grant_type", "redirect_uris", "url",
                "description", "public",
            )
        )

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(ApplicationRegistration, self).form_valid(form)


class ApplicationUpdate(ApplicationOwnerIsUserMixin, UpdateView):
    """
    View used to update an application owned by the request.user
    """
    context_object_name = "application"
    template_name = "oauth2_provider/application_form.html"

    def get_form_class(self):
        """
        Returns the form class for the application model
        """
        return modelform_factory(
            get_application_model(),
            fields=(
                "name", "client_id", "client_secret", "client_type",
                "authorization_grant_type", "redirect_uris", "url",
                "description", "public",
            )
        )
