import os
from src.RMLtoShacl import RMLtoSHACL
from rdflib.graph import Graph
from rdflib import compare

def test_RML2SHACL_TC3008():

    RtoS = RMLtoSHACL()
    expected_graph = Graph()
    expected_graph.parse(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'expected.ttl'), format="ttl")

    mapping_file = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'mapping.ttl')
    ontology_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'ontology')
    if not os.path.exists(ontology_path):
        ontology_path = None
    schema_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'schema')
    if not os.path.exists(schema_path):
        schema_path = None
    cwd = os.getcwd()
    tempfolder = os.path.abspath(os.path.join(cwd, '../../../../temp'))
    result_graph = RtoS.evaluateFiles(mapping_file, ontology_path, schema_path, tempfolder)

    assert compare.isomorphic(expected_graph, result_graph)