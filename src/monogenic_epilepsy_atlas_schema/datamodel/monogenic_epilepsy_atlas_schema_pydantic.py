from __future__ import annotations

import re
import sys
from datetime import (
    date,
    datetime,
    time
)
from decimal import Decimal
from enum import Enum
from typing import (
    Any,
    ClassVar,
    Literal,
    Optional,
    Union
)

from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    RootModel,
    SerializationInfo,
    SerializerFunctionWrapHandler,
    field_validator,
    model_serializer
)


metamodel_version = "1.12.0"
version = "None"


class ConfiguredBaseModel(BaseModel):
    model_config = ConfigDict(
        serialize_by_alias = True,
        validate_by_name = True,
        validate_assignment = True,
        validate_default = True,
        extra = "forbid",
        arbitrary_types_allowed = True,
        use_enum_values = True,
        strict = False,
    )





class LinkMLMeta(RootModel):
    root: dict[str, Any] = {}
    model_config = ConfigDict(frozen=True)

    def __getattr__(self, key:str):
        return getattr(self.root, key)

    def __getitem__(self, key:str):
        return self.root[key]

    def __setitem__(self, key:str, value):
        self.root[key] = value

    def __contains__(self, key:str) -> bool:
        return key in self.root


linkml_meta = LinkMLMeta({'default_prefix': 'monogenic_epilepsy_atlas_schema',
     'default_range': 'string',
     'description': 'This is the LinkML schema for the Monogenic Epilepsy Atlas '
                    'schema',
     'id': 'https://w3id.org/bfurner/monogenic-epilepsy-atlas-schema',
     'imports': ['linkml:types'],
     'license': 'Apache-2.0',
     'name': 'monogenic-epilepsy-atlas-schema',
     'prefixes': {'linkml': {'prefix_prefix': 'linkml',
                             'prefix_reference': 'https://w3id.org/linkml/'},
                  'monogenic_epilepsy_atlas_schema': {'prefix_prefix': 'monogenic_epilepsy_atlas_schema',
                                                      'prefix_reference': 'https://w3id.org/bfurner/monogenic-epilepsy-atlas-schema/'},
                  'schema': {'prefix_prefix': 'schema',
                             'prefix_reference': 'http://schema.org/'}},
     'source_file': 'src/monogenic_epilepsy_atlas_schema/schema/monogenic_epilepsy_atlas_schema.yaml',
     'title': 'Monogenic Epilepsy Atlas Schema'} )

class YesNoUnknown(str, Enum):
    """
    A simple enumeration for yes, no, or unknown
    """
    YES = "YES"
    """
    True
    """
    NO = "NO"
    """
    False
    """
    UNKNOWN = "UNKNOWN"
    """
    unknown
    """


class OrganizationType(str, Enum):
    """
    A simple enumeration for the type of organization
    """
    CHAPTER = "CHAPTER"
    """
    A chapter (e.g., regional)
    """
    CONSORTIUM = "CONSORTIUM"
    """
    A consortium or umbrella organization
    """
    INFORMAL_COMMUNITY = "INFORMAL_COMMUNITY"
    """
    An informal community (e.g., a Facebook group)
    """
    PATIENT_ADVOCACY = "PATIENT_ADVOCACY"
    """
    A patient advocacy organization
    """


