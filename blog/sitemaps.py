from django.contrib.sitemaps import Sitemap
from .models import Post

class PostSitemap(Sitemap): #indicate the change frequency of your post pages and their relevance in your websit
    changefreq = 'weekly'
    priority = 0.9
    
    def items(self):
        return Post.published.all()
    
    def lastmod(self, obj): #corresponds to the post updated date field
        return obj.updated