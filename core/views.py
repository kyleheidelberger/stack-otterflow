from django.shortcuts import render
from django.views import generic
from core.models import Question, Category, Favorite, Answer, OtterProfile
from django.contrib.auth.decorators import login_required

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_questions = Question.objects.all().count()
    recent_questions_list = Question.objects.all()[0:5]
    all_cats = Category.objects.all()

    context = {
        'num_questions': num_questions,
        'recent_questions_list': recent_questions_list,
        'all_cats': all_cats,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

class CategoryListView(generic.ListView):
    model = Category

class CategoryDetailView(generic.DetailView):
    model = Category
    
class OtterProfileDetailView(generic.DetailView):
    model = OtterProfile

@login_required
def user_favorites(request):
    favorites = Favorite.objects.filter(favorited_by=request.user)

    favorites_list = []

    for favorite in favorites:
        favorites_list.append(favorite.question)

    context = {
        'favorites': favorites,
        'favorites_list': favorites_list,
    }

    return render(request, 'core/added_favorites.html', context)


@login_required
def add_to_favorites(request, pk):
    question = get_object_or_404(Question, pk=pk)
    
    new_favorite, created = Favorite.objects.get_or_create(question=question, favorited_by=request.user)
    if not created:
        new_favorite.delete()

    context = {
    'question': question,
    'new_favorite': new_favorite,
    'created': created,
    }

    return render(request, 'core/favorite_added.html', context)