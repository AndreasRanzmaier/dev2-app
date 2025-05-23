def highest_mountain(mountains):
    if not mountains:
        return None
    
    return max(mountains, key=lambda mountains: mountains['height'])