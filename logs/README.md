# Logs Directory

This directory contains logs from automated processes and integration checks.

## Structure

- `connection-checks/` - Logs from API connection validation tests
- `*.log` - General application logs

## Note

All log files are excluded from version control via `.gitignore`. Only this README and directory structure documentation should be committed.

## Log Retention

- Development logs: Keep for 30 days
- Connection check logs: Archive quarterly
- Error logs: Review immediately, keep for 90 days

## Security

Ensure logs do not contain:
- API keys or tokens
- Personal identifiable information (PII)
- Raw API responses with sensitive data
