from django.contrib.sitemaps import Sitemap
from e2074.models import Post,Party

class PostSitemap(Sitemap):
    priority = 0.5

    def items(self):
        return Post.objects.all()

    def lastmod(self, obj):
        return obj.posted

class PartySitemap(Sitemap):
    priority = 0.5

    def items(self):
        return Party.objects.all()
