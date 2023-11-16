from django.views import View
from django.shortcuts import render
from bs4 import BeautifulSoup


class ExternalSiteProxyView(View):
    template_name = 'site_proxy/external_site_proxy.html'

    def get(self, request, user_site_name, original_routes):
        try:
            internal_page_path = 'site_proxy/internal_page.html'
            response = render(request, internal_page_path, {'user_site_name': user_site_name,
                                                            'original_routes': original_routes})
            content = response.content.decode('utf-8')
            content = self.replace_links(content, user_site_name, original_routes)
            return render(request, self.template_name, {'content': content})

        except Exception as e:
            return render(request, self.template_name, {'content': f"Error: {e}"})

    def replace_links(self, content, user_site_name, original_routes):
        soup = BeautifulSoup(content, 'html.parser')

        for tag in soup.find_all(['a', 'link', 'script']):
            if 'href' in tag.attrs and not tag['href'].startswith(('http:', 'https:')):
                tag['href'] = f'/site_proxy/external_site_proxy/{user_site_name}/{original_routes}/{tag["href"]}'

            elif 'src' in tag.attrs and not tag['src'].startswith(('http:', 'https:')):
                tag['src'] = f'/site_proxy/external_site_proxy/{user_site_name}/{original_routes}/{tag["src"]}'

        return str(soup)

