from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponse
from .models import Article, Testimonial, TeamMember, FAQ, Service, Therapy, ServiceDetail, ServiceArticle, FamilyTherapyArticle, TherapyArticle, ApproachFormEntry


# You would replace this with actual database queries in a real application.
dummy_data = [
    {'title': 'Mindful Meditation', 'content': 'Learn to calm your mind with this guided session.', 'page': 'meditation'},
    {'title': 'Cognitive Behavioral Therapy', 'content': 'Explore our therapy options for anxiety and stress.', 'page': 'therapy'},
    {'title': 'About DEE PLUS', 'content': 'Find out more about our mission and team.', 'page': 'about'},
    {'title': 'Contact Us', 'content': 'Get in touch with us for any inquiries.', 'page': 'contact'},
    {'title': 'Sleep Meditation', 'content': 'A featured meditation to help you get a good night\'s rest.', 'page': 'meditation'},
]

def home(request):
    articles = Article.objects.all().order_by('-date')
    testimonials = Testimonial.objects.all()
    team_members = TeamMember.objects.all()
    faqs = FAQ.objects.all()
    services = Service.objects.all()

    context = {
        'articles': articles,
        'testimonials': testimonials,
        'team_members': team_members,
        'faqs': faqs,
        'services': services,
    }
    return render(request, 'meditation_app/home.html', context)

def therapy_page(request):
    try:
        therapy_content = Therapy.objects.get(pk=1)
    except Therapy.DoesNotExist:
        therapy_content = None

    services = Service.objects.all()

    context = {
        'therapy_content': therapy_content,
        'services': services,
    }
    return render(request, 'meditation_app/therapy.html', context)

def service_detail(request, service_id):
    service = get_object_or_404(Service, pk=service_id)
    service_detail_content = get_object_or_404(ServiceDetail, service=service)
    articles = service_detail_content.articles.all()

    context = {
        'service_detail_content': service_detail_content,
        'articles': articles,
    }
    return render(request, 'meditation_app/service_detail.html', context)


def family_therapy(request):
    # FamilyTherapyArticle மாடலில் இருந்து அனைத்து தரவையும் பெறவும்
    articles = FamilyTherapyArticle.objects.all()
    context = {
        'articles': articles
    }
    return render(request, 'meditation_app/family_therapy.html', context)


# தனிப்பட்ட சிகிச்சைக்கான view
def individual_therapy(request):
    articles = TherapyArticle.objects.filter(therapy_type='Individual')
    context = {
        'articles': articles,
        'page_title': "Individual Therapy"
    }
    return render(request, 'meditation_app/therapy_template.html', context)

# ஜோடி சிகிச்சைக்கான view
def couples_therapy(request):
    articles = TherapyArticle.objects.filter(therapy_type='Couples')
    context = {
        'articles': articles,
        'page_title': "Couples Therapy"
    }
    return render(request, 'meditation_app/therapy_template.html', context)

# ஆன்லைன் சிகிச்சைக்கான view
def online_therapy(request):
    articles = TherapyArticle.objects.filter(therapy_type='Online')
    context = {
        'articles': articles,
        'page_title': "Online Therapy"
    }
    return render(request, 'meditation_app/therapy_template.html', context)

# குழு சிகிச்சைக்கான view
def group_therapy(request):
    articles = TherapyArticle.objects.filter(therapy_type='Group')
    context = {
        'articles': articles,
        'page_title': "Group Therapy"
    }
    return render(request, 'meditation_app/therapy_template.html', context)


def submit_approach_form(request):
    """
    Submits the approach form. It redirects back to the form page to show the pop-up.
    The actual form data will not be saved at this stage.
    """
    if request.method == 'POST':
        # Temporarily storing form data in session or cache if needed for later use
        # For this example, we'll redirect back to the form page with a query parameter
        return redirect('meditation_app:approach_form') + '?show_popup=true'
    
    return redirect('home')

def approach_form_view(request):
    """
    Renders the approach form page.
    """
    return render(request, 'meditation_app/Approach_form.html')

def payment_view(request):
    return render(request, 'meditation_app/payment.html')

def about_view(request):
    return render(request, 'meditation_app/about.html')

def meditation_view(request):
    return render(request, 'meditation_app/meditation.html')

def discover_meditations_view(request):
    return render(request, 'meditation_app/discover-popular-meditations.html')

def contact_view(request):
    return render(request, 'meditation_app/contact.html')




def search_results(request):
    query = request.GET.get('q', '')
    results = []
    if query:
        # Filter dummy data based on the query.
        results = [
            item for item in dummy_data
            if query.lower() in item['title'].lower() or query.lower() in item['content'].lower()
        ]
    
    context = {
        'query': query,
        'results': results,
    }
    return render(request, 'meditation_app/search_results.html', context)



def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            auth_login(request, user)
            return redirect('home')  # or dashboard
        else:
            messages.error(request, 'Invalid credentials')
    return render(request, 'meditation_app/login.html')

def register_view(request):
    """
    Handles user registration.

    Validates form data before attempting to create a new user.
    """
    if request.method == 'POST':
        # Get form data from the POST request
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password1')
        password2 = request.POST.get('password2')

        # --- VALIDATION CHECKS ---
        # 1. Check if username, email, or passwords are empty
        if not username or not email or not password or not password2:
            messages.error(request, 'All fields are required.')
            return render(request, 'meditation_app/register.html') # Assuming your template is named register.html

        # 2. Check if passwords match
        if password != password2:
            messages.error(request, 'Passwords do not match.')
            return render(request, 'meditation_app/register.html')

        # 3. Check for existing user with the same username
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists. Please choose another.')
            return render(request, 'meditation_app/register.html')
        
        # 4. Check for an existing user with the same email
        if User.objects.filter(email=email).exists():
            messages.error(request, 'An account with this email already exists.')
            return render(request, 'meditation_app/register.html')

        # If all checks pass, create the user
        try:
            # The create_user method handles password hashing securely
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            messages.success(request, 'Account created successfully! You can now log in.')
            return redirect('login') # Redirect to the login page after successful registration
        except Exception as e:
            # Catch any other potential exceptions during user creation
            messages.error(request, f'An unexpected error occurred: {e}')
            return render(request, 'meditation_app/register.html')

    # For GET requests, render the empty registration form
    return render(request, 'meditation_app/register.html')
