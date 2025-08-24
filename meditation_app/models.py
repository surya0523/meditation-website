# from django.db import models

# class Therapy(models.Model):
#     title = models.CharField(max_length=200)
#     description = models.TextField()
#     # Change from CharField to ImageField
#     image = models.ImageField(upload_to='therapies/') 
    
#     def __str__(self):
#         return self.title

# class TeamMember(models.Model):
#     name = models.CharField(max_length=100)
#     title = models.CharField(max_length=100)
#     # Change from CharField to ImageField
#     image = models.ImageField(upload_to='team/') 
    
#     def __str__(self):
#         return self.name

# class Testimonial(models.Model):
#     client_name = models.CharField(max_length=100)
#     testimonial_text = models.TextField()
#     # Change from CharField to ImageField
#     client_image = models.ImageField(upload_to='testimonials/')
    
#     def __str__(self):
#         return f'Testimonial by {self.client_name}'

# class FAQ(models.Model):
#     question = models.CharField(max_length=255)
#     answer = models.TextField()
    
#     def __str__(self):
#         return self.question

# class Article(models.Model):
#     title = models.CharField(max_length=200)
#     date = models.DateField()
#     image = models.ImageField(upload_to='articles/')
#     content = models.TextField()
    
#     def __str__(self):
#         return self.title


# # வெவ்வேறு வகையான சேவைகளை சேமிக்க
# class Service(models.Model):
#     service_name = models.CharField(max_length=100)
#     service_image = models.ImageField(upload_to='services/')

#     def __str__(self):
#         return self.service_name

# # ஒவ்வொரு சேவையின் விரிவான பக்கத்திற்கும் தகவலை சேமிக்க
# # class ServiceDetail(models.Model):
# #     service = models.OneToOneField(Service, on_delete=models.CASCADE)
# #     title = models.CharField(max_length=200)
# #     description = models.TextField()
# #     image = models.ImageField(upload_to='service_details/')

# #     def __str__(self):
# #         return f"Detail for {self.service.service_name}"

# # ஒவ்வொரு விரிவான பக்கத்திலும் உள்ள கட்டுரைகளை சேமிக்க
# # class Article(models.Model):
# #     service_detail = models.ForeignKey(ServiceDetail, on_delete=models.CASCADE, related_name='articles')
# #     title = models.CharField(max_length=255)
# #     description = models.TextField()
# #     image = models.ImageField(upload_to='articles/')

# #     def __str__(self):
# #         return self.title
    
from django.db import models

class Therapy(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='therapies/') 
    
    def __str__(self):
        return self.title

class TeamMember(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='team/') 
    
    def __str__(self):
        return self.name

class Testimonial(models.Model):
    client_name = models.CharField(max_length=100)
    testimonial_text = models.TextField()
    client_image = models.ImageField(upload_to='testimonials/')
    
    def __str__(self):
        return f'Testimonial by {self.client_name}'

class FAQ(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()
    
    def __str__(self):
        return self.question

# General Blog/News Article
class Article(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    image = models.ImageField(upload_to='articles/')
    content = models.TextField()
    
    def __str__(self):
        return self.title

# வெவ்வேறு வகையான சேவைகளை சேமிக்க
class Service(models.Model):
    service_name = models.CharField(max_length=100)
    service_image = models.ImageField(upload_to='services/')

    def __str__(self):
        return self.service_name

# ஒவ்வொரு சேவையின் விரிவான பக்கத்திற்கும் தகவலை சேமிக்க
class ServiceDetail(models.Model):
    service = models.OneToOneField(Service, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='service_details/')

    def __str__(self):
        return f"Detail for {self.service.service_name}"

# ஒவ்வொரு விரிவான பக்கத்திலும் உள்ள கட்டுரைகளை சேமிக்க
class ServiceArticle(models.Model):
    service_detail = models.ForeignKey(ServiceDetail, on_delete=models.CASCADE, related_name='articles')
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='articles/')

    def __str__(self):
        return self.title



class FamilyTherapyArticle(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='family_therapy_articles/')
    reviewer = models.CharField(max_length=100, help_text="Medically reviewed by...")

    def __str__(self):
        return self.title
    

# பொதுவான சிகிச்சை கட்டுரைகளுக்கான புதிய மாடல்
class TherapyArticle(models.Model):
    # சிகிச்சை வகையை அடையாளம் காண field
    therapy_type = models.CharField(max_length=50, choices=[
        ('Individual', 'Individual Therapy'),
        ('Couples', 'Couples Therapy'),
        ('Online', 'Online Therapy'),
        ('Group', 'Group Therapy'),
    ])
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='therapy_articles/')
    reviewer = models.CharField(max_length=100, help_text="Medically reviewed by...")

    def __str__(self):
        return f"{self.therapy_type} - {self.title}"
    

# படிவத் தரவைச் சேமிப்பதற்கான புதிய மாதிரி (New model for saving form data)
class ApproachFormEntry(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    mobile_no = models.CharField(max_length=15)
    email_id = models.EmailField()
    no_of_therapy_day = models.IntegerField()
    family_members_count = models.IntegerField()
    address = models.TextField()
    time_availability = models.CharField(max_length=50)
    city = models.CharField(max_length=100)
    submitted_at = models.DateTimeField(auto_now_add=True) # படிவம் சமர்ப்பிக்கப்பட்ட நேரத்தைக் குறிக்க

    def __str__(self):
        return f'{self.first_name} {self.last_name} - {self.submitted_at}'    