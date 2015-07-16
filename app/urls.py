from django.conf.urls import patterns

urlpatterns = patterns('',

      (r'^$', 'app.views.index'),

      (r'^brand/(?P<brand>[-\w]+)/all_json_models/$', 'all_json_models'),

)