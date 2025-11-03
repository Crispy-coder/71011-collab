document
 
/* 1. Namespaces */
prefix ex <http://example.com/teal-survey/>
prefix prov <http://www.w3.org/ns/prov#>
prefix s <http://schema.org/>
 
/* 2. Agents */
agent(ex:TealTeam, [prov:type="prov:Organization", prov:label="Teal Team"])
agent(ex:SurveyRespondents, [prov:type="prov:Collection", prov:label="Survey Respondents"])
 
agent(ex:Alice, [prov:type="prov:Person", prov:label="Alice"])
agent(ex:Brian, [prov:type="prov:Person", prov:label="Brian"])
agent(ex:Carl, [prov:type="prov:Person", prov:label="Carl"])
agent(ex:David, [prov:type="prov:Person", prov:label="David"])
 
agent(ex:Tutors, [prov:type="prov:Organization", prov:label="Tutors"])
agent(ex:Excel, [prov:type="prov:SoftwareAgent", prov:label="Excel"])
agent(ex:Qualtrics, [prov:type="prov:SoftwareAgent", prov:label="Qualtrics"])
agent(ex:PowerPoint, [prov:type="prov:SoftwareAgent", prov:label="PowerPoint"])
 
/* 3. Entities */
entity(ex:Topic, [prov:type="prov:Entity", prov:label="Cycle to Work"])
 
entity(ex:Internet, [
    prov:type="prov:Collection",
    prov:label="External Online Information",
    ex:source1="https://www.gov.uk/government/publications/cycle-to-work-scheme-implementation-guidance",
    ex:source2="https://www.cyclescheme.co.uk/"
])
 
entity(ex:SurveyDraft, [prov:type="prov:Entity", prov:label="Survey Draft"])
entity(ex:FinalSurvey, [prov:type="prov:Entity", prov:label="Final Survey"])
entity(ex:SurveyResponse, [prov:type="prov:Entity", prov:label="Survey Response"])
entity(ex:RawData, [prov:type="prov:Entity", prov:label="Raw Data Export"])
entity(ex:Documentation, [prov:type="prov:Entity", prov:label="Documentation"])
entity(ex:Metadata, [prov:type="prov:Entity", prov:label="Metadata"])
entity(ex:Attributes, [prov:type="prov:Entity", prov:label="Attributes"])
entity(ex:CleanedData, [prov:type="prov:Entity", prov:label="Cleaned Dataset"])
 
entity(ex:StandardisedData, [
    prov:type="prov:Entity",
    prov:label="Standardised Dataset",
    ex:variable1="Income",
    ex:variable2="Distance Travelled",
    ex:variable3="Work Model"
])
 
entity(ex:BasicIndex, [prov:type="prov:Entity", prov:label="Basic Index"])
entity(ex:FinalIndex, [prov:type="prov:Entity", prov:label="Final Index"])
entity(ex:Presentation, [prov:type="prov:Entity", prov:label="Presentation Slides"])
entity(ex:BasicPROVDiagram, [prov:type="prov:Entity", prov:label="Initial PROV Diagram"])
 
/* 4. Activities (now with timestamps) */
activity(ex:Research, -, -, [prov:label="Research Topic", prov:startedAtTime="2025-02-01T10:00:00Z", prov:endedAtTime="2025-02-01T12:00:00Z"])
activity(ex:SurveyDiscussion, -, -, [prov:label="Survey Discussion", prov:startedAtTime="2025-02-02T09:00:00Z", prov:endedAtTime="2025-02-02T10:30:00Z"])
activity(ex:PlayGovRole, -, -, [prov:label="Role-Play Exercise", prov:startedAtTime="2025-02-02T10:30:00Z", prov:endedAtTime="2025-02-02T11:00:00Z"])
activity(ex:PostingUploading, -, -, [prov:label="Posting Survey", prov:startedAtTime="2025-02-03T14:00:00Z", prov:endedAtTime="2025-02-03T14:10:00Z"])
activity(ex:CreateDocumentation, -, -, [prov:label="Write Documentation", prov:startedAtTime="2025-02-05T09:00:00Z", prov:endedAtTime="2025-02-05T11:00:00Z"])
activity(ex:UserPersonas, -, -, [prov:label="User Personas Analysis"])
activity(ex:CompleteSurvey, -, -, [prov:label="Survey Completion by Participants"])
activity(ex:PreprocessData, -, -, [prov:label="Data Preprocessing"])
activity(ex:ResearchIndexIndicators, -, -, [prov:label="Research Index Indicators"])
activity(ex:IndexDiscussion, -, -, [prov:label="Index Discussion"])
activity(ex:DataStandardisation, -, -, [prov:label="Data Standardisation"])
activity(ex:CreateIndexFormula, -, -, [prov:label="Create Index Formula"])
activity(ex:CreatePresentation, -, -, [prov:label="Create Presentation"])
activity(ex:CreateBasicPROVDiagram, -, -, [prov:label="Create Basic PROV Diagram"])
 
