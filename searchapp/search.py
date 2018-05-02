from elasticsearch_dsl.connections import connections
from elasticsearch_dsl import DocType, Text, Date, Search
from elasticsearch.helpers import bulk
from elasticsearch import Elasticsearch
from . import models

# Create a connection to ElasticSearch
connections.create_connection()

# ElasticSearch "model" mapping out what fields to index
class SearchCompaniesIndex(DocType):
    company_name = Text()
    email_address = Text()
    address_city = Text()
    state = Text()
    zipcode = Text()
    phone_number = Text()
    fax_number = Text()
    sic_code = Text()
    sic_description = Text()
    webaddress = Text()

    class Meta:
        index = 'companies-index'

# Bulk indexing function, run in shell
def bulk_indexing():
    print("Start init")
    SearchCompaniesIndex.init()
    es = Elasticsearch()
    bulk(client=es, actions=(b.indexing() for b in models.SearchCompanies.objects.all().iterator()))

# Simple search function
def search(company_name):
    s = Search().filter('term', company_name=company_name)
    response = s.execute()
    return response

def test():
    return print("search is working")