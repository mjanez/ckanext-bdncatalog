from ckan.plugins.toolkit import missing, _
from ckan.logic import NotFound, get_action
from ckanext.scheming.validation import scheming_validator
import json
import logging
log = logging.getLogger(__name__)


@scheming_validator
def multiple_text_single_output(value):
    """
    Return stored json representation as a list
    """
    try:
        return json.loads(value)
    except (ValueError, TypeError, AttributeError):
        if [value] is not None:
            return [value] 
        return value
