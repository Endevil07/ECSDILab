"""
.. module:: DBPedia2

DBPedia2
******

:Description: DBPedia2

    Different Auxiliary functions used for different purposes

:Authors:
    bejar

:Version: 

:Date:  23/04/2015
"""

__author__ = 'bejar'

from SPARQLWrapper import SPARQLWrapper, JSON, XML, RDF, N3
from rdflib import Graph, BNode, Literal

from AgentUtil.SPARQLPoints import DBPEDIA

# Configuramos el SPARQL de wikipedia
sparql = SPARQLWrapper(DBPEDIA)

# Obtenemos tods los tipos asignados a barcelona
# Si hacemos una query obtenemos un objeto de tipo answerset
# que contiene las vinculaciones de las variables de la query
sparql.setQuery("""
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    SELECT  DISTINCT ?val
    WHERE {?val  rdfs:domain  <http://dbpedia.org/ontology/City>.
          }
    LIMIT 1000
""")

# Los SELECT no siempre retornan un grafo RDF valido, por lo que es mas seguro obtener
# la informacion como JSON
sparql.setReturnFormat(JSON)

# Obtenemos los resultados y los imprimimos talcual
results = sparql.query()
results.print_results()
