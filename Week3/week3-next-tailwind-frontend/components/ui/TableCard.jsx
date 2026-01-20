export default function TableCard({ title, children }) {
  return (
    <div className="bg-white border border-gray-200 rounded shadow-sm">
      {/* Header */}
      <div className="px-4 py-3 border-b border-gray-200 font-semibold text-gray-800">
        {title}
      </div>

      {/* Body */}
      <div className="p-4 overflow-x-auto">
        {children}
      </div>
    </div>
  );
}
