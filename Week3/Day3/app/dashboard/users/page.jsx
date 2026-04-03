import UsersTable from "@/components/tables/UsersTable";

export default function UsersPage() {
  return (
    <div className="space-y-6 text-gray-900">
      <h1 className="text-2xl font-semibold text-gray">Users</h1>
      <UsersTable />
    </div>
  );
}
