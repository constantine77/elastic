from .models import SearchCompanies
from django.db.models.signals import post_save
from django.dispatch import receiver


# Signal to save each new search companies instance into ElasticSearch
@receiver(post_save, sender=SearchCompanies)
def index_post(sender, instance, **kwargs):
    print(instance)
    instance.indexing()