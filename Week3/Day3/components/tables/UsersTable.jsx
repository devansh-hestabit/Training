import TableCard from "@/components/ui/TableCard";
import InputNav from "@/components/ui/InputNav";
import Badge from "@/components/ui/Badge";

const USERS = [
  { name: "User", email: "user@example.com", role: "User", created: "18/10/2024 05:27", updated: "18/10/2024 05:27" },
  { name: "Dr. Ray Stoltenberg", email: "rosalinda42@example.com", role: "User", created: "18/10/2024 05:27", updated: "18/10/2024 05:27" },
  { name: "Mrs. Mertie Murray MD", email: "ernser.susanna@example.net", role: "Admin", created: "18/10/2024 05:27", updated: "18/10/2024 05:27" },
  { name: "Gilbert Rice", email: "willard.walter@example.org", role: "User", created: "18/10/2024 05:27", updated: "18/10/2024 05:27" },
  { name: "Sydnie Rau", email: "doug.padberg@example.org", role: "User", created: "18/10/2024 05:27", updated: "18/10/2024 05:27" },
  { name: "Mr. Arvid Veum DDS", email: "schinner.meaghan@example.org", role: "User", created: "18/10/2024 05:27", updated: "18/10/2024 05:27" },
  { name: "Jayme Beier DDS", email: "orn.ahmed@example.com", role: "Admin", created: "18/10/2024 05:27", updated: "18/10/2024 05:27" },
  { name: "Uriah Swaniawski", email: "wilburn.champlin@example.org", role: "User", created: "18/10/2024 05:27", updated: "18/10/2024 05:27" },
  { name: "Rosanna Heaney", email: "boconner@example.com", role: "User", created: "18/10/2024 05:27", updated: "18/10/2024 05:27" },
  { name: "Adan Reichel", email: "mya.labadie@example.com", role: "User", created: "18/10/2024 05:27", updated: "18/10/2024 05:27" },
];

export default function UsersTable() {
  return (
    <TableCard>
      {/* Header */}
      <div className="flex items-center justify-between mb-4">
        <h2 className="text-lg font-semibold">User List</h2>
        <div className="w-64">
          <InputNav placeholder="Search" />
        </div>
      </div>

      {/* Table */}
      <div className="overflow-x-auto">
        <table className="w-full text-sm">
          <thead className="border-b text-gray-600">
            <tr>
              <th className="py-3 text-left">Name ↓</th>
              <th className="text-left">Email ↓</th>
              <th className="text-left">Role ↓</th>
              <th className="text-left">Created at</th>
              <th className="text-left">Updated at</th>
              <th />
            </tr>
          </thead>

          <tbody>
            {USERS.map((user, index) => (
              <tr key={index} className="border-b last:border-none hover:bg-gray-50">
                <td className="py-3">{user.name}</td>
                <td>{user.email}</td>
                <td>
                  <Badge text={user.role} />
                </td>
                <td>{user.created}</td>
                <td>{user.updated}</td>
                <td className="text-right text-purple-600 cursor-pointer">👤</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>

      {/* Footer */}
      <div className="flex items-center justify-between mt-4 text-sm text-gray-500">
        <span>Showing 1 to 10 of 10 results</span>

        <div className="flex items-center gap-3">
          <span>Per page</span>
          <select className="border rounded px-2 py-1">
            <option>10</option>
          </select>

          <div className="flex items-center gap-1">
            <button className="px-2 py-1 border rounded text-blue-600">1</button>
            <button className="px-2 py-1 border rounded">→</button>
          </div>
        </div>
      </div>
    </TableCard>
  );
}
