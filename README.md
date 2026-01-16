📄 Document Upload with Metadata API

Django REST Framework + JWT Authentication

A robust backend system to upload documents with dynamic metadata, including support for typed metadata (string, date, choice, etc.), metadata choices, and JWT-secured APIs.

🚀 Features

Upload documents with metadata

Dynamic metadata keys (string, integer, date, choice, etc.)

Choice-based metadata support

JWT authentication (Bearer token)

PostgreSQL database

Clean RESTful API design

Production-ready serializers & viewsets

🛠 Tech Stack

| Layer       | Technology            |
| ----------- | --------------------- |
| Backend     | Django 3.2            |
| API         | Django REST Framework |
| Auth        | JWT (SimpleJWT)       |
| Database    | PostgreSQL            |
| File Upload | Django FileField      |

📂 Data Models Overview
🔹 UploadDocument

| Field                   | Type            |
| ----------------------- | --------------- |
| doc_id                  | CharField (PK)  |
| document                | File            |
| document_name           | String          |
| doc_type                | pdf, docx, xlsx |
| doc_created_by          | User            |
| created_at / updated_at | DateTime        |

🔹 MetadataKey

| Field           | Type                       |
| --------------- | -------------------------- |
| metadata_key    | Unique String              |
| metadata_type   | string, date, choice, etc. |
| metadata_choice | ManyToMany (optional)      |

🔹 MetadataChoice

| Field       | Type          |
| ----------- | ------------- |
| meta_choice | Unique String |

🔹 MetadataUpload

| Field             | Type       |
| ----------------- | ---------- |
| meta_key          | ForeignKey |
| meta_upload_doc   | ForeignKey |
| meta_upload_value | String     |

🔐 Authentication

This API uses JWT Bearer Authentication

Token Header Format

Authorization: Bearer <access_token>

📌 API Endpoints
🔑 Authentication

| Method | Endpoint              | Description   |
| ------ | --------------------- | ------------- |
| POST   | `/api/token/`         | Get JWT token |
| POST   | `/api/token/refresh/` | Refresh token |

Login Example

{
  "username": "admin",
  "password": "admin123"
}

📘 Metadata Choice APIs
➕ Create Metadata Choice

POST /api/metadata-choices/

{
  "meta_choice": "Permanent"
}

📄 List Metadata Choices

GET /api/metadata-choices/

[
  {
    "id": 1,
    "meta_choice": "Permanent"
  },
  {
    "id": 2,
    "meta_choice": "Contract"
  }
]

🏷 Metadata Key APIs
➕ Create Metadata Key (Choice Type)

POST /api/metadata-keys/

{
  "metadata_key": "Employee Type",
  "metadata_description": "Type of employee",
  "metadata_type": "choice",
  "metadata_choice": [1, 2]
}

➕ Create Metadata Key (Date Type)

{
  "metadata_key": "Joining Date",
  "metadata_description": "Employee joining date",
  "metadata_type": "date"
}

📄 List Metadata Keys

GET /api/metadata-keys/

[
  {
    "key_id": 1,
    "metadata_key": "Employee Type",
    "metadata_description": "Type of employee",
    "metadata_type": "choice",
    "metadata_choice": [
      { "id": 1, "meta_choice": "Permanent" },
      { "id": 2, "meta_choice": "Contract" }
    ]
  }
]

📤 Document Upload with Metadata
➕ Upload Document

POST /api/documents/
Content-Type: multipart/form-data

| Key           | Value                 |
| ------------- | --------------------- |
| doc_id        | DOC-1001              |
| document_name | Employee Offer Letter |
| doc_type      | pdf                   |
| document      | *(file)*              |
| metadata      | JSON string           |

📦 Metadata JSON (Postman)

[
  {
    "key": "Employee Name",
    "value": "Rahul Sharma"
  },
  {
    "key": "Joining Date",
    "value": "2026-01-10"
  },
  {
    "key": "Employee Type",
    "value": "Permanent"
  }
]

📌 Important:

metadata must be sent as a STRING

Metadata keys must exist beforehand

📄 Get Uploaded Document with Metadata
📥 Get Document Details

GET /api/documents/DOC-1001/

{
  "doc_id": "DOC-1001",
  "document": "/media/uploads/offer_letter.pdf",
  "document_name": "Employee Offer Letter",
  "doc_type": "pdf",
  "status": "ac",
  "locked": false,
  "doc_created_at": "2026-01-15T10:00:00Z",
  "doc_updated_on": "2026-01-15T10:00:00Z",
  "metadata": [
    {
      "meta_key": "Employee Name",
      "meta_upload_value": "Rahul Sharma"
    },
    {
      "meta_key": "Joining Date",
      "meta_upload_value": "2026-01-10"
    },
    {
      "meta_key": "Employee Type",
      "meta_upload_value": "Permanent"
    }
  ]
}

🧪 Postman Tips

Use Body → form-data

For metadata, paste JSON and select Text

For document, select File

Always include Authorization → Bearer Token

🧩 Metadata Type Rules

| Type    | Example Value |
| ------- | ------------- |
| string  | Rahul Sharma  |
| integer | 1200000       |
| date    | 2026-01-10    |
| bool    | true          |
| choice  | Permanent     |

📦 Installation (Quick Start)

git clone <repo-url>

cd upload_document_with_metadata

python -m venv apivenv

source apivenv/bin/activate

pip install -r requirements.txt

python manage.py migrate

python manage.py runserver


👨‍💻 Author

Dattatraya Walunj

Backend Engineer – Django & DRF



