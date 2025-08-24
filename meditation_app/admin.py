# # meditation_app/admin.py
# from django.contrib import admin
# from .models import Therapy, TeamMember, Testimonial,Article, FAQ, Service

# # Register your models here.
# admin.site.register(Therapy)
# admin.site.register(TeamMember)
# admin.site.register(Testimonial)
# admin.site.register(FAQ)
# admin.site.register(Article)

# admin.site.register(Service)


from django.contrib import admin
from .models import Therapy, TeamMember, Testimonial, FAQ, Article, Service, ServiceDetail, ServiceArticle, FamilyTherapyArticle, TherapyArticle, ApproachFormEntry

admin.site.register(Therapy)
admin.site.register(TeamMember)
admin.site.register(Testimonial)
admin.site.register(FAQ)
admin.site.register(Article)
admin.site.register(Service)
admin.site.register(FamilyTherapyArticle)

admin.site.register(TherapyArticle)
admin.site.register(ApproachFormEntry)
# admin.site.register(ServiceDetail)
# admin.site.register(ServiceArticle)
