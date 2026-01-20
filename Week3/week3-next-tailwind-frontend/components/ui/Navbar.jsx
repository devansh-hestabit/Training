"use client";

import Input from "@/components/ui/InputNav";
import Link from "next/link";

export default function Navbar({ isOpen, onToggleSidebar }) {
  return (
    <header className="h-16 bg-gray-800 text-white flex items-center justify-between px-6">
      {/* Left side */}
      <div className="flex items-center gap-4">
        <span className="text-lg font-semibold">HestaCart</span>

        <button
          onClick={onToggleSidebar}
          className={`
            text-xl cursor-pointer
            transition-transform duration-300
            ${isOpen ? "rotate-90" : "rotate-0"}
          `}
        >
          ☰
        </button>
      </div>

      {/* Right side */}
      <div className="flex items-center gap-4">
        {/* Search */}
        <div className="relative">
          <span className="absolute left-3 top-1/2 -translate-y-1/2 text-gray-500">
            🔍
          </span>
          <Input placeholder="Search for..." />
        </div>

        {/* Icons */}
        <span className="cursor-pointer">🔔</span>
        <Link
          href="/dashboard/profile"
          className="cursor-pointer hover:opacity-80"
        >
          👤
        </Link>

        {/* Back to Home */}
        <Link
          href="/"
          className="ml-2 px-3 py-1 rounded text-sm bg-gray-700 hover:bg-gray-600 transition"
        >
          Home
        </Link>
      </div>
    </header>
  );
}
