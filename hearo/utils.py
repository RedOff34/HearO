from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.contrib.auth.decorators import user_passes_test

def logout_required(function=None, redirect_url='/Main'):
    """
    Decorator for views that checks that the user is logged out, redirecting
    to the specified page if necessary.
    """
    actual_decorator = user_passes_test(
        lambda u: u.is_anonymous,
        login_url=redirect_url
    )
    if function:
        return actual_decorator(function)
    return actual_decorator