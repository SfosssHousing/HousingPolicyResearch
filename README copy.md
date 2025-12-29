# sfosss

This repository serves as a sandbox for experiments.

The `.gitignore` file prevents temporary or virtual environment files from being tracked.

# ChatGPT Notion Sync (sample implementation)

This repository provides a minimal, test driven implementation of the building
blocks that are required to synchronise a Notion database with summaries
produced by ChatGPT.  The focus is on demonstrating how configuration is
handled and how the sync routine interacts with a Notion client.

## Configuration

All configuration is provided through environment variables and exposed via the
`Settings` dataclass.

| Variable                       | Description                                                         |
| ------------------------------ | ------------------------------------------------------------------- |
| `NOTION_TOKEN`                 | Secret token used to authenticate against the Notion API.           |
| `NOTION_DATABASE_ID`           | Identifier of the database that holds the source pages.             |
| `NOTION_SUMMARY_PROPERTY_NAME` | Name of the rich-text property that stores the generated summaries. |
| `NOTION_CHANGELOG_PAGE_ID`     | Optional identifier of the page that receives change log updates.   |

## Job application automation

The repository now includes `chatgpt_notion_sync.job_app_manager`, a Reminders-
centric CLI built for macOS 26.1 and iOS 26.1 devices.  It provisions a tidy
`JobApplications` workspace inside both the iCloud and GitHub document trees,
creates `Applications/`, `Reference/`, and `Reminders/` subfolders, and exports
a Reminders.app friendly CSV template focused on deadline awareness and
incomplete task tracking.  The automation is intentionally isolated to the
`JobApplications` folder—there is no Notion dependency or integration path, so
other repositories remain untouched.  Provide the job data as JSON and, if
desired, a profile JSON containing your skills/interests for match scoring:

```bash
python -m chatgpt_notion_sync.job_app_manager \
  --job-data data/jobs.json \
  --profile data/profile.json
```

The generated file `job_application_reminders.csv` is stored in the `Reminders/`
subdirectory for both locations so the workspace stays decluttered.  Import the
rows into Reminders or Numbers to highlight overdue or incomplete deliverables
and keep application files organised locally.

## Chat and project task tracker

The repository also ships `chatgpt_notion_sync.task_list`, a lightweight utility
for assembling a CSV task tracker from ChatGPT chat exports.  Tasks are grouped
by project, subject, or unknown context; chats within a project are ordered by
their last-updated date and tasks within each chat are prioritised.  The output
CSV lives under the default `~/ChatGPT/Projects/Tasks` directory so it remains
accessible whether you open ChatGPT on iOS, macOS, or the web.  Interactive
checkbox glyphs (`☐`/`☑`) are included to keep progress visible at a glance.

```bash
python -m chatgpt_notion_sync.task_list \
  --chat-export data/chat_tasks.json \
  --output-dir ~/ChatGPT/Projects/Tasks \
  --filename chat_tasks.csv
```

Each row captures the category (`project`, `unassigned`, or `unknown`), project
or subject label, chat title, last update timestamp, task description, priority,
and a checkbox cell for tracking completion.  Provide your own JSON export with
per-chat task lists to generate an updated `<Tasks>` table whenever you open
ChatGPT.

## Running the tests

```bash
pytest
```
