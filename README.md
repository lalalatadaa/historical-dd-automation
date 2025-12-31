Historical Due Diligence Automation System

End-to-end historical due diligence automation for land, title, and entity research with evidence tracking, chain-of-title analysis, conflict detection, and narrative reporting.

⸻

What this system does (plain English)

This system turns historical due diligence into a repeatable, defensible workflow.

It helps you:
	•	Organize complex land, title, and entity research into structured cases
	•	Track documents, entities, parcels, recordings, aliases, and evidence
	•	Detect chain-of-title gaps, vesting issues, lien lifecycle problems
	•	Preserve proof (documents, screenshots, captures)
	•	Produce a clear, evidence-backed story of what happened over time
	•	Export a report pack suitable for legal, financial, or archival use

It is designed for:
	•	Historical due diligence specialists
	•	Land/title researchers
	•	Investigators
	•	Heirs, trustees, and researchers reconstructing ownership history
	•	Anyone who needs an accurate narrative, not just raw documents

⸻

Core concepts (how the system thinks)

Concept	Meaning
Case	One investigation (property, family, corporation, time period)
Entity	Person, company, parcel, or address
Alias	Alternate name for an entity (identity resolution)
Document	Uploaded PDF/photo (deed, index page, screenshot, etc.)
Recording	Structured index row for a recorded instrument
Recording Party	Who appears on a recording (grantor, grantee, trustee…)
Recording Parcel	Which parcel(s) a recording applies to
Evidence	Page-level citation supporting extracted facts
Queue	What’s missing, conflicting, or risky
Story	Human-readable narrative built from verified data


⸻

What makes this different

✔ Accuracy over speed
✔ Explicit uncertainty (nothing is silently assumed)
✔ Evidence-first (every fact can be traced)
✔ Designed to reduce cognitive overload
✔ Built for real historical ambiguity (not “perfect data”)

⸻

How it works (high level)
	1.	Create a case
	2.	Add entities (people, parcels, companies)
	3.	Upload documents
	4.	Create or seed recordings (index rows)
	5.	Link parties and parcels to recordings
	6.	Resolve identities (aliases)
	7.	Check the queue (what’s missing or conflicting)
	8.	Generate the story
	9.	Export the report pack

⸻

Running the system (important)

This system runs as a FastAPI backend.
Your iPhone is the control panel, not the server.

Recommended environment

✅ GitHub Codespaces (works entirely from iPhone Safari)

⸻

Quick start (iPhone + GitHub Codespaces)

1) Create the repository
	•	GitHub → New repository
	•	Name: historical-dd-automation
	•	Add README
	•	Create repository

2) Add project files

Paste the provided project files into the repository using:
	•	Add file → Create new file
	•	Follow folder paths exactly (e.g. app/main.py)

3) Start a Codespace
	•	Repo → Code → Codespaces
	•	Create codespace on main

4) Run the server (in Codespaces terminal)

pip install -U pip
pip install -e .
rm -f app.db
uvicorn app.main:app --host 0.0.0.0 --port 8000

5) Open the control panel on your iPhone

Open the forwarded port, then go to:

/docs

This is your full UI.

⸻

Everyday workflow (no tech knowledge needed)

Step 1: Create a case

POST /api/v1/cases

Example:

{
  "title": "Imperial County Chain of Title",
  "description": "Starting at 662 Block 8 Lot 4",
  "risk_level": "high",
  "client_slug": "HOLLY",
  "site_slug": "SALTONSEA"
}

Save the returned case_id.

⸻

Step 2: Add entities

POST /api/v1/cases/{case_id}/entities/batch

[
  { "entity_type": "person", "display_name": "Jack S Stiles", "role": "primary_subject" },
  {
    "entity_type": "parcel",
    "display_name": "662 Block 8 Lot 4",
    "role": "target_parcel",
    "identifiers": { "county": "Imperial", "state": "CA" }
  }
]


⸻

Step 3: Upload documents

POST /api/v1/cases/{case_id}/documents

Upload:
	•	Deeds
	•	Recorder index pages
	•	Screenshots
	•	PDFs
	•	Photos

⸻

Step 4: Create recordings (index rows)

Fast method:

POST /api/v1/cases/{case_id}/recordings/seed-from-document/{document_id}

Accurate method:

POST /api/v1/cases/{case_id}/recordings

Fill in:
	•	doc_type
	•	date_recorded
	•	instrument_number
	•	grantor
	•	grantee

⸻

Step 5: Link parties and parcels

Attach meaning to the recording.

Parties

POST /api/v1/cases/{case_id}/recordings/{recording_id}/parties

Parcels

POST /api/v1/cases/{case_id}/recordings/{recording_id}/parcels


⸻

Step 6: Add aliases (identity accuracy)

POST /api/v1/cases/{case_id}/entities/{entity_id}/aliases

Use when names vary across documents.

⸻

Step 7: Check the queue (stress reducer)

GET /api/v1/cases/{case_id}/queue

This tells you:
	•	What’s missing
	•	What conflicts
	•	What needs resolution next

⸻

Step 8: Generate the story

GET /api/v1/cases/{case_id}/story

Returns a clear, chronological narrative with explicit uncertainty notes.

⸻

Step 9: Export report pack

POST /api/v1/cases/{case_id}/export/report-pack

Outputs:
	•	Story (Markdown)
	•	Case snapshot (JSON)
	•	Stored in the case report folder

⸻

Design philosophy
	•	Nothing is silently assumed
	•	Missing data is flagged, not hidden
	•	Conflicts are preserved, not overwritten
	•	The system tells the truth even when the truth is unclear

This protects you legally, ethically, and historically.

⸻

What’s intentionally NOT automated (yet)
	•	Legal conclusions
	•	Title insurance opinions
	•	Final ownership determinations

The system supports human judgment, it does not replace it.

⸻

Future upgrades (already designed for)
	•	OCR-based extraction
	•	Alembic migrations
	•	DOCX/PDF templated reports
	•	GIS parcel overlays
	•	Advanced entity resolution scoring
	•	Multi-parcel case logic

⸻

Bottom line

This is not a toy app.

It is a professional historical due diligence engine designed to:
	•	reduce stress
	•	increase accuracy
	•	preserve evidence
	•	and tell the most honest story possible
