# encoding: utf-8

from rdflib.namespace import Namespace, RDFS, RDF, SKOS, XSD
from ckanext.dcat.profiles import RDFProfile
import ckan.lib.munge as munge

from ckanext.dcat.utils import resource_uri

from rdflib import URIRef, BNode, Literal

import json

DCT = Namespace("http://purl.org/dc/terms/")
SCHEMA = Namespace('http://schema.org/')
OWL = Namespace('http://www.w3.org/2002/07/owl#')
XML = Namespace('http://www.w3.org/2001/XMLSchema')

GEO = Namespace("http://www.opengis.net/ont/geosparql#")
DARWIN = Namespace("http://rs.tdwg.org/dwc/terms/")
MALLA = Namespace("https://datos.iepnb.es/def/sector-publico/cuadricula-espacial#")
CUADRICULAESP= Namespace("https://datos.iepnb.es/def/sector-publico/cuadricula-espacial#")
PLINIAN = Namespace("https://datos.iepnb.es/def/sector-publico/medio-ambiente/pliniancore#")
#PLINIANT = Namespace("https://datos.iepnb.es/def/sector-publico/medio-ambiente/pliniancore/")
GEOSF = Namespace("http://www.opengis.net/ont/sf#")


namespaces = {
    'dct': DCT,
    'skos': SKOS,
    'owl': OWL,
    'xml': XML,
    'geo': GEO,
    'Darwin': DARWIN,
    'CuadricualEsp': CUADRICULAESP,
    'Plinian': PLINIAN,
    #'PlinianT': PLINIANT,
    'GeoSf': GEOSF,
}

class EidosRDFProfile(RDFProfile):
    '''
    An RDF profile for Eidos

    It requires the European DCAT-AP profile (`euro_dcat_ap`)
    '''

    def add_rdf_type(self, g, dataset_ref, _type):
        if _type == 'collection':
            g.add((dataset_ref, RDF.type, PLINIAN.Collection))
        elif _type == 'direct_threats_type':
            g.add((dataset_ref, RDF.type, PLINIAN.Direct_Threats_Type))
        elif _type == 'distribution_type':
            g.add((dataset_ref, RDF.type, PLINIAN.Distribution_Type))
        elif _type == 'habitats_type':
            g.add((dataset_ref, RDF.type, PLINIAN.Habitats_Type))
        elif _type == 'invasiveness_type':
            g.add((dataset_ref, RDF.type, PLINIAN.Invasiveness_Type))
        elif _type == 'legislation_type':
            g.add((dataset_ref, RDF.type, PLINIAN.Legislation_Type))
        elif _type == 'population_biology_type':
            g.add((dataset_ref, RDF.type, PLINIAN.Population_Biology_Type))
        elif _type == 'record_metadata_type':
            g.add((dataset_ref, RDF.type, PLINIAN.Record_Metadata_Type))
        elif _type == 'reference_type':
            g.add((dataset_ref, RDF.type, PLINIAN.Reference_Type))
        elif _type == 'taxon_record':
            g.add((dataset_ref, RDF.type, PLINIAN.Taxon_Record))
        elif _type == 'threat_status_type':
            g.add((dataset_ref, RDF.type, PLINIAN.Threat_Status_Type))
        elif _type == 'vernacular_name':
            g.add((dataset_ref, RDF.type, PLINIAN.Vernacular_Name))
        elif _type == 'measurement_or_fact':
            g.add((dataset_ref, RDF.type, DARWIN.Measurement_Or_Fact))
        elif _type == 'taxon':
            g.add((dataset_ref, RDF.type, DARWIN.Taxon))
        elif _type == 'location':
            g.add((dataset_ref, RDF.type, DARWIN.Location))
        elif _type == 'management_conservation_type':
            g.add((dataset_ref, RDF.type, DCT.Management_Conservation_Type))

    def parse_dataset(self, dataset_dict, dataset_ref):
#        # Spatial label
#        spatial = self._object(dataset_ref, DCT.spatial)
#        if spatial:
#            spatial_label = self.g.label(spatial)
#            if spatial_label:
#                dataset_dict['extras'].append({'key': 'spatial_text',
#                                               'value': str(spatial_label)})

        # dataset_dict['type']='opendata'
        # dataset_dict['name']='opd-'+munge.munge_title_to_name(dataset_dict['title'])
        return dataset_dict


    def graph_from_dataset(self, dataset_dict, dataset_ref):

        g = self.g

        for prefix, namespace in namespaces.items():
            g.bind(prefix, namespace)

        #dataset_type = dataset_dict['type'][0].upper() + dataset_dict['type'][1:]
        #g.add((dataset_ref, RDF.type, PLINIANT.TaxonRecord))
        self.add_rdf_type(g, dataset_ref, dataset_dict['type']) 

        # if 'title' in dataset_dict:
        #     g.add((dataset_ref, DARWIN.scientificName, Literal(dataset_dict['title'])))

        # if 'notes' in dataset_dict:
        #     g.add((dataset_ref, PLINIAN.FullDescriptionUnstructured, Literal(dataset_dict['notes'])))

        # if 'taxonID' in dataset_dict:
        #     g.add((dataset_ref, PLINIAN.TaxonRecordID, Literal(dataset_dict['taxonID'])))
        #     g.add((dataset_ref, DARWIN.taxonID, Literal(dataset_dict['taxonID'])))

        # if 'taxonomia' in dataset_dict:
        #     g.add((dataset_ref, DARWIN.higherClassification, Literal(dataset_dict['taxonomia'])))

        # if 'code_eunis' in dataset_dict:
        #     g.add((dataset_ref, PLINIAN.CodeEUNIS, Literal(dataset_dict['code_eunis'])))

        for item in dataset_dict:
            if (dataset_dict[item]):
                item_short = None
                item_ns = None

                if item.startswith("Plinian_"):
                    #prop = item.replace("Plinian_", PLINIAN)
                    item_short  = item.replace("Plinian_", "")
                    item_ns = "PLINIAN"
                elif item.startswith("Darwin_"):
                    item_short  = item.replace("Darwin_", "")
                    item_ns = "DARWIN"
                elif item.startswith("DC_"):
                    item_short  = item.replace("DC_", "")
                    item_ns = "DCT"

                for val in dataset_dict[item]:
                    if item_short:
                        if val.startswith("http"):
                            g.add((dataset_ref, eval(item_ns + '.' + item_short), URIRef(val)))
                        else: 
                            g.add((dataset_ref, eval(item_ns + '.' + item_short), Literal(val)))

