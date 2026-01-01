# Bill Sweep Shortcut

This Shortcut checks for newly introduced or updated legislation across
jurisdictions by calling your assistant’s bill sweep endpoint.  It can be
scheduled to run automatically (e.g., daily at 8 AM) or invoked manually.

## Steps

1. **Ask for Date (optional):**
   - Add an **Ask for Input** action with the prompt "Since (YYYY‑MM‑DD)".  If
     left blank, the sweep will include all bills.  Save the result as
     `Since`.
1. **Choose Jurisdictions:**
   - Add a **Choose from List** action with the prompt "Select jurisdictions" and
     provide options such as "NYC", "NY State", "US Federal", "International".
     Allow multiple selections and save to `Jurisdictions`.  If the user cancels,
     you can default to all jurisdictions.
1. **Build JSON:**
   - Add a **Dictionary** action with keys `since` and `jurisdictions`.
   - For `since`, assign the `Since` variable.  For `jurisdictions`, assign the
     `Jurisdictions` variable.
   - Convert the dictionary to JSON using **Get Dictionary Value** set to JSON.
1. **Send to API:**
   - Add a **URL** action pointing to
     `https://your-server.example.com/sweep_bills`.
   - Add a **Get Contents of URL** action.  Set method to **POST**, body to
     the JSON and the header `Content‑Type` to `application/json`.
1. **Show Results:**
   - Use a **Show Result** or **Quick Look** action to display the returned
     summary of bills.  You might also choose to save the results as a Markdown
     file in your notes directory.

To run this sweep on a schedule, wrap the Shortcut in an automation in the
Shortcuts app (e.g., "Daily at 8 AM").
