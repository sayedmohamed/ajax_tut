from django.conf.urls.defaults import *
from django.views.generic import ListView
from models import Note

notes = Note.objects.all()

urlpatterns = patterns(
    '',
    (r'^$',ListView.as_view(model=Note,)),
	(r'^note/(?P<slug>[-\w]+)/$','django.views.generic.list_detail.object_detail',
		dict(queryset=notes,slug_field='slug')),
	(r'^note/(?P<slug>[-\w]+)/update/$','notes.views.update_note'),
	(r'^create/$','notes.views.create_note'),
    )
