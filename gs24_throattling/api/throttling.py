## for user rate throattling only because for anonymous user globally setting will be same
## this is only if we have to use for diifrent diffrent classes and for child classes

from rest_framework.throttling import UserRateThrottle

class JackRateThrottle(UserRateThrottle):
    scope = 'jack'
