# DATABASE

## Clubs

Stores information about registered clubs.

| Field         | Type      |
| ------------- | --------- |
| id            | UUID      |
| club_name     | String    |
| email         | String    |
| password_hash | String    |
| description   | String    |
| logo_url      | String    |
| created_at    | Timestamp |

---

## Events

Stores all campus events.

| Field       | Type      |
| ----------- | --------- |
| id          | UUID      |
| club_id     | UUID      |
| title       | String    |
| category    | String    |
| description | Text      |
| date        | Date      |
| time        | Time      |
| location    | String    |
| image_url   | String    |
| created_at  | Timestamp |

Relationship:

Event → belongs to one Club

---

## Announcements

Stores quick updates from clubs.

| Field      | Type      |
| ---------- | --------- |
| id         | UUID      |
| club_id    | UUID      |
| content    | Text      |
| created_at | Timestamp |

Relationship:

Announcement → belongs to one Club

---

## Categories

Predefined event categories.

| Field | Type   |
| ----- | ------ |
| id    | UUID   |
| name  | String |

Example Categories:

* Tech
* Trips and Adventures
* Other Events
* Club Events
* General Annoucements
* Sports and Marathons
* Recruitments


---

## Future Table: Interested Events

Used when students can mark interest in events.

| Field              | Type      |
| ------------------ | --------- |
| id                 | UUID      |
| event_id           | UUID      |
| student_identifier | String    |
| created_at         | Timestamp |

Relationship:

Student Interest → belongs to one Event

---

## Database Relationships

Club
│
├── Events
│
└── Announcements

Event
│
└── Interested Events (Future)

Category
│
└── Events
