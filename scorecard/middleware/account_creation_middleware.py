from scorecard.models import AccountProfile
from django.utils import timezone

class AccountCreationMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        #Check if the user is authenticated and if so, do we have an account record for them
        if request.user.is_authenticated:
            if request.session.get('account_id', None) == None:
                account = AccountProfile.objects.filter(account_user_id = request.user.id)
                if not account:
                    account = AccountProfile(last_login_date = timezone.now(), account_user = request.user)
                    account.save()
                else:
                    account = AccountProfile.objects.get(pk=account[0].id)
                request.session['account_id'] = account.id
        else:
            request.session['account_id'] = None

        return response