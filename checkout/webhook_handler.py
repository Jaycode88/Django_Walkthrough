from django.http import HttpResponse


class StripeWH_Handler:
    """ Handl Stripe webhooks """

    def __init__(self, request):
        sef.request = request

    def handle_event(self, event):
        """
        Handle a generic/unknown/unexpected webhook event
        """
        return HttpResponse(
            content=f'webhook recieved: {event["type"]}',
            status=200)
        