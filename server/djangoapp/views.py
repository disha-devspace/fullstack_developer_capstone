from django.http import JsonResponse
from django.views.decorators.http import require_GET
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
    return JsonResponse(
        [dealer_data(d) for d in dealers],
        safe=False
    )


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
    return JsonResponse(
        [dealer_data(d) for d in dealers],
        safe=False
    )


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
