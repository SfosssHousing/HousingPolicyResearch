# Draft Section Shortcut

This Shortcut generates a draft for a specific section of your policy brief by
sending a prompt to the assistant.  Invoke it from the Shortcuts app or via
the Share Sheet.

## Steps

1. **Ask for Section Name:**
   - Add an **Ask for Input** action and set the prompt to "Section name"
     (e.g., "Executive Summary", "Policy Options").  Save the result in
     a variable, e.g., `Section`.
1. **Ask for Prompt:**
   - Add another **Ask for Input** action with the prompt "Describe what this
     section should cover" and set it to allow multiple lines.  Save as
     `Prompt`.
1. **Build JSON:**
   - Add a **Dictionary** action with keys `section` and `prompt`.  Set
     their values to the `Section` and `Prompt` variables, respectively.
   - Convert the dictionary to JSON using **Get Dictionary Value** set to
     JSON.
1. **Send to API:**
   - Add a **URL** action with the endpoint URL
     `https://your-server.example.com/generate_section`.
   - Add a **Get Contents of URL** action.  Set the method to **POST** and
     the request body to the JSON.  Set the header `Content‑Type` to
     `application/json`.
1. **Display Draft:**
   - Add a **Quick Look** or **Show Result** action to display the returned
     draft text.  You can then copy it into your Quarto file.

You can extend this Shortcut to save the draft into a file or append it to
an existing document in your iCloud drive using the **Save File** action.