class UsaState(str, Enum):
    """
    A simple enumeration for the US states
    """
    AL = "AL"
    """
    Alabama
    """
    AK = "AK"
    """
    Alaska
    """
    AZ = "AZ"
    """
    Arizona
    """
    AR = "AR"
    """
    Arkansas
    """
    CA = "CA"
    """
    California
    """
    CO = "CO"
    """
    Colorado
    """
    CT = "CT"
    """
    Connecticut
    """
    DE = "DE"
    """
    Delaware
    """
    FL = "FL"
    """
    Florida
    """
    GA = "GA"
    """
    Georgia
    """
    HI = "HI"
    """
    Hawaii
    """
    ID = "ID"
    """
    Idaho
    """
    IL = "IL"
    """
    Illinois
    """
    IN = "IN"
    """
    Indiana
    """
    IA = "IA"
    """
    Iowa
    """
    KS = "KS"
    """
    Kansas
    """
    KY = "KY"
    """
    Kentucky
    """
    LA = "LA"
    """
    Louisiana
    """
    ME = "ME"
    """
    Maine
    """
    MD = "MD"
    """
    Maryland
    """
    MA = "MA"
    """
    Massachusetts
    """
    MI = "MI"
    """
    Michigan
    """
    MN = "MN"
    """
    Minnesota
    """
    MS = "MS"
    """
    Mississippi
    """
    MO = "MO"
    """
    Missouri
    """
    MT = "MT"
    """
    Montana
    """
    NE = "NE"
    """
    Nebraska
    """
    NV = "NV"
    """
    Nevada
    """
    NH = "NH"
    """
    New Hampshire
    """
    NJ = "NJ"
    """
    New Jersey
    """
    NM = "NM"
    """
    New Mexico
    """
    NY = "NY"
    """
    New York
    """
    NC = "NC"
    """
    North Carolina
    """
    ND = "ND"
    """
    North Dakota
    """
    OH = "OH"
    """
    Ohio
    """
    OK = "OK"
    """
    Oklahoma
    """
    OR = "OR"
    """
    Oregon
    """
    PA = "PA"
    """
    Pennsylvania
    """
    RI = "RI"
    """
    Rhode Island
    """
    SC = "SC"
    """
    South Carolina
    """
    SD = "SD"
    """
    South Dakota
    """
    TN = "TN"
    """
    Tennessee
    """
    TX = "TX"
    """
    Texas
    """
    UT = "UT"
    """
    Utah
    """
    VT = "VT"
    """
    Vermont
    """
    VA = "VA"
    """
    Virginia
    """
    WA = "WA"
    """
    Washington
    """
    WV = "WV"
    """
    West Virginia
    """
    WI = "WI"
    """
    Wisconsin
    """
    WY = "WY"
    """
    Wyoming
    """


class Country(str, Enum):
    """
    A simple enumeration for the countries of the world
    """
    US = "US"
    """
    United States
    """
    CA = "CA"
    """
    Canada
    """
    MX = "MX"
    """
    Mexico
    """
    GB = "GB"
    """
    United Kingdom
    """
    FR = "FR"
    """
    France
    """
    DE = "DE"
    """
    Germany
    """
    IT = "IT"
    """
    Italy
    """
    ES = "ES"
    """
    Spain
    """
    CN = "CN"
    """
    China
    """
    JP = "JP"
    """
    Japan
    """
    IN = "IN"
    """
    India
    """


class Reach(str, Enum):
    """
    A simple enumeration for the reach of an organization
    """
    REGIONAL = "REGIONAL"
    """
    A regional organization
    """
    NATIONAL = "NATIONAL"
    """
    A national organization
    """
    INTERNATIONAL = "INTERNATIONAL"
    """
    An international organization
    """



class Thing(ConfiguredBaseModel):
    """
    A generic grouping for any identifiable entity
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'schema:Thing',
         'from_schema': 'https://w3id.org/bfurner/monogenic-epilepsy-atlas-schema',
         'slot_usage': {'id': {'name': 'id', 'required': True},
                        'identity': {'name': 'identity', 'required': False}}})

    id: str = Field(default=..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['Thing'], 'slot_uri': 'schema:identifier'} })


class NamedThing(Thing):
    """
    A generic grouping for any named identifiable entity
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'schema:Thing',
         'from_schema': 'https://w3id.org/bfurner/monogenic-epilepsy-atlas-schema',
         'slot_usage': {'description': {'name': 'description', 'required': False},
                        'identity': {'name': 'identity', 'required': False},
                        'name': {'name': 'name', 'required': True}}})

    identity: Optional[list[str]] = Field(default=None, description="""A unique identifier for a thing that has carries meaning outside of the context of this schema or a particular instance of this schema.  For example, a concept in an ontology may have a URI that is used to identify it in the context of that ontology, and that URI may be used to identify the concept in other contexts as well.  In contrast, the id slot is intended to be a unique identifier for a thing within the context of this schema or a particular instance of this schema.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:identifier'} })
    name: str = Field(default=..., description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:description'} })
    id: str = Field(default=..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['Thing'], 'slot_uri': 'schema:identifier'} })


class GeneCollection(ConfiguredBaseModel):
    """
    A holder for Gene objects
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/bfurner/monogenic-epilepsy-atlas-schema',
         'tree_root': True})

    genes: Optional[list[Gene]] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['GeneCollection']} })


