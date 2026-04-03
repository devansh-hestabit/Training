import Card from "@/components/ui/Card";
import ChartCard from "@/components/ui/ChartCard";
import AreaChart from "@/components/charts/AreaChart";
import BarChart from "@/components/charts/BarChart";
import TableCard from "@/components/ui/TableCard";
import DataTable from "@/components/tables/DataTable";

export const metadata = {
  title: "Dashboard | HestaCart",
  description:
    "HestaCart dashboard provides real-time insights, analytics, and tools to manage your business efficiently.",
  robots: {
    index: false,
    follow: false,
  },
};

export default function DashboardPage() {
  return (
    <div className="space-y-6 sm:space-y-8">
      {/* Page Title */}
      <div>
        <h1 className="text-2xl sm:text-3xl font-semibold text-black">
          Dashboard
        </h1>

        <div className="bg-gray-200 px-3 py-1.5 sm:px-4 sm:py-2 rounded mt-2 text-sm sm:text-base text-black w-fit">
          Dashboard
        </div>
      </div>

      {/* Cards */}
      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4 sm:gap-6">
        <Card title="Primary Card" color="bg-blue-600">
          View Details →
        </Card>

        <Card title="Warning Card" color="bg-yellow-500">
          View Details →
        </Card>

        <Card title="Success Card" color="bg-green-600">
          View Details →
        </Card>

        <Card title="Danger Card" color="bg-pink-700">
          View Details →
        </Card>
      </div>

      {/* Charts Section */}
      <div className="grid grid-cols-1 lg:grid-cols-2 gap-4 sm:gap-6">
        <ChartCard title="Area Chart Example">
          <AreaChart />
        </ChartCard>

        <ChartCard title="Bar Chart Example">
          <BarChart />
        </ChartCard>
      </div>

      {/* Table Section */}
      <TableCard title="DataTable Example">
        <DataTable />
      </TableCard>
    </div>
  );
}
