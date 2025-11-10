from django.views.generic.base import TemplateView

class IndexView(TemplateView):
    template_name = 'seisaku/index.html'

class AboutView(TemplateView):
    template_name = "seisaku/about.html"

class PostView(TemplateView):
    template_name = "seisaku/post.html"

class ContactView(TemplateView):
    template_name = "seisaku/contact.html"