# Add Source Shortcut

Use this Shortcut on iOS or macOS to quickly add a new source to your
research workspace from the Share Sheet.  The Shortcut accepts a URL or file
(e.g. PDF) as input, prompts you for a title and notes, and sends the data to
your assistant service.

## Steps

1. **Get URL or Document:**
   - In the Shortcut editor, add a **Get Details of Safari Web Page** or
     **Get File Details** action.  Use **Get Link from Input** if the input
     is a URL.
2. **Ask for Title:**
   - Add an **Ask for Input** action and set the prompt to "Source title".
     Assign the result to a variable, e.g., `Title`.
3. **Ask for Notes (optional):**
   - Add another **Ask for Input** action with the prompt "Notes (optional)" and
     allow multiple lines.  Assign to `Notes`.
4. **Build JSON:**
   - Add a **Dictionary** action and create keys `title`, `url`, and `notes`.
     For `title`, set the value to the `Title` variable; for `url`, set it to
     the input link; for `notes`, set it to the `Notes` variable.
   - Then add a **Get Dictionary Value** action with **Get Contents of
     Dictionary** set to JSON.  This yields a JSON representation of the
     dictionary.
5. **Send to API:**
   - Add a **URL** action.  Set the URL to your assistant endpoint, e.g.,
     `https://your-server.example.com/add_source`.
   - Add a **Get Contents of URL** action.  Set the method to **POST** and
     provide the JSON as the request body.  Set the `Content‑Type` header to
     `application/json`.
6. **Show Result:**
   - Add a **Show Result** action to display the response from the server.

Optionally, you can add error handling with `If` actions to check for
connection failures or empty responses.
