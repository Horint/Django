# #coding: utf-8
# from django.conf.urls import patterns, url
#
# from blog.views import PostsListView, PostDetailView
#
# urlpatterns = [
#     path(r'^$', PostsListView.as_view(), name='list'), # то есть по URL http://имя_сайта/blog/                                          # будет выводиться список постов
#     path(r'^(?P<pk>\d+)/$', PostDetailView.as_view()), # а по URL http://имя_сайта/blog/число/                                         # будет выводиться пост с определенным номером
# ]