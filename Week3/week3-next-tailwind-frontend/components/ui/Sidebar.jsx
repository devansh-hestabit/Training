"use client";

export default function Sidebar({ isOpen }) {
  return (
    <aside
      className={`bg-gray-900 text-gray-300 min-h-[calc(100vh-4rem)]
        transition-all duration-300 ease-in-out
        ${isOpen ? "w-64" : "w-0 overflow-hidden"}
      `}
    >
      <nav className="px-4 py-6 space-y-6">
        {/* CORE */}
        <div>
          <p className="text-xs uppercase text-gray-500 mb-3">Core</p>

          <div className="flex items-center gap-3 text-white px-3 py-2 rounded bg-gray-800">
            <span>📊</span>
            <span>Dashboard</span>
          </div>
        </div>

        {/* INTERFACE */}
        <div>
          <p className="text-xs uppercase text-gray-500 mb-3">Interface</p>

          <div className="space-y-2">
            <div className="flex items-center justify-between px-3 py-2 rounded hover:bg-gray-800 cursor-pointer">
              <span>Layouts</span>
              <span>›</span>
            </div>

            <div className="flex items-center justify-between px-3 py-2 rounded hover:bg-gray-800 cursor-pointer">
              <span>Pages</span>
              <span>›</span>
            </div>
          </div>
        </div>

        {/* ADDONS */}
        <div>
          <p className="text-xs uppercase text-gray-500 mb-3">Addons</p>

          <div className="space-y-2">
            <div className="px-3 py-2 rounded hover:bg-gray-800 cursor-pointer">
              Charts
            </div>

            <div className="px-3 py-2 rounded hover:bg-gray-800 cursor-pointer">
              Tables
            </div>
          </div>
        </div>
      </nav>
    </aside>
  );
}
