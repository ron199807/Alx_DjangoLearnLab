from django.shortcuts import render, get_object_or_404, redirect
from .models import Book
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import user_passes_test, permission_required
from django.views.generic.detail import DetailView
from .models import Library

# Function based view to list all books
def list_books(request):
    books = Book.objects.all()  # Fetch all books from the database
    return render(request, 'relationship_app/list_books.html', {'books': books})




class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library



    # Custom registration view
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('list_books')  # Redirect to a view after registration
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})

# Use Django's built-in LoginView
class CustomLoginView(LoginView):
    template_name = 'relationship_app/login.html'

# Use Django's built-in LogoutView
class CustomLogoutView(LogoutView):
    template_name = 'relationship_app/logout.html'



# user role check
def is_member(user):
    return user.groups.filter(name='Member').exists()

def is_librarian(user):
    return user.groups.filter(name='Librarian').exists()

def is_admin(user):
    return user.is_superuser

# applying @user_passes_tests

@user_passes_test(is_member)
def member_view(request):
    render(request, 'relationship_app/member_view.html')

@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')


@permission_required('relationship_app.can_add_book')
def add_book(request):
    if request.methode == 'POST':
        pass
    return render(request, 'relationship_app/add_book.html')

@permission_required('relationahip_app.can_change_book')
def edit_book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    if request.method == 'POST':
        pass
    return render(request, 'relationship_app/edit_book.html', {'book': book})

@permission_required('relationahip_app.can_delete_book')
def delete_book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    return render(request, 'relationship_app/delete_book.html', {'book': book})
    
