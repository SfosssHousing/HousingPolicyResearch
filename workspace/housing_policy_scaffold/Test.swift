import Foundation
import Testing

@Suite("Workspace scaffold checks")
struct WorkspaceScaffoldTests {

    @Test("Directories exist")
    func directoriesExist() throws {
        let fm = FileManager.default
        let required = [
            "00_admin",
            "00_admin/templates",
            "10_sources",
            "20_notes",
            "30_drafts",
            "40_outputs",
            "50_data",
            "60_logs",
            "zotero",
            "raycast-extension",
            "shortcuts"
        ]
        for path in required {
            let exists = fm.fileExists(atPath: path)
            #expect(exists, "Missing required path: \(path)")
        }
    }

    @Test("Templates present")
    func templatesPresent() throws {
        let fm = FileManager.default
        let policyBrief = "00_admin/templates/policy_brief_apa7.qmd"
        let billTemplate = "00_admin/templates/nyc_bill_template.md"
        #expect(fm.fileExists(atPath: policyBrief))
        #expect(fm.fileExists(atPath: billTemplate))
    }

    @Test("Settings file present and non-empty")
    func settingsPresent() throws {
        let url = URL(fileURLWithPath: "00_admin/settings.yaml")
        let data = try Data(contentsOf: url)
        #expect(data.count > 0)
    }
}
