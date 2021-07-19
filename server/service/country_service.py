import rdflib
from service.DetermineIntention import getDetermine, getLocation

g = rdflib.Graph()
g.parse('./service/country.owl', format="xml")

PREFIX = """PREFIX owl: <http://www.w3.org/2002/07/owl#>    
            PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>   
            PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>    
            PREFIX xml: <http://www.w3.org/XML/1998/namespace>  
            PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
            PREFIX :<http://www.semanticweb.org/nightmonkey/ontologies/2021/4/untitled-ontology-14#> 
            """

predicates = [("coTenQuocGia", "tenQuocGia"), ("coTieuNgu", "noiDungTieuNgu")]


def getDetermineIntention(text):
    location = getLocation(text)
    index = getDetermine(text)
    return getSingleInformation(location, index)


def getSingleInformation(text, index):
    predicate = predicates[index]
    query = """
            SELECT ?information
            WHERE{
                ?x :objProperty ?nToken.
                ?nToken :dataProperty ?information.
                ?x :coTenQuocGia ?nName.
                ?nName :tenQuocGia ?name.
                FILTER regex(?name, 'data', 'i')
            }
        """
    query = query.replace("objProperty", predicate[0]).replace("dataProperty", predicate[1]).replace("data", text)
    results = g.query(PREFIX + query)
    data = []
    for result in results:
        data.append("%s" % result)
    return data
