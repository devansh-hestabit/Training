"use client";

import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Filler,
  Tooltip,
} from "chart.js";
import { Line } from "react-chartjs-2";

ChartJS.register(
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Filler,
  Tooltip
);

export default function AreaChart() {
  const data = {
    labels: [
      "Mar 1",
      "Mar 3",
      "Mar 5",
      "Mar 7",
      "Mar 9",
      "Mar 11",
      "Mar 13",
    ],
    datasets: [
      {
        label: "Revenue",
        data: [10000, 30000, 18000, 32000, 26000, 33000, 39000],
        fill: true,
        backgroundColor: "rgba(54, 162, 235, 0.2)",
        borderColor: "rgba(54, 162, 235, 1)",
        tension: 0.4,
        pointRadius: 4,
      },
    ],
  };

  const options = {
    responsive: true,
    maintainAspectRatio: false,
    plugins: {
      legend: { display: false },
    },
  };

  return <Line data={data} options={options} />;
}
