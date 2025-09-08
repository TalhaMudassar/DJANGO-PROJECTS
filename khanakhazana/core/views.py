from django.shortcuts import render

def home(request):
    # Popular Dishes Data
    popular_dishes = [
        {
            "image": "core/images/popularpaneer.jpg",
            "title": "Paneer Butter Masala",
            "description": "Creamy and rich, with a delightful blend of spices, perfect with naan or rice.",
            "link": "#"
        },
        {
            "image": "core/images/popularsalmon.jpg",
            "title": "Salmon Fish Curry",
            "description": "Succulent salmon in creamy, spiced curry with a perfect balance of flavors.",
            "link": "#"
        },
        {
            "image": "core/images/popularchicken.jpg",
            "title": "Butter Chicken",
            "description": "A royal dish with a creamy, nutty gravy that offers a rich, unforgettable taste.",
            "link": "#"
        },
    ]

    context = {
        "popular_dishes": popular_dishes
    }
    return render(request, 'core/home.html', context)

def menu(req):
    return render(req,'core/menu.html')


def tracking(req):
    return render(req,'core/tracking.html')

def reservation(req):
    return render(req,'core/reservation.html')

def contact(req):
    return render(req,'core/contact.html')