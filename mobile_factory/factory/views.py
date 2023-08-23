import json
from django.http import JsonResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt

COMPONENTS = {
    "A": ("LED Screen", 10.28, "Screen"),
    "B": ("OLED Screen", 24.07, "Screen"),
    "C": ("AMOLED Screen", 33.30, "Screen"),
    "D": ("Wide-Angle Camera", 25.94, "Camera"),
    "E": ("Ultra-Wide-Angle Camera", 32.39, "Camera"),
    "F": ("USB-C Port", 18.77, "Port"),
    "G": ("Micro-USB Port", 15.13, "Port"),
    "H": ("Lightning Port", 20.00, "Port"),
    "I": ("Android OS", 42.31, "OS"),
    "J": ("iOS OS", 45.00, "OS"),
    "K": ("Metallic Body", 45.00, "Body"),
    "L": ("Plastic Body", 30.00, "Body"),
}

@csrf_exempt
def create_order(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            components = data.get("components", [])

            if not is_valid_order(components):
                return JsonResponse({"error": "Invalid order"}, status=400)
            
            total_price = sum(COMPONENTS[c][1] for c in components)
            
            order_response = {
                "order_id": "some-id",
                "total": round(total_price, 2),
                "parts": [COMPONENTS[c][0] for c in components]
            }
            
            return JsonResponse(order_response, status=201)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON data"}, status=400)
    else:
        return HttpResponseBadRequest("Invalid HTTP method")

def is_valid_order(components):
    valid_categories = {"Screen", "Camera", "Port", "OS", "Body"}
    component_categories = set()

    for component in components:
        if component not in COMPONENTS:
            return False
        
        category = COMPONENTS[component][2]
        if category in component_categories:
            return False
        
        component_categories.add(category)
    
    return component_categories == valid_categories