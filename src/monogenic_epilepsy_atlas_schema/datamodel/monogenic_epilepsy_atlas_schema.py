# Auto generated from monogenic_epilepsy_atlas_schema.yaml by pythongen.py version: 0.0.1
# Schema: monogenic-epilepsy-atlas-schema
#
# id: https://w3id.org/bfurner/monogenic-epilepsy-atlas-schema
# description: This is the LinkML schema for the Monogenic Epilepsy Atlas schema
# license: Apache-2.0

import dataclasses
import re
from dataclasses import dataclass
from datetime import (
    date,
    datetime,
    time
)
from typing import (
    Any,
    ClassVar,
    Dict,
    List,
    Optional,
    Union
)

from jsonasobj2 import (
    JsonObj,
    as_dict
)
from linkml_runtime.linkml_model.meta import (
    EnumDefinition,
    PermissibleValue,
    PvFormulaOptions
)
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from linkml_runtime.utils.formatutils import (
    camelcase,
    sfx,
    underscore
)
from linkml_runtime.utils.metamodelcore import (
    bnode,
    empty_dict,
    empty_list
)
from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.yamlutils import (
    YAMLRoot,
    extended_float,
    extended_int,
    extended_str
)
from rdflib import (
    Namespace,
    URIRef
)

from linkml_runtime.linkml_model.types import Integer, String, Uriorcurie
from linkml_runtime.utils.metamodelcore import URIorCURIE

metamodel_version = "1.12.0"
version = None

# Namespaces
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
MONOGENIC_EPILEPSY_ATLAS_SCHEMA = CurieNamespace('monogenic_epilepsy_atlas_schema', 'https://w3id.org/bfurner/monogenic-epilepsy-atlas-schema/')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
DEFAULT_ = MONOGENIC_EPILEPSY_ATLAS_SCHEMA


# Types

# Class references
class ThingId(URIorCURIE):
    pass


class NamedThingId(ThingId):
    pass


class ConditionId(NamedThingId):
    pass


class GeneId(NamedThingId):
    pass


class OrganizationId(NamedThingId):
    pass


class ExternalReferenceId(NamedThingId):
    pass


class LocationId(NamedThingId):
    pass


class PersonId(NamedThingId):
    pass


