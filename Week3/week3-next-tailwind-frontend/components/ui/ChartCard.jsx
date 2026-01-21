"use client";

export default function ChartCard({ title, children }) {
  return (
    <div className="bg-white border border-gray-200 rounded-lg shadow-sm">
      <div className="px-4 py-2.5 sm:px-5 sm:py-3
                      border-b border-gray-200
                      font-semibold text-sm sm:text-base text-gray-800">
        {title}
      </div>

      <div className="p-3 sm:p-4 h-48 sm:h-64">
        {children}
      </div>
    </div>
  );
}
