from django.http import JsonResponse

class GraphQLTokenMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.secret_token = "sk_live_2f48cae0f7d94b3e9b75a32e61d1ab8a"  # store in env for production

    def __call__(self, request):
        # Only protect the /graphql/ endpoint
        if request.path == "/graphql/":
            auth = request.headers.get("Authorization", "")
            if auth != f"Bearer {self.secret_token}":
                return JsonResponse({"error": "Unauthorized"}, status=401)

        return self.get_response(request)
