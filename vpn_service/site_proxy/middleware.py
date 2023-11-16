from web_sites.models import SiteStatistics


class StatisticsMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        if request.path.startswith('/site_proxy/external_site_proxy/'):
            user = request.user.userprofile
            site_name = request.path.split('/')[3]
            print(site_name)
            data_sent = response.content.__sizeof__()

            site_stat, created = SiteStatistics.objects.get_or_create(user=user, site_name=site_name)

            if created:
                site_stat.clicks = 0
                site_stat.data_sent = 0
                site_stat.data_received = 0

            content_length = request.META.get('CONTENT_LENGTH', '')
            data_received = int(content_length) if content_length else 0

            site_stat.clicks += 1
            site_stat.data_sent += data_sent
            site_stat.data_received += data_received
            site_stat.save()

        return response


