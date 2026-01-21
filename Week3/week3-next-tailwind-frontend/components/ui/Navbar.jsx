"use client";

import Input from "@/components/ui/InputNav";
import Link from "next/link";

export default function Navbar({ isOpen, onToggleSidebar }) {
  return (
    <header className="h-16 min-h-16 bg-gray-800 text-white flex items-center justify-between px-4 sm:px-6">
      {/* Left */}
      <div className="flex items-center gap-3 shrink-0">
        <span className="text-base sm:text-lg font-semibold whitespace-nowrap">
          HestaCart
        </span>

        <button
          onClick={onToggleSidebar}
          className={`text-xl transition-transform duration-300
            ${isOpen ? "rotate-90" : "rotate-0"}
          `}
        >
          ☰
        </button>
      </div>

      {/* Right */}
      <div className="flex items-center gap-3 sm:gap-4 shrink-0">
        {/* Search */}
        <div className="relative hidden sm:block">
          <span className="absolute left-3 top-1/2 -translate-y-1/2 text-gray-500">
            🔍
          </span>
          <Input placeholder="Search..." />
        </div>

        <span className="cursor-pointer">🔔</span>

        <Link
          href="/dashboard/profile"
          className="hover:opacity-80"
        >
          👤
        </Link>

        <Link
          href="/"
          className="px-3 py-1 rounded text-sm bg-gray-700 hover:bg-gray-600 transition"
        >
          Home
        </Link>
      </div>
    </header>
  );
}
