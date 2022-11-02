import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit
from ckanext.bdncatalog import validators as v

from collections import OrderedDict


class BdncatalogPlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)
    #plugins.implements(plugins.IRoutes, inherit=True)
    plugins.implements(plugins.IFacets, inherit=True)
    plugins.implements(plugins.IValidators)


    # IValidators
    def get_validators(self):
        return {
            'multiple_text_single_output': v.multiple_text_single_output
        }

    # IFacets
    def dataset_facets(self, facets_dict, package_type):
        if package_type == 'taxon':
            return OrderedDict([
                ('facet_Darwin_class', toolkit._('Clase')),
                ('facet_Darwin_family', toolkit._('Familia')),
                ('facet_Darwin_genus', toolkit._('Género'))
            ])
            return facets_dict
        elif package_type == 'taxon_record':
            return OrderedDict([
                ('facet_Plinian_hasThreatStatus', toolkit._('Estado amenazas')),
                ('facet_Plinian_hasCollection', toolkit._('Colección')),
                ('facet_Plinian_hasDirectThreats', toolkit._('Amenazas directas')),
                ('facet_Plinian_hasHabitats', toolkit._('Hábitats'))
            ])
            return facets_dict

        else:
            return OrderedDict([
                ('organization', toolkit._(u'Organización')),
                ('type', toolkit._('Tipo'))
            ])

    # IConfigurer

    def update_config(self, config_):
        toolkit.add_template_directory(config_, 'templates')
        toolkit.add_public_directory(config_, 'public')
        toolkit.add_resource('fanstatic',
            'bdncatalog')
