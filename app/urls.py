from app.authentication.urls import urlpatterns as authentication_urls
from app.chapters.urls import urlpatterns as chapters_urls
from app.events.urls import urlpatterns as events_urls
from app.hubs.urls import urlpatterns as hubs_urls
from app.opportunities.urls import urlpatterns as opportunities_urls
from app.user_auth.urls import urlpatterns as users_urls

urlpatterns = (
    authentication_urls
    + users_urls
    + chapters_urls
    + events_urls
    + hubs_urls
    + opportunities_urls
)
