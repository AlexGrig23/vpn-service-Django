from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.utils.decorators import method_decorator

from django.views.generic import CreateView, ListView, DetailView


from web_sites.forms import WebSiteForm
from web_sites.models import SiteStatistics, WebSite


@method_decorator(login_required, name='dispatch')
class WebSiteDetailView(DetailView):
    model = WebSite
    template_name = 'web_sites/detail_web_site.html'
    context_object_name = 'web_site'

    def get_queryset(self):
        return WebSite.objects.filter(user=self.request.user.userprofile)

    def get_object(self, queryset=None):
        site_id = self.kwargs.get('site_id')
        return get_object_or_404(WebSite, id=site_id)


class WebSiteCreateView(CreateView):
    form_class = WebSiteForm
    template_name = 'web_sites/create_web_site.html'

    def form_valid(self, form):
        try:
            form.instance.user = self.request.user.userprofile
            response = super().form_valid(form)

            SiteStatistics.objects.create(
                user=self.request.user.userprofile,
                site=form.instance,
                site_name=form.instance.title
            )

            print("Site created successfully!")
            return response
        except Exception as e:
            print("Error creating site:", e)
            return super().form_invalid(form)

    def get_success_url(self):
        return reverse('web_sites:detail_web_site', args=[self.object.id])


class WebSiteStatsView(ListView):
    model = SiteStatistics
    template_name = 'web_sites/statistic.html'
    context_object_name = 'user_sites'

    def get_queryset(self):
        return SiteStatistics.objects.filter(user=self.request.user.userprofile)
