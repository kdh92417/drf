from django.contrib import admin
from news.models    import Article, Journalist, JobOffer

admin.site.register(Article)
admin.site.register(Journalist)
admin.site.register(JobOffer)