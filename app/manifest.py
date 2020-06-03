meta_resources = {
    "Attribute": {
        "Questionnaire.sourceQueries": {
            "type": {"resourceType": "Entity", "id": "Reference"},
            "path": ["sourceQueries"],
            "resource": {"resourceType": "Entity", "id": "Questionnaire"},
            "extensionUrl": "http://hl7.org/fhir/uv/sdc/StructureDefinition/sdc-questionnaire-sourceQueries",
            "isCollection": True,
        },
        "Questionnaire.launchContext": {
            "path": ["launchContext"],
            "resource": {"resourceType": "Entity", "id": "Questionnaire"},
            "extensionUrl": "http://hl7.org/fhir/uv/sdc/StructureDefinition/sdc-questionnaire-launchContext",
            "isCollection": True,
        },
        "Questionnaire.launchContext.name": {
            "type": {"resourceType": "Entity", "id": "id"},
            "path": ["launchContext", "name"],
            "resource": {"resourceType": "Entity", "id": "Questionnaire"},
            "extensionUrl": "name",
        },
        "Questionnaire.launchContext.type": {
            "type": {"resourceType": "Entity", "id": "code"},
            "path": ["launchContext", "type"],
            "resource": {"resourceType": "Entity", "id": "Questionnaire"},
            "extensionUrl": "type",
        },
        "Questionnaire.launchContext.description": {
            "type": {"resourceType": "Entity", "id": "string"},
            "path": ["launchContext", "description"],
            "resource": {"resourceType": "Entity", "id": "Questionnaire"},
            "extensionUrl": "description",
        },
        "Questionnaire.item.initialExpression": {
            "type": {"resourceType": "Entity", "id": "Expression"},
            "path": ["item", "initialExpression"],
            "resource": {"resourceType": "Entity", "id": "Questionnaire"},
            "extensionUrl": "http://hl7.org/fhir/uv/sdc/StructureDefinition/sdc-questionnaire-initialExpression",
        },
        "Questionnaire.itemContext": {
            "type": {"resourceType": "Entity", "id": "Expression"},
            "path": ["itemContext"],
            "resource": {"resourceType": "Entity", "id": "Questionnaire"},
            "extensionUrl": "http://hl7.org/fhir/uv/sdc/StructureDefinition/sdc-questionnaire-itemContext",
        },
        "Questionnaire.item.itemContext": {
            "type": {"resourceType": "Entity", "id": "Expression"},
            "path": ["item", "itemContext"],
            "resource": {"resourceType": "Entity", "id": "Questionnaire"},
            "extensionUrl": "http://hl7.org/fhir/uv/sdc/StructureDefinition/sdc-questionnaire-itemContext",
        },
        "Questionnaire.item.hidden": {
            "type": {"resourceType": "Entity", "id": "boolean"},
            "path": ["item", "hidden"],
            "resource": {"resourceType": "Entity", "id": "Questionnaire"},
            "extensionUrl": "http://hl7.org/fhir/StructureDefinition/questionnaire-hidden",
        },
        "Questionnaire.mapping": {
            "type": {"resourceType": "Entity", "id": "Reference"},
            "path": ["mapping"],
            "refers": ["Mapping"],
            "resource": {"resourceType": "Entity", "id": "Questionnaire"},
            "extensionUrl": "http://beda.software/fhir-extensions/questionnaire-mapper",
            "isCollection": True,
        },
        "Questionnaire.item.subQuestionnaire": {
            "type": {"resourceType": "Entity", "id": "canonical"},
            "path": ["item", "subQuestionnaire"],
            "resource": {"resourceType": "Entity", "id": "Questionnaire"},
            "extensionUrl": "https://jira.hl7.org/browse/FHIR-22356#subQuestionnaire",
        },
        "Questionnaire.assembledFrom": {
            "type": {"resourceType": "Entity", "id": "canonical"},
            "path": ["assembledFrom"],
            "resource": {"resourceType": "Entity", "id": "Questionnaire"},
            "extensionUrl": "https://jira.hl7.org/browse/FHIR-22356#assembledFrom",
        },
        "Questionnaire.fragmentRequiredContext": {
            "path": ["fragmentRequiredContext"],
            "resource": {"resourceType": "Entity", "id": "Questionnaire"},
            "extensionUrl": "http://hl7.org/fhir/uv/sdc/StructureDefinition/sdc-questionnaire-fragmentRequiredContext",
            "isCollection": True,
        },
        "Questionnaire.fragmentRequiredContext.name": {
            "type": {"resourceType": "Entity", "id": "id"},
            "path": ["fragmentRequiredContext", "name"],
            "resource": {"resourceType": "Entity", "id": "Questionnaire"},
            "extensionUrl": "name",
        },
        "Questionnaire.fragmentRequiredContext.type": {
            "type": {"resourceType": "Entity", "id": "code"},
            "path": ["fragmentRequiredContext", "type"],
            "resource": {"resourceType": "Entity", "id": "Questionnaire"},
            "extensionUrl": "type",
        },
        "Questionnaire.fragmentRequiredContext.description": {
            "type": {"resourceType": "Entity", "id": "string"},
            "path": ["fragmentRequiredContext", "description"],
            "resource": {"resourceType": "Entity", "id": "Questionnaire"},
            "extensionUrl": "description",
        },
        "Questionnaire.item.varaible": {
            "type": {"resourceType": "Entity", "id": "Expression"},
            "path": ["item", "varaible"],
            "resource": {"resourceType": "Entity", "id": "Questionnaire"},
            "extensionUrl": "http://hl7.org/fhir/StructureDefinition/variable",
            "isCollection": True,
        }
    },
}