class Condition(NamedThing):
    """
    A condition is a disease or disorder that is associated with a person.  It may be a monogenic disorder, or it may be a complex disorder that is associated with a monogenic disorder.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/bfurner/monogenic-epilepsy-atlas-schema',
         'slot_usage': {'aliases': {'multivalued': True,
                                    'name': 'aliases',
                                    'required': False},
                        'external_references': {'multivalued': True,
                                                'name': 'external_references',
                                                'required': False},
                        'found_in_corpus': {'multivalued': False,
                                            'name': 'found_in_corpus',
                                            'required': True},
                        'in_scope': {'multivalued': False,
                                     'name': 'in_scope',
                                     'required': True},
                        'num_pages_in_corpus': {'multivalued': False,
                                                'name': 'num_pages_in_corpus',
                                                'required': False},
                        'reports_seizures': {'multivalued': False,
                                             'name': 'reports_seizures',
                                             'required': True}}})

    aliases: Optional[list[str]] = Field(default=None, description="""An alternative human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['Condition', 'Gene', 'Organization'],
         'slot_uri': 'schema:alternateName'} })
    external_references: Optional[list[str]] = Field(default=None, description="""A list of external references that provide more information about a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['Condition', 'Gene', 'Organization']} })
    reports_seizures: YesNoUnknown = Field(default=..., description="""A flag indicating whether a condition is associated with seizures or epilepsy""", json_schema_extra = { "linkml_meta": {'domain_of': ['Condition']} })
    found_in_corpus: YesNoUnknown = Field(default=..., description="""A flag indicating whether a Gene or Condition is found in the corpus of monogenic epilepsy disorders""", json_schema_extra = { "linkml_meta": {'domain_of': ['Condition', 'Gene']} })
    num_pages_in_corpus: Optional[int] = Field(default=None, description="""The number of pages in the corpus of monogenic epilepsy disorders that mention this Gene or Condition""", json_schema_extra = { "linkml_meta": {'domain_of': ['Condition', 'Gene']} })
    in_scope: YesNoUnknown = Field(default=..., description="""A flag indicating whether a Gene, Condition, or Organization is in scope for the Monogenic Epilepsy Atlas project""", json_schema_extra = { "linkml_meta": {'domain_of': ['Condition', 'Gene', 'Organization']} })
    identity: Optional[list[str]] = Field(default=None, description="""A unique identifier for a thing that has carries meaning outside of the context of this schema or a particular instance of this schema.  For example, a concept in an ontology may have a URI that is used to identify it in the context of that ontology, and that URI may be used to identify the concept in other contexts as well.  In contrast, the id slot is intended to be a unique identifier for a thing within the context of this schema or a particular instance of this schema.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:identifier'} })
    name: str = Field(default=..., description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:description'} })
    id: str = Field(default=..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['Thing'], 'slot_uri': 'schema:identifier'} })


