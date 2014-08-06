from pymongo import MongoClient
from bson.objectid import ObjectId
from pgeo.config.settings import settings


client = MongoClient(settings['db']['metadata']['connection'])
db = settings['db']['metadata']['database']
doc = settings['db']['metadata']['document']['layer']


def find_layer_by_id(layer_id):
    return client[db][doc].find_one({'_id': ObjectId(layer_id)})


def find_layers_by_product(product, dekad, agg_type):
    q = {}
    conditions = []
    if product is not None:
        conditions.append({'meContent.seCoverage.coverageSector.codes.code': {'$in': [product]}})
    if dekad is not None:
        conditions.append({'meContent.seReferencePopulation.referencePeriod.codes.code': {'$in': [dekad]}})
    if agg_type is not None:
        conditions.append({'meStatisticalProcessing.seDatasource.seDataCompilation.aggregationProcessing': agg_type})
    q['$and'] = conditions
    return client[db][doc].find(q)