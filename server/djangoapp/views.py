import json

from django.http import JsonResponse
from django.views.decorators.http import require_GET
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout

from .models import Dealer, Review


def dealer_data(dealer):
    return {
        "id": dealer.id,
        "address": dealer.address,
        "city": dealer.city,
        "full_name": dealer.full_name,
        "zip": dealer.zip,
        "state": dealer.state,
        "short_name": dealer.short_name
    }


@require_GET
def get_all_dealers(request):
    dealers = Dealer.objects.all()
    return JsonResponse([dealer_data(d) for d in dealers], safe=False)


@require_GET
def get_dealer_by_id(request, dealer_id):
    try:
        dealer = Dealer.objects.get(id=dealer_id)
        return JsonResponse(dealer_data(dealer))
    except Dealer.DoesNotExist:
        return JsonResponse({"error": "Dealer not found"}, status=404)


@require_GET
def get_dealers_by_state(request, state):
    dealers = Dealer.objects.filter(state__iexact=state)
    return JsonResponse([dealer_data(d) for d in dealers], safe=False)


@require_GET
def get_dealer_reviews(request, dealer_id):
    reviews = Review.objects.filter(dealer_id=dealer_id)
    data = [
        {
            "id": r.id,
            "name": r.name,
            "review": r.review,
            "purchase": r.purchase,
            "sentiment": r.sentiment
        }
        for r in reviews
    ]
    return JsonResponse(data, safe=False)


@csrf_exempt
def login_user(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            user = authenticate(
                request,
                username=data.get("username"),
                password=data.get("password")
            )

            if user is not None:
                login(request, user)
                return JsonResponse({
                    "status": "success",
                    "message": "Login successful",
                    "username": user.username
                })

            return JsonResponse({
                "status": "error",
                "message": "Invalid username or password"
            }, status=401)

        except (json.JSONDecodeError, TypeError):
            return JsonResponse({"error": "Invalid request data"}, status=400)

    return JsonResponse({"error": "POST method required"}, status=405)


@csrf_exempt
def logout_user(request):
    if request.method == "POST":
        logout(request)
        return JsonResponse({
            "status": "success",
            "message": "Logout successful"
        })

    return JsonResponse({"error": "POST method required"}, status=405)
