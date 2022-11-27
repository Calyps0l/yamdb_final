from categories.urls import urlpatterns as categories_urls
from genres.urls import urlpatterns as genres_urls
from reviews.urls import urlpatterns as reviews_urls
from titles.urls import urlpatterns as titles_urls
from users.urls import urlpatterns as users_urls

urlpatterns = []

urlpatterns += categories_urls
urlpatterns += genres_urls
urlpatterns += reviews_urls
urlpatterns += users_urls
urlpatterns += titles_urls
