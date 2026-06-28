# USER FLOW

## Student Flow

Open App
↓
Home page
↓
View Event Feed
↓
Browse Events
↓
Filter by Category / Date
↓
Open Event Details
↓
View Location, Time, Description
↓
Mark Interested (Future Feature)
↓
Attend Event

---

## Club Flow

Open App
↓
Home Page
↓
Club Login
↓
Access Club Portal
↓
Create Event
↓
Enter Title
↓
Select Category
↓
Add Date & Time
↓
Add Location
↓
Upload Poster
↓
Publish Event
↓
Event Appears In Student Feed

---

## Announcement Flow

Club Login
↓
Create Announcement
↓
Write Message
↓
Publish
↓
Appears In Live Announcements Section

# FEATURES

## Student Features

* View campus events
* Search events
* Filter by category
* Filter by date
* View event details
* View announcements
* Browse events without registration
* Notification about every new post

---

## Club Features

* Club login
* Create events
* Edit events
* Delete events
* Upload event posters
* Post announcements

---

## Event Information

Each event contains:

* Title
* Category
* Date
* Time
* Location
* Description
* Poster Image

---

## Future Features

* Interested button
* Notifications to specific accounts
* Event reminders
* Club analytics
* Event bookmarks
* Personalized recommendations

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
