#!/usr/bin/env python3
"""
Connection validation script for Housing Policy Research integrations.

Tests connectivity to OpenAI, Notion, and Zotero APIs using environment variables.
Logs results to logs/connection-checks/ with timestamps.
"""
import os
import sys
from datetime import datetime
from pathlib import Path
import json

# Try to import required packages
try:
    import requests
    from dotenv import load_dotenv
except ImportError:
    print("Missing dependencies. Install with: pip install requests python-dotenv")
    sys.exit(1)

# Load environment variables
load_dotenv()


def check_openai():
    """Test OpenAI API connection."""
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        return {"status": "skipped", "reason": "OPENAI_API_KEY not set"}

    try:
        # Use the new OpenAI client if available
        from openai import OpenAI

        client = OpenAI(api_key=api_key)
        # Simple test - list models
        models = client.models.list()
        return {
            "status": "success",
            "message": f"Connected successfully, {len(models.data)} models available",
        }
    except ImportError:
        # Fall back to direct API call
        try:
            headers = {"Authorization": f"Bearer {api_key}"}
            response = requests.get(
                "https://api.openai.com/v1/models", headers=headers, timeout=10
            )
            if response.status_code == 200:
                data = response.json()
                return {
                    "status": "success",
                    "message": f"Connected successfully, {len(data.get('data', []))} models available",
                }
            else:
                return {
                    "status": "error",
                    "message": f"HTTP {response.status_code}: {response.text[:100]}",
                }
        except Exception as e:
            return {"status": "error", "message": str(e)}
    except Exception as e:
        return {"status": "error", "message": str(e)}


def check_notion():
    """Test Notion API connection."""
    api_key = os.getenv("NOTION_API_KEY")
    if not api_key:
        return {"status": "skipped", "reason": "NOTION_API_KEY not set"}

    try:
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Notion-Version": "2022-06-28",
            "Content-Type": "application/json",
        }
        # Try to search (requires integration to be connected to at least one page)
        response = requests.post(
            "https://api.notion.com/v1/search",
            headers=headers,
            json={"page_size": 1},
            timeout=10,
        )
        if response.status_code == 200:
            data = response.json()
            return {
                "status": "success",
                "message": f"Connected successfully, {len(data.get('results', []))} accessible pages found",
            }
        else:
            return {
                "status": "error",
                "message": f"HTTP {response.status_code}: {response.text[:100]}",
            }
    except Exception as e:
        return {"status": "error", "message": str(e)}


def check_zotero():
    """Test Zotero API connection."""
    api_key = os.getenv("ZOTERO_API_KEY")
    library_id = os.getenv("ZOTERO_LIBRARY_ID")
    library_type = os.getenv("ZOTERO_LIBRARY_TYPE", "group")

    if not api_key or not library_id:
        return {
            "status": "skipped",
            "reason": "ZOTERO_API_KEY or ZOTERO_LIBRARY_ID not set",
        }

    try:
        # Test connection by fetching library info
        url = f"https://api.zotero.org/{library_type}s/{library_id}/collections"
        headers = {"Zotero-API-Key": api_key}
        response = requests.get(url, headers=headers, params={"limit": 1}, timeout=10)

        if response.status_code == 200:
            return {"status": "success", "message": "Connected successfully"}
        else:
            return {
                "status": "error",
                "message": f"HTTP {response.status_code}: {response.text[:100]}",
            }
    except Exception as e:
        return {"status": "error", "message": str(e)}


def main():
    """Run all connection checks and log results."""
    print("=" * 70)
    print("Housing Policy Research - Connection Validation")
    print("=" * 70)
    print()

    # Run checks
    checks = {
        "openai": check_openai(),
        "notion": check_notion(),
        "zotero": check_zotero(),
    }

    # Display results
    for service, result in checks.items():
        status_icon = {
            "success": "✓",
            "error": "✗",
            "skipped": "-",
        }.get(result["status"], "?")

        print(f"{status_icon} {service.upper()}: {result['status'].upper()}")
        if "message" in result:
            print(f"  → {result['message']}")
        if "reason" in result:
            print(f"  → {result['reason']}")
        print()

    # Save results to log file
    log_dir = Path("logs/connection-checks")
    log_dir.mkdir(parents=True, exist_ok=True)

    now = datetime.now()
    timestamp = now.isoformat()
    log_file = log_dir / f"check_{now.strftime('%Y%m%d_%H%M%S')}.json"

    log_data = {"timestamp": timestamp, "checks": checks}

    with open(log_file, "w") as f:
        json.dump(log_data, f, indent=2)

    print(f"Results logged to: {log_file}")
    print()

    # Exit with error if any check failed
    if any(check["status"] == "error" for check in checks.values()):
        print("⚠ Some checks failed. Review the errors above.")
        sys.exit(1)
    elif all(check["status"] == "skipped" for check in checks.values()):
        print("⚠ All checks were skipped. Configure .env with API keys.")
        sys.exit(0)
    else:
        print("✓ All configured integrations are working!")
        sys.exit(0)


if __name__ == "__main__":
    main()