/* 5. Relations — unchanged logic */
 
/* 5.1 Responsibility */
wasAttributedTo(ex:Topic, ex:Tutors)
actedOnBehalfOf(ex:Tutors, ex:TealTeam, -)
wasAttributedTo(ex:SurveyDraft, ex:Qualtrics)
actedOnBehalfOf(ex:Alice, ex:TealTeam)
actedOnBehalfOf(ex:Brian, ex:TealTeam)
actedOnBehalfOf(ex:Carl, ex:TealTeam)
actedOnBehalfOf(ex:David, ex:TealTeam)
 
/* 5.2 Process responsibility */
wasAssociatedWith(ex:Research, ex:TealTeam, -)
wasAssociatedWith(ex:SurveyDiscussion, ex:TealTeam, -)
wasAssociatedWith(ex:PlayGovRole, ex:TealTeam, -)
wasAssociatedWith(ex:CreateDocumentation, ex:Excel, -)
wasAssociatedWith(ex:UserPersonas, ex:SurveyRespondents, -)
wasAssociatedWith(ex:CreatePresentation, ex:PowerPoint, -)
 
/* specialization */
specializationOf(ex:Metadata, ex:Documentation)
specializationOf(ex:Attributes, ex:Documentation)
specializationOf(ex:BasicPROVDiagram, ex:Presentation)
specializationOf(ex:FinalIndex, ex:Presentation)
 
/* 5.3 Dataflow (used) */
used(ex:Research, ex:Topic, -)
used(ex:Research, ex:Internet, -)
used(ex:SurveyDiscussion, ex:SurveyDraft, -)
used(ex:PostingUploading, ex:FinalSurvey, -)
used(ex:CreateDocumentation, ex:FinalSurvey, -)
used(ex:PreprocessData, ex:RawData, -)
used(ex:IndexDiscussion, ex:Documentation, -)
used(ex:DataStandardisation, ex:CleanedData, -)
used(ex:CreateIndexFormula, ex:StandardisedData, -)
used(ex:IndexDiscussion, ex:BasicIndex, -)
used(ex:CreateIndexFormula, ex:BasicIndex, -)
 
/* 5.3 Generation */
wasGeneratedBy(ex:SurveyDraft, ex:SurveyDiscussion, -)
wasGeneratedBy(ex:SurveyResponse, ex:PostingUploading, -)
wasGeneratedBy(ex:Documentation, ex:CreateDocumentation, -)
wasGeneratedBy(ex:SurveyDraft, ex:PlayGovRole, -)
wasGeneratedBy(ex:CleanedData, ex:PreprocessData, -)
wasGeneratedBy(ex:StandardisedData, ex:DataStandardisation, -)
wasGeneratedBy(ex:BasicIndex, ex:IndexDiscussion, -)
wasGeneratedBy(ex:FinalIndex, ex:CreateIndexFormula, -)
wasGeneratedBy(ex:Presentation, ex:CreatePresentation, -)
wasGeneratedBy(ex:BasicPROVDiagram, ex:CreateBasicPROVDiagram, -)
wasGeneratedBy(ex:SurveyResponse, ex:CompleteSurvey, -)
 
/* 5.4 Derivations */
wasDerivedFrom(ex:SurveyResponse, ex:RawData)
wasDerivedFrom(ex:FinalSurvey, ex:SurveyDraft)
wasDerivedFrom(ex:Attributes, ex:FinalSurvey)
wasDerivedFrom(ex:Metadata, ex:FinalSurvey)

/* 5.5 Layout flow chain (for visual arrangement only, does NOT change meaning) */
wasInformedBy(ex:SurveyDiscussion, ex:Research)
wasInformedBy(ex:PostingUploading, ex:SurveyDiscussion)
wasInformedBy(ex:PreprocessData, ex:PostingUploading)
wasInformedBy(ex:DataStandardisation, ex:PreprocessData)
wasInformedBy(ex:CreateIndexFormula, ex:DataStandardisation)
wasInformedBy(ex:CreatePresentation, ex:CreateIndexFormula)
wasInformedBy(ex:CreateBasicPROVDiagram, ex:CreatePresentation)

 
/* Inform relations */
wasInformedBy(ex:SurveyDiscussion, ex:PlayGovRole)
wasInformedBy(ex:PlayGovRole, ex:SurveyDiscussion)
wasInformedBy(ex:UserPersonas, ex:CompleteSurvey)
wasInformedBy(ex:IndexDiscussion, ex:PreprocessData)
wasInformedBy(ex:ResearchIndexIndicators, ex:IndexDiscussion)
wasInformedBy(ex:CreatePresentation, ex:ResearchIndexIndicators)
wasInformedBy(ex:CreatePresentation, ex:IndexDiscussion)
 
endDocument
