export default function TableCard({ title, children }) {
  return (
    <div className="bg-white border border-gray-200 rounded-lg shadow-sm w-full">
      {/* Header */}
      <div
        className="px-3 py-2.5 sm:px-4 sm:py-3
                   border-b border-gray-200
                   font-semibold text-sm sm:text-base
                   text-gray-800"
      >
        {title}
      </div>

      {/* Body */}
      <div
        className="p-3 sm:p-4
                   overflow-x-auto
                   max-w-full"
      >
        {children}
      </div>
    </div>
  );
}
