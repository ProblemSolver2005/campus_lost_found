
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q

from .models import Item


# HOME PAGE
def home(request):

    items = Item.objects.filter(status='Active').order_by('-created_at')

    search = request.GET.get('search', '')
    item_type = request.GET.get('type', '')

    if search:
        items = items.filter(
            Q(title__icontains=search) |
            Q(location__icontains=search) |
            Q(description__icontains=search)
        )

    if item_type in ['Lost', 'Found']:
        items = items.filter(item_type=item_type)

    return render(request, 'portal/home.html', {
        'items': items,
        'search': search,
        'item_type': item_type
    })


# REGISTER
def register(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if not username or not email or not password:
            messages.error(request, 'Please fill in all fields.')

        elif password != confirm_password:
            messages.error(request, 'Passwords do not match.')

        elif User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists.')

        elif User.objects.filter(email=email).exists():
            messages.error(request, 'Email already registered.')

        else:
            user = User.objects.create_user(
                username=username,
                email=email,
                password=password
            )

            login(request, user)

            return redirect('home')

    return render(request, 'portal/register.html')


# LOGIN
def user_login(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            return redirect('home')

        else:
            messages.error(request, 'Invalid username or password.')

    return render(request, 'portal/login.html')


# LOGOUT
@login_required
def user_logout(request):

    if request.method == 'POST':
        logout(request)

    return redirect('home')


# CREATE ITEM
@login_required
def create_item(request):

    if request.method == 'POST':

        title = request.POST.get('title')
        item_type = request.POST.get('item_type')
        category = request.POST.get('category')
        description = request.POST.get('description')
        location = request.POST.get('location')
        contact = request.POST.get('contact')
        image = request.FILES.get('image')

        if not all([
            title, item_type, category,
            description, location, contact
        ]):
            messages.error(request, 'Please fill in all required fields.')

        elif item_type not in ['Lost', 'Found']:
            messages.error(request, 'Invalid item type.')

        elif category not in [
            'Electronics', 'Books', 'Accessories',
            'Clothing', 'Documents', 'Other'
        ]:
            messages.error(request, 'Invalid category.')

        else:

            Item.objects.create(
                title=title,
                item_type=item_type,
                category=category,
                description=description,
                location=location,
                contact=contact,
                image=image,
                created_by=request.user
            )

            messages.success(request, 'Item reported successfully!')

            return redirect('home')

    return render(request, 'portal/item_form.html', {
        'categories': Item.CATEGORY,
        'page_title': 'Report an Item',
        'button_text': 'Submit Report'
    })


# ITEM DETAILS
def item_detail(request, id):

    item = get_object_or_404(Item, id=id)

    return render(request, 'portal/item_detail.html', {
        'item': item
    })


# MY ITEMS
@login_required
def my_items(request):

    items = Item.objects.filter(
        created_by=request.user
    ).order_by('-created_at')

    return render(request, 'portal/my_items.html', {
        'items': items
    })


# EDIT ITEM
@login_required
def edit_item(request, id):

    item = get_object_or_404(
        Item,
        id=id,
        created_by=request.user
    )

    if request.method == 'POST':

        title = request.POST.get('title')
        item_type = request.POST.get('item_type')
        category = request.POST.get('category')
        description = request.POST.get('description')
        location = request.POST.get('location')
        contact = request.POST.get('contact')
        image = request.FILES.get('image')

        if not all([
            title, item_type, category,
            description, location, contact
        ]):
            messages.error(request, 'Please fill in all required fields.')

        elif item_type not in ['Lost', 'Found']:
            messages.error(request, 'Invalid item type.')

        elif category not in [
            'Electronics', 'Books', 'Accessories',
            'Clothing', 'Documents', 'Other'
        ]:
            messages.error(request, 'Invalid category.')

        else:

            item.title = title
            item.item_type = item_type
            item.category = category
            item.description = description
            item.location = location
            item.contact = contact

            if image:
                item.image = image

            item.save()

            messages.success(request, 'Item updated successfully!')

            return redirect('my_items')

    return render(request, 'portal/item_form.html', {
        'categories': Item.CATEGORY,
        'item': item,
        'page_title': 'Edit Item',
        'button_text': 'Update Item'
    })


# DELETE ITEM
@login_required
def delete_item(request, id):

    item = get_object_or_404(
        Item,
        id=id,
        created_by=request.user
    )

    if request.method == 'POST':
        item.delete()
        messages.success(request, 'Item deleted successfully!')

    return redirect('my_items')


# MARK ITEM AS RETURNED
@login_required
def mark_returned(request, id):

    item = get_object_or_404(
        Item,
        id=id,
        created_by=request.user
    )

    if request.method == 'POST':
        item.status = 'Returned'
        item.save()
        messages.success(request, 'Item marked as returned!')

    return redirect('my_items')
