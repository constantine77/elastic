
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from .search import SearchCompaniesIndex
# Create your models here.

# SearchComp to be indexed into ElasticSearch


class SearchCompanies(models.Model):
    company_name = models.CharField(max_length=30)
    email_address = models.CharField(max_length=50)
    address_city = models.CharField(max_length=60)
    state = models.CharField(max_length=30)
    zipcode = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=30)
    fax_number = models.CharField(max_length=30)
    sic_code = models.CharField(max_length=30)
    sic_description = models.CharField(max_length=30)
    webaddress = models.URLField()

    # Method for indexing the model
    def indexing(self):
        obj = SearchCompaniesIndex(
            meta={'id': self.id},
            company_name = self.company_name,
            email_address = self.email_address,
            address_city = self.address_city,
            state = self.state,
            zipcode = self.zipcode,
            phone_number = self.phone_number,
            fax_number = self.fax_number,
            sic_code = self.sic_code,
            sic_description = self.sic_description,
            webaddress = self.webaddress
        )
        obj.save()
        return obj.to_dict(include_meta=True)



