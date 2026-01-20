"use client";

export default function ChartCard({ title, children }) {
  return (
    <div className="bg-white border border-gray-200 rounded shadow-sm">
      <div className="px-4 py-3 border-b border-gray-200 font-semibold text-gray-800">
        {title}
      </div>
      <div className="p-4 h-64">
        {children}
      </div>
    </div>
  );
}
