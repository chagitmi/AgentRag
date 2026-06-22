def build_asset_query(user_request: str, route: str) -> str:

    if route == "signature":
        return "email signature company footer logo"

    if route == "logo":
        return "company logo branding symbol"

    if route == "business_card":
        return "business card contact card"

    if route == "official_letter":
        return "official document quotation proposal"

    return user_request