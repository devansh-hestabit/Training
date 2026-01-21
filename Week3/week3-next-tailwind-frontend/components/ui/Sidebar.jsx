"use client";

import Link from "next/link";

export default function Sidebar({ isOpen }) {
  return (
    <aside
      className={`
        fixed sm:static top-16 left-0 z-40
        bg-gray-900 text-gray-300
        h-[calc(100vh-4rem)]
        transition-all duration-300 ease-in-out
        ${isOpen ? "w-64" : "w-0 overflow-hidden"}
      `}
    >
      <nav className="px-4 py-6 space-y-6 w-64">
        {/* CORE */}
        <div>
          <p className="text-xs uppercase text-gray-500 mb-3">Core</p>

          <Link
            href="/dashboard"
            className="flex items-center gap-3 text-white px-3 py-2 rounded hover:bg-gray-800"
          >
            📊 Dashboard
          </Link>
        </div>

        {/* INTERFACE */}
        <div>
          <p className="text-xs uppercase text-gray-500 mb-3">Interface</p>

          <div className="space-y-2">
            <div className="flex justify-between px-3 py-2 rounded hover:bg-gray-800 cursor-pointer">
              Layouts <span>›</span>
            </div>

            <div className="flex justify-between px-3 py-2 rounded hover:bg-gray-800 cursor-pointer">
              Pages <span>›</span>
            </div>
          </div>
        </div>

        {/* ADDONS */}
        <div>
          <p className="text-xs uppercase text-gray-500 mb-3">Addons</p>

          <div className="space-y-2">
            <Link
              href="/dashboard/profile"
              className="block px-3 py-2 rounded hover:bg-gray-800"
            >
              Profile
            </Link>

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
