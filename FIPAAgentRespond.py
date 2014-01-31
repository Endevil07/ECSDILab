# -*- coding: utf-8 -*-
"""
Created on Fri Dec 27 15:58:13 2013

Agente que responde a peticiones

Demo de agente que utiliza las performativas FIPA para comunicación entre agentes
Las performativas estan definidas en la ontologia fipa-acl.owl

@author: javier
"""
__author__ = 'javier'


from  multiprocessing import Process
from flask import Flask,request
from rdflib import Graph, RDF, RDFS, OWL, Namespace, Literal
from rdflib.namespace import FOAF
import socket

app = Flask(__name__)

# Cargamos la ontologia FIPA-ACL
acl = Namespace("http://www.nuin.org/ontology/fipa/acl#")
FIPAONT = Graph()
FIPAONT.parse("Ontologias/fipa-acl.owl")
sa = acl.SpeechAct
agn = Namespace("http;//www.agentes.org#")

@app.route("/agente")
def agent1():
    message= request.args['content']
    gm = Graph()
    gr = Graph()
    gr.bind('acl',acl)
    gm.parse(data=message)
    print gm.serialize(format='turtle')
    perf = gm.triples( (None,  RDF.type, sa)) # Obtenemos la performativa
    if perf == None:
        gr.add((acl['not-understood'], RDF.type, sa))
    else:
        aresp= gm.subject_objects(FOAF.name)
        a,n = aresp.next()
        print a, n
        ms = acl['message0001']
        gr.add((ms, RDF.type, sa))
        gr.add((ms, acl.performative, acl.confirm))
        gm.add((agn.juan, FOAF.name, Literal('Juan')))
        gm.add((ms, acl.sender, agn.juan))

    return gr.serialize(format='xml')

if __name__ == '__main__':
    #print sa
    # for s,_,_ in FIPAONT.triples( (None,  RDF.type, sa) ):
    #     print s
    app.run()