class Gene(NamedThing):
    """
    A gene is a segment of DNA that is associated with a condition.  It may be a monogenic gene, or it may be a gene that is associated with a monogenic gene.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/bfurner/monogenic-epilepsy-atlas-schema',
         'slot_usage': {'aliases': {'multivalued': True,
                                    'name': 'aliases',
                                    'required': False},
                        'causes_condition': {'multivalued': True,
                                             'name': 'causes_condition',
                                             'required': False},
                        'external_references': {'multivalued': True,
                                                'name': 'external_references',
                                                'required': False},
                        'found_in_corpus': {'multivalued': False,
                                            'name': 'found_in_corpus',
                                            'required': True},
                        'genes4epilepsy_listed': {'multivalued': False,
                                                  'name': 'genes4epilepsy_listed',
                                                  'required': True},
                        'in_scope': {'multivalued': False,
                                     'name': 'in_scope',
                                     'required': True},
                        'num_pages_in_corpus': {'multivalued': False,
                                                'name': 'num_pages_in_corpus',
                                                'required': False},
                        'pathophysiologic_mechanism': {'multivalued': False,
                                                       'name': 'pathophysiologic_mechanism',
                                                       'required': False}}})

    aliases: Optional[list[str]] = Field(default=None, description="""An alternative human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['Condition', 'Gene', 'Organization'],
         'slot_uri': 'schema:alternateName'} })
    external_references: Optional[list[str]] = Field(default=None, description="""A list of external references that provide more information about a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['Condition', 'Gene', 'Organization']} })
    found_in_corpus: YesNoUnknown = Field(default=..., description="""A flag indicating whether a Gene or Condition is found in the corpus of monogenic epilepsy disorders""", json_schema_extra = { "linkml_meta": {'domain_of': ['Condition', 'Gene']} })
    num_pages_in_corpus: Optional[int] = Field(default=None, description="""The number of pages in the corpus of monogenic epilepsy disorders that mention this Gene or Condition""", json_schema_extra = { "linkml_meta": {'domain_of': ['Condition', 'Gene']} })
    pathophysiologic_mechanism: Optional[str] = Field(default=None, description="""A description of the pathophysiologic mechanism of a Gene or Condition, if known.  For example, a gene may be associated with a condition because it is involved in a particular biological pathway that is disrupted in the condition.  In this case, the pathophysiologic mechanism would be the biological pathway that is disrupted.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Gene']} })
    genes4epilepsy_listed: YesNoUnknown = Field(default=..., description="""A flag indicating whether a Gene is listed in the Genes4Epilepsy database""", json_schema_extra = { "linkml_meta": {'domain_of': ['Gene']} })
    causes_condition: Optional[list[str]] = Field(default=None, description="""A list of conditions that are caused by a Gene""", json_schema_extra = { "linkml_meta": {'domain_of': ['Gene']} })
    in_scope: YesNoUnknown = Field(default=..., description="""A flag indicating whether a Gene, Condition, or Organization is in scope for the Monogenic Epilepsy Atlas project""", json_schema_extra = { "linkml_meta": {'domain_of': ['Condition', 'Gene', 'Organization']} })
    identity: Optional[list[str]] = Field(default=None, description="""A unique identifier for a thing that has carries meaning outside of the context of this schema or a particular instance of this schema.  For example, a concept in an ontology may have a URI that is used to identify it in the context of that ontology, and that URI may be used to identify the concept in other contexts as well.  In contrast, the id slot is intended to be a unique identifier for a thing within the context of this schema or a particular instance of this schema.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:identifier'} })
    name: str = Field(default=..., description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:description'} })
    id: str = Field(default=..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['Thing'], 'slot_uri': 'schema:identifier'} })


class Organization(NamedThing):
    """
    An organization is a group of people that is associated with a condition or gene. It may be a research organization, a patient advocacy organization, or a professional society.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/bfurner/monogenic-epilepsy-atlas-schema',
         'slot_usage': {'advocates_for_condition': {'multivalued': True,
                                                    'name': 'advocates_for_condition',
                                                    'required': False},
                        'advocates_for_gene': {'multivalued': True,
                                               'name': 'advocates_for_gene',
                                               'required': False},
                        'aliases': {'multivalued': True,
                                    'name': 'aliases',
                                    'required': False},
                        'contact_person': {'multivalued': False,
                                           'name': 'contact_person',
                                           'required': False},
                        'contact_urls': {'multivalued': True,
                                         'name': 'contact_urls',
                                         'required': False},
                        'czi_rao_cohort_year': {'multivalued': False,
                                                'name': 'czi_rao_cohort_year',
                                                'required': False},
                        'external_references': {'multivalued': True,
                                                'name': 'external_references',
                                                'required': False},
                        'has_registry_or_study': {'multivalued': False,
                                                  'name': 'has_registry_or_study',
                                                  'required': True},
                        'in_scope': {'multivalued': False,
                                     'name': 'in_scope',
                                     'required': True},
                        'is_czi_rao_grantee': {'multivalued': False,
                                               'name': 'is_czi_rao_grantee',
                                               'required': False},
                        'leader': {'multivalued': False,
                                   'name': 'leader',
                                   'required': False},
                        'logo': {'multivalued': False,
                                 'name': 'logo',
                                 'required': False},
                        'member_of_organization': {'multivalued': True,
                                                   'name': 'member_of_organization',
                                                   'required': False},
                        'organization_type': {'multivalued': False,
                                              'name': 'organization_type',
                                              'required': True},
                        'primary_location': {'multivalued': False,
                                             'name': 'primary_location',
                                             'required': False},
                        'reach': {'multivalued': False,
                                  'name': 'reach',
                                  'required': False},
                        'year_founded': {'multivalued': False,
                                         'name': 'year_founded',
                                         'required': False}}})

    aliases: Optional[list[str]] = Field(default=None, description="""An alternative human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['Condition', 'Gene', 'Organization'],
         'slot_uri': 'schema:alternateName'} })
    external_references: Optional[list[str]] = Field(default=None, description="""A list of external references that provide more information about a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['Condition', 'Gene', 'Organization']} })
    organization_type: OrganizationType = Field(default=..., description="""The type of organization.  For example, a research organization, a patient advocacy organization, or a professional society.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Organization']} })
    primary_location: Optional[str] = Field(default=None, description="""The location of an organization.  For example, a state and/or country.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Organization']} })
    reach: Optional[Reach] = Field(default=None, description="""The reach of an organization.  For example, a patient advocacy organization may have a regional, national, or international reach.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Organization']} })
    year_founded: Optional[int] = Field(default=None, description="""The year an organization was founded""", json_schema_extra = { "linkml_meta": {'domain_of': ['Organization']} })
    in_scope: YesNoUnknown = Field(default=..., description="""A flag indicating whether a Gene, Condition, or Organization is in scope for the Monogenic Epilepsy Atlas project""", json_schema_extra = { "linkml_meta": {'domain_of': ['Condition', 'Gene', 'Organization']} })
    leader: Optional[str] = Field(default=None, description="""The leader of an organization.  For example, the president of a professional society or the director of a research organization.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Organization']} })
    contact_person: Optional[str] = Field(default=None, description="""The contact person for an organization.  For example, the person who is responsible for managing the organization's website or social media accounts.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Organization']} })
    contact_urls: Optional[list[str]] = Field(default=None, description="""A link to a web resource that provides more information about how to get in contact with an organization""", json_schema_extra = { "linkml_meta": {'domain_of': ['Organization']} })
    logo: Optional[str] = Field(default=None, description="""A link to a web resource that provides a logo for an organization""", json_schema_extra = { "linkml_meta": {'domain_of': ['Organization']} })
    has_registry_or_study: YesNoUnknown = Field(default=..., description="""A flag indicating whether an organization has a registry or study for a condition or gene""", json_schema_extra = { "linkml_meta": {'domain_of': ['Organization']} })
    is_czi_rao_grantee: Optional[YesNoUnknown] = Field(default=None, description="""A flag indicating whether an organization is a grantee of the CZI Rare as One program""", json_schema_extra = { "linkml_meta": {'domain_of': ['Organization']} })
    czi_rao_cohort_year: Optional[int] = Field(default=None, description="""The year an organization was a grantee of the CZI Rare as One program""", json_schema_extra = { "linkml_meta": {'domain_of': ['Organization']} })
    advocates_for_condition: Optional[list[str]] = Field(default=None, description="""A list of conditions that an organization advocates for.  For example, a patient advocacy organization may advocate for a particular condition or set of conditions.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Organization']} })
    advocates_for_gene: Optional[list[str]] = Field(default=None, description="""A list of genes that an organization advocates for.  For example, a patient advocacy organization may advocate for a particular gene or set of genes.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Organization']} })
    member_of_organization: Optional[list[str]] = Field(default=None, description="""An organization that a given organization is a member of.  For example, a patient advocacy organization may be a member of a larger umbrella organization.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Organization']} })
    identity: Optional[list[str]] = Field(default=None, description="""A unique identifier for a thing that has carries meaning outside of the context of this schema or a particular instance of this schema.  For example, a concept in an ontology may have a URI that is used to identify it in the context of that ontology, and that URI may be used to identify the concept in other contexts as well.  In contrast, the id slot is intended to be a unique identifier for a thing within the context of this schema or a particular instance of this schema.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:identifier'} })
    name: str = Field(default=..., description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:description'} })
    id: str = Field(default=..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['Thing'], 'slot_uri': 'schema:identifier'} })


class ExternalReference(NamedThing):
    """
    An external reference is a reference to an entity in an external resource.  It may be a reference to a concept in an ontology, or it may be a reference to a record in a database.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/bfurner/monogenic-epilepsy-atlas-schema',
         'slot_usage': {'link': {'name': 'link', 'required': True}}})

    link: str = Field(default=..., description="""A link to a web resource that provides more information about a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExternalReference'], 'slot_uri': 'schema:url'} })
    identity: Optional[list[str]] = Field(default=None, description="""A unique identifier for a thing that has carries meaning outside of the context of this schema or a particular instance of this schema.  For example, a concept in an ontology may have a URI that is used to identify it in the context of that ontology, and that URI may be used to identify the concept in other contexts as well.  In contrast, the id slot is intended to be a unique identifier for a thing within the context of this schema or a particular instance of this schema.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:identifier'} })
    name: str = Field(default=..., description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:description'} })
    id: str = Field(default=..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['Thing'], 'slot_uri': 'schema:identifier'} })


class Location(NamedThing):
    """
    A location is a physical place where an organization is located.  It may be a state and/or country.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/bfurner/monogenic-epilepsy-atlas-schema',
         'slot_usage': {'country': {'multivalued': False,
                                    'name': 'country',
                                    'required': True},
                        'state': {'multivalued': False,
                                  'name': 'state',
                                  'required': False}}})

    state: Optional[UsaState] = Field(default=None, description="""The state or province where an organization is located""", json_schema_extra = { "linkml_meta": {'domain_of': ['Location']} })
    country: Country = Field(default=..., description="""The country where an organization is located""", json_schema_extra = { "linkml_meta": {'domain_of': ['Location']} })
    identity: Optional[list[str]] = Field(default=None, description="""A unique identifier for a thing that has carries meaning outside of the context of this schema or a particular instance of this schema.  For example, a concept in an ontology may have a URI that is used to identify it in the context of that ontology, and that URI may be used to identify the concept in other contexts as well.  In contrast, the id slot is intended to be a unique identifier for a thing within the context of this schema or a particular instance of this schema.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:identifier'} })
    name: str = Field(default=..., description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:description'} })
    id: str = Field(default=..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['Thing'], 'slot_uri': 'schema:identifier'} })


class Person(NamedThing):
    """
    A person is an individual who is associated with an organization, condition or gene.  It may be a researcher, a patient, or a caregiver.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/bfurner/monogenic-epilepsy-atlas-schema',
         'slot_usage': {'primary_email': {'multivalued': False,
                                          'name': 'primary_email',
                                          'required': False},
                        'professional_title': {'multivalued': False,
                                               'name': 'professional_title',
                                               'required': False}}})

    primary_email: Optional[str] = Field(default=None, description="""The main email address of a person""", json_schema_extra = { "linkml_meta": {'domain_of': ['Person'], 'slot_uri': 'schema:email'} })
    professional_title: Optional[str] = Field(default=None, description="""The professional title of a person.  For example, a researcher may have the title of \"Professor\" or \"Research Scientist\".""", json_schema_extra = { "linkml_meta": {'domain_of': ['Person']} })
    identity: Optional[list[str]] = Field(default=None, description="""A unique identifier for a thing that has carries meaning outside of the context of this schema or a particular instance of this schema.  For example, a concept in an ontology may have a URI that is used to identify it in the context of that ontology, and that URI may be used to identify the concept in other contexts as well.  In contrast, the id slot is intended to be a unique identifier for a thing within the context of this schema or a particular instance of this schema.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:identifier'} })
    name: str = Field(default=..., description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:description'} })
    id: str = Field(default=..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'domain_of': ['Thing'], 'slot_uri': 'schema:identifier'} })


# Model rebuild
# see https://pydantic-docs.helpmanual.io/usage/models/#rebuilding-a-model
Thing.model_rebuild()
NamedThing.model_rebuild()
GeneCollection.model_rebuild()
Condition.model_rebuild()
Gene.model_rebuild()
Organization.model_rebuild()
ExternalReference.model_rebuild()
Location.model_rebuild()
Person.model_rebuild()
