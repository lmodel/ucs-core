

CREATE TABLE "Agent" (
	id TEXT NOT NULL, 
	iri TEXT, 
	type TEXT, 
	name TEXT, 
	description TEXT, 
	"hasAttribute" TEXT, 
	address TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "Hardware" (
	id TEXT NOT NULL, 
	iri TEXT, 
	type TEXT, 
	name TEXT, 
	description TEXT, 
	"hasAttribute" TEXT, 
	"inTaxon" TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "Linux" (
	id TEXT NOT NULL, 
	iri TEXT, 
	type TEXT, 
	name TEXT, 
	description TEXT, 
	"hasAttribute" TEXT, 
	"inTaxon" TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "NamedThing" (
	id TEXT NOT NULL, 
	iri TEXT, 
	type TEXT, 
	name TEXT, 
	description TEXT, 
	"hasAttribute" TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "OperatingSystem" (
	id TEXT NOT NULL, 
	iri TEXT, 
	type TEXT, 
	name TEXT, 
	description TEXT, 
	"hasAttribute" TEXT, 
	"inTaxon" TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "Project" (
	id TEXT NOT NULL, 
	iri TEXT, 
	type TEXT, 
	name TEXT, 
	description TEXT, 
	"hasAttribute" TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "QuantityValue" (
	"hasUnit" TEXT, 
	"hasNumericValue" FLOAT, 
	PRIMARY KEY ("hasUnit", "hasNumericValue")
);

CREATE TABLE "Software" (
	id TEXT NOT NULL, 
	iri TEXT, 
	type TEXT, 
	name TEXT, 
	description TEXT, 
	"hasAttribute" TEXT, 
	"inTaxon" TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "Solaris" (
	id TEXT NOT NULL, 
	iri TEXT, 
	type TEXT, 
	name TEXT, 
	description TEXT, 
	"hasAttribute" TEXT, 
	"inTaxon" TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "System" (
	id TEXT NOT NULL, 
	iri TEXT, 
	type TEXT, 
	name TEXT, 
	description TEXT, 
	"hasAttribute" TEXT, 
	"inTaxon" TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "Windows" (
	id TEXT NOT NULL, 
	iri TEXT, 
	type TEXT, 
	name TEXT, 
	description TEXT, 
	"hasAttribute" TEXT, 
	"inTaxon" TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "Association" (
	id TEXT NOT NULL, 
	iri TEXT, 
	name TEXT, 
	description TEXT, 
	"hasAttribute" TEXT, 
	subject TEXT NOT NULL, 
	predicate TEXT NOT NULL, 
	object TEXT NOT NULL, 
	negated BOOLEAN, 
	type TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(subject) REFERENCES "NamedThing" (id), 
	FOREIGN KEY(object) REFERENCES "NamedThing" (id)
);

CREATE TABLE "Attribute" (
	name TEXT, 
	"hasAttributeType" TEXT NOT NULL, 
	"hasQuantitativeValue" TEXT, 
	"hasQualitativeValue" TEXT, 
	iri TEXT, 
	src TEXT, 
	PRIMARY KEY (name, "hasAttributeType", "hasQuantitativeValue", "hasQualitativeValue", iri, src), 
	FOREIGN KEY("hasQualitativeValue") REFERENCES "NamedThing" (id)
);

CREATE TABLE "Agent_providedBy" (
	backref_id TEXT, 
	"providedBy" TEXT, 
	PRIMARY KEY (backref_id, "providedBy"), 
	FOREIGN KEY(backref_id) REFERENCES "Agent" (id)
);

CREATE TABLE "Agent_xref" (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES "Agent" (id)
);

CREATE TABLE "Agent_category" (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES "Agent" (id)
);

CREATE TABLE "Agent_affiliation" (
	backref_id TEXT, 
	affiliation TEXT, 
	PRIMARY KEY (backref_id, affiliation), 
	FOREIGN KEY(backref_id) REFERENCES "Agent" (id)
);

CREATE TABLE "Hardware_providedBy" (
	backref_id TEXT, 
	"providedBy" TEXT, 
	PRIMARY KEY (backref_id, "providedBy"), 
	FOREIGN KEY(backref_id) REFERENCES "Hardware" (id)
);

CREATE TABLE "Hardware_xref" (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES "Hardware" (id)
);

CREATE TABLE "Hardware_category" (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES "Hardware" (id)
);

CREATE TABLE "Linux_providedBy" (
	backref_id TEXT, 
	"providedBy" TEXT, 
	PRIMARY KEY (backref_id, "providedBy"), 
	FOREIGN KEY(backref_id) REFERENCES "Linux" (id)
);

CREATE TABLE "Linux_xref" (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES "Linux" (id)
);

CREATE TABLE "Linux_category" (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES "Linux" (id)
);

CREATE TABLE "NamedThing_providedBy" (
	backref_id TEXT, 
	"providedBy" TEXT, 
	PRIMARY KEY (backref_id, "providedBy"), 
	FOREIGN KEY(backref_id) REFERENCES "NamedThing" (id)
);

CREATE TABLE "NamedThing_xref" (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES "NamedThing" (id)
);

CREATE TABLE "NamedThing_category" (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES "NamedThing" (id)
);

CREATE TABLE "OperatingSystem_providedBy" (
	backref_id TEXT, 
	"providedBy" TEXT, 
	PRIMARY KEY (backref_id, "providedBy"), 
	FOREIGN KEY(backref_id) REFERENCES "OperatingSystem" (id)
);

CREATE TABLE "OperatingSystem_xref" (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES "OperatingSystem" (id)
);

CREATE TABLE "OperatingSystem_category" (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES "OperatingSystem" (id)
);

CREATE TABLE "Project_providedBy" (
	backref_id TEXT, 
	"providedBy" TEXT, 
	PRIMARY KEY (backref_id, "providedBy"), 
	FOREIGN KEY(backref_id) REFERENCES "Project" (id)
);

CREATE TABLE "Project_xref" (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES "Project" (id)
);

CREATE TABLE "Project_category" (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES "Project" (id)
);

CREATE TABLE "Software_providedBy" (
	backref_id TEXT, 
	"providedBy" TEXT, 
	PRIMARY KEY (backref_id, "providedBy"), 
	FOREIGN KEY(backref_id) REFERENCES "Software" (id)
);

CREATE TABLE "Software_xref" (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES "Software" (id)
);

CREATE TABLE "Software_category" (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES "Software" (id)
);

CREATE TABLE "Solaris_providedBy" (
	backref_id TEXT, 
	"providedBy" TEXT, 
	PRIMARY KEY (backref_id, "providedBy"), 
	FOREIGN KEY(backref_id) REFERENCES "Solaris" (id)
);

CREATE TABLE "Solaris_xref" (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES "Solaris" (id)
);

CREATE TABLE "Solaris_category" (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES "Solaris" (id)
);

CREATE TABLE "System_providedBy" (
	backref_id TEXT, 
	"providedBy" TEXT, 
	PRIMARY KEY (backref_id, "providedBy"), 
	FOREIGN KEY(backref_id) REFERENCES "System" (id)
);

CREATE TABLE "System_xref" (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES "System" (id)
);

CREATE TABLE "System_category" (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES "System" (id)
);

CREATE TABLE "Windows_providedBy" (
	backref_id TEXT, 
	"providedBy" TEXT, 
	PRIMARY KEY (backref_id, "providedBy"), 
	FOREIGN KEY(backref_id) REFERENCES "Windows" (id)
);

CREATE TABLE "Windows_xref" (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES "Windows" (id)
);

CREATE TABLE "Windows_category" (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES "Windows" (id)
);

CREATE TABLE "EvidenceType" (
	id TEXT NOT NULL, 
	iri TEXT, 
	type TEXT, 
	name TEXT, 
	description TEXT, 
	"hasAttribute" TEXT, 
	license TEXT, 
	rights TEXT, 
	format TEXT, 
	"creationDate" DATE, 
	"Association_id" TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY("Association_id") REFERENCES "Association" (id)
);

CREATE TABLE "Publication" (
	id TEXT NOT NULL, 
	iri TEXT, 
	type TEXT, 
	name TEXT, 
	description TEXT, 
	"hasAttribute" TEXT, 
	license TEXT, 
	rights TEXT, 
	format TEXT, 
	"creationDate" DATE, 
	summary TEXT, 
	"Association_id" TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY("Association_id") REFERENCES "Association" (id)
);

CREATE TABLE "Association_qualifiers" (
	backref_id TEXT, 
	qualifiers TEXT, 
	PRIMARY KEY (backref_id, qualifiers), 
	FOREIGN KEY(backref_id) REFERENCES "Association" (id)
);

CREATE TABLE "Association_category" (
	backref_id TEXT, 
	category TEXT, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES "Association" (id)
);

CREATE TABLE "EvidenceType_providedBy" (
	backref_id TEXT, 
	"providedBy" TEXT, 
	PRIMARY KEY (backref_id, "providedBy"), 
	FOREIGN KEY(backref_id) REFERENCES "EvidenceType" (id)
);

CREATE TABLE "EvidenceType_xref" (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES "EvidenceType" (id)
);

CREATE TABLE "EvidenceType_category" (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES "EvidenceType" (id)
);

CREATE TABLE "Publication_providedBy" (
	backref_id TEXT, 
	"providedBy" TEXT, 
	PRIMARY KEY (backref_id, "providedBy"), 
	FOREIGN KEY(backref_id) REFERENCES "Publication" (id)
);

CREATE TABLE "Publication_category" (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES "Publication" (id)
);

CREATE TABLE "Publication_authors" (
	backref_id TEXT, 
	authors TEXT, 
	PRIMARY KEY (backref_id, authors), 
	FOREIGN KEY(backref_id) REFERENCES "Publication" (id)
);

CREATE TABLE "Publication_pages" (
	backref_id TEXT, 
	pages TEXT, 
	PRIMARY KEY (backref_id, pages), 
	FOREIGN KEY(backref_id) REFERENCES "Publication" (id)
);

CREATE TABLE "Publication_keywords" (
	backref_id TEXT, 
	keywords TEXT, 
	PRIMARY KEY (backref_id, keywords), 
	FOREIGN KEY(backref_id) REFERENCES "Publication" (id)
);

CREATE TABLE "Publication_lcshTerms" (
	backref_id TEXT, 
	"lcshTerms" TEXT, 
	PRIMARY KEY (backref_id, "lcshTerms"), 
	FOREIGN KEY(backref_id) REFERENCES "Publication" (id)
);

CREATE TABLE "Publication_xref" (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES "Publication" (id)
);
