from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from oauth2_provider.models import get_application_model


class HomePage(generic.TemplateView):
    template_name = "home.html"


class AboutPage(generic.TemplateView):
    template_name = "about.html"


class ApplicationsPage(generic.TemplateView):
    template_name = "about.html"


class AboutPageView(generic.ListView):
    """
    Show a page where the current logged-in user
    """
    template_name = "about.html"
    model = get_application_model()

    def get_queryset(self):
        """
        Show only public application
        """
        return super(AboutPageView, self).get_queryset()\
            .filter(public=True)
