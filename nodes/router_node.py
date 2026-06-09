class RouterNode:

    def route(self, user_request):

        request = user_request.lower()

        if "לוגו" in request:
            return "logo"

        if "חתימה" in request:
            return "signature"

        if "כרטיס" in request:
            return "business_card"

        if "מכתב" in request:
            return "official_letter"

        return "unknown"