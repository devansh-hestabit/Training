import Card from "@/components/ui/Card";
import ChartCard from "@/components/ui/ChartCard";
import AreaChart from "@/components/charts/AreaChart";
import BarChart from "@/components/charts/BarChart";
import TableCard from "@/components/ui/TableCard";
import DataTable from "@/components/tables/DataTable";

export default function DashboardPage() {
  return (
    <div className="space-y-6">
      {/* Page Title */}
      <div>
        <h1 className="text-3xl font-semibold text-black">Dashboard</h1>
        <div className="bg-gray-200 px-4 py-2 rounded mt-2 text-black">
          Dashboard
        </div>
      </div>

      {/* Cards */}
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
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
      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
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
