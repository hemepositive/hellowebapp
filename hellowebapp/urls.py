from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView, RedirectView
from django.contrib.auth.views import (
    password_reset,
    password_reset_done,
    password_reset_confirm,
    password_reset_complete
)
from collection.backends import MyRegistrationView


urlpatterns = patterns('',
    url(r'^$', 'collection.views.index', name='home'),
    url(r'^about/$',
    	TemplateView.as_view(template_name="about.html"),
    	name="about"),
    url(r'^contact/$',
    	TemplateView.as_view(template_name="contact.html"),
    	name="contact"),

    # things
    url(r'^things/$',
        RedirectView.as_view(pattern_name='browse')),
    url(r'^things/(?P<slug>[-\w]+)/$',
        'collection.views.thing_detail',
        name='thing_detail'),
    url(r'^things/(?P<slug>[-\w]+)/edit/$',
        'collection.views.edit_thing',
        name='edit_thing'),

    # password
    url(r'^accounts/password/reset/$',
        password_reset, {'template_name': 'registration/password_reset_form.html'},
        name="password_reset"),

    url(r'^acccouts/password/reset/done/$',
        password_reset_done,
        {'template_name': 'registration/password_reset_done'},
        name="password_reset_done"),

    url(r'^acccouts/password/reset/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$',
        password_reset_confirm,
        {'template_name': 'registration/password_reset_confirm.html'},
        name="password_reset_confirm"),

    url(r'^acccouts/password/done/$',
        password_reset_complete,
        {'template_name': 'registration/password_reset_complete.html'},
        name="password_reset_complete"),



    # registration
    url(r'^accounts/register/$',
        MyRegistrationView.as_view(),
        name='registration_register'),

    url(r'^accounts/create_thing/$',
        'collection.views.create_thing',
        name='registration_create_thing'),

    # browse
    url(r'^browse/$',
        RedirectView.as_view(pattern_name='browse')),
    url(r'^browse/name/$',
        'collection.views.browse_by_name',
        name="browse"),
    url(r'^browse/name/(?P<initial>[-\w]+)$',
        'collection.views.browse_by_name',
        name="browse_by_name"),

    # includes
    # url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
