"use client";

import Link from "next/link";

export default function PublicNavbar() {
  return (
    <header className="h-16 min-h-16 bg-gray-800 text-white flex items-center justify-between px-4 sm:px-6">
      {/* Brand */}
      <span className="text-base sm:text-lg font-semibold whitespace-nowrap">
        HestaCart
      </span>

      {/* Nav */}
      <nav className="flex items-center gap-4 sm:gap-8 text-sm font-medium">
        <Link href="/" className="hover:text-gray-300">
          Home
        </Link>

        <Link href="/about" className="hover:text-gray-300">
          About
        </Link>

        <Link href="/dashboard" className="hover:text-gray-300">
          Dashboard
        </Link>
      </nav>
    </header>
  );
}
