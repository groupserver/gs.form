#coding: utf-8
from zope.schema import *
from zope.interface import implements, providedBy, implementedBy, \
  directlyProvidedBy, alsoProvides
import logging
log = logging.getLogger('gs.content.form.utils')

def enforce_schema(inputData, schema):
    """
    SIDE EFFECTS
      * "inputData" is stated to provide the "schema" interface
      * "inputData" will provide all the properties defined in "schema"
    """

    typeMap = {
      Text:      'utext',
      TextLine:  'ustring',
      ASCII:     'utext',
      ASCIILine: 'string',
      URI:       'string',
      Bool:      'boolean',
      Float:     'float',
      Int:       'int',
      Datetime:  'date',
      Date:      'date',
    }
    fields = [field[0] for field in getFieldsInOrder(schema)]
    for field in fields:
        if not hasattr(inputData, field):
            m = u'%s has no attr %s' % (inputData.getId(), field)
            log.info(m)
            default = schema.get(field).default or ''
            t = typeMap.get(type(schema.get(field)), 'ustring')
            inputData.manage_addProperty(field, default, t)
    alsoProvides(inputData, schema)