@dataclass(repr=False)
class Thing(YAMLRoot):
    """
    A generic grouping for any identifiable entity
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SCHEMA["Thing"]
    class_class_curie: ClassVar[str] = "schema:Thing"
    class_name: ClassVar[str] = "Thing"
    class_model_uri: ClassVar[URIRef] = MONOGENIC_EPILEPSY_ATLAS_SCHEMA.Thing

    id: Union[str, ThingId] = None
    identity: Optional[Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ThingId):
            self.id = ThingId(self.id)

        if not isinstance(self.identity, list):
            self.identity = [self.identity] if self.identity is not None else []
        self.identity = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.identity]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class NamedThing(Thing):
    """
    A generic grouping for any named identifiable entity
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SCHEMA["Thing"]
    class_class_curie: ClassVar[str] = "schema:Thing"
    class_name: ClassVar[str] = "NamedThing"
    class_model_uri: ClassVar[URIRef] = MONOGENIC_EPILEPSY_ATLAS_SCHEMA.NamedThing

    id: Union[str, NamedThingId] = None
    name: str = None
    identity: Optional[Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]]] = empty_list()
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NamedThingId):
            self.id = NamedThingId(self.id)

        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if not isinstance(self.identity, list):
            self.identity = [self.identity] if self.identity is not None else []
        self.identity = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.identity]

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class GeneCollection(YAMLRoot):
    """
    A holder for Gene objects
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MONOGENIC_EPILEPSY_ATLAS_SCHEMA["GeneCollection"]
    class_class_curie: ClassVar[str] = "monogenic_epilepsy_atlas_schema:GeneCollection"
    class_name: ClassVar[str] = "GeneCollection"
    class_model_uri: ClassVar[URIRef] = MONOGENIC_EPILEPSY_ATLAS_SCHEMA.GeneCollection

    genes: Optional[Union[dict[Union[str, GeneId], Union[dict, "Gene"]], list[Union[dict, "Gene"]]]] = empty_dict()

    def __post_init__(self, *_: str, **kwargs: Any):
        self._normalize_inlined_as_list(slot_name="genes", slot_type=Gene, key_name="id", keyed=True)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Condition(NamedThing):
    """
    A condition is a disease or disorder that is associated with a person. It may be a monogenic disorder, or it may
    be a complex disorder that is associated with a monogenic disorder.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MONOGENIC_EPILEPSY_ATLAS_SCHEMA["Condition"]
    class_class_curie: ClassVar[str] = "monogenic_epilepsy_atlas_schema:Condition"
    class_name: ClassVar[str] = "Condition"
    class_model_uri: ClassVar[URIRef] = MONOGENIC_EPILEPSY_ATLAS_SCHEMA.Condition

    id: Union[str, ConditionId] = None
    name: str = None
    reports_seizures: Union[str, "YesNoUnknown"] = None
    found_in_corpus: Union[str, "YesNoUnknown"] = None
    in_scope: Union[str, "YesNoUnknown"] = None
    aliases: Optional[Union[str, list[str]]] = empty_list()
    external_references: Optional[Union[Union[str, ExternalReferenceId], list[Union[str, ExternalReferenceId]]]] = empty_list()
    num_pages_in_corpus: Optional[int] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ConditionId):
            self.id = ConditionId(self.id)

        if self._is_empty(self.reports_seizures):
            self.MissingRequiredField("reports_seizures")
        if not isinstance(self.reports_seizures, YesNoUnknown):
            self.reports_seizures = YesNoUnknown(self.reports_seizures)

        if self._is_empty(self.found_in_corpus):
            self.MissingRequiredField("found_in_corpus")
        if not isinstance(self.found_in_corpus, YesNoUnknown):
            self.found_in_corpus = YesNoUnknown(self.found_in_corpus)

        if self._is_empty(self.in_scope):
            self.MissingRequiredField("in_scope")
        if not isinstance(self.in_scope, YesNoUnknown):
            self.in_scope = YesNoUnknown(self.in_scope)

        if not isinstance(self.aliases, list):
            self.aliases = [self.aliases] if self.aliases is not None else []
        self.aliases = [v if isinstance(v, str) else str(v) for v in self.aliases]

        if not isinstance(self.external_references, list):
            self.external_references = [self.external_references] if self.external_references is not None else []
        self.external_references = [v if isinstance(v, ExternalReferenceId) else ExternalReferenceId(v) for v in self.external_references]

        if self.num_pages_in_corpus is not None and not isinstance(self.num_pages_in_corpus, int):
            self.num_pages_in_corpus = int(self.num_pages_in_corpus)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Gene(NamedThing):
    """
    A gene is a segment of DNA that is associated with a condition. It may be a monogenic gene, or it may be a gene
    that is associated with a monogenic gene.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MONOGENIC_EPILEPSY_ATLAS_SCHEMA["Gene"]
    class_class_curie: ClassVar[str] = "monogenic_epilepsy_atlas_schema:Gene"
    class_name: ClassVar[str] = "Gene"
    class_model_uri: ClassVar[URIRef] = MONOGENIC_EPILEPSY_ATLAS_SCHEMA.Gene

    id: Union[str, GeneId] = None
    name: str = None
    found_in_corpus: Union[str, "YesNoUnknown"] = None
    genes4epilepsy_listed: Union[str, "YesNoUnknown"] = None
    in_scope: Union[str, "YesNoUnknown"] = None
    aliases: Optional[Union[str, list[str]]] = empty_list()
    external_references: Optional[Union[Union[str, ExternalReferenceId], list[Union[str, ExternalReferenceId]]]] = empty_list()
    num_pages_in_corpus: Optional[int] = None
    pathophysiologic_mechanism: Optional[str] = None
    causes_condition: Optional[Union[Union[str, ConditionId], list[Union[str, ConditionId]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, GeneId):
            self.id = GeneId(self.id)

        if self._is_empty(self.found_in_corpus):
            self.MissingRequiredField("found_in_corpus")
        if not isinstance(self.found_in_corpus, YesNoUnknown):
            self.found_in_corpus = YesNoUnknown(self.found_in_corpus)

        if self._is_empty(self.genes4epilepsy_listed):
            self.MissingRequiredField("genes4epilepsy_listed")
        if not isinstance(self.genes4epilepsy_listed, YesNoUnknown):
            self.genes4epilepsy_listed = YesNoUnknown(self.genes4epilepsy_listed)

        if self._is_empty(self.in_scope):
            self.MissingRequiredField("in_scope")
        if not isinstance(self.in_scope, YesNoUnknown):
            self.in_scope = YesNoUnknown(self.in_scope)

        if not isinstance(self.aliases, list):
            self.aliases = [self.aliases] if self.aliases is not None else []
        self.aliases = [v if isinstance(v, str) else str(v) for v in self.aliases]

        if not isinstance(self.external_references, list):
            self.external_references = [self.external_references] if self.external_references is not None else []
        self.external_references = [v if isinstance(v, ExternalReferenceId) else ExternalReferenceId(v) for v in self.external_references]

        if self.num_pages_in_corpus is not None and not isinstance(self.num_pages_in_corpus, int):
            self.num_pages_in_corpus = int(self.num_pages_in_corpus)

        if self.pathophysiologic_mechanism is not None and not isinstance(self.pathophysiologic_mechanism, str):
            self.pathophysiologic_mechanism = str(self.pathophysiologic_mechanism)

        if not isinstance(self.causes_condition, list):
            self.causes_condition = [self.causes_condition] if self.causes_condition is not None else []
        self.causes_condition = [v if isinstance(v, ConditionId) else ConditionId(v) for v in self.causes_condition]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Organization(NamedThing):
    """
    An organization is a group of people that is associated with a condition or gene. It may be a research
    organization, a patient advocacy organization, or a professional society.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MONOGENIC_EPILEPSY_ATLAS_SCHEMA["Organization"]
    class_class_curie: ClassVar[str] = "monogenic_epilepsy_atlas_schema:Organization"
    class_name: ClassVar[str] = "Organization"
    class_model_uri: ClassVar[URIRef] = MONOGENIC_EPILEPSY_ATLAS_SCHEMA.Organization

    id: Union[str, OrganizationId] = None
    name: str = None
    organization_type: Union[str, "OrganizationType"] = None
    in_scope: Union[str, "YesNoUnknown"] = None
    has_registry_or_study: Union[str, "YesNoUnknown"] = None
    aliases: Optional[Union[str, list[str]]] = empty_list()
    external_references: Optional[Union[Union[str, ExternalReferenceId], list[Union[str, ExternalReferenceId]]]] = empty_list()
    primary_location: Optional[Union[str, LocationId]] = None
    reach: Optional[Union[str, "Reach"]] = None
    year_founded: Optional[int] = None
    leader: Optional[Union[str, PersonId]] = None
    contact_person: Optional[Union[str, PersonId]] = None
    contact_urls: Optional[Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]]] = empty_list()
    logo: Optional[Union[str, URIorCURIE]] = None
    is_czi_rao_grantee: Optional[Union[str, "YesNoUnknown"]] = None
    czi_rao_cohort_year: Optional[int] = None
    advocates_for_condition: Optional[Union[Union[str, ConditionId], list[Union[str, ConditionId]]]] = empty_list()
    advocates_for_gene: Optional[Union[Union[str, GeneId], list[Union[str, GeneId]]]] = empty_list()
    member_of_organization: Optional[Union[Union[str, OrganizationId], list[Union[str, OrganizationId]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, OrganizationId):
            self.id = OrganizationId(self.id)

        if self._is_empty(self.organization_type):
            self.MissingRequiredField("organization_type")
        if not isinstance(self.organization_type, OrganizationType):
            self.organization_type = OrganizationType(self.organization_type)

        if self._is_empty(self.in_scope):
            self.MissingRequiredField("in_scope")
        if not isinstance(self.in_scope, YesNoUnknown):
            self.in_scope = YesNoUnknown(self.in_scope)

        if self._is_empty(self.has_registry_or_study):
            self.MissingRequiredField("has_registry_or_study")
        if not isinstance(self.has_registry_or_study, YesNoUnknown):
            self.has_registry_or_study = YesNoUnknown(self.has_registry_or_study)

        if not isinstance(self.aliases, list):
            self.aliases = [self.aliases] if self.aliases is not None else []
        self.aliases = [v if isinstance(v, str) else str(v) for v in self.aliases]

        if not isinstance(self.external_references, list):
            self.external_references = [self.external_references] if self.external_references is not None else []
        self.external_references = [v if isinstance(v, ExternalReferenceId) else ExternalReferenceId(v) for v in self.external_references]

        if self.primary_location is not None and not isinstance(self.primary_location, LocationId):
            self.primary_location = LocationId(self.primary_location)

        if self.reach is not None and not isinstance(self.reach, Reach):
            self.reach = Reach(self.reach)

        if self.year_founded is not None and not isinstance(self.year_founded, int):
            self.year_founded = int(self.year_founded)

        if self.leader is not None and not isinstance(self.leader, PersonId):
            self.leader = PersonId(self.leader)

        if self.contact_person is not None and not isinstance(self.contact_person, PersonId):
            self.contact_person = PersonId(self.contact_person)

        if not isinstance(self.contact_urls, list):
            self.contact_urls = [self.contact_urls] if self.contact_urls is not None else []
        self.contact_urls = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.contact_urls]

        if self.logo is not None and not isinstance(self.logo, URIorCURIE):
            self.logo = URIorCURIE(self.logo)

        if self.is_czi_rao_grantee is not None and not isinstance(self.is_czi_rao_grantee, YesNoUnknown):
            self.is_czi_rao_grantee = YesNoUnknown(self.is_czi_rao_grantee)

        if self.czi_rao_cohort_year is not None and not isinstance(self.czi_rao_cohort_year, int):
            self.czi_rao_cohort_year = int(self.czi_rao_cohort_year)

        if not isinstance(self.advocates_for_condition, list):
            self.advocates_for_condition = [self.advocates_for_condition] if self.advocates_for_condition is not None else []
        self.advocates_for_condition = [v if isinstance(v, ConditionId) else ConditionId(v) for v in self.advocates_for_condition]

        if not isinstance(self.advocates_for_gene, list):
            self.advocates_for_gene = [self.advocates_for_gene] if self.advocates_for_gene is not None else []
        self.advocates_for_gene = [v if isinstance(v, GeneId) else GeneId(v) for v in self.advocates_for_gene]

        if not isinstance(self.member_of_organization, list):
            self.member_of_organization = [self.member_of_organization] if self.member_of_organization is not None else []
        self.member_of_organization = [v if isinstance(v, OrganizationId) else OrganizationId(v) for v in self.member_of_organization]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ExternalReference(NamedThing):
    """
    An external reference is a reference to an entity in an external resource. It may be a reference to a concept in
    an ontology, or it may be a reference to a record in a database.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MONOGENIC_EPILEPSY_ATLAS_SCHEMA["ExternalReference"]
    class_class_curie: ClassVar[str] = "monogenic_epilepsy_atlas_schema:ExternalReference"
    class_name: ClassVar[str] = "ExternalReference"
    class_model_uri: ClassVar[URIRef] = MONOGENIC_EPILEPSY_ATLAS_SCHEMA.ExternalReference

    id: Union[str, ExternalReferenceId] = None
    name: str = None
    link: Union[str, URIorCURIE] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ExternalReferenceId):
            self.id = ExternalReferenceId(self.id)

        if self._is_empty(self.link):
            self.MissingRequiredField("link")
        if not isinstance(self.link, URIorCURIE):
            self.link = URIorCURIE(self.link)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Location(NamedThing):
    """
    A location is a physical place where an organization is located.  It may be a state and/or country.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MONOGENIC_EPILEPSY_ATLAS_SCHEMA["Location"]
    class_class_curie: ClassVar[str] = "monogenic_epilepsy_atlas_schema:Location"
    class_name: ClassVar[str] = "Location"
    class_model_uri: ClassVar[URIRef] = MONOGENIC_EPILEPSY_ATLAS_SCHEMA.Location

    id: Union[str, LocationId] = None
    name: str = None
    country: Union[str, "Country"] = None
    state: Optional[Union[str, "UsaState"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, LocationId):
            self.id = LocationId(self.id)

        if self._is_empty(self.country):
            self.MissingRequiredField("country")
        if not isinstance(self.country, Country):
            self.country = Country(self.country)

        if self.state is not None and not isinstance(self.state, UsaState):
            self.state = UsaState(self.state)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Person(NamedThing):
    """
    A person is an individual who is associated with an organization, condition or gene. It may be a researcher, a
    patient, or a caregiver.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MONOGENIC_EPILEPSY_ATLAS_SCHEMA["Person"]
    class_class_curie: ClassVar[str] = "monogenic_epilepsy_atlas_schema:Person"
    class_name: ClassVar[str] = "Person"
    class_model_uri: ClassVar[URIRef] = MONOGENIC_EPILEPSY_ATLAS_SCHEMA.Person

    id: Union[str, PersonId] = None
    name: str = None
    primary_email: Optional[str] = None
    professional_title: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PersonId):
            self.id = PersonId(self.id)

        if self.primary_email is not None and not isinstance(self.primary_email, str):
            self.primary_email = str(self.primary_email)

        if self.professional_title is not None and not isinstance(self.professional_title, str):
            self.professional_title = str(self.professional_title)

        super().__post_init__(**kwargs)


# Enumerations
class YesNoUnknown(EnumDefinitionImpl):
    """
    A simple enumeration for yes, no, or unknown
    """
    YES = PermissibleValue(
        text="YES",
        description="True")
    NO = PermissibleValue(
        text="NO",
        description="False")
    UNKNOWN = PermissibleValue(
        text="UNKNOWN",
        description="unknown")

    _defn = EnumDefinition(
        name="YesNoUnknown",
        description="A simple enumeration for yes, no, or unknown",
    )

class OrganizationType(EnumDefinitionImpl):
    """
    A simple enumeration for the type of organization
    """
    CHAPTER = PermissibleValue(
        text="CHAPTER",
        description="A chapter (e.g., regional)")
    CONSORTIUM = PermissibleValue(
        text="CONSORTIUM",
        description="A consortium or umbrella organization")
    INFORMAL_COMMUNITY = PermissibleValue(
        text="INFORMAL_COMMUNITY",
        description="An informal community (e.g., a Facebook group)")
    PATIENT_ADVOCACY = PermissibleValue(
        text="PATIENT_ADVOCACY",
        description="A patient advocacy organization")

    _defn = EnumDefinition(
        name="OrganizationType",
        description="A simple enumeration for the type of organization",
    )

class UsaState(EnumDefinitionImpl):
    """
    A simple enumeration for the US states
    """
    AL = PermissibleValue(
        text="AL",
        description="Alabama")
    AK = PermissibleValue(
        text="AK",
        description="Alaska")
    AZ = PermissibleValue(
        text="AZ",
        description="Arizona")
    AR = PermissibleValue(
        text="AR",
        description="Arkansas")
    CA = PermissibleValue(
        text="CA",
        description="California")
    CO = PermissibleValue(
        text="CO",
        description="Colorado")
    CT = PermissibleValue(
        text="CT",
        description="Connecticut")
    DE = PermissibleValue(
        text="DE",
        description="Delaware")
    FL = PermissibleValue(
        text="FL",
        description="Florida")
    GA = PermissibleValue(
        text="GA",
        description="Georgia")
    HI = PermissibleValue(
        text="HI",
        description="Hawaii")
    ID = PermissibleValue(
        text="ID",
        description="Idaho")
    IL = PermissibleValue(
        text="IL",
        description="Illinois")
    IN = PermissibleValue(
        text="IN",
        description="Indiana")
    IA = PermissibleValue(
        text="IA",
        description="Iowa")
    KS = PermissibleValue(
        text="KS",
        description="Kansas")
    KY = PermissibleValue(
        text="KY",
        description="Kentucky")
    LA = PermissibleValue(
        text="LA",
        description="Louisiana")
    ME = PermissibleValue(
        text="ME",
        description="Maine")
    MD = PermissibleValue(
        text="MD",
        description="Maryland")
    MA = PermissibleValue(
        text="MA",
        description="Massachusetts")
    MI = PermissibleValue(
        text="MI",
        description="Michigan")
    MN = PermissibleValue(
        text="MN",
        description="Minnesota")
    MS = PermissibleValue(
        text="MS",
        description="Mississippi")
    MO = PermissibleValue(
        text="MO",
        description="Missouri")
    MT = PermissibleValue(
        text="MT",
        description="Montana")
    NE = PermissibleValue(
        text="NE",
        description="Nebraska")
    NV = PermissibleValue(
        text="NV",
        description="Nevada")
    NH = PermissibleValue(
        text="NH",
        description="New Hampshire")
    NJ = PermissibleValue(
        text="NJ",
        description="New Jersey")
    NM = PermissibleValue(
        text="NM",
        description="New Mexico")
    NY = PermissibleValue(
        text="NY",
        description="New York")
    NC = PermissibleValue(
        text="NC",
        description="North Carolina")
    ND = PermissibleValue(
        text="ND",
        description="North Dakota")
    OH = PermissibleValue(
        text="OH",
        description="Ohio")
    OK = PermissibleValue(
        text="OK",
        description="Oklahoma")
    OR = PermissibleValue(
        text="OR",
        description="Oregon")
    PA = PermissibleValue(
        text="PA",
        description="Pennsylvania")
    RI = PermissibleValue(
        text="RI",
        description="Rhode Island")
    SC = PermissibleValue(
        text="SC",
        description="South Carolina")
    SD = PermissibleValue(
        text="SD",
        description="South Dakota")
    TN = PermissibleValue(
        text="TN",
        description="Tennessee")
    TX = PermissibleValue(
        text="TX",
        description="Texas")
    UT = PermissibleValue(
        text="UT",
        description="Utah")
    VT = PermissibleValue(
        text="VT",
        description="Vermont")
    VA = PermissibleValue(
        text="VA",
        description="Virginia")
    WA = PermissibleValue(
        text="WA",
        description="Washington")
    WV = PermissibleValue(
        text="WV",
        description="West Virginia")
    WI = PermissibleValue(
        text="WI",
        description="Wisconsin")
    WY = PermissibleValue(
        text="WY",
        description="Wyoming")

    _defn = EnumDefinition(
        name="UsaState",
        description="A simple enumeration for the US states",
    )

class Country(EnumDefinitionImpl):
    """
    A simple enumeration for the countries of the world
    """
    US = PermissibleValue(
        text="US",
        description="United States")
    CA = PermissibleValue(
        text="CA",
        description="Canada")
    MX = PermissibleValue(
        text="MX",
        description="Mexico")
    GB = PermissibleValue(
        text="GB",
        description="United Kingdom")
    FR = PermissibleValue(
        text="FR",
        description="France")
    DE = PermissibleValue(
        text="DE",
        description="Germany")
    IT = PermissibleValue(
        text="IT",
        description="Italy")
    ES = PermissibleValue(
        text="ES",
        description="Spain")
    CN = PermissibleValue(
        text="CN",
        description="China")
    JP = PermissibleValue(
        text="JP",
        description="Japan")
    IN = PermissibleValue(
        text="IN",
        description="India")

    _defn = EnumDefinition(
        name="Country",
        description="A simple enumeration for the countries of the world",
    )

class Reach(EnumDefinitionImpl):
    """
    A simple enumeration for the reach of an organization
    """
    REGIONAL = PermissibleValue(
        text="REGIONAL",
        description="A regional organization")
    NATIONAL = PermissibleValue(
        text="NATIONAL",
        description="A national organization")
    INTERNATIONAL = PermissibleValue(
        text="INTERNATIONAL",
        description="An international organization")

    _defn = EnumDefinition(
        name="Reach",
        description="A simple enumeration for the reach of an organization",
    )

# Slots
class slots:
    pass

slots.id = Slot(uri=SCHEMA.identifier, name="id", curie=SCHEMA.curie('identifier'),
                   model_uri=MONOGENIC_EPILEPSY_ATLAS_SCHEMA.id, domain=None, range=URIRef)

slots.identity = Slot(uri=SCHEMA.identifier, name="identity", curie=SCHEMA.curie('identifier'),
                   model_uri=MONOGENIC_EPILEPSY_ATLAS_SCHEMA.identity, domain=None, range=Optional[Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]]])

slots.name = Slot(uri=SCHEMA.name, name="name", curie=SCHEMA.curie('name'),
                   model_uri=MONOGENIC_EPILEPSY_ATLAS_SCHEMA.name, domain=None, range=Optional[str])

slots.aliases = Slot(uri=SCHEMA.alternateName, name="aliases", curie=SCHEMA.curie('alternateName'),
                   model_uri=MONOGENIC_EPILEPSY_ATLAS_SCHEMA.aliases, domain=None, range=Optional[str])

slots.description = Slot(uri=SCHEMA.description, name="description", curie=SCHEMA.curie('description'),
                   model_uri=MONOGENIC_EPILEPSY_ATLAS_SCHEMA.description, domain=None, range=Optional[str])

slots.primary_email = Slot(uri=SCHEMA.email, name="primary_email", curie=SCHEMA.curie('email'),
                   model_uri=MONOGENIC_EPILEPSY_ATLAS_SCHEMA.primary_email, domain=None, range=Optional[str])

slots.link = Slot(uri=SCHEMA.url, name="link", curie=SCHEMA.curie('url'),
                   model_uri=MONOGENIC_EPILEPSY_ATLAS_SCHEMA.link, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.external_references = Slot(uri=MONOGENIC_EPILEPSY_ATLAS_SCHEMA.external_references, name="external_references", curie=MONOGENIC_EPILEPSY_ATLAS_SCHEMA.curie('external_references'),
                   model_uri=MONOGENIC_EPILEPSY_ATLAS_SCHEMA.external_references, domain=None, range=Optional[Union[Union[str, ExternalReferenceId], list[Union[str, ExternalReferenceId]]]])

slots.reports_seizures = Slot(uri=MONOGENIC_EPILEPSY_ATLAS_SCHEMA.reports_seizures, name="reports_seizures", curie=MONOGENIC_EPILEPSY_ATLAS_SCHEMA.curie('reports_seizures'),
                   model_uri=MONOGENIC_EPILEPSY_ATLAS_SCHEMA.reports_seizures, domain=None, range=Optional[Union[str, "YesNoUnknown"]])

slots.found_in_corpus = Slot(uri=MONOGENIC_EPILEPSY_ATLAS_SCHEMA.found_in_corpus, name="found_in_corpus", curie=MONOGENIC_EPILEPSY_ATLAS_SCHEMA.curie('found_in_corpus'),
                   model_uri=MONOGENIC_EPILEPSY_ATLAS_SCHEMA.found_in_corpus, domain=None, range=Optional[Union[str, "YesNoUnknown"]])

slots.num_pages_in_corpus = Slot(uri=MONOGENIC_EPILEPSY_ATLAS_SCHEMA.num_pages_in_corpus, name="num_pages_in_corpus", curie=MONOGENIC_EPILEPSY_ATLAS_SCHEMA.curie('num_pages_in_corpus'),
                   model_uri=MONOGENIC_EPILEPSY_ATLAS_SCHEMA.num_pages_in_corpus, domain=None, range=Optional[int])

slots.pathophysiologic_mechanism = Slot(uri=MONOGENIC_EPILEPSY_ATLAS_SCHEMA.pathophysiologic_mechanism, name="pathophysiologic_mechanism", curie=MONOGENIC_EPILEPSY_ATLAS_SCHEMA.curie('pathophysiologic_mechanism'),
                   model_uri=MONOGENIC_EPILEPSY_ATLAS_SCHEMA.pathophysiologic_mechanism, domain=None, range=Optional[str])

slots.genes4epilepsy_listed = Slot(uri=MONOGENIC_EPILEPSY_ATLAS_SCHEMA.genes4epilepsy_listed, name="genes4epilepsy_listed", curie=MONOGENIC_EPILEPSY_ATLAS_SCHEMA.curie('genes4epilepsy_listed'),
                   model_uri=MONOGENIC_EPILEPSY_ATLAS_SCHEMA.genes4epilepsy_listed, domain=None, range=Optional[Union[str, "YesNoUnknown"]])

slots.causes_condition = Slot(uri=MONOGENIC_EPILEPSY_ATLAS_SCHEMA.causes_condition, name="causes_condition", curie=MONOGENIC_EPILEPSY_ATLAS_SCHEMA.curie('causes_condition'),
                   model_uri=MONOGENIC_EPILEPSY_ATLAS_SCHEMA.causes_condition, domain=None, range=Optional[Union[str, ConditionId]])

slots.organization_type = Slot(uri=MONOGENIC_EPILEPSY_ATLAS_SCHEMA.organization_type, name="organization_type", curie=MONOGENIC_EPILEPSY_ATLAS_SCHEMA.curie('organization_type'),
                   model_uri=MONOGENIC_EPILEPSY_ATLAS_SCHEMA.organization_type, domain=None, range=Optional[Union[str, "OrganizationType"]])

slots.primary_location = Slot(uri=MONOGENIC_EPILEPSY_ATLAS_SCHEMA.primary_location, name="primary_location", curie=MONOGENIC_EPILEPSY_ATLAS_SCHEMA.curie('primary_location'),
                   model_uri=MONOGENIC_EPILEPSY_ATLAS_SCHEMA.primary_location, domain=None, range=Optional[Union[str, LocationId]])

slots.state = Slot(uri=MONOGENIC_EPILEPSY_ATLAS_SCHEMA.state, name="state", curie=MONOGENIC_EPILEPSY_ATLAS_SCHEMA.curie('state'),
                   model_uri=MONOGENIC_EPILEPSY_ATLAS_SCHEMA.state, domain=None, range=Optional[Union[str, "UsaState"]])

slots.country = Slot(uri=MONOGENIC_EPILEPSY_ATLAS_SCHEMA.country, name="country", curie=MONOGENIC_EPILEPSY_ATLAS_SCHEMA.curie('country'),
                   model_uri=MONOGENIC_EPILEPSY_ATLAS_SCHEMA.country, domain=None, range=Optional[Union[str, "Country"]])

slots.reach = Slot(uri=MONOGENIC_EPILEPSY_ATLAS_SCHEMA.reach, name="reach", curie=MONOGENIC_EPILEPSY_ATLAS_SCHEMA.curie('reach'),
                   model_uri=MONOGENIC_EPILEPSY_ATLAS_SCHEMA.reach, domain=None, range=Optional[Union[str, "Reach"]])

slots.year_founded = Slot(uri=MONOGENIC_EPILEPSY_ATLAS_SCHEMA.year_founded, name="year_founded", curie=MONOGENIC_EPILEPSY_ATLAS_SCHEMA.curie('year_founded'),
                   model_uri=MONOGENIC_EPILEPSY_ATLAS_SCHEMA.year_founded, domain=None, range=Optional[int])

slots.in_scope = Slot(uri=MONOGENIC_EPILEPSY_ATLAS_SCHEMA.in_scope, name="in_scope", curie=MONOGENIC_EPILEPSY_ATLAS_SCHEMA.curie('in_scope'),
                   model_uri=MONOGENIC_EPILEPSY_ATLAS_SCHEMA.in_scope, domain=None, range=Optional[Union[str, "YesNoUnknown"]])

slots.professional_title = Slot(uri=MONOGENIC_EPILEPSY_ATLAS_SCHEMA.professional_title, name="professional_title", curie=MONOGENIC_EPILEPSY_ATLAS_SCHEMA.curie('professional_title'),
                   model_uri=MONOGENIC_EPILEPSY_ATLAS_SCHEMA.professional_title, domain=None, range=Optional[str])

slots.leader = Slot(uri=MONOGENIC_EPILEPSY_ATLAS_SCHEMA.leader, name="leader", curie=MONOGENIC_EPILEPSY_ATLAS_SCHEMA.curie('leader'),
                   model_uri=MONOGENIC_EPILEPSY_ATLAS_SCHEMA.leader, domain=None, range=Optional[Union[str, PersonId]])

slots.contact_person = Slot(uri=MONOGENIC_EPILEPSY_ATLAS_SCHEMA.contact_person, name="contact_person", curie=MONOGENIC_EPILEPSY_ATLAS_SCHEMA.curie('contact_person'),
                   model_uri=MONOGENIC_EPILEPSY_ATLAS_SCHEMA.contact_person, domain=None, range=Optional[Union[str, PersonId]])

slots.contact_urls = Slot(uri=MONOGENIC_EPILEPSY_ATLAS_SCHEMA.contact_urls, name="contact_urls", curie=MONOGENIC_EPILEPSY_ATLAS_SCHEMA.curie('contact_urls'),
                   model_uri=MONOGENIC_EPILEPSY_ATLAS_SCHEMA.contact_urls, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.logo = Slot(uri=MONOGENIC_EPILEPSY_ATLAS_SCHEMA.logo, name="logo", curie=MONOGENIC_EPILEPSY_ATLAS_SCHEMA.curie('logo'),
                   model_uri=MONOGENIC_EPILEPSY_ATLAS_SCHEMA.logo, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.has_registry_or_study = Slot(uri=MONOGENIC_EPILEPSY_ATLAS_SCHEMA.has_registry_or_study, name="has_registry_or_study", curie=MONOGENIC_EPILEPSY_ATLAS_SCHEMA.curie('has_registry_or_study'),
                   model_uri=MONOGENIC_EPILEPSY_ATLAS_SCHEMA.has_registry_or_study, domain=None, range=Optional[Union[str, "YesNoUnknown"]])

slots.is_czi_rao_grantee = Slot(uri=MONOGENIC_EPILEPSY_ATLAS_SCHEMA.is_czi_rao_grantee, name="is_czi_rao_grantee", curie=MONOGENIC_EPILEPSY_ATLAS_SCHEMA.curie('is_czi_rao_grantee'),
                   model_uri=MONOGENIC_EPILEPSY_ATLAS_SCHEMA.is_czi_rao_grantee, domain=None, range=Optional[Union[str, "YesNoUnknown"]])

slots.czi_rao_cohort_year = Slot(uri=MONOGENIC_EPILEPSY_ATLAS_SCHEMA.czi_rao_cohort_year, name="czi_rao_cohort_year", curie=MONOGENIC_EPILEPSY_ATLAS_SCHEMA.curie('czi_rao_cohort_year'),
                   model_uri=MONOGENIC_EPILEPSY_ATLAS_SCHEMA.czi_rao_cohort_year, domain=None, range=Optional[int])

slots.advocates_for_condition = Slot(uri=MONOGENIC_EPILEPSY_ATLAS_SCHEMA.advocates_for_condition, name="advocates_for_condition", curie=MONOGENIC_EPILEPSY_ATLAS_SCHEMA.curie('advocates_for_condition'),
                   model_uri=MONOGENIC_EPILEPSY_ATLAS_SCHEMA.advocates_for_condition, domain=None, range=Optional[Union[str, ConditionId]])

slots.advocates_for_gene = Slot(uri=MONOGENIC_EPILEPSY_ATLAS_SCHEMA.advocates_for_gene, name="advocates_for_gene", curie=MONOGENIC_EPILEPSY_ATLAS_SCHEMA.curie('advocates_for_gene'),
                   model_uri=MONOGENIC_EPILEPSY_ATLAS_SCHEMA.advocates_for_gene, domain=None, range=Optional[Union[str, GeneId]])

slots.member_of_organization = Slot(uri=MONOGENIC_EPILEPSY_ATLAS_SCHEMA.member_of_organization, name="member_of_organization", curie=MONOGENIC_EPILEPSY_ATLAS_SCHEMA.curie('member_of_organization'),
                   model_uri=MONOGENIC_EPILEPSY_ATLAS_SCHEMA.member_of_organization, domain=None, range=Optional[Union[str, OrganizationId]])

slots.geneCollection__genes = Slot(uri=MONOGENIC_EPILEPSY_ATLAS_SCHEMA.genes, name="geneCollection__genes", curie=MONOGENIC_EPILEPSY_ATLAS_SCHEMA.curie('genes'),
                   model_uri=MONOGENIC_EPILEPSY_ATLAS_SCHEMA.geneCollection__genes, domain=None, range=Optional[Union[dict[Union[str, GeneId], Union[dict, Gene]], list[Union[dict, Gene]]]])

slots.Thing_id = Slot(uri=SCHEMA.identifier, name="Thing_id", curie=SCHEMA.curie('identifier'),
                   model_uri=MONOGENIC_EPILEPSY_ATLAS_SCHEMA.Thing_id, domain=Thing, range=Union[str, ThingId])

slots.Thing_identity = Slot(uri=SCHEMA.identifier, name="Thing_identity", curie=SCHEMA.curie('identifier'),
                   model_uri=MONOGENIC_EPILEPSY_ATLAS_SCHEMA.Thing_identity, domain=Thing, range=Optional[Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]]])

slots.NamedThing_identity = Slot(uri=SCHEMA.identifier, name="NamedThing_identity", curie=SCHEMA.curie('identifier'),
                   model_uri=MONOGENIC_EPILEPSY_ATLAS_SCHEMA.NamedThing_identity, domain=NamedThing, range=Optional[Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]]])

slots.NamedThing_name = Slot(uri=SCHEMA.name, name="NamedThing_name", curie=SCHEMA.curie('name'),
                   model_uri=MONOGENIC_EPILEPSY_ATLAS_SCHEMA.NamedThing_name, domain=NamedThing, range=str)

slots.NamedThing_description = Slot(uri=SCHEMA.description, name="NamedThing_description", curie=SCHEMA.curie('description'),
                   model_uri=MONOGENIC_EPILEPSY_ATLAS_SCHEMA.NamedThing_description, domain=NamedThing, range=Optional[str])

slots.Condition_aliases = Slot(uri=SCHEMA.alternateName, name="Condition_aliases", curie=SCHEMA.curie('alternateName'),
                   model_uri=MONOGENIC_EPILEPSY_ATLAS_SCHEMA.Condition_aliases, domain=Condition, range=Optional[Union[str, list[str]]])

slots.Condition_external_references = Slot(uri=MONOGENIC_EPILEPSY_ATLAS_SCHEMA.external_references, name="Condition_external_references", curie=MONOGENIC_EPILEPSY_ATLAS_SCHEMA.curie('external_references'),
                   model_uri=MONOGENIC_EPILEPSY_ATLAS_SCHEMA.Condition_external_references, domain=Condition, range=Optional[Union[Union[str, ExternalReferenceId], list[Union[str, ExternalReferenceId]]]])

slots.Condition_reports_seizures = Slot(uri=MONOGENIC_EPILEPSY_ATLAS_SCHEMA.reports_seizures, name="Condition_reports_seizures", curie=MONOGENIC_EPILEPSY_ATLAS_SCHEMA.curie('reports_seizures'),
                   model_uri=MONOGENIC_EPILEPSY_ATLAS_SCHEMA.Condition_reports_seizures, domain=Condition, range=Union[str, "YesNoUnknown"])

slots.Condition_found_in_corpus = Slot(uri=MONOGENIC_EPILEPSY_ATLAS_SCHEMA.found_in_corpus, name="Condition_found_in_corpus", curie=MONOGENIC_EPILEPSY_ATLAS_SCHEMA.curie('found_in_corpus'),
                   model_uri=MONOGENIC_EPILEPSY_ATLAS_SCHEMA.Condition_found_in_corpus, domain=Condition, range=Union[str, "YesNoUnknown"])

slots.Condition_num_pages_in_corpus = Slot(uri=MONOGENIC_EPILEPSY_ATLAS_SCHEMA.num_pages_in_corpus, name="Condition_num_pages_in_corpus", curie=MONOGENIC_EPILEPSY_ATLAS_SCHEMA.curie('num_pages_in_corpus'),
                   model_uri=MONOGENIC_EPILEPSY_ATLAS_SCHEMA.Condition_num_pages_in_corpus, domain=Condition, range=Optional[int])

slots.Condition_in_scope = Slot(uri=MONOGENIC_EPILEPSY_ATLAS_SCHEMA.in_scope, name="Condition_in_scope", curie=MONOGENIC_EPILEPSY_ATLAS_SCHEMA.curie('in_scope'),
                   model_uri=MONOGENIC_EPILEPSY_ATLAS_SCHEMA.Condition_in_scope, domain=Condition, range=Union[str, "YesNoUnknown"])

slots.Gene_aliases = Slot(uri=SCHEMA.alternateName, name="Gene_aliases", curie=SCHEMA.curie('alternateName'),
                   model_uri=MONOGENIC_EPILEPSY_ATLAS_SCHEMA.Gene_aliases, domain=Gene, range=Optional[Union[str, list[str]]])

slots.Gene_external_references = Slot(uri=MONOGENIC_EPILEPSY_ATLAS_SCHEMA.external_references, name="Gene_external_references", curie=MONOGENIC_EPILEPSY_ATLAS_SCHEMA.curie('external_references'),
                   model_uri=MONOGENIC_EPILEPSY_ATLAS_SCHEMA.Gene_external_references, domain=Gene, range=Optional[Union[Union[str, ExternalReferenceId], list[Union[str, ExternalReferenceId]]]])

slots.Gene_found_in_corpus = Slot(uri=MONOGENIC_EPILEPSY_ATLAS_SCHEMA.found_in_corpus, name="Gene_found_in_corpus", curie=MONOGENIC_EPILEPSY_ATLAS_SCHEMA.curie('found_in_corpus'),
                   model_uri=MONOGENIC_EPILEPSY_ATLAS_SCHEMA.Gene_found_in_corpus, domain=Gene, range=Union[str, "YesNoUnknown"])

slots.Gene_num_pages_in_corpus = Slot(uri=MONOGENIC_EPILEPSY_ATLAS_SCHEMA.num_pages_in_corpus, name="Gene_num_pages_in_corpus", curie=MONOGENIC_EPILEPSY_ATLAS_SCHEMA.curie('num_pages_in_corpus'),
                   model_uri=MONOGENIC_EPILEPSY_ATLAS_SCHEMA.Gene_num_pages_in_corpus, domain=Gene, range=Optional[int])

slots.Gene_pathophysiologic_mechanism = Slot(uri=MONOGENIC_EPILEPSY_ATLAS_SCHEMA.pathophysiologic_mechanism, name="Gene_pathophysiologic_mechanism", curie=MONOGENIC_EPILEPSY_ATLAS_SCHEMA.curie('pathophysiologic_mechanism'),
                   model_uri=MONOGENIC_EPILEPSY_ATLAS_SCHEMA.Gene_pathophysiologic_mechanism, domain=Gene, range=Optional[str])

slots.Gene_genes4epilepsy_listed = Slot(uri=MONOGENIC_EPILEPSY_ATLAS_SCHEMA.genes4epilepsy_listed, name="Gene_genes4epilepsy_listed", curie=MONOGENIC_EPILEPSY_ATLAS_SCHEMA.curie('genes4epilepsy_listed'),
                   model_uri=MONOGENIC_EPILEPSY_ATLAS_SCHEMA.Gene_genes4epilepsy_listed, domain=Gene, range=Union[str, "YesNoUnknown"])

slots.Gene_causes_condition = Slot(uri=MONOGENIC_EPILEPSY_ATLAS_SCHEMA.causes_condition, name="Gene_causes_condition", curie=MONOGENIC_EPILEPSY_ATLAS_SCHEMA.curie('causes_condition'),
                   model_uri=MONOGENIC_EPILEPSY_ATLAS_SCHEMA.Gene_causes_condition, domain=Gene, range=Optional[Union[Union[str, ConditionId], list[Union[str, ConditionId]]]])

slots.Gene_in_scope = Slot(uri=MONOGENIC_EPILEPSY_ATLAS_SCHEMA.in_scope, name="Gene_in_scope", curie=MONOGENIC_EPILEPSY_ATLAS_SCHEMA.curie('in_scope'),
                   model_uri=MONOGENIC_EPILEPSY_ATLAS_SCHEMA.Gene_in_scope, domain=Gene, range=Union[str, "YesNoUnknown"])

slots.Organization_aliases = Slot(uri=SCHEMA.alternateName, name="Organization_aliases", curie=SCHEMA.curie('alternateName'),
                   model_uri=MONOGENIC_EPILEPSY_ATLAS_SCHEMA.Organization_aliases, domain=Organization, range=Optional[Union[str, list[str]]])

slots.Organization_external_references = Slot(uri=MONOGENIC_EPILEPSY_ATLAS_SCHEMA.external_references, name="Organization_external_references", curie=MONOGENIC_EPILEPSY_ATLAS_SCHEMA.curie('external_references'),
                   model_uri=MONOGENIC_EPILEPSY_ATLAS_SCHEMA.Organization_external_references, domain=Organization, range=Optional[Union[Union[str, ExternalReferenceId], list[Union[str, ExternalReferenceId]]]])

slots.Organization_organization_type = Slot(uri=MONOGENIC_EPILEPSY_ATLAS_SCHEMA.organization_type, name="Organization_organization_type", curie=MONOGENIC_EPILEPSY_ATLAS_SCHEMA.curie('organization_type'),
                   model_uri=MONOGENIC_EPILEPSY_ATLAS_SCHEMA.Organization_organization_type, domain=Organization, range=Union[str, "OrganizationType"])

slots.Organization_primary_location = Slot(uri=MONOGENIC_EPILEPSY_ATLAS_SCHEMA.primary_location, name="Organization_primary_location", curie=MONOGENIC_EPILEPSY_ATLAS_SCHEMA.curie('primary_location'),
                   model_uri=MONOGENIC_EPILEPSY_ATLAS_SCHEMA.Organization_primary_location, domain=Organization, range=Optional[Union[str, LocationId]])

slots.Organization_reach = Slot(uri=MONOGENIC_EPILEPSY_ATLAS_SCHEMA.reach, name="Organization_reach", curie=MONOGENIC_EPILEPSY_ATLAS_SCHEMA.curie('reach'),
                   model_uri=MONOGENIC_EPILEPSY_ATLAS_SCHEMA.Organization_reach, domain=Organization, range=Optional[Union[str, "Reach"]])

slots.Organization_year_founded = Slot(uri=MONOGENIC_EPILEPSY_ATLAS_SCHEMA.year_founded, name="Organization_year_founded", curie=MONOGENIC_EPILEPSY_ATLAS_SCHEMA.curie('year_founded'),
                   model_uri=MONOGENIC_EPILEPSY_ATLAS_SCHEMA.Organization_year_founded, domain=Organization, range=Optional[int])

slots.Organization_in_scope = Slot(uri=MONOGENIC_EPILEPSY_ATLAS_SCHEMA.in_scope, name="Organization_in_scope", curie=MONOGENIC_EPILEPSY_ATLAS_SCHEMA.curie('in_scope'),
                   model_uri=MONOGENIC_EPILEPSY_ATLAS_SCHEMA.Organization_in_scope, domain=Organization, range=Union[str, "YesNoUnknown"])

slots.Organization_leader = Slot(uri=MONOGENIC_EPILEPSY_ATLAS_SCHEMA.leader, name="Organization_leader", curie=MONOGENIC_EPILEPSY_ATLAS_SCHEMA.curie('leader'),
                   model_uri=MONOGENIC_EPILEPSY_ATLAS_SCHEMA.Organization_leader, domain=Organization, range=Optional[Union[str, PersonId]])

slots.Organization_contact_person = Slot(uri=MONOGENIC_EPILEPSY_ATLAS_SCHEMA.contact_person, name="Organization_contact_person", curie=MONOGENIC_EPILEPSY_ATLAS_SCHEMA.curie('contact_person'),
                   model_uri=MONOGENIC_EPILEPSY_ATLAS_SCHEMA.Organization_contact_person, domain=Organization, range=Optional[Union[str, PersonId]])

slots.Organization_contact_urls = Slot(uri=MONOGENIC_EPILEPSY_ATLAS_SCHEMA.contact_urls, name="Organization_contact_urls", curie=MONOGENIC_EPILEPSY_ATLAS_SCHEMA.curie('contact_urls'),
                   model_uri=MONOGENIC_EPILEPSY_ATLAS_SCHEMA.Organization_contact_urls, domain=Organization, range=Optional[Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]]])

slots.Organization_logo = Slot(uri=MONOGENIC_EPILEPSY_ATLAS_SCHEMA.logo, name="Organization_logo", curie=MONOGENIC_EPILEPSY_ATLAS_SCHEMA.curie('logo'),
                   model_uri=MONOGENIC_EPILEPSY_ATLAS_SCHEMA.Organization_logo, domain=Organization, range=Optional[Union[str, URIorCURIE]])

slots.Organization_has_registry_or_study = Slot(uri=MONOGENIC_EPILEPSY_ATLAS_SCHEMA.has_registry_or_study, name="Organization_has_registry_or_study", curie=MONOGENIC_EPILEPSY_ATLAS_SCHEMA.curie('has_registry_or_study'),
                   model_uri=MONOGENIC_EPILEPSY_ATLAS_SCHEMA.Organization_has_registry_or_study, domain=Organization, range=Union[str, "YesNoUnknown"])

slots.Organization_is_czi_rao_grantee = Slot(uri=MONOGENIC_EPILEPSY_ATLAS_SCHEMA.is_czi_rao_grantee, name="Organization_is_czi_rao_grantee", curie=MONOGENIC_EPILEPSY_ATLAS_SCHEMA.curie('is_czi_rao_grantee'),
                   model_uri=MONOGENIC_EPILEPSY_ATLAS_SCHEMA.Organization_is_czi_rao_grantee, domain=Organization, range=Optional[Union[str, "YesNoUnknown"]])

slots.Organization_czi_rao_cohort_year = Slot(uri=MONOGENIC_EPILEPSY_ATLAS_SCHEMA.czi_rao_cohort_year, name="Organization_czi_rao_cohort_year", curie=MONOGENIC_EPILEPSY_ATLAS_SCHEMA.curie('czi_rao_cohort_year'),
                   model_uri=MONOGENIC_EPILEPSY_ATLAS_SCHEMA.Organization_czi_rao_cohort_year, domain=Organization, range=Optional[int])

slots.Organization_advocates_for_condition = Slot(uri=MONOGENIC_EPILEPSY_ATLAS_SCHEMA.advocates_for_condition, name="Organization_advocates_for_condition", curie=MONOGENIC_EPILEPSY_ATLAS_SCHEMA.curie('advocates_for_condition'),
                   model_uri=MONOGENIC_EPILEPSY_ATLAS_SCHEMA.Organization_advocates_for_condition, domain=Organization, range=Optional[Union[Union[str, ConditionId], list[Union[str, ConditionId]]]])

slots.Organization_advocates_for_gene = Slot(uri=MONOGENIC_EPILEPSY_ATLAS_SCHEMA.advocates_for_gene, name="Organization_advocates_for_gene", curie=MONOGENIC_EPILEPSY_ATLAS_SCHEMA.curie('advocates_for_gene'),
                   model_uri=MONOGENIC_EPILEPSY_ATLAS_SCHEMA.Organization_advocates_for_gene, domain=Organization, range=Optional[Union[Union[str, GeneId], list[Union[str, GeneId]]]])

slots.Organization_member_of_organization = Slot(uri=MONOGENIC_EPILEPSY_ATLAS_SCHEMA.member_of_organization, name="Organization_member_of_organization", curie=MONOGENIC_EPILEPSY_ATLAS_SCHEMA.curie('member_of_organization'),
                   model_uri=MONOGENIC_EPILEPSY_ATLAS_SCHEMA.Organization_member_of_organization, domain=Organization, range=Optional[Union[Union[str, OrganizationId], list[Union[str, OrganizationId]]]])

slots.ExternalReference_link = Slot(uri=SCHEMA.url, name="ExternalReference_link", curie=SCHEMA.curie('url'),
                   model_uri=MONOGENIC_EPILEPSY_ATLAS_SCHEMA.ExternalReference_link, domain=ExternalReference, range=Union[str, URIorCURIE])

slots.Location_state = Slot(uri=MONOGENIC_EPILEPSY_ATLAS_SCHEMA.state, name="Location_state", curie=MONOGENIC_EPILEPSY_ATLAS_SCHEMA.curie('state'),
                   model_uri=MONOGENIC_EPILEPSY_ATLAS_SCHEMA.Location_state, domain=Location, range=Optional[Union[str, "UsaState"]])

slots.Location_country = Slot(uri=MONOGENIC_EPILEPSY_ATLAS_SCHEMA.country, name="Location_country", curie=MONOGENIC_EPILEPSY_ATLAS_SCHEMA.curie('country'),
                   model_uri=MONOGENIC_EPILEPSY_ATLAS_SCHEMA.Location_country, domain=Location, range=Union[str, "Country"])

slots.Person_primary_email = Slot(uri=SCHEMA.email, name="Person_primary_email", curie=SCHEMA.curie('email'),
                   model_uri=MONOGENIC_EPILEPSY_ATLAS_SCHEMA.Person_primary_email, domain=Person, range=Optional[str])

slots.Person_professional_title = Slot(uri=MONOGENIC_EPILEPSY_ATLAS_SCHEMA.professional_title, name="Person_professional_title", curie=MONOGENIC_EPILEPSY_ATLAS_SCHEMA.curie('professional_title'),
                   model_uri=MONOGENIC_EPILEPSY_ATLAS_SCHEMA.Person_professional_title, domain=Person, range=Optional[str])
