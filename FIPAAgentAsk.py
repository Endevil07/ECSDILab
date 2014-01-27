__author__ = 'javier'


import requests
from rdflib import Namespace, URIRef, Graph, ConjunctiveGraph, Literal
from rdflib.namespace import FOAF, RDF
from rdflib.plugins.memory import IOMemory

acl = Namespace("http://www.nuin.org/ontology/fipa/acl#")
agn = Namespace("http;//www.agentes.org#")
gm = Graph()


ms = acl['message0000']
gm.bind('acl',acl)
gm.bind('foaf',FOAF)

gm.add((ms, RDF.type, acl.SpeechAct))
gm.add((ms, acl.performative, acl.request))
gm.add((agn.pepe, FOAF.name, Literal('Pepe')))
gm.add((ms, acl.sender, agn.pepe))

msg = gm.serialize(format='xml')
r=requests.get('http://127.0.0.1:5000/agente',params={'content':msg})

gr =Graph()
gr.parse(data=r.text)

print gr.serialize(format='turtle')
